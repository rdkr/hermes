install:
	helm repo add bitnami https://charts.bitnami.com/bitnami
	helm upgrade --namespace hermes --install --atomic \
 		-f postgres.yaml \
		postgres bitnami/postgresql

port-forward:
	kubectl port-forward --address 0.0.0.0 --namespace hermes svc/postgres-postgresql 5432:5432

pgadmin:
	docker run --name pgadmin -it -p 5433:80 -e PGADMIN_DEFAULT_EMAIL=admin -e PGADMIN_DEFAULT_PASSWORD=admin dpage/pgadmin4
