proxy:
	docker run -it --net host -v "$$(pwd)/envoy.yaml:/etc/envoy/envoy.yaml" \
		envoyproxy/envoy:v1.14-latest -c /etc/envoy/envoy.yaml -l debug

serve:
	DB_HOST=localhost SCHEDULER_HOST=localhost go run main.go

build:
	docker build -t rdkr/hermes-gateway-server .

run: build
	docker run -it --rm \
		--net host \
		-e DB_HOST='localhost' \
		-e DB_PW='${DB_PW}' \
		rdkr/hermes-gateway-server

push: build
	docker push rdkr/hermes-gateway-server

install:
	kubectl apply -f k8s.yaml

uninstall:
	kubectl delete -f k8s.yaml

redeploy: push
	-kubectl delete deployments -n hermes hermes-gateway
	kubectl apply -f k8s.yaml
