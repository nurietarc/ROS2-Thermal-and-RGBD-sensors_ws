# generated from rosidl_generator_py/resource/_idl.py.em
# with input from optris_drivers2:srv/TemperatureRange.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TemperatureRange_Request(type):
    """Metaclass of message 'TemperatureRange_Request'."""

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
                'optris_drivers2.srv.TemperatureRange_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__temperature_range__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__temperature_range__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__temperature_range__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__temperature_range__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__temperature_range__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TemperatureRange_Request(metaclass=Metaclass_TemperatureRange_Request):
    """Message class 'TemperatureRange_Request'."""

    __slots__ = [
        '_temperature_range_min',
        '_temperature_range_max',
    ]

    _fields_and_field_types = {
        'temperature_range_min': 'int16',
        'temperature_range_max': 'int16',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.temperature_range_min = kwargs.get('temperature_range_min', int())
        self.temperature_range_max = kwargs.get('temperature_range_max', int())

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
        if self.temperature_range_min != other.temperature_range_min:
            return False
        if self.temperature_range_max != other.temperature_range_max:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def temperature_range_min(self):
        """Message field 'temperature_range_min'."""
        return self._temperature_range_min

    @temperature_range_min.setter
    def temperature_range_min(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'temperature_range_min' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'temperature_range_min' field must be an integer in [-32768, 32767]"
        self._temperature_range_min = value

    @builtins.property
    def temperature_range_max(self):
        """Message field 'temperature_range_max'."""
        return self._temperature_range_max

    @temperature_range_max.setter
    def temperature_range_max(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'temperature_range_max' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'temperature_range_max' field must be an integer in [-32768, 32767]"
        self._temperature_range_max = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_TemperatureRange_Response(type):
    """Metaclass of message 'TemperatureRange_Response'."""

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
                'optris_drivers2.srv.TemperatureRange_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__temperature_range__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__temperature_range__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__temperature_range__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__temperature_range__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__temperature_range__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TemperatureRange_Response(metaclass=Metaclass_TemperatureRange_Response):
    """Message class 'TemperatureRange_Response'."""

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


class Metaclass_TemperatureRange(type):
    """Metaclass of service 'TemperatureRange'."""

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
                'optris_drivers2.srv.TemperatureRange')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__temperature_range

            from optris_drivers2.srv import _temperature_range
            if _temperature_range.Metaclass_TemperatureRange_Request._TYPE_SUPPORT is None:
                _temperature_range.Metaclass_TemperatureRange_Request.__import_type_support__()
            if _temperature_range.Metaclass_TemperatureRange_Response._TYPE_SUPPORT is None:
                _temperature_range.Metaclass_TemperatureRange_Response.__import_type_support__()


class TemperatureRange(metaclass=Metaclass_TemperatureRange):
    from optris_drivers2.srv._temperature_range import TemperatureRange_Request as Request
    from optris_drivers2.srv._temperature_range import TemperatureRange_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
