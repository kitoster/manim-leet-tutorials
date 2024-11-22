from manim import *

class Threesum3(Scene):
    def construct(self):
        
        # Define arrays as Text objects
        elements = [-1,0,1,2,-1,-4]
        elementsText = Text(f"{elements}", font_size = 46, color=GREEN)
        elementsText.move_to(UP * 3)
        self.add(elementsText)
        
        ptext = Text("positives = {1, 2}", font_size = 30)
        ptext.move_to(UP * 2)
        self.add(ptext)
        
        ntext = Text("negatives = {-1, -4}", font_size = 30)
        ntext.move_to (UP * 1.6)
        self.add(ntext)
        
        ztext = Text("zeroes = {0}", font_size = 30)
        ztext.move_to (UP * 1.2)
        self.add(ztext)
        
        box1 = Square(side_length=1, color=BLUE).shift(LEFT * 2)
        box2 = Square(side_length=1, color=BLUE)
        box3 = Square(side_length=1, color=BLUE).shift(RIGHT * 2)
        self.add(box1, box2, box3)
        
        text1 = Text("-num", font_size = 30, color = GREEN).next_to(box1, DOWN * 1.4)
        text2 = Text("0", font_size = 30, color = GREEN).next_to(box2, DOWN)
        text3 = Text("num", font_size = 30, color = GREEN).next_to(box3, DOWN * 1.4)
        self.add(text1, text2, text3)
        
        plus1 = Text("+").next_to(box1, RIGHT)
        plus2 = Text("+").next_to(box2, RIGHT)
        equals = Text("= 0").next_to(box3, RIGHT)
        self.add(plus1, plus2, equals)
        
        num1 = Text("-1", font_size=30, color=WHITE).move_to(box1.get_center())
        num2 = Text("0", font_size=30, color=WHITE).move_to(box2.get_center())
        num3 = Text("1", font_size=30, color=WHITE).move_to(box3.get_center())
        
        self.play(FadeIn(num1), FadeIn(num2), FadeIn(num3))
        
        self.wait(2)