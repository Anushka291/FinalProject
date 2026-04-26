# Complete Command Reference

Docker  •  Kubernetes  •  GitHub

*Windows Edition*

---

# 🐳 DOCKER — Complete Command Reference (Windows)

## 🐳 Installation & Version

| **Command** | **Description** |
| --- | --- |
| docker --version | Show Docker version |
| docker version | Show detailed client & server version info |
| docker info | Display system-wide Docker information |
| docker help | Show help for Docker commands |

## 📦 Images

| **Command** | **Description** |
| --- | --- |
| docker pull \<image\> | Download an image from Docker Hub |
| docker pull \<image\>:\<tag\> | Pull a specific version/tag |
| docker images | List all local images |
| docker images -a | List all images (including intermediates) |
| docker image ls | List images (alternative) |
| docker image inspect \<image\> | Show detailed image info |
| docker rmi \<image\> | Remove an image |
| docker rmi -f \<image\> | Force remove an image |
| docker image rm \<image\> | Remove image (alternative) |
| docker image prune | Remove unused/dangling images |
| docker image prune -a | Remove all unused images |
| docker tag \<src\> \<target\> | Tag an image with a new name |
| docker history \<image\> | Show image layer history |
| docker save -o file.tar \<image\> | Save image to tar archive |
| docker load -i file.tar | Load image from tar archive |
| docker inspect \<image\> | Return JSON metadata of an image |
| docker search \<term\> | Search Docker Hub for images |

## 🔨 Build

| **Command** | **Description** |
| --- | --- |
| docker build . | Build image from current directory Dockerfile |
| docker build -t name:tag . | Build and tag the image |
| docker build -f Dockerfile.prod . | Build using a specific Dockerfile |
| docker build --no-cache . | Build without using cache |
| docker build --build-arg KEY=VAL . | Pass build-time variables |
| docker build --target stage . | Build up to a specific multi-stage target |
| docker build --platform linux/amd64 . | Build for a specific platform |
| docker buildx build . | Build using BuildKit (extended features) |
| docker buildx build --push . | Build and push to registry |

## ▶️ Containers — Run

| **Command** | **Description** |
| --- | --- |
| docker run \<image\> | Create and start a container |
| docker run -d \<image\> | Run container in background (detached) |
| docker run -it \<image\> bash | Run with interactive terminal |
| docker run --name myapp \<image\> | Assign a name to the container |
| docker run -p 8080:80 \<image\> | Map host port 8080 to container port 80 |
| docker run -p 127.0.0.1:8080:80 \<image\> | Bind to specific host IP |
| docker run -e KEY=VALUE \<image\> | Set environment variable |
| docker run --env-file .env \<image\> | Load env vars from file |
| docker run -v /host:/container \<image\> | Mount host directory (bind mount) |
| docker run -v myvolume:/data \<image\> | Mount a named volume |
| docker run --rm \<image\> | Auto-remove container when it exits |
| docker run --restart always \<image\> | Always restart on exit |
| docker run --restart unless-stopped \<image\> | Restart unless manually stopped |
| docker run --memory 512m \<image\> | Limit container memory |
| docker run --cpus 1.5 \<image\> | Limit CPU usage |
| docker run --network mynet \<image\> | Connect to a specific network |
| docker run --user 1000:1000 \<image\> | Run as specific user:group |
| docker run --workdir /app \<image\> | Set working directory |
| docker run --read-only \<image\> | Mount root filesystem as read-only |
| docker run --privileged \<image\> | Give extended privileges to container |

## 📋 Containers — Manage

| **Command** | **Description** |
| --- | --- |
| docker ps | List running containers |
| docker ps -a | List all containers (including stopped) |
| docker ps -q | List only container IDs |
| docker start \<container\> | Start a stopped container |
| docker stop \<container\> | Gracefully stop a container (SIGTERM) |
| docker kill \<container\> | Force stop a container (SIGKILL) |
| docker restart \<container\> | Restart a container |
| docker pause \<container\> | Pause all processes in a container |
| docker unpause \<container\> | Unpause a paused container |
| docker rm \<container\> | Remove a stopped container |
| docker rm -f \<container\> | Force remove (even if running) |
| docker container prune | Remove all stopped containers |
| docker rename old new | Rename a container |
| docker update --memory 1g \<c\> | Update container resource limits |
| docker wait \<container\> | Block until container stops, print exit code |
| docker diff \<container\> | Show changes to container filesystem |
| docker port \<container\> | Show port mappings |
| docker top \<container\> | Show running processes inside container |
| docker stats | Live CPU/memory/network stats for all containers |
| docker stats \<container\> | Live stats for a specific container |

