// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from optris_drivers2:msg/Temperature.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__STRUCT_H_
#define OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__STRUCT_H_

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

/// Struct defined in msg/Temperature in the package optris_drivers2.
typedef struct optris_drivers2__msg__Temperature
{
  std_msgs__msg__Header header;
  float temperature_flag;
  float temperature_box;
  float temperature_chip;
} optris_drivers2__msg__Temperature;

// Struct for a sequence of optris_drivers2__msg__Temperature.
typedef struct optris_drivers2__msg__Temperature__Sequence
{
  optris_drivers2__msg__Temperature * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} optris_drivers2__msg__Temperature__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__STRUCT_H_
