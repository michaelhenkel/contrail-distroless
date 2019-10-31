load("@io_bazel_rules_docker//python:image.bzl", "py_image")
load("@io_bazel_rules_docker//container:container.bzl", "container_image")
load("@contrail_config_api_deps//:requirements.bzl", "requirement")

py_image(
    name = "config_api",
    srcs = ["contrail-api.py"],
    base = "//python2.7:python27",
    deps = [requirement("vine")],
    main = "contrail-api.py",
)

py_image(
    name = "config_api_debug",
    srcs = ["contrail-api.py"],
    base = "//python2.7:debug",
    deps = [
             requirement("amqp"),
             requirement("attrdict"),
             requirement("Babel"),
             requirement("bottle"),
             requirement("certifi"),
             requirement("chardet"),
             requirement("configparser"),
             requirement("contextlib2"),
             requirement("crypto"),
             requirement("debtcollector"),
             requirement("enum34"),
             requirement("funcsigs"),
             requirement("fysom"),
             requirement("gevent"),
             requirement("greenlet"),
             requirement("idna"),
             requirement("iso8601"),
             requirement("importlib_metadata"),
             requirement("kazoo"),
             requirement("keystoneauth1"),
             requirement("kombu"),
             requirement("monotonic"),
             requirement("more_itertools"),
             requirement("msgpack"),
             requirement("netaddr"),
             requirement("netifaces"),
             requirement("os-service-types"),
             requirement("oslo.config"),
             requirement("oslo.i18n"),
             requirement("oslo.serialization"),
             requirement("oslo.utils"),
             requirement("pathlib2"),
             requirement("pbr"),
             requirement("pycassa"),
             requirement("pyparsing"),
             requirement("python-keystoneclient"),
             requirement("pytz"),
             requirement("PyYAML"),
             requirement("requests"),
             requirement("rfc3986"),
             requirement("scandir"),
             requirement("setuptools"),
             requirement("six"),
             requirement("stevedore"),
             requirement("thrift"),
             requirement("urllib3"),
             requirement("vine"),
             requirement("wrapt"),
             requirement("zipp")
	    ],
    main = "contrail-api.py",
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
