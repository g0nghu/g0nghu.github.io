---
title: Sample-optimal classical shadows for pures states
date: '2025-12-09T12:09:18+08:00'
draft: true
---


## Preliminaries

**Definition**. For integer $k\geq 1$, $k$-*th moment* of an ensemble $\mathcal E$ of quantum states is
$$
\mathbb{E}_{|\psi\rangle\sim \mathcal E}\left[|\psi\rangle\langle \psi|^{\otimes k}\right].
$$
An ensemble $\mathcal E$ is a *(state) t-design* if the moments $1 \leq k \leq t$ are identical to those of the Haar distribution.

**Definition** (permutation operator). Given a permutation $\pi \in S_s$, define a permutation operator $W_\pi \in \mathbb C^{d^s\times d^s}$ such that
$$
W_\pi |x_1\rangle \cdots |x_s\rangle = |x_{\pi^{-1}(1)}\rangle \cdots |x_{\pi^{-1}(s)}\rangle,
$$
and extend by linearity. $W_\pi$ acts on $(\mathbb C^d)^{\otimes s}$ by sending the qudit in position $i$ to position $\pi(i)$.

**Definition** (symmetric subspace). The symmetric subspace of an $s$-qudit system is the subspace invariant under $W_\pi$ for all $\pi \in S_s$. Its dimension is $\kappa_s$ and the projector onto it is $\Pi^{(s)}_\text{sym}$. We have
$$\begin{gathered}
\Pi_\text{sym}^{(s)} = \frac{1}{s!}\sum_{\pi \in S_s}W_\pi,\\
\kappa_s = \binom{s + d - 1}{d - 1}.
\end{gathered}$$
The result is from the fact that an element in the symmetric subspace only depends on the occupation number. Suppose $n_i$ sites occupies states $i\in\{0, 1, \cdots d - 1\}$ and $\sum_{i = 1}^s n_i = s$.

**Lemma**.
$$
\kappa_s \int_{\psi}(|\psi\rangle\langle\psi)^{\otimes s}\mathrm d\psi = \Pi_\text{sym}^{(s)}.
$$
The result is from the fact that the LHS is invariant under any $U$ on local site and $W_\pi$. It should be proportional the projector according to Schur's Lemma.

We can get the following fact: let $n\leq 1$ and $\pi = (1\ 2\cdots n) \in S_n$, for any operators $A_1, \cdots, A_n$, we have
$$
\mathrm{Tr}_{-1}(W_\pi(A_1 \otimes A_2 \otimes \cdots \otimes A_n)) = A_n A_{n-1} \cdots A_1.
$$
$\mathrm{Tr}_{-1}$ indicates the partial trace of all but the first qudit. And 
$$
\mathrm{Tr}(W_\pi(A_1 \otimes A_2 \otimes \cdots \otimes A_n)) = \mathrm{Tr}( A_n A_{n-1} \cdots A_1).
$$

## The measurement

We define a POVM on $s$ qudits:

**Definition**. (standard symmetric joint measurement) The *standard symmetric joint measurement* is a measurement on $s$ qudits. It is defined by the POVM $\mathcal M_s = \{A_\psi\}_\psi\cup\{I - \Pi_\text{sym}^{(s)}\}$ with
$$
A_\psi = \kappa_s |\psi\rangle\langle \psi|\mathrm d\psi.
$$

If $\rho$ is pure, only $\{A_\psi\}_\psi$ is complete.

Let $\Psi$ be the density matrix random variable for $|\psi \rangle\langle \psi|$, where $\psi$ is the outcome of the measurement.

**Lemma** (first moment). For measurement $\mathcal M_s$ on pure state $\rho^{\otimes s}$, we have
$$
\mathbb E[\Psi] = \frac{I + s\rho}{d + s}.
$$
*Proof*. The expectation is 
$$
\mathbb E[\Psi] = \int \psi \cdot \mathrm{Pr}[\Psi = \psi] =
\int \psi\cdot \mathrm{Tr}(A_\psi\rho^{\otimes s}) = \kappa_s\int \psi\cdot \mathrm{Tr}(\psi^{\otimes s}\rho^{\otimes s})\mathrm d\psi.
$$
Using $A\mathrm{Tr}(B) = \mathrm{Tr}_2(A\otimes B)$, we have
$$
\mathbb E[\Psi] = \kappa_s\int \mathrm{Tr}_{-1}(\psi^{\otimes s + 1}\cdot (I\otimes \rho^{\otimes s}))\mathrm d\psi = 
\frac{\kappa_s}{\kappa_{s + 1}}\frac{1}{(s + 1)!}\sum_{\pi \in S_{s + 1}}\mathrm{Tr}_{-1}(W_\pi(I\otimes \rho^{\otimes s})).
$$
The element for summation is
$$
\mathrm{Tr}_{-1}(W_\pi(I\otimes \rho^{\otimes s})) = \begin{cases} I, & \text{if } \pi(1) = 1,\\
\rho, & \text{otherwise}.
\end{cases}
$$
$s!$ permutations satisfies that $\pi(1) = 1$ and $s \cdot s!$ permutations does not. Now we get the result. $\square$

