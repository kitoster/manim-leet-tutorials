from manim import *


class LogoAnimation(Scene):
    def construct(self):

        circle = Circle(radius=3, color=BLUE, stroke_width=8)
        
        number_1 = Text("1", font_size=300, color=GRAY).move_to(circle.get_center())
        
        self.play(Create(circle), FadeIn(number_1, scale=0.5))
        
        self.play(
            circle.animate.set_color(WHITE),  # Make the circle glow white
            run_time=0.5
        )

        self.play(
            circle.animate.set_color(BLUE),  
            run_time=0.5
        )
        
        self.wait(2)
