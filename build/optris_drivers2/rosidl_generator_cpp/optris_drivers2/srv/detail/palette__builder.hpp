// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from optris_drivers2:srv/Palette.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__SRV__DETAIL__PALETTE__BUILDER_HPP_
#define OPTRIS_DRIVERS2__SRV__DETAIL__PALETTE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "optris_drivers2/srv/detail/palette__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace optris_drivers2
{

namespace srv
{

namespace builder
{

class Init_Palette_Request_temperature_max
{
public:
  explicit Init_Palette_Request_temperature_max(::optris_drivers2::srv::Palette_Request & msg)
  : msg_(msg)
  {}
  ::optris_drivers2::srv::Palette_Request temperature_max(::optris_drivers2::srv::Palette_Request::_temperature_max_type arg)
  {
    msg_.temperature_max = std::move(arg);
    return std::move(msg_);
  }

private:
  ::optris_drivers2::srv::Palette_Request msg_;
};

class Init_Palette_Request_temperature_min
{
public:
  explicit Init_Palette_Request_temperature_min(::optris_drivers2::srv::Palette_Request & msg)
  : msg_(msg)
  {}
  Init_Palette_Request_temperature_max temperature_min(::optris_drivers2::srv::Palette_Request::_temperature_min_type arg)
  {
    msg_.temperature_min = std::move(arg);
    return Init_Palette_Request_temperature_max(msg_);
  }

private:
  ::optris_drivers2::srv::Palette_Request msg_;
};

class Init_Palette_Request_palette_scaling
{
public:
  explicit Init_Palette_Request_palette_scaling(::optris_drivers2::srv::Palette_Request & msg)
  : msg_(msg)
  {}
  Init_Palette_Request_temperature_min palette_scaling(::optris_drivers2::srv::Palette_Request::_palette_scaling_type arg)
  {
    msg_.palette_scaling = std::move(arg);
    return Init_Palette_Request_temperature_min(msg_);
  }

private:
  ::optris_drivers2::srv::Palette_Request msg_;
};

class Init_Palette_Request_palette
{
public:
  Init_Palette_Request_palette()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Palette_Request_palette_scaling palette(::optris_drivers2::srv::Palette_Request::_palette_type arg)
  {
    msg_.palette = std::move(arg);
    return Init_Palette_Request_palette_scaling(msg_);
  }

private:
  ::optris_drivers2::srv::Palette_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::optris_drivers2::srv::Palette_Request>()
{
  return optris_drivers2::srv::builder::Init_Palette_Request_palette();
}

}  // namespace optris_drivers2


namespace optris_drivers2
{

namespace srv
{

namespace builder
{

class Init_Palette_Response_success
{
public:
  Init_Palette_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::optris_drivers2::srv::Palette_Response success(::optris_drivers2::srv::Palette_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::optris_drivers2::srv::Palette_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::optris_drivers2::srv::Palette_Response>()
{
  return optris_drivers2::srv::builder::Init_Palette_Response_success();
}

}  // namespace optris_drivers2

#endif  // OPTRIS_DRIVERS2__SRV__DETAIL__PALETTE__BUILDER_HPP_
