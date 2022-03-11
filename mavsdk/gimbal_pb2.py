# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gimbal/gimbal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13gimbal/gimbal.proto\x12\x11mavsdk.rpc.gimbal";\n\x15SetPitchAndYawRequest\x12\x11\n\tpitch_deg\x18\x01 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x02 \x01(\x02"P\n\x16SetPitchAndYawResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult"Q\n\x1dSetPitchRateAndYawRateRequest\x12\x18\n\x10pitch_rate_deg_s\x18\x01 \x01(\x02\x12\x16\n\x0eyaw_rate_deg_s\x18\x02 \x01(\x02"X\n\x1eSetPitchRateAndYawRateResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult"D\n\x0eSetModeRequest\x12\x32\n\x0bgimbal_mode\x18\x01 \x01(\x0e\x32\x1d.mavsdk.rpc.gimbal.GimbalMode"I\n\x0fSetModeResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult"X\n\x15SetRoiLocationRequest\x12\x14\n\x0clatitude_deg\x18\x01 \x01(\x01\x12\x15\n\rlongitude_deg\x18\x02 \x01(\x01\x12\x12\n\naltitude_m\x18\x03 \x01(\x02"P\n\x16SetRoiLocationResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult"J\n\x12TakeControlRequest\x12\x34\n\x0c\x63ontrol_mode\x18\x01 \x01(\x0e\x32\x1e.mavsdk.rpc.gimbal.ControlMode"M\n\x13TakeControlResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult"\x17\n\x15ReleaseControlRequest"P\n\x16ReleaseControlResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult"\x19\n\x17SubscribeControlRequest"K\n\x0f\x43ontrolResponse\x12\x38\n\x0e\x63ontrol_status\x18\x01 \x01(\x0b\x32 .mavsdk.rpc.gimbal.ControlStatus"\xc7\x01\n\rControlStatus\x12\x34\n\x0c\x63ontrol_mode\x18\x01 \x01(\x0e\x32\x1e.mavsdk.rpc.gimbal.ControlMode\x12\x1d\n\x15sysid_primary_control\x18\x02 \x01(\x05\x12\x1e\n\x16\x63ompid_primary_control\x18\x03 \x01(\x05\x12\x1f\n\x17sysid_secondary_control\x18\x04 \x01(\x05\x12 \n\x18\x63ompid_secondary_control\x18\x05 \x01(\x05"\xe1\x01\n\x0cGimbalResult\x12\x36\n\x06result\x18\x01 \x01(\x0e\x32&.mavsdk.rpc.gimbal.GimbalResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t"\x84\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x10\n\x0cRESULT_ERROR\x10\x02\x12\x12\n\x0eRESULT_TIMEOUT\x10\x03\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x04\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x05*B\n\nGimbalMode\x12\x1a\n\x16GIMBAL_MODE_YAW_FOLLOW\x10\x00\x12\x18\n\x14GIMBAL_MODE_YAW_LOCK\x10\x01*Z\n\x0b\x43ontrolMode\x12\x15\n\x11\x43ONTROL_MODE_NONE\x10\x00\x12\x18\n\x14\x43ONTROL_MODE_PRIMARY\x10\x01\x12\x1a\n\x16\x43ONTROL_MODE_SECONDARY\x10\x02\x32\xe7\x05\n\rGimbalService\x12g\n\x0eSetPitchAndYaw\x12(.mavsdk.rpc.gimbal.SetPitchAndYawRequest\x1a).mavsdk.rpc.gimbal.SetPitchAndYawResponse"\x00\x12\x7f\n\x16SetPitchRateAndYawRate\x12\x30.mavsdk.rpc.gimbal.SetPitchRateAndYawRateRequest\x1a\x31.mavsdk.rpc.gimbal.SetPitchRateAndYawRateResponse"\x00\x12R\n\x07SetMode\x12!.mavsdk.rpc.gimbal.SetModeRequest\x1a".mavsdk.rpc.gimbal.SetModeResponse"\x00\x12g\n\x0eSetRoiLocation\x12(.mavsdk.rpc.gimbal.SetRoiLocationRequest\x1a).mavsdk.rpc.gimbal.SetRoiLocationResponse"\x00\x12^\n\x0bTakeControl\x12%.mavsdk.rpc.gimbal.TakeControlRequest\x1a&.mavsdk.rpc.gimbal.TakeControlResponse"\x00\x12g\n\x0eReleaseControl\x12(.mavsdk.rpc.gimbal.ReleaseControlRequest\x1a).mavsdk.rpc.gimbal.ReleaseControlResponse"\x00\x12\x66\n\x10SubscribeControl\x12*.mavsdk.rpc.gimbal.SubscribeControlRequest\x1a".mavsdk.rpc.gimbal.ControlResponse"\x00\x30\x01\x42\x1f\n\x10io.mavsdk.gimbalB\x0bGimbalProtob\x06proto3'
)

