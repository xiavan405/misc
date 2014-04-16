CC=g++
CCFLAGS=-I/usr/local/include -L/usr/local/lib
LIBS=-lbam -lz -lpthread

all : viewbam

%: %.cc
	$(CC) $(CCFLAGS) -o $@ $^ $(LIBS)
