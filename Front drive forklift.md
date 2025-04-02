# 单舵轮模型轮速计算

## 背景与初步观察
单舵轮系统 通过驱动电机控制速度，舵电机控制转向角度。需建立运动学模型描述轮速与电机转速的关系。

## 减速比
### 降低转速（Speed Reduction）：
减速器通过传动比降低主动轮（电机）的高转速，提供给从动轮一个较低的转速。
比如，减速比为10：1时，主动轮每旋转10圈，从动轮只会旋转1圈。

增加扭矩（Torque Amplification）：
减速器还能将电机提供的低扭矩放大到更高的扭矩输出。

根据能量守恒（忽略摩擦损耗）： 扭矩 × 转速 = 恒定功率 因此，转速降低时，扭矩会按相同比例增加。
例如，减速比为10：1时，从动轮的扭矩会是主动轮扭矩的10倍。

精确控制运动：
减速器可以降低负载的运动速度，这对于需要高精度运动控制的场景非常重要（如机器人关节或舵轮转向系统）。

## 转速和减速比关系
在任何机械传动系统中，实际转速和减速比之间的关系可以用以下公式表示：

$$
N_{\text{rpm-real}} = \frac{N_{\text{rpm}}}{Ratio_{\text{Reduction}}}
$$

## 轴距（旋转半径）
两从动轮间的中心点，到舵轮的直线距离。
以两个从动轮中心点为坐标轴起点，已知舵轮的坐标为x,y,则轴距:

$$
L=\sqrt {{x}^{2}+{y}^{2}}
$$

## 运动学模型
### 系统状态描述
| 符号 | 描述 |
|------|------|
| $x,y$ | 车辆质心坐标 |
| $\theta$ | 车辆朝向角 |
| $v$ | 线速度（驱动电机控制） |
| $\delta$ | 转向角（舵电机控制） |

---

# 逆解
## 驱动电机RPM → 轮速

$$
V_{\text{wheel}} = \frac{RPM_{\text{real}} \times 2\pi r} {60 \times Ratio_{\text{reduction}}}
$$



## 舵电机角度 → 舵轮角度

$$
\delta_{\text{real}} = ( \frac{Degree_{\text{steering}}}{Ratio_{\text{reduction}}} - ZeroBiasDegree) \cdot DegreeToRad
$$

## 轮速 → 整机速度

$$
V_{\text{linear}} = V_{\text{wheel}} \times \cos(\delta)
$$

$$
V_{\text{angular}} = \frac{V_{\text{wheel}} \times \sin(\delta)}{WheelBase}
$$

# 正解
## 整机速度 → 轮速、轮朝向
### 旋转运动

$$
\delta_{\text{target}} = 0.5 \cdot \pi - ZeroBiasDegree \cdot DegreeToRad
$$

$$
V_{\text{wheel}} = V_{\text{angular}} \cdot L
$$

### 静止

$$
\delta_{\text{target}} = ZeroBiasDegree \cdot DegreeToRad
$$

### 常规运动
#### 角速度 ω 与转向角 δ 之间的关系可以表示为：

$$
V_{\text{angular}}=\frac{V_{\text{linear}}}{R}
$$

$$
\delta_{\text{target}} = \arctan\left(\frac{WheelBase}{R}\right) = \arctan\left(\frac{WheelBase \cdot V_{\text{angular}}}{V_{\text{linear}}}\right)
$$

#### 轮速可以表示为：

$$
V_{\text{wheel}}=\frac{V_{\text{linear}}}{\cos(\delta)}
$$

## 轮速、轮朝向 → 驱动电机RPM、舵电机角度
### 驱动电机RPM

$$
N_{\text{rpm-real}}=\frac{V_{\text{wheel}} \cdot 60}{Radius_{\text{wheel}} \cdot 2 \cdot \pi} \cdot Ratio_{\text{Reduction}}
$$

### 舵电机角度

$$
Degree_{\text{steering}}=(\frac{\delta_{\text{target}}}{DegreeToRad} + ZeroBiasDegree) \cdot Ratio_{\text{Reduction}}
$$