## 💬 Containers — Exec & Logs

| **Command** | **Description** |
| --- | --- |
| docker exec -it \<c\> bash | Open interactive shell in running container |
| docker exec -it \<c\> sh | Open sh shell (for Alpine-based images) |
| docker exec \<c\> \<cmd\> | Run a command in running container |
| docker exec -u root \<c\> bash | Exec as root user |
| docker logs \<container\> | Fetch container logs |
| docker logs -f \<container\> | Follow/stream logs in real time |
| docker logs --tail 100 \<c\> | Show last 100 log lines |
| docker logs --since 1h \<c\> | Show logs from the last 1 hour |
| docker logs --timestamps \<c\> | Show logs with timestamps |
| docker attach \<container\> | Attach to container's stdin/stdout/stderr |
| docker cp \<c\>:/path ./local | Copy file from container to host |
| docker cp ./local \<c\>:/path | Copy file from host to container |

## 💾 Volumes

| **Command** | **Description** |
| --- | --- |
| docker volume create myvolume | Create a named volume |
| docker volume ls | List all volumes |
| docker volume inspect myvolume | Show detailed volume info |
| docker volume rm myvolume | Remove a volume |
| docker volume prune | Remove all unused volumes |

## 🌐 Networks

| **Command** | **Description** |
| --- | --- |
| docker network create mynet | Create a user-defined bridge network |
| docker network create --driver overlay mynet | Create an overlay network (Swarm) |
| docker network ls | List all networks |
| docker network inspect mynet | Show network details |
| docker network connect mynet \<c\> | Connect container to a network |
| docker network disconnect mynet \<c\> | Disconnect container from network |
| docker network rm mynet | Remove a network |
| docker network prune | Remove all unused networks |

## 🗄️ Registry & Push

| **Command** | **Description** |
| --- | --- |
| docker login | Login to Docker Hub |
| docker login registry.example.com | Login to private registry |
| docker logout | Logout from registry |
| docker push user/image:tag | Push image to Docker Hub |
| docker pull user/image:tag | Pull image from Docker Hub |
| docker tag image user/image:tag | Tag image before pushing |

## 🐙 Docker Compose

| **Command** | **Description** |
| --- | --- |
| docker compose up | Create and start all services |
| docker compose up -d | Start services in background |
| docker compose up --build | Build images then start |
| docker compose down | Stop and remove containers/networks |
| docker compose down -v | Also remove volumes |
| docker compose stop | Stop services without removing |
| docker compose start | Start stopped services |
| docker compose restart | Restart all services |
| docker compose ps | Show running services |
| docker compose logs | View output from all services |
| docker compose logs -f service | Follow logs of specific service |
| docker compose exec service bash | Open shell in running service |
| docker compose run service cmd | Run one-off command in service |
| docker compose build | Build/rebuild images |
| docker compose pull | Pull latest images |
| docker compose config | Validate and view compose file |
| docker compose scale web=3 | Scale a service to N replicas |
| docker compose top | Show running processes in services |

## 🧹 System & Cleanup

| **Command** | **Description** |
| --- | --- |
| docker system df | Show disk usage (images, containers, volumes) |
| docker system prune | Remove all unused resources |
| docker system prune -a | Remove all unused + untagged resources |
| docker system prune --volumes | Also prune unused volumes |
| docker system info | Display system-wide information |
| docker system events | Get real-time events from the Docker daemon |

---

# ☸️ KUBERNETES — Complete Command Reference (Windows)

## ☸️ Cluster Info & Config

