---
title: RG analysis of the nonlinear sigma model
date: '2025-09-09T09:28:48+08:00'
categories:
- 多体系统的量子场论
featured_image: /images/56e09d7bd5b247b19b52.png
---



A note for Chap 6.4 of Alexander Altland & Ben Simons' *Condensed Matter Field Theory*.

---

如果有一个多分量的场, 被限制在非线性的约束上, 就被称作是非线性$\sigma$模型(nonlinear $\sigma$-model). 这些约束一般反应了在相变点附近连续对称性的破缺. 接下来我们希望在低临界维度$d = 2$附近, 使用RG分析可能发生的对称性破缺.

考虑如下模型
$$\begin{gathered}
\mathcal Z = \int \mathcal Dg e^{-S[g]},\\
S[g] = \frac{1}{\lambda}\int \mathrm d^dr \mathrm{Tr}(\nabla g \nabla g^{-1}),
\end{gathered}$$
其中$g\in G$, 而$G$是某个紧致的李群(这使得我们可以定义Haar测度).

在临界维度$d = 2$以及其之下, Goldstone模式的涨落很大, 在临界维度之上则较小. 在我们的模型中, 涨落的相对大小通过参数$\lambda$控制. $\lambda \rightarrow 0$对应于弱耦合的情况, 涨落较小, $\lambda \rightarrow \infty$对应于强耦合, 几乎所有流形上的$g$均匀地贡献了这个配分函数, 表示最大程度的涨落. 我们希望能理解$d_c = 2$时在这两种情况之间的相变, 并且拓展到$d = 2 + \epsilon$.

## Field integrals over groups

如果涨落比较小, 一种常用的处理是使用生成元来表示群元素, 称作指数表示(exponential representation), 即$g = \exp(W)$, $W = i\sum^a \pi^a T_a$, $T_a$是厄米的生成元. 这样我们就把对于群的积分变成了对于坐标$\pi^a$的积分. 不过考虑到Haar测度, 我们也可以不在单位元附近展开, 而是使用$g = h\exp (W)$. 在我们的RG中, 我们往往使用一个慢变的场附近的展开($h = g_s$).

这些生成元之间可以定义内积$\langle W | W' \rangle \equiv \mathrm{Tr}(WW')$, 我们可以选择这些生成元之间是正交的, 并且通过$\langle T^a | T^b \rangle = c\delta^{ab}$归一化. 对于$U(N)$, $SU(N)$和$O(N)$, $c$分别通常取$1/2$, $1/2$, $1$.

现在我们把$g$按$W$展开, $g = 1 + W + W^2 / 2 + \cdots$, 那么对应地得到$S = \sum_n S^{(n)}$. 其中二阶(最低阶)单独拿出来是
$$\begin{aligned}
S^{(2)}[W] = & -\frac{1}{\lambda} \int \mathrm d^d r \mathrm{Tr}(\nabla W \nabla W) \\
= & \frac{1}{\lambda} \int \mathrm d^d r \nabla\pi^a \nabla \pi^b \mathrm{Tr}(T^a T^b) \\
= & \frac{1}{\lambda} \int \mathrm d^d r \nabla \pi^a \nabla \pi^a \\
= & \frac{1}{2}\int (\mathrm dq)\pi^a_p \Pi^{-1}_{p} \pi^a_{-p},
\end{aligned}$$
其中$\Pi_p = \lambda / 2p^2$表示场$\pi^a$的传播子.

我们可能需要计算一些形如$\langle \mathrm{Tr}(F(W)) \mathrm{Tr}(G(W)) \rangle$的量, 这里$\langle \cdots \rangle = \mathcal N \int \mathcal D \pi \exp(-S^{(2)}[\pi])(\cdots).$ 首先我们为了方便积分的计算需要把Haar测度变成对应$\pi$的测度, $\mathrm d_\mu g \rightarrow \prod_a\mathrm d\pi^a J(\pi)$. 对于指数表示$g \rightarrow \exp(\pi^a T^a)$来说, $J(\pi) = 1 + \mathcal O(\pi^4)$. 这样对于单圈积分来说, 可以不用考虑这个Jacobian. 此外我们需要使用一些生成元的完备性关系:
$$\begin{gathered}
\sum_{a = 1}^{N^2} T^{a}_{ij}T^a_{kl} = \frac{1}{2}\delta_{il}\delta_{jk}, \quad U(N),\\
\sum_{a = 1}^{N^2 - 1} T^{a}_{ij}T^a_{kl} = \frac{1}{2}\delta_{il}\delta_{jk} - \frac{1}{2N}\delta_{ij}\delta_{kl}, \quad SU(N),\\
\sum_{a = 1}^{N(N - 1)/2} T^{a}_{ij}T^a_{kl} = \delta_{il}\delta_{jk} - \delta_{ij}\delta_{kl}, \quad O(N).
\end{gathered}$$

