import grpc
import container.container_pb2_grpc as pb2_grpc
import container.container_pb2 as pb2
import docker

class ContainerService(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.ContainerServiceStub(self.channel)

    def create_container(self):
        request = pb2.ContainerCreationRequest()
        return self.stub.CreateContainer(request)

    def delete_container(self, container_id):
        request = pb2.ContainerDeletionRequest(container_id=container_id)
        return self.stub.DeleteContainer(request)
