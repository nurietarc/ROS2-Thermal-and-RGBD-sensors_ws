// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from optris_drivers2:msg/Temperature.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "optris_drivers2/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "optris_drivers2/msg/detail/temperature__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace optris_drivers2
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
cdr_serialize(
  const optris_drivers2::msg::Temperature & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  optris_drivers2::msg::Temperature & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
get_serialized_size(
  const optris_drivers2::msg::Temperature & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
max_serialized_size_Temperature(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace optris_drivers2

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, optris_drivers2, msg, Temperature)();

#ifdef __cplusplus
}
#endif

#endif  // OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
