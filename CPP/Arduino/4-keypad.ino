	#include <Keypad.h>
	
	const byte ROWS = 4; 
	const byte COLS = 4; 
	
	char keys[ROWS][COLS] = {
	  {'1', '2', '3', 'A'},
	  {'4', '5', '6', 'B'},
	  {'7', '8', '9', 'C'},
	  {'*', '0', '#', 'D'}
	};
	
	char altChars[ROWS][COLS][3] = {  // Define alternative characters for each key
	  {{'1', '!', '@'}, {'2', 'A', 'B'}, {'3', 'C', 'D'}, {'A', 'E', 'F'}},
	  {{'4', 'G', 'H'}, {'5', 'I', 'J'}, {'6', 'K', 'L'}, {'B', 'M', 'N'}},
	  {{'7', 'O', 'P'}, {'8', 'Q', 'R'}, {'9', 'S', 'T'}, {'C', 'U', 'V'}},
	  {{'*', 'W', 'X'}, {'0', 'Y', 'Z'}, {'#', '-', '+'}, {'D', '_', '='}}
	};
	
	byte rowPins[ROWS] = {9, 8, 7, 6};  // Connect to the row pinouts
	byte colPins[COLS] = {5, 4, 3, 2};  // Connect to the column pinouts
	
	Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);
	
	int keyPressCount[ROWS][COLS] = {0};  // Counter for each key
	unsigned long lastPressTime[ROWS][COLS] = {0};  // Timestamp for last key press
	const int resetTime = 2000;  // Reset cycle after 2 seconds of inactivity
	
	void setup() {
	  Serial.begin(9600);
	}
	
	void loop() {
	  char key = keypad.getKey();
	  if (key) {
	    int row, col;
	    
	    // Find key position in the matrix
	    for (row = 0; row < ROWS; row++) {
	      for (col = 0; col < COLS; col++) {
	        if (keys[row][col] == key) break;
	      }
	      if (col < COLS) break;
	    }
	
	    // Reset counter if time elapsed
	    if (millis() - lastPressTime[row][col] > resetTime) {
	      keyPressCount[row][col] = 0;
	    }
	
	    // Cycle through alternative characters
	    char outputChar = altChars[row][col][keyPressCount[row][col]];
	    Serial.print("Pressed: ");
	    Serial.println(outputChar);
	
	    // Increment the counter and reset if it exceeds available characters
	    keyPressCount[row][col] = (keyPressCount[row][col] + 1) % 3;
	
	    // Store the time of the last key press
	    lastPressTime[row][col] = millis();
	  }
	}