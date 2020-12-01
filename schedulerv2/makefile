build:
	podman build -t rdkr/hermes-schedulerv2 -f containerfile .

run:
	podman run \
		--pod hermes \
		--rm -it \
		-v $$(pwd):/usr/src/app \
		-e DB_PW='${DB_PW}' \
		-e DB_USER='postgres' \
		-e DB_HOST='localhost' \
		rdkr/hermes-schedulerv2 \
		python main.py

push: build
	docker push rdkr/hermes-scheduler

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
