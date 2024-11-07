// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from optris_drivers2:srv/TemperatureRange.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__SRV__DETAIL__TEMPERATURE_RANGE__TRAITS_HPP_
#define OPTRIS_DRIVERS2__SRV__DETAIL__TEMPERATURE_RANGE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "optris_drivers2/srv/detail/temperature_range__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace optris_drivers2
{

namespace srv
{

inline void to_flow_style_yaml(
  const TemperatureRange_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: temperature_range_min
  {
    out << "temperature_range_min: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature_range_min, out);
    out << ", ";
  }

  // member: temperature_range_max
  {
    out << "temperature_range_max: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature_range_max, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TemperatureRange_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: temperature_range_min
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "temperature_range_min: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature_range_min, out);
    out << "\n";
  }

  // member: temperature_range_max
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "temperature_range_max: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature_range_max, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TemperatureRange_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace optris_drivers2

namespace rosidl_generator_traits
{

[[deprecated("use optris_drivers2::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const optris_drivers2::srv::TemperatureRange_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  optris_drivers2::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use optris_drivers2::srv::to_yaml() instead")]]
inline std::string to_yaml(const optris_drivers2::srv::TemperatureRange_Request & msg)
{
  return optris_drivers2::srv::to_yaml(msg);
}

template<>
inline const char * data_type<optris_drivers2::srv::TemperatureRange_Request>()
{
  return "optris_drivers2::srv::TemperatureRange_Request";
}

template<>
inline const char * name<optris_drivers2::srv::TemperatureRange_Request>()
{
  return "optris_drivers2/srv/TemperatureRange_Request";
}

template<>
struct has_fixed_size<optris_drivers2::srv::TemperatureRange_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<optris_drivers2::srv::TemperatureRange_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<optris_drivers2::srv::TemperatureRange_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace optris_drivers2
{

namespace srv
{

inline void to_flow_style_yaml(
  const TemperatureRange_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TemperatureRange_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TemperatureRange_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace optris_drivers2

namespace rosidl_generator_traits
{

[[deprecated("use optris_drivers2::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const optris_drivers2::srv::TemperatureRange_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  optris_drivers2::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use optris_drivers2::srv::to_yaml() instead")]]
inline std::string to_yaml(const optris_drivers2::srv::TemperatureRange_Response & msg)
{
  return optris_drivers2::srv::to_yaml(msg);
}

template<>
inline const char * data_type<optris_drivers2::srv::TemperatureRange_Response>()
{
  return "optris_drivers2::srv::TemperatureRange_Response";
}

template<>
inline const char * name<optris_drivers2::srv::TemperatureRange_Response>()
{
  return "optris_drivers2/srv/TemperatureRange_Response";
}

template<>
struct has_fixed_size<optris_drivers2::srv::TemperatureRange_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<optris_drivers2::srv::TemperatureRange_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<optris_drivers2::srv::TemperatureRange_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<optris_drivers2::srv::TemperatureRange>()
{
  return "optris_drivers2::srv::TemperatureRange";
}

template<>
inline const char * name<optris_drivers2::srv::TemperatureRange>()
{
  return "optris_drivers2/srv/TemperatureRange";
}

template<>
struct has_fixed_size<optris_drivers2::srv::TemperatureRange>
  : std::integral_constant<
    bool,
    has_fixed_size<optris_drivers2::srv::TemperatureRange_Request>::value &&
    has_fixed_size<optris_drivers2::srv::TemperatureRange_Response>::value
  >
{
};

template<>
struct has_bounded_size<optris_drivers2::srv::TemperatureRange>
  : std::integral_constant<
    bool,
    has_bounded_size<optris_drivers2::srv::TemperatureRange_Request>::value &&
    has_bounded_size<optris_drivers2::srv::TemperatureRange_Response>::value
  >
{
};

template<>
struct is_service<optris_drivers2::srv::TemperatureRange>
  : std::true_type
{
};

template<>
struct is_service_request<optris_drivers2::srv::TemperatureRange_Request>
  : std::true_type
{
};

template<>
struct is_service_response<optris_drivers2::srv::TemperatureRange_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // OPTRIS_DRIVERS2__SRV__DETAIL__TEMPERATURE_RANGE__TRAITS_HPP_
