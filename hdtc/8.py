from manim import *
class Video(Scene):
    def construct(self): 
        #line1=Line((-10,0,0),(10,0,0), color=BLUE)
        rect1=Rectangle(width=20, height=8, color=BLUE,fill_color=BLUE,fill_opacity=0.4).shift(DOWN*4)
        dot1=Dot(color=WHITE).shift(DOWN*2,LEFT*2)  # 初始位置在右侧
        self.play(
            Create(rect1),
            Create(dot1),
            run_time=1.5
        )
        self.play(
            dot1.animate.shift(UP*4,RIGHT*2),
            run_time=2
        )
        self.wait(0.5)