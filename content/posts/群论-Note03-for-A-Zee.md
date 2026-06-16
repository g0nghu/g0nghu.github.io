---
title: 群论 Note03 for A.Zee.
date: '2025-03-31T00:32:26+08:00'
categories:
- notes
draft: true
---


## Group theory in the microscopic world

### Isospin and the discovery of a vast internal space

#### A small number i hte subnuclear world

中子和质子的质量很接近, 这是强相互作用的$SU(2)$对称性导致的, $N = (p, n)$构成了$SU(2)$的spinor representation, 而微小的质量差可以看作是电磁相互作用导致的.

#### The pions and the electric charge

实验上发现了$\pi^+, \pi^-$之后, 它们和核子发生相互作用, 因此也应该在isospin的变换下变换, 发现了它们和核子有如下的反应$p \rightarrow n + \pi^+, n\rightarrow p + \pi^-$. 这两个反应的初态, 都有着isospin $I = 1/2$. 我们把$\pi$介子的isospin记作$I_\pi$, 那么末态的isospin应该是$\frac{1}{2}\otimes I_\pi = (I_\pi + \frac{1}{2})\oplus |I_\pi - \frac{1}{2}|$, 应该包含$I = 1/2$的成分, 因此$I_\pi = 0$或者$1$. 但是$I_\pi = 0$不可能给出两种粒子$\pi^+, \pi^-$, 所以$I_\pi = 1$, 这是一个$3$维的表示. 这表明还有一种粒子$\pi^0$, 这一预言的确被实验证实了.

现在来考虑电荷是如何进入这些isospin的关系中的. 来考虑$p$和$n$之间的电荷差是$\Delta Q = Q_p - Q_n = 1 - 0 = I_{3, p} - I_{3, n} = \Delta I_3$, 这样我们就得到
$$
Q = I_3 + \frac{1}{2}Y,
$$
其中$Y$称作hypercharge, 是和$SU(2)$无关的算符. 并且对核子来说$Y = 1$, 对$pi$介子来说, $Y = 0$.

#### Scattering cross sections and isospin

氘核包含两个核子, 似乎可以通过核子之间的相互作用得到, $p + p \rightarrow  d + \pi^+$或者$p + n \rightarrow d + \pi^0$. 因为有$\frac{1}{2} \otimes \frac{1}{2} = 1 \oplus 0$, 如果说$d$的isospin是$1$, 因该还有$2$种相同质量的粒子, 但实际上我们并没有观察到$p-p$或者$n-n$束缚态, 所以$d$的isospin是$0$, 是两个核子的singlet.

上面两个反应中第一个反应的初态可以写成是$|1/2, 1/2; 1/2, 1/2\rangle$, 第二个反应的初态可以写成$|1/2, 1/2; 1/2, -1/2\rangle$. 我们有如下的CG分解
$$\begin{gathered}
|1, 1\rangle = |1/2, 1/2; 1/2, 1/2\rangle,\\
|1, 0\rangle = \frac{1}{\sqrt 2}\left( |1/2, -1/2; 1/2, 1/2 \rangle + |1/2, 1/2; 1/2, -1/2\rangle \right), \\
|0, 0\rangle = \frac{1}{\sqrt 2}\left(|1/2, -1/2; 1/2, 1/2\rangle - |1/2, 1/2; 1/2, -1/2\rangle\right).
\end{gathered}$$

那么上面第一个反应应该给出$I = 1$. 而第二个反应, $|1/2, 1/2; 1/2, -1/2\rangle = \frac{1}{2}(|1, 0\rangle - |0, 0\rangle)$是一个$I = 1$和$I = 0$的混合态. 但是由于isospin是守恒的, 末态$I = 1$使得我们要求初态中没有$I = 0$的分量. 这样, 第二个反应的振幅只有第一个反应的$1/\sqrt 2$.

我们可以引入变换算符$\mathcal T$, 把初态变成末态$\langle d\pi^+ | \mathcal T |pp\rangle = \langle 1, 1 | \mathcal T | 1, 1 \rangle$, 而$\langle d \pi^0 | \mathcal T| pn \rangle = \langle 1, 0 | \mathcal T (\frac{1}{\sqrt 2}(|1, 0\rangle) - |0, 0\rangle) = \frac{1}{\sqrt 2} \langle 1, 0 | \mathcal T | 1, 0 \rangle$. 这给出这两个过程的散射截面之比是$\frac{\sigma(p + p \rightarrow d + \pi^+)}{\sigma(p + n \rightarrow d + \pi^0)} = 2$.

#### Nucleon nucleon scattering and Feynman diagrams

