from manim import *

class BuySellStock (Scene):
    def construct(self):
        
        # Display the prices array as text at the top of the screen
        prices_text = Text("prices = [7, 1, 5, 3, 6, 4]", font_size=24)
        prices_text.shift(ORIGIN + LEFT * 0.5)
        self.add(prices_text)     # Add the text to the scene
         
        # Create axes with proper configuration
        axes = Axes(
            x_range=[0, 5, 1],      # x-axis from 0 to 5 with step size of 1
            y_range=[0, 8, 1],      # y-axis from 0 to 8 with step size of 1
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE},
            tips=False              # Turn off arrow tips for cleaner look
        )
        
        # Add the axes to the scene first to ensure visibility
        self.add(axes)
        
        # Example stock prices to plot
        prices = [7, 1, 5, 3, 6, 4]
        indices = list(range(len(prices)))
        
        arrayText = Text("prices = [7, 1, 5, 3, 6, 4]", font_size=30)
        self.add(arrayText)

        # Labels for the axes without using LaTeX
        x_label = Text("Index", font_size=24).next_to(axes.x_axis, DOWN)
        y_label = Text("Price", font_size=24).next_to(axes.y_axis, LEFT)
        self.add(x_label, y_label)

        # Manually add tick labels along the x-axis and y-axis
        for i in range(6):  # x-axis ticks
            tick_label = Text(str(i), font_size=18).next_to(axes.x_axis.n2p(i), DOWN)
            self.add(tick_label)

        for j in range(9):  # y-axis ticks
            tick_label = Text(str(j), font_size=18).next_to(axes.y_axis.n2p(j), LEFT)
            self.add(tick_label)

        # Convert data points to coordinate points on the axes
        points = [axes.coords_to_point(x, y) for x, y in zip(indices, prices)]
        
        # Create dots for each data point
        dots = VGroup(*[Dot(point, color=YELLOW) for point in points])
        
        # Create line segments between the points
        line_graph = VGroup(*[Line(points[i], points[i + 1], color=BLUE) for i in range(len(points) - 1)])

        # Animate the dots and line segments
        self.play(Create(dots), Create(line_graph))

        # Optional: Add markers for buy/sell points
        min_index = prices.index(min(prices))
        max_index = prices.index(max(prices[min_index + 1:]))  # Best selling point after minimum
        buy_dot = Dot(axes.coords_to_point(min_index, prices[min_index]), color=GREEN)
        sell_dot = Dot(axes.coords_to_point(max_index, prices[max_index]), color=RED)
        buy_label = Text("Buy", color=GREEN).next_to(buy_dot, DOWN)
        sell_label = Text("Sell", color=RED).next_to(sell_dot, UP)

        # Animate the buy/sell points
        self.play(FadeIn(buy_dot, buy_label), FadeIn(sell_dot, sell_label))

        # Hold final view
        self.wait(2)
