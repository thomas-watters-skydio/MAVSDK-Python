# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import poi_pb2 as poi_dot_poi__pb2


class PoiServiceStub(object):
    """
    Allow users to get poi information
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribePoiReport = channel.unary_stream(
            "/mavsdk.rpc.poi.PoiService/SubscribePoiReport",
            request_serializer=poi_dot_poi__pb2.SubscribePoiReportRequest.SerializeToString,
            response_deserializer=poi_dot_poi__pb2.PoiReportResponse.FromString,
        )


class PoiServiceServicer(object):
    """
    Allow users to get poi information
    """

    def SubscribePoiReport(self, request, context):
        """Subscribe to 'poi' updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PoiServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SubscribePoiReport": grpc.unary_stream_rpc_method_handler(
            servicer.SubscribePoiReport,
            request_deserializer=poi_dot_poi__pb2.SubscribePoiReportRequest.FromString,
            response_serializer=poi_dot_poi__pb2.PoiReportResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "mavsdk.rpc.poi.PoiService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PoiService(object):
    """
    Allow users to get poi information
    """

    @staticmethod
    def SubscribePoiReport(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/mavsdk.rpc.poi.PoiService/SubscribePoiReport",
            poi_dot_poi__pb2.SubscribePoiReportRequest.SerializeToString,
            poi_dot_poi__pb2.PoiReportResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
