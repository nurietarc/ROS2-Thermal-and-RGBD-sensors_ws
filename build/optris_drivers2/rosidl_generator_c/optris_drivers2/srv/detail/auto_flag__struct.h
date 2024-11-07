// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from optris_drivers2:srv/AutoFlag.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__SRV__DETAIL__AUTO_FLAG__STRUCT_H_
#define OPTRIS_DRIVERS2__SRV__DETAIL__AUTO_FLAG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/AutoFlag in the package optris_drivers2.
typedef struct optris_drivers2__srv__AutoFlag_Request
{
  bool auto_flag;
} optris_drivers2__srv__AutoFlag_Request;

// Struct for a sequence of optris_drivers2__srv__AutoFlag_Request.
typedef struct optris_drivers2__srv__AutoFlag_Request__Sequence
{
  optris_drivers2__srv__AutoFlag_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} optris_drivers2__srv__AutoFlag_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/AutoFlag in the package optris_drivers2.
typedef struct optris_drivers2__srv__AutoFlag_Response
{
  bool is_auto_flag_active;
} optris_drivers2__srv__AutoFlag_Response;

// Struct for a sequence of optris_drivers2__srv__AutoFlag_Response.
typedef struct optris_drivers2__srv__AutoFlag_Response__Sequence
{
  optris_drivers2__srv__AutoFlag_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} optris_drivers2__srv__AutoFlag_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // OPTRIS_DRIVERS2__SRV__DETAIL__AUTO_FLAG__STRUCT_H_
