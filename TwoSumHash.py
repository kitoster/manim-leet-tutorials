from manim import *

class HashVisualization(Scene):
    def construct(self):
        elements = [2, 1, 5, 3]
        target = 4
        boxes = []
        
        # Create the main hash map box
        hash_box = Rectangle(width=2.5, height=2, color=WHITE)
        hash_box.move_to(ORIGIN + RIGHT * 3 + DOWN * 2)

        # Create the dividing line in the center
        divider = Line(
            start=hash_box.get_top(),
            end=hash_box.get_bottom(),
            color=WHITE
        ).move_to(hash_box.get_center())

        # Move labels "Key" and "Value" to the top of the hash map box
        key_label = Text("Value  ", font_size=24).next_to(hash_box, UP).align_to(hash_box, LEFT).shift(RIGHT * 0.4)
        value_label = Text("  Index", font_size=24).next_to(hash_box, UP).align_to(hash_box, RIGHT).shift(LEFT * 0.6)

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
        array_group.move_to(ORIGIN + RIGHT * 3 + UP * 1)

        # Add the array group to the scene
        self.add(array_group)

        # Create and center the target label above the array
        target_text = Text(f"target = {target}", font_size=30)
        target_text.next_to(array_group, UP * 1.75)
        self.add(target_text)

        # Initialize an empty hash map to track key-value pairs visually
        prev_map = {}  # Dictionary for code logic
        hash_map_entries = []  # Store displayed entries

        # Placeholder for displaying the difference (diff)
        diff_text = Text("", font_size=24, color=YELLOW).next_to(target_text, UP)
        self.add(diff_text)

        # Iterate over the elements and implement the Two Sum solution
        for i, n in enumerate(elements):
            # Highlight the current element
            self.wait(2)
            self.play(boxes[i].animate.set_fill(YELLOW, opacity=0.2))

            # Calculate the difference needed to meet the target
            diff = target - n

            # Update and display the diff value
            diff_text.become(Text(f"diff = {target} - {n} = {diff}", font_size=24, color=BLUE).next_to(target_text, UP))

            # Check if diff is in the hash map (previous elements)
            if diff in prev_map:
                # If found, highlight both matching elements
                matching_index = prev_map[diff]
                self.play(
                    boxes[matching_index].animate.set_fill(GREEN, opacity=0.2),
                    boxes[i].animate.set_fill(GREEN, opacity=0.2)
                )
                
                # Display result as found pair
                result_text = Text(f"Found: [{matching_index}, {i}]", font_size=24, color=GREEN)
                result_text.next_to(target_text, DOWN * 2 + LEFT * 3)
                self.add(result_text)
                self.wait(2)
                break  # Stop the loop after finding the result

            # If diff is not found, add n and its index to prev_map and visualize
            prev_map[n] = i
            key_entry = Text(str(n), font_size=18).move_to(hash_box.get_left() + RIGHT * 0.5 + UP * (0.4 - 0.5 * len(hash_map_entries)))
            value_entry = Text(str(i), font_size=18).move_to(hash_box.get_right() + LEFT * 0.5 + UP * (0.4 - 0.5 * len(hash_map_entries)))
            hash_map_entries.append(VGroup(key_entry, value_entry))

            # Add the entries to the scene inside the hash map box
            self.add(key_entry, value_entry)

        # Final wait to view the scene
        self.wait(2)