| **Command** | **Description** |
| --- | --- |
| kubectl version | Show kubectl and cluster version |
| kubectl cluster-info | Display cluster endpoint info |
| kubectl cluster-info dump | Dump detailed cluster state for debugging |
| kubectl config view | Show kubeconfig settings |
| kubectl config get-contexts | List all contexts (clusters) |
| kubectl config current-context | Show current active context |
| kubectl config use-context \<n\> | Switch to a different cluster context |
| kubectl config set-context --current --namespace=ns | Set default namespace |
| kubectl config rename-context old new | Rename a context |
| kubectl config delete-context \<n\> | Delete a context |
| kubectl api-resources | List all available API resources |
| kubectl api-versions | List all API versions available |
| kubectl explain \<resource\> | Get documentation for a resource |

## 📁 Namespaces

| **Command** | **Description** |
| --- | --- |
| kubectl get namespaces | List all namespaces |
| kubectl get ns | Short alias for namespaces |
| kubectl create namespace \<n\> | Create a namespace |
| kubectl delete namespace \<n\> | Delete a namespace and all its resources |
| kubectl describe namespace \<n\> | Show namespace details and resource quotas |

## 🏃 Pods

| **Command** | **Description** |
| --- | --- |
| kubectl get pods | List pods in default namespace |
| kubectl get pods -n \<ns\> | List pods in specific namespace |
| kubectl get pods -A | List pods across ALL namespaces |
| kubectl get pods -o wide | List pods with node and IP info |
| kubectl get pods -o yaml | Output pod details in YAML |
| kubectl get pods -o json | Output pod details in JSON |
| kubectl get pods -w | Watch pods in real time |
| kubectl get pod \<n\> -n \<ns\> | Get a specific pod |
| kubectl describe pod \<n\> | Show detailed pod info and events |
| kubectl run \<n\> --image=\<img\> | Create and run a pod |
| kubectl run \<n\> --image=\<img\> --port=80 | Run pod and expose port |
| kubectl delete pod \<n\> | Delete a specific pod |
| kubectl delete pod \<n\> --force | Force delete a pod immediately |
| kubectl delete pods --all -n \<ns\> | Delete all pods in namespace |
| kubectl logs \<pod\> | Print pod logs |
| kubectl logs \<pod\> -f | Stream/follow pod logs |
| kubectl logs \<pod\> --tail=100 | Show last 100 lines of logs |
| kubectl logs \<pod\> --since=1h | Show logs from last 1 hour |
| kubectl logs \<pod\> -c \<container\> | Logs from specific container in pod |
| kubectl logs \<pod\> --previous | Logs from previous (crashed) container |
| kubectl exec -it \<pod\> -- bash | Open interactive shell in pod |
| kubectl exec -it \<pod\> -- sh | Open sh shell in pod |
| kubectl exec \<pod\> -- \<cmd\> | Run command in pod without TTY |
| kubectl cp \<pod\>:/path ./local | Copy file from pod to local |
| kubectl cp ./local \<pod\>:/path | Copy file from local to pod |
| kubectl top pod | Show CPU/memory usage of pods |
| kubectl top pod \<n\> | Show resource usage of specific pod |
| kubectl port-forward pod/\<n\> 8080:80 | Forward local port to pod port |
| kubectl attach \<pod\> -it | Attach to a running pod's stdin |

## 🚀 Deployments

| **Command** | **Description** |
| --- | --- |
| kubectl get deployments | List all deployments |
| kubectl get deploy -n \<ns\> | List deployments in namespace |
| kubectl describe deployment \<n\> | Show deployment details |
| kubectl create deployment \<n\> --image=\<img\> | Create a deployment |
| kubectl apply -f deployment.yaml | Create/update deployment from file |
| kubectl delete deployment \<n\> | Delete a deployment |
| kubectl scale deployment \<n\> --replicas=5 | Scale to 5 replicas |
| kubectl set image deploy/\<n\> app=image:v2 | Update container image |
| kubectl rollout status deploy/\<n\> | Check rollout progress |
| kubectl rollout history deploy/\<n\> | View rollout revision history |
| kubectl rollout undo deploy/\<n\> | Rollback to previous version |
| kubectl rollout undo deploy/\<n\> --to-revision=2 | Rollback to specific revision |
| kubectl rollout pause deploy/\<n\> | Pause a rollout (canary) |
| kubectl rollout resume deploy/\<n\> | Resume a paused rollout |
| kubectl rollout restart deploy/\<n\> | Restart all pods in deployment |
| kubectl edit deployment \<n\> | Edit deployment live in editor |
| kubectl patch deploy \<n\> -p '{"spec":{...}}' | Patch deployment field |
| kubectl get deploy \<n\> -o yaml | Export deployment as YAML |

