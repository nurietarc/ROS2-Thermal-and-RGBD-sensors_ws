# generated from rosidl_generator_py/resource/_idl.py.em
# with input from optris_drivers2:msg/Temperature.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Temperature(type):
    """Metaclass of message 'Temperature'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('optris_drivers2')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'optris_drivers2.msg.Temperature')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__temperature
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__temperature
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__temperature
            cls._TYPE_SUPPORT = module.type_support_msg__msg__temperature
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__temperature

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Temperature(metaclass=Metaclass_Temperature):
    """Message class 'Temperature'."""

    __slots__ = [
        '_header',
        '_temperature_flag',
        '_temperature_box',
        '_temperature_chip',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'temperature_flag': 'float',
        'temperature_box': 'float',
        'temperature_chip': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.temperature_flag = kwargs.get('temperature_flag', float())
        self.temperature_box = kwargs.get('temperature_box', float())
        self.temperature_chip = kwargs.get('temperature_chip', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.temperature_flag != other.temperature_flag:
            return False
        if self.temperature_box != other.temperature_box:
            return False
        if self.temperature_chip != other.temperature_chip:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def temperature_flag(self):
        """Message field 'temperature_flag'."""
        return self._temperature_flag

    @temperature_flag.setter
    def temperature_flag(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'temperature_flag' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'temperature_flag' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._temperature_flag = value

    @builtins.property
    def temperature_box(self):
        """Message field 'temperature_box'."""
        return self._temperature_box

    @temperature_box.setter
    def temperature_box(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'temperature_box' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'temperature_box' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._temperature_box = value

    @builtins.property
    def temperature_chip(self):
        """Message field 'temperature_chip'."""
        return self._temperature_chip

    @temperature_chip.setter
    def temperature_chip(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'temperature_chip' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'temperature_chip' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._temperature_chip = value
