---
title: 有关 MIPT 的研究进展
date: '2026-03-30T14:18:48+08:00'
tags:
- 研究进展
- MIPT
featured_image: /images/1053d9d79aa24752978f.png
---



写这个文档的原因在于在我做毕设的时候, 越来越意识到即使看了很多文章, 学了一些算法, 还是感觉不能声称自己了解这个领域, 尤其是希望做点新东西的时候, 不能很好地确定改用什么模型, 又使用什么指标作为测试.

这里会把读过的一些文献中实际完成的工作 (包括通过计算什么验证了什么结论), 以及它们提到了但是没有解决的问题列出来.

当然文档多数时候是未完成的.

---

### [Measurement-Induced Phase Transitions in the Dynamics of Entanglement](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.9.031009)

Phys. Rev. X 9, 031009 – Published 22 July, 2019

Authors: Brian Skinner, Jonathan Ruhman, and Adam Nahum

已完成:
- 理论和数值上证明了 $S_0$ 和 percolation 问题之间的对应, 数值结果是 1D 的;
- 使用经典 percolation 模拟了 1D 下 $S_0$ 和互信息 $I_0$ 的标度率;
- 使用 MPS 模拟了1D 下 $S_n$ 和 $I_n$ 的标度率;
- 附录中给出了拟合标度率以及经典计算 percolation 问题的方法.

未完成:
- 连续时间演化下的结果;
- 大 $q$ (局域自由度)近似的验证;
- 任何对于高维结果的数值验证;
- 高维情形下的 percolation 问题的解, 对应的 $p_c$ 和 $\nu$;
- 不同 subregion 的纠缠熵.

后续:
- 计算 2D percolation 问题给出的 $p_c$ 和 $\nu$, 也许 Tropical TNs 会有用;
- 连续 1D 时间演化;
- 考虑验证 1D 的大 $q$ 极限, 但不是很有意义;
- 更普遍的 entanglement feature (EF) 的行为, 依旧可以使用经典 percolation 模拟.

### [Theory of the phase transition in random unitary circuits with measurements](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.101.104301)

Phys. Rev. B 101, 104301 – Published 3 March, 2020

Authors: Yimu Bao, Soonwon Choi, and Ehud Altman

已完成:

- 对于每个 qudit 引入了一个 ancilla, 通过对 ancilla 的测量实现对于投影测量的推广;
- 使用 replica trick, 把 von Neumann 熵 $S_1$ 和 Fisher 信息 $\mathcal F$ 映射到一个三角晶格的类 Potts 模型上, 说明了这两个量服从同一个相变, 说明了对混态的纯化和纠缠的增长也共享这个相变, 区别仅在于统计模型的边界不同;
- 建立了统计模型到张量网络的映射;
- 通过 CFT 给出了 $n = 2$ ($n$ 是 replica trick 中使用的副本数) 下任意 $n$ 的相变点和临界指数;
- 在大 $q$ 极限下, 把 $n \geq 2$ 的统计模型映射成方晶格上的标准 Potts 模型, 给出相变点和临界指数;
- 在大 $q$ 极限下, 把 $n \rightarrow 1$ 的关于 von Neumann 熵的模型从标准 Potts 模型出发映射到 percolation 问题上, 给出了 $p_c = 1/2$ 和 $\nu = 4/3$ 的结果;
- 使用类似 MPS 时间演化计算了 $q = 2$的数值结果, 和 Phys. Rev. X 9, 031009 中给出的临界点和临界指数基本相同, 计算量 Renyi-$k$ 对不同 $k$ 服从用一个相变;
- 数值验证了在非局域的测量会破坏相变, 有限时间内一定解缠.

未完成:

- 还没有说明大 $q$ 极限下的结果实际上来源于大 $q$ 极限下 $S_n$ 和 $S_0$ 的行为相同.

后续:

- 设计统计模型的时候引入了对于 Haar random unitary 的平均, 这一步可以和 EF 或者 local scrambled circuit 的理论结合起来.

### [Measurement-induced criticality in random quantum circuits](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.101.104302)

Phys. Rev. B 101, 104302 – Published 3 March, 2020

Authors: Chao-Ming Jian, Yi-Zhuang You, Romain Vasseur, and Andreas W. W. Ludwig

已完成:

- 和上一篇基本相同.

### [Measurement-induced criticality in (2+1)-dimensional hybrid quantum circuits](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.102.014315)

Phys. Rev. B 102, 014315 – Published 30 July, 2020

Authors: Xhek Turkeshi, Rosario Fazio, and Marcello Dalmonte

已完成:

- 使用对于 Clifford 线路和 stabilizer 态的模拟;
- 测试了 2D 下 1-site 和 2-site projector 下的 MIPT, 给出了临界点和临界指数, 说明了这两种相变是同一个普适类;
- 结果和 3D percolation 问题的普适类行为不同.

未完成:

- 没有给出超过 Clifford 线路的情形, 因为对于 stabilizer 态 Renyi-$n$ 熵的值相同, 实际上相当于只测试了 $S_0$;
- 但在 1D 情形下, 不同 $n$ 的临界指数不同, 应该给出不同的, 需要考虑更一般的演化;
- 后来更精确的计算指出仅看临界指数其实和 3D percolation 的结果相同, 这篇文章中不同的结果应该是使用二分纠缠熵不够精确导致的计算错误.

### [Measurement-induced criticality and entanglement clusters: A study of one-dimensional and two-dimensional Clifford circuits](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.104.155111)

Phys. Rev. B 104, 155111 – Published 7 October, 2021

Authors: Oliver Lunt, Marcin Szyniszewski, and Arijeet Pal

已完成:

- 使用 tripartite 信息 $I_3$ 探测纠缠相变, 同样研究 Clifford 电路;
- 测试了 1D 和 2D 下 MIPT 的相变点和临界指数, 说明了仅看 bulk 的行为, 确实和 percolation 一致;
- 通过引入 ancilla 测试了 MIPT 的边界临界行为, 和 percolation 不同;
- 研究了测量横场 Ising 模型 (PTFIM), 这个模型和 3D percolation 有简单的几何映射, bulk 和边界临界指数也和 percolation 的相同;

未完成: