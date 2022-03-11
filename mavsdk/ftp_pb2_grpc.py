# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import ftp_pb2 as ftp_dot_ftp__pb2


class FtpServiceStub(object):
    """
    Implements file transfer functionality using MAVLink FTP.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Reset = channel.unary_unary(
            "/mavsdk.rpc.ftp.FtpService/Reset",
            request_serializer=ftp_dot_ftp__pb2.ResetRequest.SerializeToString,
            response_deserializer=ftp_dot_ftp__pb2.ResetResponse.FromString,
        )
        self.SubscribeDownload = channel.unary_stream(
            "/mavsdk.rpc.ftp.FtpService/SubscribeDownload",
            request_serializer=ftp_dot_ftp__pb2.SubscribeDownloadRequest.SerializeToString,
            response_deserializer=ftp_dot_ftp__pb2.DownloadResponse.FromString,
        )
        self.SubscribeUpload = channel.unary_stream(
            "/mavsdk.rpc.ftp.FtpService/SubscribeUpload",
            request_serializer=ftp_dot_ftp__pb2.SubscribeUploadRequest.SerializeToString,
            response_deserializer=ftp_dot_ftp__pb2.UploadResponse.FromString,
        )
        self.ListDirectory = channel.unary_unary(
            "/mavsdk.rpc.ftp.FtpService/ListDirectory",
            request_serializer=ftp_dot_ftp__pb2.ListDirectoryRequest.SerializeToString,
            response_deserializer=ftp_dot_ftp__pb2.ListDirectoryResponse.FromString,
        )
        self.CreateDirectory = channel.unary_unary(
            "/mavsdk.rpc.ftp.FtpService/CreateDirectory",
            request_serializer=ftp_dot_ftp__pb2.CreateDirectoryRequest.SerializeToString,
            response_deserializer=ftp_dot_ftp__pb2.CreateDirectoryResponse.FromString,
        )
        self.RemoveDirectory = channel.unary_unary(
            "/mavsdk.rpc.ftp.FtpService/RemoveDirectory",
            request_serializer=ftp_dot_ftp__pb2.RemoveDirectoryRequest.SerializeToString,
            response_deserializer=ftp_dot_ftp__pb2.RemoveDirectoryResponse.FromString,
        )
        self.RemoveFile = channel.unary_unary(
            "/mavsdk.rpc.ftp.FtpService/RemoveFile",
            request_serializer=ftp_dot_ftp__pb2.RemoveFileRequest.SerializeToString,
            response_deserializer=ftp_dot_ftp__pb2.RemoveFileResponse.FromString,
        )
        self.Rename = channel.unary_unary(
            "/mavsdk.rpc.ftp.FtpService/Rename",
            request_serializer=ftp_dot_ftp__pb2.RenameRequest.SerializeToString,
            response_deserializer=ftp_dot_ftp__pb2.RenameResponse.FromString,
        )
        self.AreFilesIdentical = channel.unary_unary(
            "/mavsdk.rpc.ftp.FtpService/AreFilesIdentical",
            request_serializer=ftp_dot_ftp__pb2.AreFilesIdenticalRequest.SerializeToString,
            response_deserializer=ftp_dot_ftp__pb2.AreFilesIdenticalResponse.FromString,
        )
        self.SetRootDirectory = channel.unary_unary(
            "/mavsdk.rpc.ftp.FtpService/SetRootDirectory",
            request_serializer=ftp_dot_ftp__pb2.SetRootDirectoryRequest.SerializeToString,
            response_deserializer=ftp_dot_ftp__pb2.SetRootDirectoryResponse.FromString,
        )
        self.SetTargetCompid = channel.unary_unary(
            "/mavsdk.rpc.ftp.FtpService/SetTargetCompid",
            request_serializer=ftp_dot_ftp__pb2.SetTargetCompidRequest.SerializeToString,
            response_deserializer=ftp_dot_ftp__pb2.SetTargetCompidResponse.FromString,
        )
        self.GetOurCompid = channel.unary_unary(
            "/mavsdk.rpc.ftp.FtpService/GetOurCompid",
            request_serializer=ftp_dot_ftp__pb2.GetOurCompidRequest.SerializeToString,
            response_deserializer=ftp_dot_ftp__pb2.GetOurCompidResponse.FromString,
        )


class FtpServiceServicer(object):
    """
    Implements file transfer functionality using MAVLink FTP.
    """

    def Reset(self, request, context):
        """
        Resets FTP server in case there are stale open sessions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubscribeDownload(self, request, context):
        """
        Downloads a file to local directory.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubscribeUpload(self, request, context):
        """
        Uploads local file to remote directory.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListDirectory(self, request, context):
        """
        Lists items from a remote directory.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateDirectory(self, request, context):
        """
        Creates a remote directory.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RemoveDirectory(self, request, context):
        """
        Removes a remote directory.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RemoveFile(self, request, context):
        """
        Removes a remote file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Rename(self, request, context):
        """
        Renames a remote file or remote directory.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AreFilesIdentical(self, request, context):
        """
        Compares a local file to a remote file using a CRC32 checksum.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SetRootDirectory(self, request, context):
        """
        Set root directory for MAVLink FTP server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SetTargetCompid(self, request, context):
        """
        Set target component ID. By default it is the autopilot.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetOurCompid(self, request, context):
        """
        Get our own component ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_FtpServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Reset": grpc.unary_unary_rpc_method_handler(
            servicer.Reset,
            request_deserializer=ftp_dot_ftp__pb2.ResetRequest.FromString,
            response_serializer=ftp_dot_ftp__pb2.ResetResponse.SerializeToString,
        ),
        "SubscribeDownload": grpc.unary_stream_rpc_method_handler(
            servicer.SubscribeDownload,
            request_deserializer=ftp_dot_ftp__pb2.SubscribeDownloadRequest.FromString,
            response_serializer=ftp_dot_ftp__pb2.DownloadResponse.SerializeToString,
        ),
        "SubscribeUpload": grpc.unary_stream_rpc_method_handler(
            servicer.SubscribeUpload,
            request_deserializer=ftp_dot_ftp__pb2.SubscribeUploadRequest.FromString,
            response_serializer=ftp_dot_ftp__pb2.UploadResponse.SerializeToString,
        ),
        "ListDirectory": grpc.unary_unary_rpc_method_handler(
            servicer.ListDirectory,
            request_deserializer=ftp_dot_ftp__pb2.ListDirectoryRequest.FromString,
            response_serializer=ftp_dot_ftp__pb2.ListDirectoryResponse.SerializeToString,
        ),
        "CreateDirectory": grpc.unary_unary_rpc_method_handler(
            servicer.CreateDirectory,
            request_deserializer=ftp_dot_ftp__pb2.CreateDirectoryRequest.FromString,
            response_serializer=ftp_dot_ftp__pb2.CreateDirectoryResponse.SerializeToString,
        ),
        "RemoveDirectory": grpc.unary_unary_rpc_method_handler(
            servicer.RemoveDirectory,
            request_deserializer=ftp_dot_ftp__pb2.RemoveDirectoryRequest.FromString,
            response_serializer=ftp_dot_ftp__pb2.RemoveDirectoryResponse.SerializeToString,
        ),
        "RemoveFile": grpc.unary_unary_rpc_method_handler(
            servicer.RemoveFile,
            request_deserializer=ftp_dot_ftp__pb2.RemoveFileRequest.FromString,
            response_serializer=ftp_dot_ftp__pb2.RemoveFileResponse.SerializeToString,
        ),
        "Rename": grpc.unary_unary_rpc_method_handler(
            servicer.Rename,
            request_deserializer=ftp_dot_ftp__pb2.RenameRequest.FromString,
            response_serializer=ftp_dot_ftp__pb2.RenameResponse.SerializeToString,
        ),
        "AreFilesIdentical": grpc.unary_unary_rpc_method_handler(
            servicer.AreFilesIdentical,
            request_deserializer=ftp_dot_ftp__pb2.AreFilesIdenticalRequest.FromString,
            response_serializer=ftp_dot_ftp__pb2.AreFilesIdenticalResponse.SerializeToString,
        ),
        "SetRootDirectory": grpc.unary_unary_rpc_method_handler(
            servicer.SetRootDirectory,
            request_deserializer=ftp_dot_ftp__pb2.SetRootDirectoryRequest.FromString,
            response_serializer=ftp_dot_ftp__pb2.SetRootDirectoryResponse.SerializeToString,
        ),
        "SetTargetCompid": grpc.unary_unary_rpc_method_handler(
            servicer.SetTargetCompid,
            request_deserializer=ftp_dot_ftp__pb2.SetTargetCompidRequest.FromString,
            response_serializer=ftp_dot_ftp__pb2.SetTargetCompidResponse.SerializeToString,
        ),
        "GetOurCompid": grpc.unary_unary_rpc_method_handler(
            servicer.GetOurCompid,
            request_deserializer=ftp_dot_ftp__pb2.GetOurCompidRequest.FromString,
            response_serializer=ftp_dot_ftp__pb2.GetOurCompidResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "mavsdk.rpc.ftp.FtpService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class FtpService(object):
    """
    Implements file transfer functionality using MAVLink FTP.
    """

    @staticmethod
    def Reset(
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
        return grpc.experimental.unary_unary(
            request,
            target,
            "/mavsdk.rpc.ftp.FtpService/Reset",
            ftp_dot_ftp__pb2.ResetRequest.SerializeToString,
            ftp_dot_ftp__pb2.ResetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SubscribeDownload(
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
            "/mavsdk.rpc.ftp.FtpService/SubscribeDownload",
            ftp_dot_ftp__pb2.SubscribeDownloadRequest.SerializeToString,
            ftp_dot_ftp__pb2.DownloadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SubscribeUpload(
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
            "/mavsdk.rpc.ftp.FtpService/SubscribeUpload",
            ftp_dot_ftp__pb2.SubscribeUploadRequest.SerializeToString,
            ftp_dot_ftp__pb2.UploadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListDirectory(
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
        return grpc.experimental.unary_unary(
            request,
            target,
            "/mavsdk.rpc.ftp.FtpService/ListDirectory",
            ftp_dot_ftp__pb2.ListDirectoryRequest.SerializeToString,
            ftp_dot_ftp__pb2.ListDirectoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateDirectory(
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
        return grpc.experimental.unary_unary(
            request,
            target,
            "/mavsdk.rpc.ftp.FtpService/CreateDirectory",
            ftp_dot_ftp__pb2.CreateDirectoryRequest.SerializeToString,
            ftp_dot_ftp__pb2.CreateDirectoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def RemoveDirectory(
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
        return grpc.experimental.unary_unary(
            request,
            target,
            "/mavsdk.rpc.ftp.FtpService/RemoveDirectory",
            ftp_dot_ftp__pb2.RemoveDirectoryRequest.SerializeToString,
            ftp_dot_ftp__pb2.RemoveDirectoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def RemoveFile(
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
        return grpc.experimental.unary_unary(
            request,
            target,
            "/mavsdk.rpc.ftp.FtpService/RemoveFile",
            ftp_dot_ftp__pb2.RemoveFileRequest.SerializeToString,
            ftp_dot_ftp__pb2.RemoveFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Rename(
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
        return grpc.experimental.unary_unary(
            request,
            target,
            "/mavsdk.rpc.ftp.FtpService/Rename",
            ftp_dot_ftp__pb2.RenameRequest.SerializeToString,
            ftp_dot_ftp__pb2.RenameResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def AreFilesIdentical(
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
        return grpc.experimental.unary_unary(
            request,
            target,
            "/mavsdk.rpc.ftp.FtpService/AreFilesIdentical",
            ftp_dot_ftp__pb2.AreFilesIdenticalRequest.SerializeToString,
            ftp_dot_ftp__pb2.AreFilesIdenticalResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SetRootDirectory(
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
        return grpc.experimental.unary_unary(
            request,
            target,
            "/mavsdk.rpc.ftp.FtpService/SetRootDirectory",
            ftp_dot_ftp__pb2.SetRootDirectoryRequest.SerializeToString,
            ftp_dot_ftp__pb2.SetRootDirectoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SetTargetCompid(
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
        return grpc.experimental.unary_unary(
            request,
            target,
            "/mavsdk.rpc.ftp.FtpService/SetTargetCompid",
            ftp_dot_ftp__pb2.SetTargetCompidRequest.SerializeToString,
            ftp_dot_ftp__pb2.SetTargetCompidResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetOurCompid(
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
        return grpc.experimental.unary_unary(
            request,
            target,
            "/mavsdk.rpc.ftp.FtpService/GetOurCompid",
            ftp_dot_ftp__pb2.GetOurCompidRequest.SerializeToString,
            ftp_dot_ftp__pb2.GetOurCompidResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
