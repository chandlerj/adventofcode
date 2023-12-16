/*
 * part 2 plan
 * Lets consider the line "two1nine". Reading 
 * in this line should result in 29 being
 * appended to the calibration values list. 
 */
# include<iostream>
# include<string>
# include<vector>
# include<numeric>
# include<fstream>
# include<sstream>
# include<unordered_map>

int sum_calibration_values(std::string input);
int sum_calibration_values_pt2(std::string input);
int check_possible_word(std::string &possible_word, std::unordered_map<std::string, int> name_to_sym);
std::string read_file(std::string path);

int main(){

    // correct calibration number: 142
    std::string testInput = R"(1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet)";
    // correct calibration number: 281
    std::string testInput2 = R"(two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen)";
    
    std::string input_file = read_file("data.txt");

    int sum = sum_calibration_values_pt2(testInput2);        
    std::cout << sum << std::endl;
    return 0;
}

int sum_calibration_values_pt2(std::string input){
    std::unordered_map<std::string, int>name_to_sym = {
        {"one", 1},
        {"two", 2},
        {"three", 3},
        {"four", 4},
        {"five", 5},
        {"six", 6},
        {"seven", 7},
        {"eight", 8},
        {"nine", 9},
        {"zero", 0}
    };
    std::vector<int> cal_vals; 
    std::vector<int> values; // buffer to hold all numerics found in a line
//if input[i] is a char, check if it is a part of a word in the name_to_sym map.
    std::string possible_word; 
    for(int i = 0; i < input.size(); i++){
        if(input[i] == '\n' || i == input.size() - 1){
            
            //append the current value to the calibration vector
            cal_vals.push_back(((values.front() * 10) + values.back()));
            
            std::cout << cal_vals.back() << std::endl;
            values.clear();
        }
        else if(std::isdigit(input[i])){
            values.push_back(input[i] - '0');
        }
        else{
            //append character to possible_word and check if
            //still possible word
            possible_word.push_back(input[i]);
            int check_num = check_possible_word(possible_word, name_to_sym);
            if (check_num != -1){
                values.push_back(check_num);
            }
            else if (possible_word.size() >= 5 && check_num == -1){
                possible_word.clear();
            }
        }
    }

    int result = std::reduce(cal_vals.begin(), cal_vals.end());

    return result;
}
int check_possible_word(std::string &possible_word, std::unordered_map<std::string, int> name_to_sym){
     for(auto name : name_to_sym){ // for number
        std::string intrim_word = name.first;
        for(int i = 0; i < intrim_word.size(); i++){
            if (i >= intrim_word.size() && possible_word == intrim_word){
                std::cout << "Found number " << intrim_word << " which is the same as " << name.second << std::endl;
                return name.second;
            }
            if(possible_word[i] == intrim_word[i]){

                std::cout << "possible match " << possible_word << " <--> " << intrim_word << std::endl;
                continue;
            }
            else{

                break;
            }
        }
     
    }
     
    return -1;
}
int sum_calibration_values(std::string input){

    std::vector<int> cal_vals; 
    std::vector<int> values; 
    
    for(int i = 0; i < input.size(); i++){
        //append the current value to the calibration vector
        //and reset the value list
        if(input[i] == '\n' || i == input.size() - 1){

            cal_vals.push_back(((values.front() * 10) + values.back()));

            std::cout << cal_vals.back() << std::endl;
            values.clear();
        }
        else if(std::isdigit(input[i])){
            values.push_back(input[i] - '0');
        }
    }

    int result = std::reduce(cal_vals.begin(), cal_vals.end());

    return result;
}

std::string read_file(std::string path){
    std::ifstream file(path);
    std::string file_contents;

    if(file){
        std::ostringstream stringStream;
        stringStream << file.rdbuf();
        file_contents = stringStream.str();
    }
    return file_contents;
}


