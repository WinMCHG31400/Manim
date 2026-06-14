from manim import *
class Video(Scene):
    def construct(self): 
        dot = Dot(color=BLUE)  # 初始位置在右侧
        block=Square(side_length=3, color=WHITE)
        block.rotate(PI/2)
        self.play(Create(dot),
                  Create(block),
                  run_time=1)
        for cycle_num in range(5):  # 循环5圈
            # 创建新圆
            circle = Circle(radius=3, color="#4f6f8f", stroke_width=6)
            
            # 画圆动画
            self.play(
                Create(circle, run_time=1, rate_func=linear),
            )
            
            # 创建残影副本
            ghost = circle.copy()
            ghost.set_stroke(opacity=0.2, color=BLUE_D)
            
            # 添加残影并准备下一圈
            if cycle_num < 4:  # 最后一圈不留残影
                self.add(ghost)
                self.play(
                    circle.animate.set_stroke(opacity=0).scale(0.95),
                    run_time=0.5
                )
                self.remove(circle)
            
        self.wait(2)
        