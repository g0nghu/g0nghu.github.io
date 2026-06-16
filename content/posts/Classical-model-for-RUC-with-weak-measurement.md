---
title: Classical model for RUC with weak measurement
date: '2026-04-03T15:25:25+08:00'
tags:
- MIPT
categories:
- MIPT
featured_image: /images/808d6b104d9044cda88c.jpg
---



Ref:

1. Yimu Bao, Soonwon Choi, & Ehud Altman. Phys. Rev. X 9, 031009 – Published 22 July, 2019.

---

## Weak measurement

最早对于 MIPT 的讨论, 使用的都是投影测量, 一种可能的推广是使用弱测量 (weak measurement), 给每个 qudit 一个 ancilla qudit, 需要测量的时候就作用一个门把系统 qudit 和辅助 qudit 纠缠起来, 在辅助 qudit 上进行测量, 这个测量的强弱取决于施加纠缠的门的参数.

![](/images/13c450e1459e404d8b5f.png)

具体来说, 对于一个 $q$-qudit 来说, 我们引入的辅助 qudit 的维数是 $q + 1$. 这个门的给的纠缠强弱通过参数 $\alpha$ 控制:
$$
\hat R_\alpha = \sum_{i = 1}^q \hat P_i \otimes \mathrm e^{- \mathrm i \alpha \hat X_i},
$$
其中 $\hat P_{i} = | i \rangle_s \langle i |_s$ 表示对于系统 qudit 在 computational basis 上的投影, 而 $\hat X_i = |0\rangle_m \langle i |_m + |i \rangle_m \langle 0 |_m$ 表示在辅助 qudit 上的类 Pauli-$X$ 作用, 所有的辅助 qudit 被初始化到 $|0 \rangle_m$.

当 $\alpha = 0$, $\hat R_{\alpha}$ 并没有把辅助 qudit 和系统 qudit 纠缠起来, 所以相当于没有测量. 当 $\alpha = \pi / 2$, 如果系统 qudit 处在 $|i\rangle_s$, 就把辅助 qudit 投影到 $|i\rangle_m$, 这样一来, 测量辅助 qudit 得到不同态的概率就和系统 qudit 给出的 Born 概率完全相同, 并且测量同时会把系统 qudit 也投影到相同的测量结果上, 这实际上就对应了投影测量.

定量的解释基于如果我们在测量之后给辅助 qudit 作用一个 dephasing 门 $\mathcal N_\phi [\rho] = \sum_i |i\rangle_m \langle i|_m \rho | i\rangle_m \langle i |_m$, 
$$
\mathcal N_\phi [\hat R_\alpha (\rho_\text{in} \otimes |0\rangle_m \langle 0 |_m)\hat R_\alpha^\dagger]
 = (1 - p) \rho_\text{in} \otimes |0\rangle_m \langle 0 |_m + 
 p \sum_i \hat P_i \rho_\text{in} \hat P_i \otimes |i \rangle_m \langle i|_m,
$$
对于系统的约化密度矩阵来说, 总的量子信道和一个概率为 $p = \sin^2 \alpha$ 的投影测量的信道是相同的.

## Observable

希望用于观测 MIPT 发生的物理量是 von Neumann 熵
$$
S[\rho_A] = - \mathrm{Tr}[\rho_A \log \rho_A]
$$
和 Fisher 信息. 前者描述了系统的两个部分 (subregion $A$ 和它的补 $\bar{A}$) 之间的纠缠, 后者表述了当线路的初态发生改变, 线路输出的概率分布会在多大程度上发生改变, 也就是说, 系统传递信息的能力如何. Fisher 信息的定义依赖于所谓的 Kullback-Leibler (KL) divergence (relative entropy)
$$
D_\text{KL}(P_0 || P_\theta) = {\sum_x} P_0(x) \log \left(\frac{P_0(x)}{P_\theta(x)}\right),
$$
Fisher 信息被定义为其二阶导
$$
\mathcal F \equiv \partial_\theta^2 D_\text{KL}(P_0 || P_\theta)|_{\theta = 0}.
$$
这里不使用一阶导的原因是因为 $D_\text{KL}(P_0 || P_\theta) \geq 0$ 并且 $D_\text{KL}(P_0 || P_0) = 0$, 因此一阶导在 $\theta = 0$ 处总是 $0$.

希望使用 Fisher 信息来探测这个纠缠相变的原因是因为 Fisher 信息的获取只需要得到线路最终的概率分布即可, 相比于纠缠熵需要完全确定量子轨迹 (quantum trajectory) 下的多次测量来说, 在实验上的测量要简单很多.

