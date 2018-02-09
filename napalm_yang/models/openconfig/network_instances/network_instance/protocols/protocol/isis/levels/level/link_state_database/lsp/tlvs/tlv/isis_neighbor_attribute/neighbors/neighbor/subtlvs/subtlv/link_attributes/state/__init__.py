
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/isis-neighbor-attribute/neighbors/neighbor/subtlvs/subtlv/link-attributes/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS Extended Reachability sub-TLV
19.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__local_protection',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__local_protection = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINK_EXCLUDED': {}, u'LOCAL_PROTECTION': {}},)), is_leaf=False, yang_name="local-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'isis-neighbor-attribute', u'neighbors', u'neighbor', u'subtlvs', u'subtlv', u'link-attributes', u'state']

  def _get_local_protection(self):
    """
    Getter method for local_protection, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/isis_neighbor_attribute/neighbors/neighbor/subtlvs/subtlv/link_attributes/state/local_protection (enumeration)

    YANG Description: Link local-protection attributes.
    """
    return self.__local_protection
      
  def _set_local_protection(self, v, load=False):
    """
    Setter method for local_protection, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/isis_neighbor_attribute/neighbors/neighbor/subtlvs/subtlv/link_attributes/state/local_protection (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_protection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_protection() directly.

    YANG Description: Link local-protection attributes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINK_EXCLUDED': {}, u'LOCAL_PROTECTION': {}},)), is_leaf=False, yang_name="local-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_protection must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINK_EXCLUDED': {}, u'LOCAL_PROTECTION': {}},)), is_leaf=False, yang_name="local-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
        })

    self.__local_protection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_protection(self):
    self.__local_protection = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINK_EXCLUDED': {}, u'LOCAL_PROTECTION': {}},)), is_leaf=False, yang_name="local-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)

  local_protection = __builtin__.property(_get_local_protection)


  _pyangbind_elements = {'local_protection': local_protection, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/isis-neighbor-attribute/neighbors/neighbor/subtlvs/subtlv/link-attributes/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS Extended Reachability sub-TLV
19.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__local_protection',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__local_protection = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINK_EXCLUDED': {}, u'LOCAL_PROTECTION': {}},)), is_leaf=False, yang_name="local-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'isis-neighbor-attribute', u'neighbors', u'neighbor', u'subtlvs', u'subtlv', u'link-attributes', u'state']

  def _get_local_protection(self):
    """
    Getter method for local_protection, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/isis_neighbor_attribute/neighbors/neighbor/subtlvs/subtlv/link_attributes/state/local_protection (enumeration)

    YANG Description: Link local-protection attributes.
    """
    return self.__local_protection
      
  def _set_local_protection(self, v, load=False):
    """
    Setter method for local_protection, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/isis_neighbor_attribute/neighbors/neighbor/subtlvs/subtlv/link_attributes/state/local_protection (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_protection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_protection() directly.

    YANG Description: Link local-protection attributes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINK_EXCLUDED': {}, u'LOCAL_PROTECTION': {}},)), is_leaf=False, yang_name="local-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_protection must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINK_EXCLUDED': {}, u'LOCAL_PROTECTION': {}},)), is_leaf=False, yang_name="local-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
        })

    self.__local_protection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_protection(self):
    self.__local_protection = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINK_EXCLUDED': {}, u'LOCAL_PROTECTION': {}},)), is_leaf=False, yang_name="local-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)

  local_protection = __builtin__.property(_get_local_protection)


  _pyangbind_elements = {'local_protection': local_protection, }

