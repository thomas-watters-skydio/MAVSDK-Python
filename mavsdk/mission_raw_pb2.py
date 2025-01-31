# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mission_raw/mission_raw.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1dmission_raw/mission_raw.proto\x12\x16mavsdk.rpc.mission_raw\x1a\x14mavsdk_options.proto"R\n\x14UploadMissionRequest\x12:\n\rmission_items\x18\x01 \x03(\x0b\x32#.mavsdk.rpc.mission_raw.MissionItem"]\n\x15UploadMissionResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult"\x1c\n\x1a\x43\x61ncelMissionUploadRequest"c\n\x1b\x43\x61ncelMissionUploadResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult"\x18\n\x16\x44ownloadMissionRequest"\x9b\x01\n\x17\x44ownloadMissionResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\x12:\n\rmission_items\x18\x02 \x03(\x0b\x32#.mavsdk.rpc.mission_raw.MissionItem"\x1e\n\x1c\x43\x61ncelMissionDownloadRequest"e\n\x1d\x43\x61ncelMissionDownloadResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult"\x15\n\x13StartMissionRequest"\\\n\x14StartMissionResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult"\x15\n\x13PauseMissionRequest"\\\n\x14PauseMissionResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult"\x15\n\x13\x43learMissionRequest"\\\n\x14\x43learMissionResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult"-\n\x1cSetCurrentMissionItemRequest\x12\r\n\x05index\x18\x01 \x01(\x05"e\n\x1dSetCurrentMissionItemResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult"!\n\x1fSubscribeMissionProgressRequest"\\\n\x17MissionProgressResponse\x12\x41\n\x10mission_progress\x18\x01 \x01(\x0b\x32\'.mavsdk.rpc.mission_raw.MissionProgress" \n\x1eSubscribeMissionChangedRequest"1\n\x16MissionChangedResponse\x12\x17\n\x0fmission_changed\x18\x01 \x01(\x08";\n"ImportQgroundcontrolMissionRequest\x12\x15\n\rqgc_plan_path\x18\x01 \x01(\t"\xb3\x01\n#ImportQgroundcontrolMissionResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\x12\x46\n\x13mission_import_data\x18\x02 \x01(\x0b\x32).mavsdk.rpc.mission_raw.MissionImportData"1\n\x0fMissionProgress\x12\x0f\n\x07\x63urrent\x18\x01 \x01(\x05\x12\r\n\x05total\x18\x02 \x01(\x05"\xd8\x01\n\x0bMissionItem\x12\x0b\n\x03seq\x18\x01 \x01(\r\x12\r\n\x05\x66rame\x18\x02 \x01(\r\x12\x0f\n\x07\x63ommand\x18\x03 \x01(\r\x12\x0f\n\x07\x63urrent\x18\x04 \x01(\r\x12\x14\n\x0c\x61utocontinue\x18\x05 \x01(\r\x12\x0e\n\x06param1\x18\x06 \x01(\x02\x12\x0e\n\x06param2\x18\x07 \x01(\x02\x12\x0e\n\x06param3\x18\x08 \x01(\x02\x12\x0e\n\x06param4\x18\t \x01(\x02\x12\t\n\x01x\x18\n \x01(\x05\x12\t\n\x01y\x18\x0b \x01(\x05\x12\t\n\x01z\x18\x0c \x01(\x02\x12\x14\n\x0cmission_type\x18\r \x01(\r"\xc6\x01\n\x11MissionImportData\x12:\n\rmission_items\x18\x01 \x03(\x0b\x32#.mavsdk.rpc.mission_raw.MissionItem\x12;\n\x0egeofence_items\x18\x02 \x03(\x0b\x32#.mavsdk.rpc.mission_raw.MissionItem\x12\x38\n\x0brally_items\x18\x03 \x03(\x0b\x32#.mavsdk.rpc.mission_raw.MissionItem"\xc8\x03\n\x10MissionRawResult\x12?\n\x06result\x18\x01 \x01(\x0e\x32/.mavsdk.rpc.mission_raw.MissionRawResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t"\xde\x02\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x10\n\x0cRESULT_ERROR\x10\x02\x12!\n\x1dRESULT_TOO_MANY_MISSION_ITEMS\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x12\n\x0eRESULT_TIMEOUT\x10\x05\x12\x1b\n\x17RESULT_INVALID_ARGUMENT\x10\x06\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x07\x12\x1f\n\x1bRESULT_NO_MISSION_AVAILABLE\x10\x08\x12\x1d\n\x19RESULT_TRANSFER_CANCELLED\x10\t\x12"\n\x1eRESULT_FAILED_TO_OPEN_QGC_PLAN\x10\n\x12#\n\x1fRESULT_FAILED_TO_PARSE_QGC_PLAN\x10\x0b\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x0c\x32\x93\x0b\n\x11MissionRawService\x12n\n\rUploadMission\x12,.mavsdk.rpc.mission_raw.UploadMissionRequest\x1a-.mavsdk.rpc.mission_raw.UploadMissionResponse"\x00\x12\x84\x01\n\x13\x43\x61ncelMissionUpload\x12\x32.mavsdk.rpc.mission_raw.CancelMissionUploadRequest\x1a\x33.mavsdk.rpc.mission_raw.CancelMissionUploadResponse"\x04\x80\xb5\x18\x01\x12t\n\x0f\x44ownloadMission\x12..mavsdk.rpc.mission_raw.DownloadMissionRequest\x1a/.mavsdk.rpc.mission_raw.DownloadMissionResponse"\x00\x12\x8a\x01\n\x15\x43\x61ncelMissionDownload\x12\x34.mavsdk.rpc.mission_raw.CancelMissionDownloadRequest\x1a\x35.mavsdk.rpc.mission_raw.CancelMissionDownloadResponse"\x04\x80\xb5\x18\x01\x12k\n\x0cStartMission\x12+.mavsdk.rpc.mission_raw.StartMissionRequest\x1a,.mavsdk.rpc.mission_raw.StartMissionResponse"\x00\x12k\n\x0cPauseMission\x12+.mavsdk.rpc.mission_raw.PauseMissionRequest\x1a,.mavsdk.rpc.mission_raw.PauseMissionResponse"\x00\x12k\n\x0c\x43learMission\x12+.mavsdk.rpc.mission_raw.ClearMissionRequest\x1a,.mavsdk.rpc.mission_raw.ClearMissionResponse"\x00\x12\x86\x01\n\x15SetCurrentMissionItem\x12\x34.mavsdk.rpc.mission_raw.SetCurrentMissionItemRequest\x1a\x35.mavsdk.rpc.mission_raw.SetCurrentMissionItemResponse"\x00\x12\x88\x01\n\x18SubscribeMissionProgress\x12\x37.mavsdk.rpc.mission_raw.SubscribeMissionProgressRequest\x1a/.mavsdk.rpc.mission_raw.MissionProgressResponse"\x00\x30\x01\x12\x89\x01\n\x17SubscribeMissionChanged\x12\x36.mavsdk.rpc.mission_raw.SubscribeMissionChangedRequest\x1a..mavsdk.rpc.mission_raw.MissionChangedResponse"\x04\x80\xb5\x18\x00\x30\x01\x12\x9c\x01\n\x1bImportQgroundcontrolMission\x12:.mavsdk.rpc.mission_raw.ImportQgroundcontrolMissionRequest\x1a;.mavsdk.rpc.mission_raw.ImportQgroundcontrolMissionResponse"\x04\x80\xb5\x18\x01\x42(\n\x15io.mavsdk.mission_rawB\x0fMissionRawProtob\x06proto3'
)


