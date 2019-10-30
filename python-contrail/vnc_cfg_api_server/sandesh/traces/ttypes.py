#
# Autogenerated by Sandesh Compiler (1.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
# Copyright (c) 2013 Juniper Networks, Inc. All rights reserved.
#

from pysandesh.Thrift import TType, TMessageType, TException

from pysandesh.transport import TTransport
from pysandesh.protocol import TBinaryProtocol, TProtocol
try:
  from pysandesh.protocol import fastbinary
except:
  fastbinary = None

import cStringIO
import uuid
import netaddr
from sys import getsizeof
from itertools import chain
import bottle
from pysandesh import sandesh_base
from pysandesh.sandesh_http import SandeshHttp
from pysandesh.sandesh_uve import SandeshUVETypeMaps
from pysandesh.util import UTCTimestampUsec, UTCTimestampUsecToString
from pysandesh import util
from pysandesh.gen_py.sandesh.constants import *



class RestApiTrace(sandesh_base.SandeshTrace):

  thrift_spec = None

  def __init__(self, request_id=None, url=None, method=None, request_data=None, status=None, response_body=None, request_error=None, file=None, line=None, sandesh=sandesh_base.sandesh_global):
    sandesh_base.SandeshTrace.__init__(self, type=SandeshType.TRACE)
    self.request_id = request_id
    self.url = url
    self.method = method
    self.request_data = request_data
    self.status = status
    self.response_body = response_body
    self.request_error = request_error
    self.file = file
    self.line = line
    self._scope = sandesh.scope()
    self._module = sandesh.module()
    self._source = sandesh.source_id()
    self._node_type = sandesh.node_type()
    self._instance_id = sandesh.instance_id()
    self._seqnum = 0
    self._timestamp = UTCTimestampUsec()
    self._versionsig = 2028020299
    self._hints = 0

  def log(self, trace=False):
    log_str = cStringIO.StringIO()
    if trace:
      log_str.write(str(self._timestamp))
      log_str.write(' ')
    log_str.write(self.__class__.__name__ + ': ')
    if self.request_id is not None:
      log_str.write(self.request_id)
      log_str.write('  ')
    if self.url is not None:
      log_str.write(self.url)
      log_str.write('  ')
    if self.method is not None:
      log_str.write(self.method)
      log_str.write('  ')
    if self.request_data is not None:
      log_str.write(self.request_data)
      log_str.write('  ')
    if self.status is not None:
      log_str.write(self.status)
      log_str.write('  ')
    if self.response_body is not None:
      log_str.write(self.response_body)
      log_str.write('  ')
    if self.request_error is not None:
      log_str.write(self.request_error)
      log_str.write('  ')
    if self.file is not None:
      log_str.write(self.file)
      log_str.write('  ')
    if self.line is not None:
      log_str.write(str(self.line))
      log_str.write('  ')
    return log_str.getvalue()

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return -1
    read_cnt = 0
    (length, sandesh_name) = iprot.readSandeshBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          (length, self.request_id) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          (length, self.url) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          (length, self.method) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          (length, self.request_data) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          (length, self.status) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          (length, self.response_body) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          (length, self.request_error) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == -32768:
        if ftype == TType.STRING:
          (length, self.file) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == -32767:
        if ftype == TType.I32:
          (length, self.line) = iprot.readI32();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readSandeshEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeSandeshBegin(self.__class__.__name__) < 0: return -1
    if self.file is not None:
      annotations = {}
      if oprot.writeFieldBegin('file', TType.STRING, -32768, annotations) < 0: return -1
      if oprot.writeString(self.file) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.line is not None:
      annotations = {}
      if oprot.writeFieldBegin('line', TType.I32, -32767, annotations) < 0: return -1
      if oprot.writeI32(self.line) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.request_id is not None:
      annotations = {}
      if oprot.writeFieldBegin('request_id', TType.STRING, 1, annotations) < 0: return -1
      if oprot.writeString(self.request_id) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.url is not None:
      annotations = {}
      if oprot.writeFieldBegin('url', TType.STRING, 2, annotations) < 0: return -1
      if oprot.writeString(self.url) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.method is not None:
      annotations = {}
      if oprot.writeFieldBegin('method', TType.STRING, 3, annotations) < 0: return -1
      if oprot.writeString(self.method) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.request_data is not None:
      annotations = {}
      if oprot.writeFieldBegin('request_data', TType.STRING, 4, annotations) < 0: return -1
      if oprot.writeString(self.request_data) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.status is not None:
      annotations = {}
      if oprot.writeFieldBegin('status', TType.STRING, 5, annotations) < 0: return -1
      if oprot.writeString(self.status) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.response_body is not None:
      annotations = {}
      if oprot.writeFieldBegin('response_body', TType.STRING, 6, annotations) < 0: return -1
      if oprot.writeString(self.response_body) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.request_error is not None:
      annotations = {}
      if oprot.writeFieldBegin('request_error', TType.STRING, 7, annotations) < 0: return -1
      if oprot.writeString(self.request_error) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeSandeshEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def compare(self, other):
    if not isinstance(other, self.__class__):
      return False
    if self.file != other.file:
      return False
    if self.line != other.line:
      return False
    if self.request_id != other.request_id:
      return False
    if self.url != other.url:
      return False
    if self.method != other.method:
      return False
    if self.request_data != other.request_data:
      return False
    if self.status != other.status:
      return False
    if self.response_body != other.response_body:
      return False
    if self.request_error != other.request_error:
      return False
    return True

  def __sizeof__(self):
    size = 0
    if self.request_id is not None:
      size += getsizeof(self.request_id)
    if self.url is not None:
      size += getsizeof(self.url)
    if self.method is not None:
      size += getsizeof(self.method)
    if self.request_data is not None:
      size += getsizeof(self.request_data)
    if self.status is not None:
      size += getsizeof(self.status)
    if self.response_body is not None:
      size += getsizeof(self.response_body)
    if self.request_error is not None:
      size += getsizeof(self.request_error)
    if self.file is not None:
      size += getsizeof(self.file)
    if self.line is not None:
      size += getsizeof(self.line)
    return size

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class DBRequestTrace(sandesh_base.SandeshTrace):

  thrift_spec = None

  def __init__(self, request_id=None, operation=None, body=None, error=None, file=None, line=None, sandesh=sandesh_base.sandesh_global):
    sandesh_base.SandeshTrace.__init__(self, type=SandeshType.TRACE)
    self.request_id = request_id
    self.operation = operation
    self.body = body
    self.error = error
    self.file = file
    self.line = line
    self._scope = sandesh.scope()
    self._module = sandesh.module()
    self._source = sandesh.source_id()
    self._node_type = sandesh.node_type()
    self._instance_id = sandesh.instance_id()
    self._seqnum = 0
    self._timestamp = UTCTimestampUsec()
    self._versionsig = 3446691644
    self._hints = 0

  def log(self, trace=False):
    log_str = cStringIO.StringIO()
    if trace:
      log_str.write(str(self._timestamp))
      log_str.write(' ')
    log_str.write(self.__class__.__name__ + ': ')
    if self.request_id is not None:
      log_str.write(self.request_id)
      log_str.write('  ')
    if self.operation is not None:
      log_str.write(self.operation)
      log_str.write('  ')
    if self.body is not None:
      log_str.write(self.body)
      log_str.write('  ')
    if self.error is not None:
      log_str.write(self.error)
      log_str.write('  ')
    if self.file is not None:
      log_str.write(self.file)
      log_str.write('  ')
    if self.line is not None:
      log_str.write(str(self.line))
      log_str.write('  ')
    return log_str.getvalue()

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return -1
    read_cnt = 0
    (length, sandesh_name) = iprot.readSandeshBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          (length, self.request_id) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          (length, self.operation) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          (length, self.body) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          (length, self.error) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == -32768:
        if ftype == TType.STRING:
          (length, self.file) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == -32767:
        if ftype == TType.I32:
          (length, self.line) = iprot.readI32();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readSandeshEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeSandeshBegin(self.__class__.__name__) < 0: return -1
    if self.file is not None:
      annotations = {}
      if oprot.writeFieldBegin('file', TType.STRING, -32768, annotations) < 0: return -1
      if oprot.writeString(self.file) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.line is not None:
      annotations = {}
      if oprot.writeFieldBegin('line', TType.I32, -32767, annotations) < 0: return -1
      if oprot.writeI32(self.line) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.request_id is not None:
      annotations = {}
      if oprot.writeFieldBegin('request_id', TType.STRING, 1, annotations) < 0: return -1
      if oprot.writeString(self.request_id) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.operation is not None:
      annotations = {}
      if oprot.writeFieldBegin('operation', TType.STRING, 2, annotations) < 0: return -1
      if oprot.writeString(self.operation) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.body is not None:
      annotations = {}
      if oprot.writeFieldBegin('body', TType.STRING, 3, annotations) < 0: return -1
      if oprot.writeString(self.body) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.error is not None:
      annotations = {}
      if oprot.writeFieldBegin('error', TType.STRING, 4, annotations) < 0: return -1
      if oprot.writeString(self.error) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeSandeshEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def compare(self, other):
    if not isinstance(other, self.__class__):
      return False
    if self.file != other.file:
      return False
    if self.line != other.line:
      return False
    if self.request_id != other.request_id:
      return False
    if self.operation != other.operation:
      return False
    if self.body != other.body:
      return False
    if self.error != other.error:
      return False
    return True

  def __sizeof__(self):
    size = 0
    if self.request_id is not None:
      size += getsizeof(self.request_id)
    if self.operation is not None:
      size += getsizeof(self.operation)
    if self.body is not None:
      size += getsizeof(self.body)
    if self.error is not None:
      size += getsizeof(self.error)
    if self.file is not None:
      size += getsizeof(self.file)
    if self.line is not None:
      size += getsizeof(self.line)
    return size

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class MessageBusNotifyTrace(sandesh_base.SandeshTrace):

  thrift_spec = None

  def __init__(self, request_id=None, operation=None, body=None, error=None, file=None, line=None, sandesh=sandesh_base.sandesh_global):
    sandesh_base.SandeshTrace.__init__(self, type=SandeshType.TRACE)
    self.request_id = request_id
    self.operation = operation
    self.body = body
    self.error = error
    self.file = file
    self.line = line
    self._scope = sandesh.scope()
    self._module = sandesh.module()
    self._source = sandesh.source_id()
    self._node_type = sandesh.node_type()
    self._instance_id = sandesh.instance_id()
    self._seqnum = 0
    self._timestamp = UTCTimestampUsec()
    self._versionsig = 3446691644
    self._hints = 0

  def log(self, trace=False):
    log_str = cStringIO.StringIO()
    if trace:
      log_str.write(str(self._timestamp))
      log_str.write(' ')
    log_str.write(self.__class__.__name__ + ': ')
    if self.request_id is not None:
      log_str.write(self.request_id)
      log_str.write('  ')
    if self.operation is not None:
      log_str.write(self.operation)
      log_str.write('  ')
    if self.body is not None:
      log_str.write(self.body)
      log_str.write('  ')
    if self.error is not None:
      log_str.write(self.error)
      log_str.write('  ')
    if self.file is not None:
      log_str.write(self.file)
      log_str.write('  ')
    if self.line is not None:
      log_str.write(str(self.line))
      log_str.write('  ')
    return log_str.getvalue()

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return -1
    read_cnt = 0
    (length, sandesh_name) = iprot.readSandeshBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          (length, self.request_id) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          (length, self.operation) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          (length, self.body) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          (length, self.error) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == -32768:
        if ftype == TType.STRING:
          (length, self.file) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == -32767:
        if ftype == TType.I32:
          (length, self.line) = iprot.readI32();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readSandeshEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeSandeshBegin(self.__class__.__name__) < 0: return -1
    if self.file is not None:
      annotations = {}
      if oprot.writeFieldBegin('file', TType.STRING, -32768, annotations) < 0: return -1
      if oprot.writeString(self.file) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.line is not None:
      annotations = {}
      if oprot.writeFieldBegin('line', TType.I32, -32767, annotations) < 0: return -1
      if oprot.writeI32(self.line) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.request_id is not None:
      annotations = {}
      if oprot.writeFieldBegin('request_id', TType.STRING, 1, annotations) < 0: return -1
      if oprot.writeString(self.request_id) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.operation is not None:
      annotations = {}
      if oprot.writeFieldBegin('operation', TType.STRING, 2, annotations) < 0: return -1
      if oprot.writeString(self.operation) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.body is not None:
      annotations = {}
      if oprot.writeFieldBegin('body', TType.STRING, 3, annotations) < 0: return -1
      if oprot.writeString(self.body) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.error is not None:
      annotations = {}
      if oprot.writeFieldBegin('error', TType.STRING, 4, annotations) < 0: return -1
      if oprot.writeString(self.error) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeSandeshEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def compare(self, other):
    if not isinstance(other, self.__class__):
      return False
    if self.file != other.file:
      return False
    if self.line != other.line:
      return False
    if self.request_id != other.request_id:
      return False
    if self.operation != other.operation:
      return False
    if self.body != other.body:
      return False
    if self.error != other.error:
      return False
    return True

  def __sizeof__(self):
    size = 0
    if self.request_id is not None:
      size += getsizeof(self.request_id)
    if self.operation is not None:
      size += getsizeof(self.operation)
    if self.body is not None:
      size += getsizeof(self.body)
    if self.error is not None:
      size += getsizeof(self.error)
    if self.file is not None:
      size += getsizeof(self.file)
    if self.line is not None:
      size += getsizeof(self.line)
    return size

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)


_SANDESH_REQUEST_LIST = [
]


_SANDESH_UVE_LIST = [
]


_SANDESH_ALARM_LIST = [
]
