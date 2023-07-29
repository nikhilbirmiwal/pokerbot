load("//toolchain/python:defs.bzl", "python_binary", "python_library")

python_library(
    name = "lib",
    srcs = ["lib.py"],
)

python_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [":lib"],
)
