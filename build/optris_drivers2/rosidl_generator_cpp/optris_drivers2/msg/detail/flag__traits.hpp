// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from optris_drivers2:msg/Flag.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__TRAITS_HPP_
#define OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "optris_drivers2/msg/detail/flag__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace optris_drivers2
{

namespace msg
{

inline void to_flow_style_yaml(
  const Flag & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: flag_state
  {
    out << "flag_state: ";
    rosidl_generator_traits::value_to_yaml(msg.flag_state, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Flag & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: flag_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "flag_state: ";
    rosidl_generator_traits::value_to_yaml(msg.flag_state, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Flag & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace optris_drivers2

namespace rosidl_generator_traits
{

[[deprecated("use optris_drivers2::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const optris_drivers2::msg::Flag & msg,
  std::ostream & out, size_t indentation = 0)
{
  optris_drivers2::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use optris_drivers2::msg::to_yaml() instead")]]
inline std::string to_yaml(const optris_drivers2::msg::Flag & msg)
{
  return optris_drivers2::msg::to_yaml(msg);
}

template<>
inline const char * data_type<optris_drivers2::msg::Flag>()
{
  return "optris_drivers2::msg::Flag";
}

template<>
inline const char * name<optris_drivers2::msg::Flag>()
{
  return "optris_drivers2/msg/Flag";
}

template<>
struct has_fixed_size<optris_drivers2::msg::Flag>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<optris_drivers2::msg::Flag>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<optris_drivers2::msg::Flag>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__TRAITS_HPP_
