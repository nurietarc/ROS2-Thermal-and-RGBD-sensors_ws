// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from optris_drivers2:srv/AutoFlag.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__SRV__DETAIL__AUTO_FLAG__BUILDER_HPP_
#define OPTRIS_DRIVERS2__SRV__DETAIL__AUTO_FLAG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "optris_drivers2/srv/detail/auto_flag__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace optris_drivers2
{

namespace srv
{

namespace builder
{

class Init_AutoFlag_Request_auto_flag
{
public:
  Init_AutoFlag_Request_auto_flag()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::optris_drivers2::srv::AutoFlag_Request auto_flag(::optris_drivers2::srv::AutoFlag_Request::_auto_flag_type arg)
  {
    msg_.auto_flag = std::move(arg);
    return std::move(msg_);
  }

private:
  ::optris_drivers2::srv::AutoFlag_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::optris_drivers2::srv::AutoFlag_Request>()
{
  return optris_drivers2::srv::builder::Init_AutoFlag_Request_auto_flag();
}

}  // namespace optris_drivers2


namespace optris_drivers2
{

namespace srv
{

namespace builder
{

class Init_AutoFlag_Response_is_auto_flag_active
{
public:
  Init_AutoFlag_Response_is_auto_flag_active()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::optris_drivers2::srv::AutoFlag_Response is_auto_flag_active(::optris_drivers2::srv::AutoFlag_Response::_is_auto_flag_active_type arg)
  {
    msg_.is_auto_flag_active = std::move(arg);
    return std::move(msg_);
  }

private:
  ::optris_drivers2::srv::AutoFlag_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::optris_drivers2::srv::AutoFlag_Response>()
{
  return optris_drivers2::srv::builder::Init_AutoFlag_Response_is_auto_flag_active();
}

}  // namespace optris_drivers2

#endif  // OPTRIS_DRIVERS2__SRV__DETAIL__AUTO_FLAG__BUILDER_HPP_
