---
title: Quantum Monte Carlo for Spins and Bosons
date: '2024-11-26T11:36:41+08:00'
categories:
- notes
---


我配置的katex居然无法渲染`\ket{\psi}`，只能全部改成`|\psi \rangle`这种东西。更奇怪的是居然到现在才第一次遇到这个问题。

---

# Quantum Monte Carlo for spin and bosonic systems

## World line QMC

The partition function 
$$Z = \sum_{\text{path}} \langle{\alpha_0}|e^{-\Delta_\tau H}| \alpha_{L-1}\rangle \cdots \langle \alpha_2 | e^{-\Delta_\tau H} |\alpha_{1}\rangle \langle{\alpha_1} | e^{-\Delta_\tau H}|\alpha_{0}\rangle$$
in which $e^{-\Delta_\tau H} = 1 - \Delta_\tau H$.

The **path periodic path**
$$\alpha_0 \rightarrow \alpha_1 \rightarrow \cdots \rightarrow \alpha_{L-1} \rightarrow \alpha_0$$

A purely kinetic energy Hamiltonian for hard-core bosons ($n_i = a_i^\dagger a_i \in \{0,1\}$) is
$$H = K = -\sum_{<i,j>}K_{i,j} = -\sum_{<i,j>}(a_i^\dagger a_j + a_j^\dagger a_i)$$
which can be written as a $S = 1/2$ XY model
$$H = -2\sum_{<i,j>}(S_i^x S_j^x + S_i^y S_j^y) =  -\sum_{<i,j>}(S_i^+ S_j^- + S_i^- S_j^+)$$

The matrix element $e^{-\Delta_\tau H} = \prod_{<i, j>}(1+\Delta_\tau K_{i,j})$ does not vanish only when $|\alpha_{l+1}\rangle = |{\alpha_l}\rangle$ or $|\alpha_{l+1}\rangle = \Delta_\tau K_{ij}|{\alpha_l}\rangle$. The matrix element for the two condition are $1$ or $\Delta_\tau$, respectively. The the partition function is $Z = \sum_{\{\alpha\}}\Delta_\tau^{n_K} = \sum_{\{\alpha\}}W(\{\alpha\})$, in which $n_K$ is how many hop happens in a path.

The calculation for expectation values are similar and only the last matrix element is different
$$\langle O\rangle = \frac{1}{Z}\mathrm{Tr}(Oe^{-\beta H}) = \frac{1}{Z}\sum_{\text{path}} \langle{\alpha_0}|e^{-\Delta_\tau H}|\alpha_{L-1}\rangle\cdots \langle{\alpha_2}|e^{-\Delta_\tau H}|\alpha_{1}\rangle \langle{\alpha_1}|e^{-\Delta_\tau H}O|\alpha_{0}\rangle$$

If we get the sample for different path with the probability $W(\{\alpha\})$, the expectation value is 
$$\langle O\rangle = \frac{\sum_{\{\alpha\}}O(\{\alpha\})W(\{\alpha\})}{\sum_{\{\alpha\}}(\{\alpha\})} = \langle O(\{\alpha\})\rangle_W$$
where $O(\{\alpha\}) = \frac{\langle{\alpha_1}|Oe^{-\Delta_\tau H}|{\alpha_0}\rangle}{\langle{\alpha_1}|1-\Delta_\tau H|{\alpha_0}\rangle}$ is the **estimator** and $W(\{\alpha\})$ is **weight**.

- The estimator for the kinetic operator $K_{i,j}$ ($K_{i,j}e^{-\Delta_\tau K} \approx K_{i,j}$) is 
$$K_{i,j}(\{\alpha\}) = \frac{\langle{\alpha_1}|K_{i,j}|{\alpha_0}\rangle}{\langle{\alpha_1}|1-\Delta_\tau K|{\alpha_0}\rangle}
= \begin{cases}
0 & \text{no jump} \\
\frac{1}{\Delta_\tau} = \frac{L}{\beta} & \text{jump between $i$ and $j$}
\end{cases}$$
This means that $\langle K_{i,j} \rangle = \langle n_{i,j} \rangle / \beta$. By summation we get $\langle K \rangle =-\langle n_K\rangle / \beta$. The number of jumps should be order of $N\beta$, i.e. $\langle n_K \rangle = -\langle K \rangle \beta \sim N\beta$.
- For diagonal operators, the position where the operators is not important and $O$ can be inserted anywhere in the time slice. $O(\{\alpha\}) = \frac{1}{L} \sum_{l = 0}^{L-1}O(\alpha_l)$. **why here we do not directly use $O(\alpha_0)$?**

