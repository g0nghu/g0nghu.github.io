---
title: QOC and optimization problem
date: '2025-09-09T16:59:18+08:00'
categories:
- notes
---



这篇笔记给出了GRAPE算法, 以及如何把这种QCO的算法应用于寻找给定Hamiltonian的基态.

## GRAPE algorithm

考虑一个系统, 其Hamiltonian可以写成如下的形式:
$$
H(t) = H_0 + \sum_{k = 1}^m u_k(t) H_k.
$$
一般来说, $H_0$是这个系统本身的Hamiltonian, 其他的$H_{k > 0}$是实验中加在系统上的控制, 比如说激光, 随时变的参数$u_k(t)$表示了我们如何操控这些外加的相互作用.

QOC (Quantum optimal control)关心的是, 对于上述受参控的系统, 我们如何给出$u_k(t)$的具体形式, 使得一个初始态$\rho_0$可以演化到需求的目标态$C$上.

这个问题可以变分地解决, 为了简单起见, 考虑$\rho_0$和$C$都厄米的情况, 这时我们可以定义fidelity作为优化的目标:
$$
\Phi_0 = \langle C|\rho(T)\rangle = \mathrm{Tr}(C^\dagger \rho(T)).
$$

首先把时间离散化, $\Delta t = T/N$, 在第$j$个$\Delta t$的时间间隔中, 认为$u_k(t)$是不变的, 并记作$u_k(j)$. 现在可以写下在每个$\Delta t$中的时间演化算符, 
$$
U_j = \exp \left[
    -i \Delta t \left( H_0 + \sum_{k = 1}^m u_k(j)H_k \right)
\right].
$$
最后时间演化得到的态就是
$$
\rho(T) = U_N \cdots U_1 \rho_0 U_1^\dagger \cdots U_N^\dagger.
$$
相应的fidelity是
$$
\Phi_0 = \langle C | U_N \cdots U_1 \rho_0 U_1^\dagger \cdots U_N^\dagger \rangle = 
\langle U_{j + 1}^\dagger \cdots U_N^\dagger C U_N \cdots C_{j + 1}^\dagger | U_j \cdots U_1 \rho_0 U_1^\dagger \cdots U_j^\dagger \rangle.
$$
把这个表达式的左右两部分记作$\lambda_j$和$\rho_j$, 分别表示目标态和初始态反向和正向演化到第$j$个时间步的时候的态.

现在考虑把某个控制参数改变一点$u_k(j) \rightarrow u_k(j) + \delta u_k(j)$, fidelity会如何变化, 首先利用$\frac{\mathrm d}{\mathrm d x}\left. e^{A + xB}\right|_{x = 0} = e^A\int_0^1 e^{A\tau}B e^{-A\tau}\mathrm d\tau$, 可以得到$U_j$的变化是
$$\begin{gathered}
\delta U_j = -i \Delta t \bar H_k \delta u_k(j) U_j, \\
\bar H_k \Delta t = \int_0^{\Delta t} U_j(\tau) H_k U_j(-\tau) \mathrm d \tau, \\
U_j(\tau) = \exp\left[-i\tau \left(H_0 + \sum_{k = 1}^m u_k(j)H_k\right)\right].
\end{gathered}$$
不过在$\Delta t$很小的时候, $\bar H_k \approx H_k$, 进一步可以得到fidelity的变化是
$$
\delta\Phi_0 = \langle \lambda_i | (\delta U_j U_j^\dagger \rho_j + \rho_j U_j \delta U_j^\dagger)\rangle = 
-i\Delta t \langle \lambda_j | [H_k, \rho_j]\rangle \delta u_k(j).
$$

最简单的GRAPE (gradient ascent pulse engineering)算法就是根据这个梯度直接进行梯度下降, 直到给出满意的$\Phi_0$. GRAPE还有一些其他的变种, 但是总的想法是不变的, 根据情况可能会选用一些不同的fidelity.

## Direct quantum optimal control

系统的时间演化算符服从$\frac{\partial U}{\partial t} = - i H[\bm u(t)] U$, 上面的QOC问题的另一种形式是
$$\begin{gathered}
\max_{\{\bm u_j\}_{j = 1}^n} \mathcal F(U_n, U_{\mathrm{target}}), \\
\text{subject to} \quad U_n = \prod_{j = 1}^n \exp(-i H(\bm u(j))\Delta t).
\end{gathered}$$

