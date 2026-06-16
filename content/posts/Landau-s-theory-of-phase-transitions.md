---
title: Landau's theory of phase transitions
date: '2025-02-04T15:14:12+08:00'
categories:
- notes
---



A note for Nicolas Dupuis's book *Field theory of condensed matter and ultracold gases*.

# Landau's theory of phase transitions

## Landau's theory as a mean-field theory

### Microscopic Landau's theory

The order parameter field $\bm{\varphi}$ is usually defined as at a mesoscopic scale $\Lambda^{-1}$ which is much larger than the lattice spacing but small wrt macroscopic scales. By coarse graining, we get such field $\bm\varphi$ to get a low-energy effective description and the partition function becomes
$$
Z = \int \mathcal{D}[\bm\varphi]e^{-S[\bm\varphi]}.
$$
The momentum of the Fourier transformation field $\bm\varphi(\bm p)$ satisfies $|\bm p| < \Lambda$. A example of a $N$-component field with O($N$) symmetry is
$$
S[\bm \varphi] = \int \mathrm{d}^d r \left(\frac{1}{2}(\nabla \bm\varphi)^2 + \frac{r_0}{2}\bm\varphi^2 + \frac{u_0}{4!}\bm \varphi^4 \right).
$$
Such an approach is not appropriate to compute the transition temperature but sufficient to understand the behavior near the critical point. The approach can be done using mean-field (saddle-point) approximation,
$$
Z_{MF} \approx e^{-S[\bm \varphi]},
$$
where $\bm \varphi$ is determined by the saddle-point $\delta S/\delta \bm\varphi=0$. We can also get the free energy,
$$
F = -\frac{1}{\beta}\ln Z_{MF} = \frac{1}{\beta}S[\bm m].
$$

### Phenomenological Landau's theory

The free energy density $f=F/V$ is an analytic function of the order parameter and should satisfy the symmetry. Near the critical point, the order parameter is small and $f$ can be expanded,
$$
\beta f = \beta f_0 + \frac{r_0}{2}\bm m^2 + \frac{u_0}{4!}\bm m^4 - \bm h \cdot \bm m.
$$
This is the case when the order is homogeneous. When the order parameter is inhomogeneous, a deviation should be included,
$$
\begin{gathered}
F[m] = \int \mathrm{d}^d r f(\bm m , \nabla \bm m), \\
\beta f = \beta f_0 + \frac{1}{2}(\nabla \bm m)^2 + \frac{r_0}{2}\bm m^2 + \frac{u_0}{4!}\bm m^4 - \bm h \cdot \bm m
\end{gathered}.
$$
This is the Ginzburg-Landau free energy. $f_0$ is free energy density in the disordered phase in the absence of magnetic field. $r_0=\bar{r_0}(T-T_{c0})$ and $u_0$ is a constant. Now we want to calculate the critical exponent of the model. In a uniform field ($\bm h = h \bm e_1$),
$$
\frac{\partial \beta f}{\partial m} = r_0 m + \frac{u_0}{6}m^3 - h = 0.
$$
For a vanishing field,
$$
m = \begin{cases}
0 & \text{if }\  T \geq T_{c0} \\
\sqrt{\frac{-6r_0}{u_0}} & \text{if  }\  T\leq T_{c0} 
\end{cases}.
$$
At the critical point, the order parameter is
$$
m(T_{c0}, h) = \left(\frac{6h}{u_0}\right)^{1/3}.
$$
The free energy is
$$
f = \begin{cases}
-\frac{3T\bar{r_0}^2}{2u_0}(T-T_{c0})^2 & \text{if }\ T \leq T_{c0} \\
0 & \text{if }\ T \geq T_{c0}
\end{cases}.
$$
The susceptibility is 
$$
\chi = \beta \frac{\partial m}{\partial h} = \frac{\beta}{r_0 + u_0 m^2 / 2}
=\begin{cases}
\beta / r_0 & \text{if }\ T > T_{c0} \\
\beta / 2 |r_0| & \text{if }\  T < T_{c0}
\end{cases}.
$$
The specific heat is
$$
c_V = T\frac{\partial s}{\partial T} = -T \frac{\partial^2 f}{\partial T^2} =
\begin{cases}
0 & \text{if }\ T > T_{c0} \\
3\frac{\bar{r_0}^2}{u_0}T^2 & \text{if }\ T < T_{c0} 
\end{cases}.
$$

