# 差速轮模型

## 减速比
### 降低转速（Speed reduction）：
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
N_{\text{rpm-real}} = \frac{N_{\text{rpm}}}{Ratio_{\text{reduction}}}
$$

## 轴距
两动力轮间的距离


## 运动学模型
### 系统状态描述
| 符号 | 描述 |
|------|------|
| $x,y$ | 车辆质心坐标 |
| $\theta$ | 车辆朝向角 |
| $V_{\text{linear}}$ | 整机线速度 |
| $V_{\text{angular}}$ | 整机角速度 |

---

# 逆解
## 驱动电机RPM → 轮速

# 正解
## 整机速度 → 左轮速、右轮速

$左轮速 \( V_l \)：$

$$
V_l = V_{\text{linear}} - \frac{V_{\text{angular}} \cdot L}{2}
$$

$右轮速 \( V_r \)：$

$$
V_r = V_{\text{linear}} + \frac{V_{\text{angular}} \cdot L}{2}
$$

## 左轮速、右轮速 → 驱动电机RPM

$$
N_{rpm-l} = \frac{V_{\text{wheel-l}} \cdot Ratio_{\text{reduction}}}{DegreeToRad \cdot Radius_{\text{wheel-l}}}
$$

$$
N_{rpm-r} = \frac{V_{\text{wheel-r}} \cdot Ratio_{\text{reduction}}}{DegreeToRad \cdot Radius_{\text{wheel-r}}}
$$

