#TUTORIAL FOR CONTINUOUS DEPLOYMENT WITH MULTIPLE MICRO SERVICES

#build docker image from within this directory:
#docker build -t leesimage .

#Run:
#docker run -p 5000:5000 --rm leesimage

#test from another terminal:
#curl -X POST -i http://127.0.0.1:5000/register -d '{"username":"lee","pwd":"pass"}' -H'content-type: application/json'
#expect good response
#curl -X POST -i http://127.0.0.1:5000/register -d '{"username":"lee","pwd":"pass"}' -H'content-type: application/json'
#expect error from reuse user

#curl -X POST -i http://127.0.0.1:5000/login -d '{"username":"lee","pwd":"pass"}' -H'content-type: application/json'
#expect to receive session id