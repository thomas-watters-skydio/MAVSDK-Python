# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: poi/poi.proto
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
    b'\n\rpoi/poi.proto\x12\x0emavsdk.rpc.poi\x1a\x14mavsdk_options.proto"\x1b\n\x19SubscribePoiReportRequest">\n\x11PoiReportResponse\x12)\n\x06report\x18\x01 \x01(\x0b\x32\x19.mavsdk.rpc.poi.PoiReport"\xa7\x05\n\tPoiReport\x12\x0b\n\x03uid\x18\x01 \x01(\x04\x12\x19\n\x11time_utc_detected\x18\x02 \x01(\x04\x12\x18\n\x10time_utc_updated\x18\x03 \x01(\x04\x12\x14\n\x0ctime_boot_ms\x18\x04 \x01(\r\x12\x10\n\x08latitude\x18\x05 \x01(\x05\x12\x11\n\tlongitude\x18\x06 \x01(\x05\x12\x0f\n\x07\x61lt_msl\x18\x07 \x01(\x02\x12\x11\n\talt_ellip\x18\x08 \x01(\x02\x12\x12\n\nalt_ground\x18\t \x01(\x02\x12\x16\n\x0e\x63lassification\x18\n \x01(\r\x12\t\n\x01x\x18\x0b \x01(\x02\x12\t\n\x01y\x18\x0c \x01(\x02\x12\t\n\x01z\x18\r \x01(\x02\x12\t\n\x01q\x18\x0e \x03(\x02\x12\x0c\n\x04\x64ist\x18\x0f \x01(\x02\x12\r\n\x05vel_n\x18\x10 \x01(\x02\x12\r\n\x05vel_e\x18\x11 \x01(\x02\x12\r\n\x05vel_d\x18\x12 \x01(\x02\x12\x0b\n\x03hdg\x18\x13 \x01(\x02\x12\x0e\n\x06height\x18\x14 \x01(\x02\x12\r\n\x05width\x18\x15 \x01(\x02\x12\r\n\x05\x64\x65pth\x18\x16 \x01(\x02\x12\x1d\n\x15\x61pproach_vector_start\x18\x17 \x03(\x02\x12\x1b\n\x13\x61pproach_vector_end\x18\x18 \x03(\x02\x12\x19\n\x11\x61pproach_velocity\x18\x19 \x03(\x02\x12\x0b\n\x03ttl\x18\x1a \x01(\r\x12\x1a\n\x12\x63onfidence_overall\x18\x1b \x01(\r\x12\x1c\n\x14\x63onfidence_detection\x18\x1c \x01(\r\x12!\n\x19\x63onfidence_classification\x18\x1d \x01(\r\x12\x1f\n\x17\x63onfidence_localization\x18\x1e \x01(\r\x12\x14\n\x0cstatus_flags\x18\x1f \x01(\r\x12\x10\n\x08geometry\x18  \x01(\r\x12\x0c\n\x04name\x18! \x01(\t\x12\x13\n\x0b\x61pp6_symbol\x18" \x01(\t2t\n\nPoiService\x12\x66\n\x12SubscribePoiReport\x12).mavsdk.rpc.poi.SubscribePoiReportRequest\x1a!.mavsdk.rpc.poi.PoiReportResponse"\x00\x30\x01\x42\x19\n\rio.mavsdk.poiB\x08PoiProtob\x06proto3'
)


_SUBSCRIBEPOIREPORTREQUEST = DESCRIPTOR.message_types_by_name["SubscribePoiReportRequest"]
_POIREPORTRESPONSE = DESCRIPTOR.message_types_by_name["PoiReportResponse"]
_POIREPORT = DESCRIPTOR.message_types_by_name["PoiReport"]
SubscribePoiReportRequest = _reflection.GeneratedProtocolMessageType(
    "SubscribePoiReportRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUBSCRIBEPOIREPORTREQUEST,
        "__module__": "poi.poi_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.poi.SubscribePoiReportRequest)
    },
)
_sym_db.RegisterMessage(SubscribePoiReportRequest)

PoiReportResponse = _reflection.GeneratedProtocolMessageType(
    "PoiReportResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _POIREPORTRESPONSE,
        "__module__": "poi.poi_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.poi.PoiReportResponse)
    },
)
_sym_db.RegisterMessage(PoiReportResponse)

PoiReport = _reflection.GeneratedProtocolMessageType(
    "PoiReport",
    (_message.Message,),
    {
        "DESCRIPTOR": _POIREPORT,
        "__module__": "poi.poi_pb2"
        # @@protoc_insertion_point(class_scope:mavsdk.rpc.poi.PoiReport)
    },
)
_sym_db.RegisterMessage(PoiReport)

_POISERVICE = DESCRIPTOR.services_by_name["PoiService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\rio.mavsdk.poiB\010PoiProto"
    _SUBSCRIBEPOIREPORTREQUEST._serialized_start = 55
    _SUBSCRIBEPOIREPORTREQUEST._serialized_end = 82
    _POIREPORTRESPONSE._serialized_start = 84
    _POIREPORTRESPONSE._serialized_end = 146
    _POIREPORT._serialized_start = 149
    _POIREPORT._serialized_end = 828
    _POISERVICE._serialized_start = 830
    _POISERVICE._serialized_end = 946
# @@protoc_insertion_point(module_scope)