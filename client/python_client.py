import grpc
import grpcdemo_pb2_grpc
import grpcdemo_pb2


def test_noparam_func(stub):
    response = stub.NoParamFunc(grpcdemo_pb2.Empty())
    print("Response from NoParamFunc is:[", response, "]")


def test_unary_func(stub):
    response = stub.UnaryFunc(grpcdemo_pb2.UnaryFuncRequest(name="Erdinc", height=180))
    if response.msg == "":
        print("No message from UnaryFunc")
    else:
        print("Response from UnaryFunc is:[", response.msg, "]")


def run() :
    with grpc.insecure_channel('localhost:7777') as channel:
        stub = grpcdemo_pb2_grpc.GrpcDemoStub(channel)
        print("-------------- NoParamFunc --------------")
        test_noparam_func(stub)
        print("--------------- UnaryFunc ---------------")
        test_unary_func(stub)

if __name__ == '__main__':
    run()