_UPLOADMISSIONREQUEST = DESCRIPTOR.message_types_by_name["UploadMissionRequest"]
_UPLOADMISSIONRESPONSE = DESCRIPTOR.message_types_by_name["UploadMissionResponse"]
_CANCELMISSIONUPLOADREQUEST = DESCRIPTOR.message_types_by_name["CancelMissionUploadRequest"]
_CANCELMISSIONUPLOADRESPONSE = DESCRIPTOR.message_types_by_name["CancelMissionUploadResponse"]
_DOWNLOADMISSIONREQUEST = DESCRIPTOR.message_types_by_name["DownloadMissionRequest"]
_DOWNLOADMISSIONRESPONSE = DESCRIPTOR.message_types_by_name["DownloadMissionResponse"]
_CANCELMISSIONDOWNLOADREQUEST = DESCRIPTOR.message_types_by_name["CancelMissionDownloadRequest"]
_CANCELMISSIONDOWNLOADRESPONSE = DESCRIPTOR.message_types_by_name["CancelMissionDownloadResponse"]
_STARTMISSIONREQUEST = DESCRIPTOR.message_types_by_name["StartMissionRequest"]
_STARTMISSIONRESPONSE = DESCRIPTOR.message_types_by_name["StartMissionResponse"]
_PAUSEMISSIONREQUEST = DESCRIPTOR.message_types_by_name["PauseMissionRequest"]
_PAUSEMISSIONRESPONSE = DESCRIPTOR.message_types_by_name["PauseMissionResponse"]
_CLEARMISSIONREQUEST = DESCRIPTOR.message_types_by_name["ClearMissionRequest"]
_CLEARMISSIONRESPONSE = DESCRIPTOR.message_types_by_name["ClearMissionResponse"]
_SETCURRENTMISSIONITEMREQUEST = DESCRIPTOR.message_types_by_name["SetCurrentMissionItemRequest"]
_SETCURRENTMISSIONITEMRESPONSE = DESCRIPTOR.message_types_by_name["SetCurrentMissionItemResponse"]
_SUBSCRIBEMISSIONPROGRESSREQUEST = DESCRIPTOR.message_types_by_name[
    "SubscribeMissionProgressRequest"
]
_MISSIONPROGRESSRESPONSE = DESCRIPTOR.message_types_by_name["MissionProgressResponse"]
_SUBSCRIBEMISSIONCHANGEDREQUEST = DESCRIPTOR.message_types_by_name["SubscribeMissionChangedRequest"]
_MISSIONCHANGEDRESPONSE = DESCRIPTOR.message_types_by_name["MissionChangedResponse"]
_IMPORTQGROUNDCONTROLMISSIONREQUEST = DESCRIPTOR.message_types_by_name[
    "ImportQgroundcontrolMissionRequest"
]
_IMPORTQGROUNDCONTROLMISSIONRESPONSE = DESCRIPTOR.message_types_by_name[
    "ImportQgroundcontrolMissionResponse"
]
_MISSIONPROGRESS = DESCRIPTOR.message_types_by_name["MissionProgress"]
_MISSIONITEM = DESCRIPTOR.message_types_by_name["MissionItem"]
_MISSIONIMPORTDATA = DESCRIPTOR.message_types_by_name["MissionImportData"]
_MISSIONRAWRESULT = DESCRIPTOR.message_types_by_name["MissionRawResult"]
_MISSIONRAWRESULT_RESULT = _MISSIONRAWRESULT.enum_types_by_name["Result"]
UploadMissionRequest = _reflection.GeneratedProtocolMessageType(
    "UploadMissionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPLOADMISSIONREQUEST,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.UploadMissionRequest)
    },
)
_sym_db.RegisterMessage(UploadMissionRequest)

