from manim import *

class StockPriceGraphWithTicks(Scene):
    def construct(self):
        
        axes = Axes(
            x_range=[0, 5, 1],      # x-axis from 0 to 5 with step size of 1
            y_range=[0, 8, 1],      # y-axis from 0 to 8 with step size of 1
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE},
            tips=False              
        )
        
        
        self.add(axes)

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

        prices = [7, 1, 5, 3, 6, 4]
        indices = list(range(len(prices)))

        points = [axes.coords_to_point(x, y) for x, y in zip(indices, prices)]
        
        dots = VGroup(*[Dot(point, color=YELLOW) for point in points])
        
        line_graph = VGroup(*[Line(points[i], points[i + 1], color=BLUE) for i in range(len(points) - 1)])

        self.play(Create(dots), Create(line_graph))

        min_index = prices.index(min(prices))
        max_index = prices.index(max(prices[min_index + 1:]))  # Best selling point after minimum
        buy_dot = Dot(axes.coords_to_point(min_index, prices[min_index]), color=GREEN)
        sell_dot = Dot(axes.coords_to_point(max_index, prices[max_index]), color=RED)
        buy_label = Text("Buy", color=GREEN).next_to(buy_dot, DOWN)
        sell_label = Text("Sell", color=RED).next_to(sell_dot, UP)

        self.play(FadeIn(buy_dot, buy_label), FadeIn(sell_dot, sell_label))

        self.wait(2)
