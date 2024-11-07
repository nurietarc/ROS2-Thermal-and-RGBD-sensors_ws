// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from optris_drivers2:srv/AutoFlag.idl
// generated code does not contain a copyright notice
#include "optris_drivers2/srv/detail/auto_flag__rosidl_typesupport_fastrtps_cpp.hpp"
#include "optris_drivers2/srv/detail/auto_flag__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace optris_drivers2
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
cdr_serialize(
  const optris_drivers2::srv::AutoFlag_Request & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: auto_flag
  cdr << (ros_message.auto_flag ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  optris_drivers2::srv::AutoFlag_Request & ros_message)
{
  // Member: auto_flag
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.auto_flag = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
get_serialized_size(
  const optris_drivers2::srv::AutoFlag_Request & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: auto_flag
  {
    size_t item_size = sizeof(ros_message.auto_flag);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
max_serialized_size_AutoFlag_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: auto_flag
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = optris_drivers2::srv::AutoFlag_Request;
    is_plain =
      (
      offsetof(DataType, auto_flag) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _AutoFlag_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const optris_drivers2::srv::AutoFlag_Request *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _AutoFlag_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<optris_drivers2::srv::AutoFlag_Request *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _AutoFlag_Request__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const optris_drivers2::srv::AutoFlag_Request *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _AutoFlag_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_AutoFlag_Request(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _AutoFlag_Request__callbacks = {
  "optris_drivers2::srv",
  "AutoFlag_Request",
  _AutoFlag_Request__cdr_serialize,
  _AutoFlag_Request__cdr_deserialize,
  _AutoFlag_Request__get_serialized_size,
  _AutoFlag_Request__max_serialized_size
};

static rosidl_message_type_support_t _AutoFlag_Request__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_AutoFlag_Request__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace optris_drivers2

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_optris_drivers2
const rosidl_message_type_support_t *
get_message_type_support_handle<optris_drivers2::srv::AutoFlag_Request>()
{
  return &optris_drivers2::srv::typesupport_fastrtps_cpp::_AutoFlag_Request__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, optris_drivers2, srv, AutoFlag_Request)() {
  return &optris_drivers2::srv::typesupport_fastrtps_cpp::_AutoFlag_Request__handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include <limits>
// already included above
// #include <stdexcept>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
// already included above
// #include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace optris_drivers2
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
cdr_serialize(
  const optris_drivers2::srv::AutoFlag_Response & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: is_auto_flag_active
  cdr << (ros_message.is_auto_flag_active ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  optris_drivers2::srv::AutoFlag_Response & ros_message)
{
  // Member: is_auto_flag_active
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.is_auto_flag_active = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
get_serialized_size(
  const optris_drivers2::srv::AutoFlag_Response & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: is_auto_flag_active
  {
    size_t item_size = sizeof(ros_message.is_auto_flag_active);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_optris_drivers2
max_serialized_size_AutoFlag_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: is_auto_flag_active
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = optris_drivers2::srv::AutoFlag_Response;
    is_plain =
      (
      offsetof(DataType, is_auto_flag_active) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _AutoFlag_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const optris_drivers2::srv::AutoFlag_Response *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _AutoFlag_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<optris_drivers2::srv::AutoFlag_Response *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _AutoFlag_Response__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const optris_drivers2::srv::AutoFlag_Response *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _AutoFlag_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_AutoFlag_Response(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _AutoFlag_Response__callbacks = {
  "optris_drivers2::srv",
  "AutoFlag_Response",
  _AutoFlag_Response__cdr_serialize,
  _AutoFlag_Response__cdr_deserialize,
  _AutoFlag_Response__get_serialized_size,
  _AutoFlag_Response__max_serialized_size
};

static rosidl_message_type_support_t _AutoFlag_Response__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_AutoFlag_Response__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace optris_drivers2

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_optris_drivers2
const rosidl_message_type_support_t *
get_message_type_support_handle<optris_drivers2::srv::AutoFlag_Response>()
{
  return &optris_drivers2::srv::typesupport_fastrtps_cpp::_AutoFlag_Response__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, optris_drivers2, srv, AutoFlag_Response)() {
  return &optris_drivers2::srv::typesupport_fastrtps_cpp::_AutoFlag_Response__handle;
}

#ifdef __cplusplus
}
#endif

#include "rmw/error_handling.h"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/service_type_support_decl.hpp"

namespace optris_drivers2
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

static service_type_support_callbacks_t _AutoFlag__callbacks = {
  "optris_drivers2::srv",
  "AutoFlag",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, optris_drivers2, srv, AutoFlag_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, optris_drivers2, srv, AutoFlag_Response)(),
};

static rosidl_service_type_support_t _AutoFlag__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_AutoFlag__callbacks,
  get_service_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace optris_drivers2

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_optris_drivers2
const rosidl_service_type_support_t *
get_service_type_support_handle<optris_drivers2::srv::AutoFlag>()
{
  return &optris_drivers2::srv::typesupport_fastrtps_cpp::_AutoFlag__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, optris_drivers2, srv, AutoFlag)() {
  return &optris_drivers2::srv::typesupport_fastrtps_cpp::_AutoFlag__handle;
}

#ifdef __cplusplus
}
#endif
