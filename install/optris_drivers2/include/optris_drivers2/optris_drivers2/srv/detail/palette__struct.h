// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from optris_drivers2:srv/Palette.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__SRV__DETAIL__PALETTE__STRUCT_H_
#define OPTRIS_DRIVERS2__SRV__DETAIL__PALETTE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Palette in the package optris_drivers2.
typedef struct optris_drivers2__srv__Palette_Request
{
  int16_t palette;
  int16_t palette_scaling;
  float temperature_min;
  float temperature_max;
} optris_drivers2__srv__Palette_Request;

// Struct for a sequence of optris_drivers2__srv__Palette_Request.
typedef struct optris_drivers2__srv__Palette_Request__Sequence
{
  optris_drivers2__srv__Palette_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} optris_drivers2__srv__Palette_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Palette in the package optris_drivers2.
typedef struct optris_drivers2__srv__Palette_Response
{
  bool success;
} optris_drivers2__srv__Palette_Response;

// Struct for a sequence of optris_drivers2__srv__Palette_Response.
typedef struct optris_drivers2__srv__Palette_Response__Sequence
{
  optris_drivers2__srv__Palette_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} optris_drivers2__srv__Palette_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // OPTRIS_DRIVERS2__SRV__DETAIL__PALETTE__STRUCT_H_
