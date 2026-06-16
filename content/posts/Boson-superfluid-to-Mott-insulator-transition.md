---
title: Boson superfluid to Mott insulator transition
date: '2025-07-17T18:58:04+08:00'
categories:
- 多体系统的量子场论
---



A note for Sec 3.6 for 文小刚's *多体系统的量子场论*.

---

一个玻色超流系统的低能行为可以用XY模型来描述. 零温下的$1 + 1$-D量子XY模型, 可以被一个$2-$D的XY模型描述(如果取$v = 1$), $S = \int \mathrm d^2x \chi (\partial \theta)^2$. 在虚时下的vortices可以看作是在实时下的一些instantons, 如果$\chi < \pi / 2$, 那么这些instantons (vortices)会破坏系统的长程序, 这意味这系统会打开一个能隙. 但是上面的讨论并不符合事实, 对于一个超流体来说, 应该总是有无能隙的密度波的激发才对.

为了讨论这个问题, 先考虑在超流体中的两种激发, 局域激发和全局激发(粒子数的变动, Galileo boost). 以自由玻色子为例, 基态是$| k_1, k_2, \cdots, k_n \rangle = |0, 0, \cdots, 0\rangle$, 如果把其中一些$k$的值变成非零值, 这就是一个局域激发; 如果在其中添加一些或者移除一些玻色子, 就是全局激发, 另一种全局激发是让所有$k$偏离一点, 称作Galileo boost. 一种Galileo boost的方法就是把波函数从$\varphi(x) = \varphi_0$变成$\varphi(x) = e^{i2\pi nx/L}\varphi_0$.

最小的Galileo boost就是按$k = 2\pi/L$平移所有的$k$, 这会给出一个总的动量是$K_1 = 2\pi N / L = 2\pi \rho$, 总的能量是$E_1 = K_1^2 / 2mN$. 能看出一个Galileo boost对于动量的贡献要比对于能量的贡献显著很多, 说明Galileo boost并不是声波的起源. 那么这个系统的谱就是在不同的Galileo boost附近的声波所贡献的.

对于低能的XY模型来说, 
$$
L_{XY} = \frac{\chi}{2}\dot{\theta}^2 - \frac{\rho}{2m}(\partial_x \theta)^2,
$$
我们想知道这个模型会不会给出类似的谱. 首先展开
$$
\theta(x, t) = \theta_0(t) + n \frac{2\pi x}{L} + \sum_{k \neq 0} \theta_k L^{-1/2}e^{ikx},
$$
第一项是一个$n$-vortex, 第二项是在周围的扰动. 这样作用量成为
$$
S_{\text{XY}} = \frac{\chi L}{2}\dot{\theta}_0^2 - \frac{K_n^2}{2mN} + \sum_{k>0}\left[
    \chi \dot{\theta}_k^\dagger \dot{\theta}_k - \frac{\rho k^2}{2m}\theta_k^\dagger \theta_k
\right].
$$
在将一个玻色系统有效化成XY模型时, 注意到$\dot{\theta}_0$描述了玻色子粒子数的变化. 此外, $(\theta_k, \theta_{-k})$描述了对应于二维声波的谐振子. 一个在$(x, t)$处的vortex对应了一个算符$O_v(x, t)$, 在$\theta(x, t)$的展开中, 它以$n\frac{2\pi x}{L}$的形式出现, 是一个Galileo boost. 那么vortex的出现, 应该对应于一个Galileo boost的效果, 也就是说, $O_v(x, t)$会把一个在$k = 0$的态映射到$k = 2\pi \rho$的态.

在虚时下考虑, 这样一个系统的配分函数就是
$$
Z = Z_0 \sum_n \frac{1}{n!n!} \int \prod_{i = 1}^{2n} \mathrm d^2 \bm r_i
K^{2n}e^{i2\pi \rho}e^{i2\pi \rho\sum_j q_j x_j}
e^{\sum_{i<j} q_i q_j 2\pi \eta \ln \frac{|x_i - x_j|}{l}}.
$$
$Z_0$是系统不考虑vortex时的配分函数. 这里多出的额外的一项$i2\pi \rho \sum_j q_j x_j$表示了vortices所携带的动量, 来源于计算XY模型时的Berry相. 这个相位因子限制了vortices应该是禁闭的, 所以这个系统不会出现涡旋的等离子体, 总是处在超流相.

如果我们引入一个周期势, 其周期和玻色子的平均间距$a = 1/\rho$一致, 这个周期势就会和上面的相位干涉, 使得这个相位产生非零的平均值. 这时系统可以解禁闭, 并且允许出现KT相变. 当$\chi v > 2/\pi$时有无能隙的激发, 并且有着准长程序, 当$\chi c < 2/\pi$的时候出现一个能隙, 玻色系统构成一个Mott绝缘体.