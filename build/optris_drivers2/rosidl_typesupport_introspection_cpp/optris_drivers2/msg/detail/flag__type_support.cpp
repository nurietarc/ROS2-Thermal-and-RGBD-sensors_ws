// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from optris_drivers2:msg/Flag.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "optris_drivers2/msg/detail/flag__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace optris_drivers2
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Flag_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) optris_drivers2::msg::Flag(_init);
}

void Flag_fini_function(void * message_memory)
{
  auto typed_message = static_cast<optris_drivers2::msg::Flag *>(message_memory);
  typed_message->~Flag();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Flag_message_member_array[2] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(optris_drivers2::msg::Flag, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "flag_state",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(optris_drivers2::msg::Flag, flag_state),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Flag_message_members = {
  "optris_drivers2::msg",  // message namespace
  "Flag",  // message name
  2,  // number of fields
  sizeof(optris_drivers2::msg::Flag),
  Flag_message_member_array,  // message members
  Flag_init_function,  // function to initialize message memory (memory has to be allocated)
  Flag_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Flag_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Flag_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace optris_drivers2


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<optris_drivers2::msg::Flag>()
{
  return &::optris_drivers2::msg::rosidl_typesupport_introspection_cpp::Flag_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, optris_drivers2, msg, Flag)() {
  return &::optris_drivers2::msg::rosidl_typesupport_introspection_cpp::Flag_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
