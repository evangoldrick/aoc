#!/bin/bash

javac -d ./build/ *.java &&
java -cp ./build/ Both $1
