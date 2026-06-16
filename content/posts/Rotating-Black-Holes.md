---
title: Rotating Black Holes
date: '2025-04-09T10:57:35+08:00'
categories:
- 广义相对论
---


A note for Chap 15 of James.B.Hartle's *An Introduction to Einstein's General Relativity*.

---

# Rotating black holes

Schwarzchild黑洞并非是广义相对论预言的最普遍的黑洞, Schwarzchild黑洞只有一个参数$M$. Roy Kerr在1963年给出了Einstein场方程的另一个真空解, 可以描述另一种更一般的黑洞, 它有两个参数质量$M$和角动量$J$, 叫做Kerr黑洞.

## The Kerr Geometry

我们使用单位制$c = G = 1$. 这样Kerr度规可以写成
$$
\mathrm ds^2 = - \left(1 - \frac{2Mr}{\rho^2}\right) \mathrm dt^2
-\frac{4Mar\sin^2\theta}{\rho^2}\mathrm d\phi \mathrm dt
+\frac{\rho^2}{\Delta}\mathrm dr^2
+\rho^2 \mathrm d\theta^2
+\left(r^2 + a^2 + \frac{2Mra^2\sin^2\theta}{\rho^2}\right)\sin^2\theta\mathrm d\phi^2,
$$
其中
$$\begin{gathered}
a \equiv J/M, \\
\rho^2 \equiv r^2 + a^2 \cos^2\theta,\\
\Delta \equiv r^2 - 2Mr + a^2.
\end{gathered}$$
这里$a$称作*Kerr参数*, 量纲是$1$, 使用的坐标称作*Boyer-Lindquist-coordinates坐标*. 我们接下来考察Kerr几何的一些性质:
- **Asymptotically flat**. 对于$r\gg M$并且$r\gg a$, 这个线元变成
$$
\mathrm ds^2 \approx -\left(1 - \frac{2M}{r}\right)\mathrm dt^2
+\left(1 + \frac{2M}{r}\right)\mathrm dr^2
+r^2\left(\mathrm d\theta^2 + \sin^2\theta \mathrm d\phi^2\right)
-\frac{4Ma}{r^2}\sin^2\theta r\mathrm d\phi \mathrm dt.
$$
在远离黑洞的位置处, 时空是接近平直的. 通过远处卫星的轨道可以确定$M$的大小, 而通过远处陀螺仪的进动可以确定$J$的大小.
- **Stationary, axisymmetric**. 上面给出的Kerr度规和时间$t$无关(stationary), 也和取向$\phi$无关(axisymmetric). 我们可以找到两个Killing vector
$$\begin{gathered}
\xi^\alpha = (1, 0, 0, 0), \\
\eta^\alpha = (0, 0, 0, 1).
\end{gathered}$$
此外如果按$\theta=\pi/2$的平面反射$\theta\rightarrow\pi-\theta$, 这个度规是不变的.
- **Schwarzschild when not rotating**. 令$a = 0$, Kerr度规完全变成Schwarzchild度规, 也就是说Schawarzchild黑洞是一种零角动量的Kerr黑洞.
- **Coordinate singularities, real singularities and horizon**. $\Delta = 0$或者$\rho = 0$都对应了Kerr度规的奇点. $\rho = 0$对应$r = 0, \theta = \pi/2$, 这个点时空曲率无穷大, 对应于Schwarzchild几何中$r = 0$的奇点. $\Delta = 0$给出
$$
r_\pm = M \pm \sqrt{M^2 - a^2}.
$$
当$a<M$时有这两个奇点. $r_+$成为Kerr黑洞的视界. 也就是说, 如果想要成为一个Kerr黑洞, 必须满足$a<M$. 当物质落入黑洞时, 它的角动量也带给黑洞, 在这个过程中黑洞的角动量逐渐接近$J = M^2$的极限, 这种接近极限情况的黑洞可以自然形成.

## The horizon of a rotating black hole

视界(horizon)是光能逃逸到无穷远的区域的内表面, 限制了无穷远观察者能获得信息的范围. 对于一个Schwarzchild黑洞来说, 视界是$r = 2M$. 我们说一个曲面是*null*的, 如果在这个曲面上存在一个类光的切向量场, 并且存在两个与之正交的类空的切向量场. 对于Kerr度规来说, 我们可以证明视界$r = r_+$是null的: 首先, 这个视界的切向量应该写成
$$
t^\alpha = (t^t, 0, t^\theta, t^\phi).
$$
如果有一个类光的(null)的切向量场, 应该满足
$$
g_{\mu\nu}l^\nu l^\mu =
\left(\frac{2Mr_+\sin\theta}{\rho_+}\right)^2\left(l^\phi - \frac{a}{2Mr_+}l^t\right)^2 + \rho_+^2(l^\theta)^2 = 0. 
$$
这个方程的唯一解是$l^\theta = 0, l^\phi = \frac{a}{2Mr_+}l^t$. 在最多相差一个常数因子的情况下, 在$r = r_+$曲面上唯一的null切向量场是
$$
l^\alpha = (1, 0, 0, \Omega_H),\ \ \Omega_H = \frac{a}{2Mr_+}.
$$
$(0, 0, 1, 0)$和$(0, 0, 0, 1)$是两个和$\bm l$正交的类空切向量. 这样就说明了$r = r_+$是null的, $\bm l$同时也是一个法向量场, 也是视界上的某条类光曲线的切向量, 按这个角度发出的光线会被限制在这个曲面上, 以$\Omega_H$的角速度旋转($\mathrm d\phi/\mathrm dt = l^\phi/l^t$).

