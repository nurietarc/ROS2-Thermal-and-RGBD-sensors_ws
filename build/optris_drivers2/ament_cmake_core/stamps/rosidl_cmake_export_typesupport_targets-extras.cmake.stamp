# generated from
# rosidl_cmake/cmake/template/rosidl_cmake_export_typesupport_targets.cmake.in

set(_exported_typesupport_targets
  "__rosidl_generator_c:optris_drivers2__rosidl_generator_c;__rosidl_typesupport_fastrtps_c:optris_drivers2__rosidl_typesupport_fastrtps_c;__rosidl_generator_cpp:optris_drivers2__rosidl_generator_cpp;__rosidl_typesupport_fastrtps_cpp:optris_drivers2__rosidl_typesupport_fastrtps_cpp;__rosidl_typesupport_introspection_c:optris_drivers2__rosidl_typesupport_introspection_c;__rosidl_typesupport_c:optris_drivers2__rosidl_typesupport_c;__rosidl_typesupport_introspection_cpp:optris_drivers2__rosidl_typesupport_introspection_cpp;__rosidl_typesupport_cpp:optris_drivers2__rosidl_typesupport_cpp;__rosidl_generator_py:optris_drivers2__rosidl_generator_py")

# populate optris_drivers2_TARGETS_<suffix>
if(NOT _exported_typesupport_targets STREQUAL "")
  # loop over typesupport targets
  foreach(_tuple ${_exported_typesupport_targets})
    string(REPLACE ":" ";" _tuple "${_tuple}")
    list(GET _tuple 0 _suffix)
    list(GET _tuple 1 _target)

    set(_target "optris_drivers2::${_target}")
    if(NOT TARGET "${_target}")
      # the exported target must exist
      message(WARNING "Package 'optris_drivers2' exports the typesupport target '${_target}' which doesn't exist")
    else()
      list(APPEND optris_drivers2_TARGETS${_suffix} "${_target}")
    endif()
  endforeach()
endif()
