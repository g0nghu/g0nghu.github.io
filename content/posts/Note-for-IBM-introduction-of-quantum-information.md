---
title: Note for IBM introduction of quantum information
date: '2026-06-03T17:24:22+08:00'
categories:
- 量子信息和量子计算
draft: true
---


# Understanding quantum information and computation

这篇笔记是为 IBM 的公开免费课程 [Understanding quantum information and computation with John Watrous](https://www.youtube.com/playlist?list=PLOFEBzvs-VvqKKMXX4vbi4EB1uaErFMSO) 所作, 我听下来体感很不错. 课程有配套的讲义 [arxiv: 2507.11536](https://arxiv.org/abs/2507.11536), 补充了一些视频中没有涉及到的细节, 到现在来说我还没有看, 后面遇到需要补充的地方会翻一下.

---

## Quantum circuit

### Projection measurement

一个投影测量被定义为一组投影算子, 满足 $\sum_{a \in \Gamma} \Pi_a = \mathbb I$, 这里 $\Gamma$ 表示测量结果, 对应一组经典状态. 所有的投影测量都可以被幺正演化和标准基测量实现.

只要令 $U$ 满足下面的形式,
$$U = \begin{pmatrix}
\Pi_0 & \cdots \\
\vdots & \cdot \\
\Pi_{n - 1} & \cdots
\end{pmatrix}.$$
$U$ 作用在 $(Y, X)$ 的复合系统中, $X$ 是希望实现投影测量的系统, $Y$ 有经典状态 $\{0, \cdots n - 1\}$, 这样
$$
U (|0\rangle \otimes |\phi\rangle) = \sum_{i = 0}^{n - 1} |i\rangle \otimes \Pi_i|\phi\rangle.
$$
之后对系统 $Y$ 做标准基测量, 以 $\norm{\Pi_i|\Psi\rangle}$ 的概率得到态 $\Pi_i\phi\rangle$.

### No-cloning theorem

不可克隆定理指的是我们无法使用给定的量子线路克隆一个**未知**的态, 而不是说我们无法重复制备一个态.

**Theorem**. 两个系统 $X$ 和 $Y$ 都被经典状态集 $\{0, \cdots, d - 1\}(d \geq 2)$ 描述, 不存在一个作用在复合系统 $(X, Y)$ 上的幺正算符 $U$ 使得 $\forall |\psi\rangle \in X$, 
$$
U(|\psi\rangle \otimes |0\rangle) = |\psi\rangle \otimes |\psi\rangle.
$$

*Proof*. 假设存在这样的幺正变换 $U$, 对于 $|\psi\rangle = c_1 |\psi_1\rangle + c_2 |\psi\rangle$, 有
$$
U(|\psi \rangle \otimes |0\rangle) = |\psi\rangle \otimes |\psi\rangle = c_i c_j |\psi_i\rangle \otimes |\psi_j \rangle.
$$
但另一方面, $U$ 是线性的, 
$$
U(|\psi\rangle \otimes |0\rangle) = c_i U(|\psi_i \rangle \otimes |0\rangle) = c_i |\psi_i\rangle \otimes |\psi_i\rangle. \qquad \square
$$

尽管使用一个给定的线路来克隆未知量子态是不可能的, 但如果条件放宽, 下面这些我们是可以做到的:
- 近似克隆;
- 克隆某个标准基, $\mathrm{CNOT}(|a\rangle \otimes |0\rangle) = |a\rangle \otimes |a\rangle$.

是实际上这一点并不是在量子中独有的, 我们也无法克隆一个经典的概率态. 我们能获得只有某个结果, 因此任何确定或随机算法都缺少足够的信息让我们重建每个结果出现的概率, 因此无法实现克隆. 这里克隆的困难在于它是非线性的, 因此不能被随机矩阵或者幺正算符描述.

### Discriminating non-orthogonal states

首先说明什么是完美区分 (perfect discrimination): 对于两个态 $|\psi\rangle$ 和 $|\phi\rangle$, 如果存在某个投影测量, 能把测量结果 $0$ 和 $1$ 完美对应对应到 $|\psi\rangle$ 和 $|\phi\rangle$ 上, 就说它们可以被完美区分.

**Theorem**. 两个量子态可以被完美区分当且仅当它们是正交的.

*Proof*. 首先一个投影测量可以被表示成幺正算符和标准基测量, 假设这个幺正演化是 $U$. 为了能完美区分两个态, 有
$$\begin{gathered}
U(|0\rangle \otimes |\psi\rangle) = |\pi_0\rangle |0\rangle,\\
U(|0\rangle \otimes |\phi\rangle) = |\pi_1\rangle |1\rangle.
\end{gathered}$$
这给出 $\langle \psi | \phi \rangle = \langle \pi_0 | \pi_1 \rangle \langle 0 | 1 \rangle$. 反过来说, 如果已经知道 $\langle \psi |\phi\rangle = 0$, 只要设计
$$ U = \begin{pmatrix}
|\psi\rangle & |\phi\rangle & \cdots
\end{pmatrix}$$
即可. $\square$

## Entanglement action

一个 Bell 态 $|\phi^+\rangle = (|00\rangle + |11\rangle) / \sqrt 2$ 被称作一个 e-bit. 在一些应用中, e-bit, 或者说纠缠, 被看作是一种资源.

### Quantum teleportation

- Alice 希望向 Bob 发送一个 qubit $Q$;
- 无法在物理上把这个 qubit 送出;
- 允许经典通讯;
- Alice 和 Bob 之间有一个 e-bit.

需要注意的是, 这里 $Q$ 是未知的, 并且这个传输需要保留 $Q$ 和可能的外界系统之间的关联. 这里不可克隆定理依旧是正确的, 当 Bob 获得这个 qubit 的时候, Alice 已经失去了它.

*Protocol*:
![](/images/2e0c72231a9d4b369eee.png)

Alice 对她手里的 qubits 做如图的变换, 然后进行测量, 根据测量的结果, Bob 对他手里的 e-bit 的另一半进行变换, 就可以恢复 $|\psi\rangle$. 只需要显式地写下 $|\psi\rangle$ 就可以证明这个协议的有效性. 这里使用的示意图是一个独立的 $Q$, 如果 $Q$ 和外部有关联, 这个协议也成立. 可以通过显式地计算这里的每个门的作用来验证这一点, 另一个更直观的理解是, 这个协议在单比特情形下给出一个恒同变换, 那么在多比特情形下也会给出一个恒同变换.

### Superdense coding

- Alice 要把两个经典比特传递给 Bob;
- Alice 只能向 Bob 发送一个 qubit;
- Alice 和 Bob 之间有一个 e-bit.

考虑到 Holevo's Theorem, 不可能从 $1$-个 qubit 中读出 $2$ 个经典比特的信息, 这也是我们必须借助 e-bit 的原因.

*Protocol*.
![](/images/83f91ebe2857483787fd.png)

这个协议看起来就像是把 teleportation 的线路反过来. Alice 根据手上的两个经典 bit 来对 e-bit 做变换 (值得注意的是, 由于纠缠的存在, Alice 一个人就可以改变整个 Bell 态), 可能把这个 e-bit 变成某个 Bell state:
$$\begin{aligned}
|\phi^+\rangle \rightarrow ^{00} |\phi^+\rangle, \\
|\phi^+\rangle \rightarrow ^{01} |\phi^-\rangle, \\
|\phi^+\rangle \rightarrow ^{10} |\psi^+\rangle, \\
|\phi^+\rangle \rightarrow ^{11} |\psi^-\rangle.
\end{aligned}$$
之后只要在 Bell 基下测量就可以了. $\square$

从 teleportation 和 superdense coding 可以看出, 我们可以消耗一个 e-bit 来实现 1 个 qubit 和 两个经典 bit 之间的相互转化.

### CHSH game

这实际上就是 Bell 不等式, 我们可以构造一个观测量, 只有在量子力学成立的情况下, 才会出现符合条件的测量结果. 但这里从一个"游戏"的视角来看这个问题.

这里的游戏实际上是一种非局域游戏, 包含两个参与者和一个裁判. 裁判向两个参与者给出一个问题的一部分, 然后结合二人的回答来判断他们是否胜利. 获胜条件是实现给定的, 但是题目是未知, 两人可以在赛前商讨策略, 但在游戏开始的时候 (给定题目之前), 二人就被禁止相互通讯. 在 CHSH 游戏中:

- 裁判给 Alice 和 Bob 的问题 $x, y \sim U\{0,1\}$, 二人的回答 $a, b \in \{0, 1\}$;
- 获胜条件是 $a \oplus b = x \wedge y$.
  
首先考虑经典情况, 假设我们使用某种确定策略, 这要求
$$\begin{gathered}
a(0) \oplus b(0) = 0,\\
a(0) \oplus b(1) = 0,\\
a(0) \oplus b(1) = 0,\\
a(1) \oplus b(1) = 1.\\
\end{gathered}$$
对任何确定策略来说最多只能同时满足上面的三条, 也就是获胜概率为 $3/4$. 而任何的概率策略是确定策略的线性组合, 获胜概率也不超过 $3/4$.

接下来我们考虑量子的情况, 假设 Alice 和 Bob 之间有一个 e-bit. 定义 $|\psi_\theta \rangle = \cos \theta |0\rangle + \sin \theta |1\rangle$, 有
$$\begin{gathered}
\langle \psi_\alpha | \psi_\beta \rangle = \cos(\alpha - \beta), \\
\langle \psi_\alpha \otimes \psi_\beta | \phi^+ \rangle = \cos(\alpha - \beta) / 2.
\end{gathered}$$
定义 $U_\theta = |0\rangle\langle \psi_\theta| + |1 \rangle\langle \psi_{\theta + \pi / 2}|$, 由于 $|\psi_\theta\rangle$ 和 $|\psi_{\theta + \pi / 2}\rangle$ 是正交的, $U_\theta$ 是幺正的, 表示一个 $\theta$ 的旋转.

在考虑了 e-bit 之后的策略是:
- Alice: 如果 $x = 0$, 作用 $U_0$, 如果 $x = 1$, 作用 $U_{\pi / 4}$, 测量给出 $a$;
- Bob: 如果 $y = 0$, 作用 $U_{\pi / 8}$, 如果 $y = 1$, 作用 $U_{-\pi / 8}$, 测量给出 $b$.
![](/images/ed5bb38a8e824c07b3fb.png)

这种策略的成功率是 $(2 + \sqrt{2})/4 \approx 0.85$.

## Quantum query algorithm

一个 query 算法的输入并不是一个字符串, 而是一个函数 $f: \Sigma^n \rightarrow \Sigma^m$, 我们的算法通过一次或者多次调用这个函数, 来获取这个函数的某种性质. 作为一些例子:

**OR**.
- 输入: $f: \Sigma^n \rightarrow \Sigma$;
- 输出: `bool`$(\exist x \in \Sigma^n, \text{ s.t.} f(x) = 1)$.

**Parity**.
- 输入: $f: \Sigma^n \rightarrow \Sigma$;
- 输出: #$(x\in \Sigma s.t. f(x) = 1)$`// 2`.

**Minimum**.
- 输入: $f: \Sigma^n \rightarrow \Sigma^m$;
- 输出: $f(\Sigma^n)$ 中按字典序最靠前的字符串.

有时候 query 算法会带有某种承诺 (promise), 那些不满足承诺的输入被认为是不关心的.

**Unique search**.
- 输入: $f: \Sigma^n \rightarrow \Sigma$;
- 承诺: 存在唯一的 $z \in \Sigma^n$, s.t. $f(z) = 1$;
- 输出: $z$.

在量子情形, 一次 query 是通过作用一次 query 门实现的[^1]. 一种实现方式是 XOR query 门 $U_f$, $\forall f: \Sigma^n \rightarrow \Sigma^m$,
$$
U_f |y\rangle |x\rangle = |y \oplus f(x)\rangle |x\rangle.
$$
把 ancilla 设成 $0$, 可以直接获得值
$$
U_f |0\rangle |x\rangle = |f(x)\rangle |x\rangle.
$$
在 query 算法的语境下, 一般认为这些 query 门是事先给定的, 我们关心是重复调用这些门的代价 (而不是构造的代价).

### Deutsch's algorithm

Deutsch 算法 (1985) 用于函数的奇偶性判断, 现在使用的版本对 Deutsch 最早的说法做了改进. 问题具体描述是:
- 输入: $f: \Sigma^m \rightarrow \Sigma^n$;
- 输出: `bool`$(f(0) \oplus f(1))$.

任何经典算法都要至少进行两次 query. 而通过一个量子线路:
![](/images/1559dc9ae70b41319ff9.png)
只需要一次 query 就可以实现, 这个算法就是 Deutsch's algorithm.

推导上面线路的过程中涉及到所谓 **phase kickback** 的技巧:
$$\begin{gathered}
|b \oplus c\rangle = X^c |b \rangle;\\
U_f |b\rangle |a \rangle = X^{f(a)}|b\rangle |a\rangle;\\
U_f|-\rangle |a\rangle = (-)^{f(a)}|-\rangle |a\rangle.
\end{gathered}$$

### Deutsch-Jozsa circuit

实际上是 Deutsch circuit 的推广.
- 输入: $f: \Sigma^n \rightarrow \Sigma$;
- 承诺: $f$ 一定是常函数或者平衡的 ($|f^{-1}(\{0\})| = |f^{-1}(\{1\})|$);
- 输出: $0$, 如果 $f$ 是常函数; $1$, 如果 $f$ 是平衡的.

使用量子算法可以在 1 次 query 下得到结果:
![](/images/77d1b49c21ba4a979c92.png)
如果 $y = 0^n$, 输出 $0$, 否则输出 $1$.

在进行推到之前要首先了解 Hadamard 门对一个比特串的变换,
$$\begin{gathered}
H|a\rangle = (|0\rangle + (-)^a|1\rangle) / \sqrt 2 = \frac{1}{\sqrt 2} \sum_{b\in \Sigma} (-)^{ab} |b\rangle;\\
H^{\otimes n}|x_{n - 1}x_{n- 2}\cdots x_1 x_0\rangle = \left(\frac{1}{\sqrt 2}\right)^n \sum_{y \in \Sigma^n} (-)^{x \cdot y}|y_{n - 1}\cdots y_1y_0\rangle.
\end{gathered}$$
这里 $x\cdot y = \sum_i x_iy_i\mod 2$.

把一层 Hadamard 门作用之后的态记作 $|\pi_0\rangle$, 
$$\begin{gathered}
|\pi_0\rangle = |-\rangle \otimes \frac{1}{\sqrt{2^n}}\sum_x |x\rangle,\\
|\pi_2\rangle = U_f |\pi_1\rangle = \frac{1}{\sqrt{2^n}} |-\rangle\otimes \sum_x (-)^{f(x)}|x\rangle. 
\end{gathered}$$
作用第二层 Hadamard 门之后的态是
$$
|\pi_3\rangle = \frac{1}{2^n} |-\rangle \oplus \sum_{x, y}(-)^{f(x) \oplus x \cdot y} |y\rangle.
$$
那么给出测量结果 $y= 0$ 的概率是
$$
p(0^n) = \left|\sum_x(-)^{f(x)}\right|.
$$

相比之下如果使用一个确定的经典算法, 需要 $2^{n - 1} + 1$ 次 query. 一个概率算法可以以比较高的概率以较低成本实现, 这个算法的表述是:
1. 均匀抽样选择 $k$ 个输入 $x^1, \cdots, x^k \in \Sigma^n$;
2. 如果值全部相同, 输出 $0$, 否则输出 $1$.
这个概率算法在 $f$ 是常函数的情况下一定成功, 在 $f$ 是平衡的情况下以 $1 - 2^{-k + 1}$ 的概率成功.

### Bernstein - Vazirani problem

- 输入: $f: \Sigma^n \rightarrow \Sigma$;
- 承诺: $\exist s$, s.t. $f(x) = s\cdot x$, $\forall x \in \Sigma^n$;
- 输出: $s$.

任何经典算法需要至少 $n$ 次查询才能获得结果, 一个量子的解决方法使用 Deutsch-Jozsa 线路, 而线路的输出就是 $s$. 这是因为
$$\begin{aligned}
|\pi_3\rangle = & \frac{1}{2^n} |-\rangle \oplus \sum_{x, y}(-)^{f(x) \oplus x \cdot y} |y\rangle \\
= & \frac{1}{2^n} |-\rangle \oplus \sum_{x, y}(-)^{x \cdot (y + s)} |y\rangle \\
= & |-\rangle \otimes |s\rangle.
\end{aligned}$$

### Simon's algorithm

Simon 问题被描述为:
- 输入: $f: \Sigma^n \rightarrow \Sigma^m$;
- 承诺: $\exist s \in \Sigma^n$, s.t. $x, y\in \Sigma^n$, $[f(x) = f(y)] \Leftrightarrow [(x = y) \text{ or } (x \oplus s = y)]$;
- 输出: $s$.

依旧和 Deutsch-Jozsa 线路类似, 只是把最下面的 $H|1\rangle$ 换成 $|0^m \rangle$, 线路输出记为 $y$. 线路经过 $U_f$ 之后得到$|\pi_2\rangle = \frac{1}{\sqrt{2^n}}\sum_x |f(x) \rangle |x\rangle$. 经过第二排 Hadamard 门之后是
$$
|\pi_3\rangle =  \frac{1}{\sqrt{2^n}} \sum_x |f(x) \rangle \otimes \frac{1}{\sqrt{2^n}}\sum_y (-)^{x \cdot y}|y\rangle.
$$
测量得到 $y$ 的概率是
$$\begin{aligned}
p(y) = & \norm{\frac{1}{2^n} \sum_x (-1)^{x \cdot y} |f(x) \rangle} \\
= & \frac{1}{2^{2n}} \sum_{z \in \mathrm{range}(f)} \left| \sum_{x \in f^{-1}(\{z\})} (-)^{x \cdot y}\right|.
\end{aligned}$$
如果 $z = 0^n$, 那么 $p(y) = \frac{1}{2^n}$, 结果是均匀分布的. 如果 $z \neq 0^n$,
$$\begin{aligned}
p(y) = & \frac{1}{2^{2n}}\sum_{z \in \mathrm{range}(f)} \left|(-)^{w\cdot y} + (-)^{(w  + s) \cdot y}\right|^2 \\
= & \frac{1}{2^{2n}}\sum_{z \in \mathrm{range}(f)}\left| 1 + (-)^{s \cdot y}\right|^2 \\
= & \begin{cases}
\frac{1}{2^{n - 1}}, & \text{ if } s \cdot y = 0,\\
0, & \text{ if } s \cdot y = 1.
\end{cases}
\end{aligned}$$

需要进行一个后处理, 假设我们运行了线路 $k = n + r$ 次, 得到 $y^1, \cdots, y^k$. 把这些 $y$ 按行排列得到矩阵 $M$, 在任何 $s$ 下都有 $Ms = 0$, 也就是说 $s$ 一定在 $M$ 的零空间中. 我们以 $1 - 2^{-r}$ 的成功率得到这个零空间是 $\{0^n, s\}$.

任何经典概率算法需要 $2^{n / 2 - 1} - 1$ 次 query 才能以高于 $1/2$ 的成功率得到 $s$. 因此 Simon 算法对于这样一个可能没有什么用的特定问题给出了指数加速.

## Phase estimation problem and factorization

相位估计问题: $U$ 是 $N \times N$ 的幺正矩阵, 特征值是 $\lambda_i = \e^{2\pi \i \theta_i}$,
- $U$ 在线路中已经实现, 作用在 $n$ 个 qubits 上;
- 有一个 $n$-qubit 态 $|\psi\rangle$, 是 $U$ 的某个本征态;
- 目标: 找到 $|\psi\rangle$ 对应的特征值, 或者说 $\theta$.

在计算中我们使用二进制浮点数来近似, $\theta = y / 2^m$.

我们将使用这一技术来实现因式分解.

### Phase kickback

这里考虑一个关键组件:
![](/images/ca2adc572eea49ad8e8a.png)

在经过 $\mathrm{C}U$ 门之后的态是:
$$\begin{gathered}
|\pi_2\rangle = (|0\rangle \otimes |\psi\rangle + \e^{2\pi \i \theta} |1\rangle \otimes |\psi\rangle) / \sqrt 2, \\
|\pi_3\rangle = H(|0\rangle + \e^{2\pi\i \theta}|1\rangle) \otimes |\psi \rangle / \sqrt 2 =  ((1 + \e^{2\pi \i \theta})|0\rangle + (1 + \e^{2\pi \i \theta})|1\rangle)\otimes \psi / 2.
\end{gathered}$$

最终测量的结果是
$$\begin{gathered}
p_0 = \cos^2 \pi \theta, \quad p_1 = \sin^2 \pi \theta.
\end{gathered}$$

如果 $y \in \{0, 1\}$, 我们实际上已经得到了答案. 如果在线路中多加一个 $U$, 那么最终的测量概率中 $\theta \rightarrow 2\theta$, 似乎可以通过加入更多 $U$ 来提高分辨率.

### Two control bits

想象一个和前面的线路类似的线路, 只是有 2 个 ancilla, 第一个控制一个 $U$, 第二个控制 $U^2$, 并且缺少最后的 Hadamard 门. 经过第一层 Hadamard 门之后, 态是 $|\pi_1\rangle = |\psi\rangle \otimes \frac{1}{2} \sum_{a_1a_0} |a_1a_0\rangle$. 在经过三层 $\mathrm{C}U$ ($U$ 和 $U^2$) 之后, 态变成
$$
|\pi_3\rangle = |\psi\rangle \otimes \frac{1}{2} \sum_{a_1a_0} \e^{2\pi \i (a_0 + 2a_1)\theta}|a_1a_0\rangle.
$$
假设 $\theta = y / 4,\ y\in \{0, 1, 2, 3\}$. 定义 $|\phi_y\rangle = \frac{1}{2}\sum_{x = 0}^3 \e^{\i 2\pi \frac{xy}{4}}|y\rangle$, 这是对 $|y\rangle$ 做 FT 得到的态, 它们是正交的, 可以在这组基下做投影测量, 对 $|\pi_3\rangle$ 的两个 ancilla 做这个投影测量, 可以确定 $y \in \{0, 1, 2, 3\}$.

### QFT

现在考虑如何实现这一组投影测量, 实际上我们需要的是一个实现量子傅里叶变换的算符:
$$
\mathrm{QFT}_N = \frac{1}{\sqrt N} \sum_{xy} \e^{2\pi \i xy / N} |x\rangle \langle y |. 
$$
类似于 FFT, 这个线路可以被迭代地实现. 假设我们已经有了在 $|x\rangle$ 上作用的 $\mathrm{QFT_{2^{m - 1}}}$, 引入一个新的 ancilla, 以及一组 control phase 门, 可以实现 $\mathrm{QFT}_{2^m}$. 首先作用 $\mathrm{QFT}_{2^{m - 1}}$,
$$
(\mathrm{QFT}_{2^{m -1}} |x\rangle)|a\rangle = \left(\frac{1}{\sqrt{2^{m - 1}}} \sum_{y} \omega_{2^{m -1}}^{xy}|y\rangle\right)|a\rangle.
$$
接下来给 $y$ 的第 $k$ 位作用一个受 $a$ 控制的 $\omega_{2^{k + 2}}$ 相位门, 整个态变成
$$
\left(\frac{1}{\sqrt{2^{m - 1}}} \sum_{y} \omega_{2^{m -1}}^{xy}\omega_{2^m}^{ay}|y\rangle\right)|a\rangle.
$$
对 $a$ 作用 Hadamard 门, 有
$$
\left(\frac{1}{\sqrt{2^{m}}} \sum_{y} \omega_{2^{m -1}}^{xy}\omega_{2^m}^{ay}|y\rangle\right)\sum_b \omega_2^{ab}|b\rangle.
$$
现在线路排布的顺序是 $y_{m - 1}\cdots y_1 y_0 b$, 作用一组 SWAP 门, 把顺序变成 $b y_{m - 1}\cdots y_1y_0 \rightarrow y_my_{m - 1}\cdots y_1y_0$. 注意到这就是 $\mathrm{QFT}_{2^m}$ 变换之后的结果, 而 $\mathrm{QFT}_2$ 就是 $H$.

### Arbitrary precision

现在只要有之前的 $\mathrm{C}U$ 构成的线路, 然后作用 QFT, 我们可以以任意的精度确定 $y$.

![](/images/ea2680f2b97a43b7952b.png)

$U$ 的作用如果是顺序的, 代价很高, 因为我们会需要 $U^{2^{m - 1}}$ 这样的线路, 代价是指数的, 对于某些特定问题, 线路是可以被优化的.

经过完整的线路得到 $y$ 的概率是
$$
p_y = \left|\frac{1}{2^m}\sum_{x = 0}^{2^m - 1}\e^{2\pi \i x(\theta - y / 2^m)}\right|^2.
$$
假设 $y / 2^m$ 是对 $\theta$ 的最佳估计, $|\theta - y / 2^m| \leq 2^{-(m + 1)}$. 可以证明测量得到得到 $y$ 的概率至少是 
$$
p_y \geq \frac{4}{\pi^2} \approx 0.405.
$$

而如果 $y$ 的取值使得在 $\theta$ 和 $y / 2^m$ 之间有另一个更好的估计, 那么 $p_y \leq 1/4$. 这样只要我们重复运行上面的线路, 就可以得到对 $\theta$ 任意精度的估计.

### The order-finding problem

定义 $\mathbb Z_N = [N]$, $\mathbb Z_N^* = \{\alpha \in \mathbb Z_N | \gcd(\alpha, N) = 1\}$, $\forall \alpha \in \mathbb Z_N^*$, $\exist k \in \mathbb Z$, s.t. $\alpha^k = 1$, 最小的 $k$ 被称作 $\mathbb Z_N^*$ 中 $\alpha$ 的阶.

- 输入: $(\alpha, N)$, 并且 $\gcd(\alpha, N) = 1$;
- 输出: $\alpha$ 的阶 $r$.

定义 $M_\alpha$, $M_\alpha|x\rangle = |\alpha x\rangle$, 这里 $\alpha \in \mathbb Z_N^*$, $x \in \mathbb Z_N$. 在 $\gcd(\alpha, N) = 0$ 的情况下 $M_\alpha$ 只是一个置换门, 所以是幺正的, 这也保证了我们可以独立为 $M^k$ 构造线路, 从而避免了潜在的指数复杂度, 这里涉及到我们如何使用量子线路实现经典的 boolean 线路. 而 $M_\alpha$ 的特征向量是
$$
|\psi_n\rangle = \frac{1}{\sqrt{r}} \sum_{k = 0}^{r - 1}\omega_r^{nk}|\alpha^{k}\rangle,
$$
并且有特征值 $\omega_{r}^{nk}$.

假设我们已经获得了 $|\psi_1\rangle$,
- 给定 $|\psi_1\rangle$ 和 $M_\alpha$, 我们可以使用相位估计来获得 $y / 2^m \approx 1/r$.
- 输出 $\mathrm{range}(2^m / y)$.

如果要求这种方式一定给出正确的 $r$, 要求的精度是
$$
\left| \frac{y}{2^m} - \frac{1}{r} \right| \leq \frac{1}{2N^2}.
$$
那么选择 $m = 2 [\log N] + 1$ 即可.

如果获得的是 $|\psi_j \rangle$, 使用相位估计得到的是 $j / r$. 我们选择输出最接近 $y / 2^m$ 的 $u / v$, 这里 $u, v$ 是两个整数, 可以通过 *continued fraction* 算法实现. 虽然在 $j$ 是 $r$ 的因子的时候无法给出正确的结果, 但可以如果计算很多次, 会恢复 $r$.

接下来的问题是如何获得 $|\psi_j\rangle$? 实际上只要使用 $|0\rangle = \frac{1}{\sqrt r} \sum_j |\psi_j\rangle$ 即可, 把这个态输入相位估计的线路相当于随机选择 $|\psi_j\rangle$.

### Shor's algorithm for factorization

1. 随机选取 $$

[^1]: 有时候似乎称作 oracle, 而 XOR query 或者 phase query 都被看作是 oracle.