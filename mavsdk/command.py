# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import command_pb2, command_pb2_grpc
from enum import Enum


class CommandLong:
    """
 

     Parameters
     ----------
     target_system : uint32_t
          actually uint8

     target_component : uint32_t
          actually uint8

     command : uint32_t
          actually uint16

     confirmation : uint32_t
          actually uint8

     param1 : float
          PARAM1, see MAV_CMD enum

     param2 : float
          PARAM2, see MAV_CMD enum

     param3 : float
          PARAM3, see MAV_CMD enum

     param4 : float
          PARAM4, see MAV_CMD enum

     param5 : float
          PARAM5, see MAV_CMD enum

     param6 : float
          PARAM6, see MAV_CMD enum

     param7 : float
          PARAM7, see MAV_CMD enum

     """

    def __init__(
        self,
        target_system,
        target_component,
        command,
        confirmation,
        param1,
        param2,
        param3,
        param4,
        param5,
        param6,
        param7,
    ):
        """ Initializes the CommandLong object """
        self.target_system = target_system
        self.target_component = target_component
        self.command = command
        self.confirmation = confirmation
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.param5 = param5
        self.param6 = param6
        self.param7 = param7

    def __eq__(self, to_compare):
        """ Checks if two CommandLong are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # CommandLong object
            return (
                (self.target_system == to_compare.target_system)
                and (self.target_component == to_compare.target_component)
                and (self.command == to_compare.command)
                and (self.confirmation == to_compare.confirmation)
                and (self.param1 == to_compare.param1)
                and (self.param2 == to_compare.param2)
                and (self.param3 == to_compare.param3)
                and (self.param4 == to_compare.param4)
                and (self.param5 == to_compare.param5)
                and (self.param6 == to_compare.param6)
                and (self.param7 == to_compare.param7)
            )

        except AttributeError:
            return False

    def __str__(self):
        """ CommandLong in string representation """
        struct_repr = ", ".join(
            [
                "target_system: " + str(self.target_system),
                "target_component: " + str(self.target_component),
                "command: " + str(self.command),
                "confirmation: " + str(self.confirmation),
                "param1: " + str(self.param1),
                "param2: " + str(self.param2),
                "param3: " + str(self.param3),
                "param4: " + str(self.param4),
                "param5: " + str(self.param5),
                "param6: " + str(self.param6),
                "param7: " + str(self.param7),
            ]
        )

        return f"CommandLong: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcCommandLong):
        """ Translates a gRPC struct to the SDK equivalent """
        return CommandLong(
            rpcCommandLong.target_system,
            rpcCommandLong.target_component,
            rpcCommandLong.command,
            rpcCommandLong.confirmation,
            rpcCommandLong.param1,
            rpcCommandLong.param2,
            rpcCommandLong.param3,
            rpcCommandLong.param4,
            rpcCommandLong.param5,
            rpcCommandLong.param6,
            rpcCommandLong.param7,
        )

    def translate_to_rpc(self, rpcCommandLong):
        """ Translates this SDK object into its gRPC equivalent """

        rpcCommandLong.target_system = self.target_system

        rpcCommandLong.target_component = self.target_component

        rpcCommandLong.command = self.command

        rpcCommandLong.confirmation = self.confirmation

        rpcCommandLong.param1 = self.param1

        rpcCommandLong.param2 = self.param2

        rpcCommandLong.param3 = self.param3

        rpcCommandLong.param4 = self.param4

        rpcCommandLong.param5 = self.param5

        rpcCommandLong.param6 = self.param6

        rpcCommandLong.param7 = self.param7


class CommandResult:
    """
 

     Parameters
     ----------
     result : Result
         
     result_str : std::string
         
     """

    class Result(Enum):
        """
     

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request was successful

         NO_SYSTEM
              No system is connected

         CONNECTION_ERROR
              Connection error

         BUSY
              Vehicle is busy

         COMMAND_DENIED
              Command refused by vehicle

         COMMAND_DENIED_LANDED_STATE_UNKNOWN
              Command refused because landed state is unknown

         COMMAND_DENIED_NOT_LANDED
              Command refused because vehicle not landed

         TIMEOUT
              Request timed out

         VTOL_TRANSITION_SUPPORT_UNKNOWN
              Hybrid/VTOL transition support is unknown

         NO_VTOL_TRANSITION_SUPPORT
              Vehicle does not support hybrid/VTOL transitions

         PARAMETER_ERROR
              Error getting or setting parameter

         UNSUPPORTED
              Action not supported

         """

        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        COMMAND_DENIED = 5
        COMMAND_DENIED_LANDED_STATE_UNKNOWN = 6
        COMMAND_DENIED_NOT_LANDED = 7
        TIMEOUT = 8
        VTOL_TRANSITION_SUPPORT_UNKNOWN = 9
        NO_VTOL_TRANSITION_SUPPORT = 10
        PARAMETER_ERROR = 11
        UNSUPPORTED = 12

        def translate_to_rpc(self):
            if self == CommandResult.Result.UNKNOWN:
                return command_pb2.CommandResult.RESULT_UNKNOWN
            if self == CommandResult.Result.SUCCESS:
                return command_pb2.CommandResult.RESULT_SUCCESS
            if self == CommandResult.Result.NO_SYSTEM:
                return command_pb2.CommandResult.RESULT_NO_SYSTEM
            if self == CommandResult.Result.CONNECTION_ERROR:
                return command_pb2.CommandResult.RESULT_CONNECTION_ERROR
            if self == CommandResult.Result.BUSY:
                return command_pb2.CommandResult.RESULT_BUSY
            if self == CommandResult.Result.COMMAND_DENIED:
                return command_pb2.CommandResult.RESULT_COMMAND_DENIED
            if self == CommandResult.Result.COMMAND_DENIED_LANDED_STATE_UNKNOWN:
                return command_pb2.CommandResult.RESULT_COMMAND_DENIED_LANDED_STATE_UNKNOWN
            if self == CommandResult.Result.COMMAND_DENIED_NOT_LANDED:
                return command_pb2.CommandResult.RESULT_COMMAND_DENIED_NOT_LANDED
            if self == CommandResult.Result.TIMEOUT:
                return command_pb2.CommandResult.RESULT_TIMEOUT
            if self == CommandResult.Result.VTOL_TRANSITION_SUPPORT_UNKNOWN:
                return command_pb2.CommandResult.RESULT_VTOL_TRANSITION_SUPPORT_UNKNOWN
            if self == CommandResult.Result.NO_VTOL_TRANSITION_SUPPORT:
                return command_pb2.CommandResult.RESULT_NO_VTOL_TRANSITION_SUPPORT
            if self == CommandResult.Result.PARAMETER_ERROR:
                return command_pb2.CommandResult.RESULT_PARAMETER_ERROR
            if self == CommandResult.Result.UNSUPPORTED:
                return command_pb2.CommandResult.RESULT_UNSUPPORTED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == command_pb2.CommandResult.RESULT_UNKNOWN:
                return CommandResult.Result.UNKNOWN
            if rpc_enum_value == command_pb2.CommandResult.RESULT_SUCCESS:
                return CommandResult.Result.SUCCESS
            if rpc_enum_value == command_pb2.CommandResult.RESULT_NO_SYSTEM:
                return CommandResult.Result.NO_SYSTEM
            if rpc_enum_value == command_pb2.CommandResult.RESULT_CONNECTION_ERROR:
                return CommandResult.Result.CONNECTION_ERROR
            if rpc_enum_value == command_pb2.CommandResult.RESULT_BUSY:
                return CommandResult.Result.BUSY
            if rpc_enum_value == command_pb2.CommandResult.RESULT_COMMAND_DENIED:
                return CommandResult.Result.COMMAND_DENIED
            if (
                rpc_enum_value
                == command_pb2.CommandResult.RESULT_COMMAND_DENIED_LANDED_STATE_UNKNOWN
            ):
                return CommandResult.Result.COMMAND_DENIED_LANDED_STATE_UNKNOWN
            if rpc_enum_value == command_pb2.CommandResult.RESULT_COMMAND_DENIED_NOT_LANDED:
                return CommandResult.Result.COMMAND_DENIED_NOT_LANDED
            if rpc_enum_value == command_pb2.CommandResult.RESULT_TIMEOUT:
                return CommandResult.Result.TIMEOUT
            if rpc_enum_value == command_pb2.CommandResult.RESULT_VTOL_TRANSITION_SUPPORT_UNKNOWN:
                return CommandResult.Result.VTOL_TRANSITION_SUPPORT_UNKNOWN
            if rpc_enum_value == command_pb2.CommandResult.RESULT_NO_VTOL_TRANSITION_SUPPORT:
                return CommandResult.Result.NO_VTOL_TRANSITION_SUPPORT
            if rpc_enum_value == command_pb2.CommandResult.RESULT_PARAMETER_ERROR:
                return CommandResult.Result.PARAMETER_ERROR
            if rpc_enum_value == command_pb2.CommandResult.RESULT_UNSUPPORTED:
                return CommandResult.Result.UNSUPPORTED

        def __str__(self):
            return self.name

    def __init__(self, result, result_str):
        """ Initializes the CommandResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two CommandResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # CommandResult object
            return (self.result == to_compare.result) and (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ CommandResult in string representation """
        struct_repr = ", ".join(
            ["result: " + str(self.result), "result_str: " + str(self.result_str)]
        )

        return f"CommandResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcCommandResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return CommandResult(
            CommandResult.Result.translate_from_rpc(rpcCommandResult.result),
            rpcCommandResult.result_str,
        )

    def translate_to_rpc(self, rpcCommandResult):
        """ Translates this SDK object into its gRPC equivalent """

        rpcCommandResult.result = self.result.translate_to_rpc()

        rpcCommandResult.result_str = self.result_str


class CommandError(Exception):
    """ Raised when a CommandResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Command(AsyncBase):
    """
 

     Generated by dcsdkgen - MAVSDK Command API
    """

    # Plugin name
    name = "Command"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = command_pb2_grpc.CommandServiceStub(channel)

    def _extract_result(self, response):
        """ Returns the response status and description """
        return CommandResult.translate_from_rpc(response.command_result)

    async def send_command_long(self, command):
        """
     

         Parameters
         ----------
         command : CommandLong
             
         Raises
         ------
         CommandError
             If the request fails. The error contains the reason for the failure.
        """

        request = command_pb2.SendCommandLongRequest()

        command.translate_to_rpc(request.command)

        response = await self._stub.SendCommandLong(request)

        result = self._extract_result(response)

        if result.result != CommandResult.Result.SUCCESS:
            raise CommandError(result, "send_command_long()", command)
