// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from optris_drivers2:srv/Palette.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__SRV__DETAIL__PALETTE__STRUCT_HPP_
#define OPTRIS_DRIVERS2__SRV__DETAIL__PALETTE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__optris_drivers2__srv__Palette_Request __attribute__((deprecated))
#else
# define DEPRECATED__optris_drivers2__srv__Palette_Request __declspec(deprecated)
#endif

namespace optris_drivers2
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Palette_Request_
{
  using Type = Palette_Request_<ContainerAllocator>;

  explicit Palette_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->palette = 0;
      this->palette_scaling = 0;
      this->temperature_min = 0.0f;
      this->temperature_max = 0.0f;
    }
  }

  explicit Palette_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->palette = 0;
      this->palette_scaling = 0;
      this->temperature_min = 0.0f;
      this->temperature_max = 0.0f;
    }
  }

  // field types and members
  using _palette_type =
    int16_t;
  _palette_type palette;
  using _palette_scaling_type =
    int16_t;
  _palette_scaling_type palette_scaling;
  using _temperature_min_type =
    float;
  _temperature_min_type temperature_min;
  using _temperature_max_type =
    float;
  _temperature_max_type temperature_max;

  // setters for named parameter idiom
  Type & set__palette(
    const int16_t & _arg)
  {
    this->palette = _arg;
    return *this;
  }
  Type & set__palette_scaling(
    const int16_t & _arg)
  {
    this->palette_scaling = _arg;
    return *this;
  }
  Type & set__temperature_min(
    const float & _arg)
  {
    this->temperature_min = _arg;
    return *this;
  }
  Type & set__temperature_max(
    const float & _arg)
  {
    this->temperature_max = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    optris_drivers2::srv::Palette_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const optris_drivers2::srv::Palette_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<optris_drivers2::srv::Palette_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<optris_drivers2::srv::Palette_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::srv::Palette_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::srv::Palette_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::srv::Palette_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::srv::Palette_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<optris_drivers2::srv::Palette_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<optris_drivers2::srv::Palette_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__optris_drivers2__srv__Palette_Request
    std::shared_ptr<optris_drivers2::srv::Palette_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__optris_drivers2__srv__Palette_Request
    std::shared_ptr<optris_drivers2::srv::Palette_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Palette_Request_ & other) const
  {
    if (this->palette != other.palette) {
      return false;
    }
    if (this->palette_scaling != other.palette_scaling) {
      return false;
    }
    if (this->temperature_min != other.temperature_min) {
      return false;
    }
    if (this->temperature_max != other.temperature_max) {
      return false;
    }
    return true;
  }
  bool operator!=(const Palette_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Palette_Request_

// alias to use template instance with default allocator
using Palette_Request =
  optris_drivers2::srv::Palette_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace optris_drivers2


#ifndef _WIN32
# define DEPRECATED__optris_drivers2__srv__Palette_Response __attribute__((deprecated))
#else
# define DEPRECATED__optris_drivers2__srv__Palette_Response __declspec(deprecated)
#endif

namespace optris_drivers2
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Palette_Response_
{
  using Type = Palette_Response_<ContainerAllocator>;

  explicit Palette_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit Palette_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    optris_drivers2::srv::Palette_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const optris_drivers2::srv::Palette_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<optris_drivers2::srv::Palette_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<optris_drivers2::srv::Palette_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::srv::Palette_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::srv::Palette_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::srv::Palette_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::srv::Palette_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<optris_drivers2::srv::Palette_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<optris_drivers2::srv::Palette_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__optris_drivers2__srv__Palette_Response
    std::shared_ptr<optris_drivers2::srv::Palette_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__optris_drivers2__srv__Palette_Response
    std::shared_ptr<optris_drivers2::srv::Palette_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Palette_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const Palette_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Palette_Response_

// alias to use template instance with default allocator
using Palette_Response =
  optris_drivers2::srv::Palette_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace optris_drivers2

namespace optris_drivers2
{

namespace srv
{

struct Palette
{
  using Request = optris_drivers2::srv::Palette_Request;
  using Response = optris_drivers2::srv::Palette_Response;
};

}  // namespace srv

}  // namespace optris_drivers2

#endif  // OPTRIS_DRIVERS2__SRV__DETAIL__PALETTE__STRUCT_HPP_
