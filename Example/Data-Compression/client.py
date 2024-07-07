# Data-Compression: Client

import grpc
import example_pb2
import example_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051', compression=grpc.Compression.Gzip) as channel:
        stub = example_pb2_grpc.DataServiceStub(channel)
        response = stub.GetData(example_pb2.DataRequest(data_id="3"))
        print(f"Received data size: {len(response.data)} bytes")

        print("ehhhh...I dont see any evidence of compression no matter what is used")


if __name__ == "__main__":
    run()

# EOF
