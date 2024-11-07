// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from optris_drivers2:srv/TemperatureRange.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "optris_drivers2/srv/detail/temperature_range__struct.h"
#include "optris_drivers2/srv/detail/temperature_range__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool optris_drivers2__srv__temperature_range__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[64];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("optris_drivers2.srv._temperature_range.TemperatureRange_Request", full_classname_dest, 63) == 0);
  }
  optris_drivers2__srv__TemperatureRange_Request * ros_message = _ros_message;
  {  // temperature_range_min
    PyObject * field = PyObject_GetAttrString(_pymsg, "temperature_range_min");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->temperature_range_min = (int16_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // temperature_range_max
    PyObject * field = PyObject_GetAttrString(_pymsg, "temperature_range_max");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->temperature_range_max = (int16_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * optris_drivers2__srv__temperature_range__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of TemperatureRange_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("optris_drivers2.srv._temperature_range");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "TemperatureRange_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  optris_drivers2__srv__TemperatureRange_Request * ros_message = (optris_drivers2__srv__TemperatureRange_Request *)raw_ros_message;
  {  // temperature_range_min
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->temperature_range_min);
    {
      int rc = PyObject_SetAttrString(_pymessage, "temperature_range_min", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // temperature_range_max
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->temperature_range_max);
    {
      int rc = PyObject_SetAttrString(_pymessage, "temperature_range_max", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "optris_drivers2/srv/detail/temperature_range__struct.h"
// already included above
// #include "optris_drivers2/srv/detail/temperature_range__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool optris_drivers2__srv__temperature_range__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[65];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("optris_drivers2.srv._temperature_range.TemperatureRange_Response", full_classname_dest, 64) == 0);
  }
  optris_drivers2__srv__TemperatureRange_Response * ros_message = _ros_message;
  {  // success
    PyObject * field = PyObject_GetAttrString(_pymsg, "success");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->success = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * optris_drivers2__srv__temperature_range__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of TemperatureRange_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("optris_drivers2.srv._temperature_range");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "TemperatureRange_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  optris_drivers2__srv__TemperatureRange_Response * ros_message = (optris_drivers2__srv__TemperatureRange_Response *)raw_ros_message;
  {  // success
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->success ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "success", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
