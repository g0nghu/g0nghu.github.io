---
title: Superfluidity and superconductivity
date: '2025-07-20T12:39:34+08:00'
categories:
- 多体系统的量子场论
featured_image: /images/83fc097e91f0406a8308.png
---



A note for Sec 3.7 for 文小刚's *多体系统的量子场论*.

---

# Superfluidity and superconductivity

## Coupling to a gauge field and conserved current

一个简单的玻色子模型如下:
$$
L(\varphi) = i\frac{1}{2}(\varphi^* \partial_t \varphi - \varphi \partial_t \varphi^*) -
\frac{1}{2m}\partial_{\bm x}\varphi^* \partial_{\bm x}\varphi + \mu |\varphi|^2 - \frac{V_0}{2}|\varphi|^4.
$$
这个模型有着全局$U(1)$对称性, 在$\varphi \rightarrow \varphi e^{if}$的变换下Lagrangian不变, 当然它并没有一个局域的$U(1)$对称性. 如果令$\varphi \rightarrow \varphi e^{if(\bm x, t)}$, 那么有
$$
L(\varphi e^{if(\bm x, t)}) = i\frac{1}{2}(\varphi^* (\partial_0 + i\partial_0 f)\varphi - \varphi(\partial_0 - i\partial_0 f)\varphi^*) -
\frac{1}{2m}|(\partial_i + i\partial_i f)\varphi|^2 + \mu|\varphi|^2 - \frac{V_0}{2}|\varphi|^4.
$$
如果这些玻色子是带电的, 那么它们可以和一个电磁规范场耦合. 如果我们想要一个满足$U(1)$规范不变的Lagrangian, 就把$\partial_\mu f$替换成$A_\mu$, 得到(当然这样只是一种构造的方式)
$$
L(\varphi, A_\mu) = i\frac{1}{2}(\varphi^* (\partial_0 + iA_0)\varphi - \varphi(\partial_0 - iA_0)\varphi^*) -
\frac{1}{2m}|(\partial_i + iA_i)\varphi|^2 + \mu|\varphi|^2 - \frac{V_0}{2}|\varphi|^4.
$$
这个Lagrangian在如下的规范变换下是不变的:
$$\begin{gathered}
\varphi \rightarrow \tilde{\varphi} = e^{if(\bm x, t)}\varphi, \\
A_\mu \rightarrow \tilde{A}_\mu = A_\mu - \partial_\mu f.
\end{gathered}$$
我们得到的是最简单的满足$U(1)$规范不变性的Lagrangian, 并且说它具有最小耦合(minimal coupling). 如果令$A_\mu \rightarrow A_\mu + g\partial_\nu F_{\mu\nu}$, $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, 就得到另一种满足要求的Lagrangian, 这是因为$F_{\mu\nu}$本身是规范不变的.

上面的Lagrangian实际上只描述了电磁场是如何和玻色系统耦合的, 完整的Lagrangian应该还要把电磁场自身加进去:
$$\begin{aligned}
L(\varphi, A_\mu) = & i\frac{1}{2}(\varphi^* (\partial_0 + iA_0)\varphi - \varphi(\partial_0 - iA_0)\varphi^*) -
\frac{1}{2m}|(\partial_i + iA_i)\varphi|^2 \\ & + 
\mu|\varphi|^2 - \frac{V_0}{2}|\varphi|^4 + 
\frac{1}{8\pi e^2}\left(\frac{1}{c}\bm E^2 - c\bm B^2\right),
\end{aligned}$$
其中$E_i = \partial_0 A_i - \partial_i A_0$, $B_i = \epsilon_{ijk}\partial_j A_k = \frac{1}{2}\epsilon_{ijk}F_{jk}$.

我们知道一个$U(1)$规范理论应该有一个守恒荷, 接下来我们来寻找它. 考虑$\varphi_c(\bm x, t)$给出经典的运动方程, 那么$S(e^{if(\bm x, t)}\varphi_c, A_\mu) = S(\varphi_c, A_\mu) + \mathcal O(f^2)$, 这样就有
$$\begin{aligned}
S(\varphi_c, A_\mu) = & S(\varphi_c, A_\mu - \partial_\mu f) + \mathcal O(f^2)\\
= & S(\varphi_c, A_\mu) + \int \mathrm d^d\bm x\mathrm dt \partial_\mu f J^{\mu}(\varphi_c, A_\mu) + \mathcal O(f^2),
\end{aligned}$$
其中$J^\mu(\varphi, A_\mu) \equiv - \partial_{A_\mu}L(\varphi, A_\mu)$. 这说明如果$\varphi$满足经典的运动方程, 那么有$\int \mathrm d^d\bm x\mathrm dt \partial_\mu f J^{\mu}(\varphi_c, A_\mu) = 0$, 因为$f$是任意的, 这意味这一个守恒方程
$$
\partial_\mu J^\mu = \partial_t \rho + \partial_i J^i = 0.
$$
当然这个守恒方程对于$A_\mu = 0$也是成立的.