## 🔁 ReplicaSets

| **Command** | **Description** |
| --- | --- |
| kubectl get replicasets | List all ReplicaSets |
| kubectl get rs | Short alias for ReplicaSets |
| kubectl describe rs \<n\> | Show ReplicaSet details |
| kubectl delete rs \<n\> | Delete a ReplicaSet |
| kubectl scale rs \<n\> --replicas=3 | Scale a ReplicaSet |

## 🌐 Services

| **Command** | **Description** |
| --- | --- |
| kubectl get services | List all services |
| kubectl get svc | Short alias for services |
| kubectl get svc -n \<ns\> | List services in namespace |
| kubectl describe svc \<n\> | Show service details |
| kubectl expose deploy \<n\> --port=80 --type=ClusterIP | Expose deployment as ClusterIP |
| kubectl expose deploy \<n\> --port=80 --type=NodePort | Expose as NodePort |
| kubectl expose deploy \<n\> --port=80 --type=LoadBalancer | Expose as LoadBalancer |
| kubectl delete service \<n\> | Delete a service |
| kubectl port-forward svc/\<n\> 8080:80 | Forward local port to service port |
| kubectl get endpoints \<svc-name\> | List endpoints backing a service |

## 📋 ConfigMaps

| **Command** | **Description** |
| --- | --- |
| kubectl get configmaps | List all ConfigMaps |
| kubectl get cm | Short alias for ConfigMaps |
| kubectl describe cm \<n\> | Show ConfigMap details |
| kubectl create cm \<n\> --from-literal=KEY=VAL | Create from literal value |
| kubectl create cm \<n\> --from-file=./config.conf | Create from file |
| kubectl create cm \<n\> --from-env-file=.env | Create from .env file |
| kubectl apply -f configmap.yaml | Create/update ConfigMap from file |
| kubectl delete cm \<n\> | Delete a ConfigMap |
| kubectl edit cm \<n\> | Edit ConfigMap live |

## 🔐 Secrets

| **Command** | **Description** |
| --- | --- |
| kubectl get secrets | List all secrets |
| kubectl describe secret \<n\> | Show secret details (values hidden) |
| kubectl create secret generic \<n\> --from-literal=KEY=VAL | Create generic secret |
| kubectl create secret generic \<n\> --from-file=./cred | Create secret from file |
| kubectl create secret docker-registry \<n\> --docker-server=\<srv\> --docker-username=\<u\> --docker-password=\<p\> | Create Docker registry secret |
| kubectl create secret tls \<n\> --cert=tls.crt --key=tls.key | Create TLS secret |
| kubectl apply -f secret.yaml | Create/update secret from file |
| kubectl delete secret \<n\> | Delete a secret |
| kubectl get secret \<n\> -o yaml | View secret (base64 encoded) |
| kubectl get secret \<n\> -o jsonpath='{.data.KEY}' │ base64 -d | Decode a specific secret value |

## 📥 Ingress

| **Command** | **Description** |
| --- | --- |
| kubectl get ingress | List all ingress resources |
| kubectl get ing | Short alias for ingress |
| kubectl get ing -n \<ns\> | List ingress in namespace |
| kubectl describe ingress \<n\> | Show ingress details |
| kubectl apply -f ingress.yaml | Create/update ingress from file |
| kubectl delete ingress \<n\> | Delete an ingress resource |
| kubectl edit ingress \<n\> | Edit ingress live |

## 💾 Volumes & PVC

| **Command** | **Description** |
| --- | --- |
| kubectl get pv | List PersistentVolumes |
| kubectl get pvc | List PersistentVolumeClaims |
| kubectl get pvc -n \<ns\> | List PVCs in namespace |
| kubectl describe pvc \<n\> | Show PVC details and binding status |
| kubectl apply -f pvc.yaml | Create PVC from file |
| kubectl delete pvc \<n\> | Delete a PVC |
| kubectl get storageclass | List available storage classes |
| kubectl describe storageclass \<n\> | Show storage class details |

