load("@io_bazel_rules_docker//python:image.bzl", "py_image")
load("@io_bazel_rules_docker//container:container.bzl", "container_image")
load("@contrail_config_api_deps//:requirements.bzl", "requirement")
load("@bazel_tools//tools/build_defs/pkg:pkg.bzl", "pkg_tar")
load(":gensandesh.bzl", "gensandesh")

gensandesh(
    name = "acl",
    #command = "$(location @contrail_repository//:src/config/uve/acl.sandesh)",
    command = "$(location @contrail_repository//:acl_sandesh)",
    srcs = ["@contrail_repository//:acl_sandesh"],
#    output = "request_skeleton.py",
    #srcs = ["@contrail_repository//:src/config/uve/acl.sandesh"],
    #srcs = ["@contrail_repository//:src/config/uve/acl.sandesh"],
)

genrule(
    name = "sandesh_acl",
    srcs = [
                "@contrail_common_repository//:src_common",
                "@contrail_repository//:controller_src",
                "@contrail_repository//:acl_sandesh",
		"@contrail_repository//:cfgm_cpuinfo.sandesh",
                "@contrail_repository//:config_req.sandesh",
                "@contrail_repository//:greenlets.sandesh",
                "@contrail_repository//:msg_traces.sandesh",
                "@contrail_repository//:physical_router_config.sandesh",
                "@contrail_repository//:physical_router.sandesh",
                "@contrail_repository//:service_instance.sandesh",
		"@contrail_repository//:service_status.sandesh",
                "@contrail_repository//:virtual_machine.sandesh",
                "@contrail_repository//:virtual_network.sandesh",
                "@contrail_repository//:vnc_api.sandesh",
	   ],
    outs = [
                "acl/request_skeleton.py",
		"acl/constants.py",
		"acl/__init__.py",
		"acl/ttypes.py",
		"acl/http_request.py",
                "cfgm_cpuinfo/request_skeleton.py",
                "cfgm_cpuinfo/constants.py",
                "cfgm_cpuinfo/__init__.py",
                "cfgm_cpuinfo/ttypes.py",
                "cfgm_cpuinfo/http_request.py",
                "config_req/request_skeleton.py",
                "config_req/constants.py",
                "config_req/__init__.py",
                "config_req/ttypes.py",
                "config_req/http_request.py",
                "greenlets/request_skeleton.py",
                "greenlets/constants.py",
                "greenlets/__init__.py",
                "greenlets/ttypes.py",
                "greenlets/http_request.py",
                "msg_traces/request_skeleton.py",
                "msg_traces/constants.py",
                "msg_traces/__init__.py",
                "msg_traces/ttypes.py",
                "msg_traces/http_request.py",
                "physical_router_config/request_skeleton.py",
                "physical_router_config/constants.py",
                "physical_router_config/__init__.py",
                "physical_router_config/ttypes.py",
                "physical_router_config/http_request.py",
                "physical_router/request_skeleton.py",
                "physical_router/constants.py",
                "physical_router/__init__.py",
                "physical_router/ttypes.py",
                "physical_router/http_request.py",
                "service_instance/request_skeleton.py",
                "service_instance/constants.py",
                "service_instance/__init__.py",
                "service_instance/ttypes.py",
                "service_instance/http_request.py",
                "service_status/request_skeleton.py",
                "service_status/constants.py",
                "service_status/__init__.py",
                "service_status/ttypes.py",
                "service_status/http_request.py",
                "virtual_machine/request_skeleton.py",
                "virtual_machine/constants.py",
                "virtual_machine/__init__.py",
                "virtual_machine/ttypes.py",
                "virtual_machine/http_request.py",
                "virtual_network/request_skeleton.py",
                "virtual_network/constants.py",
                "virtual_network/__init__.py",
                "virtual_network/ttypes.py",
                "virtual_network/http_request.py",
                "vnc_api/request_skeleton.py",
                "vnc_api/constants.py",
                "vnc_api/__init__.py",
                "vnc_api/ttypes.py",
                "vnc_api/http_request.py",
    ],
    cmd  = """
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:acl_sandesh)
    cp acl/request_skeleton.py $(location acl/request_skeleton.py)
    cp acl/constants.py $(location acl/constants.py)
    cp acl/__init__.py $(location acl/__init__.py)
    cp acl/ttypes.py $(location acl/ttypes.py)
    cp acl/http_request.py $(location acl/http_request.py)
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:cfgm_cpuinfo.sandesh)
    cp cfgm_cpuinfo/request_skeleton.py $(location cfgm_cpuinfo/request_skeleton.py)
    cp cfgm_cpuinfo/constants.py $(location cfgm_cpuinfo/constants.py)
    cp cfgm_cpuinfo/__init__.py $(location cfgm_cpuinfo/__init__.py)
    cp cfgm_cpuinfo/ttypes.py $(location cfgm_cpuinfo/ttypes.py)
    cp cfgm_cpuinfo/http_request.py $(location cfgm_cpuinfo/http_request.py)
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:config_req.sandesh)
    cp config_req/request_skeleton.py $(location config_req/request_skeleton.py)
    cp config_req/constants.py $(location config_req/constants.py)
    cp config_req/__init__.py $(location config_req/__init__.py)
    cp config_req/ttypes.py $(location config_req/ttypes.py)
    cp config_req/http_request.py $(location config_req/http_request.py)
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:greenlets.sandesh)
    cp greenlets/request_skeleton.py $(location greenlets/request_skeleton.py)
    cp greenlets/constants.py $(location greenlets/constants.py)
    cp greenlets/__init__.py $(location greenlets/__init__.py)
    cp greenlets/ttypes.py $(location greenlets/ttypes.py)
    cp greenlets/http_request.py $(location greenlets/http_request.py)
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:msg_traces.sandesh)
    cp msg_traces/request_skeleton.py $(location msg_traces/request_skeleton.py)
    cp msg_traces/constants.py $(location msg_traces/constants.py)
    cp msg_traces/__init__.py $(location msg_traces/__init__.py)
    cp msg_traces/ttypes.py $(location msg_traces/ttypes.py)
    cp msg_traces/http_request.py $(location msg_traces/http_request.py)
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:physical_router_config.sandesh)
    cp physical_router_config/request_skeleton.py $(location physical_router_config/request_skeleton.py)
    cp physical_router_config/constants.py $(location physical_router_config/constants.py)
    cp physical_router_config/__init__.py $(location physical_router_config/__init__.py)
    cp physical_router_config/ttypes.py $(location physical_router_config/ttypes.py)
    cp physical_router_config/http_request.py $(location physical_router_config/http_request.py)
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:physical_router_config.sandesh)
    cp physical_router_config/request_skeleton.py $(location physical_router_config/request_skeleton.py)
    cp physical_router_config/constants.py $(location physical_router_config/constants.py)
    cp physical_router_config/__init__.py $(location physical_router_config/__init__.py)
    cp physical_router_config/ttypes.py $(location physical_router_config/ttypes.py)
    cp physical_router_config/http_request.py $(location physical_router_config/http_request.py)
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:physical_router.sandesh)
    cp physical_router/request_skeleton.py $(location physical_router/request_skeleton.py)
    cp physical_router/constants.py $(location physical_router/constants.py)
    cp physical_router/__init__.py $(location physical_router/__init__.py)
    cp physical_router/ttypes.py $(location physical_router/ttypes.py)
    cp physical_router/http_request.py $(location physical_router/http_request.py)
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:service_instance.sandesh)
    cp service_instance/request_skeleton.py $(location service_instance/request_skeleton.py)
    cp service_instance/constants.py $(location service_instance/constants.py)
    cp service_instance/__init__.py $(location service_instance/__init__.py)
    cp service_instance/ttypes.py $(location service_instance/ttypes.py)
    cp service_instance/http_request.py $(location service_instance/http_request.py)
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:service_status.sandesh)
    cp service_status/request_skeleton.py $(location service_status/request_skeleton.py)
    cp service_status/constants.py $(location service_status/constants.py)
    cp service_status/__init__.py $(location service_status/__init__.py)
    cp service_status/ttypes.py $(location service_status/ttypes.py)
    cp service_status/http_request.py $(location service_status/http_request.py)
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:virtual_machine.sandesh)
    cp virtual_machine/request_skeleton.py $(location virtual_machine/request_skeleton.py)
    cp virtual_machine/constants.py $(location virtual_machine/constants.py)
    cp virtual_machine/__init__.py $(location virtual_machine/__init__.py)
    cp virtual_machine/ttypes.py $(location virtual_machine/ttypes.py)
    cp virtual_machine/http_request.py $(location virtual_machine/http_request.py)
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:virtual_network.sandesh)
    cp virtual_network/request_skeleton.py $(location virtual_network/request_skeleton.py)
    cp virtual_network/constants.py $(location virtual_network/constants.py)
    cp virtual_network/__init__.py $(location virtual_network/__init__.py)
    cp virtual_network/ttypes.py $(location virtual_network/ttypes.py)
    cp virtual_network/http_request.py $(location virtual_network/http_request.py)
    ./$(location //contrail/sandesh:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:vnc_api.sandesh)
    cp vnc_api/request_skeleton.py $(location vnc_api/request_skeleton.py)
    cp vnc_api/constants.py $(location vnc_api/constants.py)
    cp vnc_api/__init__.py $(location vnc_api/__init__.py)
    cp vnc_api/ttypes.py $(location vnc_api/ttypes.py)
    cp vnc_api/http_request.py $(location vnc_api/http_request.py)
    """,
    tools = ["//contrail/sandesh:sandeshbin"],
)
#./build/bin/sandesh --gen py:new_style -I controller/src/ -I src/contrail-common -out /tmp controller/src/config/uve/acl.sandesh


