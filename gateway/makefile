proxy:
	docker run -it -p 8080:8080 -v "$$(pwd)/envoy.yaml:/etc/envoy/envoy.yaml" \
		grpcweb/envoy -c /etc/envoy/envoy.yaml -l trace

build:
	docker build -t rdkr/hermes-gateway-proxy -f gateway-proxy.dockerfile .
	docker build -t rdkr/hermes-gateway-server -f gateway-server.dockerfile .

run-proxy: build
	docker run -it --rm rdkr/hermes-gateway-proxy

run: build
	docker run -it --rm \
		-e DB_HOST='host.docker.internal' \
		-e DB_PW='${DB_PW}' \
		rdkr/hermes-gateway-server

push: build
	docker push rdkr/hermes-gateway-server
	docker push rdkr/hermes-gateway-proxy

install:
	kubectl apply -f k8s.yaml

uninstall:
	kubectl delete -f k8s.yaml

redeploy:
	kubectl delete deployments -n hermes hermes-gateway
	kubectl apply -f k8s.yaml
