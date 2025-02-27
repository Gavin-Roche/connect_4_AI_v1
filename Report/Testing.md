[Meeting the Brief](README.md) |
[Investigation and Plan](Investigation_&_plan.md) |
[Design](Design.md) |
[Implementation](Implementation.md) |
[Testing](Testing.md) |
[Evaluation](Evaluation.md) |
[References](References.md) |
[Summary word count](Word_count.md)

# Testing
At each phase of the process, I did extensive testing of the parts of the program. Two of the these include the play again function and the user clean data function 

The play again function is to see if the user wants to play again. It will take them back to the main menu if the input is “n” or “N” and it will replay the game type if the input is “y” or “Y”. This was simple to test for and was implemented easily. 

The user clean data function is to validate all inputs other than the inputs into the function play again it will make sure they are integers and are between the values the intended in the program, if not it will keep asking until it gets a valid input. 

The entries into the user clean data and replay function where: 

| No  | Description                                                                         | Test data | Expected result                | Actual result                    | Passed the test |
|---- |-------------------------------------------------------------------------------------|-----------|--------------------------------|----------------------------------|-----------------|
| 1   | Testing inputting a number for play again                                           | 1         | Message saying: Input Invalid  | Message saying: Input Invalid    | Yes             |
| 2   | Testing inputting a yes for play again                                              | y         | Plays the game again           | Plays the game again             | Yes             |
| 3   | Testing a floating-point number for a menu selection                                | 2.5       | Message saying: Input Invalid  | Message saying: Input Invalid    | Yes             |
| 4   | Testing an out-of-range integer for a menu selection expecting a number between 1-5 | 6         | Message saying: Input Invalid  | Message saying: Input Invalid    | Yes             |
| 5   | Testing a valid integer for a menu selection expecting a number between 1-5         | 5         | Option 5 is picked             | Option 5 is picked               | Yes             |
