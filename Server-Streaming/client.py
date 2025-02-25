# Server Streaming: Chat Client

import grpc
import messages_pb2
import messages_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = messages_pb2_grpc.ChatServiceStub(channel)
        for message in stub.ChatStream(messages_pb2.ChatMessage(message="Start")):
            print(f"Received Message: {message.message}")


if __name__ == "__main__":
    run()

# EOF
