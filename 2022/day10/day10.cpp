/*
 * addx V takes two cycles to complete. After two cycles, 
 * the X register is increased by the value V. (V can be negative.)
 * noop takes one cycle to complete. It has no other effect.
 */
#include<iostream> 
#include<vector> 
#include <string>
#include <fstream>

int main(){
  std::ifstream filepath("testInput.txt");
  std::string log;
  std::vector<std::string> log_list;
  if (filepath){
    while(filepath.good()){
      std::getline(filepath, log);
      std::cout << log << std::endl;
    }
  }

  return 0;
}

