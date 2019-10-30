load("@io_bazel_rules_docker//python:image.bzl", "py_image")
load("@io_bazel_rules_docker//container:container.bzl", "container_image")
load("@contrail_config_api_deps//:requirements.bzl", "requirement")

py_image(
    name = "config_api",
    srcs = ["hello.py"],
    base = "//python2.7:python27",
    deps = [requirement("vine")],
    main = "hello.py",
)

py_image(
    name = "config_api_debug",
    srcs = ["hello.py"],
    base = "//python2.7:debug",
    deps = [
             requirement("amqp"),
             requirement("attrdict"),
             requirement("bottle"),
             requirement("certifi"),
             requirement("chardet"),
             requirement("configparser"),
             requirement("contextlib2"),
             requirement("crypto"),
             requirement("fysom"),
             requirement("gevent"),
             requirement("greenlet"),
             requirement("idna"),
             requirement("kazoo"),
             requirement("kombu"),
             requirement("netaddr"),
             requirement("netifaces"),
             requirement("pathlib2"),
             requirement("pycassa"),
             requirement("python-keystoneclient"),
             requirement("requests"),
             requirement("scandir"),
             requirement("setuptools"),
             requirement("six"),
             requirement("stevedore"),
             requirement("thrift"),
             requirement("vine")
	    ],
    main = "hello.py",
)

container_image(
    name = "configapi",
    base = ":config_api",
)

container_image(
    name = "configapi_debug",
    base = ":config_api_debug",
)

load("@io_bazel_rules_docker//container:container.bzl", "container_push")
container_push(
   name = "publish",
   image = ":configapi",
   format = "Docker",
   registry = "index.docker.io",
   repository = "michaelhenkel/distroless_config",
   tag =  "latest",
   #tag =  "@BUILD_NUMBER@",
)

container_push(
   name = "publish-debug",
   image = ":configapi_debug",
   format = "Docker",
   registry = "index.docker.io",
   repository = "michaelhenkel/distroless_config",
   tag =  "debug",
   #tag =  "@BUILD_NUMBER@",
)
