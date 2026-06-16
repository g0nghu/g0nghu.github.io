---
title: Gaussian model
date: '2025-02-05T21:37:02+08:00'
categories:
- notes
---



# Gaussian model

The Landau theory (or the mean-field theory) take the only value of the field. A simple improvement is to take into account Gaussian fluctuations.

The initial $\varphi^4$ theory is
$$
S = \int \mathrm d^d r \left(\frac{r_0}{2}\varphi^2 + \frac{1}{2}(\nabla \varphi)^2 + \frac{u_0}{4!}\varphi^4\right).
$$
Expand it near the saddle point. For $T > T_{c0}$, it is just
$$
S[\bm \varphi] = \frac{1}{2}\sum_{\bm p, i}|\varphi(\bm p)|^2(\bm p^2 + r_0)
$$
For $T < T_{c0}$, $\bm \varphi(\bm r) = \left(\sqrt{\frac{-6r_0}{u_0}}+\varphi_1'(\bm r)\right)\bm e_1 + \sum_{i=2}^N\varphi_i'(\bm r)\bm e_i$. At the saddle point the first order term must vanish and only second order should be included.
$$
\begin{aligned}
S[\bm \varphi] = & \int \mathrm d^dr \left(\frac{r_0}{2}(\sum_{i=2}^N\varphi_i'^2(\bm r) + (\sqrt{\frac{-6r_0}{u_0}}+\varphi_1'(\bm r))^2) + \frac{u_0}{4!}\bm \varphi^4 + \frac{1}{2}(\nabla \bm \varphi'(\bm r))^2\right) \\
= & S_{MF} + \int \mathrm d^dr \left(-r_0 \varphi_1'(\bm r)^2 + (\nabla \bm \varphi'(\bm r))^2\right) \\
= & S_{MF} + \frac{1}{2}\sum_{\bm p} \left[|\varphi_1'(\bm p)|^2(\bm p^2 - 2r_0) + \sum_{i=2}^N |\varphi_i'(\bm p)|^2 \bm p^2 \right]
\end{aligned}
$$

## Correlation functions

The correlation functions in the momentum space when $T > T_{c0}$ (disordered phase) are
$$
G_\parallel(\bm p) = G_{\perp}(\bm p) = \frac{1}{\bm p^2 + \xi^{-2}}.
$$
And for $T < T_{c0}$ (ordered phase), 
$$\begin{gathered}
G_\parallel(\bm p) \frac{1}{\bm p^2 + \xi^{-2}} \\
G_\perp(\bm p) = \frac{1}{\bm p^2}
\end{gathered}.$$
The two correlation length are different. The Gaussian fluctuations do not change the value of the order parameter and the transition temperature. Now we want to get the correlation functions in the real space.

The $G(\bm r)$ of $1/\bm p^2$ is satisfies the equation
$$
-\nabla^2G(\bm r) = \delta(\bm r).
$$
The solution is direct:
$$
G(\bm  r) = \begin{cases}
\frac{1}{(d-2)S_d r^{d-2}} & \text{if} & d > 2 \\
-\frac{1}{2\pi}\ln r + \text{const} & \text{if} & d = 2
\end{cases}.
$$
The $G(\bm r) = G(r)$ for $1/(\bm p^2 + \xi^{-2})$ satisfies
$$
(-\nabla^2 + \xi^{-2})G(\bm r) = (-\frac{\partial^2}{\partial r^2} - \frac{d-1}{r}\frac{\partial}{\partial r} + \xi^{-2})G(r) = \delta(\bm r).
$$
A trial solution is $e^{-r/\xi}/r^p$ at large distance.
$$
\left(p(p+1)-p(d-1)\frac{1}{r^2}\right)\frac{1}{r^2} + \left(\frac{2p}{\xi}-\frac{d-1}{\xi}\right)\frac{1}{r} = 0
$$
For $r \ll \xi$, $p = d - 2$. The $r$ dependence is logarithmic when $d=2$ and the assumption is not right. for $r \gg \xi$, $p = (d-1)/2$. The exact solution is the second kind of modified Bessel function.

## Goldstone's theorem

In the broken-symmetry phase, $G_\perp(\bm p) = \frac{1}{\bm p^2}$ and the uniform transverse susceptibility $\chi_\perp = \beta G_\perp(\bm p = 0)$ is infinite. It requires an infinitesimal field to rotate the direction of the magnetization. The reason is the soft modes: field configurations $\bm \varphi(\bm p)$ whose action $S[\varphi]$ vanishes in the long-wavelength limit $\bm p \rightarrow 0$.

This can be considered as a manifestation of Goldstone's theorem: a spontaneously broken continuous symmetry implies the existence of a low-energy mode whose energy $\omega_{\bm p}$ vanishes for $\bm p \rightarrow 0$. For the $\varphi^4$ theory with O($N$) symmetry, there are $N-1$ Goldstone modes.

The fluctuation gives the change of the action (transverse fluctuation)
$$
S[\delta \bm \varphi_\perp] = \frac{\rho_s}{2}\sum_{\bm p}\delta \bm \varphi_\perp(-\bm p)G^{-1}_\perp \delta \bm \varphi_\perp(\bm p) = \frac{\rho_s}{2}\int \mathrm d^dr (\nabla \delta \bm \varphi_\perp)^2,
$$
from which we know the transverse correlation function is
$$
G_\perp(\bm p) = \frac{m^2}{\rho_s \bm p^2}.
$$
Any spatial variation of the order parameter in the direction perpendicular to the ordering raises the energy of the system.

## Mermin-Wagner theorem - Lower critical dimension

The transverse fluctuation is described by $\delta \bm \varphi_\perp = m \delta \tilde{\bm \varphi}_\perp$ and 
$$
\langle \delta \bm \varphi_\perp (\bm r) \rangle^2 = (N-1)\int\frac{\mathrm d^dp}{(2\pi)^d}G_\perp(\bm p) = (N-1)\frac{S_d}{(2\pi)^d}\int_0^\Lambda \frac{\mathrm dp}{p^{3-d}}.
$$
When $d \leq 2$, the integral is infrared divergent and the assumption of SSB is wrong. Thermally excited transverse fluctuations destroy long-rangle order. This is Mermin-Wagner theorem: no SSB of continuous symmetry in 2D.

For the case of $N = 1$, the symmetry is discrete. For Ising model, the ground state is all-spin-down. Suppose the linear size of the system is $N$ and there is a droplet of spin-up with linear size $L$. The energy cost is $\sim 2JL^{d-1}$ and the entropy is $\sim \ln L$. The critical dimension is $1$.

By now we get two critical dimension $d_c^-$ and $d_c^+$. Below $d_c^-$ there is no ordered phase. Between the two value, there is order phase but the critical behavior is not described by mean-field theory. The mean-filed theory is correct with dimension higher than $d_c^+$.

## Breakdown of mean-field theory - Upper critical dimension

Here we want to discuss the reason for breakdown of mean-field theory with $d_c^- < d < d_c^+$.

### Fluctuation corrections to the specific heat - Ginzburg criterion

For the disordered phase, the partition function is
$$
Z = \prod_{\bm p}(r_0 + \bm p^2)^{-N/2}.
$$
The specific heat is
$$\begin{aligned}
c_V = & -T\frac{\partial^2 f}{\partial T^2} = -\frac{T\bar{r_0}^2}{V}\frac{\partial^2}{\partial r_0^2}\left(-(\frac{r_0}{\bar{r_0}}+T_{c0})\ln Z\right) \\
= & \frac{NT\bar{r_0^2}}{2V}\left(T\sum_{\bm p}\frac{1}{(\bm p^2 + r_0)^2} - \frac{1}{\bar{r_0}}\sum_{\bm p}\frac{1}{r_0 + \bm p^2}\right).
\end{aligned}$$
Near the critical point $r_0 \rightarrow 0$ so the first term is the most singular part.
$$
c_V^{\text{sing}} = \frac{N}{2}T^2 \bar{r_0}^2 K_d \int_0^{\infty}\mathrm dp \frac{p^{d-1}}{(\bm p^2 + r_0)^2} = \frac{N}{2}T^2 \bar{r_0}^2 K_d \xi^{4-d} I(\Lambda \xi),
$$
where $K_d = S_d / (2\pi)^d$ and $I(\Lambda \xi) = \int_0^{\Lambda \xi}\mathrm dx\frac{x^{d-1}}{(1+x^2)^2}$. If $d>4$ the integral is dominated bu the upper cutoff. We get the singular part of the specific heat,
$$
c_V^{\text{sing}} \approx \frac{N}{2}T^2 \bar{r_0}^2 K_d \times \begin{cases}
\frac{\Lambda^{d-4}}{d-4} & \text{if} & d>4, \\
\ln(\Lambda \xi)& \text{if} & d=4, \\
I\xi^{4-d}\ \text{independent of $\Lambda$} & \text{if} & d<4.
\end{cases}
$$

A similar analysis can be made below $T_{c0}$. The specific heat is
$$
c_V^{\text{sing}} \approx c_{V,MF}^{\text{sing}} + 2T^2 \bar{r_0}^2 K_d \times \begin{cases}
\frac{\Lambda^{d-4}}{d-4} & \text{if} & d>4, \\
\ln(\Lambda \xi)& \text{if} & d=4, \\
I\xi^{4-d}\ \text{independent of $\Lambda$} & \text{if} & d<4.
\end{cases}
$$

The Ginzburg criterion decides the temperature region the mean-field approximation is correct, $\Delta c_{V,MF} \sim c_{V, fl}$. Or we can rescale the action to make the variables to be dimensionless.
$$
S[\tilde{\bm \varphi}] = \int \mathrm d^dr \left[\frac{1}{2}(\nabla_{\tilde{\bm r}}\tilde{\bm \varphi})^2 + \frac{1}{2}\tilde{\bm \varphi}^2 + \frac{\tilde{u_0}}{4!}\tilde{\bm \varphi}^4\right],
$$
where $\tilde{\bm r} = \bm r / \xi$, $\tilde{\bm \varphi} = \xi^{(d-2)/2}\bm \varphi$, $\tilde{u_0} = \xi^{4-d}u_0$. In dimension $d > 4$, near the critical point $\tilde{u_0} \rightarrow 0$ and the theory becomes increasingly accurate. For $d < 4$ the perturbation becomes meaningless. The Ginzburg criterion can also be gotten from $\tilde   {u_0} \sim 1$.