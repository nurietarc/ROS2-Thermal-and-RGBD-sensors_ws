// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from optris_drivers2:msg/Flag.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__STRUCT_HPP_
#define OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__STRUCT_HPP_

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
# define DEPRECATED__optris_drivers2__msg__Flag __attribute__((deprecated))
#else
# define DEPRECATED__optris_drivers2__msg__Flag __declspec(deprecated)
#endif

namespace optris_drivers2
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Flag_
{
  using Type = Flag_<ContainerAllocator>;

  explicit Flag_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->flag_state = 0ul;
    }
  }

  explicit Flag_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->flag_state = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _flag_state_type =
    uint32_t;
  _flag_state_type flag_state;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__flag_state(
    const uint32_t & _arg)
  {
    this->flag_state = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    optris_drivers2::msg::Flag_<ContainerAllocator> *;
  using ConstRawPtr =
    const optris_drivers2::msg::Flag_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<optris_drivers2::msg::Flag_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<optris_drivers2::msg::Flag_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::msg::Flag_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::msg::Flag_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::msg::Flag_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::msg::Flag_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<optris_drivers2::msg::Flag_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<optris_drivers2::msg::Flag_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__optris_drivers2__msg__Flag
    std::shared_ptr<optris_drivers2::msg::Flag_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__optris_drivers2__msg__Flag
    std::shared_ptr<optris_drivers2::msg::Flag_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Flag_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->flag_state != other.flag_state) {
      return false;
    }
    return true;
  }
  bool operator!=(const Flag_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Flag_

// alias to use template instance with default allocator
using Flag =
  optris_drivers2::msg::Flag_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace optris_drivers2

#endif  // OPTRIS_DRIVERS2__MSG__DETAIL__FLAG__STRUCT_HPP_
