#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
//#include "std_msgs/msg/string.hpp"
#include "custom_messages/msg/can_msg.hpp"	//custom message

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
* member function as a callback from the timer. */

class rosNode : public rclcpp::Node
{
  public:
    rosNode()
    : Node("rosNode"), count_(0)
    {
      publisher_ = this->create_publisher<custom_messages::msg::CanMsg>("/can_rx", 10);
      timer_ = this->create_wall_timer(
      500ms, std::bind(&rosNode::timer_callback, this));
    }

  private:
    void timer_callback()
    {
      auto can = custom_messages::msg::CanMsg();
      can.id = 32;
      can.dlc = count_++;
      RCLCPP_INFO(this->get_logger(), "Publishing: 'id:%d dlc:%d'", can.id, can.dlc);
      publisher_->publish(can);
    }
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<custom_messages::msg::CanMsg>::SharedPtr publisher_;
    size_t count_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<rosNode>());
  rclcpp::shutdown();
  return 0;
}
