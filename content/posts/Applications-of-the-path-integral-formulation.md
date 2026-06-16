---
title: Applications of the path integral formulation
date: '2025-04-10T15:26:42+08:00'
categories:
- 多体系统的量子场论
featured_image: /images/611c39a5001a4fe5b97c.png
---


A note for Sec 2.4 for 文小刚's *多体系统的量子场论*.

---

## Applications of the path integral formulation

### Tunneling through a barrier

我们试图使用量子场论去计算一些非微扰的结果, 一个例子就是隧穿. 考虑一个对称的双势阱, 就像我们在讨论经典的对称性自发破缺时候常画的那种(很遗憾这里没有图片, 加图片会严重增加工作量, 我可能宁可选一张有意思的封面).

如果不允许隧穿的话, 在两个局部最小值$x_0, -x_0$附近, 势的形状可以用一个频率为$\omega_0$的谐振子描述, 那么我们可以计算下面的传播子
$$\begin{gathered}
\langle x_0 |e^{-TH} |x_0 \rangle = \langle -x_0 |e^{-TH} | -x_0 \rangle = e^{-T\omega_0/2}, \\
\langle x_0 | e^{-TH} | -x_0 \rangle  = 0.
\end{gathered}$$

如果我们考虑隧穿的话, 这个结果显然不正确, 因为除了稳定路径, 还有那些在两个极值点之间变换的路径需要考虑. 这显然是非微扰的结果, 因为当我们考虑在稳定路径周围的微扰时, 不可能得到隧穿.

我们使用虚时路径积分和驻点近似. 除了$x_c(t) = x_0$和$x_c(t) = -x_0$这两个路径之外, 还有从$x_0$到$-x_0$的稳定路径, 这条路径最小化了作用量$\int\mathrm d\tau (\frac{1}{2}m\dot{x}^2 + V(x))$, 那么它应该满足了运动方程$\frac{\mathrm d^2 x}{\mathrm d\tau^2} = V'(x)$. 这个路径就好像在虚时$\tau$下按$-V(x)$的运动, 一种可能的解是前半段时间$x = x_0$, 然后在短时间内位置从$x_0$变到$-x_0$, 之后一直待在$-x_0$. 这种在$x_0$和$-x_0$之间的移动叫做*instanton*. 那么实际上的稳定路径可以有多个instanton.

当我们计算传播子的时候, 需要考虑所有的可能的稳定路径. 如果我们计算从$x_0$到$x_0$的传播子, 那么那些包含偶数个instanton的路径都应该被考虑:
$$\begin{aligned}
\langle x_0 | e^{-TH} | x_0 \rangle = & e^{-T\omega_0/2}\sum_{n=\text{even}}
\int_0^T \mathrm d\tau_n \cdots \int_0^{\tau_2} \mathrm d\tau_1 (Ke^{-S_0})^{n} \\
= & e^{-T\omega_0/2}\sum_{n = \text{even}} \frac{T^n}{n!}(Ke^{-S_0})^n \\
= & e^{-T\omega_0/2} \frac{1}{2} \left(e^{TKe^{-S_0}} + e^{-TKe^{-S_0}}\right)\\
= & e^{-T\omega_0/2} \cosh (TKe^{-S_0}).
\end{aligned}$$
上面的$e^{-T\omega_0/2}$的来自于路径的主要部分还是静止在极值点, $S_0$是稳定路径中instanton的作用量, 而$K$是在其周围的路径导致的微扰, 在这里应该有一个和频率相同的量纲, 很粗略的说, 大概是粒子撞上势垒的频率. 这里对$n$个$\tau_i$的积分来源于每个instanton出现的时间是不确定的. 那么类似的, 我们也可以得到
$$\begin{aligned}
\langle x_0 | e^{-TH} | -x_0 \rangle = & e^{-T\omega_0/2}\sum_{n=\text{odd}}
\int_0^T \mathrm d\tau_n \cdots \int_0^{\tau_2} \mathrm d\tau_1 (Ke^{-S_0})^{n} \\
= & e^{-T\omega_0/2} \sinh (TKe^{-S_0}).
\end{aligned}$$
那么考虑对称或者反对称的态$|\psi_\pm\rangle = (|x_0\rangle \pm |-x_0\rangle)/\sqrt 2$. 有
$$
\langle \psi_\pm | e^{-TH} | \psi_\pm \rangle = \exp(-T(\frac{\omega_0}{2} \pm Ke^{-S_0})). 
$$
那么$|\psi_\pm\rangle$是两个能量是$\frac{\omega_0}{2}\pm Ke^{-S_0}$的本征态(大概, 起码是对称或者反对称的).

