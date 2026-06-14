from manim import *
# manim "C:\manim_projects\1.py" -p

class Video(Scene):
    def construct(self):
        π=PI
        horse_curve = ParametricFunction(
            lambda t: np.array([
                np.cos(2*t) + 0.4 * np.cos(4*t) + 2/9 * np.cos(6*t),
                20/3 * np.sin(t) -2/3 * np.cos(3*t) + 2/7 * np.sin(5*t),
                0
            ]),
            t_range=[0, 2*PI],
            color=RED,
            stroke_width=4
        ).scale(0.8).shift(LEFT * 3 + DOWN)
        
        self.play(Create(horse_curve), run_time=3)
        self.wait(1)
        