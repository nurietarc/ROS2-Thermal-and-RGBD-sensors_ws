// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from optris_drivers2:srv/TemperatureRange.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__SRV__DETAIL__TEMPERATURE_RANGE__STRUCT_H_
#define OPTRIS_DRIVERS2__SRV__DETAIL__TEMPERATURE_RANGE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/TemperatureRange in the package optris_drivers2.
typedef struct optris_drivers2__srv__TemperatureRange_Request
{
  int16_t temperature_range_min;
  int16_t temperature_range_max;
} optris_drivers2__srv__TemperatureRange_Request;

// Struct for a sequence of optris_drivers2__srv__TemperatureRange_Request.
typedef struct optris_drivers2__srv__TemperatureRange_Request__Sequence
{
  optris_drivers2__srv__TemperatureRange_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} optris_drivers2__srv__TemperatureRange_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/TemperatureRange in the package optris_drivers2.
typedef struct optris_drivers2__srv__TemperatureRange_Response
{
  bool success;
} optris_drivers2__srv__TemperatureRange_Response;

// Struct for a sequence of optris_drivers2__srv__TemperatureRange_Response.
typedef struct optris_drivers2__srv__TemperatureRange_Response__Sequence
{
  optris_drivers2__srv__TemperatureRange_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} optris_drivers2__srv__TemperatureRange_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // OPTRIS_DRIVERS2__SRV__DETAIL__TEMPERATURE_RANGE__STRUCT_H_