尽管视界由$r = r_+$完全确定, 其上的几何并不是完全球对称的,
$$
\mathrm d\Sigma^2 = \rho_+^2\mathrm d\theta^2 + \left(\frac{2Mr_+}{\rho_+}\right)^2\sin^2\theta \mathrm d\phi^2.
$$
也可以由此得到视界的面积$A = \int 2Mr_+\sin\theta \mathrm d\theta d\phi = 8\pi M(M + \sqrt{M^2 - a^2})$. 这个视界是单向的, 可以从外界进入视界, 但是不能离开.

## Orbits in the equatorial plane

在Kerr度规下, 运动轨道不再和Schwarzchild度规下一样一定保持在一个平面内, 并且现在只有沿旋转轴方向的角动量是是守恒的. 作为一个简单的例子, 我们来考虑赤道面内的轨道.

首先考虑到$\theta\rightarrow \pi - \theta$的对称性, $4$-速度的$\theta$的分量是$0$. 这样限制在$\theta = \pi/2$赤道面里的线元就是
$$
\mathrm ds^2 = -\left(1 - \frac{2M}{r}\right)\mathrm dt^2 - \frac{4aM}{r}\mathrm dt\mathrm d\phi
+\frac{r^2}{\Delta}\mathrm dr^2 + \left(r^2 + a^2 + \frac{2Ma^2}{r}\right)\mathrm d\phi^2.
$$
通过之前我们构造的两个killing vector, 可以给出两个守恒量, 
$$\begin{gathered}
e \equiv - \bm \xi \cdot \bm u,\\
l \equiv \bm \eta \cdot \bm u.
\end{gathered}$$
赤道面里的轨道通过这两个守恒量完全参数化, 此外$4$-速度还应该满足$u^\mu u_\mu = -1$. 现在可以写一部分运动方程
$$\begin{gathered}
\frac{\mathrm dt}{\mathrm d\tau} = \frac{1}{\Delta}\left[
    \left(r^2 + a^2 + \frac{2Ma^2}{r}e - \frac{2Ma}{r}l\right)
\right], \\
\frac{\mathrm d\phi}{\mathrm d\tau} = \frac{1}{\Delta}\left[
    \left(1 - \frac{2M}{r}\right)l + \frac{2Ma}{r}e
\right].
\end{gathered}$$
$r$方向的运动方程可以通过$\bm u$的归一化条件得到,
$$\begin{gathered}
\frac{e^2 - 1}{2} = \frac{1}{2}\left(\frac{\mathrm dr}{\mathrm d\tau}\right)^2 + V_{\text{eff}}(r, e, l),\\
V_{\text{eff}} = - \frac{M}{r} + \frac{l^2 - a^2(e^2 - 1)}{2r^2} - \frac{M(l - ae)^2}{r^3}.
\end{gathered}$$
对于光来说, 只需要把只需要修改条件为$u^\mu u_\mu = 0$就可以, 它的有效势依赖于$r, b \equiv |l/e|, \sigma \equiv \mathrm{sign}(l)$.

Kerr黑洞和Schwarzchild黑洞对于$r$的依赖势类似的, 但是Kerr黑洞会拖曳周围的时空, 具体来说, $l$的符号会应影响感受到的有效势.

作为一个例子, 对光来说, 考虑$M = a$的极端Kerr黑洞, 存在一个$r = 2M$的corotating的不稳定轨道和一个$r = 4M$的counterrotating的不稳定轨道. 对一个一般的粒子, 在一个$r = R$的圆形轨道上, 满足
$$
\frac{e^2 - 1}{2} = V_{\text{eff}}(R, e, l).
$$
此外在圆轨道应该是一个驻点,
$$
\left.\frac{\partial V_{\text{eff}(r, e, l)}}{\partial r}\right|_{r=R} = 0.
$$
如果同时还要求这个轨道是稳定的, 应该有二阶导大于$0$. 如果是一个最内层的稳定轨道, 也就是处在临界状态, 会要求二阶导等于零. 这些方程完全确定了所有可能的圆轨道. 也可以计算这些轨道的结合能$1 - e$: 轨道上的能量和处在无穷远的能量差.

### The orbit of a radially infalling particle