利用CG分解, 我们可以写下面的表达式,
$$\begin{gathered}
|p\rangle \sim -\sqrt{1/3}|\pi^0, p\rangle + \sqrt{2/3}|\pi^+, n\rangle,\\
|n\rangle \sim -\sqrt{2/3}|\pi^-, p\rangle + \sqrt{1/3}|\pi^0, n\rangle.
\end{gathered}$$
这并不是说左右两边是相等的, 而是说在isospin的变换下, $|p\rangle$变换形式如同右边的线性组合, 并且$|p\rangle$处在$|\pi^+, n\rangle$的振幅是处在$|\pi^0, p\rangle$的$-\sqrt 2$倍. 这给出了$\pi$介子核子之间的相互作用系数之间的相对大小, 写成矩阵元的形式是
$$\begin{aligned}
g_{p, \pi^0 p} = g, \ g_{p, \pi^+ n} = -\sqrt 2 g, \ g_{n, \pi^-p} = \sqrt 2 g, \ g_{n, \pi^0, n} = -g.
\end{aligned}$$

现在我们可以给出核子之间相互作用的大小, 对于$p + p \rightarrow p + p$, 可以在中间态产生一个虚的$\pi^0$来传递相互作用, 那么总的相互作用是$g^2$, 对于$n-n$的相互作用是相同的, 此外需要注意$n-p$相互作用, 可能发生两种不同的中间过程, 对应于在初态和末态中是否交换$p$和$n$, 但总的相互作用还是$g^2$.

#### Pion nucleon coupling and the tensor approach

我们可以使用spinor来得到$\pi$介子和核子的相互作用强度(相对大小), 首先写下核子$N = (p, n)$变换如同$SU(2)$的$I = 1/2$的defining representation, $N^i \rightarrow U^i_{\ j}N^j$, $N_i \rightarrow N_j (U^\dagger)^j_{\ i}$, 在变换下$N_iN^i$不变.

$I = 1$的vector表示构成了$SU(2)$的伴随表示, 可以写成$\phi^i_{\ j}$, 无迹且厄米, 可以写成Pauli矩阵的线性组合$$
\phi = \vec{\pi}\cdot \vec{\tau} = \begin{pmatrix}
    \pi_3 & \pi_1 - i\pi_2 \\
    \pi_1 + i\pi_2 & -\pi_3
\end{pmatrix} = \begin{pmatrix}
    \pi_0 & \sqrt 2\pi^+ \\
    \sqrt 2\pi^- & -\pi^0
\end{pmatrix}.
$$
在$SU(2)$变换下, $\phi^i_{\ j}\rightarrow U^i_{\ j}\phi^l_{\ n}(U^\dagger)^n_{\ j}$. 那么在Lagrangian中表示$pi$介子和核子相互作用的一项应该写成$fN_i\phi^{i}_{\ j}N^j$, 展开之后就是
$$
N_i\phi^i_{\ j}N^j = (\bar{p}\pi^0 p - \bar{n}\pi^0 n) + \sqrt 2(\bar{p} \pi^+ n + \bar{n}\pi^- p).
$$
和我们之前的得到的结果相同.

### The Eightfold Way of $SU(3)$

#### We now need two floors

对于$SU(2)$, 我们可以使用$\epsilon^{ij}$来消除所有的上指标或者下指标. 这导致$\psi^i$和$\psi_i$荷载了两个不等价的表示, 我们记作$3$和$3^*$, 物理上对应夸克和反夸克.

相比于$N>3$的$SU(N)$来说, $SU(3)$很特别的一点是可以只考虑无迹对称的张量$\varphi^{i_1i_2\cdots i_m}_{j_1j_2\cdots j_n}$. 这样我们可以使用两个数$(m, n)$来唯一地确定$SU(3)$地表示. 来考虑这一论断地证明. 特别地对于$\varphi^{ij}$来说, 反对称的部分可以通过乘上一个$\epsilon_{ijk}$成为一个$(0, 1)$型的张量. 考虑$(1, 1)$型的张量, 如果说它是不是无迹的, 只需要减去它的迹. 这是对于$p = m + n = 2$的论证. 现在来考虑$p = 3$的部分, 先看$(3, 0)$型的张量$\varphi^{ijk} = \varphi^{\{ij\}k} + \varphi^{[ij]k}$, 反对称的部分可以被收缩成$\varphi^k_l = \epsilon_{ijl}\varphi^{[ij]k}$, 接下来对称的部分可以写成$3\varphi^{\{ij\}k} = (\varphi^{\{ij\}k} + \varphi^{\{jk\}i} + \varphi^{\{ki\}j}) + (\varphi^{\{ij\}k} - \varphi^{\{jk\}i}) + (\varphi^{\{ij\}k} - \varphi^{\{ki\}j})$, 其中后面两个括号分贝对于$ki$和$kj$反对称, 第一个括号对于$ijk$是完全对称的. 不停地考虑$p\rightarrow p+1$, 就可以证明上面的论断.

