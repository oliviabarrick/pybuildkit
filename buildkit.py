#!/usr/bin/env python
import grpc
import github.com.moby.buildkit.api.services.control.control_pb2_grpc as control_pb2_grpc
import github.com.moby.buildkit.api.services.control.control_pb2 as control_pb2
import github.com.moby.buildkit.solver.pb.ops_pb2 as ops_pb2

channel = grpc.insecure_channel('unix:/run/buildkit/buildkitd.sock')

control = control_pb2_grpc.ControlStub(channel)

print(control.ListWorkers(control_pb2.ListWorkersRequest()))

alive = True

def create_session(session_id):
    response = control.Solve(control_pb2.SolveRequest(
        Ref="helloworld",
        Definition=ops_pb2.Definition(),
        Exporter="docker",
        ExporterAttrs={
            "name": "myimage:latest",
        },
        Session=session_id,
        Frontend="dockerfile.v0",
        FrontendAttrs={
            "filename": "Dockerfile"
        },
        Cache=control_pb2.CacheOptions(ExportRef="", ImportRef="")
    ))

    print(response)

    yield control_pb2.BytesMessage(data=b'\0')

for b in control.Session(create_session("1234"), metadata=(
    ("x-docker-expose-session-uuid", "1234"),
    ("x-docker-expose-session-name", "1234"),
    ("x-docker-expose-session-sharedkey", "1234")
)):
    print(b)
