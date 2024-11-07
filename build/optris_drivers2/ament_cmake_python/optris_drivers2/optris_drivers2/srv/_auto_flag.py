# generated from rosidl_generator_py/resource/_idl.py.em
# with input from optris_drivers2:srv/AutoFlag.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AutoFlag_Request(type):
    """Metaclass of message 'AutoFlag_Request'."""

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
                'optris_drivers2.srv.AutoFlag_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__auto_flag__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__auto_flag__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__auto_flag__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__auto_flag__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__auto_flag__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AutoFlag_Request(metaclass=Metaclass_AutoFlag_Request):
    """Message class 'AutoFlag_Request'."""

    __slots__ = [
        '_auto_flag',
    ]

    _fields_and_field_types = {
        'auto_flag': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.auto_flag = kwargs.get('auto_flag', bool())

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
        if self.auto_flag != other.auto_flag:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def auto_flag(self):
        """Message field 'auto_flag'."""
        return self._auto_flag

    @auto_flag.setter
    def auto_flag(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'auto_flag' field must be of type 'bool'"
        self._auto_flag = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AutoFlag_Response(type):
    """Metaclass of message 'AutoFlag_Response'."""

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
                'optris_drivers2.srv.AutoFlag_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__auto_flag__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__auto_flag__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__auto_flag__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__auto_flag__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__auto_flag__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AutoFlag_Response(metaclass=Metaclass_AutoFlag_Response):
    """Message class 'AutoFlag_Response'."""

    __slots__ = [
        '_is_auto_flag_active',
    ]

    _fields_and_field_types = {
        'is_auto_flag_active': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.is_auto_flag_active = kwargs.get('is_auto_flag_active', bool())

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
        if self.is_auto_flag_active != other.is_auto_flag_active:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def is_auto_flag_active(self):
        """Message field 'is_auto_flag_active'."""
        return self._is_auto_flag_active

    @is_auto_flag_active.setter
    def is_auto_flag_active(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_auto_flag_active' field must be of type 'bool'"
        self._is_auto_flag_active = value


class Metaclass_AutoFlag(type):
    """Metaclass of service 'AutoFlag'."""

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
                'optris_drivers2.srv.AutoFlag')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__auto_flag

            from optris_drivers2.srv import _auto_flag
            if _auto_flag.Metaclass_AutoFlag_Request._TYPE_SUPPORT is None:
                _auto_flag.Metaclass_AutoFlag_Request.__import_type_support__()
            if _auto_flag.Metaclass_AutoFlag_Response._TYPE_SUPPORT is None:
                _auto_flag.Metaclass_AutoFlag_Response.__import_type_support__()


class AutoFlag(metaclass=Metaclass_AutoFlag):
    from optris_drivers2.srv._auto_flag import AutoFlag_Request as Request
    from optris_drivers2.srv._auto_flag import AutoFlag_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
