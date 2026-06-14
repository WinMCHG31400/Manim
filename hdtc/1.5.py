from manim import *
class Video(Scene):
    def construct(self): 
        ba = Dot(radius=0.1, color="#aad0f0")
        cycle = Circle(radius=3, color="#4f6f8f", stroke_width=4)
        self.play(
            FadeIn(ba, run_time=0.8, rate_func=linear),  # 0.8秒完成
            Create(cycle, run_time=4, rate_func=smooth), )# 4秒完成
        
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
        
        # 添加标签
        x_label = axes.get_x_axis_label("t")
        y_label = axes.get_y_axis_label("x(t)")
        self.play(
            cycle.animate.shift(UP*2, RIGHT*2).scale(0.4),
            ba.animate.shift(UP*2, RIGHT*2).scale(0.4),
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=2
        )
        
        self.wait(0.5)
        self.play(
            ba.animate.shift(LEFT*2),
            run_time=2
        )
        self.wait(0.5)
        self.play(FadeOut(ba), FadeOut(cycle),FadeOut(axes),FadeOut(x_label),FadeOut(y_label), run_time=1.5)
        self.wait(0.5)