from manim import *
class Video(Scene):
    def construct(self): 
        cir=Circle(radius=2.5, color=BLUE, fill_color=BLUE, fill_opacity=0.4)
        line1=Line((-2.5,-2.5,0),(2.5,2.5,0), color=RED)
        line2=Line((-2.5,2.5,0),(2.5,-2.5,0), color=RED)
        self.play(
            Create(cir),
            Create(line1),
            Create(line2),
            run_time=1.5
        )
        self.wait(2)
        