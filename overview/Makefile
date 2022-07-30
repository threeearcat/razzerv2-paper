NAME=overview

INPUT=$(NAME).md
OUTPUT=$(NAME).pdf

all: $(OUTPUT)

$(OUTPUT): $(INPUT)
	pandoc -t beamer --slide-level=2 -o $(OUTPUT) $(INPUT)

clean:
	rm $(OUTPUT)

.PHONY: all clean
