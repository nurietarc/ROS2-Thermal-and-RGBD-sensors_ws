// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from optris_drivers2:msg/Temperature.idl
// generated code does not contain a copyright notice
#include "optris_drivers2/msg/detail/temperature__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
optris_drivers2__msg__Temperature__init(optris_drivers2__msg__Temperature * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    optris_drivers2__msg__Temperature__fini(msg);
    return false;
  }
  // temperature_flag
  // temperature_box
  // temperature_chip
  return true;
}

void
optris_drivers2__msg__Temperature__fini(optris_drivers2__msg__Temperature * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // temperature_flag
  // temperature_box
  // temperature_chip
}

bool
optris_drivers2__msg__Temperature__are_equal(const optris_drivers2__msg__Temperature * lhs, const optris_drivers2__msg__Temperature * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // temperature_flag
  if (lhs->temperature_flag != rhs->temperature_flag) {
    return false;
  }
  // temperature_box
  if (lhs->temperature_box != rhs->temperature_box) {
    return false;
  }
  // temperature_chip
  if (lhs->temperature_chip != rhs->temperature_chip) {
    return false;
  }
  return true;
}

bool
optris_drivers2__msg__Temperature__copy(
  const optris_drivers2__msg__Temperature * input,
  optris_drivers2__msg__Temperature * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // temperature_flag
  output->temperature_flag = input->temperature_flag;
  // temperature_box
  output->temperature_box = input->temperature_box;
  // temperature_chip
  output->temperature_chip = input->temperature_chip;
  return true;
}

optris_drivers2__msg__Temperature *
optris_drivers2__msg__Temperature__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__msg__Temperature * msg = (optris_drivers2__msg__Temperature *)allocator.allocate(sizeof(optris_drivers2__msg__Temperature), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(optris_drivers2__msg__Temperature));
  bool success = optris_drivers2__msg__Temperature__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
optris_drivers2__msg__Temperature__destroy(optris_drivers2__msg__Temperature * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    optris_drivers2__msg__Temperature__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
optris_drivers2__msg__Temperature__Sequence__init(optris_drivers2__msg__Temperature__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__msg__Temperature * data = NULL;

  if (size) {
    data = (optris_drivers2__msg__Temperature *)allocator.zero_allocate(size, sizeof(optris_drivers2__msg__Temperature), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = optris_drivers2__msg__Temperature__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        optris_drivers2__msg__Temperature__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
optris_drivers2__msg__Temperature__Sequence__fini(optris_drivers2__msg__Temperature__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      optris_drivers2__msg__Temperature__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

optris_drivers2__msg__Temperature__Sequence *
optris_drivers2__msg__Temperature__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__msg__Temperature__Sequence * array = (optris_drivers2__msg__Temperature__Sequence *)allocator.allocate(sizeof(optris_drivers2__msg__Temperature__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = optris_drivers2__msg__Temperature__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
optris_drivers2__msg__Temperature__Sequence__destroy(optris_drivers2__msg__Temperature__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    optris_drivers2__msg__Temperature__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
optris_drivers2__msg__Temperature__Sequence__are_equal(const optris_drivers2__msg__Temperature__Sequence * lhs, const optris_drivers2__msg__Temperature__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!optris_drivers2__msg__Temperature__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
optris_drivers2__msg__Temperature__Sequence__copy(
  const optris_drivers2__msg__Temperature__Sequence * input,
  optris_drivers2__msg__Temperature__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(optris_drivers2__msg__Temperature);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    optris_drivers2__msg__Temperature * data =
      (optris_drivers2__msg__Temperature *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!optris_drivers2__msg__Temperature__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          optris_drivers2__msg__Temperature__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!optris_drivers2__msg__Temperature__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
