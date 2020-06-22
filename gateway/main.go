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
	port = "localhost:9090"
)

// server is used to implement helloworld.GreeterServer.
type server struct {
	db *sql.DB
	pb.UnimplementedGatewayServer
}

func (s *server) resolveToken(token string) (int, string, string, error) {
	var id int
	var name string
	var tz string

	err := s.db.QueryRow("select player_id, player_name, player_tz from players where magic_token = $1", token).Scan(&id, &name, &tz)
	if err != nil {
		if err == sql.ErrNoRows {
			return 0, "", "", errors.New("invalid token")
		}
		log.Fatal(err)
	}

	return id, name, tz, nil
}

func (s *server) resolveEvent(event string) (int, error) {
	var id int
	err := s.db.QueryRow("select event_id from events where event_name = $1", event).Scan(&id)
	if err != nil {
		if err == sql.ErrNoRows {
			return 0, errors.New("invalid event")
		}
		log.Fatal(err)
	}
	return id, nil
}

func (s *server) GetPlayer(ctx context.Context, in *pb.Login) (*pb.Player, error) {
	_, id, tz, err := s.resolveToken(in.Token)
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

	playerID, _, _, err := s.resolveToken(in.Token)
	if err != nil {
		return nil, err
	}

	rows, err := s.db.Query("SELECT timerange_id, timeranges.start, timeranges.end, tz FROM events JOIN timeranges ON (events.event_id = timeranges.event_id) WHERE events.event_name = $1 AND timeranges.player_id = $2", in.Event, playerID)
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
	log.Printf("GetTimeranges: %d, %d", playerID, len(timeranges))
	return &pb.Timeranges{Timeranges: timeranges}, nil
}

func (s *server) SetTimeranges(ctx context.Context, in *pb.Timeranges) (*pb.Empty, error) {
	playerID, _, tz, err := s.resolveToken(in.Token)
	if err != nil {
		return nil, err
	}
	eventID, err := s.resolveEvent(in.Event)
	if err != nil {
		return nil, err
	}

	stmt, err := s.db.Prepare("INSERT INTO timeranges (player_id, \"start\", \"end\", tz, event_id) VALUES ($1, $2, $3, $4, $5)")
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
	playerID, _, _, err := s.resolveToken(in.Token)
	if err != nil {
		return nil, err
	}

	stmt, err := s.db.Prepare("DELETE FROM timeranges WHERE timerange_id = $1 AND player_id = $2")
	if err != nil {
		log.Fatal(err)
	}

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
