from manim import *

class HashVisualization(Scene):
    def construct(self):
        elements = [2, 1, 5, 3]
        target = 4
        boxes = []
        
        # HASH MAP START
        # Create the main hash map box
        hash_box = Rectangle(width=2.5, height=2, color=WHITE)
        hash_box.move_to(ORIGIN + RIGHT * 3 + DOWN * 2)

        # Create the dividing line in the center
        divider = Line(
            start=hash_box.get_top(),
            end=hash_box.get_bottom(),
            color=WHITE
        ).move_to(hash_box.get_center())

        # Create labels for each half of the hash map box
        key_text = Text("Key", font_size=24).move_to(hash_box.get_left() + RIGHT * 0.75)
        value_text = Text("Value", font_size=24).move_to(hash_box.get_right() + LEFT * 0.75)

        # Group everything for the hash map
        hash_map_group = VGroup(hash_box, divider, key_text, value_text)
        
        # Add the hash map to the scene
        self.add(hash_map_group)
        # HASH MAP END
        
        # Create array elements with boxes
        for i, elem in enumerate(elements):
            text = Text(str(elem), font_size=24)
            box = Rectangle(width=text.width + 1, height=text.height + 1, color=WHITE)
            text.move_to(box.get_center())
            box_with_text = VGroup(box, text)
            boxes.append(box_with_text)

        # Arrange the array horizontally and position it above the hash map
        array_group = VGroup(*boxes).arrange(RIGHT, buff=0.1)
        array_group.move_to(ORIGIN + RIGHT * 3 + UP * 1)

        # Add the array group to the scene
        self.add(array_group)

        # Create and center the target label above the array
        target_text = Text(f"target = {target}", font_size=30)
        target_text.next_to(array_group, UP * 1.75)
        self.add(target_text)

        # Final pause to view everything in the scene
        self.wait(2)
