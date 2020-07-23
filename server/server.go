package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"
	"strconv"

	pb "github.com/erdincmutlu/grpc_demo/grpcdemopb"
	"google.golang.org/grpc"
)

const serverPort = "7777"

// GrpcDemo is the struct
type GrpcDemo struct {
}

// NoParamFunc is a simple function call
func (s *GrpcDemo) NoParamFunc(_ context.Context, _ *pb.Empty) (*pb.Empty, error) {
	fmt.Printf("In NoParamFunc\n")
	// return &pb.Empty{}, nil
	return new(pb.Empty), nil
}

// UnaryFunc is a unary function call
func (s *GrpcDemo) UnaryFunc(_ context.Context, req *pb.UnaryFuncRequest) (*pb.UnaryFuncResponse, error) {
	fmt.Printf("In UnaryFunc\n")
	msg := "Hello " + req.Name + "! You are " + strconv.FormatInt(req.Height, 10) + "cm tall"
	return &pb.UnaryFuncResponse{Msg: msg}, nil
}

func main() {
	flag.Parse()
	fmt.Printf("Starting GRPC server at port %s\n", serverPort)
	startGRPCServer()
	select {}
}

func startGRPCServer() {
	lis, err := net.Listen("tcp", "localhost:"+serverPort)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	grpcServer := grpc.NewServer()
	pb.RegisterGrpcDemoServer(grpcServer, &GrpcDemo{})
	// ... // determine whether to use TLS
	grpcServer.Serve(lis)
}