对于我们上面给出的玻色子模型来说, 守恒流是
$$\begin{gathered}
J^0 = \rho = \varphi^* \varphi,\\
J^i = - \frac{i}{2m}(\varphi^*\partial_i\varphi - \varphi \partial_i \varphi^*) + A_i |\varphi|^2.
\end{gathered}$$

## Current correlation functions and electromagnetic responses

我们希望知道当系统和一个外界的规范势场耦合的时候的响应. 首先定义
$$\begin{gathered}
j^0 = \rho, \\
j^i = - \frac{i}{2m}(\varphi^* \partial_i \varphi - \varphi \partial_i \varphi^*).
\end{gathered}$$
系统的Lagrangian(没有考虑电磁场自己的部分)可以重新写成, 
$$
L(\varphi, A_\mu) = L(\varphi) - A_0j^0 - A_ij^i - \frac{1}{2m}(A^i)^2\rho.
$$
可以看到规范势和我们关心的流是线性耦合的, 那么根据线性响应理论应该有
$$
\langle J^\mu(\bm x, t) \rangle = \langle j^\mu(\bm x, t) \rangle + (1 - \delta^{\mu 0})A^\mu \langle\rho\rangle = \int \mathrm d^d \bm x \mathrm dt \Pi^{\mu\nu}(\bm x, t; \bm x', t')A_\nu(\bm x', t'),
$$
其中的这些响应函数应该由下式给出:
$$\begin{gathered}
\Pi^{00}(\bm x, t; \bm x', t') = -i \Theta(t - t')\langle [\rho(\bm x, t), \rho(\bm x', t')] \rangle, \\
\Pi^{0i}(\bm x, t; \bm x', t') = -i \Theta(t - t') \langle [\rho(\bm x, t), j^i(\bm x', t')] \rangle, \\
\Pi^{i0}(\bm x, t; \bm x', t') = -i \Theta(t - t') \langle [j^i(\bm x, t), \rho(\bm x', t')] \rangle, \\
\Pi^{ij}(\bm x, t; \bm x', t') = -i \Theta(t - t') \langle [j^i(\bm x, t), j^j(\bm x', t')]\rangle + \delta^{ij}\delta(\bm x - \bm x')\delta(t - t')\langle \rho \rangle.
\end{gathered}$$
如果定义$\pi^{\mu\nu}(\bm x, t;, \bm x', t') = -i \Theta(t - t')\langle [j^\mu(\bm x, t), j^\nu(\bm x', t')] \rangle$, 那么有
$$
\Pi^{\mu\nu} = \pi^{\mu\nu} + \delta^{\mu\nu}(1 - \delta^{\mu 0})(1 - \delta^{\nu 0})\delta(\bm x - \bm x')\delta(t - t')\langle \rho \rangle.
$$
注意到$(\Pi^{\mu\nu}(\bm x, t; \bm x', t'))^* = \Pi^{\nu\mu}(\bm x', t';, \bm x, t)$, 那么$(\Pi^{\mu\nu}_{k_\lambda})^* = \Pi^{\nu\mu}_{-k_\lambda}$. 考虑到守恒流的存在, 这些响应函数之间并不是完全独立的, 应该满足
$$
k_\lambda \Pi^{\mu\nu}_{k_\lambda} = 0.
$$
现在$\Pi$的所有分量都只要从$\Pi^{ij}$确定即可,
$$\begin{gathered}
\Pi^{0i}_{k_\lambda} = (\Pi^{i0}_{-k_\lambda})^\dagger = -\frac{k_j}{\omega}\Pi^{ji}_{k_\lambda}, \\
\Pi^{00}_{k_\lambda} = -\frac{k_j}{\omega}\Pi^{0j}_{\lambda} = \frac{k_i k_j}{\omega^2} \Pi^{ij}_{k_\lambda}.
\end{gathered}$$
如果系统是旋转不变的, 我们还可以进一步写成横向和纵向分量, 
$$
\Pi^{ij}_{k_\lambda} = \frac{k_ik_j}{\bm k^2} \Pi^{||}_{k_\lambda} + (\delta_{ij} - \frac{k_ik_j}{\bm k^2})\Pi^\perp_{k_\lambda}.
$$
$\pi^{ij}$和$\Pi^{ij}$的表达是类似的, 现在
$$\begin{gathered}
\Pi^{0i}_{k_\lambda} = -k_i \Pi^{||}_{k_\lambda}, \\
\Pi^{00}_{k_\lambda} = \frac{\bm k^2}{\omega^2}\Pi^{||}_{k_\lambda}.
\end{gathered}$$
并且有
$$\begin{gathered}
\Pi^{||}_{k_\lambda} = \pi^{||}_{k_\lambda} + \langle \rho \rangle, \\
\Pi^{\perp}_{k_\lambda} = \pi^{\perp}_{k_\lambda} + \langle \rho \rangle.
\end{gathered}$$

**这些响应函数都对应一些重要的物理量**:

当$\omega \rightarrow 0$时, 有$\delta \rho(\bm k) = \Pi^{00}_{0, \bm k}A_0(\bm k)$(这时$\Pi^{00}$比$\Pi^{0i}$要大一个量级), 这给出$-\Pi^{00}_{0, \bm k} = \chi(\bm k)$就是系统的压缩系数. 此外还能得到$\Pi^{||}_{k_\lambda} = -\chi(\bm k)\frac{\omega^2}{\bm k^2}$, 这要在$\omega\rightarrow 0$时, $\pi^{||}_{k_\lambda}$和$\langle \rho \rangle$要相互抵消并以$\omega^2$的方式趋于零($\chi(k)$应该是有限的).

然后考虑$\omega\rightarrow 0$时的$\Pi^{\perp}$的行为, 可以猜测他应该是某种横场的响应函数, 比如和磁化率相关. 如果取$A_0 = 0$, 有
$$\begin{aligned}
i\epsilon^{ijk}k_jM_k = & -j^i = -\Pi^{ij}A_j = - (\delta^{ij}\mathrm k^2 - k^ik^j)A_j\frac{\Pi^{\perp}_{k_\lambda}}{\bm k^2} \\
= & \epsilon^{imn}\epsilon^{nlj}k_mk_l A_j \frac{\Pi^{\perp}_{k_\lambda}}{\bm k^2}
= - i\epsilon^{ijk}k_jB_k\frac{\Pi^{\perp}_{k_\lambda}}{\bm k^2}.
\end{aligned}$$
这样就得到$M_i = -\frac{\Pi^{\perp}_{k_\lambda}}{\bm k^2}B_i$, 那么我们就得到磁化率是$-\Pi^{\perp}_{k_\lambda}/\bm k^2$.

当$|\bm k|\rightarrow \omega$时, 电磁场看作几乎是均匀的, 会在背景上产生一个方向由$A_i$决定波矢由$\bm k$决定的电流:
$$
J^i(\omega) = \lim_{\bm k \rightarrow 0} \frac{\Pi^{ij}}{-i\omega}(-i\omega)A_{j, (\omega, \bm k)}.
$$
当$\bm k\rightarrow 0$时, $\Pi^{ij}_{k_\lambda}$应该是各向同性的, 这要求$\Pi^{||}_{k_\lambda} = \Pi^{\perp}_{k_\lambda}$, 那么根据上面的表达式我们得到各向同性的电导率
$$
\sigma(\omega) = \frac{\Pi^{||}_{\omega, 0}}{-i\omega} = \frac{\Pi^{\perp}_{\omega, 0}}{-i\omega}.
$$
其实部给出了电导率
$$
\mathrm{Re}\sigma(\omega) = -\mathrm{Im}\frac{\Pi^{||}_{\omega, 0}}{\omega} = \mathrm{Im}\frac{\Pi^{\perp}_{\omega, 0}}{\omega},
$$
虚部给出系统的介电常数
$$
\epsilon(\omega) = - \frac{\mathrm{Im}\sigma(\omega)}{\omega} = \mathrm{Re}\frac{\Pi^{||}_{\omega, 0}}{\omega^2} = \mathrm{Re}\frac{\Pi^{\perp}_{\omega, 0}}{\omega^2}.
$$
这样在$\omega \gg |\bm k|$的情况下, 有
$$
\Pi^{||}_{\omega, 0} = \Pi^{\perp}_{\omega, 0} = i\omega \mathrm{Re}\sigma(\omega) + \omega^2\epsilon(\omega).
$$
这个结果可以从另一个角度看待, 由$\partial_{\bm x}\cdot \bm P = -\delta \rho$,
$$
ik_iP^i = -\delta \rho = - \Pi^{00}A_0 = -\frac{\bm k^2}{\omega^2}\Pi^{||}_{k_\lambda}A_0 = i\frac{\Pi^{||}_{k_\lambda}}{\omega^2}k_i E_i,
$$
和上面给出的介电常数是一致的.

现在来考虑对于我们的玻色系统这些响应函数是什么. 这个理论的低能部分应该是一个耦合了规范场的XY模型,
$$
L = \frac{\chi}{2}((\partial_0\theta + A_0)^2 - v^2(\partial_i\theta + A_i)^2).
$$
并且有
$$\begin{gathered}
j^0 = -\chi \partial_0\theta,\\
j^i = \chi v^2 \partial_i \theta.
\end{gathered}$$
那么就有
$$
\pi^{00} = \chi^2(-i\omega)(i\omega)\langle \theta_{\omega, \bm k}\theta_{-\omega, -\bm k}\rangle = \chi \frac{\omega^2}{\omega^2 - v^2 \bm k^2 + i0^+\mathrm{sgn}(\omega)}.
$$
类似地可以得到其他分量, 最终可以得到
$$\begin{gathered}
\Pi^{||} = \chi v^2\left(
    \frac{v^2\bm k^2}{\omega^2 - v^2\bm k^2 + i0^+\mathrm{sgn}(\omega)} + 1
\right),\\
\Pi^{\perp} = \chi v^2.
\end{gathered}$$
那么对于这个系统来说, 压缩系数$-\Pi^{00}_{0, \bm k} = \chi$, 磁化率$-\chi v^2/c\bm k^2$. 电导率是
$$
\mathrm{Re}\sigma(\omega) = \pi \frac{\rho}{m}\delta(\omega).
$$
对于有限频率来说, 电导率是零.

如果我们取Coulomb规范$\partial_{\bm x}\bm A = 0$, 那么电流和规范势之间有着简单的关系, 
$$
\bm J = \Pi^\perp A = \frac{\rho}{m}\bm A.
$$
这就是London方程, 用于唯象地描述超导体的一些性质.

## Superfluidity and finite-temperature effects

首先考虑一个玻色系统, 在低温下, 激发是比较稀疏的, 我们可以假设这些激发之间是没有相互作用的. 如果这个系统被放置在自由空间中, 它在Galileo变换下应该是不变的. 现在有一个在基态上的单激发$(\epsilon, \bm k)$, 现在系统总的能动量是$(E = E_G + \epsilon, \bm P = \bm k)$. 如果对这个系统作一个速度是$\bm v$的boost, 总的动量和能量变成$(E = E_G + \epsilon + \frac{1}{2}Nmv^2 + \bm v \cdot \bm k, \bm P = \bm k + Nm\bm v)$, 这样我们得到在boost之后这个激发所具有的能量是
$$
\epsilon_{\bm v}(\bm k) = \epsilon(\bm k) + \bm v \cdot \bm k.
$$
在有限温度下, 激发态的占据数由玻色分布$n_B(\epsilon)$决定, 这给出系统在有限温度下, boost之后的能动量是
$$\begin{gathered}
\tilde{E} = E_G + \sum_{\bm k} \epsilon_{\bm v}(\bm k)n_B(\epsilon(\bm k)) + \frac{1}{2}Nmv^2,\\
\tilde{\bm P} = \sum_{\bm k}\bm k n_B(\epsilon(\bm k)) + Nm\bm v = Nm\bm v
\end{gathered}$$
这个结果说明系统并没有处在热平衡中, 在热平衡下的系统应该具有的能动量是
$$\begin{gathered}
E_{\bm v} = E_G + \sum_{\bm k}\epsilon_{\bm v}(\bm k)n_B(\epsilon_{\bm v}(\bm k)) + \frac{1}{2}Nmv^2,\\
\bm P_{\bm v} = \sum_{\bm k} \bm k n_B(\epsilon_{\bm v}(\bm k)) + Nm\bm v.
\end{gathered}$$
对于很小的$\bm v$, 可以写成
$$\begin{aligned}
E_{\bm v} & = E_G + \sum_{\bm k}(\epsilon(\bm k) + \bm v\cdot \bm k)n_B(\epsilon(\bm k)) + 
\sum_{\bm k}(\epsilon(\bm k) + \bm v\cdot \bm k)
\left((\bm v \cdot \bm k)n'_B(\epsilon(\bm k)) + \frac{1}{2}(\bm v \cdot \bm k)^2 n''_B(\epsilon(\bm k))\right) + \frac{1}{2}Nmv^2\\
& = E_G + \sum_{\bm k} \epsilon(\bm k)n_B(\epsilon(\bm k)) + \sum_{\bm k}(\bm v\cdot \bm k)^2
\left(n_B'(\epsilon(\bm k)) + \frac{1}{2}\epsilon(\bm k)n_B''(\epsilon(\bm k))\right) + \frac{1}{2}Nmv^2\\
& = E_G - \frac{1}{2}\mathcal Vm\rho_n v^2 + \frac{1}{2d}v^2 \sum_{\bm k}k^2\frac{\mathrm d}{\mathrm d\epsilon(\bm k)}[\epsilon(\bm k)n_B'(\epsilon(\bm k))] + \frac{1}{2}Nmv^2\\
& = E_G + \frac{1}{2}\left(Nm - \mathcal V(\rho_n m + \delta \rho_n m)\right)v^2,
\end{aligned}$$
其中
$$\begin{gathered}
\rho_n = -\frac{1}{md}\int \frac{\mathrm d^d \bm k}{(2\pi)^d}k^2n_B'(\epsilon(\bm k)),\\
\delta \rho_n = - \frac{1}{md}\int\frac{\mathrm d^d \bm k}{(2\pi)^d}k^2\frac{\mathrm d}{\mathrm d\epsilon(\bm k)}(\epsilon(k)n_B'(\epsilon(k))).
\end{gathered}$$
此外动量是
$$
\bm P_{\bm v} = (Nm - \mathcal V\rho_n m)\bm v.
$$
如果我们的激发是线性色散的$\epsilon(\bm k)\propto k$, 那么在温度不高时$\rho_n \propto T^{d+1}$.

上面的计算说明, 如果我们让这些激发进行弛豫, 最终系统的总动量并不会弛豫到零, 在热平衡时, 这些玻色子依旧在运动, 这就是超流性的来源. 在对称性破缺的相中, 玻色子场写成
$$
\varphi = \varphi_0 + \delta \varphi.
$$

当我们boost这个系统的时候, 原本的周期边界条件$\varphi(L) = \varphi(0)$成为$\varphi(L) = e^{imvL}\varphi(0)$, 并且玻色子场的凝聚部分成为$\varphi_0 \rightarrow e^{imvx}\varphi_0$. 但现在系统依然需要遵守周期边界条件, 这要求$mvL \in 2\pi \mathbb Z$. 这就使得在不同$v$的取值中, $\varphi_0$只要不为零, 就不能随意变动. 一种使得$\varphi_0$的相位归零的方式是一些vortex的产生和移动. 这说明即使移动中的超流体有较高的能量, 它也不能轻易弛豫到基态上, 在二者之间有着一个较高的势垒. 当然最终会非常缓慢地停下来.

另一方面, 涨落的部分$\delta\varphi$并没有这些限制, 它的值可以随意地取到零, 所以涨落会轻易地弛豫到平衡.

上面的讨论说明了超流体中有两种组分, 一种对应于凝聚的部分, 这一部分是超流的, 另一部分是对应于激发的正常态. 要保持超流, $\bm v$不能太大, 否则$\epsilon_{\bm v}(\bm k)$的取值可能成为负的, 导致不稳定性, 从而破坏超流. 临界速度是$v_c = \min(\epsilon(\bm k)/k)$.对于自由玻色子来说, $v_c = 0$, 尽管这个系统有长程序, 也不构成超流体.

我们可以定义系统的超流密度是
$$
\rho_s = \frac{\bm P_{\bm v}}{\mathcal V m\bm v} = \rho - \rho_n.
$$
如果这些玻色子是带电的, 并且和一个电磁规范场$A_\mu$耦合在仪器, 那么一个twisted但没有场的情况$(\bm A = 0, e^{im\bm v \cdot \bm x}\varphi_0)$和一个untwisted的并且和场耦合在一起的情形$(\bm A = m\bm v, \varphi_0)$是等价的, 在这种情况下, 系统的总动量可以重新写成
$$
\bm j = \frac{\bm P_{\bm v}}{m\mathcal V} = \frac{\rho_s}{m}\bm A.
$$
这就是London方程.

<!-- ## Tunneling and Josephson effects

考虑两个系统$L$和$R$, 都处在超流或者超导态, 中间被一个隧穿算符$I = \varphi_L\varphi_R^\dagger$耦合, 耦合强度是$\Gamma$:
$$
H = H_R + H_L + \Gamma I + \Gamma I^\dagger.
$$
如果有一个电磁规范场, 这个Hamiltonian要重新写成
$$
H = H_R + H_L + \Gamma e^{-ia}I + \Gamma e^{ia}I^\dagger.
$$
这里$a = \int_L^R \bm A\cdot \mathrm d\bm x$. 隧穿流是
$$
j_T = \frac{\partial H}{\partial a} = -i\Gamma(Ie^{-ia} + I^\dagger e^{ia}).
$$
在$A_0 = 0$的规范下, $V = V_L - V_R$满足$a(t) = \int_L^R \bm A\cdot \mathrm d\bm x = Vt$. 把隧穿作为一个微扰, 根据线性响应理论, 有
$$
\langle j_T \rangle(t) = -i\Gamma\int^t \mathrm dt'\langle[j_T(t), e^{-ia(t')}I(t') + h.c.]\rangle + \langle j_T\rangle_0(t).
$$
第二项表示在没有隧穿项时的平均值, 如果 -->

## Anderson-Higgs mechanism

我们的玻色子和规范场耦合在一起之后, 完整的配分函数应该是
$$
Z = \int \mathcal D\varphi \mathcal D A_\mu \exp\left[
    i\int \mathrm dt\mathrm d^d \bm x \left(L(\varphi, A_\mu) + \frac{1}{8\pi e^2}(\bm E^2 - \bm B^2)\right)
\right].
$$
对于经典的运动方程, 如果$\varphi(\bm x, t), A_\mu(\bm x, t)$是一组解, 那么对其作规范变换之后$\tilde{\varphi}(\bm x, t), \tilde{A}_\mu(\bm x, t)$也是一组解, 也就是说, $(\varphi, A_\mu)$到真实的物理情景是多对一的对应的.

在对称性破缺的相中, $|\varphi(\bm x, t)|\neq 0$, 我们可以取规范使得$\varphi$的虚部为零, 把这个结果记作$\phi(\bm x, t)$. 在取定了规范之后, 现在运动方程的解和物理情景是一一对应的. 在这个规范下, $\phi = \varphi_0 + \delta \phi$, 只会有密度的涨落, 没有相位的涨落, 将密度涨落积分后我们得到对应的低能有效理论:
$$
L_{\text{eff}} = \frac{1}{2V_0}(A_0)^2 - \frac{\rho}{2m}(A_i)^2 + \frac{1}{8\pi e^2}(\bm E^2 - \bm B^2).
$$
注意到
$$
\bm E^2 = (\partial_0A_i)^2 + (\partial_i A_0)^2 - 2\partial_i A_0 \partial_0 A_i.
$$
Lagrangian中不包含有$A_0$的时间导数, 所以$A_0$不是动力学的, 积掉$A_0$自由度得到
$$
L_{\text{eff}} = \partial_0 A_h\left(\frac{1}{8\pi e^2}\delta_{ij} + \frac{1}{2}\frac{V_0}{(4\pi e^2)^2}\partial_j\partial_i\right)\partial_0 A_i - \frac{\rho}{2m}A_i^2 - \frac{1}{8\pi e^2}\bm B^2.
$$
引入横纵场
$$
A_i = \hat{k}_iA^{||} + \hat{n}_a A_a^{\perp}.
$$
这里$\hat{k}, \hat{n}_1, \hat{n}_2$构成一组局部正交坐标架. 现在可以把Lagrangian重新写成
$$
L_{\text{eff}} = \frac{1}{8\pi e^2}\left((\partial_0 A_a^\perp)^2 - (\partial_i A_a^\perp)^2\right) -
\frac{\rho}{2m}(A_a^\perp)^2 + \frac{1}{8\pi e^2}\partial_0 A^{||}\left(
    1 + \frac{V_0}{4\pi e^2}(\partial_i)^2
\right)\partial_0 A^{||} - \frac{\rho}{2m}(A^{||})^2.
$$
这三个自由度都有一个相同的能隙$\Delta = e\sqrt{4\pi \rho/m}$. 也就是说, 无能隙的规范自由度和无能隙的Nambu-Goldstone模式的耦合, 会导致能隙的打开, 这一现象称作Anderson-Higgs机制.