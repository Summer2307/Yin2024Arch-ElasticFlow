# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import common_pb2 as common__pb2
import scheduler_to_master_pb2 as scheduler__to__master__pb2

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
        + f' but the generated code in scheduler_to_master_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SchedulerToMasterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Schedule = channel.unary_unary(
                '/SchedulerToMaster/Schedule',
                request_serializer=scheduler__to__master__pb2.ScheduleRequest.SerializeToString,
                response_deserializer=scheduler__to__master__pb2.ScheduleResponse.FromString,
                _registered_method=True)
        self.BroadcastFinish = channel.unary_unary(
                '/SchedulerToMaster/BroadcastFinish',
                request_serializer=common__pb2.Empty.SerializeToString,
                response_deserializer=common__pb2.Empty.FromString,
                _registered_method=True)
        self.TrainingBegin = channel.unary_unary(
                '/SchedulerToMaster/TrainingBegin',
                request_serializer=common__pb2.Empty.SerializeToString,
                response_deserializer=common__pb2.Empty.FromString,
                _registered_method=True)


class SchedulerToMasterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Schedule(self, request, context):
        """Send scheduling results to master
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BroadcastFinish(self, request, context):
        """send broadcast finish message to workers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TrainingBegin(self, request, context):
        """send train begin message to workers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SchedulerToMasterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Schedule': grpc.unary_unary_rpc_method_handler(
                    servicer.Schedule,
                    request_deserializer=scheduler__to__master__pb2.ScheduleRequest.FromString,
                    response_serializer=scheduler__to__master__pb2.ScheduleResponse.SerializeToString,
            ),
            'BroadcastFinish': grpc.unary_unary_rpc_method_handler(
                    servicer.BroadcastFinish,
                    request_deserializer=common__pb2.Empty.FromString,
                    response_serializer=common__pb2.Empty.SerializeToString,
            ),
            'TrainingBegin': grpc.unary_unary_rpc_method_handler(
                    servicer.TrainingBegin,
                    request_deserializer=common__pb2.Empty.FromString,
                    response_serializer=common__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SchedulerToMaster', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('SchedulerToMaster', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SchedulerToMaster(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Schedule(request,
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
            '/SchedulerToMaster/Schedule',
            scheduler__to__master__pb2.ScheduleRequest.SerializeToString,
            scheduler__to__master__pb2.ScheduleResponse.FromString,
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
    def BroadcastFinish(request,
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
            '/SchedulerToMaster/BroadcastFinish',
            common__pb2.Empty.SerializeToString,
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
    def TrainingBegin(request,
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
            '/SchedulerToMaster/TrainingBegin',
            common__pb2.Empty.SerializeToString,
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