计算$S_0$, 虚时下经典的路径是$\dot{x} = \sqrt{2V(x)/m}$, 那么可以得到
$$
S_0 = \int_{-\infty}^{\infty}\mathrm d\tau \left(\frac{1}{2}m\dot{x}^2 + V(x)\right)
= \int_{-x_0}^{x_0}\mathrm dx \sqrt{2mV(x)}.
$$
那么因为隧穿导致的能量修正是$\Delta E = 2K \exp(\int_{-x_0}^{x_0}\mathrm dx\sqrt{2mV(x)})$, 这就是WKB近似给出的结果. 但相比于WKB近似, 因为我们给出了一个路径, 因此可以估计隧穿的时间.

### Fate of a meta-stable state

现在我们来考虑一个势, 在最中间有一个势垒, 左边会掉到负无穷, 右边先下降到$0$($x_0$), 然后上升到正无穷, 形成一个势阱, 负半轴上的零点是$x_1$.

有一个粒子, 开始在$x_0$处, 我们关心它如何逐渐泄露出这个势阱. 为了描述这个隧导致的衰减, 我们需要计算$\langle x_0 |e^{-iTH}| x_0 \rangle$并希望它随时间衰减. 如果考虑虚时的路径积分的话, 除了路径$x_c(t) = x_0$, 还有其他的稳定路径, 从$x_0$出发, 经过整数个和$x_1$之间的instanton回到$x_0$. 和上一节讨论的类似, 
$$
\langle x_0 |e^{-iTH}| x_0 \rangle = e^{-T(\frac{\omega_0}{2} - Ke^{-S_0})}.
$$
为了在做一个Wick旋转之后得到衰减的结果, 要求$K$应该是虚的, 我们接下来来说明这一点.

