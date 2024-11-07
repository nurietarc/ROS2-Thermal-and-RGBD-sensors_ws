// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from optris_drivers2:srv/AutoFlag.idl
// generated code does not contain a copyright notice
#include "optris_drivers2/srv/detail/auto_flag__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
optris_drivers2__srv__AutoFlag_Request__init(optris_drivers2__srv__AutoFlag_Request * msg)
{
  if (!msg) {
    return false;
  }
  // auto_flag
  return true;
}

void
optris_drivers2__srv__AutoFlag_Request__fini(optris_drivers2__srv__AutoFlag_Request * msg)
{
  if (!msg) {
    return;
  }
  // auto_flag
}

bool
optris_drivers2__srv__AutoFlag_Request__are_equal(const optris_drivers2__srv__AutoFlag_Request * lhs, const optris_drivers2__srv__AutoFlag_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // auto_flag
  if (lhs->auto_flag != rhs->auto_flag) {
    return false;
  }
  return true;
}

bool
optris_drivers2__srv__AutoFlag_Request__copy(
  const optris_drivers2__srv__AutoFlag_Request * input,
  optris_drivers2__srv__AutoFlag_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // auto_flag
  output->auto_flag = input->auto_flag;
  return true;
}

optris_drivers2__srv__AutoFlag_Request *
optris_drivers2__srv__AutoFlag_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__srv__AutoFlag_Request * msg = (optris_drivers2__srv__AutoFlag_Request *)allocator.allocate(sizeof(optris_drivers2__srv__AutoFlag_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(optris_drivers2__srv__AutoFlag_Request));
  bool success = optris_drivers2__srv__AutoFlag_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
optris_drivers2__srv__AutoFlag_Request__destroy(optris_drivers2__srv__AutoFlag_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    optris_drivers2__srv__AutoFlag_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
optris_drivers2__srv__AutoFlag_Request__Sequence__init(optris_drivers2__srv__AutoFlag_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__srv__AutoFlag_Request * data = NULL;

  if (size) {
    data = (optris_drivers2__srv__AutoFlag_Request *)allocator.zero_allocate(size, sizeof(optris_drivers2__srv__AutoFlag_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = optris_drivers2__srv__AutoFlag_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        optris_drivers2__srv__AutoFlag_Request__fini(&data[i - 1]);
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
optris_drivers2__srv__AutoFlag_Request__Sequence__fini(optris_drivers2__srv__AutoFlag_Request__Sequence * array)
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
      optris_drivers2__srv__AutoFlag_Request__fini(&array->data[i]);
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

optris_drivers2__srv__AutoFlag_Request__Sequence *
optris_drivers2__srv__AutoFlag_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__srv__AutoFlag_Request__Sequence * array = (optris_drivers2__srv__AutoFlag_Request__Sequence *)allocator.allocate(sizeof(optris_drivers2__srv__AutoFlag_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = optris_drivers2__srv__AutoFlag_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
optris_drivers2__srv__AutoFlag_Request__Sequence__destroy(optris_drivers2__srv__AutoFlag_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    optris_drivers2__srv__AutoFlag_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
optris_drivers2__srv__AutoFlag_Request__Sequence__are_equal(const optris_drivers2__srv__AutoFlag_Request__Sequence * lhs, const optris_drivers2__srv__AutoFlag_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!optris_drivers2__srv__AutoFlag_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
optris_drivers2__srv__AutoFlag_Request__Sequence__copy(
  const optris_drivers2__srv__AutoFlag_Request__Sequence * input,
  optris_drivers2__srv__AutoFlag_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(optris_drivers2__srv__AutoFlag_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    optris_drivers2__srv__AutoFlag_Request * data =
      (optris_drivers2__srv__AutoFlag_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!optris_drivers2__srv__AutoFlag_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          optris_drivers2__srv__AutoFlag_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!optris_drivers2__srv__AutoFlag_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
optris_drivers2__srv__AutoFlag_Response__init(optris_drivers2__srv__AutoFlag_Response * msg)
{
  if (!msg) {
    return false;
  }
  // is_auto_flag_active
  return true;
}

void
optris_drivers2__srv__AutoFlag_Response__fini(optris_drivers2__srv__AutoFlag_Response * msg)
{
  if (!msg) {
    return;
  }
  // is_auto_flag_active
}

bool
optris_drivers2__srv__AutoFlag_Response__are_equal(const optris_drivers2__srv__AutoFlag_Response * lhs, const optris_drivers2__srv__AutoFlag_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // is_auto_flag_active
  if (lhs->is_auto_flag_active != rhs->is_auto_flag_active) {
    return false;
  }
  return true;
}

bool
optris_drivers2__srv__AutoFlag_Response__copy(
  const optris_drivers2__srv__AutoFlag_Response * input,
  optris_drivers2__srv__AutoFlag_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // is_auto_flag_active
  output->is_auto_flag_active = input->is_auto_flag_active;
  return true;
}

optris_drivers2__srv__AutoFlag_Response *
optris_drivers2__srv__AutoFlag_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__srv__AutoFlag_Response * msg = (optris_drivers2__srv__AutoFlag_Response *)allocator.allocate(sizeof(optris_drivers2__srv__AutoFlag_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(optris_drivers2__srv__AutoFlag_Response));
  bool success = optris_drivers2__srv__AutoFlag_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
optris_drivers2__srv__AutoFlag_Response__destroy(optris_drivers2__srv__AutoFlag_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    optris_drivers2__srv__AutoFlag_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
optris_drivers2__srv__AutoFlag_Response__Sequence__init(optris_drivers2__srv__AutoFlag_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__srv__AutoFlag_Response * data = NULL;

  if (size) {
    data = (optris_drivers2__srv__AutoFlag_Response *)allocator.zero_allocate(size, sizeof(optris_drivers2__srv__AutoFlag_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = optris_drivers2__srv__AutoFlag_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        optris_drivers2__srv__AutoFlag_Response__fini(&data[i - 1]);
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
optris_drivers2__srv__AutoFlag_Response__Sequence__fini(optris_drivers2__srv__AutoFlag_Response__Sequence * array)
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
      optris_drivers2__srv__AutoFlag_Response__fini(&array->data[i]);
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

optris_drivers2__srv__AutoFlag_Response__Sequence *
optris_drivers2__srv__AutoFlag_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  optris_drivers2__srv__AutoFlag_Response__Sequence * array = (optris_drivers2__srv__AutoFlag_Response__Sequence *)allocator.allocate(sizeof(optris_drivers2__srv__AutoFlag_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = optris_drivers2__srv__AutoFlag_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
optris_drivers2__srv__AutoFlag_Response__Sequence__destroy(optris_drivers2__srv__AutoFlag_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    optris_drivers2__srv__AutoFlag_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
optris_drivers2__srv__AutoFlag_Response__Sequence__are_equal(const optris_drivers2__srv__AutoFlag_Response__Sequence * lhs, const optris_drivers2__srv__AutoFlag_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!optris_drivers2__srv__AutoFlag_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
optris_drivers2__srv__AutoFlag_Response__Sequence__copy(
  const optris_drivers2__srv__AutoFlag_Response__Sequence * input,
  optris_drivers2__srv__AutoFlag_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(optris_drivers2__srv__AutoFlag_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    optris_drivers2__srv__AutoFlag_Response * data =
      (optris_drivers2__srv__AutoFlag_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!optris_drivers2__srv__AutoFlag_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          optris_drivers2__srv__AutoFlag_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!optris_drivers2__srv__AutoFlag_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
