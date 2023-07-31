# buildifier-ignore-all
load("@rules_python//python:defs.bzl", "py_binary", "py_library")

def python_library(srcs, deps = [], name = "lib", **kwargs):
    py_library(
        name = name,
        srcs = srcs,
        deps = deps,
        **kwargs
    )

def python_binary(name, srcs = [], **kwargs):
    py_binary(
        name = name,
        srcs = srcs,
        **kwargs
    )