这样的表示意味着Schrodinger方程在这里实际上是提供了我们参数化$U_n$的方式, 这种情况下, 不论在优化过程中$\bm u(j)$的值如何变化, $U_j$都是物理的. 但这种方式把优化空间局限在了服从Schrodinger方程的子空间中, 可能会影响优化的效果, 或者是把结果限制在局部最小值中. 一种改进的做法是考虑把Schrodinger方程作为一个约束, 但并不限制$U_j$的形式:
$$\begin{gathered}
\max_{\{\bm u_j, U_j\}_{j = 1}^n} \mathcal F(U_n, U_{\mathrm{target}}), \\
\text{subject to} \quad U_{j + 1} = \exp(-iH(\bm u(j))\Delta t)U_j.
\end{gathered}$$

在实践中, $U_j$和$\bm u(j)$一起作为待优化的参数, 而把Schrodinger方程作为Lagrange乘子放进目标函数中. 这种做法允许$U_j$出现非物理的跳变, 探索更大的参数空间, 有助于克服局部最小值的限制.

## Optimization for ground state

上面所述的两种算法, 其目的都是为把初始态按照参数化的演化方式, 变成一个预期的态. 另一种常见的情景是, 目标态并不清楚, 比如基态的优化, 我们希望能通过这种参数化的方式给出一个Hamiltonian的基态.

这里介绍一种叫做QOCA的方法, 但其他方法基本也是类似的, 区别主要在于参数化目标态的方式. 如果我们希望求解基态的Hamiltonian是$H_{\mathrm{prob}} = \sum_j H_j$, 在使用QOCA时, 需要引入另一组控制用的drive Hamiltonian $\{H_k\}$. 而目标态参数化成
$$\begin{gathered}
|\psi(\bm \theta, \bm \delta) \rangle = U_{\text{QOCA}}(\bm \theta, \bm \delta)|\psi_0 \rangle, \\
U_{\text{QOCA}}(\bm \theta, \bm \delta) = \prod_d \left(
    \prod_j e^{i\theta_{j, d}H_j} \prod_k e^{i\delta_{k, d}H_k}
\right).
\end{gathered}$$
上式中$d$表示线路深度, $\bm \theta$和$\bm \delta$是希望优化的参数. 现在只要把目标函数设定成能量, 就可以实现基态的求解. 在这种变分拟设下, 初态$|\psi_0\rangle$的选取一般是重要的, 只是在这个QOCA的算法中, 其影响不至于使得算法不收敛.

此外, 我们引入了额外的driving Hamiltonian, 这使得在优化过程中, 目标态不会局限在某个给定的sector中, 这有助于寻找对称性破缺的基态.

## Discussion

根据Ref[2]指出, 想要实现一个任意的unitary, 我们只要少数全局控制Hamiltonian, 那么在上面的拟设中, 是不是可以写下与具体模型无关, 只和系统几何构型以及对称性有关的一些driving Hamiltonian就可以求解基态.

~~Direct optimization相对于GRAPE来说是一个进步, 因为它本身解除了GRAPE对于使用到的$U_j$的限制, 使得目标态可以探索一些非物理的空间.~~

~~但是在基态求解的问题中, 本来就没有这种限制, 如果考虑了破坏对称性的一些driving Hamiltonian的话, 可以近似任何的unitary. 所以Ref[2]给出的新算法, 可能并不能给基态优化在算法上提出一些改进, 但是可以帮助我们写下一些更普适的ansatz.~~

我们可以按照Ref[2]给出的结果, 写下一些比较普适的ansatz, 并按照给出的direct optimization, 不限制$U_j$的形式, 把这部分作为约束(Lagrange乘子)放进目标函数里.

---

References:

1. Optimal control of coupled spin dynamics: design of NMR pulse sequences by gradient ascent algorithms, Journal of Magnetic Resonance 172 (2005) 296–305.
2. Universal Dynamics with Globally Controlled Analog Quantum Simulators, 	arXiv:2508.19075.
3. Quantum-optimal-control-inspired ansatz for variational quantum algorithms, 	arXiv:2008.01098.