当然在这个问题下, 我们要考虑对所有线路中测量结果的可能性 $\langle\cdot\rangle = \sum_{i_M} p_{i_M}$ 和整个 Haar 矩阵的系综 $\bar \cdot$:
$$\begin{gathered}
\overline{\langle S_A(\mathcal U)\rangle} = \overline{\sum_{i_M}p_{i_M}S[\rho_A(\mathcal U, i_m)]}, \\
D_\text{KL}(P_0||P_\theta) = \overline{\sum_x P_0(x) \log \left( \frac{P_0(x)}{P_\theta(x)}\right)},
\end{gathered}$$
这里 KL divergence 表达式中对 $x$ 的求和涉及线路中所有测量的结果.

### Replica trick

$\mathrm{Tr}(\rho \log \rho)$ 这样的量一般是很难计算的, 常见的处理方法是使用 replica trick: $\mathrm{Tr}(\rho \log \rho) = \lim_{n \rightarrow 1}\frac{\mathrm {\log (\mathrm{Tr}(\rho^n))}}{n - 1}$.

我们在这里计算的 von Neumann 熵还有额外的困难, 来源于我们还需要对可能的 Harr unitary $\mathcal U$ 和所有可能的测量结果 $i_M$ 取平均. 所以处理的第一步是试图去掉对于 $i_M$ 的平均:
$$
\overline{\langle S_A(\mathcal U) \rangle} = \overline{\tilde{S}(A|M)} \equiv \overline{S[\tilde{\rho}_{AM}]} - \overline{S[\tilde{\rho}_{M}]}.
$$
这里的 $\tilde \rho_X  = \mathrm{Tr}_{\bar X} \mathcal N_\phi[\rho]$, 这一步把 $p_{i_M}$ 以密度矩阵的形式也写进表达式中了, 也就避免了对 $i_M$ 求平均. 利用 replica trick 则需要计算:
$$
\tilde S^{(n)}(A | M) \equiv \frac{\log (\overline{\mathrm{Tr}\tilde \rho_{AM}^n}) - \log (\overline{\mathrm{Tr}\tilde \rho_{M}^n})}{1 - n}.
$$

对于 KL divergence 和 Fisher 信息, 使用相同的处理, 要计算的量实际上变成
$$\begin{gathered}
D^{(n)}(P_0 || P_\theta) \equiv \frac{\log (\overline{\mathrm{Tr}(\tilde \rho_{M, 0} \tilde \rho_{M, \theta}^{n - 1})}) - \log\overline{\mathrm{Tr(\tilde \rho_{M, 0}^n)}}}{1 - n}, \\
\mathcal F^{(n)} \equiv \partial_\theta^2 D^{(n)}(P_0 || P_\theta)|_{\theta = 0}.
\end{gathered}$$

## Mapping to spin models

不论是计算 von Neumann 熵还是 Fisher 信息, 都要计算一些矩
$$
\mu_{AM}^{(n)} = \mathrm{Tr}(\tilde \rho_{AM, 1} \tilde \rho_{AM, 2} \cdots \tilde \rho_{AM, n}).
$$
的平均值. 我们希望能将其映射成一个统计模型 $\overline{\mu_{AM}^{(n)}} = \mathcal Z_{AM}^{(n)}$.

### Case of 2-order for von Neumann entropy

我们展示如何处理平均局域纯度 $\overline{\mu_{AM}^{(2)}} = \overline{\mathrm{Tr}(\tilde \rho_{AM}^2)}$. 如果引入 SWAP 算符则有
$$
\mu_{AM}^{(2)} = \mathrm{Tr}\left(
    \left(\mathcal C^{(2)}_A \otimes \mathcal I_B^{(2)} \otimes \mathcal C_M^{(2)}\right)
    \left(\tilde \rho_{ABM} \otimes \tilde \rho_{ABM}\right)
\right),
$$
这里的 $\mathcal C^{(n)}_X$ 是作用在子区域 $A$ 上的 cyclic 置换.

![](/images/2046d3b9b31e4226b423.png)

可以把整个 $\overline{\mu_{AM}}$ 表示成子图 (a) 的形式. 其中 $\mathcal T$ 表示作用在两组 ket 和 bra 上的 $U \otimes U^* \otimes U \otimes U^*$, 对它作 Haar 测度下的平均给出
$$
\overline{T^{2}_{\bm{ab};\bm{cd}}} = \sum_{\sigma, \tau = \pm 1} w_g^{(2)}(\sigma, \tau) \hat\tau_{\bm{ab}} \hat\sigma_{\bm{cd}},
$$
其中 $w_g^{(2)}(\sigma, \tau)$ 是 Weingarten 函数, $\hat \sigma_{\bm{ab}}$ 被定义成
$$
\hat \sigma_{\bm{ab}} = \begin{cases}
\delta_{a_1b_1}\delta_{a_2b_2}, & \text{if } \sigma = +1, \\
\delta_{a_1b_2}\delta_{a_2b_1}, & \text{if } \sigma = -1.
\end{cases}
$$

