// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from optris_drivers2:msg/Temperature.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__STRUCT_HPP_
#define OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__optris_drivers2__msg__Temperature __attribute__((deprecated))
#else
# define DEPRECATED__optris_drivers2__msg__Temperature __declspec(deprecated)
#endif

namespace optris_drivers2
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Temperature_
{
  using Type = Temperature_<ContainerAllocator>;

  explicit Temperature_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->temperature_flag = 0.0f;
      this->temperature_box = 0.0f;
      this->temperature_chip = 0.0f;
    }
  }

  explicit Temperature_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->temperature_flag = 0.0f;
      this->temperature_box = 0.0f;
      this->temperature_chip = 0.0f;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _temperature_flag_type =
    float;
  _temperature_flag_type temperature_flag;
  using _temperature_box_type =
    float;
  _temperature_box_type temperature_box;
  using _temperature_chip_type =
    float;
  _temperature_chip_type temperature_chip;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__temperature_flag(
    const float & _arg)
  {
    this->temperature_flag = _arg;
    return *this;
  }
  Type & set__temperature_box(
    const float & _arg)
  {
    this->temperature_box = _arg;
    return *this;
  }
  Type & set__temperature_chip(
    const float & _arg)
  {
    this->temperature_chip = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    optris_drivers2::msg::Temperature_<ContainerAllocator> *;
  using ConstRawPtr =
    const optris_drivers2::msg::Temperature_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<optris_drivers2::msg::Temperature_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<optris_drivers2::msg::Temperature_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::msg::Temperature_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::msg::Temperature_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::msg::Temperature_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::msg::Temperature_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<optris_drivers2::msg::Temperature_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<optris_drivers2::msg::Temperature_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__optris_drivers2__msg__Temperature
    std::shared_ptr<optris_drivers2::msg::Temperature_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__optris_drivers2__msg__Temperature
    std::shared_ptr<optris_drivers2::msg::Temperature_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Temperature_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->temperature_flag != other.temperature_flag) {
      return false;
    }
    if (this->temperature_box != other.temperature_box) {
      return false;
    }
    if (this->temperature_chip != other.temperature_chip) {
      return false;
    }
    return true;
  }
  bool operator!=(const Temperature_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Temperature_

// alias to use template instance with default allocator
using Temperature =
  optris_drivers2::msg::Temperature_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace optris_drivers2

#endif  // OPTRIS_DRIVERS2__MSG__DETAIL__TEMPERATURE__STRUCT_HPP_
