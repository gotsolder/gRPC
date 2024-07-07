# Request-Cancel: Client

import grpc
import cancel_example_pb2
import cancel_example_pb2_grpc
import time


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = cancel_example_pb2_grpc.CancelServiceStub(channel)
    request = cancel_example_pb2.Request(request_data="Start")
    future = stub.LongRunningOperation.future(request)

    # future.cancel()    # cancels the request
    # future.cancelled() # checks if it was cancelled
    # future.done()      # checks if the request is complete

    print("Request Canceled: ", future.cancelled())
    print("Request Done: ", future.done())
    print("Response:", future._state.response)

    print("...")
    time.sleep(3)
    future.cancel()

    print("Request Canceled: ", future.cancelled())
    print("Request Done: ", future.done())

    try:
        if not future.done():
            print("Still Waiting for Response...")
        response = future.result()
        print(f"Response Received: {response.response_data}")
    except grpc.FutureCancelledError as e:
        print("Request was cancelled", e)
    except grpc.RpcError as e:
        print("Some other error occurred?\n", e)


if __name__ == "__main__":
    run()

# EOF
