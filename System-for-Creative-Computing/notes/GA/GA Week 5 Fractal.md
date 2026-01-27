This week we're exploring a technique called recursion, where a function calls itself. When a function calls itself (recursion), this often means similar things happen at different scales. This 'self-similarity' is a key feature of fractals. Throughout the session we will be looking at core principles relating to recursion and studying the design of various famous fractal patterns.  Look at this [photograph](https://media.giphy.com/media/RHPxe7KPnb8KaAtBbE/giphy.gif)

[What are Fractals?](https://moodle.port.ac.uk/mod/url/view.php?id=191062)

### PRACTICES



![[Pasted image 20251107104532 1.png]]
*%% making Fractals tree %%*



### USEFUL CODE

Some code that might be useful. More extensive details and examples in the P5JS reference.

| Code                                                      | Example                                                                                                   | Definition                                                                                                                                         | Help Link                                            |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| line(x1, y1, x2, y2)                                      | line (50, 50, 100, 100);                                                                                  | Draws a line, 4 values needed, xy start and xy end                                                                                                 | [Link](https://p5js.org/reference/#/p5/line)         |
| stroke (r, g, b, alpha optional);                         | stroke (255, 0, 0);                                                                                       | Set the colour for lines<br><br>(google colour picker for help)                                                                                    | [Link](https://p5js.org/reference/#/p5/fill)         |
| strokeWeight(value)                                       | strokeWeight(10);                                                                                         | Sets stroke weight e.g. pen thickness.                                                                                                             | [Link](https://p5js.org/reference/#/p5/strokeweight) |
| Function name(){<br><br>Thing to do<br><br>}              | Function doThisThing() {<br><br>Print(“I am doing it”);<br><br>}                                          | Define functions that can be called.                                                                                                               |                                                      |
| random(n)                                                 | Random(-3,3);                                                                                             | Generates a random number as a floating point number.                                                                                              | [Link](https://p5js.org/reference/#/p5/random)       |
| curve(x1, y1, x2, y2, x3, y3, x4, y4)                     | curve(5, 26, 5, 26, 73, 24, 73, 61);                                                                      | Draw a curve, using 4 x/y points. xy 1&4 are control points for the curve. xy 2&3 are start and end points for the curve                           | [Link](https://p5js.org/reference/#/p5/curve)        |
| function mousePressed(){<br><br>Code to execute }         | function mousePressed(){<br><br>Print(“you clicked!”); }                                                  | Executes code in {} when mouse clicks on canvas                                                                                                    | [Link](https://p5js.org/reference/#/p5/mousepressed) |
| push()                                                    | push();                                                                                                   | The push() function saves the current drawing settings, pop() restores the original settings. push() and pop() functions are always used together. | [Link](https://p5js.org/reference/#/p5/push)         |
| pop()                                                     | pop();                                                                                                    | [Link](https://p5js.org/reference/#/p5/pop)                                                                                                        |                                                      |
| translate(x, y);                                          | translate(20,20);                                                                                         | Specifies an amount to displace objects within the display window I.e. move our 0,0 point.                                                         | [Link](https://p5js.org/reference/#/p5/translate)    |
| rotate(angle);                                            | rotate(PI / 4);                                                                                           | Rotates a shape by the amount specified by the angle parameter.                                                                                    | [Link](https://p5js.org/reference/#/p5/rotate)       |
| function keyPressed () {<br><br>body of function<br><br>} | function keyPressed () {<br><br>   if (keyCode == ENTER) {<br><br>     saveCanvas ("screen-####.jpg");} } | The keyPressed() function is called once every time a key is pressed.<br><br>Example saves canvas as image.                                        | [Link](https://p5js.org/reference/#/p5/keyPressed)   |


![[Pasted image 20251107120007.png]]