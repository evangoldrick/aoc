#include <string>
#include <fstream>
#include <sstream>

std::string getFileAsString(std::string const &  fileName) {
    std::ifstream file(fileName);

    std::stringstream fileStream;
    fileStream << file.rdbuf();

    return fileStream.str();
}

inline std::string getFileAsString(char const * const fileName) {
    std::string fileNameAsString = std::string(fileName);

    return getFileAsString(fileNameAsString);
}
