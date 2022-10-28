#include <string>
#include <vector>

std::vector<std::string> stdStringSplit(std::string const & str, char const delimeter) {
    std::vector<std::string> returnVal;

    int lastSplit = 0;
    for (int currentChar = 0; currentChar < str.length(); ++currentChar) {
        if (str.at(currentChar) == delimeter) {
            returnVal.push_back(str.substr(lastSplit, currentChar - lastSplit));
            lastSplit = currentChar + 1;
        }
    }
    returnVal.push_back(str.substr(lastSplit, str.length() - lastSplit));
    return returnVal;
}
