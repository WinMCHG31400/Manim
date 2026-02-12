from manim import *
class Video(Scene):
    def construct(self): 
        dot = Dot(color=BLUE)
        # 创建尾迹轨迹
        traced_path = TracedPath(
            dot.get_center,           # 追踪粒子的位置
            stroke_color=BLUE,        # 尾迹颜色
            stroke_width=8,          # 尾迹粗细
            stroke_opacity=[0, 0.8], # 透明度渐变 [起点, 终点]
            dissipating_time=1.5     # 尾迹消散时间
        )
        block=Square(side_length=5, color=WHITE)
        line1=Line((-2.5,-2.5,0),(2.5,2.5,0), color=RED)
        line2=Line((-2.5,2.5,0),(2.5,-2.5,0), color=RED)
        block.rotate(PI/2)
        self.play(
            AnimationGroup(
                Create(dot),
                Create(traced_path),
                run_time=0.5
            ),
            AnimationGroup(
                FadeIn(block),
                run_time=1.5
            ),
            AnimationGroup(
                FadeIn(line1),
                FadeIn(line2),
                run_time=1.5
            )
        )
        block.rotate(-PI/2)
        self.wait(1.5)
        self.play(
            AnimationGroup(
                Uncreate(line1),
                Uncreate(line2),
                Uncreate(block),
                run_time=1.5
            ),
            AnimationGroup(
                dot.animate.shift(RIGHT*4),
                run_time=2
            )
        )
        self.wait(2)
        self.play(FadeOut(dot), run_time=1)
        