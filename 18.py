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
                "include_tip": True,
            }
        )
        
        # 添加标签
        x_label = axes.get_x_axis_label("y")
        y_label = axes.get_y_axis_label("x")
        c2=Circle(radius=3, color="#4f6f8f", stroke_width=6,fill_color="#4f6f8f",fill_opacity=1).shift(UP*2, RIGHT*2).scale(0.4)
        self.play(
            FadeIn(c2),FadeIn(axes),FadeIn(x_label),FadeIn(y_label), run_time=1.5)
        self.play(
            Uncreate(axes),
            Uncreate(x_label),
            Uncreate(y_label),
            Uncreate(c2),
            run_time=5
        )
        self.wait(2.5)
        