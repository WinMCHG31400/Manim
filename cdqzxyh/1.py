from manim import *
import re
# manim "C:\manim_projects\cdqzxyh\1.py" -p
class LyricsScroll(Scene):
    def construct(self):
        # 直接读取LRC文件
        lyrics = self.parse_lrc_file("C:/manim_projects/cdqzxyh/lrc/14.lrc")
        
        # 创建滚动歌词区域
        lyrics_group = VGroup()
        for i, (time, text) in enumerate(lyrics):
            lyric = Text(text, font_size=32, color=GRAY)
            lyric.move_to(ORIGIN + DOWN * i * 0.8)
            lyrics_group.add(lyric)
        
        lyrics_group.move_to(ORIGIN)
        self.add(lyrics_group)
        
        # 动画滚动效果
        for i, (time, text) in enumerate(lyrics):
            # 高亮当前歌词
            current = lyrics_group[i]
            original_color = current.color
            
            # 高亮效果
            current.set_color(YELLOW)
            current.scale(1.1)
            
            # 等待对应时间
            if i < len(lyrics) - 1:
                wait_time = lyrics[i+1][0] - time
                if(wait_time > 0):
                    self.wait(wait_time)
            else:
                self.wait(2)
            
            # 恢复
            current.set_color(original_color)
            current.scale(1/1.1)
            
            # 向上滚动
            if i < len(lyrics) - 3:
                self.play(lyrics_group.animate.shift(UP * 0.8), run_time=0.3)
        
        self.wait(2)
    
    def parse_lrc_file(self, filename):
        """解析LRC文件"""
        lyrics = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    # 匹配时间标签 [mm:ss.xx]
                    matches = re.findall(r'\[(\d+):(\d+\.\d+)\](.*)', line)
                    for match in matches:
                        minutes = int(match[0])
                        seconds = float(match[1])
                        time = minutes * 60 + seconds
                        text = match[2].strip()
                        if text:  # 只添加非空歌词
                            lyrics.append((time, text))
            
            # 按时间排序
            lyrics.sort(key=lambda x: x[0])
            return lyrics
        except FileNotFoundError:
            print(f"文件 {filename} 不存在")
            exit
            return []
        except Exception as e:
            print(f"读取文件出错: {e}")
            return []

# 创建动画
scene = LyricsScroll()
scene.render()