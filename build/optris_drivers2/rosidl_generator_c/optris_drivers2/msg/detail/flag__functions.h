// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from optris_drivers2:msg/Flag.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__FUNCTIONS_H_
#define OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "optris_drivers2/msg/rosidl_generator_c__visibility_control.h"

#include "optris_drivers2/msg/detail/flag__struct.h"

/// Initialize msg/Flag message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * optris_drivers2__msg__Flag
 * )) before or use
 * optris_drivers2__msg__Flag__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_optris_drivers2
bool
optris_drivers2__msg__Flag__init(optris_drivers2__msg__Flag * msg);

/// Finalize msg/Flag message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_optris_drivers2
void
optris_drivers2__msg__Flag__fini(optris_drivers2__msg__Flag * msg);

/// Create msg/Flag message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * optris_drivers2__msg__Flag__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_optris_drivers2
optris_drivers2__msg__Flag *
optris_drivers2__msg__Flag__create();

/// Destroy msg/Flag message.
/**
 * It calls
 * optris_drivers2__msg__Flag__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_optris_drivers2
void
optris_drivers2__msg__Flag__destroy(optris_drivers2__msg__Flag * msg);

/// Check for msg/Flag message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_optris_drivers2
bool
optris_drivers2__msg__Flag__are_equal(const optris_drivers2__msg__Flag * lhs, const optris_drivers2__msg__Flag * rhs);

/// Copy a msg/Flag message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_optris_drivers2
bool
optris_drivers2__msg__Flag__copy(
  const optris_drivers2__msg__Flag * input,
  optris_drivers2__msg__Flag * output);

/// Initialize array of msg/Flag messages.
/**
 * It allocates the memory for the number of elements and calls
 * optris_drivers2__msg__Flag__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_optris_drivers2
bool
optris_drivers2__msg__Flag__Sequence__init(optris_drivers2__msg__Flag__Sequence * array, size_t size);

/// Finalize array of msg/Flag messages.
/**
 * It calls
 * optris_drivers2__msg__Flag__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_optris_drivers2
void
optris_drivers2__msg__Flag__Sequence__fini(optris_drivers2__msg__Flag__Sequence * array);

/// Create array of msg/Flag messages.
/**
 * It allocates the memory for the array and calls
 * optris_drivers2__msg__Flag__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_optris_drivers2
optris_drivers2__msg__Flag__Sequence *
optris_drivers2__msg__Flag__Sequence__create(size_t size);

/// Destroy array of msg/Flag messages.
/**
 * It calls
 * optris_drivers2__msg__Flag__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_optris_drivers2
void
optris_drivers2__msg__Flag__Sequence__destroy(optris_drivers2__msg__Flag__Sequence * array);

/// Check for msg/Flag message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_optris_drivers2
bool
optris_drivers2__msg__Flag__Sequence__are_equal(const optris_drivers2__msg__Flag__Sequence * lhs, const optris_drivers2__msg__Flag__Sequence * rhs);

/// Copy an array of msg/Flag messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_optris_drivers2
bool
optris_drivers2__msg__Flag__Sequence__copy(
  const optris_drivers2__msg__Flag__Sequence * input,
  optris_drivers2__msg__Flag__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__FUNCTIONS_H_
