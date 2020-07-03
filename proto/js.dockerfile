FROM node
RUN apt update && apt install -y protobuf-compiler
RUN wget https://github.com/grpc/grpc-web/releases/download/1.2.0/protoc-gen-grpc-web-1.2.0-linux-x86_64 && \
    mv protoc-gen-grpc-web-1.2.0-linux-x86_64 /usr/local/bin/protoc-gen-grpc-web && \
    chmod +x /usr/local/bin/protoc-gen-grpc-web
ENTRYPOINT [ "protoc" ] 