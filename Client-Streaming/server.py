# Client Streaming: Chat Server

import grpc
from concurrent import futures
import streaming_pb2
import streaming_pb2_grpc


class StreamingService(streaming_pb2_grpc.StreamingServiceServicer):
    def StreamData(self, request_iterator, context):
        result = ""
        for request in request_iterator:
            result += request.data + " "

        return streaming_pb2.ResponseMessage(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streaming_pb2_grpc.add_StreamingServiceServicer_to_server(StreamingService(), server)
    server.add_insecure_port('[::]:50051')
    print("Client-Streaming: Server Start...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

# EOF
