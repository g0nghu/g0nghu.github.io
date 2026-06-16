---
title: The scaling hypothesis
date: '2025-02-06T15:24:43+08:00'
categories:
- notes
---



# The scaling hypothesis

## Scaling form of the correlation function

Consider the propagator $G(\bm p) = \langle \varphi(\bm p)\varphi(-\bm p) \rangle$ in the $\varphi^4$ theory with a one-component field. $S[\varphi]$ should be dimensionless. So $[\varphi(\bm r)] = d/2 - 1$ and $[G(\bm p )] = -2$. We write $G(\bm p)$ in a dimensionless form (scaling form)
$$
G(\bm p) = \frac{1}{\bm p^2}\mathcal G(p\xi, \frac{a}{\xi}),
$$
where $a$ is a characteristic length which does not diverge at the transition ($\Lambda^{-1}$).

Assume in the limit $p\xi \rightarrow \infty$, $pa\rightarrow 0$ and $a/\xi \rightarrow 0$, $\mathcal G$ behaves like
$$
\mathcal G(p\xi, \frac{a}{\xi}) \sim (p\xi)^{x_1}(a/\xi)^{x_2}.
$$
For a well-defined $\mathcal G$, we must have $x_1 = x_2 = \eta$. So $G(\bm p, T_c) \sim \frac{a^\eta}{p^{2-\eta}}$. A more general approach is to write (**a different** $\mathcal G$)
$$
\begin{aligned}
G(\bm p) = & \frac{1}{p^{2-\eta}}\mathcal G(p\xi, a/\xi) \\
= & \frac{1}{p^{2-\eta}}\mathcal G(p\xi, 0) + \text{higher powers of } a/\xi.
\end{aligned}
$$
The new definition is well-defined in the limit $\xi\rightarrow \infty$ ($\mathcal G\rightarrow a^\eta$).

Consider the scale transformation $\bm p \rightarrow s\bm p$, $\xi \rightarrow \xi/s$, $a\rightarrow a/\xi$. If we are interested at the physics in long-distance near the phase transition, we can take the limit $\xi/a \rightarrow \infty$ while keeping $p\xi$ fixed. We have
$$
\begin{gathered}
G(\bm p, \xi) = \frac{1}{p^{2-\eta}}\mathcal G(p\xi), \\
G(s\bm p, \xi/s) = s^{-2 + \eta}G(\bm p, \xi).
\end{gathered}
$$
This shows that the field has acquired an anomalous dimension,
$$\begin{gathered}
[\varphi(\bm p)] = -1 + \eta/2, \\
d_\varphi = [\varphi(\bm r)] = d/2 -1 + \eta/2 = d_\varphi^0 + \eta/2.
\end{gathered}$$

Another form is to write the correlation function as
$$
G(\bm p, \xi) = T\chi \mathcal G(p\xi),
$$
where $\chi = T^{-1}G(\bm p=0, \xi)$ is the susceptibility. This $\mathcal G$ is a universal scaling function, independent of the parameters of the model and $\mathcal G(0) = 1$.

If we write $G$ as a function of $\bm p, t$,
$$\begin{gathered}
G(\bm p, t) = \frac{1}{p^{2-\eta}}\mathcal G_\pm(p|t|^{-\nu}), & G(s\bm p, s^{1/\nu}t) = s^{-2+\eta}G(\bm p, t), \\
G(\bm r, t) = \frac{1}{r^{d-2+\eta}}\mathcal G_\pm(r|t|^{\nu}), & G(\bm r/s, s^{1/\nu}t) = s^{-2+\eta}G(\bm r, t).
\end{gathered}$$

If we choose $\bm p = 0$ and $s = |t|^{-\nu}$, we have $\chi \sim |t|^{\nu(\eta - 2)}$. This is the scaling law
$$
\gamma = \gamma' = \nu(2-\eta).
$$

## Scaling form of the free energy density

The magnetization density $m$ being the average value of the field, one expect $m\sim \xi^{-d_\varphi} \sim (-t)^{\nu d_\varphi}$. So
$$
\beta = \nu d_\varphi = \frac{\nu}{2}(d - 2 + \eta).
$$
The free energy density $f = -T\ln Z / V$ has scaling dimension $d$. The singular part is $f_s \sim \xi^{-d}$. From $m = -\frac{\partial f_s}{\partial H} = -\frac{1}{T}\frac{\partial f_s}{\partial h}$, the scaling dimension of $h$ is $d_h = d - d_\varphi = \frac{1}{2}(d + 2 - \eta)$.