_GIMBALMODE = DESCRIPTOR.enum_types_by_name["GimbalMode"]
GimbalMode = enum_type_wrapper.EnumTypeWrapper(_GIMBALMODE)
_CONTROLMODE = DESCRIPTOR.enum_types_by_name["ControlMode"]
ControlMode = enum_type_wrapper.EnumTypeWrapper(_CONTROLMODE)
GIMBAL_MODE_YAW_FOLLOW = 0
GIMBAL_MODE_YAW_LOCK = 1
CONTROL_MODE_NONE = 0
CONTROL_MODE_PRIMARY = 1
CONTROL_MODE_SECONDARY = 2


_SETPITCHANDYAWREQUEST = DESCRIPTOR.message_types_by_name["SetPitchAndYawRequest"]
_SETPITCHANDYAWRESPONSE = DESCRIPTOR.message_types_by_name["SetPitchAndYawResponse"]
_SETPITCHRATEANDYAWRATEREQUEST = DESCRIPTOR.message_types_by_name["SetPitchRateAndYawRateRequest"]
_SETPITCHRATEANDYAWRATERESPONSE = DESCRIPTOR.message_types_by_name["SetPitchRateAndYawRateResponse"]
_SETMODEREQUEST = DESCRIPTOR.message_types_by_name["SetModeRequest"]
_SETMODERESPONSE = DESCRIPTOR.message_types_by_name["SetModeResponse"]
_SETROILOCATIONREQUEST = DESCRIPTOR.message_types_by_name["SetRoiLocationRequest"]
_SETROILOCATIONRESPONSE = DESCRIPTOR.message_types_by_name["SetRoiLocationResponse"]
_TAKECONTROLREQUEST = DESCRIPTOR.message_types_by_name["TakeControlRequest"]
_TAKECONTROLRESPONSE = DESCRIPTOR.message_types_by_name["TakeControlResponse"]
_RELEASECONTROLREQUEST = DESCRIPTOR.message_types_by_name["ReleaseControlRequest"]
_RELEASECONTROLRESPONSE = DESCRIPTOR.message_types_by_name["ReleaseControlResponse"]
_SUBSCRIBECONTROLREQUEST = DESCRIPTOR.message_types_by_name["SubscribeControlRequest"]
_CONTROLRESPONSE = DESCRIPTOR.message_types_by_name["ControlResponse"]
_CONTROLSTATUS = DESCRIPTOR.message_types_by_name["ControlStatus"]
_GIMBALRESULT = DESCRIPTOR.message_types_by_name["GimbalResult"]
_GIMBALRESULT_RESULT = _GIMBALRESULT.enum_types_by_name["Result"]
SetPitchAndYawRequest = _reflection.GeneratedProtocolMessageType(
    "SetPitchAndYawRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETPITCHANDYAWREQUEST,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetPitchAndYawRequest)
    },
)
_sym_db.RegisterMessage(SetPitchAndYawRequest)

SetPitchAndYawResponse = _reflection.GeneratedProtocolMessageType(
    "SetPitchAndYawResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETPITCHANDYAWRESPONSE,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetPitchAndYawResponse)
    },
)
_sym_db.RegisterMessage(SetPitchAndYawResponse)

SetPitchRateAndYawRateRequest = _reflection.GeneratedProtocolMessageType(
    "SetPitchRateAndYawRateRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETPITCHRATEANDYAWRATEREQUEST,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetPitchRateAndYawRateRequest)
    },
)
_sym_db.RegisterMessage(SetPitchRateAndYawRateRequest)

SetPitchRateAndYawRateResponse = _reflection.GeneratedProtocolMessageType(
    "SetPitchRateAndYawRateResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETPITCHRATEANDYAWRATERESPONSE,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetPitchRateAndYawRateResponse)
    },
)
_sym_db.RegisterMessage(SetPitchRateAndYawRateResponse)

SetModeRequest = _reflection.GeneratedProtocolMessageType(
    "SetModeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETMODEREQUEST,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetModeRequest)
    },
)
_sym_db.RegisterMessage(SetModeRequest)

SetModeResponse = _reflection.GeneratedProtocolMessageType(
    "SetModeResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETMODERESPONSE,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetModeResponse)
    },
)
_sym_db.RegisterMessage(SetModeResponse)

SetRoiLocationRequest = _reflection.GeneratedProtocolMessageType(
    "SetRoiLocationRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETROILOCATIONREQUEST,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetRoiLocationRequest)
    },
)
_sym_db.RegisterMessage(SetRoiLocationRequest)

SetRoiLocationResponse = _reflection.GeneratedProtocolMessageType(
    "SetRoiLocationResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETROILOCATIONRESPONSE,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetRoiLocationResponse)
    },
)
_sym_db.RegisterMessage(SetRoiLocationResponse)

