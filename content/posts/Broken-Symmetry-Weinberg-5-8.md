---
title: Broken Symmetry (Weinberg 5.8)
date: '2024-11-27T13:15:04+08:00'
categories:
- notes
---


Consider the parity symmetry in $1$-D case, $V(x) = -V(-x)$. If $\psi(x)$ is a solution for Schrodinger equation with energy $E$, $\psi(-x)$ must be another solution with energy $E$. In a degenerated case, we can find two state with the same energy $E$ and determined parity $1$ and $-1$, respectively.

Consider the potential when we talk about SSB, i.e. with a high thick barrier centered at $x=0$. If the barrier is infinitely high and thick, there will be two degenerated energy eigenstates with $E_0$, one with a wave function $\psi_0(x)$ that is non-zero only for $x>0$, and the other with a wave function $\psi_0(-x)$ that's non-zero only for $x<0$. We could form even or odd solution by the linear combination $(\psi_0(x)\pm \psi_0(-x))/\sqrt 2$. However, if the barrier is only **finite** high and thick, the even and odd solutions are not degenerated anymore, but with a small energy difference. But the odd and even solutions should still be eigenstates.

We use WKB approximation to check the energy splitting. Within the barrier, the even and odd solution should be the form
$$\psi_\pm (x) \propto \left[\exp(\int_0^x\kappa(x')\mathrm{d}x') \pm \exp(\int_0^{-x}\kappa(x')\mathrm{d}x')\right]$$
where $\kappa(x) = \sqrt{\frac{2m}{\hbar^2}(V(x)-E)}$. We need to check the condition for WKB approximation so we calculate the logarithmic derivatives of the wave functions,
$$\frac{\psi_\pm'(x)}{\psi_\pm(x)} \approx -\frac{\kappa'(x)}{2\kappa(x)} + \kappa(x)\left[\frac{\exp(\int_0^{x}\kappa(x')\mathrm{d}x')\mp \exp(\int_0^{-x}\kappa(x')\mathrm{d}x')}{\exp(\int_0^{x}\kappa(x')\mathrm{d}x') \pm \exp(\int_0^{-x}\kappa(x')\mathrm{d}x')}\right]$$
The first term $\frac{\kappa'}{\kappa}$ is small enough for a smooth and thick barrier. For a thick barrier extending from $-a$ to $a$,
$$\int_0^a \kappa \mathrm{d} x = \int_{-a}^0 \kappa \mathrm{d}x \gg 1$$
The logarithmic derivatives at the barrier edges are
$$\frac{\psi_\pm'(a)}{\psi_\pm(a)} = \frac{\psi_\pm'(-a)}{\psi_\pm(-a)} \approx -\frac{\kappa'(x)}{2\kappa(x)}  + \kappa\left[1\mp 2\exp(-\int_{-a}^a \kappa(x')\mathrm{d}x')\right]$$

Then we can determine the energy using the condition that the logarithmic derivatives must match the logarithmic derivative of the wave function just outside the barrier. For the odd and even solution, the difference is just a term proportional to $\exp(-\int_{-a}^a\kappa(x)\mathrm d x)$. Thus the energy differs by $\delta E$ proportional to $\exp(-\int_{-a}^a\kappa(x)\mathrm d x)$.

Because the odd and even solutions have nearly the same energy, the broken-symmetry state $\psi_0(x)$ and $\psi_0(-x)$ are nearly energy eigenstates. The question is, **why the broken-symmetry states are realized in nature rather than energy eigenstates?** An answer is for the phase fluctuation and perturbation. The phase changes have no correlation between the two sides of the barrier. The fluctuations change a state that is even or odd into a incoherent mixture of broken-symmetry states. The real states realized in nature are the states that are stable up to such perturbations, i.e. the broken-symmetry states.

The broken state are not indeed stable. They have a very slowly tunneling. For example, if at $t=0$ the state is $\psi_0(x)$,
$$\psi(x, 0) = \frac{1}{2}[\psi_0(x)+\psi_0(-x)]+\frac{1}{2}[\psi_0(x)-\psi_0(-x)]$$
The evolution for the state is that
$$
\begin{aligned}
\psi(x, t) = & \frac{1}{2}[\psi_0(x)+\psi_0(-x)]\exp(-i(E+\delta E)t/\hbar) \\
& + \frac{1}{2}[\psi_0(x)-\psi_0(-x)]\exp(-i(E-\delta E)t/\hbar) \\
= & \exp(-iEt/\hbar)[\psi_0(x)\cos(\delta E t/\hbar)-i\psi_0(-x)\sin(\delta Et/\hbar)]
\end{aligned}
$$
This is indeed a very slow oscillation. For a high and thick barrier, a broken-symmetry state can exist for a very long time.

This helps us understand SSB. We can only find chiral states in large molecules like proteins and sugars. Or we could only find such states in an infinitely large system.