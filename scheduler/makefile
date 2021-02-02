build:
	podman build -f dockerfile -t rdkr/hermes-scheduler .

run: build
	podman run --pod hermes -it --rm \
		--net host \
		-e DISCORD_TOKEN="${DISCORD_TOKEN}" \
		-e HERMES_PREFIX='£' \
		-e EVENT_DB_ENDPOINT='localhost:50051' \
		rdkr/hermes-scheduler python main.py

push: build
	podman push rdkr/hermes-scheduler

install:
	kubectl apply -f k8s.yaml

uninstall:
	kubectl delete -f k8s.yaml

redeploy: push
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
