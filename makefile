DOCKER_USER := hugo421

.PHONY: up kube-start push deploy open status clean

up: kube-start push deploy
	@echo "Deployed. Now run: make open"

kube-start:
	minikube status >/dev/null 2>&1 || minikube start --cpus=4 --memory=3000

push:
	docker build -t $(DOCKER_USER)/chess-frontend:latest ./frontend
	docker build -t $(DOCKER_USER)/opening-service:latest ./opening-service
	docker build -t $(DOCKER_USER)/game-service:latest ./game-service
	docker build -t $(DOCKER_USER)/chess-db:latest ./database
	docker push $(DOCKER_USER)/chess-frontend:latest
	docker push $(DOCKER_USER)/opening-service:latest
	docker push $(DOCKER_USER)/game-service:latest
	docker push $(DOCKER_USER)/chess-db:latest

deploy:
	kubectl apply -f kubernetes.yml

open:
	minikube service frontend-service

status:
	kubectl get pods,services

clean:
	-kubectl delete -f kubernetes.yml