这个过程如子图 (c) 和 (d) 所示, 现在已经初步在层的每个门的位置处放置了两个格点 $\tau$ 和 $\sigma$, 它们之间通过权重 $w_g^{(2)}(\sigma, \tau)$ 连接. 层与层之间的连接依赖于不同的 $\mathcal T^{(2)}$ 之间的 $\mathcal M^{(2)}$. $\mathcal M^{(2)}$ 实际上是作用在两组 ket 和 bra 上的 $R_{\alpha}^*$ 和两个 dephasing 门 $\mathcal N_\phi$. 这个信道和两边的 $\sigma$ 和 $\tau$ 收缩之后会给出 $w_d(\sigma, \tau)$, 见子图 (f).

注意到所有的 $w$ 对于 $\sigma$ 和 $\tau$ 都是对称的, 只依赖于相对置换 $\tau^{-1} \sigma$.

现在整个"配分函数" (其实不一定是, 因为其中有的项不一定是非负的) 可以写成
$$
\overline{\mu_{AM}^{(2)}} = \sum_{\sigma_r, \tau_r} W_\text{top} W_\text{bottom} \prod_{\langle r, r' \rangle} w^{(2)}(\sigma_r, \tau_{r'}).
$$
上边界最终要和 $\mathcal C^{(2)}_A \otimes \mathcal I_B^{(2)}$ 收缩, 所以对于上边界中 subregion $A$ 中的 $\sigma$ 取 $-1$, 而 subregion $B = \bar A$ 中的 $\sigma$ 取 $+1$. 下边界是系统的初态, 对于 von Neumann 熵的计算来说总有 $W_\text{bottom} = 1$, 而如果是计算 Fisher 信息的话, 如果下边界的置换把 $1$ 置换成其他元素, $W_\text{bottom}$ 取 $|\langle \psi_0| \delta U(\theta) | \psi_0 \rangle|$, 否则取 $1$. 对于这里 $n = 2$ 的情况, 相当于增加了一个在边界上的磁场 $h (1 - \sigma_{x_0, 1})$.

### Description

$\tilde S^{(n)}(A|M)$ 现在可以被看成是在边界上引入一个 domain wall 需要的自由能, 而 $\tilde D^{(n)}_\text{KL}$ 则是在边界引入磁场消耗的自由能, 对应的 $\mathcal F^{(n)}$ 和边界磁化的热力学期望有关.

这个系统的纠缠相变可以通过这个类 Potts ($n = 2$ 就是 Ising 模型) 来解释, 系统处于铁磁相的时候, 引入 domain wall 会导致引入和系统尺寸成正比的能量消耗, 也就是体积律, 而在顺磁相的时候几乎只影响局域, 所以只有一个常数的消耗.

### Classical Ising model

尽管 $w_g^{(2)}(\sigma, \tau)$ 可能小于 $0$, 但可以积掉 $\tau$ 自由度, 变成一个真正的统计模型, 如子图 (c):
$$
\beta \mathcal H = \sum_{\langle r, r' \rangle_d} J_d \sigma_r \sigma_{r'} + \sum_{\langle r, r'\rangle} J_h \sigma_r \sigma_{r'}.
$$
在这个模型中总有 $J_d + J_h \leq 0$, 这个模型是精确可解的, 在
$$
2 \mathrm e^{2J_h} = -2\sinh(2J_d)
$$
处发生铁磁到顺磁的相变.

### Standard Potts model

在 $q \rightarrow \infty$ 时, $J_h \rightarrow 0$. 统计模型变成一个在正方格点上的 Potts 模型, 这个模型也是精确可解的. 进一步的如果取 $n \rightarrow 1$ 的极限, 从 Potts 模型出发可以进一步变成一个 percolation 问题.

## Non-local measurement

如果系统中的弱测量不是局域的, 系统一定在有限时间内被纯化, 也就是说非局域测量会导致这个纠缠相变的消失. 非局域性反映在统计模型中, 就是不作用 dephasing 门, 这导致了统计模型中的置换对称性被破坏, 如果时间足够长, 系统在边界的磁化可以预期总是 $1$, 也就是 Fisher 信息是 $0$, 系统在长时间下末态基本与初态无关. 这种行为可以看作是非局域测量总能破环了通过幺正演化传播的信息, 而局域测量则需要一定强度才能破坏这些已经被传递到周围的信息.