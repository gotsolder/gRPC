# Request-Cancel: Server

from concurrent import futures
import grpc
import time
import cancel_example_pb2
import cancel_example_pb2_grpc


class CancelServiceServicer(cancel_example_pb2_grpc.CancelServiceServicer):
    def LongRunningOperation(self, request, context):
        for i in range(10):
            if context.is_active():
                print(f"Processing {i}...")
                time.sleep(1)
            else:
                print("Request was cancelled")
                return cancel_example_pb2.Response(response_data="Cancelled")

        print("Request was Completed")
        return cancel_example_pb2.Response(response_data="Completed")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cancel_example_pb2_grpc.add_CancelServiceServicer_to_server(CancelServiceServicer(), server)
    server.add_insecure_port('[::]:50051')

    server.start()
    print("Request-Cancel: Server Start...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

# EOF
