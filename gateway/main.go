package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"net"
	"os"

	pb "gateway/proto"

	"google.golang.org/grpc"

	"database/sql"

	_ "github.com/lib/pq"
)

const (
	port = ":9090"
)

// server is used to implement helloworld.GreeterServer.
type server struct {
	db *sql.DB
	pb.UnimplementedGatewayServer
}

func (s *server) resolveToken(token string) (string, string, error) {
	var id string
	var tz string

	err := s.db.QueryRow("select id, tz from player where token = $1", token).Scan(&id, &tz)
	if err != nil {
		if err == sql.ErrNoRows {
			return "", "", errors.New("invalid token")
		}
		log.Fatal(err)
	}

	return id, tz, nil
}

func (s *server) resolveEvent(event string) (int, error) {
	var id int
	err := s.db.QueryRow("select id from events where name = $1", event).Scan(&id)
	if err != nil {
		if err == sql.ErrNoRows {
			return 0, errors.New("invalid event")
		}
		log.Fatal(err)
	}
	return id, nil
}

func (s *server) GetPlayer(ctx context.Context, in *pb.Login) (*pb.Player, error) {
	id, tz, err := s.resolveToken(in.Token)
	if err != nil {
		return nil, err
	}
	if tz != in.Tz {
		return nil, errors.New("tz mismatch - use discord")
	}
	_, err = s.resolveEvent(in.Event)
	if err != nil {
		return nil, err
	}
	log.Printf("GetPlayer: %s, %s", id, in.Event)
	return &pb.Player{Name: id, Tz: tz}, nil
}

func (s *server) GetTimeranges(ctx context.Context, in *pb.Login) (*pb.Timeranges, error) {

	name, _, err := s.resolveToken(in.Token)
	if err != nil {
		return nil, err
	}

	rows, err := s.db.Query("SELECT timerange.id, timerange.start, timerange.end, timerange.tz FROM events JOIN timerange ON (events.id = timerange.event_id) WHERE events.name = $1 AND timerange.player_id = $2", in.Event, name)
	if err != nil {
		log.Fatal(err)
	}

	var (
		id         int32
		start      int32
		end        int32
		tz         string
		timeranges []*pb.Timerange
	)

	defer rows.Close()
	for rows.Next() {
		err := rows.Scan(&id, &start, &end, &tz)
		if err != nil {
			log.Fatal(err)
		}
		timeranges = append(timeranges, &pb.Timerange{Id: id, Start: start, End: end, Tz: tz})
	}

	err = rows.Err()
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("GetTimeranges: %s, %d", name, len(timeranges))
	return &pb.Timeranges{Timeranges: timeranges}, nil
}

func (s *server) SetTimeranges(ctx context.Context, in *pb.Timeranges) (*pb.Empty, error) {
	playerID, tz, err := s.resolveToken(in.Token)
	if err != nil {
		return nil, err
	}
	eventID, err := s.resolveEvent(in.Event)
	if err != nil {
		return nil, err
	}

	stmt, err := s.db.Prepare("INSERT INTO timerange (player_id, \"start\", \"end\", tz, event_id) VALUES ($1, $2, $3, $4, $5)")
	if err != nil {
		log.Fatal(err)
	}
	log.Println(stmt)
	for _, timerange := range in.Timeranges {
		_, err := stmt.Exec(playerID, timerange.Start, timerange.End, tz, eventID)
		if err != nil {
			log.Fatal(err)
		}
	}

	return &pb.Empty{}, nil
}

func (s *server) DeleteTimeranges(ctx context.Context, in *pb.Timeranges) (*pb.Empty, error) {
	playerID, _, err := s.resolveToken(in.Token)
	if err != nil {
		return nil, err
	}

	stmt, err := s.db.Prepare("DELETE FROM timerange WHERE id = $1 AND player_id = $2")
	if err != nil {
		log.Fatal(err)
	}
	log.Println(stmt)
	for _, timerange := range in.Timeranges {
		_, err := stmt.Exec(timerange.Id, playerID)
		if err != nil {
			log.Fatal(err)
		}
	}

	return &pb.Empty{}, nil
}

func main() {

	dbString := fmt.Sprintf("host=%s port=%d user=%s "+
		"password=%s dbname=%s sslmode=disable",
		os.Getenv("DB_HOST"), 5432, "postgres", os.Getenv("DB_PW"), "postgres")

	db, err := sql.Open("postgres", dbString)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	err = db.Ping()
	if err != nil {
		log.Fatal(err)
	}
	log.Println("connected to db")

	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	log.Println("server listening")

	s := grpc.NewServer()
	pb.RegisterGatewayServer(s, &server{db: db})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