## 📊 StatefulSets & DaemonSets

| **Command** | **Description** |
| --- | --- |
| kubectl get statefulsets | List StatefulSets |
| kubectl get sts | Short alias for StatefulSets |
| kubectl describe sts \<n\> | Show StatefulSet details |
| kubectl scale sts \<n\> --replicas=3 | Scale a StatefulSet |
| kubectl delete sts \<n\> | Delete a StatefulSet |
| kubectl get daemonsets | List DaemonSets |
| kubectl get ds | Short alias for DaemonSets |
| kubectl describe ds \<n\> | Show DaemonSet details |
| kubectl delete ds \<n\> | Delete a DaemonSet |

## ⚡ Jobs & CronJobs

| **Command** | **Description** |
| --- | --- |
| kubectl get jobs | List all Jobs |
| kubectl describe job \<n\> | Show Job details |
| kubectl create job \<n\> --image=\<img\> | Create a one-shot Job |
| kubectl delete job \<n\> | Delete a Job |
| kubectl get cronjobs | List all CronJobs |
| kubectl get cj | Short alias for CronJobs |
| kubectl describe cj \<n\> | Show CronJob details |
| kubectl apply -f cronjob.yaml | Create/update CronJob from file |
| kubectl delete cronjob \<n\> | Delete a CronJob |

## 📈 HPA & Autoscaling

| **Command** | **Description** |
| --- | --- |
| kubectl get hpa | List all HPAs |
| kubectl describe hpa \<n\> | Show HPA details and current metrics |
| kubectl autoscale deploy \<n\> --min=2 --max=10 --cpu-percent=70 | Create HPA for deployment |
| kubectl delete hpa \<n\> | Delete an HPA |
| kubectl top nodes | Show CPU/memory usage of nodes |
| kubectl top pods -A | Show resource usage across all pods |

## 🖥️ Nodes

| **Command** | **Description** |
| --- | --- |
| kubectl get nodes | List all cluster nodes |
| kubectl get nodes -o wide | List nodes with IP and OS info |
| kubectl describe node \<n\> | Show detailed node info |
| kubectl top node | Show node CPU/memory usage |
| kubectl cordon \<node\> | Mark node as unschedulable |
| kubectl uncordon \<node\> | Mark node as schedulable again |
| kubectl drain \<node\> | Safely evict all pods from node |
| kubectl drain \<node\> --ignore-daemonsets | Drain ignoring DaemonSet pods |
| kubectl drain \<node\> --force | Force drain (removes unmanaged pods) |
| kubectl label node \<n\> key=val | Add a label to a node |
| kubectl taint node \<n\> key=val:NoSchedule | Taint a node |
| kubectl taint node \<n\> key:NoSchedule- | Remove a taint from a node |

## 🔒 RBAC — Roles & Bindings

| **Command** | **Description** |
| --- | --- |
| kubectl get roles -n \<ns\> | List roles in a namespace |
| kubectl get rolebindings -n \<ns\> | List role bindings in namespace |
| kubectl get clusterroles | List cluster-wide roles |
| kubectl get clusterrolebindings | List cluster-wide role bindings |
| kubectl describe role \<n\> -n \<ns\> | Show role permissions |
| kubectl apply -f rbac.yaml | Create role/rolebinding from file |
| kubectl create serviceaccount \<n\> -n \<ns\> | Create a service account |
| kubectl get serviceaccounts | List service accounts |
| kubectl auth can-i \<verb\> \<resource\> | Check your own RBAC permissions |
| kubectl auth can-i \<verb\> \<resource\> --as=user | Check another user's permissions |

## 📝 Apply, Edit & Delete (General)

