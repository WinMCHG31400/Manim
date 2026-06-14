from manim import *
from math import *
#      manim "C:\manim_projects\dtb\1.py" -p
class LyricsVideo(Scene):
    def construct(self):
        text_1=Text("一个视频带你在数学上弄懂", font_size=30).shift(UP*0.5)
        text_2=Text("导体棒在磁场中的运动规律", font_size=48).shift(DOWN*0.5)
        self.play(Write(text_1), run_time=2)
        self.play(Write(text_2), run_time=2)
        self.wait(2)
        self.play(FadeOut(text_1), FadeOut(text_2), run_time=1.5)
        line1=Line((-4,3,0),(4,3,0),color=WHITE)
        line2=Line((-4,1,0),(4,1,0),color=WHITE)
        line3=Line((-4,3,0),(-4,2.25,0),color=WHITE)
        line4=Line((-4,1.75,0),(-4,1,0),color=WHITE)
        rect1=Rectangle(width=2, height=0.5, color=BLUE, fill_color=BLUE, fill_opacity=0.4).move_to((-4,2,0))
        b_grid=VGroup()
        for x in np.arange(-4.5,5,1):
            for y in np.arange(0.5,4.5,1):
                cross = VGroup(
                    Line([x-0.15, y-0.15, 0], [x+0.15, y+0.15, 0], color=RED, stroke_width=2),
                    Line([x-0.15, y+0.15, 0], [x+0.15, y-0.15, 0], color=RED, stroke_width=2)
                )
                b_grid.add(cross)
        self.play(Create(b_grid),Create(line1), Create(line2), Create(line3), Create(line4), Create(rect1), run_time=2)
        line5=Line((-2,3.5,0),(-2,0.5,0),color=BLUE)
        self.play(Create(line5), run_time=1.5)
        text_3=Text("R", font_size=30).move_to((-4,2,0))
        text_4=Text("m,L", font_size=30).move_to((-2,0,0))
        self.play(Write(text_3), Write(text_4), run_time=2)
        #这是一个简单的磁场，导体棒放在接有电阻的电路中
        self.wait(1.5)
        vec1=Arrow(start=[-2,2,0],end=[0,2,0], color=YELLOW,buff=0)
        text_5=Text("v", font_size=30).move_to((-1,1.75,0))
        self.play(Create(vec1), Write(text_5), run_time=2)
        v_grid=VGroup(vec1,text_5)
        #现在我给它一个向右的加速度
        # def x_fun1(t):
        #     return 2*exp(-0.5*t)
        # self.remove(v_grid)
        # line5.add_updater(
        #     lambda d, dt: d.move_to([x_fun1(self.time), 0, 0])
        # )
        # self.wait(3)
        # #它将向右运动
        # self.wait(1.5)
        # self.play(FadeIn(v_grid),line5.animate.move_to((-2,2,0)), run_time=2)
        pic1=VGroup(b_grid,line1, line2, line3, line4, line5, rect1, text_3, text_4,v_grid)
        self.play(pic1.animate.scale(0.7).shift(UP*0.5), run_time=2)
        #我们对它进行受力分析
        self.wait(1.5)
        text0=MathTex(r"\frac{B^2L^2}{R}v=ma").shift(DOWN*0.5)
        text1=MathTex(r"a=-\frac{B^2L^2}{mR}v") 
        self.play(Write(text0), run_time=2)
        self.wait(1.5)
        self.play(Transform(text0,text1), run_time=2)
        self.wait(1.5)
        text2=MathTex(r"\frac{dv}{dt}=-\frac{B^2L^2}{mR}v")
        self.remove(text0)
        self.play(Transform(text1,text2), run_time=2)
        self.wait(1.5)
        text3=MathTex(r"\frac{dv}{dt}+\frac{B^2L^2}{mR}v=0").shift(DOWN*0.5)
        self.play(Write(text2),text1.animate.shift(UP*1), run_time=2)
        self.play(Transform(text2,text3), run_time=2)
        self.remove(text2)
        text4=MathTex(r"v=Ce^{-\frac{B^2L^2}{mR}t}")
        text5=MathTex(r"v\big|_{t=0}=v_0")
        self.play(Write(text4),text3.animate.shift(UP*1.5), FadeOut(text1),run_time=2)
        self.play(Write(text5),text3.animate.shift(UP*1), text4.animate.shift(UP*1),run_time=2)
        group1=VGroup(text4,text5)
        text6=MathTex(r"v_0=Ce^0")
        text7=MathTex(r"v=v_0e^{-\frac{B^2L^2}{mR}t}")
        self.play(Transform(group1,text6),run_time=2)
        self.remove(group1)
        self.play(Transform(text6,text7),run_time=2)
        self.remove(text6)
        self.wait(2)
        self.wait(10.5)