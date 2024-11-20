from manim import *

class Threesum1(Scene):
    def construct(self):
        
        elements = [-1,0,1,2,-1,-4]
        elementsText = Text(f"{elements}", font_size = 40)
        elementsText.move_to(UP * 1.5)
        self.add(elementsText)
        
        box1 = Square(side_length=1, color=BLUE).shift(LEFT * 2)
        box2 = Square(side_length=1, color=BLUE)
        box3 = Square(side_length=1, color=BLUE).shift(RIGHT * 2)
        
        # Add placeholders ("a", "b", "c") under the boxes
        text1 = Text("a", color = GREEN).next_to(box1, DOWN * 1.4)
        text2 = Text("b", color = GREEN).next_to(box2, DOWN)
        text3 = Text("c", color = GREEN).next_to(box3, DOWN * 1.4)
        
        # Create the equation symbols
        plus1 = Text("+").next_to(box1, RIGHT)
        plus2 = Text("+").next_to(box2, RIGHT)
        equals = Text("= 0").next_to(box3, RIGHT)
        
        # Add everything to the scene
        self.play(Create(box1), Create(box2), Create(box3))
        self.play(Write(text1), Write(text2), Write(text3))
        self.play(Write(plus1), Write(plus2), Write(equals))
        
        # Keep the final result on screen
        self.wait(2)