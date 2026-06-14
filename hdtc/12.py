from manim import *
class Video(Scene):
    def construct(self): 
        dot = Dot(color=BLUE)
        block=Square(side_length=3, color=WHITE)
        block.rotate(PI/2)
        self.play(Create(dot),
                  Create(block),
                  run_time=1)
        line1=Line((-2.5,-2.5,0),(2.5,2.5,0), color=RED)
        line2=Line((-2.5,2.5,0),(2.5,-2.5,0), color=RED)
        self.play(
            Create(line1),
            Create(line2),
            run_time=1.5
        )
        self.wait(2)
        