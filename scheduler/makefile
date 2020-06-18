build:
	docker build -t rdkr/hermes-scheduler .

run: build
	docker run -it --rm \
		-e DISCORD_TOKEN="${DISCORD_TOKEN}" \
		-e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
		-e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
		-e DB_USER='postgres' \
		-e DB_HOST='host.docker.internal' \
		-e DB_PW='${DB_PW}' \
		rdkr/hermes-scheduler python main.py

push: build
	docker push rdkr/hermes-scheduler

install:
	helm repo add bitnami https://charts.bitnami.com/bitnami
	helm upgrade --namespace hermes --install --atomic \
 		-f postgres.yaml \
		postgres bitnami/postgresql
	kubectl apply -f k8s.yaml

uninstall:
	kubectl delete -f k8s.yaml

redeploy:
	kubectl delete deployments -n hermes hermes-scheduler
	kubectl apply -f k8s.yaml

.PHONY: lint auto-format test cov

lint: auto-format
	python3 -m pylint *.py scheduler/*.py tests/*.py
# 	python3 -m pydocstyle *.py scheduler/*.py tests/*.py

auto-format:
	black *.py

test:
	coverage run --source scheduler -m pytest -s tests
	coverage html

cov: test
	open htmlcov/index.html