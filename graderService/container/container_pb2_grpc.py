# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import container.container_pb2 as container__pb2


class ContainerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateContainer = channel.unary_unary(
                '/containerService.ContainerService/CreateContainer',
                request_serializer=container__pb2.ContainerCreationResponse.SerializeToString,
                response_deserializer=container__pb2.ContainerCreationResponse.FromString,
                )
        self.DeleteContainer = channel.unary_unary(
                '/containerService.ContainerService/DeleteContainer',
                request_serializer=container__pb2.ContainerDeletionRequest.SerializeToString,
                response_deserializer=container__pb2.ContainerDeletionResponse.FromString,
                )


class ContainerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateContainer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteContainer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ContainerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateContainer': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateContainer,
                    request_deserializer=container__pb2.ContainerCreationResponse.FromString,
                    response_serializer=container__pb2.ContainerCreationResponse.SerializeToString,
            ),
            'DeleteContainer': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteContainer,
                    request_deserializer=container__pb2.ContainerDeletionRequest.FromString,
                    response_serializer=container__pb2.ContainerDeletionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'containerService.ContainerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ContainerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateContainer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerService.ContainerService/CreateContainer',
            container__pb2.ContainerCreationResponse.SerializeToString,
            container__pb2.ContainerCreationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteContainer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerService.ContainerService/DeleteContainer',
            container__pb2.ContainerDeletionRequest.SerializeToString,
            container__pb2.ContainerDeletionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
