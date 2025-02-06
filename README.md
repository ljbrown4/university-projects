# **University Projects**  

## **TTS**  

The program provides a variety of functions to interact with stock prices, including finding the latest price, calculating the average, identifying the lowest price and its corresponding day, determining the maximum single-day price change, and checking if any price exceeds a given threshold. Additionally, it includes a feature to suggest the best days to buy and sell for maximum profit. The user interface is built around a loop that continuously displays a menu of options and processes user input until they choose to exit.  

---

## **Final Project**  

This code defines a `TextModel` class that analyzes textual data and classifies it based on linguistic features. It includes helper functions for cleaning text (`clean_text`), stemming words (`stem`), and comparing feature dictionaries (`compare_dictionaries`). The `TextModel` class stores features such as word frequency, word length distribution, sentence length distribution, stem frequency, and adjacent word pairs. It provides methods for adding text from strings and files, saving and loading model data, computing similarity scores, and classifying unknown text by comparing it to reference models. The script includes test functions to demonstrate text classification on sample data.  

---

## **Calendar Dates**  

This code defines a `Date` class that represents calendar dates using day, month, and year attributes. It includes methods for checking leap years, determining the number of days in a month, copying a date, and finding the day of the week. Additional methods allow for advancing the date by one day, checking if one date is before or after another, and calculating the number of days between two dates. The class provides useful operations for manipulating and comparing dates effectively.  

---

## **Connect Four**  

This project implements a Connect Four game using object-oriented programming in Python. The `Board` class handles game board operations, including adding and removing checkers, checking for wins, and resetting the board. The `Player` class represents a human player, while the `RandomPlayer` selects moves randomly. The `connect_four` function facilitates gameplay between two players, processing moves and determining the game outcome. Additionally, the `AIPlayer` class uses a lookahead strategy with different tiebreaking methods to make intelligent moves. The AI evaluates board states recursively, making strategic decisions based on potential future moves.  

## ** Array Recursion **
The `ArrayRecursion` class provides recursive methods to search for an item in an array and to reverse an array into a formatted string representation.

- **Search Method:** Recursively traverses the array from a given start index, returning `true` if the item is found and `false` otherwise.
- **Reverse Method:** Constructs a string representation of the array in reverse order using recursion.
- **Testing:** The `main` method contains test cases to demonstrate the functionality.

## **Sudoku Solver**
This Java program implements a `Sudoku` class that represents and solves a 9x9 Sudoku puzzle using recursive backtracking.

- **Grid Representation:** Maintains a 9x9 puzzle state while tracking fixed values.
- **Optimization:** Uses boolean arrays for rows, columns, and 3x3 subgrids to optimize constraint checking.
- **Recursive Solving:** The `solveRB` method fills in empty cells while ensuring validity using the `isValid` method.
- **File Handling:** Reads an initial puzzle configuration from a file, prints the state, and attempts to solve it. If a solution is found, it is displayed; otherwise, the user is informed that no solution exists.

## **String Node**
The `StringNode` class represents a string using a linked list structure, where each node contains a character and a reference to the next node.

- **Linked List Operations:** Includes methods for manipulating the linked list, such as `charAt`, `indexOf`, `insertAfter`, `deleteChar`, `copy`, and `removeAllSpaces`.
- **Functionality:** Provides flexible character-based operations within the linked list structure.
- **Testing:** The `main` method demonstrates sample usage of these methods for string manipulation.