UploadMissionResponse = _reflection.GeneratedProtocolMessageType(
    "UploadMissionResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPLOADMISSIONRESPONSE,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.UploadMissionResponse)
    },
)
_sym_db.RegisterMessage(UploadMissionResponse)

CancelMissionUploadRequest = _reflection.GeneratedProtocolMessageType(
    "CancelMissionUploadRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELMISSIONUPLOADREQUEST,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.CancelMissionUploadRequest)
    },
)
_sym_db.RegisterMessage(CancelMissionUploadRequest)

CancelMissionUploadResponse = _reflection.GeneratedProtocolMessageType(
    "CancelMissionUploadResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELMISSIONUPLOADRESPONSE,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.CancelMissionUploadResponse)
    },
)
_sym_db.RegisterMessage(CancelMissionUploadResponse)

DownloadMissionRequest = _reflection.GeneratedProtocolMessageType(
    "DownloadMissionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DOWNLOADMISSIONREQUEST,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.DownloadMissionRequest)
    },
)
_sym_db.RegisterMessage(DownloadMissionRequest)

DownloadMissionResponse = _reflection.GeneratedProtocolMessageType(
    "DownloadMissionResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DOWNLOADMISSIONRESPONSE,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.DownloadMissionResponse)
    },
)
_sym_db.RegisterMessage(DownloadMissionResponse)

