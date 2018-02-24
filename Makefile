.PHONY: protobuf
protobuf:
	python -m grpc_tools.protoc -I .  --python_out=protobufs --grpc_python_out=protobufs github.com/moby/buildkit/api/services/control/control.proto
	python -m grpc_tools.protoc -I .  --python_out=protobufs --grpc_python_out=protobufs github.com/moby/buildkit/solver/pb/ops.proto
	python -m grpc_tools.protoc -I .  --python_out=protobufs --grpc_python_out=protobufs github.com/gogo/protobuf/gogoproto/gogo.proto
	mv protobufs/github.com/moby/buildkit/api/services/control/control_pb2_grpc.py protobufs/github/com/moby/buildkit/api/services/control/
	mv protobufs/github.com/moby/buildkit/solver/pb/ops_pb2_grpc.py protobufs/github/com/moby/buildkit/solver/pb/
	mv protobufs/github.com/gogo/protobuf/gogoproto/gogo_pb2_grpc.py protobufs/github/com/gogo/protobuf/gogoproto/
	rm -rf protobufs/github.com/
	rm -rf github
	mv protobufs/github github
	rm -rf protobufs
