# Bidirectional Streaming: Chat client

import grpc
import messages_pb2
import messages_pb2_grpc
import time


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = messages_pb2_grpc.ChatServiceStub(channel)

        def request_generator():
            messages = ["Hi?", "gRPC Bidirectional!", "Well!"]
            for msg in messages:
                print(f"Client Message: {msg}")
                yield messages_pb2.ChatMessage(message=msg)
                time.sleep(2)

        responses = stub.Chat(request_generator())
        for response in responses:
            print(f"Received Messages: {response.message}")


if __name__ == "__main__":
    run()

# EOF
