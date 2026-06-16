---
title: Measurement Induced Phase Transitions (MIPT)
date: '2026-03-30T09:42:17+08:00'
tags:
- MIPT
- 概要
categories:
- MIPT
featured_image: /images/48e78f53ff8a45ce889d.jpg
---


Ref:
1. B. Skinner, Introduction to random unitary circuits and measurements (lecture notes, 2023)

---

MIPT 是在随机幺正演化的线路上, 以一定的概率$p$对中间线路的结果进行测量. 一般来说, 一个幺正演化会倾向于使得系统中的纠缠增加, 而测量则会即时地把系统投影到一个直积态上从而降低系统的纠缠. 这两种机制之间的竞争使得在某个$p = p_c$的临界概率上, 系统可能会发生一个由体积率到面积率之间纠缠相变.

## Random unitary operators and minimal cut

在接下来的讨论中, 我们会使用 Renyi-$0$ 熵, 其被定义为
$$
S_0 = \log (\text{\# nonzero terms in the Schmidt decomposition of } |\psi\rangle).
$$
尽管这个值对于态的变化并不连续, 但它实际上给其他的 Renyi 熵提供了一个上界和行为上的参考.

一个对于随机幺正线路 (RUC) 的问题是: 为什么研究这个系统? 一个比较普遍的回答是, 通过研究随机幺正线路, 我们希望能获得对于一般系统纠缠增长的普适结论, 即使存在一些特例. 这些对于纠缠增长的了解有助于我们进一步了解热化的发生以及控制计算成本.

### The minimal cut

对于一个 RUC 来说, 一个可能的对于子系统 A, B 的切割 (cut) 按照下图给出, 
![](/images/c162cafbacb446c0badb.png)

这条红线把系统分成两个部分, 一些门的输入和输出暴露在外, 这些暴露在外的腿对应于两个部分之间是如何传递信息, 也就是说, 建立纠缠的. 考虑到每个腿最多可以传递$1$个 bit 的信息, 应该有
$$
S_n \leq N_\text{cut} \times \log 2.
$$
这个关系可以通过更精确的分析得到. 我们把子图 A 中包含的门记作$U_A$, 包含的末态自旋记作$\sigma_A$, 包含的初态自旋记作$\sigma_A'$ (对 B 类似), 被切断的自由度记作$\sigma_\text{shared}$. 有
$$\begin{aligned}
|\psi \rangle = & \sum_{\sigma_A, \sigma_B, \sigma_\text{shared}}a(\sigma_A, \sigma_\text{shared}) |\sigma_A\rangle \otimes b(\sigma_B, \sigma_\text{shared}) |\sigma \rangle \\
 = & \sum_{\sigma_\text{shared}} \left(\sum_{\sigma_A}a(\sigma_A, \sigma_\text{shared})|\sigma_A\rangle\right)\otimes \left(\sum_{\sigma_B}b(\sigma_B, \sigma_\text{shared})|\sigma_B\rangle\right),
\end{aligned}$$
其中$a(\sigma_A, \sigma_\text{shared}) = \langle \sigma_A, \sigma_\text{shared} |U_A| \sigma_A' \rangle$ (对 B 类似). 可以看到这个表达式实际上提供了一种分解的方法, 包含$2^{N_\text{cut}}$个项. 据此我们可以得到上面的约束关系.

如果我们能找到最小的切割, 那么实际上就是确定了$S_0$:
$$
S_n \leq N_\text{min, cut} \times \log 2 = S_0.
$$

### Universality class of KPZ equation

我们的最小切割问题可以被映射成为另一个经典问题 DPRE (directed polymer in a random environment), 大致是把把一个多聚体以最小的能量放置在一个随机势场中. 这些问题都属于 KPZ (Kardar-Parisi-Zhang) 普适类. 现在我们可以确定一些有关$S(x, t)$的一般结果:
1. $S(x, t)$在短时间中线性增长, 最终会饱和到$S(x, t \gg x) \sim x$;
2. $S(x, t)$的统计涨落是 $\delta S \propto t^{1/3}$;
3. 涨落有关联长度$\xi \propto t^{2/3}$.

### One interpretation of KPZ equation

<!-- TODO: one interpretation of KPZ equation -->

### Large-$q$ limit

尽管上面的讨论描述的都是$S_0$, 但一般来说会认为$S_0$可以一定程度上反应$S_n$的行为. 尤其在局域自由度$q\rightarrow \infty$的情况下, $S_0$和其他$S_n$有相同的行为.

考虑一个态$|\psi \rangle$的Schmidt分解, $|\psi = \sum_{i = 1}^q \sqrt{\lambda_i}|i_A\rangle \otimes |i_B\rangle$, $\sum_i \lambda_i = 1$. 因为线路中的门都是随机的, 可以认为直积态在经过门之后所有的$\lambda_i = 0$. 当$q$很大的时候, 可以认为$\lambda_i \sim 1/q$, 那么$\sum_{i = 1}^q \lambda_i^n \sim q^{1 - n}$. 在这种情况下$S_n = \log q = S_0$.

## The measurement-induced entanglement phase transition

在测量频率临界点$p_c$的两端, 出现两个相: 纠缠相和解缠相. 前者赋予一个纯态体积率的熵, 并且不能纯化一个混态; 而后者赋予一个纯态$\mathcal O(1)$量级的熵, 并且在$\mathcal O(1)$时间内可以纯化一个混态.

接下来我们把这个问题等效到渗流问题上, 来更好地理解.

### The post-selection problem

考虑到线路中不但包含了随机的幺正矩阵, 还包括了测量和对应的随机结果 (这些测量结果的分布服从 Born's Rule). 在实验上希望观察到MIPT, 就要求不但要重复运行线路来重建最终的量子态, 还需要额外的运行次数, 来保证线路中每次测量都能获得相同的结果, 这使得要求的测量次数的量级是指数的$\mathcal O(2^{\# \text{ measurement}})$. 这被称作后选择 (post-selection) 问题.

### The minimal cut and mapping to percolation

![](/images/ef5e7101c88049a1b26d.png)

图中展示了在一个包含测量的线路中, 存在切割的一个示例. 当一个切割经过存在测量的位置的时候, 这个腿实际上并不传递信息, 因为通过测量我们已经知道了这个位置的状态, 这使得这条腿在时间上未来和过去并不关联. 这就是测量的存在能降低纠缠的直观解释. 那么现在系统的熵$S_0$依旧可以表示成系统的中的最小切割, 只是那些存在测量的点并不计入切割的长度 (直观的理解是认为它本来就是断的).

这个问题也有对应于经典问题 first passage percolation, 这个问题的普适行为是:
1. $p < p_c$, 线路 (网络) 中存在一些大洞, 大洞的平均尺寸是 $\xi \sim (p_c - p)^{-\nu}$;
2. $p = p_c$, 关联长度$\xi$发散, 可以认为最小割从很小的一些洞中, 穿过一个边寻找更大的洞, 直到离开体系;
3. $p > p_c$, 线路已经破碎, 存在一些各自不连通的尺度约为$\xi \sim (p - p_c)^\nu$的区域, 最小切割离开它初始所在的区域之后就可以自由地离开系统了.

![](/images/fc66d7d5a5bb46b3b2f0.webp)

由此可以到纠缠, 这里先考虑$t \gg L$的情况, $t \ll L$的情况只需要交换$t$和$L$即可. 对于$p < p_c$, 最小割要离开系统需要经过$t / \xi$个大洞, 经过每个大洞会切割一个边. 对于$p < p_c$, 可以认为最小割离开系统需要从一个大洞跳到另一个尺寸倍增的大洞, 这样的变换要经过$\log t$次. 对于$p > p_c$的情况, 最小割线只需要经过第一个联通的区域即可, 所以结果是把$p = p_c$的结果中的$t$换成$\xi$. 最终得到:
$$
S(t, L\rightarrow \infty) \sim \begin{cases} & t \times (p - p_c)^\nu, & p < p_c \\
& \log t, & p = p_c \\
& - \nu \log(p - p_c), & p > p_c
\end{cases}.$$

通过检测纠缠熵如上的行为, 可以判断 MIPT 的发生. 对于$S_0$来说, $p_c = 1/2$, $\nu = 4/3$. 对于其他的$n$, 这些标度还不确定. 

### Mutual information and its classical interpretation

对于一个系统中的两个子区域$a$和$b$, 其互信息 (mutual information) 被定义为
$$
I_n(a, b) = S_n(a) + S_n(b) - S_n(a \cup b).
$$
考虑$a$和$b$距离很远的情况, 从系统中移除$a\cup b$的代价, 和移除$a$, 然后移除$b$的代价应该是相同的, $S(a \cup b) = S(a) + S(b)$. 那么$I_n(a, b) = 0$.

要使得这个量非零, 就必须要求子区域$a$和$b$处在同一个联通的区域中, 也就是说, 距离大概小于$\xi$. 这个解释指出当 MIPT 发生的时候, 会看到 $I_n(a, b)$出现一个峰, 对应$\xi$的发散.

### The entanglement transition as a purification transition

正如一开始所指出的, 实际上上面给出的 MIPT 也描述了线路纯化能力在$p = p_c$处的转变. 值得指出的一点是, 当系统中的测量密集到在某个$t$处, 测量实际上完全切断了线路, 那在这个位置处, 线路中的信息传递被完全破环, 忘记了关于初态的信息, 对于混态作为初态来说, 这意味着纯化的发生. 那么对于任意的$p$来说, 只要时间足够长, 系统总是会纯化. 只是在有限时间内, $p_c$两侧的行为不同.