from manim import *

class ArrayVisualization(Scene):
    def construct(self):
        elements = [2, 1, 5, 3]
        target = 4
        boxes = []
    
 
        # Create array elements with boxes
        for i, elem in enumerate(elements):
            text = Text(str(elem))
            box = Rectangle(width=text.width + 0.5, height=text.height + 0.5)
            box.set_stroke(color=WHITE)
            text.move_to(box.get_center())
            box_with_text = VGroup(box, text)
            boxes.append(box_with_text)

        # Create a group of all boxes
        array_group = VGroup(*boxes).arrange(RIGHT)
        array_group.move_to(ORIGIN + RIGHT * 3)  # Center the entire array

        # Add the centered array to the scene
        self.add(array_group)

        # Create and center the target label
        target_text = Text(f"target = {target}", font_size = 30)
        target_text.move_to(ORIGIN + UP * 1 + RIGHT * 3)
        self.add(target_text)

        # Initialize pointers
        pointer_i = Text("i", color=BLUE).next_to(array_group[0], DOWN)
        pointer_j = Text("j", color=GREEN).next_to(array_group[1], DOWN)

        pointer_i.shift(RIGHT * 3)
        pointer_j.shift(RIGHT * 3)
        
        self.add(pointer_i)
        self.add(pointer_j)

        # Create a text box for the sum
        sum_text = Text("", font_size=30)
        sum_text.next_to(array_group, DOWN * 6)  # Position it further below the array
        sum_text.shift(RIGHT * 3)
        self.add(sum_text)

        self.wait(1)

        # Iterate over the array to find the target
        for i in range(len(elements) - 1):
            for j in range(i + 1, len(elements)):
                # Show pointers moving
                self.play(pointer_i.animate.next_to(array_group[i], DOWN))
                self.play(pointer_j.animate.next_to(array_group[j], DOWN))
                self.wait(0.5)

                # Calculate the sum and create a new text for it
                current_sum = elements[i] + elements[j]
                new_sum_text = Text(f"{elements[i]} + {elements[j]} = {current_sum}", font_size=24)
                new_sum_text.next_to(array_group, DOWN * 5)  # Position it further below the array

                # Transform the old sum_text to the new one
                self.play(Transform(sum_text, new_sum_text))
                self.wait(1)

                # Check if the sum matches the target
                if current_sum == target:
                    # Highlight the matched elements
                    self.play(
                        array_group[i].animate.set_stroke(YELLOW, 4),
                        array_group[j].animate.set_stroke(YELLOW, 4)
                    )
                    self.wait(5)
                    break  # Exit loop if match found

        self.wait(2)  # Wait to display everything at the end
