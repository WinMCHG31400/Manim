from manim import *
class Video(Scene):
    def construct(self): 
        cir=Circle(radius=4, color=WHITE, fill_color=WHITE, fill_opacity=0.4)
        cir2=Circle(radius=1, color=BLUE, fill_color=BLUE, fill_opacity=0.6).shift(LEFT*2)
        cir3=Circle(radius=1, color=BLUE, fill_color=BLUE, fill_opacity=0.6).shift(RIGHT*2)
        self.play(
            FadeIn(cir),
            run_time=1.5
        )
        self.play(
            Create(cir2),
            Create(cir3),
            run_time=1.5
        )
        self.wait(2)