| **Command** | **Description** |
| --- | --- |
| kubectl apply -f file.yaml | Create or update resource from file |
| kubectl apply -f ./folder/ | Apply all YAML files in a folder |
| kubectl apply -f https://url/file.yaml | Apply from a URL |
| kubectl create -f file.yaml | Create resource (fails if exists) |
| kubectl replace -f file.yaml | Replace resource from file |
| kubectl delete -f file.yaml | Delete resource defined in file |
| kubectl edit \<resource\> \<n\> | Open resource in live editor (vim) |
| kubectl patch \<resource\> \<n\> -p '{"key":"value"}' | Patch a resource with JSON |
| kubectl label \<resource\> \<n\> key=val | Add/update a label |
| kubectl annotate \<resource\> \<n\> key=val | Add/update an annotation |
| kubectl get all -n \<ns\> | List all resource types in namespace |
| kubectl get all -A | List all resources in all namespaces |
| kubectl diff -f file.yaml | Show what would change before applying |
| kubectl dry-run=client -f file.yaml | Dry run (validate only, no apply) |
| kubectl get \<resource\> \<n\> -o yaml > out.yaml | Export resource to YAML file |

## 🔍 Debugging & Troubleshooting

| **Command** | **Description** |
| --- | --- |
| kubectl describe \<resource\> \<n\> | Show events and full details |
| kubectl get events -n \<ns\> | List all events in namespace |
| kubectl get events --sort-by=.lastTimestamp | Events sorted by time |
| kubectl logs \<pod\> --previous | Logs from crashed/restarted container |
| kubectl debug pod/\<n\> -it --image=busybox | Attach a debug container to pod |
| kubectl run tmp --image=curlimages/curl -it --rm -- sh | Temporary debug pod (auto-removed) |
| kubectl exec -it \<pod\> -- env | Check env vars injected into pod |
| kubectl exec -it \<pod\> -- cat /etc/hosts | Inspect pod /etc/hosts |
| kubectl get pod \<n\> -o jsonpath='{.status.phase}' | Get pod phase via JSONPath |
| kubectl wait --for=condition=ready pod/\<n\> | Wait until pod is ready |
| kubectl wait --for=condition=available deploy/\<n\> | Wait for deployment to be available |

---

# 🐙 GITHUB / GIT — Complete Command Reference (Windows)

## ⚙️ Git Config (First-Time Setup)

| **Command** | **Description** |
| --- | --- |
| git config --global user.name "Your Name" | Set your global username |
| git config --global user.email "you@email.com" | Set your global email |
| git config --global core.editor "code --wait" | Set VS Code as default editor |
| git config --global core.autocrlf true | Auto convert line endings (Windows) |
| git config --global init.defaultBranch main | Set default branch name to main |
| git config --list | List all config settings |
| git config --global alias.st status | Create a git alias (git st = git status) |
| git config --global credential.helper manager | Use Windows Credential Manager |

## 📁 Repository Setup

| **Command** | **Description** |
| --- | --- |
| git init | Initialize a new local repo in current folder |
| git init \<folder\> | Initialize repo in a new folder |
| git clone \<url\> | Clone a remote repository |
| git clone \<url\> \<folder\> | Clone into a specific folder |
| git clone --depth 1 \<url\> | Shallow clone (latest commit only) |
| git clone -b \<branch\> \<url\> | Clone a specific branch |
| git remote -v | Show remote connections |
| git remote add origin \<url\> | Add a remote named origin |
| git remote set-url origin \<url\> | Change remote URL |
| git remote remove origin | Remove a remote |
| git remote rename old new | Rename a remote |

## 📝 Staging & Committing

| **Command** | **Description** |
| --- | --- |
| git status | Show working tree status |
| git status -s | Short status format |
| git add \<file\> | Stage a specific file |
| git add . | Stage all changes in current directory |
| git add -A | Stage all changes (new, modified, deleted) |
| git add -p | Interactively stage chunks (patch mode) |
| git add -u | Stage modified and deleted (not new files) |
| git commit -m "message" | Commit with a message |
| git commit -am "message" | Stage tracked files and commit together |
| git commit --amend -m "new msg" | Amend the last commit message |
| git commit --amend --no-edit | Amend commit without changing message |
| git reset HEAD \<file\> | Unstage a file (keep changes) |
| git restore \<file\> | Discard changes in working directory |
| git restore --staged \<file\> | Unstage a file |
| git rm \<file\> | Remove file from working tree and staging |
| git rm --cached \<file\> | Remove from staging only (keep local file) |
| git mv old.txt new.txt | Rename/move a file and stage the change |