现在作为一个例子, 可以计算对于$G = O(N)$, 
$$\begin{aligned}
& \langle \mathrm{Tr}(AW_p)\mathrm{Tr}(A'W_{p'})\rangle \\
= & - \langle \pi^a_{p}\pi^{a'}_{p'} \rangle \mathrm{Tr}(AT^a)\mathrm{Tr}(A'T^{a'}) \\
= & - \delta_{p, -p'}\Pi_p \mathrm{Tr}(AT^a)\mathrm{Tr}(A'T^a) \\
= & - \delta_{p, -p'}\Pi_p(\mathrm{Tr}(AA') - \mathrm{Tr}(AA'^T)).
\end{aligned}$$

## One-loop expansion

**Step I**: 首先把场的高能和低能部分区分开, 定义$g(r) = g_s(r)g_f(r)$, 动量的范围被确定在$[0, \Lambda b^{-1}]$和$[\Lambda b^{-1}, \Lambda]$内. 接下来可以作用量也分开:
$$
S[g_sg_f] = S[g_s] + S[g_f] + S[g_s, g_f].
$$
前两项的形式和$S[g]$是相同的, 最后一项的形式是
$$
S[g_s, g_f] = \frac{2}{\lambda}\int \mathrm d^d r \mathrm{Tr}\left(
    g_s^{-1}\nabla g_s g_f \nabla g_s^{-1}
\right).
$$

**Step II**: 接下来需要积分掉$g_f$的自由度. 按照$g_f$的生成元展开成$g_f = e^{W}$. 总的来说, 我们需要考虑的作用量形式总是$\int \mathrm{Tr} (XW^n)$, 其中$X$完全由慢场的自由度表示. 考虑到动量守恒, $n = 1$对应的积分一定是零. 按二阶来展开$g_f = 1 + W + W^2 / 2$就有:
$$
S[g_f, W] = \frac{1}{\lambda} \int \mathrm d^d r \mathrm{Tr}(\Phi_\mu[\nabla_\mu W, W])
= - \frac{2i}{\lambda}\int(\mathrm dq)(\mathrm dp) p_\mu \mathrm{Tr}(\Phi_{\mu, -q}W_pW_{-p}),
$$
其中$\Phi_\mu = g_s^{-1}\partial_\mu g_s$, 并且考虑了$p + q \sim p$.

我们还需要把$e^{S}$按阶展开, 但是考虑到每个$S$中都含有一个对于$g_s$的微分, 而二阶以上的微分是不相关的, 所以按阶展开的时候最高只需要考虑到二阶. 只考虑单圈, 现在得到
$$
S[g] \rightarrow S[g_s] - \ln \left(
    1 + \frac{1}{2}\langle S[g_s, W]^2 \rangle_W 
\right) \approx S[g_s] - \frac{1}{2} \langle S[g_s, W]^2 \rangle_W.
$$
继续计算:
$$\begin{gathered}
\langle S[g_s, W]^2 \rangle_W = \int (\mathrm dq)(\mathrm dq') (\mathrm dp)(\mathrm dp')
\langle \mathrm{Tr}(A_{q, p}W_pW_{-p}) \mathrm{Tr}(A_{q', p'}W_{p'}W_{-p'})\rangle_W,
\end{gathered}$$
其中$A_{p, q} = -2i L^d \lambda^{-1} p_\mu \Phi_{\mu, -q}$.
这里这个复杂的平均值, 如果是$O(N)$的场结果是$(N - 2)\Pi_p \Pi_{p + q} \mathrm{Tr}(A_{p, q}(A_{-p, p + q} - A_{-q, -p}))$, 最终可以得到
$$\begin{gathered}
\langle S[g_s, W]^2 \rangle_W \approx C\lambda S[g_s], \\
C = \frac{2(N - 2)\Omega^d(\Lambda^{d - 2} - (\Lambda / b)^{d - 2})}{(2\pi)^2 d (d - 2)}
\overset{d = 2 + \epsilon}{\approx} \frac{(N - 2)\ln b}{2\pi}.
\end{gathered}$$

**Step III**: 最后进行尺度变换, 得到
$$
S[g] \rightarrow \left(1 - \frac{(N - 2)\ln b \lambda}{4\pi}\right)S[g_s] \rightarrow \left(1 - \frac{(N - 2)\ln b \lambda}{4\pi}\right)b^{\epsilon}S[g].
$$

可以看到这个RG过程整体上减小了耦合系数, 
$$
\lambda_r = \left(1 - \frac{(N - 2)\ln b \lambda}{4\pi}\right)^{-1} b^{-\epsilon}\lambda 
\approx \lambda + \lambda\left(\frac{(N - 2)\lambda}{4\pi} - \epsilon\right)\ln b.
$$
现在我们得到对$O(N)$的场的RG方程:
$$
\frac{\mathrm d\lambda}{\mathrm d\ln b} = - \epsilon\lambda + \frac{(N - 2)\lambda^2}{4\pi} + \mathcal O(\lambda^3, \epsilon^2, \lambda^2\epsilon).
$$