TakeControlRequest = _reflection.GeneratedProtocolMessageType(
    "TakeControlRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TAKECONTROLREQUEST,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.TakeControlRequest)
    },
)
_sym_db.RegisterMessage(TakeControlRequest)

TakeControlResponse = _reflection.GeneratedProtocolMessageType(
    "TakeControlResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TAKECONTROLRESPONSE,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.TakeControlResponse)
    },
)
_sym_db.RegisterMessage(TakeControlResponse)

ReleaseControlRequest = _reflection.GeneratedProtocolMessageType(
    "ReleaseControlRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _RELEASECONTROLREQUEST,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.ReleaseControlRequest)
    },
)
_sym_db.RegisterMessage(ReleaseControlRequest)

ReleaseControlResponse = _reflection.GeneratedProtocolMessageType(
    "ReleaseControlResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _RELEASECONTROLRESPONSE,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.ReleaseControlResponse)
    },
)
_sym_db.RegisterMessage(ReleaseControlResponse)

SubscribeControlRequest = _reflection.GeneratedProtocolMessageType(
    "SubscribeControlRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUBSCRIBECONTROLREQUEST,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SubscribeControlRequest)
    },
)
_sym_db.RegisterMessage(SubscribeControlRequest)

ControlResponse = _reflection.GeneratedProtocolMessageType(
    "ControlResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTROLRESPONSE,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.ControlResponse)
    },
)
_sym_db.RegisterMessage(ControlResponse)

ControlStatus = _reflection.GeneratedProtocolMessageType(
    "ControlStatus",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTROLSTATUS,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.ControlStatus)
    },
)
_sym_db.RegisterMessage(ControlStatus)

GimbalResult = _reflection.GeneratedProtocolMessageType(
    "GimbalResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _GIMBALRESULT,
        "__module__": "gimbal.gimbal_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.GimbalResult)
    },
)
_sym_db.RegisterMessage(GimbalResult)

_GIMBALSERVICE = DESCRIPTOR.services_by_name["GimbalService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\020io.mavsdk.gimbalB\013GimbalProto"
    _GIMBALMODE._serialized_start = 1471
    _GIMBALMODE._serialized_end = 1537
    _CONTROLMODE._serialized_start = 1539
    _CONTROLMODE._serialized_end = 1629
    _SETPITCHANDYAWREQUEST._serialized_start = 42
    _SETPITCHANDYAWREQUEST._serialized_end = 101
    _SETPITCHANDYAWRESPONSE._serialized_start = 103
    _SETPITCHANDYAWRESPONSE._serialized_end = 183
    _SETPITCHRATEANDYAWRATEREQUEST._serialized_start = 185
    _SETPITCHRATEANDYAWRATEREQUEST._serialized_end = 266
    _SETPITCHRATEANDYAWRATERESPONSE._serialized_start = 268
    _SETPITCHRATEANDYAWRATERESPONSE._serialized_end = 356
    _SETMODEREQUEST._serialized_start = 358
    _SETMODEREQUEST._serialized_end = 426
    _SETMODERESPONSE._serialized_start = 428
    _SETMODERESPONSE._serialized_end = 501
    _SETROILOCATIONREQUEST._serialized_start = 503
    _SETROILOCATIONREQUEST._serialized_end = 591
    _SETROILOCATIONRESPONSE._serialized_start = 593
    _SETROILOCATIONRESPONSE._serialized_end = 673
    _TAKECONTROLREQUEST._serialized_start = 675
    _TAKECONTROLREQUEST._serialized_end = 749
    _TAKECONTROLRESPONSE._serialized_start = 751
    _TAKECONTROLRESPONSE._serialized_end = 828
    _RELEASECONTROLREQUEST._serialized_start = 830
    _RELEASECONTROLREQUEST._serialized_end = 853
    _RELEASECONTROLRESPONSE._serialized_start = 855
    _RELEASECONTROLRESPONSE._serialized_end = 935
    _SUBSCRIBECONTROLREQUEST._serialized_start = 937
    _SUBSCRIBECONTROLREQUEST._serialized_end = 962
    _CONTROLRESPONSE._serialized_start = 964
    _CONTROLRESPONSE._serialized_end = 1039
    _CONTROLSTATUS._serialized_start = 1042
    _CONTROLSTATUS._serialized_end = 1241
    _GIMBALRESULT._serialized_start = 1244
    _GIMBALRESULT._serialized_end = 1469
    _GIMBALRESULT_RESULT._serialized_start = 1337
    _GIMBALRESULT_RESULT._serialized_end = 1469
    _GIMBALSERVICE._serialized_start = 1632
    _GIMBALSERVICE._serialized_end = 2375
# @@protoc_insertion_point(module_scope)
