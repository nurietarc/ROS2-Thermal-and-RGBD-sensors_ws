// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from optris_drivers2:srv/TemperatureRange.idl
// generated code does not contain a copyright notice

#ifndef OPTRIS_DRIVERS2__SRV__DETAIL__TEMPERATURE_RANGE__STRUCT_HPP_
#define OPTRIS_DRIVERS2__SRV__DETAIL__TEMPERATURE_RANGE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__optris_drivers2__srv__TemperatureRange_Request __attribute__((deprecated))
#else
# define DEPRECATED__optris_drivers2__srv__TemperatureRange_Request __declspec(deprecated)
#endif

namespace optris_drivers2
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TemperatureRange_Request_
{
  using Type = TemperatureRange_Request_<ContainerAllocator>;

  explicit TemperatureRange_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->temperature_range_min = 0;
      this->temperature_range_max = 0;
    }
  }

  explicit TemperatureRange_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->temperature_range_min = 0;
      this->temperature_range_max = 0;
    }
  }

  // field types and members
  using _temperature_range_min_type =
    int16_t;
  _temperature_range_min_type temperature_range_min;
  using _temperature_range_max_type =
    int16_t;
  _temperature_range_max_type temperature_range_max;

  // setters for named parameter idiom
  Type & set__temperature_range_min(
    const int16_t & _arg)
  {
    this->temperature_range_min = _arg;
    return *this;
  }
  Type & set__temperature_range_max(
    const int16_t & _arg)
  {
    this->temperature_range_max = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    optris_drivers2::srv::TemperatureRange_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const optris_drivers2::srv::TemperatureRange_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<optris_drivers2::srv::TemperatureRange_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<optris_drivers2::srv::TemperatureRange_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::srv::TemperatureRange_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::srv::TemperatureRange_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::srv::TemperatureRange_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::srv::TemperatureRange_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<optris_drivers2::srv::TemperatureRange_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<optris_drivers2::srv::TemperatureRange_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__optris_drivers2__srv__TemperatureRange_Request
    std::shared_ptr<optris_drivers2::srv::TemperatureRange_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__optris_drivers2__srv__TemperatureRange_Request
    std::shared_ptr<optris_drivers2::srv::TemperatureRange_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TemperatureRange_Request_ & other) const
  {
    if (this->temperature_range_min != other.temperature_range_min) {
      return false;
    }
    if (this->temperature_range_max != other.temperature_range_max) {
      return false;
    }
    return true;
  }
  bool operator!=(const TemperatureRange_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TemperatureRange_Request_

// alias to use template instance with default allocator
using TemperatureRange_Request =
  optris_drivers2::srv::TemperatureRange_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace optris_drivers2


#ifndef _WIN32
# define DEPRECATED__optris_drivers2__srv__TemperatureRange_Response __attribute__((deprecated))
#else
# define DEPRECATED__optris_drivers2__srv__TemperatureRange_Response __declspec(deprecated)
#endif

namespace optris_drivers2
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TemperatureRange_Response_
{
  using Type = TemperatureRange_Response_<ContainerAllocator>;

  explicit TemperatureRange_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit TemperatureRange_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    optris_drivers2::srv::TemperatureRange_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const optris_drivers2::srv::TemperatureRange_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<optris_drivers2::srv::TemperatureRange_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<optris_drivers2::srv::TemperatureRange_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::srv::TemperatureRange_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::srv::TemperatureRange_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      optris_drivers2::srv::TemperatureRange_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<optris_drivers2::srv::TemperatureRange_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<optris_drivers2::srv::TemperatureRange_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<optris_drivers2::srv::TemperatureRange_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__optris_drivers2__srv__TemperatureRange_Response
    std::shared_ptr<optris_drivers2::srv::TemperatureRange_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__optris_drivers2__srv__TemperatureRange_Response
    std::shared_ptr<optris_drivers2::srv::TemperatureRange_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TemperatureRange_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const TemperatureRange_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TemperatureRange_Response_

// alias to use template instance with default allocator
using TemperatureRange_Response =
  optris_drivers2::srv::TemperatureRange_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace optris_drivers2

namespace optris_drivers2
{

namespace srv
{

struct TemperatureRange
{
  using Request = optris_drivers2::srv::TemperatureRange_Request;
  using Response = optris_drivers2::srv::TemperatureRange_Response;
};

}  // namespace srv

}  // namespace optris_drivers2

#endif  // OPTRIS_DRIVERS2__SRV__DETAIL__TEMPERATURE_RANGE__STRUCT_HPP_
