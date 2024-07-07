# Bidirectional Streaming: Chat Server

import grpc
from concurrent import futures
import messages_pb2
import messages_pb2_grpc
import time


class ChatService(messages_pb2_grpc.ChatServiceServicer):
    def Chat(self, request_iterator, context):
        for request in request_iterator:
            print(f"Client Message: {request.message}")
            response_message = f"Server Response: {request.message}"
            print(f"Server Message: {response_message}")
            yield messages_pb2.ChatMessage(message=response_message)
            time.sleep(1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:50051')
    print("Bidirectional-Streaming: Server Start...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

# EOF
