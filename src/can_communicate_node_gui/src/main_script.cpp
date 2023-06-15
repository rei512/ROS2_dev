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

class rosNode: public rclcpp::Node {
  public:
	rosNode()
	: Node("canCommuNode"), count_(0)
	{
	  publisher_ = this->create_publisher<custom_messages::msg::CanMsg>("/can_rx", 10);
	  //can.dlc = 8;
	  //RCLCPP_INFO(this->get_logger(), "Publishing: 'id:%d dlc:%d'", can.id, can.dlc);
	  //timer_ = this->create_wall_timer(
	  //500ms, std::bind(&rosNode::timer_callback, this));
	}

	void loop() {
		while(1) {
			//std::cout << this << std::endl;
			std::printf("%dch frametype:%d Address:%d DLC:%d\ndata:", can.channel, can.frametype, can.id, can.dlc);
			for(int i=0;i < can.dlc;i++) {
				std::cout  << " "<< can.data[i];
			}
			std::cout << std::endl;
			std::string input;
			std::cout << "> ";
			std::cin >> input;
			if(input[0] != '!') {
				for(int i=0;i<8;i++) {
					can.data[i] = input[i];
				}
				publish();
				//RCLCPP_INFO(this->get_logger(), "Publishing: 'ch:%d frame:%d id:%d dlc:%d data:%s'", can.channel, can.frametype, can.id, can.dlc, &can.data[0]);
			}

			if(!input.compare(1, 2, "CH")) {
				if(input[4] == '0') {
					can.channel = true;
				} else if(input[4] == '1') {
					can.channel = false;
				} else {
					printf("invalid action. please input 0/1");
				}
			}

			if(!input.compare(1, 11, "frametype")) {
				if(input[12] == '0') {
					can.frametype = true;
				} else if(input[12] == '1') {
					can.frametype = false;
				} else {
					printf("invalid action. please input 0/1");
				}
			}
			if(!input.compare(1, 2, "Address")) {
				can.id = std::stoi(input.substr(9));
			}

			if(!input.compare(1, 2, "DLC")) {
				can.dlc = std::stoi(input.substr(5));
			}

			if(!input.compare(1, 4, "exit")) {
				std::cout << "exit" << std::endl;
				return;
			}
		}
	}

	friend std::ostream& operator<<(std::ostream& stream, const rosNode &node);


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

//std::ostream& operator<<(std::ostream& stream, const rosNode &node) {
//	const std::string value = "\n\n\n\nCH:" << std::noboolalpha << node.can.channel << "\tflametype: " << node.can.frametype << "\tAddress: " << node.can.id << "\tDLC: " << node.can.dlc;
//	stream << value;
//	return stream;
//};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rosNode can;
  //rclcpp::spin(std::make_shared<rosNode>());
  can.loop();
  rclcpp::shutdown();
  return 0;
}
