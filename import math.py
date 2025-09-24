import math

class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def distance(self, other): return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

points = []
for i in range(5):  # 生成5个随机点
    points.append(Point(i*10, i*5))

print("所有坐标点:")
for i, p in enumerate(points): 
    print(f"点{i+1}: ({p.x}, {p.y})")

if len(points) > 1:
    dist = points[0].distance(points[1])
    print(f"\n点1和点2之间的距离: {dist:.2f}")

# 找出中心点
avg_x = sum(p.x for p in points) / len(points)
avg_y = sum(p.y for p in points) / len(points)
print(f"\n中心点坐标: ({avg_x:.1f}, {avg_y:.1f})")