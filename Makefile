CC = pyinstaller

SOURCES = Main.py Session.py Utils.py
TARGET = mrhash

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $< --onefile --distpath . --name $(TARGET) > /dev/null 2>&1

clean:
	rm -rf build $(TARGET).spec


