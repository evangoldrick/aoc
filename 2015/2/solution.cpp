#include "../../cpp_helpers/fileReading.hpp"
#include "../../cpp_helpers/extraStringsMethods.hpp"
#include <string>
#include <vector>

struct Present {
    int l;
    int w;
    int h;
    
    Present(int l, int w, int h) {
        this->l = l;
        this->w = w;
        this->h = h;
    }

    int wrappingPaperArea() {
        int slack;
        if (l*w <= w*h && l*w <= h*l) {
            slack = l*w;
        } else if (w*h <= l*w && w*h <= h*l) {
            slack = w*h;
        } else {
            slack = h*l;
        }
        return 2*l*w + 2*w*h + 2*h*l + slack;
    }

    int ribbonLength() {
        int sideRibbonLength = 0;
        if (l <= h && w <= h) {
            sideRibbonLength = 2 * (l + w);
        } else if (w <= l && h <= l) {
            sideRibbonLength = 2 * (w + h);
        } else {
            sideRibbonLength = 2 * (l + h);
        }

        return l*w*h + sideRibbonLength;
    }
};

int main() {
    std::string text = getFileAsString("input.txt");
    
    std::vector<std::string> lines = stdStringSplit(text, '\n');

    std::vector<Present> presents;

    for (auto& line : lines) {
        std::vector<std::string> dimensions = stdStringSplit(line, 'x');
        presents.push_back(*(new Present(stoi(dimensions.at(0)), stoi(dimensions.at(1)), stoi(dimensions.at(2)))));
    }


    int areaSum = 0;
    int ribbonSum = 0;

    for (auto& present : presents) {
        areaSum += present.wrappingPaperArea();
        ribbonSum += present.ribbonLength();
    }
    
    printf("Surface Area: %d\n", areaSum);
    printf("Ribbon Length: %d\n", ribbonSum);

    return 0;
}