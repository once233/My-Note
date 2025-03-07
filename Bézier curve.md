## 二次贝塞尔曲线的计算

研究表明，\( a_2 \) 的计算方式与二次贝塞尔曲线的扩展形式相关。在标准二次贝塞尔曲线中，参数方程为：

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

### 合并同类项

$$
**constant item**:
\( x_0 \)
$$
$$
**\( t \) item**:
-2 \cdot x_0 \cdot t + 2 \cdot x_1 \cdot t = (-2 \cdot x_0 + 2 \cdot x_1) \cdot t
$$
$$
**\( t^2 \) item**:
\[
x_0 \cdot t^2 - 2 \cdot x_1 \cdot t^2 + x_2 \cdot t^2 = (x_0 - 2 \cdot x_1 + x_2) \cdot t^2
$$
