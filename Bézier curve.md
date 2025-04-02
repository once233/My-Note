# 二次贝塞尔曲线的计算

在标准二次贝塞尔曲线中，参数方程为：

$$
P(t) = (1 - t)^2 P_0 + 2(1 - t)t P_1 + t^2 P_2
$$

对于 \( x \) 坐标，展开为：

$$
x(t) = x_0 \cdot (1 - 2t + t^2) + 2 \cdot x_1 \cdot t \cdot (1 - t) + x_2 \cdot t^2
$$

进一步展开：

$$
x(t) = x_0 - 2 \cdot x_0 \cdot t + x_0 \cdot t^2 + 2 \cdot x_1 \cdot t - 2 \cdot x_1 \cdot t^2 + x_2 \cdot t^2
$$

## 合并同类项

**constant-item**:

$\( x_0 \)$

**t-item**:

$-2 \cdot x_0 \cdot t + 2 \cdot x_1 \cdot t = (-2 \cdot x_0 + 2 \cdot x_1) \cdot t$


**t^2-item**:

$x_0 \cdot t^2 - 2 \cdot x_1 \cdot t^2 + x_2 \cdot t^2 = (x_0 - 2 \cdot x_1 + x_2) \cdot t^2$


## 二次贝塞尔曲线的矩阵表示

## 标准参数方程
给定三个控制点 $P_0$, $P_1$, $P_2$，二次贝塞尔曲线可表示为：
$$
B(t) = (1-t)^2P_0 + 2t(1-t)P_1 + t^2P_2 \quad (t \in [0,1])
$$

## 矩阵形式
$$
B(t) = \begin{bmatrix} 1 & t & t^2 & t^3 \end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0 \\
-3 & 3 & 0 & 0 \\
3 & -6 & 3 & 0 \\
-1 & 3 & -3 & 1 \\
\end{bmatrix}
\begin{bmatrix} 
P_1 \\
P_2 \\
P_3 \\
P_4 \\
\end{bmatrix}
$$

