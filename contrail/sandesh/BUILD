load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library", "cc_test")
load("@rules_bison//bison:bison.bzl", "bison_cc_library")
load("@rules_bison//bison:bison.bzl", "bison")
load("@rules_flex//flex:flex.bzl", "flex")

cc_library(
    name = "main",
    srcs = [ "@sandesh_repository//:main_cc", ],
    hdrs = [ "@sandesh_repository//:sandesh_headers", ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "md5",
    srcs = [ "@sandesh_repository//:md5_c", ],
    hdrs = [ "@sandesh_repository//:sandesh_headers", ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
#bison(
#    name = "sandeshy_bison",
#    src = "@sandesh_repository//:sandeshy_yy"
#)
genrule(
    name = "sandeshy_bison",
    srcs = ["@sandesh_repository//:sandeshy_yy"],
    outs = ["sandeshy.cc","sandeshy.hh"],
    #cmd = "bison -d --output=$@ $<",
    #cmd = "$(BISON) -d -o $@ $<",
    cmd = "$(BISON) --defines=$(location sandeshy.hh) -o $(location sandeshy.cc) $<",
    toolchains = [
        "@rules_bison//bison:current_bison_toolchain",
        "@rules_m4//m4:current_m4_toolchain",
    ],
)
cc_library(
    name = "sandeshy",
    srcs = [ ":sandeshy_bison" ],
    hdrs = [ "@sandesh_repository//:sandesh_headers", ],
    copts = ["--std=c99 -Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
genrule(
    name = "sandeshl_flex",
    srcs = ["@sandesh_repository//:sandeshl_ll"],
    outs = ["sandeshl.cc"],
    cmd = "flex -w -t $< > $@",
    #cmd = "$(FLEX) -w -t $< > $@",
    toolchains = [
        "@rules_flex//flex:current_flex_toolchain",
        "@rules_m4//m4:current_m4_toolchain",
    ],
)
#flex(
#    name = "sandeshl_flex",
#    src = "@sandesh_repository//:sandeshl_ll",
#)
cc_library(
    name = "sandeshl",
    srcs = [ ":sandeshl_flex" ],
    hdrs = [ "@sandesh_repository//:sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    deps = [":sandeshy"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)

cc_library(
    name = "t_cpp_generator",
    srcs = [ "@sandesh_repository//:t_cpp_generator_cc" ],
    hdrs = [ "@sandesh_repository//:sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "t_html_generator",
    srcs = [ "@sandesh_repository//:t_html_generator_cc" ],
    hdrs = [ "@sandesh_repository//:sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "t_generator",
    srcs = [ "@sandesh_repository//:t_generator_cc" ],
    hdrs = [ "@sandesh_repository//:sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "t_xsd_generator",
    srcs = [ "@sandesh_repository//:t_xsd_generator_cc" ],
    hdrs = [ "@sandesh_repository//:sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "t_c_generator",
    srcs = [ "@sandesh_repository//:t_c_generator_cc" ],
    hdrs = [ "@sandesh_repository//:sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "t_py_generator",
    srcs = [ "@sandesh_repository//:t_py_generator_cc" ],
    hdrs = [ "@sandesh_repository//:sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "t_doc_generator",
    srcs = [ "@sandesh_repository//:t_doc_generator_cc" ],
    hdrs = [ "@sandesh_repository//:sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "parse",
    srcs = [ "@sandesh_repository//:parse_cc",":md5" ],
    hdrs = [ "@sandesh_repository//:sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    deps = [":md5"],
    visibility = [ "//visibility:public" ],
)

cc_binary(
    name = "sandeshbin",
    #srcs = [
#	     ":main",
#	     ":md5",
#	     ":sandeshy",
#	     ":sandeshl",
#	     ":t_cpp_generator",
#	     ":t_html_generator",
#	     ":t_generator",
#	     ":t_xsd_generator",
#	     ":t_c_generator",
#	     ":t_py_generator",
#	     ":t_doc_generator",
#	     ":parse",
#	],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    deps = [
             ":main",
             ":md5",
             ":sandeshy",
             ":sandeshl",
             ":t_cpp_generator",
             ":t_html_generator",
             ":t_generator",
             ":t_xsd_generator",
             ":t_c_generator",
             ":t_py_generator",
             ":t_doc_generator",
             ":parse",
        ],
    linkstatic = 1,
    visibility = [ "//visibility:public" ],
)
