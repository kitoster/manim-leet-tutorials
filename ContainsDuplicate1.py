from manim import *

class ContainsDuplicate1(Scene):
    def construct(self):
        # Define the example array and the sorted array
        example_array = [1, 2, 3, 1]
        sorted_array = sorted(example_array)  # This uses Python's built-in sort

        # Create the original array visual
        #original_text = Text("Original Array:", font_size=24).move_to(UP * 2)
        original_dots = VGroup(*[Text(str(num), font_size=50).move_to(i * RIGHT) for i, num in enumerate(example_array)])
        
        # Create the sorted array visual
        #sorted_text = Text("Sorted Array:", font_size=24).move_to(DOWN * 1.5)
        sorted_dots = VGroup(*[Text(str(num), font_size=50).move_to(i * RIGHT) for i, num in enumerate(sorted_array)])
        
        # Position the sorted array below the original array
        sorted_dots.shift(DOWN * 1)

        # Add the title and original array to the scene
        self.play(FadeIn(original_dots))

        # Pause briefly, then transition to showing the sorted array
        self.wait(1)
        self.play(FadeIn(sorted_dots))

        # Optionally highlight duplicates in the sorted array
        duplicate_indices = [i for i in range(1, len(sorted_array)) if sorted_array[i] == sorted_array[i - 1]]
        for index in duplicate_indices:
            self.play(sorted_dots[index - 1].animate.set_color(YELLOW), sorted_dots[index].animate.set_color(YELLOW))
        
        self.wait(2)