**Lemma** (second moment). For measurement $\mathcal M_s$ on pure state $\rho^{\otimes s}$, we have
$$
\mathbb E[\Psi \otimes \Psi] = \frac{2}{(d + s)(d + s + 1)}\left((I + s\rho)^{\otimes 2} - \frac{s(s + 1)}{2}(\rho\otimes \rho)\right)\Pi_\text{sym}^{(2)}.
$$
*Proof*. The evaluation is similar:
$$\begin{aligned}
\mathbb E[\Psi\otimes \Psi] = &\int (\psi\otimes \psi)\cdot \mathrm{Pr}[\Psi = \psi]\\
= & \int (\psi\otimes \psi)\cdot \kappa_s \mathrm{Tr}(\psi^{\otimes s}\rho^{\otimes s})\mathrm d\psi\\
= & \kappa_s\int \mathrm{Tr}_{-1, 2}\left(\psi^{\otimes s+2}\cdot(I^{\otimes 2}\rho^{\otimes s})\right)\mathrm d\psi \\
= & \frac{\kappa_s}{\kappa_{s + 2}}\frac{1}{(s + 2)!}\sum_{\pi \in S_{s + 2}}\mathrm{Tr}_{-1, 2}(W_\pi(I^{\otimes 2}\otimes \rho^{\otimes s})).
\end{aligned}$$
With a detailed discussion in the original article of the calculation of the trace, we can get the lemma. $\square$

**Corollary**. Let $\hat{\rho} = \frac{(d + s)\Psi - I}{s}$. For any observable $O \in \mathrm{Obs}(B)$ and $\epsilon > 0$, we bound the probability of failure as 
$$
\mathrm{Pr}[|\mathrm{Tr}(O\hat \rho) - \mathrm{Tr}(O\rho)|\geq \epsilon] \leq \frac{1}{\epsilon^2 s^2}\left[\mathrm{Tr(O^2) + 8s||O^2||}\right].
$$
*Proof*. First we can get
$$
\mathbb E[\hat\rho] = \mathbb E\left[\frac{(d + s)\Psi - I}{s}\right] = \rho.
$$
Next we need to calculate the variance. First consider traceless operator $O$, where $\mathrm{Tr}(O) = 0$.
$$
\mathrm{Var}(\mathrm{Tr}(O\hat\rho)) = \mathrm{Var}\left(\frac{(d + s)\mathrm{Tr}(O\Psi) - \mathrm{Tr}(O)}{s}\right) = \left(\frac{d + s}{s}\right)^2 (\mathbb E[\mathrm{Tr}(O\Psi)^2] - \mathbb E[\mathrm{Tr}(O\Psi)]^2).
$$
The first term is evaluated using $\mathrm{Tr}(O\Psi)^2 = \mathrm{Tr}((O\otimes O)(\Psi \otimes \Psi))$ (here is typo in the original paper),
$$\begin{aligned}
(d + s)^2\mathbb E[\mathrm{Tr}(O\Psi)^2] = & \frac{2(d + s)}{d + s + 1}\mathrm{Tr}\left[
    O^{\otimes 2}\left((I + s\rho)^{\otimes 2} - \frac{s(s + 1)}{2}\rho^{\otimes 2}\Pi_\text{sym}^{(2)}\right)
\right]\\
\leq & \mathrm{Tr}\left[
O^{\otimes 2}\left(I^{\otimes 2} + s(I\otimes \rho + \rho \otimes I) + \frac{s(s - 1)}{2}\right)2\Pi_\text{sym}^{(2)}.
\right]
\end{aligned}$$
Recall that $2\Pi_\text{sym}^{(2)} = W_{(1)(2)} + W_{(12)}$, we have
$$\begin{gathered}
W_{(1)(2)}: \mathrm{Tr}(O)^2 + 2s\mathrm{Tr}(O)\mathrm{Tr}(O\rho) + \frac{s(s - 1)}{2}\mathrm{Tr}(O\rho)^2,\\
W_{(12)}: \mathrm{Tr}(O^2) + 2s\mathrm{Tr}(O^2\rho) + \frac{s(s - 1)}{2}\mathrm{Tr}((O\rho)^2),
\end{gathered}$$
and for $\rho$ is pure, $\mathrm{Tr}((\rho O)^2) = \mathrm{Tr}(O\rho)^2$.
The second term is 
$$
(d + s)^2\mathbb E[\mathrm{Tr}(O\Psi)]^2 = s^2\mathrm{Tr}(O\rho)^2.
$$
Using the Holder's inequality,
> Holder's inequality (the norm is the Schatten norm): $\mathrm{Tr}(O\rho)\leq ||O\rho||_1 \leq ||O||_\infty ||\rho||_1\leq ||O||_\infty$.

