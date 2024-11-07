// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from optris_drivers2:msg/Flag.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__STRUCT_H_
#define OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/Flag in the package optris_drivers2.
typedef struct optris_drivers2__msg__Flag
{
  std_msgs__msg__Header header;
  uint32_t flag_state;
} optris_drivers2__msg__Flag;

// Struct for a sequence of optris_drivers2__msg__Flag.
typedef struct optris_drivers2__msg__Flag__Sequence
{
  optris_drivers2__msg__Flag * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} optris_drivers2__msg__Flag__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__STRUCT_H_
