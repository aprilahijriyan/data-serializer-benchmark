# data-serializer-benchmark

Simple script to compare module for "Serialize data in Python".

For now I'm just including the modules below for comparison:

* python built-in json module
* orjson
* MessagePack (aka `msgpack`)
* msgspec (`json` and `msgpack`)


# Results

Running `bench.py` script with python 3.9 on Macbook Pro 2015. Here are the results:

```
$ python bench.py
Function 'msgspec_msgpack_dumps' took 0.0008 seconds
Function 'orjson_dumps' took 0.0098 seconds
Function 'msgspec_json_dumps' took 0.0104 seconds
Function 'msgpack_dumps' took 0.0224 seconds
Function 'msgpack_loads' took 0.0525 seconds
Function 'msgspec_json_loads' took 0.0583 seconds
Function 'msgspec_msgpack_loads' took 0.0605 seconds
Function 'json_dumps' took 0.0770 seconds
Function 'orjson_loads' took 0.0785 seconds
Function 'json_loads' took 0.0869 seconds
```
