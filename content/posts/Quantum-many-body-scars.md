---
title: Quantum many-body scars
date: '2025-11-17T15:49:13+08:00'
categories:
- Notes
draft: true
---


## Model

Consider the PXP model:
$$
H = \sum_i P_{i - 1}X_i P_{i + 1}.
$$
$P = | 1 \rangle \langle 1 | = (1 - Z) / 2$ is the projector onto the local ground state.

This model forbids adjacent Rydberg atoms, i.e. for any configuration without two neighboring excitations $|0\rangle$, it cannot evolve into a state with two neighboring excitations. So we can consider the restricted Hilbert space.

### The dimension of the restricted Hilbert space

First consider **OBC**. Suppose the restricted Hilbert space's dimension is $\mathcal D(L)$. Now add a site, if the configuration on the $(L+1)$th site is $|0\rangle$, then the configuration on the $L$th site could only be $|1\rangle$. The first $(L-1)$ sites have no constrain. If the configuration on the $(L+1)$th site is $|1\rangle$, the first $L$ sites have no constrain. So $\mathcal D(L+1) = \mathcal D(L) + \mathcal D(L - 1)$.

For $D(1) = 2 = F_3$, $D(2) = 3 = F_4$,
$$
\mathcal D_{\text{OBC}}(L) = F_{L+2},
$$
where $F_n$ is the $n$th Fibonacci number.

For the **PBC** case. If the configuration on the $(L + 1)$th site is $|1\rangle$, then no constrain is applied to the rest $L$-length OBC chain. If the configuration on the $(L+1)$th site is $|0\rangle$, then the $1$th site and the $L$th site must be $|1\rangle$ and the rest $(L-2)$ sites have no constrain. So
$$
\mathcal D_\text{PBC}(L) = \mathcal D_\text{OBC}(L-1) + \mathcal D_\text{OBC}(L-3) = 
F_{L+1} + F_{L-1}. 
$$