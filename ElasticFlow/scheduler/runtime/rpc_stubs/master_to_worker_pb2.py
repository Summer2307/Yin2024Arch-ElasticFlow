# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: master_to_worker.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'master_to_worker.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16master_to_worker.proto\x1a\x0c\x63ommon.proto\"\xed\x01\n\x07JobInfo\x12\x10\n\x08job_name\x18\x01 \x01(\t\x12\x12\n\nbatch_size\x18\x02 \x01(\r\x12\x0e\n\x06job_id\x18\x03 \x01(\r\x12\x16\n\x0enproc_per_node\x18\x04 \x01(\r\x12\x0e\n\x06nnodes\x18\x05 \x01(\r\x12\x11\n\tnode_rank\x18\x06 \x01(\r\x12\x11\n\tmaster_ip\x18\x07 \x01(\t\x12\x13\n\x0bmaster_port\x18\x08 \x01(\r\x12\x10\n\x08gpu_list\x18\t \x01(\r\x12\x12\n\niterations\x18\n \x01(\r\x12\r\n\x05ranks\x18\x0b \x03(\r\x12\x14\n\x0c\x66rom_scratch\x18\x0c \x01(\x08\"+\n\rRunJobRequest\x12\x1a\n\x08job_info\x18\x01 \x01(\x0b\x32\x08.JobInfo\".\n\x10UpdateJobRequest\x12\x1a\n\x08job_info\x18\x01 \x01(\x0b\x32\x08.JobInfo\"D\n\x10\x42roadcastRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\r\x12\x13\n\x0bglobal_rank\x18\x02 \x01(\r\x12\x0b\n\x03src\x18\x03 \x01(\r\"N\n\x0fNewGroupRequest\x12\x0f\n\x07\x66or_ddp\x18\x01 \x01(\x08\x12\x0e\n\x06job_id\x18\x02 \x01(\r\x12\r\n\x05ranks\x18\x03 \x03(\r\x12\x0b\n\x03src\x18\x04 \x01(\r\" \n\x0eKillJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\r2\xb7\x02\n\x0eMasterToWorker\x12\"\n\x06RunJob\x12\x0e.RunJobRequest\x1a\x06.Empty\"\x00\x12(\n\tUpdateJob\x12\x11.UpdateJobRequest\x1a\x06.Empty\"\x00\x12&\n\x08NewGroup\x12\x10.NewGroupRequest\x1a\x06.Empty\"\x00\x12$\n\x07KillJob\x12\x0f.KillJobRequest\x1a\x06.Empty\"\x00\x12#\n\x0f\x42roadcastFinish\x12\x06.Empty\x1a\x06.Empty\"\x00\x12!\n\rTrainingBegin\x12\x06.Empty\x1a\x06.Empty\"\x00\x12#\n\x0fRestartTrainers\x12\x06.Empty\x1a\x06.Empty\"\x00\x12\x1c\n\x08ShutDown\x12\x06.Empty\x1a\x06.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'master_to_worker_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_JOBINFO']._serialized_start=41
  _globals['_JOBINFO']._serialized_end=278
  _globals['_RUNJOBREQUEST']._serialized_start=280
  _globals['_RUNJOBREQUEST']._serialized_end=323
  _globals['_UPDATEJOBREQUEST']._serialized_start=325
  _globals['_UPDATEJOBREQUEST']._serialized_end=371
  _globals['_BROADCASTREQUEST']._serialized_start=373
  _globals['_BROADCASTREQUEST']._serialized_end=441
  _globals['_NEWGROUPREQUEST']._serialized_start=443
  _globals['_NEWGROUPREQUEST']._serialized_end=521
  _globals['_KILLJOBREQUEST']._serialized_start=523
  _globals['_KILLJOBREQUEST']._serialized_end=555
  _globals['_MASTERTOWORKER']._serialized_start=558
  _globals['_MASTERTOWORKER']._serialized_end=869
# @@protoc_insertion_point(module_scope)