By now we get how to calculate for a system only consisting kinetic energy. If there is an diagonal interaction $V$, we have
$$\langle {\alpha_{l+1}}|e^{-\Delta_\tau H} |{\alpha_l}\rangle= \langle{\alpha_{l+1}}| e^{-\Delta_\tau K}e^{-\Delta_\tau V} |{\alpha_l} \rangle= e^{-\Delta_\tau V_l}\langle{\alpha_{l+1}}| e^{-\Delta_\tau K}|{\alpha_l}\rangle$$
So the weight is
$$W(\{\alpha\}) = \Delta_\tau^{n_K} \exp\left(-\Delta_\tau \sum_{l=0}^{L-1}V_l \right)$$

## Continuous time limit

Now the world line is continuous in time. We need to consider the probability with another pair of hopping from $a$ to $b$ and from $b$ to $a$. Consider the probability for insertion and removal in the time interval $(\tau_1, \tau_2)$. First in a discrete case, $\tau_2 = \tau_1 + m\tau$, there are $m(m-1)/2$ ways to inserting. The total relative weight is $\Delta_\tau^2m(m-1)/2$, versus $1$ for removing events. In the continuum limit $\Delta_\tau^2m(m-1)/2\rightarrow (\tau_2 - \tau_1)^2/2$.

The **acceptance** probabilities for insertion and removal are
$$
\begin{gathered}
P_{\text{insert}} = \frac{(\tau_2 - \tau_1)^2/2}{1 + (\tau_2 - \tau_1)^2/2}\\
P_{\text{remove}} = \frac{1}{1+ (\tau_2 - \tau_1)^2/2}
\end{gathered}
$$

## Series expansion representation (SSE)

The Taylor expansion of the Boltzmann operator is $e^{-\beta H} = \sum_{n=0}^\infty \frac{(-\beta)^n}{n!}H^n$. The partition function is 
$$Z = \sum_{n=0}^\infty \frac{(-\beta)^n}{n!} 
\sum_{\{\alpha\}_n}\langle{\alpha_0}|H|\alpha_{n-1}\rangle\cdots \langle{\alpha_2}|H|\alpha_1\rangle\langle{\alpha_1}|H|\alpha_0\rangle$$

The energy is 
$$E = -\frac{1}{Z}\sum_{n=1}^\infty \frac{(-\beta)^n}{n!}\frac{n}{\beta}\cdots \sum_{\{\alpha\}_n}\langle{\alpha_0}|H|{\alpha_{n}}\rangle\cdots \langle{\alpha_2}|H|{\alpha_1}\rangle\langle{\alpha_1}|H|{\alpha_0}\rangle = -\frac{\langle n\rangle}{\beta}$$
from which we have $\langle n\rangle \propto N\beta$.

**Fixed length scheme**: cut-off at $n=L$, we need to fill in with unit operators $I$,
$$Z = \sum_{S}\frac{(-\beta)^n(L-n)!}{L!}\sum_{\{\alpha\}_L}\sum_{\{S_i\}}\langle{\alpha_0}|S_L|{\alpha_{L-1}}\rangle\cdots \langle{\alpha_2}|S_2|{\alpha_1}\rangle \langle{\alpha_1}|S_1|{\alpha_0}\rangle$$
where $n$ is the number of $S_i = H$ instances in the sequence $S$.