So we can get some critical exponent of the system: $\alpha = (\text{discontinuous})$, $\delta = 3$, $\gamma = 1$, $\beta = 1/2$. The rest is the correlation length and correlation function. Consider the case when it is not uniform,
$$
\begin{aligned}
0 = & \frac{\delta \beta F[\bm m]}{\delta m_i(\bm r)} = \frac{\delta}{\delta m_i(\bm r)}\left(\beta f_0 + \frac{1}{2}(\nabla \bm m)^2 + \frac{r_0}{2}\bm m^2 + \frac{u_0}{4!}\bm m^4 - \bm h \cdot \bm m\right) \\
= & -\nabla^2 m_i(\bm r) + r_0 m_i(\bm r) + \frac{u_0}{6}\bm m (\bm r)^2 m_i (\bm r) - h_i(\bm r). 
\end{aligned}
$$
Near the critical point, we have $|\bm m| \propto |r_0|^{1/2}$. So $|\bm h| \propto |r_0|^{3/2}$, $|\nabla \bm m| \propto |r_0|^{3/2}$.

The susceptibility is
$$
\chi_{ij}(\bm r - \bm r') = \frac{\delta m_i(\bm r)}{\delta H_j(\bm r')}\rvert_{\bm H=0} = \beta \frac{\delta m_i(\bm r)}{\delta h_j(\bm r')}\rvert_{\bm h=0}.
$$
Take the deviation of $h_j(\bm r')$ and set $\bm h(\bm r) = 0$,
$$
\left(r_0 - \nabla^2 + \frac{u_0}{6}m^2 + \delta_{i1}\frac{u_0}{3}m^2\right)\chi_{ij}(\bm r - \bm r') = \beta \delta_{ij}\delta(\bm r -\bm r').
$$
In the Fourier space, if $T > T_{c0}$,
$$
\chi_\parallel(\bm p) = \chi_\perp(\bm p) = \frac{\beta}{\bm p^2 + r_0},
$$
if $T < T_{c0}$,
$$
\begin{gathered}
\chi_\parallel(\bm p) = \frac{\beta}{\bm p^2 + 2|r_0|}, \\
\chi_\perp(\bm p) = \frac{\beta}{\bm p^2}.
\end{gathered}
$$
The longitudinal and transverse component can be gotten from
$$
G_{ij}(\bm p) = \frac{m_im_j}{m^2}G_\parallel(p) + \left(\delta_{ij} - \frac{m_im_j}{m^2}\right)G_\perp(\bm p).
$$
From this we get $\nu = 1/2$ and $\eta = 0$.

### Effective action $\Gamma[\bm m]$ within the Landau approximation

Sometimes it seems better to use the effective action $\Gamma[\bm m]$ (or the Gibbs free energy $G[\bm m] = \beta ^{-1}\Gamma[\bm m]$). When the system is coupled to an external field, the partition function reads
$$
Z[\bm h] = \int \mathcal{D} \mathrm e^{-S[\bm \varphi]+\int \mathrm d ^d r \bm h \cdot \bm \varphi}
$$
and the order parameter is given by
$$
m_i(\bm r) = \langle \varphi_i(\bm r)\rangle = \frac{\delta \ln Z[\bm h]}{\delta h_i(\bm r)}.
$$
The effective action is defined as the Legendre transform
$$
\Gamma[\bm m] = -\ln Z[\bm h] + \int \mathrm d^d r \bm h \cdot \bm m
$$
and it satisfies
$$
\frac{\Gamma [\bm m]}{\delta m_i(\bm r)} = h_i(\bm r).
$$

In the mean-field approximation, $\bm m(\bm r) = \bm \varphi (\bm r)$ and $\Gamma[\bm m ] = S[\bm m].$ The zero-field (connected) correlation function is given by the inverse of the two-point vertex
$$
\Gamma_{ij}^{(2)}(\bm r - \bm r') = \frac{\delta^2\Gamma[\bm m]}{\delta m_i(\bm r)\delta m_j(\bm r')}\vert_{\bm m(\bm r) = \bm m}.
$$

### Universality and breakdown

The mean-field theory shows that the systems with the same symmetry share the same critical exponents. But this only holds when the dimension $d > d_c$. For our $\varphi^4$ theory,
$$
\frac{\Delta M^2}{M^2} \sim \xi^{4-d}
$$
So the critical dimension is $d_c = 4$. For lower dimension, the exponents depend on the dimension and the number of components of the order parameter.

## $\varphi^4$ theory for classical spin model

The Hamiltonian of Ising model is
$$
\beta H = -\frac{1}{2}\sum_{i,j}\sigma_i K_{ij}\sigma_j - \sum_i h_i \sigma_i.
$$
The mean-field method is to write $\sigma_i = (\sigma_i - m_i) + m_i$ where $m_i = \langle \sigma_i \rangle$, 
$$
\beta H_{MF} = -\sum_i(h_i  + \sum_j K_{ij}m_j)\sigma_i - \frac{1}{2}\sum_{ij}m_i K_{ij} m_j.
$$
The self-consistent equation is 
$$
m_i = \frac{\mathrm{Tr}(\sigma_i \mathrm e^{-\beta H_{MF}})}{\mathrm{Tr}\mathrm (e^{-\beta H_{MF}})} = \tanh\left(h_i + \sum_j K_{ij} m_j\right).
$$

Now we want to rewrite the partition function through a continuous field $\varphi_i$ using the Hubbard-Stratonovich transformation
$$
\mathrm e^{\frac{1}{2}\sum_{ij}\sigma_i K_{ij} \sigma_j} = \int_{-\infty}^{\infty} \mathrm e^{-\frac{1}{2}\sum_{ij}\varphi_i K^{-1}_{ij} \varphi_j + \sum_i \varphi_i \sigma_i}.
$$
Then sum over $\sigma_i$. The partition function is
$$
Z = \int_{-\infty}^{\infty} \prod_i \mathrm d\varphi_i \mathrm e^{-\frac{1}{2}\sum_{ij}(\varphi_i - h_i) K^{-1}_{ij} (\varphi_j - h_j) + \sum_i \ln 2\cosh \varphi_i}.
$$
In our case, $K_{ij}$ only exists for nearest neighbor interaction. The F-T is
$$
\begin{aligned}
K(\bm p) = & \sum_{ij}K_{ij}\mathrm e^{i \bm p \cdot (\bm r_i - \bm r_j)} \\
= & 2 K \sum_\nu \cos p_\nu \\
= & 2 K (d - \frac{\bm p^2}{2})
\end{aligned}.
$$
Here only long wave length is considered. We can get the inverse
$$
K^{-1}(\bm p) = \frac{1}{2Kd}(1+\frac{\bm p^2}{2d}).
$$
By now we get the effective action for low energy case and it is indeed a $\varphi^4$ theory.
$$
S[\varphi] = \int \mathrm d^d r \left((\frac{1}{4Kd}-\frac{1}{2})\varphi^2 + \frac{1}{8Kd^2}(\nabla \varphi)^2 + \frac{1}{12}\varphi^4 \right).
$$

The behavior of the $\varphi^4$ theory and the spin model is not the same. The $\varphi^4$ theory describes the property of the spin model in long distance and could be used for a critical system.