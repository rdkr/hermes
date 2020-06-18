FROM golang

RUN apt update && apt install -y protobuf-compiler
RUN go get github.com/golang/protobuf/protoc-gen-go
