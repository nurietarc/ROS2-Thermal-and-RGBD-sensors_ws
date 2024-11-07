// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from optris_drivers2:msg/Temperature.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__BUILDER_HPP_
#define OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "optris_drivers2/msg/detail/temperature__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace optris_drivers2
{

namespace msg
{

namespace builder
{

class Init_Temperature_temperature_chip
{
public:
  explicit Init_Temperature_temperature_chip(::optris_drivers2::msg::Temperature & msg)
  : msg_(msg)
  {}
  ::optris_drivers2::msg::Temperature temperature_chip(::optris_drivers2::msg::Temperature::_temperature_chip_type arg)
  {
    msg_.temperature_chip = std::move(arg);
    return std::move(msg_);
  }

private:
  ::optris_drivers2::msg::Temperature msg_;
};

class Init_Temperature_temperature_box
{
public:
  explicit Init_Temperature_temperature_box(::optris_drivers2::msg::Temperature & msg)
  : msg_(msg)
  {}
  Init_Temperature_temperature_chip temperature_box(::optris_drivers2::msg::Temperature::_temperature_box_type arg)
  {
    msg_.temperature_box = std::move(arg);
    return Init_Temperature_temperature_chip(msg_);
  }

private:
  ::optris_drivers2::msg::Temperature msg_;
};

class Init_Temperature_temperature_flag
{
public:
  explicit Init_Temperature_temperature_flag(::optris_drivers2::msg::Temperature & msg)
  : msg_(msg)
  {}
  Init_Temperature_temperature_box temperature_flag(::optris_drivers2::msg::Temperature::_temperature_flag_type arg)
  {
    msg_.temperature_flag = std::move(arg);
    return Init_Temperature_temperature_box(msg_);
  }

private:
  ::optris_drivers2::msg::Temperature msg_;
};

class Init_Temperature_header
{
public:
  Init_Temperature_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Temperature_temperature_flag header(::optris_drivers2::msg::Temperature::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Temperature_temperature_flag(msg_);
  }

private:
  ::optris_drivers2::msg::Temperature msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::optris_drivers2::msg::Temperature>()
{
  return optris_drivers2::msg::builder::Init_Temperature_header();
}

}  // namespace optris_drivers2

#endif  // OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__BUILDER_HPP_
