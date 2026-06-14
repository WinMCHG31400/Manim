from manim import *
class Video(Scene):
    def construct(self): 
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 10, 1],
            x_length=8,
            y_length=6,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "include_tip": True,
            }
        )
        
        x_label = axes.get_x_axis_label(
            MathTex("t_1")
        )
        
        y_label = axes.get_y_axis_label(
            MathTex("t_2")
        )
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=2
        )
        self.wait(2)