CancelMissionDownloadRequest = _reflection.GeneratedProtocolMessageType(
    "CancelMissionDownloadRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELMISSIONDOWNLOADREQUEST,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.CancelMissionDownloadRequest)
    },
)
_sym_db.RegisterMessage(CancelMissionDownloadRequest)

CancelMissionDownloadResponse = _reflection.GeneratedProtocolMessageType(
    "CancelMissionDownloadResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELMISSIONDOWNLOADRESPONSE,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.CancelMissionDownloadResponse)
    },
)
_sym_db.RegisterMessage(CancelMissionDownloadResponse)

StartMissionRequest = _reflection.GeneratedProtocolMessageType(
    "StartMissionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _STARTMISSIONREQUEST,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.StartMissionRequest)
    },
)
_sym_db.RegisterMessage(StartMissionRequest)

StartMissionResponse = _reflection.GeneratedProtocolMessageType(
    "StartMissionResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _STARTMISSIONRESPONSE,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.StartMissionResponse)
    },
)
_sym_db.RegisterMessage(StartMissionResponse)

PauseMissionRequest = _reflection.GeneratedProtocolMessageType(
    "PauseMissionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _PAUSEMISSIONREQUEST,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.PauseMissionRequest)
    },
)
_sym_db.RegisterMessage(PauseMissionRequest)

PauseMissionResponse = _reflection.GeneratedProtocolMessageType(
    "PauseMissionResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _PAUSEMISSIONRESPONSE,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.PauseMissionResponse)
    },
)
_sym_db.RegisterMessage(PauseMissionResponse)

ClearMissionRequest = _reflection.GeneratedProtocolMessageType(
    "ClearMissionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CLEARMISSIONREQUEST,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.ClearMissionRequest)
    },
)
_sym_db.RegisterMessage(ClearMissionRequest)

ClearMissionResponse = _reflection.GeneratedProtocolMessageType(
    "ClearMissionResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CLEARMISSIONRESPONSE,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.ClearMissionResponse)
    },
)
_sym_db.RegisterMessage(ClearMissionResponse)

SetCurrentMissionItemRequest = _reflection.GeneratedProtocolMessageType(
    "SetCurrentMissionItemRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETCURRENTMISSIONITEMREQUEST,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.SetCurrentMissionItemRequest)
    },
)
_sym_db.RegisterMessage(SetCurrentMissionItemRequest)

SetCurrentMissionItemResponse = _reflection.GeneratedProtocolMessageType(
    "SetCurrentMissionItemResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETCURRENTMISSIONITEMRESPONSE,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.SetCurrentMissionItemResponse)
    },
)
_sym_db.RegisterMessage(SetCurrentMissionItemResponse)

SubscribeMissionProgressRequest = _reflection.GeneratedProtocolMessageType(
    "SubscribeMissionProgressRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUBSCRIBEMISSIONPROGRESSREQUEST,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.SubscribeMissionProgressRequest)
    },
)
_sym_db.RegisterMessage(SubscribeMissionProgressRequest)