$$\begin{gathered}
s^2\mathrm{Var}(\mathrm{Tr}(\hat\rho\Psi))\leq \mathrm{Tr}(O^2) + 2s\mathrm{Tr}(O^2\rho) - s\mathrm{Tr}(O\rho)^2 \leq \mathrm{Tr}(O^2) + 2s ||O^2||,\\
\mathrm{Var}(\mathrm{Tr}(\hat\rho\Psi)) \leq \frac{\mathrm{Tr} O^2 + 2s||O^2||}{s^2}.
\end{gathered}$$
We get the variance for *traceless operator*. For a operator $O$ with trace, its traceless part is $O_0 = O - \mathrm{Tr}(O)I/d$ and we have
$$
\mathrm{Var}(\mathrm{Tr}(O\hat\rho)) = \mathrm{Var}(\mathrm{Tr}(O_0\hat\rho))\leq\frac{\mathrm{Tr} O_0^2 + 2s||O_0^2||}{s^2}.
$$
For $\mathrm{Tr}(O_0^2) = \mathrm{Tr}(O^2) - \mathrm{Tr}(O)^2 / d \leq \mathrm{Tr}(O^2)$, and $||O_0^2|| = ||O_0||^2\leq (2||O||)^2$, the variance is 
$$
\mathrm{Var}(\mathrm{Tr}(O\hat\rho)) \leq \frac{1}{s^2}(\mathrm{Tr}(O)^2 + 8s||O^2||).
$$
> Chebyshev's inequality: $P(|X - \mu| \geq t)\leq \sigma^2 / t^2$.

Using the Chebyshev's inequality, we get the result. $\square$

Here we can get the upper bound for the sample complexity of classical shadows for pure states and joint measurements.

**Theorem**.
$$
\mathbf{Shadows}(B, \epsilon, \delta) = \mathcal O\left(\left(\frac{\sqrt B}{\epsilon} + \frac{1}{\epsilon^2}\right)\log\frac{1}{\delta}\right).
$$
*Proof*. For a single batch estimate $\hat\rho^{(i)}$, the probability of failure is
$$
\mathrm{Pr}[|\mathrm{Tr}(O\hat\rho^{(i)}) - \mathrm{Tr}(O\rho)|\geq \epsilon]\leq \frac{1}{\epsilon^2 s^2}\left(\mathrm{Tr}(O)^2 + 8s||O^2||\right) \leq \frac{B + 8s}{\epsilon^2 s^2}.
$$
If we want the probability of failure to be less than some constant $p < 1/2$, we need 
$$
s > \frac{4 + \sqrt{16 + p\epsilon^2 B}}{p\epsilon^2} = \mathcal O\left(\frac{\sqrt B}{\epsilon} + \frac{1}{\epsilon^2}\right).
$$
Another median estimation is applied:
$$
E = \text{median}(\mathrm{Tr}(O\hat\rho^{(1)}), \cdots, \mathrm{Tr}(O\hat\rho^{(k)})).
$$
Assume there are an odd number of batches, so the median is some $\mathrm{Tr}(O\hat\rho^{(i)})$. If $E$ is a bad estimate ($|E - \mathrm{Tr(O\rho)}|>\epsilon$), then at least $k/2$ of the batch estimates are wrong. Different batches are independent so
$$
\mathrm{Pr}[|E - \mathrm{Tr}(O\rho)|\geq \epsilon] \leq \mathrm{Pr}\left[\#\{i:|\mathrm{Tr}(O\hat\rho^{(i)}) - \mathrm{Tr}(O\rho)|\geq \epsilon\}\geq \frac{k}{2}\right]\leq \sqrt{4p(1 - p)}^k.
$$
Setting this less than teh failure probability $\delta$, we have
$$
k \geq \frac{\log \delta^{-1}}{\log (4p(1-p))^{-1/2}}.
$$
This is where the factor $\log \delta^{-1}$ comes from. $\square$