#### The dimension of $SU(3)$ tensors

现在来考虑$(m, n)$型的对称张量有多少个独立分量. 如果只有上指标, 根据我们对于$SO(3)$的讨论, 结果是$\frac{1}{2}(m+1)(m+2)$, 那么现在同时有如果上下指标, 应该是$\frac{1}{4}(m+1)(m+2)(n+1)(n+2)$. 现在考虑无迹条件$\delta_i^j \varphi^{i_1i_2\cdots i_m}_{j_1j_2\cdots j_n} = 0$, 等式左边是一个$(m - 1, n - 1)$型的对称张量, 有$\frac{1}{4}m(m+1)n(n+1)$个独立分量, 因为张量$\varphi$是完全对称的, 所以具体收缩哪两个指标是无关紧要的. 这样我们得到$SU(3)$的$(m, n)$表示的维度, 或者说$(m, n)$型对称无迹张量的独立分量个数,
$$
\mathcal D(m, n) = \frac{1}{4}(m+1)(m+2)(n+1)(n+2) - \frac{1}{4}m(m+1)n(n+1) = \frac{1}{2}(m + 1)(n + 1)(m + n + 2).
$$

#### Multiplication of $SU(3)$ irreducible representations

作为一个例子, 考虑$3\otimes 3^*$, 这是$\psi^i$和$\chi_j$的乘积$\psi^i\chi_j$, 这个张量的迹和它的无迹部分分别是两个不可约表示, 这样就有
$$
(1, 0)\otimes (0, 1) = (1, 1)\oplus (0, 0).
$$
或者可以写成$3\otimes 3^* = 8 \oplus 1$.

另外一个很简单的例子是$(1, 0)\otimes (1, 0) = (2, 0)\otimes (0, 1)$, 即$3\otimes 3 = 6 \oplus 3^*$.

接下来是一个稍微复杂的情况, $3\otimes 6$或者$(1, 0) \otimes (2, 0)$. 我们写下两个对称无迹张量$\psi^i, \varphi^{jk}$, 他们的乘积是$\psi^i\chi^{jk} = T^{ijk}$. 先挑出其中的反对称部分$\zeta^k_m = \epsilon_{mij}\psi^i\varphi^{jk}$, 并且$\zeta_k^k = \epsilon_{ijk}\psi^i\varphi^{jk} = 0$, 是无迹的, 这一部分是$(1, 1) = 8$. 然后看剩下的部分, 是完全对称的, $(3, 0) = 8$. 这样就有了
$$
(1, 0)\otimes (2, 0) = (3, 0) \oplus (1, 1),
$$
或者说
$$
3\otimes 6 = 10 \oplus 8.
$$

利用上面的结果我们甚至可以写下, 
$$
3\otimes 3 \otimes 3 = (6\oplus 3^*) \otimes 3 = 10 \oplus 8 \oplus 8 \oplus 1.
$$

最后来看$(1, 1)\otimes (1, 1)$, 把两个无迹对称的$(1, 1)$型张量相乘, 得到$\tilde{T}^{ik}_{jl} = \psi^i_j \chi_l^k$. 考虑两个迹$P_j^k = \psi^i_j \chi^k_i$和$Q_l^i = \psi^i_j \chi^j_l$, 这是两个$(1, 1)$型张量, 并且有相同的迹, 这对应$8\oplus 8 \oplus 1$. 去掉这些迹, 我们的得到一个无迹的张量$T^{ik}_{jl}$. 

反对称化上指标, 得到$A^{ik}_{jl} = T^{[ik]}_{jl}$, 这时下指标被自动对称化了. 现在来说明这一点: 令$B_{mjl} = \epsilon_{ikm}A^{ik}_{jl}$, 那么$B_{mjl}\epsilon^{jln} = \epsilon_{ikm}\epsilon^{jln}A^{ik}_{jl} = 0$, 这是由于$A$无迹导致的, 这样$B_{mjl}$是完全对称的, 表示$(0, 3) = 10^*$. 接下来可以反对称化下指标, 得到$(3, 0) = 10$. 现在只剩下了上下指标都完全对称的部分, 对应$(2, 2)$. 现在我们得到
$$
(1, 1)\oplus (1, 1) = (2, 2)\oplus (3, 0) \oplus (0, 3) \oplus (1, 1) \oplus (1, 1) \oplus (0, 0),
$$
或者说
$$
8 \otimes 8 = 27 \oplus 10 \oplus 10^* \oplus 8 \oplus 8 \oplus 1.
$$

