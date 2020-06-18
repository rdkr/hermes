install:
	helm repo add bitnami https://charts.bitnami.com/bitnami
	helm upgrade --namespace hermes --install --atomic \
 		-f postgres.yaml \
		postgres bitnami/postgresql

port-forward:
	kubectl port-forward --namespace hermes svc/postgres-postgresql 5432:5432
