# Unary: Client

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="Alice"))
        print("Greeter client received: " + response.message)


def run2():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)

    response = stub.SayHello(helloworld_pb2.HelloRequest(name="Alice"))
    print("Greeter client received: " + response.message)

    response = stub.SayHello(helloworld_pb2.HelloRequest(name="Greg"))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run2()

# EOF