现在粒子的在虚时下的运动是由$-V(x)$确定的, 现在我们说的一个instanton是指从$x_0$出发到$x_1$又回到$x_0$, 或者叫一个bounce, 把包含一个bounce这个路径叫做$x_c(\tau)$. 那么$Ke^{-S_0}$应该是在$x_c$附近和$x(t) = x_0$附近的路径积分的比值,
$$
Ke^{-S_0} = \frac{\int_{x_c}\mathcal D\delta x e^{-S}}{\int_{x=x_0}\mathcal D\delta x e^{-S}}.
$$
具体地, 在$x_c$附近
$$
S = S_0 + \int \mathrm d\tau \delta x \frac{1}{2}\left[-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_c(\tau))\right]\delta x,
$$
在$x_0$附近
$$
S = \int d\tau \delta x \frac{1}{2}\left[-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_0)\right]\delta x.
$$
上面三个表达式是由于: 首先在$x=x_0$上的积分是$0$, 然后我们要计算的是$Ke^{-S_0}$, 这个值只有在instanton上的贡献, 所以我们要除掉平凡路径$x_0$的贡献. 现在得到
$$
K = \left(\frac{\det(-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_0))}{\det(-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_c))}\right).
$$
问题是上面的表达式的分母上的矩阵, 实际上有零特征值. 如果我们考虑路径$x_c(\tau)$和一个按时间平移一点的路径$x_c(\tau + \eta)$, 它们都是稳定路径, 满足对应的运动方程
$$
-m\frac{\mathrm d^2 x_c(\tau)}{\mathrm d\tau^2} + V'(x_c(\tau)) =
-m\frac{\mathrm d^2 x_c(\tau + \eta)}{\mathrm d\tau^2} + V'(x_c(\tau + \eta)) = 0.
$$
这样我们就得到
$$
\left[-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_c)\right]\dot{x_c}(\tau) = 0.
$$
这说明$\dot{x_c}(\tau)$是一个特征值为零的路径, 并且依赖于$bounce$发生的位置. 那么之间的讨论是有问题的, 正确的表达式是
$$
\int \mathrm d\tau_1 Ke^{-S_0} = \frac{\int_{x_c}\mathcal D\delta x e^{-S}}{\int_{x=x_0}\mathcal D\delta x e^{-S}},
$$
需要积分掉bounce在时间轴上出现的位置. 现在来仔细地讨论这个表达式: 首先给出$-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_c)$的第$n$个归一化的特征向量是$x_n$, 那么有$\delta x = \sum_n c_n x_n$, 我们可以定义如下的截断的配分函数
$$\begin{aligned}
Z_N(x_c) \equiv & A_N \int \prod_1^N \frac{\mathrm dc_n}{\sqrt{2\pi}} e^{-\int \mathrm d\tau \delta x \frac{1}{2}\left[-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_c(\tau))\right]\delta x} \\
= & A_N \left(\det_N\left(-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_c(\tau))\right)\right)^{-1/2}.
\end{aligned}$$
这里$\det_N$表示前$n$个特征值的乘积, 取$N\rightarrow \infty$就得到真正的配分函数. 由于零模$x_1$的存在, 上式需要重写为
$$
Z_N(x_c) = A_N\int \frac{\mathrm dc_1}{\sqrt{2\pi}}\left(\det'_N\left(-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_c(\tau))\right)\right),
$$
$\det'$表示不计入零特征值. 对$c_1$表示零模的自由度, 实际上就是$\tau_1$, 表示bounce发生的时间, $\mathrm d\tau_1 = \frac{\mathrm dc_1}{\sqrt{S_0/m}}$, 这一点可以按如下推导看出,
$$
\frac{m}{2}\frac{\mathrm d}{\mathrm d\tau}(\dot{x_c})^2 = \frac{\mathrm d}{\mathrm d\tau}V(x_c),
$$
如果$V(x_0) = 0$, 就有$\frac{m}{2}\dot{x_c}^2 = V(x_c)$. 计算一个bounce导致的作用量是
$$
S_0 = \int \mathrm d\tau \left[\frac{1}{2}m\dot{x_c}^2 + V(x_c)\right] = \int \mathrm d\tau m\dot{x_c}^2.
$$
由此我们得到归一化的零模是
$$
x_1(\tau) = \frac{\dot{x_c}(\tau)}{\sqrt{S_0/m}}.
$$
那么现在在$x_c$附近一个$\delta x = c_1x_1$的扰动, 实际上是相当于把$x_c(\tau)$的时间平移$\mathrm d\tau = \frac{c_1}{\sqrt{S_0/m}}$. 现在有
$$
Z_N(x_c) = A_N\int \mathrm d\tau_1 \sqrt{\frac{S_0}{2\pi m}}\left(\det'_N\left(-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_c(\tau))\right)\right)^{-1/2}.
$$
类似地可以写下
$$
Z_N(x_0) = A_N\left(\det_N\left(-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_0)\right)\right)^{-1/2}.
$$
现在得到
$$
\int \mathrm d\tau K = \lim_{N\rightarrow\infty}\frac{Z_N(x_c)}{Z_N(x_0)},
$$
$$
K = \sqrt{\frac{S_0}{2\pi m}}\left(\frac{\det\left(-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_0)\right)}{\det'\left(-m\frac{\mathrm d^2}{\mathrm d\tau^2} + V''(x_c)\right)}\right)^{1/2}.
$$
分子和分母相差一个特征值给出了$K$的量纲和频率相同. 分子上的矩阵的特征值都是正的, 分母上的算符, 我们已知它有一个有一个node的零模, 那么一定有一个唯一的负特征值没有node, 这导致$K$是虚数.

我们上一节讨论的隧穿也可以用类似的方法处理, 但这种情况下$x_c(t)$没有node, 所以没有一个更小负特征值, $K$是实数. 

### Quantum theory of friction

摩擦是一种耗散, 我们需要考虑一个开放系统来描述这个现象. 考虑下面的系统
$$
Z = \mathrm{const}\times \int \mathcal D[x(t)] \mathcal D[h_i(t)]
\exp\left[i\int \mathrm dt \left(
    \frac{1}{2}m\dot{x}^2 + \sum_i\left(\frac{1}{2}\dot{h_i}^2 - \frac{1}{2}\left(\Omega_i h_i + g_i x\right)^2\right)
\right)\right].
$$
这描述了一个和环境谐振子耦合的谐振子. 如果这个系统有平移对阵性的话, 我们可以积掉$h_i$的自由度,
$$
Z = \mathrm{const}\times \int \mathcal D[x(t)]\exp\left[
    i\int \mathrm dt \frac{m}{2}\dot{x}^2 + i \int \mathrm dt \mathrm dt'
    \frac{1}{4}G_{os}(t - t')(x(t) - x(t'))^2.
\right]
$$
这里的$G_{os}$应该是按照耦合系数的平方加权,
$$\begin{aligned}
G_{os}(t - t') = & \sum_i \Omega_i^2 g_i^2 (-i) \langle h_i(t)h_i(0) \rangle \\
= & -i \sum_i \frac{g_i^2 \Omega_i}{2}e^{-i|t - t'|\Omega_i} \\
= & -i \int_0^\infty \mathrm d\Omega n(\Omega) \frac{\Omega g^2(\Omega)}{2}e^{-i|t - t'|\Omega}.
\end{aligned}$$
这里$n(\Omega) = \sum_i \delta(\Omega - \Omega_i)$是态密度, $g^2(\Omega) = \sum_i g_i^2 \delta(\Omega - \Omega_i) / \sum_i \delta(\Omega - \Omega_i)$.

上面我们给出的有效理论可以给出运动方程, 这种有两个时间的运动方程之前没有处理过, 所以写得详细一点, 对这个作用量变分可以得到(过程中涉及一次交换$t$和$t'$)
$$
m\ddot{x} = \int \mathrm dt' G_{os}(t - t')(x(t) - x(t')).
$$
右边第一项积分是$G_{os}(\omega)$, 第二项是$G_{os}(t)$和$x(t)$的卷积, F.T.得到
$$
-\omega^2 m x_\omega = -(G_{os}(\omega) - G_{os}(0))x_\omega.
$$
这是一个描述了阻尼的系统的运动方程,
$$\begin{aligned}
-\omega^2 m^* x_\omega = & - (-i\omega)\gamma x_\omega,\\
m* = m - \frac{\mathrm{Re}(G_{os}(\omega) - G_{os}(0))}{\omega^2}, \ \ \ & \gamma = -\frac{\mathrm{Im}G_{os}(\omega)}{\omega}. 
\end{aligned}$$

上面描述的理论有一个问题: 如果$\mathrm{Im}G_{os}(\omega) < 0$, 那么$\omega > 0$时$\gamma > 0$, 但$\omega < 0$时$\gamma < 0$, 这时不合理的. 注意到在我们最开始的理论是满足时间反演不变的, 如果$\omega > 0$对应了衰减, 那$\omega < 0$就对应衰减的反过程.

现在我们希望能找到一个破环时间反演的形式. 在这个系统中, $t = -\infty$的态$|0_-\rangle$和$t = \infty$的态$|0_+\rangle$是正交的, 粒子被环境减速, 环境部分被激发到高能的态上. 这样我们计算$\langle 0 | U(\infty, -\infty) | 0 \rangle$是零, 只能用来描述这种耗散系统的平衡性质. 一种改进的办法是考虑Schwinger-Keldysh形式, 一个封闭路径积分$Z_{\text{close}} = \langle 0 |U(-\infty, \infty)U(\infty, -\infty)| 0 \rangle$.

或者利用我们之前说的, 把运动方程中的时序关联函数换成响应函数就可以, 利用$\mathrm{Im}D(\omega) = \mathrm{sgn}(\omega)\mathrm{Im}R(\omega)$, 我们就可以得到合法的阻尼系数
$$
\gamma = \frac{\pi}{2}n(|\omega|)g^2(|\omega|).
$$

实际系统中$\Omega$的频率应该是截断的, 如果选取$n(\Omega)g^2(\Omega) = n_0 g_0 e^{-\Omega^2/\Omega_0^2}$, 那么系统的运动由如下作用量描述
$$
S = \int \mathrm dt \frac{m}{2}\dot{x}^2
+i \int \mathrm dt \mathrm dt' \frac{\gamma(x(t) - x(t'))^2}{4\pi(t - t')^2}.
$$

### Quantum theory of an RCL circuit

如果引入$\hat{q}|q\rangle = q|q\rangle$, 电容的Hamiltonian是$\frac{\hat{q}^2}{2C}$, 如果把$\hat{q}$对应动量, 那对应的Lagrangian是$\frac{1}{2}C\dot{x}^2$. 如果考虑一个CL电路, 总的Lagrangian是
$$
L_{CL} = \frac{C}{2}\dot{x}^2 - \frac{1}{2L}x^2,
$$
给出运动方程
$$
C\frac{\mathrm d^2 x}{\mathrm dt^2} = -\frac{x}{L}.
$$
我们现在可以使用一组共轭的变量$[\hat{q}, \hat{x}] = i$, 写下CL电路形如谐振子的Hamiltonian,
$$
H = \frac{1}{2C}\hat{q}^2 + \frac{1}{2L}\hat{x}^2.
$$
如果考虑并联一个电阻, 实际上相当于阻尼, 运动方程变成
$$
C\frac{\mathrm d^2 x}{\mathrm dt^2} = -\frac{x}{L} - \frac{1}{R}\frac{\mathrm dx}{\mathrm dt}.
$$
那么我们可以使用下面的作用量来描述这个并联RLC电路
$$
S_{\text{RLC}} = \int \mathrm dt \left(\frac{1}{2}C\dot{x}^2 - \frac{1}{2L}x^2\right)
+i\int \mathrm dt\mathrm dt' \frac{(x(t) - x(t'))^2}{4\pi R(t - t')^2}.
$$
如果要考虑电荷的量子化, $q = e^* \times \text{integer}$, 因为我们说电量对应于动量, 动量的量子化表明$x$是周期边界的, 周期是$\frac{2\pi}{e^*}$. 这时我们需要把上面的作用量周期化, 最简单的做法是
$$
S_{\text{RLC}} = \int \mathrm dt \left(\frac{1}{2}C\dot{x}^2 - \frac{1 - \cos(e^* x)}{Le^{*2}}\right)
+i\int \mathrm dt \mathrm dt' \frac{\sin^2(\frac{e^*}{2}(x(t) - x(t')))}{\pi R e^{*2}(t - t')^2}.
$$
在$e^*\rightarrow 0$的极限下回到之前没有周期化的作用量.

### Relationship between dissipation and fluctuation

考虑一个经典的涨落$x(t)$, 定义它的总功率是
$$
P_{\text{tot}} = \int_0^\infty \mathrm dt |x(t)|^2 / t_\infty = 2\int_0^\infty \frac{\mathrm d\omega}{2\pi}x_{-\omega}x_\omega / t_\infty.
$$
$x_{-\omega}x_\omega / t_\infty$是功率谱. 那么对于量子涨落, 它的功率谱被定义为
$$
P(\omega) = 2\langle x_{-\omega}x_\omega \rangle / t_\infty = -2\mathrm{Im}G_\omega.
$$
利用$\mathrm{Im}G(\omega) = \frac{\mathrm{Im}D(\omega)}{\tanh(\beta\omega / 2)}$, 可以从响应函数得到功率谱.

考虑一个带有阻尼的系统
$$
m\ddot{x} = - K x - \gamma \dot{x} + f(t).
$$
这个系统的解可以写成
$$
x(t) = - \frac{1}{-m \frac{\mathrm d^2}{\mathrm dt^2} - \gamma \frac{\mathrm d}{\mathrm dt} - K}f.
$$
这个解可以看成是对于$\delta H = -f(t)x$的响应, $x(t) = \int \mathrm dt' D(t - t')f(t) \equiv -Df$. 这样有
$$
D = \frac{1}{-m \frac{\mathrm d^2}{\mathrm dt^2} - \gamma \frac{\mathrm d}{\mathrm dt} - K}.
$$
$D$描述了耗散, $G$描述了涨落, 根据之前关联函数之间的关系, 我们把这两种现象联系在一起. 此外由于$D$对温度没有依赖, 所以
$$
P^V(\omega) = \frac{1}{\tanh(\hbar \omega/ 2T)}P_0^V(\omega).
$$
和经典涨落的谱之间有如下关系, 对于简谐系统都是适用的,
$$
P^V(\omega) = \frac{\hbar \omega}{2T\tanh(\hbar \omega / 2T)}.
$$

### Path integral description of a random differential equation

在之前我们考虑的带有阻尼的运动方程中, 如果取$f = 0$, 在足够长时间之后, $x=0$. 但是因为有阻尼的存在, 实际上我们需要考虑系统的涨落, 一种处理方式是考虑一个随机分布的$f(t)$. 为了验证这种假设的合理性, 我们计算平均关联函数
$$
\langle x(t_b)x(t_a) \rangle = \int \mathcal D[f(t)] \mathcal D[x(t)]
x(t_b)x(t_a) P[f(t)] \delta [x(t) - x^f(f)],
$$
其中$x = \mathcal K^{-1}f$是在$f(t)$下的运动方程, 因为$\mathcal K$不依赖于$f$, 我们有
$$
\delta(x(t) - x^f(t)) \propto \delta(\mathcal K x(t) - f(t)).
$$
这个关联函数可以被重写成
$$\begin{aligned}
\langle x(t_b)x(t_a) \rangle = & \frac{\int \mathcal D[f(t)] \mathcal D[x(t)]
x(t_b)x(t_a) P[f(t)] \delta(\mathcal K x(t) - f(t))}{\int \mathcal D[f(t)] \mathcal D[x(t)] P[f(t)] \delta(\mathcal K x(t) - f(t))} \\
= & \frac{\int \mathcal D[f(t)] \mathcal D[x(t)] \mathcal D[\lambda(t)]
x(t_b)x(t_a) P[f(t)] e^{i\int \lambda[\mathcal K x - f]}}{\int \mathcal D[f(t)] \mathcal D[x(t)] \mathcal D[\lambda(t)] P[f(t)] e^{i\int \lambda[\mathcal K x - f]}}.
\end{aligned}$$
通过引入一个新的场, 我们把这个(热)平均值写成了路径积分的形式. 如果$f(t)$的分布是Gaussian的,
$$\begin{gathered}
P[f(t)] \propto e^{-\frac{1}{2}\int f\mathcal V f},\\
\int f\mathcal V f = \int \mathrm dt\mathrm dt' f(t')\mathcal V(t, t')f(t),
\end{gathered}$$
我们可以积掉这个路径积分
$$\begin{aligned}
\langle x(t_b)x(t_a) \rangle = & \frac{\mathcal D[x(t)]\mathcal D[\lambda(t)]
x(t_b)x(t_a)e^{\int i\lambda \mathcal K x - \frac{1}{2}\lambda \mathcal V^{-1} \lambda}}
{\mathcal D[x(t)]\mathcal D[\lambda(t)]
e^{\int i\lambda \mathcal K x - \frac{1}{2}\lambda \mathcal V^{-1} \lambda}} \\
= & \frac{\mathcal D[x(t)] x(t_b)x(t_a) e^{-\int \frac{1}{2}x\mathcal K^T \mathcal V \mathcal K x}}
{\mathcal D[x(t)] e^{-\int \frac{1}{2}x\mathcal K^T \mathcal V \mathcal K x}}\\
= & (\mathcal K^T\mathcal V \mathcal K)^{-1}(t_b - t_a).
\end{aligned}$$
这里$\mathcal K^T\mathcal V \mathcal K$的逆就是$\mathcal K^T\mathcal V \mathcal K(t)\mathcal G(t - t') = \delta(t - t')$的解. 由此也可以看出$\langle x(t_b)x(t_a) \rangle = \langle x(t_a)x(t_b) \rangle$, 这样它的F.T.就是实的并且等于一半的功率谱. 为了产生合适的$x$的涨落, 要求
$$
\mathcal K^{T} \mathcal V \mathcal K = \frac{\tanh(\omega \hbar / 2T)[(-m\omega^2 + K)^2 + \omega^2\gamma^2]}{\gamma \omega \hbar},
$$
或者说
$$
\mathcal V = \frac{\tanh(\omega \hbar / 2T)}{\gamma\omega\hbar}.
$$
现在我们成功地用一个经典随机方程模拟了量子涨落.