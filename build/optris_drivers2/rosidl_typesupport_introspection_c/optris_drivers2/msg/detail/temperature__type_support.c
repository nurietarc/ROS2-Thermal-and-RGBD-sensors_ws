// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from optris_drivers2:msg/Temperature.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "optris_drivers2/msg/detail/temperature__rosidl_typesupport_introspection_c.h"
#include "optris_drivers2/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "optris_drivers2/msg/detail/temperature__functions.h"
#include "optris_drivers2/msg/detail/temperature__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  optris_drivers2__msg__Temperature__init(message_memory);
}

void optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_fini_function(void * message_memory)
{
  optris_drivers2__msg__Temperature__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_message_member_array[4] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(optris_drivers2__msg__Temperature, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "temperature_flag",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(optris_drivers2__msg__Temperature, temperature_flag),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "temperature_box",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(optris_drivers2__msg__Temperature, temperature_box),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "temperature_chip",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(optris_drivers2__msg__Temperature, temperature_chip),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_message_members = {
  "optris_drivers2__msg",  // message namespace
  "Temperature",  // message name
  4,  // number of fields
  sizeof(optris_drivers2__msg__Temperature),
  optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_message_member_array,  // message members
  optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_init_function,  // function to initialize message memory (memory has to be allocated)
  optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_message_type_support_handle = {
  0,
  &optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_optris_drivers2
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, optris_drivers2, msg, Temperature)() {
  optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_message_type_support_handle.typesupport_identifier) {
    optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &optris_drivers2__msg__Temperature__rosidl_typesupport_introspection_c__Temperature_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
