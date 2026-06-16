---
title: Theta terms
date: '2025-11-18T21:09:54+08:00'
categories:
- 多体系统的量子场论
draft: true
---


# $\theta$-terms

Consider a field: $\phi: M\rightarrow T$. These fields can be classified by the topological charge $W$, which should be an integer, e.g. the winding number of $\phi: S^1\rightarrow S^1$.

A topological action $S_\text{top}[\phi] \equiv F(W)$ may appear in the total action.
$$
S[\phi] = S_0[\phi] + S_\text{top}[\phi].
$$
The continuous deformation should not change $S_\text{top}$, which gives a constrain of the form of $F(W)$. Consider two fields $\phi_1$ and $\phi_2$ that are locally non-zero at different parts. Then $F(W_1 + W_2) = S_\text{top}[\phi_1*\phi_2] = S_\text{top}[\phi_1] + S_\text{top}[\phi_2] = F(W_1) + F(W_2)$. $F$ must take the following form:
$$
F(W) = i\theta W.
$$
This is called the **$\theta$-term**.

For $W$ is an integer, $\theta$ is defined on $[0, 2\pi]$. This term is imaginary and does not affect the equation of motion (EOM).

## Geometry of $\theta$-terms

The $\theta$-term can be naturally defined by the volume of the target manifold. On the target manifold, the volume is defined through a $n$-form, 
$$
\mathrm{Vol}_T = \int_T \omega.
$$
$\omega$ is renormalized to make $\mathrm{Vol}_T = 1$.

The $\theta$-term is defined using the pull-back of the filed $\int_M \phi^* \omega = \int_T \omega$. For a diffeomorphism, the result is still $1$. But for a general field, the value changes as different $\mathbb Z$. The topological action is 
$$
S_\text{top}[\phi] = i\theta\int_M \phi^* \omega.
$$

- A winding number can exist from low-dimensional bases.
  
  Consider $T = \mathbb R^2/\{0, 0\}$ and $S^1\subset T$. Closed curves in $T$ can be continuously deformed into curves on $S^1$. So the winding number of $\phi: S^1 \rightarrow T$ can be constructed by the winding number of $\phi': S^1 \rightarrow S^1$.

- $S_\text{top}[\phi]$ is invariant under continuous deformation of $\phi$.

  *Proof*: Consider two fields $\phi: M \rightarrow T$ and $\phi'$, which differ a map $\psi: T \rightarrow T$ ($\phi' = \phi \circ \psi$). Suppose $\psi$ is locally different from identity only on a local domain $U\subset T$. Then
  $$
    S_\text{top}[\phi'] - S_\text{top}[\phi] = i\theta\int_M(\phi^*\omega - (\psi\circ \phi)^*\omega) = i\theta\int_M \phi^*(\omega - \psi^* \omega).
  $$ 
  Now define $\kappa = \phi^*(\omega - \psi^* \omega)$. This is a $n$-form and must can be locally represented by a $(n-1)$-form $\xi$ (only locally), $\mathrm d\xi = \kappa$. Using the Stokes' theorem, the above integral becomes $i\theta\int_M \mathrm d\xi = i\theta \int_{\partial M}\xi = 0$.