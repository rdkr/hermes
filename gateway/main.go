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

func (s *server) GetPlayer(ctx context.Context, in *pb.Login) (*pb.Player, error) {

	var id string
	var tz string

	err := s.db.QueryRow("select id, tz from player where token = $1", in.Token).Scan(&id, &tz)
	if err != nil {
		if err == sql.ErrNoRows {
			return nil, errors.New("invalid token")
		}
		log.Fatal(err)
	}

	log.Printf("LOGIN: %s", id)

	return &pb.Player{Name: id, Tz: tz}, nil
}

func (s *server) GetIntervals(ctx context.Context, in *pb.Login) (*pb.Timeranges, error) {
	log.Printf("Received: %v", in)
	return &pb.Timeranges{}, nil
}

func (s *server) SetIntervals(ctx context.Context, in *pb.Timeranges) (*pb.Empty, error) {
	log.Printf("Received: %v", in)
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

	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterGatewayServer(s, &server{db: db})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
