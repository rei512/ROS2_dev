#include <chrono>
#include <functional>
#include <memory>
#include <string>
#include <iostream>

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
	  //RCLCPP_INFO(this->get_logger(), "Publishing: 'id:%d dlc:%d'", can.id, can.dlc);
	  //timer_ = this->create_wall_timer(
	  //500ms, std::bind(&rosNode::timer_callback, this));
	}

	void loop() {
		while(1) {
			std::string input;
			std::cout << "> ";
			std::cin >>input;
			if(input[2] != '!') {
				if(input[2] == '\n') {
					std::cout << "Empty!" << std::endl;
				}
				publish();
				RCLCPP_INFO(this->get_logger(), "Publishing: 'id:%d dlc:%d'", can.id, can.dlc);
			}
			if(!input.compare(1, 4, "exit")) {
				std::cout << "exit" << std::endl;
				return;
			}
		}
	}

  private:
	//void timer_callback()
	//{
	//  auto can = custom_messages::msg::CanMsg();
	//  can.id = 32;
	//  can.dlc = count_++;
	//  RCLCPP_INFO(this->get_logger(), "Publishing: 'id:%d dlc:%d'", can.id, can.dlc);
	//  publisher_->publish(can);
	//}
	//rclcpp::TimerBase::SharedPtr timer_;
	rclcpp::Publisher<custom_messages::msg::CanMsg>::SharedPtr publisher_;
	size_t count_;
	custom_messages::msg::CanMsg can;

	void publish() {
		publisher_->publish(can);
	}

};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rosNode can;
  //rclcpp::spin(std::make_shared<rosNode>());
  can.loop();
  rclcpp::shutdown();
  return 0;
}
