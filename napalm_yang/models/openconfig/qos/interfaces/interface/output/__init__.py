
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

from . import interface_ref
from . import classifers
from . import queues
from . import scheduler_policy
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos - based on the path /qos/interfaces/interface/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for QoS data related to the egress
interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_ref','__classifers','__queues','__scheduler_policy',)

  _yang_name = 'output'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__scheduler_policy = YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__queues = YANGDynClass(base=queues.queues, is_container='container', yang_name="queues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__classifers = YANGDynClass(base=classifers.classifers, is_container='container', yang_name="classifers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)

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
      return [u'qos', u'interfaces', u'interface', u'output']

  def _get_interface_ref(self):
    """
    Getter method for interface_ref, mapped from YANG variable /qos/interfaces/interface/output/interface_ref (container)

    YANG Description: Reference to an interface or subinterface
    """
    return self.__interface_ref
      
  def _set_interface_ref(self, v, load=False):
    """
    Setter method for interface_ref, mapped from YANG variable /qos/interfaces/interface/output/interface_ref (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_ref is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_ref() directly.

    YANG Description: Reference to an interface or subinterface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_ref must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__interface_ref = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_ref(self):
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_classifers(self):
    """
    Getter method for classifers, mapped from YANG variable /qos/interfaces/interface/output/classifers (container)

    YANG Description: Classifiers to be applied to the interface.
    """
    return self.__classifers
      
  def _set_classifers(self, v, load=False):
    """
    Setter method for classifers, mapped from YANG variable /qos/interfaces/interface/output/classifers (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_classifers is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_classifers() directly.

    YANG Description: Classifiers to be applied to the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=classifers.classifers, is_container='container', yang_name="classifers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """classifers must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=classifers.classifers, is_container='container', yang_name="classifers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__classifers = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_classifers(self):
    self.__classifers = YANGDynClass(base=classifers.classifers, is_container='container', yang_name="classifers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_queues(self):
    """
    Getter method for queues, mapped from YANG variable /qos/interfaces/interface/output/queues (container)

    YANG Description: Surrounding container for a list of queues that are
instantiated on an interface.
    """
    return self.__queues
      
  def _set_queues(self, v, load=False):
    """
    Setter method for queues, mapped from YANG variable /qos/interfaces/interface/output/queues (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queues is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queues() directly.

    YANG Description: Surrounding container for a list of queues that are
instantiated on an interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=queues.queues, is_container='container', yang_name="queues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queues must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=queues.queues, is_container='container', yang_name="queues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__queues = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queues(self):
    self.__queues = YANGDynClass(base=queues.queues, is_container='container', yang_name="queues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_scheduler_policy(self):
    """
    Getter method for scheduler_policy, mapped from YANG variable /qos/interfaces/interface/output/scheduler_policy (container)

    YANG Description: Scheduler policy associated with the interface.
    """
    return self.__scheduler_policy
      
  def _set_scheduler_policy(self, v, load=False):
    """
    Setter method for scheduler_policy, mapped from YANG variable /qos/interfaces/interface/output/scheduler_policy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_scheduler_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_scheduler_policy() directly.

    YANG Description: Scheduler policy associated with the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """scheduler_policy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__scheduler_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_scheduler_policy(self):
    self.__scheduler_policy = YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)

  interface_ref = __builtin__.property(_get_interface_ref, _set_interface_ref)
  classifers = __builtin__.property(_get_classifers, _set_classifers)
  queues = __builtin__.property(_get_queues, _set_queues)
  scheduler_policy = __builtin__.property(_get_scheduler_policy, _set_scheduler_policy)


  _pyangbind_elements = {'interface_ref': interface_ref, 'classifers': classifers, 'queues': queues, 'scheduler_policy': scheduler_policy, }


from . import interface_ref
from . import classifers
from . import queues
from . import scheduler_policy
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-interfaces - based on the path /qos/interfaces/interface/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for QoS data related to the egress
interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_ref','__classifers','__queues','__scheduler_policy',)

  _yang_name = 'output'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__scheduler_policy = YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__queues = YANGDynClass(base=queues.queues, is_container='container', yang_name="queues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__classifers = YANGDynClass(base=classifers.classifers, is_container='container', yang_name="classifers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)

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
      return [u'qos', u'interfaces', u'interface', u'output']

  def _get_interface_ref(self):
    """
    Getter method for interface_ref, mapped from YANG variable /qos/interfaces/interface/output/interface_ref (container)

    YANG Description: Reference to an interface or subinterface
    """
    return self.__interface_ref
      
  def _set_interface_ref(self, v, load=False):
    """
    Setter method for interface_ref, mapped from YANG variable /qos/interfaces/interface/output/interface_ref (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_ref is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_ref() directly.

    YANG Description: Reference to an interface or subinterface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_ref must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__interface_ref = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_ref(self):
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_classifers(self):
    """
    Getter method for classifers, mapped from YANG variable /qos/interfaces/interface/output/classifers (container)

    YANG Description: Classifiers to be applied to the interface.
    """
    return self.__classifers
      
  def _set_classifers(self, v, load=False):
    """
    Setter method for classifers, mapped from YANG variable /qos/interfaces/interface/output/classifers (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_classifers is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_classifers() directly.

    YANG Description: Classifiers to be applied to the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=classifers.classifers, is_container='container', yang_name="classifers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """classifers must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=classifers.classifers, is_container='container', yang_name="classifers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__classifers = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_classifers(self):
    self.__classifers = YANGDynClass(base=classifers.classifers, is_container='container', yang_name="classifers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_queues(self):
    """
    Getter method for queues, mapped from YANG variable /qos/interfaces/interface/output/queues (container)

    YANG Description: Surrounding container for a list of queues that are
instantiated on an interface.
    """
    return self.__queues
      
  def _set_queues(self, v, load=False):
    """
    Setter method for queues, mapped from YANG variable /qos/interfaces/interface/output/queues (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queues is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queues() directly.

    YANG Description: Surrounding container for a list of queues that are
instantiated on an interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=queues.queues, is_container='container', yang_name="queues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queues must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=queues.queues, is_container='container', yang_name="queues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__queues = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queues(self):
    self.__queues = YANGDynClass(base=queues.queues, is_container='container', yang_name="queues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_scheduler_policy(self):
    """
    Getter method for scheduler_policy, mapped from YANG variable /qos/interfaces/interface/output/scheduler_policy (container)

    YANG Description: Scheduler policy associated with the interface.
    """
    return self.__scheduler_policy
      
  def _set_scheduler_policy(self, v, load=False):
    """
    Setter method for scheduler_policy, mapped from YANG variable /qos/interfaces/interface/output/scheduler_policy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_scheduler_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_scheduler_policy() directly.

    YANG Description: Scheduler policy associated with the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """scheduler_policy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__scheduler_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_scheduler_policy(self):
    self.__scheduler_policy = YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)

  interface_ref = __builtin__.property(_get_interface_ref, _set_interface_ref)
  classifers = __builtin__.property(_get_classifers, _set_classifers)
  queues = __builtin__.property(_get_queues, _set_queues)
  scheduler_policy = __builtin__.property(_get_scheduler_policy, _set_scheduler_policy)


  _pyangbind_elements = {'interface_ref': interface_ref, 'classifers': classifers, 'queues': queues, 'scheduler_policy': scheduler_policy, }


from . import interface_ref
from . import classifers
from . import queues
from . import scheduler_policy
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-elements - based on the path /qos/interfaces/interface/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for QoS data related to the egress
interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_ref','__classifers','__queues','__scheduler_policy',)

  _yang_name = 'output'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__scheduler_policy = YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__queues = YANGDynClass(base=queues.queues, is_container='container', yang_name="queues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__classifers = YANGDynClass(base=classifers.classifers, is_container='container', yang_name="classifers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)

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
      return [u'qos', u'interfaces', u'interface', u'output']

  def _get_interface_ref(self):
    """
    Getter method for interface_ref, mapped from YANG variable /qos/interfaces/interface/output/interface_ref (container)

    YANG Description: Reference to an interface or subinterface
    """
    return self.__interface_ref
      
  def _set_interface_ref(self, v, load=False):
    """
    Setter method for interface_ref, mapped from YANG variable /qos/interfaces/interface/output/interface_ref (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_ref is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_ref() directly.

    YANG Description: Reference to an interface or subinterface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_ref must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__interface_ref = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_ref(self):
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_classifers(self):
    """
    Getter method for classifers, mapped from YANG variable /qos/interfaces/interface/output/classifers (container)

    YANG Description: Classifiers to be applied to the interface.
    """
    return self.__classifers
      
  def _set_classifers(self, v, load=False):
    """
    Setter method for classifers, mapped from YANG variable /qos/interfaces/interface/output/classifers (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_classifers is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_classifers() directly.

    YANG Description: Classifiers to be applied to the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=classifers.classifers, is_container='container', yang_name="classifers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """classifers must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=classifers.classifers, is_container='container', yang_name="classifers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__classifers = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_classifers(self):
    self.__classifers = YANGDynClass(base=classifers.classifers, is_container='container', yang_name="classifers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_queues(self):
    """
    Getter method for queues, mapped from YANG variable /qos/interfaces/interface/output/queues (container)

    YANG Description: Surrounding container for a list of queues that are
instantiated on an interface.
    """
    return self.__queues
      
  def _set_queues(self, v, load=False):
    """
    Setter method for queues, mapped from YANG variable /qos/interfaces/interface/output/queues (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queues is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queues() directly.

    YANG Description: Surrounding container for a list of queues that are
instantiated on an interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=queues.queues, is_container='container', yang_name="queues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queues must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=queues.queues, is_container='container', yang_name="queues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__queues = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queues(self):
    self.__queues = YANGDynClass(base=queues.queues, is_container='container', yang_name="queues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_scheduler_policy(self):
    """
    Getter method for scheduler_policy, mapped from YANG variable /qos/interfaces/interface/output/scheduler_policy (container)

    YANG Description: Scheduler policy associated with the interface.
    """
    return self.__scheduler_policy
      
  def _set_scheduler_policy(self, v, load=False):
    """
    Setter method for scheduler_policy, mapped from YANG variable /qos/interfaces/interface/output/scheduler_policy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_scheduler_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_scheduler_policy() directly.

    YANG Description: Scheduler policy associated with the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """scheduler_policy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__scheduler_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_scheduler_policy(self):
    self.__scheduler_policy = YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)

  interface_ref = __builtin__.property(_get_interface_ref, _set_interface_ref)
  classifers = __builtin__.property(_get_classifers, _set_classifers)
  queues = __builtin__.property(_get_queues, _set_queues)
  scheduler_policy = __builtin__.property(_get_scheduler_policy, _set_scheduler_policy)


  _pyangbind_elements = {'interface_ref': interface_ref, 'classifers': classifers, 'queues': queues, 'scheduler_policy': scheduler_policy, }

