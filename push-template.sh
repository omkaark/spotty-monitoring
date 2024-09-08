docker build --platform linux/amd64 -t spotty-monitoring:latest . 
docker tag spotty-monitoring:latest repo_name/spotty-monitoring:latest
docker push repo_name/spotty-monitoring:latest