from manim import *
class LyricsVideo(Scene):
    def construct(self):
        lyrics = [
            [208.05, 212.7, "来不及 来不及"],
            [212.7, 217.15, "你曾笑着哭泣"],
            [217.15, 221.6, "来不及 来不及"],
            [221.6, 226.05, "如何将你救起"],
            [226.05, 230.45, "寒冬去 暖春至"],
            [230.45, 235.0, "你仍困住循环里"],
            [235.0, 239.85, "蒸发弃 轮回启"],
            [239.85, 243.7, "你明明不曾放弃"],
        ]
        for i in range(0, len(lyrics) - 1, 2):
            text = Text(lyrics[i][2])
            self.play(Write(text), run_time=2.0)
            t = lyrics[i][1] - lyrics[i][0] - 3.0
            if t > 0:
                self.wait(t)  # 等待到歌词结束
            text2 = Text(lyrics[i + 1][2])
            self.play(Transform(text, text2), run_time=2.0)
            t = lyrics[i + 1][1] - lyrics[i + 1][0] - 3.0
            if t > 0:
                self.wait(t)  # 等待到歌词结束
            self.play(FadeOut(text2),FadeOut(text), run_time=1.0)
            self.wait()  # 等待0.5秒再显示下一句歌词
        self.wait(0.5)