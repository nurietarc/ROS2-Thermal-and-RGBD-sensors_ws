// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from optris_drivers2:msg/Flag.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__BUILDER_HPP_
#define OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "optris_drivers2/msg/detail/flag__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace optris_drivers2
{

namespace msg
{

namespace builder
{

class Init_Flag_flag_state
{
public:
  explicit Init_Flag_flag_state(::optris_drivers2::msg::Flag & msg)
  : msg_(msg)
  {}
  ::optris_drivers2::msg::Flag flag_state(::optris_drivers2::msg::Flag::_flag_state_type arg)
  {
    msg_.flag_state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::optris_drivers2::msg::Flag msg_;
};

class Init_Flag_header
{
public:
  Init_Flag_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Flag_flag_state header(::optris_drivers2::msg::Flag::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Flag_flag_state(msg_);
  }

private:
  ::optris_drivers2::msg::Flag msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::optris_drivers2::msg::Flag>()
{
  return optris_drivers2::msg::builder::Init_Flag_header();
}

}  // namespace optris_drivers2

#endif  // OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__BUILDER_HPP_
