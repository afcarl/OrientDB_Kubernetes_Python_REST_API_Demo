# Deploy OrientDB v3.0.18 in container on Kubernetes & connect w/ Python 3.7 via REST API:

# 1) Download the minikube binary from the following location: https://github.com/kubernetes/minikube/releases, The file name is minikube-windows-amd64.exe. Rename to minikube.exe

# 2) Download the kubectl command line utilityfrom the following location: http://storage.googleapis.com/kubernetes-release/release/v1.4.0/bin/windows/amd64/kubectl.exe

#
# 3) Admin CMD Window #1:
### a. minikube.exe start --vm-driver="virtualbox"
### b. minikube.exe dashboard
#
# 4) Admin CMD Window #2:
### a. kubectl create secret generic orientdb-pass --from-file=password.txt
### b. kubectl apply -f local-volumes.yaml
### c. kubectl apply -f orientdb.yaml
#
# 5) References:
### a. Tutorial : Getting Started with Kubernetes on your Windows Laptop with Minikube: https://rominirani.com/tutorial-getting-started-with-kubernetes-on-your-windows-laptop-with-minikube-3269b54a226

### b. Host a graph database such as OrientDB on IBM Container Service using Kubernetes APIs: https://github.com/IBM/deploy-graph-db-container

### c. Getting Started with Kubernetes: Deploy a Docker Container with Kubernetes in 5 minutes: https://codeburst.io/getting-started-with-kubernetes-deploy-a-docker-container-with-kubernetes-in-5-minutes-eb4be0e96370

### d. Orientdb: OrientDB a Multi-Model Open Source NoSQL DBMS that combines graphs and documents: https://docs.docker.com/samples/library/orientdb/

### e. Docker run reference: https://docs.docker.com/engine/reference/run/

### f. Deployments: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

### g. Tinkerpop Toy Graph Database: http://tinkerpop.apache.org/docs/current/tutorials/getting-started/
