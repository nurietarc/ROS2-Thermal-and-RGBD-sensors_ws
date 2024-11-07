// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from optris_drivers2:srv/AutoFlag.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__SRV__DETAIL__AUTO_FLAG__STRUCT_HPP_
#define OPTRIS_DRIVERS2__SRV__DETAIL__AUTO_FLAG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__optris_drivers2__srv__AutoFlag_Request __attribute__((deprecated))
#else
# define DEPRECATED__optris_drivers2__srv__AutoFlag_Request __declspec(deprecated)
#endif

namespace optris_drivers2
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AutoFlag_Request_
{
  using Type = AutoFlag_Request_<ContainerAllocator>;

  explicit AutoFlag_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->auto_flag = false;
    }
  }

  explicit AutoFlag_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->auto_flag = false;
    }
  }

  // field types and members
  using _auto_flag_type =
    bool;
  _auto_flag_type auto_flag;

  // setters for named parameter idiom
  Type & set__auto_flag(
    const bool & _arg)
  {
    this->auto_flag = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    optris_drivers2::srv::AutoFlag_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const optris_drivers2::srv::AutoFlag_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<optris_drivers2::srv::AutoFlag_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<optris_drivers2::srv::AutoFlag_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::srv::AutoFlag_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::srv::AutoFlag_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::srv::AutoFlag_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::srv::AutoFlag_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<optris_drivers2::srv::AutoFlag_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<optris_drivers2::srv::AutoFlag_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__optris_drivers2__srv__AutoFlag_Request
    std::shared_ptr<optris_drivers2::srv::AutoFlag_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__optris_drivers2__srv__AutoFlag_Request
    std::shared_ptr<optris_drivers2::srv::AutoFlag_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AutoFlag_Request_ & other) const
  {
    if (this->auto_flag != other.auto_flag) {
      return false;
    }
    return true;
  }
  bool operator!=(const AutoFlag_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AutoFlag_Request_

// alias to use template instance with default allocator
using AutoFlag_Request =
  optris_drivers2::srv::AutoFlag_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace optris_drivers2


#ifndef _WIN32
# define DEPRECATED__optris_drivers2__srv__AutoFlag_Response __attribute__((deprecated))
#else
# define DEPRECATED__optris_drivers2__srv__AutoFlag_Response __declspec(deprecated)
#endif

namespace optris_drivers2
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AutoFlag_Response_
{
  using Type = AutoFlag_Response_<ContainerAllocator>;

  explicit AutoFlag_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_auto_flag_active = false;
    }
  }

  explicit AutoFlag_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_auto_flag_active = false;
    }
  }

  // field types and members
  using _is_auto_flag_active_type =
    bool;
  _is_auto_flag_active_type is_auto_flag_active;

  // setters for named parameter idiom
  Type & set__is_auto_flag_active(
    const bool & _arg)
  {
    this->is_auto_flag_active = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    optris_drivers2::srv::AutoFlag_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const optris_drivers2::srv::AutoFlag_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<optris_drivers2::srv::AutoFlag_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<optris_drivers2::srv::AutoFlag_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::srv::AutoFlag_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::srv::AutoFlag_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::srv::AutoFlag_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::srv::AutoFlag_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<optris_drivers2::srv::AutoFlag_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<optris_drivers2::srv::AutoFlag_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__optris_drivers2__srv__AutoFlag_Response
    std::shared_ptr<optris_drivers2::srv::AutoFlag_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__optris_drivers2__srv__AutoFlag_Response
    std::shared_ptr<optris_drivers2::srv::AutoFlag_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AutoFlag_Response_ & other) const
  {
    if (this->is_auto_flag_active != other.is_auto_flag_active) {
      return false;
    }
    return true;
  }
  bool operator!=(const AutoFlag_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AutoFlag_Response_

// alias to use template instance with default allocator
using AutoFlag_Response =
  optris_drivers2::srv::AutoFlag_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace optris_drivers2

namespace optris_drivers2
{

namespace srv
{

struct AutoFlag
{
  using Request = optris_drivers2::srv::AutoFlag_Request;
  using Response = optris_drivers2::srv::AutoFlag_Response;
};

}  // namespace srv

}  // namespace optris_drivers2

#endif  // OPTRIS_DRIVERS2__SRV__DETAIL__AUTO_FLAG__STRUCT_HPP_
