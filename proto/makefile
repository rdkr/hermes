all: ../gateway/proto/hermes.pb.go ../frontend/src/proto/hermes_grpc_web_pb.js ../frontend/src/proto/hermes_pb.js

../gateway/proto/hermes.pb.go: hermes.proto
	docker build -t grpc-go -f go.dockerfile .
	docker run \
		-v '${PWD}:/build' \
		-v '${PWD}/../gateway/proto:/out' \
		grpc-go \
			protoc \
				--proto_path /build hermes.proto \
				--go_opt=paths=source_relative \
				--go_out=plugins=grpc:/out

../frontend/src/proto/hermes_grpc_web_pb.js ../frontend/src/proto/hermes_pb.js: hermes.proto
	protoc hermes.proto \
		--js_out=import_style=commonjs:../frontend/src/proto \
		--grpc-web_out=import_style=commonjs,mode=grpcwebtext:../frontend/src/proto
	ls ../frontend/src/proto -1 \
		| xargs -I % sed -i '1i/* eslint-disable */'  ../frontend/src/proto/%

install:
	npm i grpc-web
