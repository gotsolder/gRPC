#!/usr/bin/bash

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. my_service.proto

# 'python -m grpc_tools.protoc' : Executes the Protobuf compiler included in 'grpcio-tools' package
# '-I.' : Sets the search path for '.proto' files to the current directory
# '--python_out=.' : Stores the generated Python code (related to messages) in the current directory
# '--grpc_python_out=.' :  Stores the generated Python code (related to gRPC services)  in the current directory
# 'my_service.proto' : Name of the '.proto' file to compile