考虑一个零动能, 从无穷远开始落入黑洞的粒子$e = 1$, $l = 0$. 轨道的形状由下面的微分方程决定
$$
\frac{\mathrm d\phi}{\mathrm dr} = \frac{\mathrm d\phi/\mathrm d\tau}{\mathrm dr/\mathrm d\tau} 
= -\frac{2Ma}{r\Delta}\left[\frac{2M}{r}\left(1 - \frac{a^2}{r^2}\right)\right]^{-1/2}.
$$
尽管下落的物体自身并没有角动量, 由于旋转黑洞的存在, 它仍然在下落过程中产生角位移.

## The ergoshpere

### Stationary observers

我们定义一个静止的观察者, 如果其$4$-速度只有时间分量,
$$
u_{\text{obs}}^\alpha = (u^t_{obs}, 0, 0, 0).
$$
并且满足$u_\mu u^\mu = -1$, 这意味着
$$
u_{\text{obs}\mu}u^\mu_{\text{obs}} = - \left(1 - \frac{2Mr}{\rho^2}\right)(u^t_{\text{obs}})^2 = -1.
$$
当靠近Kerr黑洞的视界到一定程度的时候, $g_{tt}$就会变成$0$, 再往里就给不出一个$u_{\text{obs}^t}$的解了, 具体地, 这个边界是
$$
r = r_e(\theta) = M + \sqrt{M^2 - a^2\cos^2\theta}.
$$
这个曲面内部是不允许有静止观察者的. 这个曲面和视界之间的区域叫做能层(ergosphere). 在能层中不允许有一个静止的观察者, 但或许可以允许观察者的$r, \theta$坐标固定, $\phi$方向上有一个角速度, 
$$
u^\alpha_{\text{obs}} = u_{\text{obs}}^t(1, 0, 0, \Omega_{\text{obs}}) 
= u^t_{\text{obs}}(\xi^\alpha + \Omega_{\text{obs}}\eta^\alpha).
$$
对于能层内的每一组坐标$r, \theta$, 都有一个最小的$\Omega_{\text{obs}}$作为允许上面描述的这种观察者出现的下界.

### Extracting rotational energy

我们来考虑Penrose过程: 一个粒子从无穷远飞进能层, 然后衰变成两个粒子, 其中一个粒子掉进视界内, 而另一个粒子又飞回无穷远. 通过这种过程, 我们有可能从一个Kerr黑洞中获得能量.

在衰变过程中能动量应该是守恒的, 并且衰变是一个局部过程, 小范围内时空是平直的, 满足
$$
\bm p_{\text{in}} = \bm p_{\text{out}} + \bm p_{\text{bh}}.
$$
飞出来的粒子的静止质量是$m_{\text{out}}$, 它的能量是$E_{\text{out}} = m_{out}e$. 我们有
$$
E_{\text{out}} = E_{\text{in}} - E_{\text{bh}}.
$$
在能层里$g_{tt} > 0$, 这样$\xi^\alpha$就是类空的. 在这种情况下$E_{\text{bh}}$不再有能量的含义, 它只是动量的某个分量, 并且可能正, 可能负, 这样我们就可以通过这个过程从黑洞中获得能量.

在这个过程中不但黑洞的能量会减少, 黑洞的角动量也会减少, 考虑一个corotating的在能层里面的观察者,
$$
u^\alpha_{\text{obs}} = u^t_{\text{obs}}(\xi^\alpha + \Omega_{\text{obs}}\eta^\alpha).
$$
这个观察者观察到的落入黑洞的粒子应该有正的能量,
$$
-(\xi^\alpha + \Omega_{\text{obs}\eta^\alpha})p_\alpha \geq 0.
$$
这样就有
$$
E_{bh} \geq \Omega_{\text{obs}}L_{bh}.
$$
因为$E_{bh}$是负的, 所以$L_{bh}$也是负的. 通过Penrose过程, 我们可以不断地把Kerr黑洞的旋转部分的能量降低到$0$, 但是不可能使整个黑洞消失, 黑洞的视界面积在这个过程中是不减的(实际上黑洞的视界面积在各种情况下都是不减的), 我们考虑视界面积的变化
$$\begin{gathered}
\Delta A = \frac{8\pi}{\kappa}\left(\Delta M - \Omega_H\Delta J\right), \\
\kappa \equiv \frac{(M^2 - a^2)^{1/2}}{2Mr_+}.
\end{gathered}$$
在视界附近的观察者, 如果和前面得到的null切向量场相同的运动的话, 有着最大的角速度$\Omega_H$, 也就是说$\Delta M > \Omega_H \Delta J$, 这就说明在Penrose过程会增大Kerr黑洞的视界面积.

我们定义约化质量$M_{\text{ir}} = \left(\frac{A}{16\pi}\right)^{-1/2}$, 这个值是不减的, 利用黑洞视界面积的表达式我们有
$$
M^2 = M_{\text{ir}}^2 + \frac{J^2}{2M_{\text{ir}}^2}.
$$
这给出了黑洞能量的组成, Penrose过程降低的是第二项, 第一项是不减的.