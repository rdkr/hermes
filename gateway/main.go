package main

import (
	"context"
	"log"
	"net"

	pb "gateway/proto"

	"google.golang.org/grpc"
)

const (
	port = ":9090"
)

// server is used to implement helloworld.GreeterServer.
type server struct {
	pb.UnimplementedEchoServiceServer
}

func (s *server) Echo(ctx context.Context, in *pb.EchoRequest) (*pb.EchoResponse, error) {
	log.Printf("Received: %v", in)
	return &pb.EchoResponse{}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterEchoServiceServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
