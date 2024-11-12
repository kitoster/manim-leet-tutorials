from manim import *

class BuySellStock2(Scene):
    def construct(self):
        
        # Stock prices array
        prices = [7, 1, 5, 3, 6, 4]
        
        # Display the prices array as text at the top of the screen
        prices_text = Text("prices = [7, 1, 5, 3, 6, 4]", font_size=36)
        prices_text.move_to(ORIGIN + UP * 2)
        self.add(prices_text)
        
        # Display the max profit value, initially set to 0
        max_profit = 0
        maxP_text = Text(f"maxProfit = {max_profit}", font_size=28)
        maxP_text.next_to(prices_text, DOWN)
        self.add(maxP_text)

        # Create axes for the graph
        axes = Axes(
            x_range=[0, len(prices) - 1, 1],
            y_range=[0, max(prices) + 1, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE},
            tips=False
        )
        axes.to_edge(DOWN)
        self.add(axes)
        
        # Add labels for axes
        x_label = Text("Index", font_size=24).next_to(axes.x_axis, DOWN)
        y_label = Text("Price", font_size=24).next_to(axes.y_axis, LEFT * 1.5)
        self.add(x_label, y_label)

        # Manual tick labels for the x-axis and y-axis
        for i, price in enumerate(prices):
            tick_label_x = Text(str(i), font_size=18).next_to(axes.x_axis.n2p(i), DOWN)
            tick_label_y = Text(str(price), font_size=18).next_to(axes.y_axis.n2p(price), LEFT)
            self.add(tick_label_x, tick_label_y)
        
        # Create points and connect them with lines
        points = [axes.coords_to_point(i, price) for i, price in enumerate(prices)]
        dots = VGroup(*[Dot(point, color=YELLOW) for point in points])
        lines = VGroup(*[Line(points[i], points[i + 1], color=BLUE) for i in range(len(points) - 1)])
        self.play(Create(dots), Create(lines))

        # Initialize l and r pointers
        l, r = 0, 1

        # Iterate through the prices array
        while r < len(prices):
            # Create circles for left and right pointers
            left_circle = Circle(radius=0.3, color=BLUE).move_to(points[l])
            right_circle = Circle(radius=0.3, color=GREEN).move_to(points[r])
            
            # Animate the appearance of the left and right circles
            self.play(Create(left_circle), Create(right_circle))

            # Check if the trade is profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                
                # Flash circles yellow if the trade is profitable
                flash_left_circle = left_circle.copy().set_color(YELLOW)
                flash_right_circle = right_circle.copy().set_color(YELLOW)
                self.play(Transform(left_circle, flash_left_circle), Transform(right_circle, flash_right_circle))
                
                # Update max profit if higher and display it
                if profit > max_profit:
                    max_profit = profit
                    new_maxP_text = Text(f"maxProfit = {max_profit}", font_size=28)
                    new_maxP_text.next_to(prices_text, DOWN)
                    self.play(Transform(maxP_text, new_maxP_text))
                    maxP_text = new_maxP_text  # Update reference for future transforms

            else:
                # Move left pointer (l) to right pointer (r) if trade is not profitable
                l = r
            
            # Advance the right pointer (r) for the next comparison
            r += 1

            # Remove previous circles to prepare for the next pair
            self.play(FadeOut(left_circle), FadeOut(right_circle))
            self.wait(0.5)  # Pause between each iteration for clarity

        # Hold the final view
        self.wait(2)
