from manim import *
class Video(Scene):
    def construct(self): 
        dot1 = Dot(color=RED) # 初始位置在右侧
        circle1=Circle(radius=1,color=WHITE)
        self.play(
            Create(dot1),
            Create(circle1),
            run_time=0.5
        )
        dot2= Dot(color=RED).shift(UP*2,RIGHT*2)
        circle2=Circle(radius=1,color=WHITE).shift(UP*2,RIGHT*2)
        self.play(
            Create(dot2),
            Create(circle2),
            run_time=0.5
        )
        dot3= Dot(color=RED).shift(DOWN*3,RIGHT*1)
        cicle3=Circle(radius=1,color=WHITE).shift(DOWN*3,RIGHT*1)
        self.play(
            Create(dot3),
            Create(cicle3),
            run_time=0.5
        )
        dot4= Dot(color=RED).shift(UP*3,LEFT*2)
        circle4=Circle(radius=1,color=WHITE).shift(UP*3,LEFT*2)
        self.play(
            Create(dot4),
            Create(circle4),
            run_time=0.5
        )
        dot5= Dot(color=RED).shift(DOWN*2,LEFT*3)
        circle5=Circle(radius=1,color=WHITE).shift(DOWN*2,LEFT*3)
        self.play(
            Create(dot5),
            Create(circle5),
            run_time=0.5
        )
        self.wait(2)
        