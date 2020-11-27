proxy:
	podman run -it --net host -v "$$(pwd)/envoy.yaml:/etc/envoy/envoy.yaml" \
		envoyproxy/envoy:v1.14-latest -c /etc/envoy/envoy.yaml -l debug

serve:
	DB_HOST=localhost SCHEDULER_HOST=localhost go run main.go

build:
	podman build -f containerfile -t rdkr/hermes-gateway .

run: build
	podman run -it --rm \
		--net host \
		-e DB_HOST='localhost' \
		-e DB_PW='${DB_PW}' \
		rdkr/hermes-gateway

push: build
	podman push rdkr/hermes-gateway

install:
	kubectl apply -f k8s.yaml

uninstall:
	kubectl delete -f k8s.yaml

redeploy: push
	-kubectl delete deployments -n hermes hermes-gateway
	kubectl apply -f k8s.yaml
