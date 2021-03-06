# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpcdemo_pb2 as grpcdemo__pb2


class GrpcDemoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NoParamFunc = channel.unary_unary(
                '/grpcdemopb.GrpcDemo/NoParamFunc',
                request_serializer=grpcdemo__pb2.Empty.SerializeToString,
                response_deserializer=grpcdemo__pb2.Empty.FromString,
                )
        self.UnaryFunc = channel.unary_unary(
                '/grpcdemopb.GrpcDemo/UnaryFunc',
                request_serializer=grpcdemo__pb2.UnaryFuncRequest.SerializeToString,
                response_deserializer=grpcdemo__pb2.UnaryFuncResponse.FromString,
                )


class GrpcDemoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def NoParamFunc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnaryFunc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GrpcDemoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NoParamFunc': grpc.unary_unary_rpc_method_handler(
                    servicer.NoParamFunc,
                    request_deserializer=grpcdemo__pb2.Empty.FromString,
                    response_serializer=grpcdemo__pb2.Empty.SerializeToString,
            ),
            'UnaryFunc': grpc.unary_unary_rpc_method_handler(
                    servicer.UnaryFunc,
                    request_deserializer=grpcdemo__pb2.UnaryFuncRequest.FromString,
                    response_serializer=grpcdemo__pb2.UnaryFuncResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpcdemopb.GrpcDemo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GrpcDemo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def NoParamFunc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcdemopb.GrpcDemo/NoParamFunc',
            grpcdemo__pb2.Empty.SerializeToString,
            grpcdemo__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnaryFunc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcdemopb.GrpcDemo/UnaryFunc',
            grpcdemo__pb2.UnaryFuncRequest.SerializeToString,
            grpcdemo__pb2.UnaryFuncResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
