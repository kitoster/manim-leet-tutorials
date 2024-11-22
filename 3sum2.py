from manim import *

class Threesum2(Scene):
    def construct(self):
        
        # Define arrays as Text objects
        elements = [-1,0,1,2,-1,-4]
        elementsText = Text(f"{elements}", font_size = 46, color=GREEN)
        
        nlist = Text("n = [-1, -1, 4]", font_size=42)
        plist = Text("p = [1, 2]", font_size=42)
        zlist = Text("z = [0]", font_size=42)

        # Align each array to the left
        nlist.to_edge(LEFT).shift(UP * 1.2)  # Top-left
        plist.to_edge(LEFT)                  # Center-left
        zlist.to_edge(LEFT).shift(DOWN * 1.2)  # Bottom-left
        elementsText.to_edge(LEFT).shift(UP * 2.4)
        
        self.add(elementsText)

        # Add a fade-in animation for each array
        self.play(FadeIn(nlist))
        self.wait(0.5)  # Pause briefly
        self.play(FadeIn(plist))
        self.wait(0.5)  # Pause briefly
        self.play(FadeIn(zlist))

        # Keep the scene displayed
        self.wait(2)