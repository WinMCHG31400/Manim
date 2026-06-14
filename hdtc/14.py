from manim import *
class Video(Scene):
    def construct(self): 
        dot = Dot(color=BLUE,radius=0.4).shift(RIGHT*5,UP*5)  # 初始位置在右侧
        
        # 创建尾迹轨迹
        traced_path = TracedPath(
            dot.get_center,           # 追踪粒子的位置
            stroke_color=BLUE,        # 尾迹颜色
            stroke_width=12,  # 尾迹粗细
            stroke_opacity=[0, 0.8], # 透明度渐变 [起点, 终点]
            dissipating_time=1.5     # 尾迹消散时间
        )
        line=Line((-10,-2,0),(10,-2,0), color=WHITE)
        self.add(dot,traced_path)
        # 让粒子运动
        self.play(Create(line),run_time=2)
        self.play(dot.animate.shift(LEFT*5,DOWN*7),run_time=3)
        self.play(FadeOut(dot), run_time=1)
        self.play(FadeOut(line), run_time=1)
        self.wait(1.5)