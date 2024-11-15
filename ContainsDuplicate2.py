from manim import *


class ContainsDuplicate2(Scene):
    def construct(self):
        elements = [1, 2, 3, 1]
        boxes = []

        # Create the main hash map box
        hash_box = Rectangle(width=3, height=2, color=WHITE)
        hash_box.move_to(ORIGIN + DOWN * 1)

        # Create the dividing line in the center
        divider = Line(
            start=hash_box.get_top(),
            end=hash_box.get_bottom(),
            color=WHITE
        ).move_to(hash_box.get_center())

        # Move labels "Key" and "Value" to the top of the hash map box
        key_label = Text("Value", font_size=24).next_to(hash_box, UP).shift(RIGHT * 0.7)
        value_label = Text("Index", font_size=24).next_to(hash_box, UP).shift(LEFT * 0.6)

        # Group everything for the hash map
        hash_map_group = VGroup(hash_box, divider, key_label, value_label)

        # Add the hash map to the scene
        self.add(hash_map_group)

        # Create array elements with boxes
        for i, elem in enumerate(elements):
            text = Text(str(elem), font_size=24)
            box = Rectangle(width=text.width + 1, height=text.height + 1, color=WHITE)
            text.move_to(box.get_center())
            box_with_text = VGroup(box, text)
            boxes.append(box_with_text)

        # Arrange the array horizontally and position it above the hash map
        array_group = VGroup(*boxes).arrange(RIGHT, buff=0.1)
        array_group.move_to(ORIGIN + UP * 2)

        # Add the array group to the scene
        self.add(array_group)

        # Simulate the hash map
        hash_map = {}
        hash_map_visuals = VGroup()

        # Process each element in the array
        for i, elem in enumerate(elements):
            # Highlight the current element
            self.play(boxes[i].animate.set_color(YELLOW), run_time=0.5)

            if elem in hash_map:
                # Highlight all previous occurrences of this element as yellow
                for idx in hash_map[elem]:
                    self.play(boxes[idx].animate.set_color(YELLOW), run_time=0.5)

                # Optionally, display a message for the duplicate
                # duplicate_text = Text(f"Duplicate found: {elem}", font_size=24, color=RED)
                # duplicate_text.move_to(ORIGIN + DOWN * 3)
                # self.play(FadeIn(duplicate_text), run_time=1)
                # self.wait(1)
                # self.play(FadeOut(duplicate_text))
                break
            else:
                # Add the element to the hash map with its index as a list
                if elem not in hash_map:
                    hash_map[elem] = []
                hash_map[elem].append(i)

                # Create text labels for keys and values (no boxes around values)
                key_text = Text(str(i), font_size=22)  # Index will be shown here
                value_text = Text(str(elem), font_size=22)  # Value will be shown here

                # Adjust vertical position of text to move it upwards
                vertical_offset = len(hash_map) * 0.5  # Adjust for the number of entries

                # Move the key and value texts starting from the origin
                key_text.move_to(ORIGIN + LEFT * .7 + DOWN * (vertical_offset))
                value_text.move_to(ORIGIN + RIGHT * .8 + DOWN * (vertical_offset))

                # Add the key and value text labels to the hash map visuals
                entry = VGroup(key_text, value_text)
                hash_map_visuals.add(entry)

                # Add the new entry to the scene
                self.play(FadeIn(entry), run_time=0.5)

            # Reset color of the element
            self.play(boxes[i].animate.set_color(WHITE), run_time=0.2)

        # Wait at the end to display final hash map
        self.wait(2)
