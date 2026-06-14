
from manim import *
class Video(Scene):
    def construct(self): 
        self.camera.background_opacity = 0
        text1 = Text("科幻世界2025.5", font_size=30)
        text2 = Text("《白日梦蓝》", font_size=30)
        text3 = Text("《海底》填词", font_size=48) 
        text4 = Text("填词：WinMCHG31400", font_size=20) 
        text6 = Text("演唱：AI", font_size=20) 
        text5 = Text("钢琴：MuseScore(软件)", font_size=20) 
        
        # 1. 中间偏左上
        text1.shift(UP*1.25 + LEFT*1.5)
        
        # 2. 中间偏右上  
        text2.shift(UP*1.25 + RIGHT*2)
        
        # 3. 中间偏大（正中央）
        text3.move_to(ORIGIN).shift(UP*0.5)  # 稍微向上调整
        
        # 4,5,6 中间偏右下偏小
        text_group = VGroup(text4, text5, text6)
        text_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        text_group.shift(DOWN*1)
        
        # 显示所有文本
        self.play(
            Write(text1),
            Write(text2),
            Write(text3),
            Write(text4),
            Write(text5),
            Write(text6),
            run_time=2
        )
        self.wait(2)