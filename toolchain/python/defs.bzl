# buildifier-ignore-all
load("@rules_python//python:defs.bzl", "py_binary", "py_library")

def python_library(name, srcs, **kwargs):
    py_library(
        name = name,
        srcs = srcs,
        **kwargs
    )

def python_binary(name, srcs = [], **kwargs):
    py_binary(
        name = name,
        srcs = srcs,
        **kwargs
    )
