# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import common_pb2 as common__pb2
import trainer_to_scheduler_pb2 as trainer__to__scheduler__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in trainer_to_scheduler_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TrainerToSchedulerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReportStable = channel.unary_unary(
                '/TrainerToScheduler/ReportStable',
                request_serializer=trainer__to__scheduler__pb2.ReportStableRequest.SerializeToString,
                response_deserializer=common__pb2.Empty.FromString,
                _registered_method=True)
        self.ReportReady = channel.unary_unary(
                '/TrainerToScheduler/ReportReady',
                request_serializer=trainer__to__scheduler__pb2.ReportReadyRequest.SerializeToString,
                response_deserializer=common__pb2.Empty.FromString,
                _registered_method=True)


class TrainerToSchedulerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReportStable(self, request, context):
        """Report to scheduler that the job is training stable
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportReady(self, request, context):
        """Report to scheduler that the job is training ready
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrainerToSchedulerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReportStable': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportStable,
                    request_deserializer=trainer__to__scheduler__pb2.ReportStableRequest.FromString,
                    response_serializer=common__pb2.Empty.SerializeToString,
            ),
            'ReportReady': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportReady,
                    request_deserializer=trainer__to__scheduler__pb2.ReportReadyRequest.FromString,
                    response_serializer=common__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TrainerToScheduler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('TrainerToScheduler', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TrainerToScheduler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReportStable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/TrainerToScheduler/ReportStable',
            trainer__to__scheduler__pb2.ReportStableRequest.SerializeToString,
            common__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReportReady(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/TrainerToScheduler/ReportReady',
            trainer__to__scheduler__pb2.ReportReadyRequest.SerializeToString,
            common__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)