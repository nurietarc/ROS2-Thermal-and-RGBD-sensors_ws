// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from optris_drivers2:msg/Flag.idl
// generated code does not contain a copyright notice
#include "optris_drivers2/msg/detail/flag__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
optris_drivers2__msg__Flag__init(optris_drivers2__msg__Flag * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    optris_drivers2__msg__Flag__fini(msg);
    return false;
  }
  // flag_state
  return true;
}

void
optris_drivers2__msg__Flag__fini(optris_drivers2__msg__Flag * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // flag_state
}

bool
optris_drivers2__msg__Flag__are_equal(const optris_drivers2__msg__Flag * lhs, const optris_drivers2__msg__Flag * rhs)
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
  // flag_state
  if (lhs->flag_state != rhs->flag_state) {
    return false;
  }
  return true;
}

bool
optris_drivers2__msg__Flag__copy(
  const optris_drivers2__msg__Flag * input,
  optris_drivers2__msg__Flag * output)
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
  // flag_state
  output->flag_state = input->flag_state;
  return true;
}

optris_drivers2__msg__Flag *
optris_drivers2__msg__Flag__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__msg__Flag * msg = (optris_drivers2__msg__Flag *)allocator.allocate(sizeof(optris_drivers2__msg__Flag), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(optris_drivers2__msg__Flag));
  bool success = optris_drivers2__msg__Flag__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
optris_drivers2__msg__Flag__destroy(optris_drivers2__msg__Flag * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    optris_drivers2__msg__Flag__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
optris_drivers2__msg__Flag__Sequence__init(optris_drivers2__msg__Flag__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__msg__Flag * data = NULL;

  if (size) {
    data = (optris_drivers2__msg__Flag *)allocator.zero_allocate(size, sizeof(optris_drivers2__msg__Flag), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = optris_drivers2__msg__Flag__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        optris_drivers2__msg__Flag__fini(&data[i - 1]);
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
optris_drivers2__msg__Flag__Sequence__fini(optris_drivers2__msg__Flag__Sequence * array)
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
      optris_drivers2__msg__Flag__fini(&array->data[i]);
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

optris_drivers2__msg__Flag__Sequence *
optris_drivers2__msg__Flag__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__msg__Flag__Sequence * array = (optris_drivers2__msg__Flag__Sequence *)allocator.allocate(sizeof(optris_drivers2__msg__Flag__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = optris_drivers2__msg__Flag__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
optris_drivers2__msg__Flag__Sequence__destroy(optris_drivers2__msg__Flag__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    optris_drivers2__msg__Flag__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
optris_drivers2__msg__Flag__Sequence__are_equal(const optris_drivers2__msg__Flag__Sequence * lhs, const optris_drivers2__msg__Flag__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!optris_drivers2__msg__Flag__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
optris_drivers2__msg__Flag__Sequence__copy(
  const optris_drivers2__msg__Flag__Sequence * input,
  optris_drivers2__msg__Flag__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(optris_drivers2__msg__Flag);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    optris_drivers2__msg__Flag * data =
      (optris_drivers2__msg__Flag *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!optris_drivers2__msg__Flag__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          optris_drivers2__msg__Flag__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!optris_drivers2__msg__Flag__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
