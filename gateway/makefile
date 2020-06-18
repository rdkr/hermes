proxy:
	docker run -it -p 8080:8080 -v "$$(pwd)/envoy.yaml:/etc/envoy/envoy.yaml" \
		grpcweb/envoy -c /etc/envoy/envoy.yaml -l trace
