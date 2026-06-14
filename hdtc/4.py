from manim import *
class Video(Scene):
    def construct(self): 
        c1=Circle(radius=3, color="#4f6f8f", stroke_width=6)
        c2=Circle(radius=3, color="#4f6f8f", stroke_width=6,fill_color="#4f6f8f",fill_opacity=1)
        self.play(
            Create(c1, run_time=2, rate_func=linear)
        )
        self.play(
            FadeOut(c1, run_time=1.5, rate_func=linear),
            FadeIn(c2, run_time=1.5, rate_func=linear)
        )
        self.wait(0.5)
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 10, 1],
            x_length=8,
            y_length=6,
            axis_config={
                "color": WHITE,
                "include_tip": True,
            }
        )
        
        # 添加标签
        x_label = axes.get_x_axis_label("y")
        y_label = axes.get_y_axis_label("x")
        self.play(
            c2.animate.shift(UP*2, RIGHT*2).scale(0.4),
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=3
        )
        self.wait(2)
        