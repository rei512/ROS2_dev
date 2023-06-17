#include <chrono>
#include <functional>
#include <memory>
#include <string>
#include <iostream>
#include <sstream>
#include <ranges>
#include <vector>

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
	  can.dlc = 8;
	  for(int i=0;i<8;i++) {
		can.data.push_back(0);
	  }
	  //RCLCPP_INFO(this->get_logger(), "Publishing: 'id:%d dlc:%d'", can.id, can.dlc);
	  //timer_ = this->create_wall_timer(
	  //500ms, std::bind(&rosNode::timer_callback, this));
	}

	void loop() {
		while(1) {
			//std::cout << this << std::endl;
			std::string input;
			std::string tmp;
			std::stringstream ss;
			static bool hex = true;
			std::vector<std::string> item;
			int value;

			if(hex) {
				ss << std::hex << can.id;
				value = std::stoi(ss.str());
				std::printf("\n\n%dch frametype:%d Address:0x%d DLC:%d\ndata:", can.channel, can.frametype, value, can.dlc);
				ss.str("");
				ss.clear(std::stringstream::goodbit);
			} else {
				std::printf("\n\n%dch frametype:%d Address:%d DLC:%d\ndata:", can.channel, can.frametype, can.id, can.dlc);
			}
			
			
			
			for(int i=0;i < can.dlc;i++) {
				value =can.data[i];

				if(hex) {
					ss << std::hex << value;
					std::cout  << " 0x"<< ss.str();
					ss.str("");
					ss.clear(std::stringstream::goodbit);
				} else {
					std::cout  << " "<< value;
				}
			}

			std::cout << "\n> ";

			getline(std::cin, input);

			ss << input;

			while(std::getline(ss, tmp, ' ')) {
				item.push_back(tmp);
			}

			if(item.empty()) {
				std::cout << "input data is empty!" << std::endl;
				continue;
			}

			if(item[0] == "!exit") {
				return;
			}

			if(item[0] == "!HEX") {
				if(item.size() == 2 && (item[1] == "TRUE" || item[1] == "true")) {
					hex = true;
				}
				else if(item.size() == 2 && (item[1] == "FALSE" || item[1] == "false")) {
					hex = false;
				}
				else {
					std::cout << "invalid value or segment. please input TRUE/FALSE" << std::endl;
				}
			}

			else if(item[0] == "!SEND") {
				publish();
				std::cout << "Published!" << std::endl;
			}

			else if(item[0] == "!H" || item[0] == "!HELP") {
				std::cout << "Here is the !HELP messages\n!CH \t- channel select 0/1	\n!FT \t- frametype select 0(data)/1(rtr)	\n!ADD\t- Address select 0 - 2047(0x7FF)	\n!DLC\t- Data Length Code 0 - 8	\n!SEND\t- Publish messages	\n!HEX\t- Show value in hexadecimal, else decimal TRUE/FALSE 	\n!exit\t- close application(!!! DO NOT USE Ctrl+C !!!)	\n" << std::endl;
			}

			else if(item[0] == "!CH") {
				if(item.size() == 2 && item[1] == "1") {
					can.channel = true;
				}
				else if(item.size() == 2 && item[1] == "0") {
					can.channel = false;
				}
				else {
					std::cout << "invalid value or segment. please input 0/1" << std::endl;
				}
			}

			else if(item[0] == "!FT") {
				if(item.size() == 2 && item[1] == "1") {
					can.frametype = true;
				}
				else if(item.size() == 2 && item[1] == "0") {
					can.frametype = false;
				}
				else {
					std::cout << "invalid value or segment. please input 0/1" << std::endl;
				}
			}

			else if(item.size() == 2 && item[0] == "!ADD" && std::stod(item[1])  >= 0 && std::stod(item[1]) < 2048) {
				can.id = (int)std::stod(item[1]);
			}

			else if(item.size() == 2 && item[0] == "!DLC" && std::stod(item[1])  >= 0 && std::stod(item[1]) <= 8) {
				can.dlc = (char)std::stod(item[1]);
			}

			else if(item.size() == can.dlc) {
				for(int i=0;i<can.dlc;i++) {
					can.data[i] = (char)std::stod(item[i]);
				} 
			}

			else {
				std::cout << "invalid value,segment or command. check command !H(!HELP)" << std::endl;
			}

			//for(auto &s : item) {
			//	std::cout << s << std::endl;
			//}

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
