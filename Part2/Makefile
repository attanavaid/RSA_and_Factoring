# Names of your .c files.
SRCS = main.c

# Name of the program you are building
BIN = main

# Compiler flags to pass to the system's C compiler while building
# the source files
CFLAGS = -g -Wall -Wextra -pedantic -std=gnu11 -lgmpxx -lgmp

# Flags to pass to the linker while linking your program
LDFLAGS = -g -lgmpxx -lgmp

# No need to edit anything below this line...
OBJS = $(SRCS:.c=.o)

all: $(BIN)

%.o: %.c
	$(CC) -c $< -o $@ $(CFLAGS)

$(BIN): $(OBJS)
	$(CC) -o $@ $(OBJS) $(LDFLAGS)

clean:
	-rm -f $(OBJS)
	-rm -f $(BIN)