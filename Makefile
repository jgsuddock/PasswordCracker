test: main.o
	g++ -g -std=c++11 main.o -o test
main.o: main.cpp
	g++ -g -c -std=c++11 main.cpp
clean:
	rm *.o test