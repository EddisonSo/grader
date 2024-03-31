import grpc
from concurrent import futures
import time
import container.container_pb2_grpc as pb2_grpc
import container.container_pb2 as pb2
import docker

client = docker.DockerClient(base_url="unix://var/run/docker.sock")

class ContainerService(pb2_grpc.ContainerServiceServicer):
    def __init__(self, *args, **kwargs):
        pass

    def CreateContainer(self, request, context):
        result = True
        
        container = client.containers.run("ubuntu:latest", detach=True, privileged=True)
        print(f"created container: {container.id}")
        
        response = {"container_id": container.id, "result":result}

        return pb2.ContainerCreationResponse(**response)

    def DeleteContainer(self, request, context):
        container_id = request.container_id
        result = True

        container = client.containers.get(container_id)
        container.remove()
        print(f"deleted container: {container.id}")

        response = {"container_id": container_id, "result":result}

        return pb2.ContainerDeletionResponse(**response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ContainerServiceServicer_to_server(ContainerService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
