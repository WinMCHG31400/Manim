from manim import *
class Video(Scene):
    def construct(self): 
        for cycle_num in range(5):  # 循环5圈
            # 创建新圆
            circle = Circle(radius=2, color="#4f6f8f", stroke_width=6)   
            dot = Dot(color=BLUE)
            traced_path = TracedPath(
                dot.get_center,           # 追踪粒子的位置
                stroke_color=BLUE,        # 尾迹颜色
                stroke_width=8,          # 尾迹粗细
                stroke_opacity=[0, 0.8], # 透明度渐变 [起点, 终点]
                dissipating_time=1.5     # 尾迹消散时间
            )
            self.play(
                AnimationGroup(
                Create(dot),
                Create(traced_path),
                run_time=0.1
                )
            )
            # 画圆动画
            self.play(
                AnimationGroup(
                    dot.animate.shift(RIGHT*3,UP*3),
                    run_time=2
                ),
                AnimationGroup(
                    Create(circle, run_time=3, rate_func=linear),
                    run_time=1
                ),
                
            )
            self.play(
                AnimationGroup(
                    FadeOut(dot),
                    run_time=1
                )
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
            
            self.wait(0.2)
        self.wait(2)
        