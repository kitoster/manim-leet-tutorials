from manim import *

class ArrayVisualization(Scene):
    def construct(self):
        elements = [2, 1, 5, 3]
        target = 4
        boxes = []
        
        code_lines = [
            "for i in range(len(nums) - 1):",
            "    for j in range(i + 1, len(nums)): ",
            "        if nums[i] + nums[j] == target:",
            "            return [i, j]",
            "    return []"
        ]

        # Create a group for all the code lines
        code_text = VGroup()
        for line in code_lines:
            code_line = Text(line, font_size=22, line_spacing=0.5)  # Add line spacing for better readability
            code_text.add(code_line)

        # Arrange the code text vertically
        code_text.arrange(DOWN, buff=0.1)

        # Create a rectangle for the background
        code_box = Rectangle(
            width=6,  # Adjust the width as necessary
            height=2 * len(code_lines),  # Height based on number of lines
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=2
        )
        code_box.move_to(LEFT * 4)  # Position it on the left side of the screen

        # Move the text block into position inside the rectangle
        code_text.move_to(code_box.get_center())

        # Add the rectangle and the code text to the scene
        self.add(code_box, code_text)

        self.wait(2)  # Pause for a moment to see the code block

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
        target_text = Text(f"target = {target}")
        target_text.move_to(ORIGIN + UP * 2 + RIGHT * 3)
        self.add(target_text)

        # Initialize pointers
        pointer_i = Text("i", color=BLUE).next_to(array_group[0], DOWN)
        pointer_j = Text("j", color=GREEN).next_to(array_group[1], DOWN)

        pointer_i.shift(RIGHT * 3)
        pointer_j.shift(RIGHT * 3)
        
        self.add(pointer_i)
        self.add(pointer_j)

        # Create a text box for the sum
        sum_text = Text("", font_size=28)
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
                    self.wait(1)
                    break  # Exit loop if match found

        self.wait(2)  # Wait to display everything at the end