## 🌿 Branches

| **Command** | **Description** |
| --- | --- |
| git branch | List local branches |
| git branch -a | List all branches (local and remote) |
| git branch -r | List remote branches only |
| git branch \<n\> | Create a new branch |
| git checkout \<branch\> | Switch to a branch |
| git checkout -b \<branch\> | Create and switch to new branch |
| git switch \<branch\> | Switch branches (modern syntax) |
| git switch -c \<branch\> | Create and switch (modern syntax) |
| git branch -d \<branch\> | Delete a branch (safe) |
| git branch -D \<branch\> | Force delete a branch |
| git branch -m old new | Rename a branch |
| git branch -m new | Rename current branch |
| git branch --merged | List branches merged into current |
| git branch --no-merged | List branches not yet merged |
| git push origin --delete \<branch\> | Delete a remote branch |

## 🔀 Merging & Rebasing

| **Command** | **Description** |
| --- | --- |
| git merge \<branch\> | Merge branch into current branch |
| git merge --no-ff \<branch\> | Merge with a merge commit always |
| git merge --squash \<branch\> | Squash all commits into one before merge |
| git merge --abort | Abort an in-progress merge |
| git rebase \<branch\> | Rebase current branch onto another |
| git rebase -i HEAD~3 | Interactive rebase last 3 commits |
| git rebase --abort | Abort rebase in progress |
| git rebase --continue | Continue after resolving rebase conflict |
| git rebase --skip | Skip current patch during rebase |
| git cherry-pick \<commit\> | Apply a specific commit to current branch |
| git cherry-pick \<c1\>..\<c2\> | Cherry-pick a range of commits |

## ⬆️ Push & Pull

| **Command** | **Description** |
| --- | --- |
| git push | Push to tracked remote branch |
| git push origin \<branch\> | Push branch to origin |
| git push -u origin \<branch\> | Push and set upstream tracking |
| git push --force | Force push (overwrites remote — dangerous) |
| git push --force-with-lease | Safer force push (fails if remote changed) |
| git push --tags | Push all local tags to remote |
| git push origin \<tag\> | Push a specific tag |
| git pull | Fetch and merge from tracked remote |
| git pull origin \<branch\> | Pull specific branch from origin |
| git pull --rebase | Pull and rebase instead of merge |
| git fetch | Download remote changes without merging |
| git fetch origin | Fetch from origin |
| git fetch --all | Fetch from all remotes |
| git fetch --prune | Fetch and delete stale remote-tracking branches |

## 🏷️ Tags

| **Command** | **Description** |
| --- | --- |
| git tag | List all tags |
| git tag \<n\> | Create a lightweight tag |
| git tag -a v1.0 -m "Release v1.0" | Create an annotated tag |
| git tag -a v1.0 \<commit\> | Tag a specific past commit |
| git push origin v1.0 | Push a tag to remote |
| git push origin --tags | Push all tags to remote |
| git tag -d \<n\> | Delete a local tag |
| git push origin --delete \<tag\> | Delete a remote tag |
| git show v1.0 | Show tag details and associated commit |
| git checkout v1.0 | Checkout a specific tag (detached HEAD) |

## 📜 Log & History

| **Command** | **Description** |
| --- | --- |
| git log | Show commit history |
| git log --oneline | Compact one-line per commit view |
| git log --oneline --graph --all | Visual branch graph with all branches |
| git log -n 10 | Show last 10 commits |
| git log --author="Name" | Filter commits by author |
| git log --since="2 weeks ago" | Show commits from last 2 weeks |
| git log --until="2025-01-01" | Show commits until a date |
| git log -- \<file\> | Show commit history for a specific file |
| git log -p \<file\> | Show diffs for a specific file |
| git log --stat | Show files changed per commit |
| git log --grep="bug" | Search commits by message keyword |
| git log -S "functionName" | Find commits that added/removed text |
| git show \<commit\> | Show a specific commit's details and diff |
| git blame \<file\> | Show who changed each line of a file |
| git reflog | Show history of HEAD movements (recovery tool) |
| git shortlog -sn | Count commits per author |