MissionProgressResponse = _reflection.GeneratedProtocolMessageType(
    "MissionProgressResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MISSIONPROGRESSRESPONSE,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.MissionProgressResponse)
    },
)
_sym_db.RegisterMessage(MissionProgressResponse)

SubscribeMissionChangedRequest = _reflection.GeneratedProtocolMessageType(
    "SubscribeMissionChangedRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUBSCRIBEMISSIONCHANGEDREQUEST,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.SubscribeMissionChangedRequest)
    },
)
_sym_db.RegisterMessage(SubscribeMissionChangedRequest)

MissionChangedResponse = _reflection.GeneratedProtocolMessageType(
    "MissionChangedResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MISSIONCHANGEDRESPONSE,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.MissionChangedResponse)
    },
)
_sym_db.RegisterMessage(MissionChangedResponse)

ImportQgroundcontrolMissionRequest = _reflection.GeneratedProtocolMessageType(
    "ImportQgroundcontrolMissionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMPORTQGROUNDCONTROLMISSIONREQUEST,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.ImportQgroundcontrolMissionRequest)
    },
)
_sym_db.RegisterMessage(ImportQgroundcontrolMissionRequest)

ImportQgroundcontrolMissionResponse = _reflection.GeneratedProtocolMessageType(
    "ImportQgroundcontrolMissionResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMPORTQGROUNDCONTROLMISSIONRESPONSE,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.ImportQgroundcontrolMissionResponse)
    },
)
_sym_db.RegisterMessage(ImportQgroundcontrolMissionResponse)

MissionProgress = _reflection.GeneratedProtocolMessageType(
    "MissionProgress",
    (_message.Message,),
    {
        "DESCRIPTOR": _MISSIONPROGRESS,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.MissionProgress)
    },
)
_sym_db.RegisterMessage(MissionProgress)

MissionItem = _reflection.GeneratedProtocolMessageType(
    "MissionItem",
    (_message.Message,),
    {
        "DESCRIPTOR": _MISSIONITEM,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.MissionItem)
    },
)
_sym_db.RegisterMessage(MissionItem)

MissionImportData = _reflection.GeneratedProtocolMessageType(
    "MissionImportData",
    (_message.Message,),
    {
        "DESCRIPTOR": _MISSIONIMPORTDATA,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.MissionImportData)
    },
)
_sym_db.RegisterMessage(MissionImportData)

MissionRawResult = _reflection.GeneratedProtocolMessageType(
    "MissionRawResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _MISSIONRAWRESULT,
        "__module__": "mission_raw.mission_raw_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.MissionRawResult)
    },
)
_sym_db.RegisterMessage(MissionRawResult)

