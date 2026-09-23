DOCKER_USER := hugo421

.PHONY: up kube-start push deploy open status clean

up: kube-start push deploy
	@echo "Deployed. Now run: make open"

kube-start:
	minikube status >/dev/null 2>&1 || minikube start --cpus=4 --memory=3000

push:
	docker buildx build --platform linux/amd64,linux/arm64 -t $(DOCKER_USER)/chess-frontend:latest --push ./frontend
	docker buildx build --platform linux/amd64,linux/arm64 -t $(DOCKER_USER)/opening-service:latest --push ./opening-service
	docker buildx build --platform linux/amd64,linux/arm64 -t $(DOCKER_USER)/game-service:latest --push ./game-service
	docker buildx build --platform linux/amd64,linux/arm64 -t $(DOCKER_USER)/chess-db:latest --push ./database

deploy:
	kubectl apply -f kubernetes.yml

open:
	minikube service frontend-service

status:
	kubectl get pods,services

clean:
	-kubectl delete -f kubernetes.yml
