// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from optris_drivers2:msg/Temperature.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__TRAITS_HPP_
#define OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "optris_drivers2/msg/detail/temperature__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace optris_drivers2
{

namespace msg
{

inline void to_flow_style_yaml(
  const Temperature & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: temperature_flag
  {
    out << "temperature_flag: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature_flag, out);
    out << ", ";
  }

  // member: temperature_box
  {
    out << "temperature_box: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature_box, out);
    out << ", ";
  }

  // member: temperature_chip
  {
    out << "temperature_chip: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature_chip, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Temperature & msg,
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

  // member: temperature_flag
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "temperature_flag: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature_flag, out);
    out << "\n";
  }

  // member: temperature_box
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "temperature_box: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature_box, out);
    out << "\n";
  }

  // member: temperature_chip
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "temperature_chip: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature_chip, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Temperature & msg, bool use_flow_style = false)
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
  const optris_drivers2::msg::Temperature & msg,
  std::ostream & out, size_t indentation = 0)
{
  optris_drivers2::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use optris_drivers2::msg::to_yaml() instead")]]
inline std::string to_yaml(const optris_drivers2::msg::Temperature & msg)
{
  return optris_drivers2::msg::to_yaml(msg);
}

template<>
inline const char * data_type<optris_drivers2::msg::Temperature>()
{
  return "optris_drivers2::msg::Temperature";
}

template<>
inline const char * name<optris_drivers2::msg::Temperature>()
{
  return "optris_drivers2/msg/Temperature";
}

template<>
struct has_fixed_size<optris_drivers2::msg::Temperature>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<optris_drivers2::msg::Temperature>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<optris_drivers2::msg::Temperature>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__TRAITS_HPP_