#### Multiplication rule for $SU(3)$

更一般地, 如果相乘$(m, n)$和$(m', n')$, 要如何分解呢? 这个表示通过一个有$m + m'$个上指标和$n + n'$个下指标的张量荷载. 我们把一个有$m + m'$个上指标和$n + n'$个指标, 并且前$n$个下指标, $m$个上指标和$n'$个下指标, $m'$个上指标分别是是完全对称的张量记作$(m, n; m', n')$. 这种张量比$(m, n)\otimes (m', n')$多出来交叉求迹是$0$的要求.

这样我们可以慢慢地把迹从这个张量中减去, 得到
$$
(m, n)\otimes (m', n') = (m, n; m', n') \oplus (m - 1, n; m', n' - 1) \oplus (m, n - 1; m' - 1, n') \oplus \cdots.
$$
注意上面的迹都是交叉求迹, 因为如果对着$m, n$中的各自一个指标收缩得到的迹已经是没有迹的. 我们把乘积分解成一些形如$(m - p, n - q; m' - q, n' - p)$的表示, 这些表示是可约的. 现在可以从$m - p, n - q$中各自选出一个上指标进行对称化, 和我们之前的讨论是类似的, 这是下指标会被自动反对称化, 接下来只要持续这个过程就可以了.

#### Quarks and triality

我们可以根据$SU(3)$的不可约表示的triality $(m - n)\mathrm{mod}\ l3$来分类. 先来看$SU(3)$群的中心, 是三个纯量阵$I, \omega I = z, \omega^2 I = z^2$. 对于一个$(m, n)$型的张量, 每个上指标给出$\omega$的乘积, 每个下指标给出$\omega^*$的乘积, 这样这个张量总共多出一个$e^{2\pi i (m  - n)/3}$的因子.

我们把荷载了基本表示$3$的三种粒子称作夸克, 分别记作$u, d, s$, 它们的反粒子$\bar{u}, \bar{d}, \bar{s}$荷载了$3^*$. 强相互作用粒子由夸克组成, 每个上指标给出一个夸克, 每个下指标给出一个反夸克. 实验上观察到的粒子都是triality是$0$的, 这说明夸克或者traility不是$0$的的粒子都是禁闭的.

#### You shall know the whole by its parts: the analog of crystal field splitting

我们可能关心$SU(3)$破缺之后的情况. $SU(3)$的最大的子群是$SU(2)\times U(1)$, $SU(2)$表示isospin, $U(1)$对应于$e^{i\theta Y}$, $Y$是厄米无迹阵的hypercharge阵
$$
Y = \frac{1}{3}\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & -2 
\end{pmatrix}.
$$
在$SU(2)$的isospin的变换下, $u, d$夸克之间相互变换, 而$s$夸克不变, 它们分别有hypercharge $1/3, 1/3, -2/3$. 通过我们把$SU(3)$限制在$SU(2)\times U(1)$上, 原本的不可约表示变成$3 \rightarrow (2, 1)\oplus (-1, 2)$, 这两个数字分别表示$SU(2)$的不可约表示的维度和$3Y$, 或者使用一个更紧凑的符号$I_{3Y}$.

把$G$限制在子群$H$上, 它的fundamental representation分解的形式展示了$H$是如何嵌入在$G$中的, 只要知道了fundamental representation的分解方式, 其他表示在这种限制下的分解也可以得到. 此外$3^* \rightarrow 2_{-1} + 1_{2}$.

现在来考虑当$SU(3)$被限制在$SU(2)$上时, $3\otimes 3^* = 8 \oplus 1$成为什么.
$$
3 \otimes 3^* \rightarrow (2\oplus 1) \otimes (2 \oplus 1) = 3 \oplus 1 \oplus 2 \oplus 2 \oplus 1.
$$
这样我们就有$8 \rightarrow 3 \oplus 1 \oplus 2 \oplus 2$. 这在物理上意味着介子包含$1$个triplet, $2$个doublet和$1$和singlet.

#### Harmonic oscillator in 3-dimensional space and $SU(3)$

三维的谐振子的能级是$E_{n_1n_2n_3} = (n_1 + n_2 + n_3 + 3/2)\hbar \omega$, 只和三个量子数的和有关, 这个简并是$SU(3)$带来的, 简并度是$\mathcal D(n) = (n + 1)(n + 2) / 2$, 和我们之前给出的$SU(3)$的不可约表示的维度是相同的.

### The Lie algebra of $SU(3)$ and its root vectors