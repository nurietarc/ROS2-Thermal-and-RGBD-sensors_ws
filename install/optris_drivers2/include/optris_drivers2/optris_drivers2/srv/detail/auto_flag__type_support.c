// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from optris_drivers2:srv/AutoFlag.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "optris_drivers2/srv/detail/auto_flag__rosidl_typesupport_introspection_c.h"
#include "optris_drivers2/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "optris_drivers2/srv/detail/auto_flag__functions.h"
#include "optris_drivers2/srv/detail/auto_flag__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void optris_drivers2__srv__AutoFlag_Request__rosidl_typesupport_introspection_c__AutoFlag_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  optris_drivers2__srv__AutoFlag_Request__init(message_memory);
}

void optris_drivers2__srv__AutoFlag_Request__rosidl_typesupport_introspection_c__AutoFlag_Request_fini_function(void * message_memory)
{
  optris_drivers2__srv__AutoFlag_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember optris_drivers2__srv__AutoFlag_Request__rosidl_typesupport_introspection_c__AutoFlag_Request_message_member_array[1] = {
  {
    "auto_flag",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(optris_drivers2__srv__AutoFlag_Request, auto_flag),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers optris_drivers2__srv__AutoFlag_Request__rosidl_typesupport_introspection_c__AutoFlag_Request_message_members = {
  "optris_drivers2__srv",  // message namespace
  "AutoFlag_Request",  // message name
  1,  // number of fields
  sizeof(optris_drivers2__srv__AutoFlag_Request),
  optris_drivers2__srv__AutoFlag_Request__rosidl_typesupport_introspection_c__AutoFlag_Request_message_member_array,  // message members
  optris_drivers2__srv__AutoFlag_Request__rosidl_typesupport_introspection_c__AutoFlag_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  optris_drivers2__srv__AutoFlag_Request__rosidl_typesupport_introspection_c__AutoFlag_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t optris_drivers2__srv__AutoFlag_Request__rosidl_typesupport_introspection_c__AutoFlag_Request_message_type_support_handle = {
  0,
  &optris_drivers2__srv__AutoFlag_Request__rosidl_typesupport_introspection_c__AutoFlag_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_optris_drivers2
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, optris_drivers2, srv, AutoFlag_Request)() {
  if (!optris_drivers2__srv__AutoFlag_Request__rosidl_typesupport_introspection_c__AutoFlag_Request_message_type_support_handle.typesupport_identifier) {
    optris_drivers2__srv__AutoFlag_Request__rosidl_typesupport_introspection_c__AutoFlag_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &optris_drivers2__srv__AutoFlag_Request__rosidl_typesupport_introspection_c__AutoFlag_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "optris_drivers2/srv/detail/auto_flag__rosidl_typesupport_introspection_c.h"
// already included above
// #include "optris_drivers2/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "optris_drivers2/srv/detail/auto_flag__functions.h"
// already included above
// #include "optris_drivers2/srv/detail/auto_flag__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void optris_drivers2__srv__AutoFlag_Response__rosidl_typesupport_introspection_c__AutoFlag_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  optris_drivers2__srv__AutoFlag_Response__init(message_memory);
}

void optris_drivers2__srv__AutoFlag_Response__rosidl_typesupport_introspection_c__AutoFlag_Response_fini_function(void * message_memory)
{
  optris_drivers2__srv__AutoFlag_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember optris_drivers2__srv__AutoFlag_Response__rosidl_typesupport_introspection_c__AutoFlag_Response_message_member_array[1] = {
  {
    "is_auto_flag_active",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(optris_drivers2__srv__AutoFlag_Response, is_auto_flag_active),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers optris_drivers2__srv__AutoFlag_Response__rosidl_typesupport_introspection_c__AutoFlag_Response_message_members = {
  "optris_drivers2__srv",  // message namespace
  "AutoFlag_Response",  // message name
  1,  // number of fields
  sizeof(optris_drivers2__srv__AutoFlag_Response),
  optris_drivers2__srv__AutoFlag_Response__rosidl_typesupport_introspection_c__AutoFlag_Response_message_member_array,  // message members
  optris_drivers2__srv__AutoFlag_Response__rosidl_typesupport_introspection_c__AutoFlag_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  optris_drivers2__srv__AutoFlag_Response__rosidl_typesupport_introspection_c__AutoFlag_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t optris_drivers2__srv__AutoFlag_Response__rosidl_typesupport_introspection_c__AutoFlag_Response_message_type_support_handle = {
  0,
  &optris_drivers2__srv__AutoFlag_Response__rosidl_typesupport_introspection_c__AutoFlag_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_optris_drivers2
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, optris_drivers2, srv, AutoFlag_Response)() {
  if (!optris_drivers2__srv__AutoFlag_Response__rosidl_typesupport_introspection_c__AutoFlag_Response_message_type_support_handle.typesupport_identifier) {
    optris_drivers2__srv__AutoFlag_Response__rosidl_typesupport_introspection_c__AutoFlag_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &optris_drivers2__srv__AutoFlag_Response__rosidl_typesupport_introspection_c__AutoFlag_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "optris_drivers2/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "optris_drivers2/srv/detail/auto_flag__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers optris_drivers2__srv__detail__auto_flag__rosidl_typesupport_introspection_c__AutoFlag_service_members = {
  "optris_drivers2__srv",  // service namespace
  "AutoFlag",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // optris_drivers2__srv__detail__auto_flag__rosidl_typesupport_introspection_c__AutoFlag_Request_message_type_support_handle,
  NULL  // response message
  // optris_drivers2__srv__detail__auto_flag__rosidl_typesupport_introspection_c__AutoFlag_Response_message_type_support_handle
};

static rosidl_service_type_support_t optris_drivers2__srv__detail__auto_flag__rosidl_typesupport_introspection_c__AutoFlag_service_type_support_handle = {
  0,
  &optris_drivers2__srv__detail__auto_flag__rosidl_typesupport_introspection_c__AutoFlag_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, optris_drivers2, srv, AutoFlag_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, optris_drivers2, srv, AutoFlag_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_optris_drivers2
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, optris_drivers2, srv, AutoFlag)() {
  if (!optris_drivers2__srv__detail__auto_flag__rosidl_typesupport_introspection_c__AutoFlag_service_type_support_handle.typesupport_identifier) {
    optris_drivers2__srv__detail__auto_flag__rosidl_typesupport_introspection_c__AutoFlag_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)optris_drivers2__srv__detail__auto_flag__rosidl_typesupport_introspection_c__AutoFlag_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, optris_drivers2, srv, AutoFlag_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, optris_drivers2, srv, AutoFlag_Response)()->data;
  }

  return &optris_drivers2__srv__detail__auto_flag__rosidl_typesupport_introspection_c__AutoFlag_service_type_support_handle;
}
