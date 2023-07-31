load("@pypi//:requirements.bzl", "requirement")
load("//toolchain/python:defs.bzl", "python_library")

package(default_visibility = ["//visibility:public"])

python_library(
    srcs = glob(["*.py"]),
    deps = [
        "//src/core/player:lib",
        requirement("pydealer"),
    ],
)
