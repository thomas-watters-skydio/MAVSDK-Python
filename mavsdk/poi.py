# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import poi_pb2, poi_pb2_grpc
from enum import Enum


class PoiReport:
    """
 

     Parameters
     ----------
     uid : uint64_t
         
     time_utc_detected : uint64_t
         
     time_utc_updated : uint64_t
         
     time_boot_ms : uint32_t
         
     latitude : int32_t
         
     longitude : int32_t
         
     alt_msl : float
         
     alt_ellip : float
         
     alt_ground : float
         
     classification : uint32_t
         
     x : float
         
     y : float
         
     z : float
         
     q : [float]
         
     dist : float
         
     vel_n : float
         
     vel_e : float
         
     vel_d : float
         
     hdg : float
         
     height : float
         
     width : float
         
     depth : float
         
     approach_vector_start : [float]
         
     approach_vector_end : [float]
         
     approach_velocity : [float]
         
     ttl : uint32_t
          actually uint16

     confidence_overall : uint32_t
          actually uint8

     confidence_detection : uint32_t
          actually uint8

     confidence_classification : uint32_t
          actually uint8

     confidence_localization : uint32_t
          actually uint8

     status_flags : uint32_t
          actually uint8

     geometry : uint32_t
          actually uint8

     name : std::string
          32 byte string

     app6_symbol : std::string
          31 byte string

     """

    def __init__(
        self,
        uid,
        time_utc_detected,
        time_utc_updated,
        time_boot_ms,
        latitude,
        longitude,
        alt_msl,
        alt_ellip,
        alt_ground,
        classification,
        x,
        y,
        z,
        q,
        dist,
        vel_n,
        vel_e,
        vel_d,
        hdg,
        height,
        width,
        depth,
        approach_vector_start,
        approach_vector_end,
        approach_velocity,
        ttl,
        confidence_overall,
        confidence_detection,
        confidence_classification,
        confidence_localization,
        status_flags,
        geometry,
        name,
        app6_symbol,
    ):
        """ Initializes the PoiReport object """
        self.uid = uid
        self.time_utc_detected = time_utc_detected
        self.time_utc_updated = time_utc_updated
        self.time_boot_ms = time_boot_ms
        self.latitude = latitude
        self.longitude = longitude
        self.alt_msl = alt_msl
        self.alt_ellip = alt_ellip
        self.alt_ground = alt_ground
        self.classification = classification
        self.x = x
        self.y = y
        self.z = z
        self.q = q
        self.dist = dist
        self.vel_n = vel_n
        self.vel_e = vel_e
        self.vel_d = vel_d
        self.hdg = hdg
        self.height = height
        self.width = width
        self.depth = depth
        self.approach_vector_start = approach_vector_start
        self.approach_vector_end = approach_vector_end
        self.approach_velocity = approach_velocity
        self.ttl = ttl
        self.confidence_overall = confidence_overall
        self.confidence_detection = confidence_detection
        self.confidence_classification = confidence_classification
        self.confidence_localization = confidence_localization
        self.status_flags = status_flags
        self.geometry = geometry
        self.name = name
        self.app6_symbol = app6_symbol

    def __eq__(self, to_compare):
        """ Checks if two PoiReport are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # PoiReport object
            return (
                (self.uid == to_compare.uid)
                and (self.time_utc_detected == to_compare.time_utc_detected)
                and (self.time_utc_updated == to_compare.time_utc_updated)
                and (self.time_boot_ms == to_compare.time_boot_ms)
                and (self.latitude == to_compare.latitude)
                and (self.longitude == to_compare.longitude)
                and (self.alt_msl == to_compare.alt_msl)
                and (self.alt_ellip == to_compare.alt_ellip)
                and (self.alt_ground == to_compare.alt_ground)
                and (self.classification == to_compare.classification)
                and (self.x == to_compare.x)
                and (self.y == to_compare.y)
                and (self.z == to_compare.z)
                and (self.q == to_compare.q)
                and (self.dist == to_compare.dist)
                and (self.vel_n == to_compare.vel_n)
                and (self.vel_e == to_compare.vel_e)
                and (self.vel_d == to_compare.vel_d)
                and (self.hdg == to_compare.hdg)
                and (self.height == to_compare.height)
                and (self.width == to_compare.width)
                and (self.depth == to_compare.depth)
                and (self.approach_vector_start == to_compare.approach_vector_start)
                and (self.approach_vector_end == to_compare.approach_vector_end)
                and (self.approach_velocity == to_compare.approach_velocity)
                and (self.ttl == to_compare.ttl)
                and (self.confidence_overall == to_compare.confidence_overall)
                and (self.confidence_detection == to_compare.confidence_detection)
                and (self.confidence_classification == to_compare.confidence_classification)
                and (self.confidence_localization == to_compare.confidence_localization)
                and (self.status_flags == to_compare.status_flags)
                and (self.geometry == to_compare.geometry)
                and (self.name == to_compare.name)
                and (self.app6_symbol == to_compare.app6_symbol)
            )

        except AttributeError:
            return False

    def __str__(self):
        """ PoiReport in string representation """
        struct_repr = ", ".join(
            [
                "uid: " + str(self.uid),
                "time_utc_detected: " + str(self.time_utc_detected),
                "time_utc_updated: " + str(self.time_utc_updated),
                "time_boot_ms: " + str(self.time_boot_ms),
                "latitude: " + str(self.latitude),
                "longitude: " + str(self.longitude),
                "alt_msl: " + str(self.alt_msl),
                "alt_ellip: " + str(self.alt_ellip),
                "alt_ground: " + str(self.alt_ground),
                "classification: " + str(self.classification),
                "x: " + str(self.x),
                "y: " + str(self.y),
                "z: " + str(self.z),
                "q: " + str(self.q),
                "dist: " + str(self.dist),
                "vel_n: " + str(self.vel_n),
                "vel_e: " + str(self.vel_e),
                "vel_d: " + str(self.vel_d),
                "hdg: " + str(self.hdg),
                "height: " + str(self.height),
                "width: " + str(self.width),
                "depth: " + str(self.depth),
                "approach_vector_start: " + str(self.approach_vector_start),
                "approach_vector_end: " + str(self.approach_vector_end),
                "approach_velocity: " + str(self.approach_velocity),
                "ttl: " + str(self.ttl),
                "confidence_overall: " + str(self.confidence_overall),
                "confidence_detection: " + str(self.confidence_detection),
                "confidence_classification: " + str(self.confidence_classification),
                "confidence_localization: " + str(self.confidence_localization),
                "status_flags: " + str(self.status_flags),
                "geometry: " + str(self.geometry),
                "name: " + str(self.name),
                "app6_symbol: " + str(self.app6_symbol),
            ]
        )

        return f"PoiReport: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPoiReport):
        """ Translates a gRPC struct to the SDK equivalent """
        return PoiReport(
            rpcPoiReport.uid,
            rpcPoiReport.time_utc_detected,
            rpcPoiReport.time_utc_updated,
            rpcPoiReport.time_boot_ms,
            rpcPoiReport.latitude,
            rpcPoiReport.longitude,
            rpcPoiReport.alt_msl,
            rpcPoiReport.alt_ellip,
            rpcPoiReport.alt_ground,
            rpcPoiReport.classification,
            rpcPoiReport.x,
            rpcPoiReport.y,
            rpcPoiReport.z,
            rpcPoiReport.q,
            rpcPoiReport.dist,
            rpcPoiReport.vel_n,
            rpcPoiReport.vel_e,
            rpcPoiReport.vel_d,
            rpcPoiReport.hdg,
            rpcPoiReport.height,
            rpcPoiReport.width,
            rpcPoiReport.depth,
            rpcPoiReport.approach_vector_start,
            rpcPoiReport.approach_vector_end,
            rpcPoiReport.approach_velocity,
            rpcPoiReport.ttl,
            rpcPoiReport.confidence_overall,
            rpcPoiReport.confidence_detection,
            rpcPoiReport.confidence_classification,
            rpcPoiReport.confidence_localization,
            rpcPoiReport.status_flags,
            rpcPoiReport.geometry,
            rpcPoiReport.name,
            rpcPoiReport.app6_symbol,
        )

    def translate_to_rpc(self, rpcPoiReport):
        """ Translates this SDK object into its gRPC equivalent """

        rpcPoiReport.uid = self.uid

        rpcPoiReport.time_utc_detected = self.time_utc_detected

        rpcPoiReport.time_utc_updated = self.time_utc_updated

        rpcPoiReport.time_boot_ms = self.time_boot_ms

        rpcPoiReport.latitude = self.latitude

        rpcPoiReport.longitude = self.longitude

        rpcPoiReport.alt_msl = self.alt_msl

        rpcPoiReport.alt_ellip = self.alt_ellip

        rpcPoiReport.alt_ground = self.alt_ground

        rpcPoiReport.classification = self.classification

        rpcPoiReport.x = self.x

        rpcPoiReport.y = self.y

        rpcPoiReport.z = self.z

        for elem in self.q:
            rpcPoiReport.q.append(elem)

        rpcPoiReport.dist = self.dist

        rpcPoiReport.vel_n = self.vel_n

        rpcPoiReport.vel_e = self.vel_e

        rpcPoiReport.vel_d = self.vel_d

        rpcPoiReport.hdg = self.hdg

        rpcPoiReport.height = self.height

        rpcPoiReport.width = self.width

        rpcPoiReport.depth = self.depth

        for elem in self.approach_vector_start:
            rpcPoiReport.approach_vector_start.append(elem)

        for elem in self.approach_vector_end:
            rpcPoiReport.approach_vector_end.append(elem)

        for elem in self.approach_velocity:
            rpcPoiReport.approach_velocity.append(elem)

        rpcPoiReport.ttl = self.ttl

        rpcPoiReport.confidence_overall = self.confidence_overall

        rpcPoiReport.confidence_detection = self.confidence_detection

        rpcPoiReport.confidence_classification = self.confidence_classification

        rpcPoiReport.confidence_localization = self.confidence_localization

        rpcPoiReport.status_flags = self.status_flags

        rpcPoiReport.geometry = self.geometry

        rpcPoiReport.name = self.name

        rpcPoiReport.app6_symbol = self.app6_symbol


class Poi(AsyncBase):
    """
     Allow users to get poi information

     Generated by dcsdkgen - MAVSDK Poi API
    """

    # Plugin name
    name = "Poi"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = poi_pb2_grpc.PoiServiceStub(channel)

    async def poi_report(self):
        """
         Subscribe to 'poi' updates.

         Yields
         -------
         report : PoiReport
             
         
        """

        request = poi_pb2.SubscribePoiReportRequest()
        poi_report_stream = self._stub.SubscribePoiReport(request)

        try:
            async for response in poi_report_stream:

                yield PoiReport.translate_from_rpc(response.report)
        finally:
            poi_report_stream.cancel()