_MISSIONRAWSERVICE = DESCRIPTOR.services_by_name["MissionRawService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\025io.mavsdk.mission_rawB\017MissionRawProto"
    _MISSIONRAWSERVICE.methods_by_name["CancelMissionUpload"]._options = None
    _MISSIONRAWSERVICE.methods_by_name[
        "CancelMissionUpload"
    ]._serialized_options = b"\200\265\030\001"
    _MISSIONRAWSERVICE.methods_by_name["CancelMissionDownload"]._options = None
    _MISSIONRAWSERVICE.methods_by_name[
        "CancelMissionDownload"
    ]._serialized_options = b"\200\265\030\001"
    _MISSIONRAWSERVICE.methods_by_name["SubscribeMissionChanged"]._options = None
    _MISSIONRAWSERVICE.methods_by_name[
        "SubscribeMissionChanged"
    ]._serialized_options = b"\200\265\030\000"
    _MISSIONRAWSERVICE.methods_by_name["ImportQgroundcontrolMission"]._options = None
    _MISSIONRAWSERVICE.methods_by_name[
        "ImportQgroundcontrolMission"
    ]._serialized_options = b"\200\265\030\001"
    _UPLOADMISSIONREQUEST._serialized_start = 79
    _UPLOADMISSIONREQUEST._serialized_end = 161
    _UPLOADMISSIONRESPONSE._serialized_start = 163
    _UPLOADMISSIONRESPONSE._serialized_end = 256
    _CANCELMISSIONUPLOADREQUEST._serialized_start = 258
    _CANCELMISSIONUPLOADREQUEST._serialized_end = 286
    _CANCELMISSIONUPLOADRESPONSE._serialized_start = 288
    _CANCELMISSIONUPLOADRESPONSE._serialized_end = 387
    _DOWNLOADMISSIONREQUEST._serialized_start = 389
    _DOWNLOADMISSIONREQUEST._serialized_end = 413
    _DOWNLOADMISSIONRESPONSE._serialized_start = 416
    _DOWNLOADMISSIONRESPONSE._serialized_end = 571
    _CANCELMISSIONDOWNLOADREQUEST._serialized_start = 573
    _CANCELMISSIONDOWNLOADREQUEST._serialized_end = 603
    _CANCELMISSIONDOWNLOADRESPONSE._serialized_start = 605
    _CANCELMISSIONDOWNLOADRESPONSE._serialized_end = 706
    _STARTMISSIONREQUEST._serialized_start = 708
    _STARTMISSIONREQUEST._serialized_end = 729
    _STARTMISSIONRESPONSE._serialized_start = 731
    _STARTMISSIONRESPONSE._serialized_end = 823
    _PAUSEMISSIONREQUEST._serialized_start = 825
    _PAUSEMISSIONREQUEST._serialized_end = 846
    _PAUSEMISSIONRESPONSE._serialized_start = 848
    _PAUSEMISSIONRESPONSE._serialized_end = 940
    _CLEARMISSIONREQUEST._serialized_start = 942
    _CLEARMISSIONREQUEST._serialized_end = 963
    _CLEARMISSIONRESPONSE._serialized_start = 965
    _CLEARMISSIONRESPONSE._serialized_end = 1057
    _SETCURRENTMISSIONITEMREQUEST._serialized_start = 1059
    _SETCURRENTMISSIONITEMREQUEST._serialized_end = 1104
    _SETCURRENTMISSIONITEMRESPONSE._serialized_start = 1106
    _SETCURRENTMISSIONITEMRESPONSE._serialized_end = 1207
    _SUBSCRIBEMISSIONPROGRESSREQUEST._serialized_start = 1209
    _SUBSCRIBEMISSIONPROGRESSREQUEST._serialized_end = 1242
    _MISSIONPROGRESSRESPONSE._serialized_start = 1244
    _MISSIONPROGRESSRESPONSE._serialized_end = 1336
    _SUBSCRIBEMISSIONCHANGEDREQUEST._serialized_start = 1338
    _SUBSCRIBEMISSIONCHANGEDREQUEST._serialized_end = 1370
    _MISSIONCHANGEDRESPONSE._serialized_start = 1372
    _MISSIONCHANGEDRESPONSE._serialized_end = 1421
    _IMPORTQGROUNDCONTROLMISSIONREQUEST._serialized_start = 1423
    _IMPORTQGROUNDCONTROLMISSIONREQUEST._serialized_end = 1482
    _IMPORTQGROUNDCONTROLMISSIONRESPONSE._serialized_start = 1485
    _IMPORTQGROUNDCONTROLMISSIONRESPONSE._serialized_end = 1664
    _MISSIONPROGRESS._serialized_start = 1666
    _MISSIONPROGRESS._serialized_end = 1715
    _MISSIONITEM._serialized_start = 1718
    _MISSIONITEM._serialized_end = 1934
    _MISSIONIMPORTDATA._serialized_start = 1937
    _MISSIONIMPORTDATA._serialized_end = 2135
    _MISSIONRAWRESULT._serialized_start = 2138
    _MISSIONRAWRESULT._serialized_end = 2594
    _MISSIONRAWRESULT_RESULT._serialized_start = 2244
    _MISSIONRAWRESULT_RESULT._serialized_end = 2594
    _MISSIONRAWSERVICE._serialized_start = 2597
    _MISSIONRAWSERVICE._serialized_end = 4024
# @@protoc_insertion_point(module_scope)
