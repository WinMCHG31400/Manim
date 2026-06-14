from manim import *
class Video(ThreeDScene):
    def construct(self): 
        grid = ThreeDAxes(
            x_range=[-12, 12, 0.6],
            y_range=[-12, 12, 0.6],
            z_range=[-12, 12, 0.6],
            x_length=20,
            y_length=20,
            z_length=20,
            axis_config={
                "color": WHITE,
                "include_tip": False,
                "stroke_width": 1,
            }
        )
        grid.z_axis.remove(grid.z_axis)
        black_hole = Sphere(radius=0.3, color=BLUE)
        # 设置相机
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        # 强引力扭曲函数
        def strong_gravity(point):
            x, y, z = point
            r = np.sqrt(x**2 + y**2 + z**2)
            
            if r < 0.5:
                return [0.0, 0.0, -10.0]  # 掉入奇点
            
            # 史瓦西度规风格的强扭曲
            rs = 0.1  # 史瓦西半径
            factor = 1 - rs/r
            
            if factor <= 0:
                return [x * 0.1, y * 0.1, z * 0.1 - 5]  # 事件视界内
            
            # 强烈的径向拉伸
            radial_factor = 1 / np.sqrt(factor) * 0.8
            
            # 角度扭曲
            theta = np.arctan2(y, x)
            phi = np.arctan2(z, np.sqrt(x**2 + y**2))
            
            new_r = r * radial_factor
            
            # 转换回直角坐标
            nx = new_r * np.cos(theta) * np.cos(phi)
            ny = new_r * np.sin(theta) * np.cos(phi)
            nz = new_r * np.sin(phi)
            
            return [nx, ny, nz]  # 向下拉
        
        # 应用扭曲
        warped_grid = grid.copy()
        warped_grid.apply_function(strong_gravity)
        
        # 显示
        self.play(FadeIn(grid), FadeIn(black_hole), run_time=1)
        self.wait()
        
        # 剧烈扭曲
        self.play(
            Transform(grid, warped_grid),
            run_time=4,
            rate_func=rush_into
        )
        
        self.wait(2)