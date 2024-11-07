// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from optris_drivers2:srv/AutoFlag.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__SRV__DETAIL__AUTO_FLAG__TRAITS_HPP_
#define OPTRIS_DRIVERS2__SRV__DETAIL__AUTO_FLAG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "optris_drivers2/srv/detail/auto_flag__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace optris_drivers2
{

namespace srv
{

inline void to_flow_style_yaml(
  const AutoFlag_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: auto_flag
  {
    out << "auto_flag: ";
    rosidl_generator_traits::value_to_yaml(msg.auto_flag, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AutoFlag_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: auto_flag
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "auto_flag: ";
    rosidl_generator_traits::value_to_yaml(msg.auto_flag, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AutoFlag_Request & msg, bool use_flow_style = false)
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
  const optris_drivers2::srv::AutoFlag_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  optris_drivers2::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use optris_drivers2::srv::to_yaml() instead")]]
inline std::string to_yaml(const optris_drivers2::srv::AutoFlag_Request & msg)
{
  return optris_drivers2::srv::to_yaml(msg);
}

template<>
inline const char * data_type<optris_drivers2::srv::AutoFlag_Request>()
{
  return "optris_drivers2::srv::AutoFlag_Request";
}

template<>
inline const char * name<optris_drivers2::srv::AutoFlag_Request>()
{
  return "optris_drivers2/srv/AutoFlag_Request";
}

template<>
struct has_fixed_size<optris_drivers2::srv::AutoFlag_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<optris_drivers2::srv::AutoFlag_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<optris_drivers2::srv::AutoFlag_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace optris_drivers2
{

namespace srv
{

inline void to_flow_style_yaml(
  const AutoFlag_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: is_auto_flag_active
  {
    out << "is_auto_flag_active: ";
    rosidl_generator_traits::value_to_yaml(msg.is_auto_flag_active, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AutoFlag_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: is_auto_flag_active
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_auto_flag_active: ";
    rosidl_generator_traits::value_to_yaml(msg.is_auto_flag_active, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AutoFlag_Response & msg, bool use_flow_style = false)
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
  const optris_drivers2::srv::AutoFlag_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  optris_drivers2::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use optris_drivers2::srv::to_yaml() instead")]]
inline std::string to_yaml(const optris_drivers2::srv::AutoFlag_Response & msg)
{
  return optris_drivers2::srv::to_yaml(msg);
}

template<>
inline const char * data_type<optris_drivers2::srv::AutoFlag_Response>()
{
  return "optris_drivers2::srv::AutoFlag_Response";
}

template<>
inline const char * name<optris_drivers2::srv::AutoFlag_Response>()
{
  return "optris_drivers2/srv/AutoFlag_Response";
}

template<>
struct has_fixed_size<optris_drivers2::srv::AutoFlag_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<optris_drivers2::srv::AutoFlag_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<optris_drivers2::srv::AutoFlag_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<optris_drivers2::srv::AutoFlag>()
{
  return "optris_drivers2::srv::AutoFlag";
}

template<>
inline const char * name<optris_drivers2::srv::AutoFlag>()
{
  return "optris_drivers2/srv/AutoFlag";
}

template<>
struct has_fixed_size<optris_drivers2::srv::AutoFlag>
  : std::integral_constant<
    bool,
    has_fixed_size<optris_drivers2::srv::AutoFlag_Request>::value &&
    has_fixed_size<optris_drivers2::srv::AutoFlag_Response>::value
  >
{
};

template<>
struct has_bounded_size<optris_drivers2::srv::AutoFlag>
  : std::integral_constant<
    bool,
    has_bounded_size<optris_drivers2::srv::AutoFlag_Request>::value &&
    has_bounded_size<optris_drivers2::srv::AutoFlag_Response>::value
  >
{
};

template<>
struct is_service<optris_drivers2::srv::AutoFlag>
  : std::true_type
{
};

template<>
struct is_service_request<optris_drivers2::srv::AutoFlag_Request>
  : std::true_type
{
};

template<>
struct is_service_response<optris_drivers2::srv::AutoFlag_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // OPTRIS_DRIVERS2__SRV__DETAIL__AUTO_FLAG__TRAITS_HPP_