For spin-$1/2$ Heisenberg model,
$$H = J\sum_{b=1}^{N_b}S_{i(b)}S_{j(b)}$$
We write the Hamiltonian in diagonal(1) and off-diagonal(2) bond operators,
$$
\begin{gathered}
H_{1, b} = \frac{1}{4} - S_{i(b)}^z S_{j(b)}^z \\
H_{2, b} = \frac{1}{2}(S_{i(b)}^+S_{j(b)}^- + S_{i(b)}^-S_{j(b)}^+) \\
H = -J \sum_{b=1}^{N_b}(H_{1, b} - H_{2, b}) + \frac{JN_b}{4}
\end{gathered}
$$
All the nonzero element of the elements are
$$
\begin{gathered}
\langle{\uparrow_{i(b)}\downarrow_{j(b)}}|H_{1, b}|{\uparrow_{i(b)}\downarrow_{j(b)}}\rangle = \frac{1}{2} \\
\langle{\downarrow_{i(b)}\uparrow_{j(b)}}|H_{1, b}|{\downarrow_{i(b)}\uparrow_{j(b)}}\rangle = \frac{1}{2} \\
\langle{\downarrow_{i(b)}\uparrow_{j(b)}}|H_{2, b}|{\uparrow_{i(b)}\downarrow_{j(b)}}\rangle = \frac{1}{2} \\
\langle{\uparrow_{i(b)}\downarrow_{j(b)}}|H_{2, b}|{\downarrow_{i(b)}\uparrow_{j(b)}}\rangle = \frac{1}{2}
\end{gathered}
$$

The partion function can be rewritten as
$$Z = \sum_\alpha \sum_n (-1)^(n_2)\frac{\beta^n}{n!}\sum_{S_n}\langle{\alpha}|\prod_{p=0}^{n-1}H_{a(p), b(p)}|{\alpha}\rangle$$
where $S_n = [a(0), b(0)], [a(1), b(1)],\cdots [a(n-1), b(n-1)]$ and $n_2 = $ #off-diagonal operators in the sqruence. Using the fixed length scheme and noting $H_{0, 0} = I$,
$$Z = \sum_\alpha \sum_{S_L}(-1)^{n_2}\frac{\beta^n(L-n)!}{L!}\langle{\alpha}|\prod_{p=0}^{L-1}H_{a(p), b(p)}|{\alpha}\rangle$$

This is where we can start our Monte Carlo. We sample for $(\alpha, H_{a(p), b(p)})$ with the probability
$$W(\alpha, S_L) = \left(\frac{\beta}{2}\right)^n \frac{(L-n)!}{L!}$$
where we drop $(-1)^{n_2}$. For a regular lattice, it must be $1$ but for frustrated systems, might be $-1$. This is where the sign problem comes from.

The problem we need to solve is that how we store a configuration $(\alpha, S_L)$. One possible way is to store the initial state $\alpha$ and all the operators in time slice $p$. We can construct an injective map $[a(p), b(p)]\mapsto s(p) = 2a(p) + b(p) - 1$. $s(p) = 0$ is for unit operator.

But some times we want to know how many and what operators are applied on a site. We can construct another injective map $X(v)$. $v = 4p+l$: $p$ is the time slice and $l$ is the leg index. $X(v)$ is where a leg is connected and $X(X(v)) = v$.

From the Metropolis algorithm, the acceptation probability is 
$$P_{\text{accept}} = \min(1, \frac{W(\alpha', S_L')P_{\text{select}}(\alpha',S_L'\rightarrow \alpha, S_L)}{W(\alpha, S_L)P_{\text{select}}(\alpha,S_L\rightarrow \alpha', S_L')})$$

Now the question is how to update $(\alpha, S_L)$. First consider the **diagonal update**, i.e. $[0, 0]_p\leftrightarrow [1, b]_p$. $P_\text{select}(a=0\rightarrow a=1) = 1/N_b$, $P_\text{select}(a=1\rightarrow a=0) = 1$. The acceptance probabilities are
$$
\begin{gathered}
P_\text{accept}([0, 0]\rightarrow [1, b]) = \min(1, \frac{\beta N_b}{2(L-n)}) \\
P_\text{accept}([1, b]\rightarrow [0, 0]) = \min(1, \frac{2(L-n+1)}{\beta N_b})
\end{gathered}
$$

The diagonal update tells us how to insert and remove operators. Changing the type of operators and state $\alpha$ need **off-diagonal update**. It's not so convenient to use local off-diagonal update when some leg of the corresponding operator is connected to another operator. However, we can still do the **loop update**. A loop is all the legs connected by operators without crossing them. Then what we need to do is
- construct all loops, flip with probability $1/2$
- update the spins in the stored state

Details can be found in 5.2.3 in the reference.

---

最重要的问题可能是如何把配分函数转化成一个抽样问题以及如何更新抽样，其余的问题已经有Metropolis算法解决。

---

今天真的冷啊，风好大。