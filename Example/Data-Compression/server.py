# Data-Compression: Server

import grpc
from concurrent import futures
import example_pb2
import example_pb2_grpc


class DataServiceServicer(example_pb2_grpc.DataServiceServicer):
    def GetData(self, request, context):
        data_id = request.data_id
        print(f"Received: {data_id=}")
        data = b"This is a large data example.   " * 10000
        print(f"Original data size: {len(data)} bytes")
        return example_pb2.DataResponse(data=data)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         compression=grpc.Compression.Gzip)
    example_pb2_grpc.add_DataServiceServicer_to_server(DataServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Data-Compression: Server Start...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

# EOF
