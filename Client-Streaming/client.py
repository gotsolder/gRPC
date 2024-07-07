# Client Streaming: Chat client

import grpc
import streaming_pb2
import streaming_pb2_grpc


def generate_request():
    messages = ["message 1", "message 2", "message 3"]
    for message in messages:
        yield streaming_pb2.RequestMessage(data=message)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = streaming_pb2_grpc.StreamingServiceStub(channel)
        response = stub.StreamData(generate_request())
        print("Response from server: " + response.result)


if __name__ == "__main__":
    run()

# EOF
