// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from optris_drivers2:srv/AutoFlag.idl
// generated code does not contain a copyright notice
#include "optris_drivers2/srv/detail/auto_flag__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "optris_drivers2/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "optris_drivers2/srv/detail/auto_flag__struct.h"
#include "optris_drivers2/srv/detail/auto_flag__functions.h"
#include "fastcdr/Cdr.h"

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

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _AutoFlag_Request__ros_msg_type = optris_drivers2__srv__AutoFlag_Request;

static bool _AutoFlag_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _AutoFlag_Request__ros_msg_type * ros_message = static_cast<const _AutoFlag_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: auto_flag
  {
    cdr << (ros_message->auto_flag ? true : false);
  }

  return true;
}

static bool _AutoFlag_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _AutoFlag_Request__ros_msg_type * ros_message = static_cast<_AutoFlag_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: auto_flag
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->auto_flag = tmp ? true : false;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_optris_drivers2
size_t get_serialized_size_optris_drivers2__srv__AutoFlag_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _AutoFlag_Request__ros_msg_type * ros_message = static_cast<const _AutoFlag_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name auto_flag
  {
    size_t item_size = sizeof(ros_message->auto_flag);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _AutoFlag_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_optris_drivers2__srv__AutoFlag_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_optris_drivers2
size_t max_serialized_size_optris_drivers2__srv__AutoFlag_Request(
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

  // member: auto_flag
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
    using DataType = optris_drivers2__srv__AutoFlag_Request;
    is_plain =
      (
      offsetof(DataType, auto_flag) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _AutoFlag_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_optris_drivers2__srv__AutoFlag_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_AutoFlag_Request = {
  "optris_drivers2::srv",
  "AutoFlag_Request",
  _AutoFlag_Request__cdr_serialize,
  _AutoFlag_Request__cdr_deserialize,
  _AutoFlag_Request__get_serialized_size,
  _AutoFlag_Request__max_serialized_size
};

static rosidl_message_type_support_t _AutoFlag_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_AutoFlag_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, optris_drivers2, srv, AutoFlag_Request)() {
  return &_AutoFlag_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "optris_drivers2/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "optris_drivers2/srv/detail/auto_flag__struct.h"
// already included above
// #include "optris_drivers2/srv/detail/auto_flag__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

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

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _AutoFlag_Response__ros_msg_type = optris_drivers2__srv__AutoFlag_Response;

static bool _AutoFlag_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _AutoFlag_Response__ros_msg_type * ros_message = static_cast<const _AutoFlag_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: is_auto_flag_active
  {
    cdr << (ros_message->is_auto_flag_active ? true : false);
  }

  return true;
}

static bool _AutoFlag_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _AutoFlag_Response__ros_msg_type * ros_message = static_cast<_AutoFlag_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: is_auto_flag_active
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->is_auto_flag_active = tmp ? true : false;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_optris_drivers2
size_t get_serialized_size_optris_drivers2__srv__AutoFlag_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _AutoFlag_Response__ros_msg_type * ros_message = static_cast<const _AutoFlag_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name is_auto_flag_active
  {
    size_t item_size = sizeof(ros_message->is_auto_flag_active);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _AutoFlag_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_optris_drivers2__srv__AutoFlag_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_optris_drivers2
size_t max_serialized_size_optris_drivers2__srv__AutoFlag_Response(
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

  // member: is_auto_flag_active
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
    using DataType = optris_drivers2__srv__AutoFlag_Response;
    is_plain =
      (
      offsetof(DataType, is_auto_flag_active) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _AutoFlag_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_optris_drivers2__srv__AutoFlag_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_AutoFlag_Response = {
  "optris_drivers2::srv",
  "AutoFlag_Response",
  _AutoFlag_Response__cdr_serialize,
  _AutoFlag_Response__cdr_deserialize,
  _AutoFlag_Response__get_serialized_size,
  _AutoFlag_Response__max_serialized_size
};

static rosidl_message_type_support_t _AutoFlag_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_AutoFlag_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, optris_drivers2, srv, AutoFlag_Response)() {
  return &_AutoFlag_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "optris_drivers2/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "optris_drivers2/srv/auto_flag.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t AutoFlag__callbacks = {
  "optris_drivers2::srv",
  "AutoFlag",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, optris_drivers2, srv, AutoFlag_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, optris_drivers2, srv, AutoFlag_Response)(),
};

static rosidl_service_type_support_t AutoFlag__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &AutoFlag__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, optris_drivers2, srv, AutoFlag)() {
  return &AutoFlag__handle;
}

#if defined(__cplusplus)
}
#endif