## 🔍 Diff & Comparison

| **Command** | **Description** |
| --- | --- |
| git diff | Show unstaged changes |
| git diff --staged | Show staged changes (ready to commit) |
| git diff HEAD | Show all uncommitted changes |
| git diff \<branch1\> \<branch2\> | Compare two branches |
| git diff \<commit1\> \<commit2\> | Compare two commits |
| git diff \<commit\> -- \<file\> | Compare file at specific commit vs now |
| git diff --stat | Summary of files changed (no content) |
| git diff --word-diff | Show word-level diff instead of line-level |

## 🗄️ Stash

| **Command** | **Description** |
| --- | --- |
| git stash | Save current changes to stash |
| git stash push -m "description" | Stash with a description |
| git stash list | List all stashed changes |
| git stash pop | Apply most recent stash and remove it |
| git stash apply | Apply most recent stash (keep it) |
| git stash apply stash@{2} | Apply a specific stash entry |
| git stash drop stash@{1} | Delete a specific stash entry |
| git stash clear | Delete all stashed entries |
| git stash branch \<branch\> | Create branch from stash |
| git stash show -p | Show diff of most recent stash |
| git stash --include-untracked | Stash including untracked files |

## ↩️ Undo & Reset

| **Command** | **Description** |
| --- | --- |
| git revert \<commit\> | Create a new commit that undoes a commit |
| git revert HEAD | Revert the most recent commit |
| git revert HEAD~3..HEAD | Revert last 3 commits |
| git reset --soft HEAD~1 | Undo commit, keep changes staged |
| git reset --mixed HEAD~1 | Undo commit, keep changes unstaged (default) |
| git reset --hard HEAD~1 | Undo commit and discard all changes |
| git reset --hard origin/main | Reset to match remote main branch |
| git clean -fd | Remove untracked files and directories |
| git clean -n | Dry run — show what would be deleted |
| git restore \<file\> | Discard local changes in a file |
| git restore . | Discard all local changes |
| git checkout -- \<file\> | Restore file from last commit (older syntax) |

## 🔧 GitHub CLI (gh)

| **Command** | **Description** |
| --- | --- |
| gh auth login | Authenticate with GitHub |
| gh auth status | Check authentication status |
| gh repo create | Create a new GitHub repository |
| gh repo clone \<user/repo\> | Clone a GitHub repository |
| gh repo view | View repository info |
| gh repo fork \<user/repo\> | Fork a repository |
| gh pr list | List pull requests |
| gh pr create | Create a pull request |
| gh pr checkout \<number\> | Checkout a PR locally |
| gh pr review \<number\> --approve | Approve a pull request |
| gh pr merge \<number\> | Merge a pull request |
| gh pr view \<number\> | View PR details |
| gh pr close \<number\> | Close a pull request |
| gh issue list | List issues |
| gh issue create | Create a new issue |
| gh issue view \<number\> | View issue details |
| gh issue close \<number\> | Close an issue |
| gh release list | List releases |
| gh release create v1.0 | Create a new release |
| gh workflow list | List GitHub Actions workflows |
| gh workflow run \<n\> | Manually trigger a workflow |
| gh run list | List workflow runs |
| gh run view \<id\> | View a specific workflow run |
| gh gist create \<file\> | Create a GitHub Gist |

## 🪟 Windows-Specific Tips

| **Command** | **Description** |
| --- | --- |
| git config --global core.autocrlf true | Auto-convert LF to CRLF on Windows |
| git config --global core.longpaths true | Enable long file paths on Windows |
| git config --global credential.helper manager-core | Use Git Credential Manager |
| ssh-keygen -t ed25519 -C "you@email.com" | Generate SSH key (run in Git Bash) |
| cat ~/.ssh/id_ed25519.pub | Display public SSH key (Git Bash) |
| type %USERPROFILE%\\.ssh\\id_ed25519.pub | Display public key in CMD |
| git config --global gpg.program "C:\\Program Files\\Git\\usr\\bin\\gpg.exe" | Set GPG path on Windows |
| git config --global http.sslBackend schannel | Use Windows SSL backend |
