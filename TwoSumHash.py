from manim import *

class HashVisualization(Scene):
    def construct(self):
        elements = [2, 1, 5, 3]
        target = 4
        boxes = []
        
        # HASH MAP START
        box = Rectangle(width=2.5, height=2, color=WHITE)
        box.move_to(ORIGIN + RIGHT * 3 + DOWN * 2)  # Center the entire array

        # Create the dividing line
        divider = Line(
            start=box.get_top(),
            end=box.get_bottom(),
            color=WHITE
        )

        # Position the divider at the center of the box
        divider.move_to(box.get_center())

        # Group the box and the divider for hash map
        split_box = VGroup(box, divider)

        # Add the split box to the scene
        self.add(split_box)
        # HASH MAP END
        
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
        array_group.move_to(ORIGIN + RIGHT * 3 + UP * 1)  # Center the entire array

        # Add the centered array to the scene
        self.add(array_group)

        # Create and center the target label
        target_text = Text(f"target = {target}", font_size = 30)
        target_text.move_to(ORIGIN + UP * 2 + RIGHT * 3)
        self.add(target_text)   