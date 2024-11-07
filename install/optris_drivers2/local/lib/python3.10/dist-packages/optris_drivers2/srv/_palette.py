# generated from rosidl_generator_py/resource/_idl.py.em
# with input from optris_drivers2:srv/Palette.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Palette_Request(type):
    """Metaclass of message 'Palette_Request'."""

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
                'optris_drivers2.srv.Palette_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__palette__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__palette__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__palette__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__palette__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__palette__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Palette_Request(metaclass=Metaclass_Palette_Request):
    """Message class 'Palette_Request'."""

    __slots__ = [
        '_palette',
        '_palette_scaling',
        '_temperature_min',
        '_temperature_max',
    ]

    _fields_and_field_types = {
        'palette': 'int16',
        'palette_scaling': 'int16',
        'temperature_min': 'float',
        'temperature_max': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.palette = kwargs.get('palette', int())
        self.palette_scaling = kwargs.get('palette_scaling', int())
        self.temperature_min = kwargs.get('temperature_min', float())
        self.temperature_max = kwargs.get('temperature_max', float())

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
        if self.palette != other.palette:
            return False
        if self.palette_scaling != other.palette_scaling:
            return False
        if self.temperature_min != other.temperature_min:
            return False
        if self.temperature_max != other.temperature_max:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def palette(self):
        """Message field 'palette'."""
        return self._palette

    @palette.setter
    def palette(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'palette' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'palette' field must be an integer in [-32768, 32767]"
        self._palette = value

    @builtins.property
    def palette_scaling(self):
        """Message field 'palette_scaling'."""
        return self._palette_scaling

    @palette_scaling.setter
    def palette_scaling(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'palette_scaling' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'palette_scaling' field must be an integer in [-32768, 32767]"
        self._palette_scaling = value

    @builtins.property
    def temperature_min(self):
        """Message field 'temperature_min'."""
        return self._temperature_min

    @temperature_min.setter
    def temperature_min(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'temperature_min' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'temperature_min' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._temperature_min = value

    @builtins.property
    def temperature_max(self):
        """Message field 'temperature_max'."""
        return self._temperature_max

    @temperature_max.setter
    def temperature_max(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'temperature_max' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'temperature_max' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._temperature_max = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Palette_Response(type):
    """Metaclass of message 'Palette_Response'."""

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
                'optris_drivers2.srv.Palette_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__palette__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__palette__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__palette__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__palette__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__palette__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Palette_Response(metaclass=Metaclass_Palette_Response):
    """Message class 'Palette_Response'."""

    __slots__ = [
        '_success',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())

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
        if self.success != other.success:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value


class Metaclass_Palette(type):
    """Metaclass of service 'Palette'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('optris_drivers2')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'optris_drivers2.srv.Palette')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__palette

            from optris_drivers2.srv import _palette
            if _palette.Metaclass_Palette_Request._TYPE_SUPPORT is None:
                _palette.Metaclass_Palette_Request.__import_type_support__()
            if _palette.Metaclass_Palette_Response._TYPE_SUPPORT is None:
                _palette.Metaclass_Palette_Response.__import_type_support__()


class Palette(metaclass=Metaclass_Palette):
    from optris_drivers2.srv._palette import Palette_Request as Request
    from optris_drivers2.srv._palette import Palette_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
