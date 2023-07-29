load("//toolchain/python:defs.bzl", "python_binary", "python_library")

package(default_visibility = ["//visibility:private"])

python_library(
    name = "lib",
    srcs = glob(["*.py"]),
)

python_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [":lib"],
)
