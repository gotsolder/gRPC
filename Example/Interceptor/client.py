# Interceptor: Client

import grpc
import interceptor_example_pb2
import interceptor_example_pb2_grpc


class LoggingInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request):
        method = client_call_details.method
        print(f"Sending request to method: {method}")
        response = continuation(client_call_details, request)
        print(f"Received response from method: {method}")


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        intercept_channel = grpc.intercept_channel(channel, LoggingInterceptor())
        stub = interceptor_example_pb2_grpc.EchoServiceStub(intercept_channel)
        response = stub.Echo(interceptor_example_pb2.EchoRequest(message="THIS FAILS"))
        print(f"Response: {response.message}")


if __name__ == "__main__":
    run()

# EOF