py_library(
    name = "vnc_cfg_api_server",
    srcs = ["@contrail_repository//:vnc_cfg_api_server"],
)

py_library(
    name = "sandesh_libs",
    srcs = [":sandesh_acl"],
)

py_library(
    name = "cfgm_common",
    srcs = ["@contrail_repository//:cfgm_common",":sandesh_libs"],
    imports = [":sandesh_libs"],
)

DEPS = [
	"@contrail_repository//:cfgm_common",
	#":vnc_cfg_api_server",
	#":cfgm_common",
	#":sandesh_libs",
	"@contrail_repository//:vnc_cfg_api_server",
	"@contrail_api_repository//:vnc_api",
	"@sandesh_repository//:pysandesh",
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
        requirement("zipp"),
      ]


py_image(
    name = "config_api_debug",
    srcs = ["@contrail_repository//:src/config/api-server/vnc_cfg_api_server/vnc_cfg_api_server.py"],
    base = "//python2.7:debug",
    imports = ["sandesh"],
    #imports = [":sandesh_libs"],
    deps = DEPS,
    main = "vnc_cfg_api_server.py",
)

container_image(
    name = "configapi",
    base = ":config_api",
)

container_image(
    name = "configapi_debug",
    base = ":config_api_debug",
    #tars = [":contrail-libs-2"],
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
