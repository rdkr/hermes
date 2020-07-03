all: ../gateway/proto/hermes.pb.go ../frontend/src/proto/hermes_grpc_web_pb.js ../frontend/src/proto/hermes_pb.js

../gateway/proto/hermes.pb.go: hermes.proto
	docker run \
		-v '${PWD}:/build' \
		-v '${PWD}/../gateway/proto:/out' \
		grpc-go-protoc \
			--proto_path /build hermes.proto\
			--go_opt=paths=source_relative \
			--go_out=plugins=grpc:/out \

../frontend/src/proto/hermes_grpc_web_pb.js ../frontend/src/proto/hermes_pb.js: hermes.proto
	docker run \
		-v '${PWD}:/build' \
		-v '${PWD}/../frontend/src/proto:/out' \
		grpc-js-protoc \
			--proto_path /build /build/hermes.proto \
			--js_out=import_style=commonjs,binary:/out	 \
			--grpc-web_out=import_style=commonjs,mode=grpcwebtext:/out	
	ls ../frontend/src/proto -1 \
		| xargs -I % sed -i '1i/* eslint-disable */'  ../frontend/src/proto/%

install:
	docker build -t grpc-js-protoc -f js.dockerfile .
	docker build -t grpc-go-protoc -f go.dockerfile .