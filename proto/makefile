../gateway/proto/echo.pb.go:
	docker build -t grpc-go -f go.dockerfile .
	docker run \
		-v '${PWD}:/build' \
		-v '${PWD}/../gateway/proto:/out' \
		grpc-go \
			protoc \
				--proto_path /build echo.proto \
				--go_opt=paths=source_relative \
				--go_out=plugins=grpc:/out

proto:
	protoc echo.proto \
		--js_out=import_style=commonjs:../frontend/src/proto \
		--grpc-web_out=import_style=commonjs,mode=grpcwebtext:../frontend/src/proto



inst:
	go get github.com/golang/protobuf/protoc-gen-go
	npm i grpc-web
