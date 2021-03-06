# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: katib.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='katib.proto',
  package='api.v1.alpha3',
  syntax='proto3',
  serialized_pb=_b('\n\x0bkatib.proto\x12\rapi.v1.alpha3\x1a\x1cgoogle/api/annotations.proto\"\x1c\n\x1aGetKatibSuggestionsRequest\"\x1a\n\x18GetKatibSuggestionsReply2w\n\x0fKatibSuggestion\x12\x64\n\x0eGetSuggestions\x12).api.v1.alpha3.GetKatibSuggestionsRequest\x1a\'.api.v1.alpha3.GetKatibSuggestionsReplyb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETKATIBSUGGESTIONSREQUEST = _descriptor.Descriptor(
  name='GetKatibSuggestionsRequest',
  full_name='api.v1.alpha3.GetKatibSuggestionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=88,
)


_GETKATIBSUGGESTIONSREPLY = _descriptor.Descriptor(
  name='GetKatibSuggestionsReply',
  full_name='api.v1.alpha3.GetKatibSuggestionsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=116,
)

DESCRIPTOR.message_types_by_name['GetKatibSuggestionsRequest'] = _GETKATIBSUGGESTIONSREQUEST
DESCRIPTOR.message_types_by_name['GetKatibSuggestionsReply'] = _GETKATIBSUGGESTIONSREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetKatibSuggestionsRequest = _reflection.GeneratedProtocolMessageType('GetKatibSuggestionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETKATIBSUGGESTIONSREQUEST,
  __module__ = 'katib_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.GetKatibSuggestionsRequest)
  ))
_sym_db.RegisterMessage(GetKatibSuggestionsRequest)

GetKatibSuggestionsReply = _reflection.GeneratedProtocolMessageType('GetKatibSuggestionsReply', (_message.Message,), dict(
  DESCRIPTOR = _GETKATIBSUGGESTIONSREPLY,
  __module__ = 'katib_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.GetKatibSuggestionsReply)
  ))
_sym_db.RegisterMessage(GetKatibSuggestionsReply)



_KATIBSUGGESTION = _descriptor.ServiceDescriptor(
  name='KatibSuggestion',
  full_name='api.v1.alpha3.KatibSuggestion',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=118,
  serialized_end=237,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSuggestions',
    full_name='api.v1.alpha3.KatibSuggestion.GetSuggestions',
    index=0,
    containing_service=None,
    input_type=_GETKATIBSUGGESTIONSREQUEST,
    output_type=_GETKATIBSUGGESTIONSREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_KATIBSUGGESTION)

DESCRIPTOR.services_by_name['KatibSuggestion'] = _KATIBSUGGESTION

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class KatibSuggestionStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetSuggestions = channel.unary_unary(
          '/api.v1.alpha3.KatibSuggestion/GetSuggestions',
          request_serializer=GetKatibSuggestionsRequest.SerializeToString,
          response_deserializer=GetKatibSuggestionsReply.FromString,
          )


  class KatibSuggestionServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def GetSuggestions(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_KatibSuggestionServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetSuggestions': grpc.unary_unary_rpc_method_handler(
            servicer.GetSuggestions,
            request_deserializer=GetKatibSuggestionsRequest.FromString,
            response_serializer=GetKatibSuggestionsReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'api.v1.alpha3.KatibSuggestion', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaKatibSuggestionServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def GetSuggestions(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaKatibSuggestionStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def GetSuggestions(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    GetSuggestions.future = None


  def beta_create_KatibSuggestion_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('api.v1.alpha3.KatibSuggestion', 'GetSuggestions'): GetKatibSuggestionsRequest.FromString,
    }
    response_serializers = {
      ('api.v1.alpha3.KatibSuggestion', 'GetSuggestions'): GetKatibSuggestionsReply.SerializeToString,
    }
    method_implementations = {
      ('api.v1.alpha3.KatibSuggestion', 'GetSuggestions'): face_utilities.unary_unary_inline(servicer.GetSuggestions),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_KatibSuggestion_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('api.v1.alpha3.KatibSuggestion', 'GetSuggestions'): GetKatibSuggestionsRequest.SerializeToString,
    }
    response_deserializers = {
      ('api.v1.alpha3.KatibSuggestion', 'GetSuggestions'): GetKatibSuggestionsReply.FromString,
    }
    cardinalities = {
      'GetSuggestions': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'api.v1.alpha3.KatibSuggestion', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
