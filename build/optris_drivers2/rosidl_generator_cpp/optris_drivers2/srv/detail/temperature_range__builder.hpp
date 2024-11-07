// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from optris_drivers2:srv/TemperatureRange.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__SRV__DETAIL__TEMPERATURE_RANGE__BUILDER_HPP_
#define OPTRIS_DRIVERS2__SRV__DETAIL__TEMPERATURE_RANGE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "optris_drivers2/srv/detail/temperature_range__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace optris_drivers2
{

namespace srv
{

namespace builder
{

class Init_TemperatureRange_Request_temperature_range_max
{
public:
  explicit Init_TemperatureRange_Request_temperature_range_max(::optris_drivers2::srv::TemperatureRange_Request & msg)
  : msg_(msg)
  {}
  ::optris_drivers2::srv::TemperatureRange_Request temperature_range_max(::optris_drivers2::srv::TemperatureRange_Request::_temperature_range_max_type arg)
  {
    msg_.temperature_range_max = std::move(arg);
    return std::move(msg_);
  }

private:
  ::optris_drivers2::srv::TemperatureRange_Request msg_;
};

class Init_TemperatureRange_Request_temperature_range_min
{
public:
  Init_TemperatureRange_Request_temperature_range_min()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TemperatureRange_Request_temperature_range_max temperature_range_min(::optris_drivers2::srv::TemperatureRange_Request::_temperature_range_min_type arg)
  {
    msg_.temperature_range_min = std::move(arg);
    return Init_TemperatureRange_Request_temperature_range_max(msg_);
  }

private:
  ::optris_drivers2::srv::TemperatureRange_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::optris_drivers2::srv::TemperatureRange_Request>()
{
  return optris_drivers2::srv::builder::Init_TemperatureRange_Request_temperature_range_min();
}

}  // namespace optris_drivers2


namespace optris_drivers2
{

namespace srv
{

namespace builder
{

class Init_TemperatureRange_Response_success
{
public:
  Init_TemperatureRange_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::optris_drivers2::srv::TemperatureRange_Response success(::optris_drivers2::srv::TemperatureRange_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::optris_drivers2::srv::TemperatureRange_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::optris_drivers2::srv::TemperatureRange_Response>()
{
  return optris_drivers2::srv::builder::Init_TemperatureRange_Response_success();
}

}  // namespace optris_drivers2

#endif  // OPTRIS_DRIVERS2__SRV__DETAIL__TEMPERATURE_RANGE__BUILDER_HPP_
