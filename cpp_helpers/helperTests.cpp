#include "extraStringsMethods.hpp"
#include "fileReading.hpp"
#include <assert.h>
#include <string>
#include <vector>

void splitTest() {
    std::string testString = std::string(" Hello World  ");
    std::vector<std::string> result = stdStringSplit(testString, ' ');
    printf("%s", result.at(1).c_str());
    fflush(stdout);
    assert(result.size() == 5);
    assert(result.at(0) == std::string(""));
    assert(result.at(1) == std::string("Hello"));
    assert(result.at(2) == std::string("World"));
    assert(result.at(3) == std::string(""));
    assert(result.at(4) == std::string(""));
}



int main() {
    splitTest();
    return 0;
}