Write the free energy density in the scaling form
$$
f_s(t, h) = \xi^{-d}\mathcal F_\pm(h\xi^{d_h}).
$$
In zero field, $f_s = \xi^{-d}\mathcal F_\pm(0)\sim |t|^{d\nu}$, and we obtain
$$
c_V = T\frac{\partial^2 f_s}{\partial T^2} \sim |t|^{d\nu - 2},
$$
i.e.
$$
\alpha = \alpha' = 2 - \nu d.
$$
To make the magnetization $m \sim \xi^{d_h - d}\mathcal F'(h\xi^{d_h})$ to be defined at $T_c$, we must hace $\mathcal F'\pm(x) \sim x^{(d - d_h)/d_h} = x^{d_\varphi/d_h}$ when $x\rightarrow \infty$.This implies
$$
m(T_c) \rightarrow h^{d_\varphi / d_h},
$$
i.e.
$$
\delta = \frac{d_h}{d_\varphi} = \frac{d + 2 -\eta}{d - 2 + \eta}.
$$

The scaling form can be write as a function of $t$, 
$$
f_s(t, h) = |t|^{2-\alpha}\mathcal F_\pm\left(\frac{h}{|t|^{\Delta}}\right),
$$
where $\Delta = \nu d_h = 2 - \alpha - \beta$ is the gap exponent. The magnetization
$$
m = -\frac{1}{T}\frac{\partial f_s}{\partial h} = -\frac{|t|^\beta}{T}\mathcal F'_{\pm}\left(\frac{h}{|t|^{\Delta}}\right).
$$

We will show why critical exponents are the same on the two sides. A more general approach is to use different component in the two sides,
$$
f_s(t, h) = |t|^{2-\alpha_\pm}\mathcal F_\pm\left(\frac{h}{|t|^{\Delta}}\right).
$$
The function should be analytic in $t$ away from the critical point,
$$
f_s(t, h) = f_0(h) + tf_1(h) + \mathcal O(t^2).
$$
Near the critical point,
$$
f_s(t, h) = |t|^{2-\alpha_\pm}\left[A_\pm\left(\frac{h}{|t|^{\Delta_\pm}}\right)^{p_\pm} + B_\pm\left(\frac{h}{|t|^{\Delta_\pm}}\right)^{q_\pm} + \cdots\right].
$$
This two expansion should be the same power of $t$, i.e. $p\Delta = 2 - \alpha$ and $q\Delta = 1 - \alpha$, so
$$
f_s(t, h) = A_\pm h^{(2-\alpha_\pm)/\Delta_\pm} + B_\pm h^{(1-\alpha_\pm)/\Delta_\pm}|t| + \mathcal O(t^2).
$$
Continuity at $t = 0$ forces $\frac{2 - \alpha_+}{\Delta_+} = \frac{2 - \alpha_-}{\Delta_-}$ and $\frac{1 - \alpha_+}{\Delta_+} = \frac{1 - \alpha_-}{\Delta_-}$, which requires that $\alpha_+ = \alpha_-$ and $\Delta_+ = \Delta_-$.

The scaling laws with dimension $d$ are called hyperscaling relations. They apply only when the transition is fluctuation dominated, i.e. at or below the upper critical dimension.

## Finite-size scaling

Suppose the linear size of a system is $L$ and $[L] = -1$. The scaling form of the free energy in the absence of a magnetic field is 
$$
f_s(t, L) = \frac{1}{\xi_\infty}\mathcal F_\pm\left(\frac{\xi_\infty}{L}\right),
$$
where $\xi_\infty \sim |t|^{-\nu}$ is the correlation of infinite system . Or we can write as 
$$
f_s(t, L) = |t|^{2-\alpha} \mathcal F_\pm\left(\frac{|t|^{-\nu}}{L}\right).
$$
We hope that $\mathcal F(x) \rightarrow \text{const}$ as $x\rightarrow 0$. So when we take the thermodynamic limit $L \rightarrow \infty$ the properties goes to the same as we talked above. When $L \ll \xi_\infty$ the system is no longer governed by the critical point (the actual correlation length can not be longer than $L$). We can write the correlation length as
$$
\xi(t, L) = L\Xi\left(\frac{\xi_\infty}{L}\right),
$$
where $\Xi(x \ll 1) \sim x$ and $\Xi(x \gg 1) \sim \text{const}$. In the case $L < \xi_\infty$, $\xi(t, L)$ should be analytic of $t$,
$$
\frac{L}{\xi(t, L)} = A + BtL^{1/\nu} + \mathcal O(t^2).
$$
This shows that with a determined $t$ (or coupling constant $K$) for various value of $L$, $L/\xi(t, L)$ becomes independent of $L$ when $t = 0$ ($K = K_c$). This could be used to determine $K_c$ and $\nu$, 
$$
\ln \frac{\partial}{\partial K}\frac{L}{\xi(t, L)}|_{K = K_c} = \text{const} + \frac{1}{\nu}\ln L.
$$