## NURBS曲线公式

NURBS曲线的公式如下：

P(u) = (Σ (N<sub>i,k</sub>(u) * w<sub>i</sub> * P<sub>i</sub>)) / (Σ (N<sub>i,k</sub>(u) * w<sub>i</sub>))

### 其中：

- N<sub>i,k</sub>(u) 是 B 样条基函数。
- w<sub>i</sub> 是第 i 个控制点的权重。
- P<sub>i</sub> 是第 i 个控制点 (x, y, z)。

这个公式用于计算给定参数 u 下的 NURBS 曲线位置 P(u)。
