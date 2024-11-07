// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from optris_drivers2:srv/Palette.idl
// generated code does not contain a copyright notice
#include "optris_drivers2/srv/detail/palette__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
optris_drivers2__srv__Palette_Request__init(optris_drivers2__srv__Palette_Request * msg)
{
  if (!msg) {
    return false;
  }
  // palette
  // palette_scaling
  // temperature_min
  // temperature_max
  return true;
}

void
optris_drivers2__srv__Palette_Request__fini(optris_drivers2__srv__Palette_Request * msg)
{
  if (!msg) {
    return;
  }
  // palette
  // palette_scaling
  // temperature_min
  // temperature_max
}

bool
optris_drivers2__srv__Palette_Request__are_equal(const optris_drivers2__srv__Palette_Request * lhs, const optris_drivers2__srv__Palette_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // palette
  if (lhs->palette != rhs->palette) {
    return false;
  }
  // palette_scaling
  if (lhs->palette_scaling != rhs->palette_scaling) {
    return false;
  }
  // temperature_min
  if (lhs->temperature_min != rhs->temperature_min) {
    return false;
  }
  // temperature_max
  if (lhs->temperature_max != rhs->temperature_max) {
    return false;
  }
  return true;
}

bool
optris_drivers2__srv__Palette_Request__copy(
  const optris_drivers2__srv__Palette_Request * input,
  optris_drivers2__srv__Palette_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // palette
  output->palette = input->palette;
  // palette_scaling
  output->palette_scaling = input->palette_scaling;
  // temperature_min
  output->temperature_min = input->temperature_min;
  // temperature_max
  output->temperature_max = input->temperature_max;
  return true;
}

optris_drivers2__srv__Palette_Request *
optris_drivers2__srv__Palette_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__srv__Palette_Request * msg = (optris_drivers2__srv__Palette_Request *)allocator.allocate(sizeof(optris_drivers2__srv__Palette_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(optris_drivers2__srv__Palette_Request));
  bool success = optris_drivers2__srv__Palette_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
optris_drivers2__srv__Palette_Request__destroy(optris_drivers2__srv__Palette_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    optris_drivers2__srv__Palette_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
optris_drivers2__srv__Palette_Request__Sequence__init(optris_drivers2__srv__Palette_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__srv__Palette_Request * data = NULL;

  if (size) {
    data = (optris_drivers2__srv__Palette_Request *)allocator.zero_allocate(size, sizeof(optris_drivers2__srv__Palette_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = optris_drivers2__srv__Palette_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        optris_drivers2__srv__Palette_Request__fini(&data[i - 1]);
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
optris_drivers2__srv__Palette_Request__Sequence__fini(optris_drivers2__srv__Palette_Request__Sequence * array)
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
      optris_drivers2__srv__Palette_Request__fini(&array->data[i]);
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

optris_drivers2__srv__Palette_Request__Sequence *
optris_drivers2__srv__Palette_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__srv__Palette_Request__Sequence * array = (optris_drivers2__srv__Palette_Request__Sequence *)allocator.allocate(sizeof(optris_drivers2__srv__Palette_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = optris_drivers2__srv__Palette_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
optris_drivers2__srv__Palette_Request__Sequence__destroy(optris_drivers2__srv__Palette_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    optris_drivers2__srv__Palette_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
optris_drivers2__srv__Palette_Request__Sequence__are_equal(const optris_drivers2__srv__Palette_Request__Sequence * lhs, const optris_drivers2__srv__Palette_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!optris_drivers2__srv__Palette_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
optris_drivers2__srv__Palette_Request__Sequence__copy(
  const optris_drivers2__srv__Palette_Request__Sequence * input,
  optris_drivers2__srv__Palette_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(optris_drivers2__srv__Palette_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    optris_drivers2__srv__Palette_Request * data =
      (optris_drivers2__srv__Palette_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!optris_drivers2__srv__Palette_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          optris_drivers2__srv__Palette_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!optris_drivers2__srv__Palette_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
optris_drivers2__srv__Palette_Response__init(optris_drivers2__srv__Palette_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  return true;
}

void
optris_drivers2__srv__Palette_Response__fini(optris_drivers2__srv__Palette_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
}

bool
optris_drivers2__srv__Palette_Response__are_equal(const optris_drivers2__srv__Palette_Response * lhs, const optris_drivers2__srv__Palette_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
optris_drivers2__srv__Palette_Response__copy(
  const optris_drivers2__srv__Palette_Response * input,
  optris_drivers2__srv__Palette_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  return true;
}

optris_drivers2__srv__Palette_Response *
optris_drivers2__srv__Palette_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__srv__Palette_Response * msg = (optris_drivers2__srv__Palette_Response *)allocator.allocate(sizeof(optris_drivers2__srv__Palette_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(optris_drivers2__srv__Palette_Response));
  bool success = optris_drivers2__srv__Palette_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
optris_drivers2__srv__Palette_Response__destroy(optris_drivers2__srv__Palette_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    optris_drivers2__srv__Palette_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
optris_drivers2__srv__Palette_Response__Sequence__init(optris_drivers2__srv__Palette_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__srv__Palette_Response * data = NULL;

  if (size) {
    data = (optris_drivers2__srv__Palette_Response *)allocator.zero_allocate(size, sizeof(optris_drivers2__srv__Palette_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = optris_drivers2__srv__Palette_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        optris_drivers2__srv__Palette_Response__fini(&data[i - 1]);
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
optris_drivers2__srv__Palette_Response__Sequence__fini(optris_drivers2__srv__Palette_Response__Sequence * array)
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
      optris_drivers2__srv__Palette_Response__fini(&array->data[i]);
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

optris_drivers2__srv__Palette_Response__Sequence *
optris_drivers2__srv__Palette_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__srv__Palette_Response__Sequence * array = (optris_drivers2__srv__Palette_Response__Sequence *)allocator.allocate(sizeof(optris_drivers2__srv__Palette_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = optris_drivers2__srv__Palette_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
optris_drivers2__srv__Palette_Response__Sequence__destroy(optris_drivers2__srv__Palette_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    optris_drivers2__srv__Palette_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
optris_drivers2__srv__Palette_Response__Sequence__are_equal(const optris_drivers2__srv__Palette_Response__Sequence * lhs, const optris_drivers2__srv__Palette_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!optris_drivers2__srv__Palette_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
optris_drivers2__srv__Palette_Response__Sequence__copy(
  const optris_drivers2__srv__Palette_Response__Sequence * input,
  optris_drivers2__srv__Palette_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(optris_drivers2__srv__Palette_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    optris_drivers2__srv__Palette_Response * data =
      (optris_drivers2__srv__Palette_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!optris_drivers2__srv__Palette_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          optris_drivers2__srv__Palette_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!optris_drivers2__srv__Palette_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
