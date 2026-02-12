from manim import *
class Video(Scene):
    def construct(self): 
        dot = Dot(color=BLUE).shift(UP*2)  # 初始位置在上方
        # 创建尾迹轨迹
        traced_path = TracedPath(
            dot.get_center,           # 追踪粒子的位置
            stroke_color=BLUE,        # 尾迹颜色
            stroke_width=8,          # 尾迹粗细
            stroke_opacity=[0, 0.8], # 透明度渐变 [起点, 终点]
            dissipating_time=1.5     # 尾迹消散时间
        )
        rect=Rectangle(width=20, height=10, color=WHITE, fill_color=WHITE, fill_opacity=0.4).shift(DOWN*4)
        rect1=Rectangle(width=10, height=10, color=WHITE, fill_color=WHITE, fill_opacity=0.4).shift(DOWN*4,LEFT*5)
        rect2=Rectangle(width=10, height=10, color=WHITE, fill_color=WHITE, fill_opacity=0.4).shift(DOWN*4,RIGHT*5)
        #rects=VGroup(rect1,rect2)
        
        self.play(AnimationGroup(
                FadeIn(dot),
                FadeIn(traced_path),
                run_time=0.5
            ),
            AnimationGroup(
                FadeIn(rect),
                run_time=1.5
            )
        )
        self.remove(rect)
        self.add(rect1, rect2)
        self.play(AnimationGroup(
                rect1.animate.shift(LEFT*5),
                rect2.animate.shift(RIGHT*5),
                run_time=1
            ),
            AnimationGroup(
                dot.animate.shift(DOWN*8),
                run_time=1
            )
        )
        self.wait(2)
        self.play(FadeOut(dot),FadeOut(rect1),FadeOut(rect2), run_time=1)
        