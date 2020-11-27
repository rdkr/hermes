all: ../gateway/proto/hermes.pb.go ../frontend/src/proto/hermes_grpc_web_pb.js ../frontend/src/proto/hermes_pb.js ../scheduler/proto/hermes_pb2.py ../scheduler/proto/hermes_pb2_grpc.py

../gateway/proto/hermes.pb.go: hermes.proto
	podman run \
		-v "${PWD}:/build" \
		-v "${PWD}/../gateway/proto:/out" \
		grpc-go-protoc \
			--proto_path /build hermes.proto \
			--go_opt=paths=source_relative \
			--go_out=plugins=grpc:/out

../frontend/src/proto/hermes_grpc_web_pb.js ../frontend/src/proto/hermes_pb.js: hermes.proto
	podman run \
		-v '${PWD}:/build' \
		-v '${PWD}/../frontend/src/proto:/out' \
		grpc-js-protoc \
			--proto_path /build /build/hermes.proto \
			--js_out=import_style=commonjs,binary:/out	 \
			--grpc-web_out=import_style=commonjs,mode=grpcwebtext:/out
	ls ../frontend/src/proto -1 \
		| xargs -I % sed -i '1i/* eslint-disable */'  ../frontend/src/proto/%

../scheduler/proto/hermes_pb2.py ../scheduler/proto/hermes_pb2_grpc.py: hermes.proto
	podman run \
		-v '${PWD}:/build' \
		-v '${PWD}/../scheduler/proto/:/out' \
		grpc-python-protoc python -m grpc.tools.protoc \
			--proto_path /build hermes.proto \
			--grpc_python_out=/out \
			--python_out=/out
	sed -i 's/import hermes_pb2/import proto.hermes_pb2/' ../scheduler/proto/hermes_pb2_grpc.py

install:
	podman build -t grpc-js-protoc -f js.dockerfile .
	podman build -t grpc-go-protoc -f go.dockerfile .
	podman build -t grpc-python-protoc -f python.dockerfile .
