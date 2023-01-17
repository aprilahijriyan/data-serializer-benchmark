import msgspec
import json
import msgpack
import time
import functools
import orjson

bench_dict = {}

def timeit(func):
    @functools.wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = format(end_time - start_time, ".4f")
        name = func.__name__
        bench_dict[name] = total_time
        return result
    return timeit_wrapper

# built-in json
@timeit
def json_loads(data: bytes):
    return json.loads(data)

@timeit
def json_dumps(data: object):
    return json.dumps(data)

# orjson
@timeit
def orjson_loads(data: bytes):
    return orjson.loads(data)

@timeit
def orjson_dumps(data: object):
    return orjson.dumps(data)

# msgpack
@timeit
def msgpack_loads(data: bytes):
    return msgpack.loads(data)

@timeit
def msgpack_dumps(data: object):
    return msgpack.dumps(data)


# msgspec (json)
@timeit
def msgspec_json_loads(data: bytes):
    return msgspec.json.decode(data)

@timeit
def msgspec_json_dumps(data: object):
    return msgspec.json.encode(data)


# msgspec (msgpack)
@timeit
def msgspec_msgpack_loads(data: bytes):
    return msgspec.msgpack.decode(data)

@timeit
def msgspec_msgpack_dumps(data: object):
    return msgspec.msgpack.encode(data)


def main():
    with open("datasets/movies.json", "rb") as fp:
        data = fp.read()

    # test built-in json module
    pyobj = json_loads(data)
    json_dumps(pyobj)

    # test orjson
    orjson_loads(data)
    orjson_dumps(pyobj)

    # test msgpack
    msgpack_data = msgpack_dumps(pyobj)
    msgpack_loads(msgpack_data)

    # test msgspec (json)
    msgspec_json_loads(data)
    msgspec_json_dumps(pyobj)

    # test msgspec (msgpack)
    msgspec_msgpack_dumps(data)
    msgspec_msgpack_loads(msgpack_data)

    for func_name, total_time in sorted(bench_dict.items(), key=lambda x: x[1]):
        print(f"Function {func_name!r} took {total_time} seconds")

if __name__ == "__main__":
    main()
