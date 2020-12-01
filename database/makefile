install:
	helm repo add bitnami https://charts.bitnami.com/bitnami
	helm upgrade --namespace hermes --install --atomic \
 		-f postgres.yaml \
		postgres bitnami/postgresql

port-forward:
	kubectl port-forward --address 0.0.0.0 --namespace hermes svc/postgres-postgresql 5432:5432

pgadmin:
	docker run --name pgadmin -it -p 5433:80 -e PGADMIN_DEFAULT_EMAIL=admin -e PGADMIN_DEFAULT_PASSWORD=admin dpage/pgadmin4

podman pod create --name hermes -p 5432:5432 -p 5433:80
podman run -d --pod hermes -v $HOME/.kube/config:/root/.kube/config -v $TERMINAL_DIR/config/doctl/config.yaml:/root/.config/doctl/config.yaml proxy kubectl port-forward --address 0.0.0.0 --namespace hermes svc/postgres-postgresql 5432:5432
podman run -d --pod hermes -e PGADMIN_DEFAULT_EMAIL=admin@admin -e PGADMIN_DEFAULT_PASSWORD=admin dpage/pgadmin4
