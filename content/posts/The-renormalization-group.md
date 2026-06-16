---
title: The renormalization group
date: '2025-02-07T14:51:32+08:00'
categories:
- notes
draft: true
---


# The renormalization group

## Renormalization-group transformations

A RG transformation is to integrate out a subset of short-distance degrees of freedom. Consider a field $\bm \varphi(\bm r)$ with $N$ components and assume an ultraviolet momentum cutoff $\Lambda$. The action is $S[\bm \varphi; K]$ with $K$ a set of coupling constant. A RG transformation has two steps:
1. Mode elimination (decimation or coarse graining): First eliminate the short-distance degrees of freedom.
$$\bm \varphi(\bm r) = \bm \varphi_<(\bm r) + \bm \varphi_>(\bm r),$$
where $\bm \varphi_<(\bm r)$ has Fourier components in the range $0 \leq p \leq \Lambda/s$ and $\bm \varphi_>(\bm r)$ in $\Lambda/s \leq p \leq \Lambda$. Then integrates out $\bm \varphi_>$ to get an effective action $S[\bm \varphi_<;K_<]$. In general, the functional form of the action is not preserved and the set $K_<$ is larger than K;
2. Rescaling: Rescale the momentum and coordinates, $\bm p' = s\bm p$ and $\bm r' = \bm r /s$, to restore the momentum cutoff to its original value ($0 \leq p \leq \Lambda$). One also defines a rescaled field,
$$\begin{gathered}
\bm \varphi'(\bm r') = \lambda_s(K)\bm \varphi_<(\bm r), \\
\bm \varphi'(\bm p') = \frac{1}{\sqrt{V'}}\int \mathrm d^dr e^{-\bm p'\cdot \bm r'}\bm \varphi'(\bm r') = s^{-d/2}\lambda_s(K)\bm \varphi_<(\bm p).
\end{gathered}$$
This is a linear RG transformation. The value of the rescaling parameter is determined by
$$
\lambda_s(K) = s^{d_\varphi^0}\sqrt{Z_s(K)}.
$$

The two steps can be summarized by
$$
e^{-S[\bm \varphi';K']} = \left\{\int_{\Lambda/s \leq p \leq \Lambda \mathcal D[\bm\varphi]}\right\}_{\bm \varphi(\bm p)\rightarrow s^{d/2}\lambda_s(K)^{-1}\bm\varphi'(\bm p')}.
$$
The RG transformation can also be done in real space for some spin models. A RG transformation can be considered as a transformation
$$
K(s) = R_s(K)
$$
acting in the space of possible actions $\{S[\bm \varphi;K]\}$. One can make
$$
R_{s_1s_2} = R_{s_1}R_{s_2}.
$$

### Infinitesimal RG transformation

Choose $s = e^{\mathrm dl}$ and $\mathrm dl\rightarrow 0$. Then integrates out field with momenta $\Lambda(1-\mathrm dl) \leq p \leq \Lambda$. After $l/\mathrm dl$ infinitesimal RG transformations, $s = e^{l}$. Given $s_1 = 1 + \epsilon (\epsilon\rightarrow 0)$ and $s_2 = s$,
$$\begin{gathered}
s \frac{\partial K(s)}{\partial s} = \beta(K(s)), \\
\beta(K(s)) = \frac{\partial R_{s'}(K(s))}{\partial s'}|_{s'=1}.
\end{gathered}$$
We can consider $K(s)$ as a function of $l$ for $l = \ln s$ and similar for the scaling factor $Z_l = Z_s(K)$. Define
$$
\eta_l = \partial_l \ln Z_l,
$$
i.e.
$$
Z_{l+\mathrm dl} = Z_l e^{\eta_l\mathrm dl}\ \ \text{or}\ \ Z_l = \exp(\int_0^l \mathrm dl'\eta_{l'}).
$$
From $\lambda_s(K) = s^{d_\varphi^0}\sqrt{Z_s(K)}$ we have
$$
\frac{\lambda_{l+\mathrm dl}}{\lambda_l} = e^{(d_\varphi^0+\eta_l/2)}\mathrm dl.
$$
We will show later how $\eta_l$ is related to $\eta$.

### Advantages of the RG approach

- A RG transformation involves only a finite number of degrees of freedom. No singularity happens.
- Different initial situations will give different trajectories. The set of such trajectories are called RG flow. The fixed point of RG flow $K^*=R_s(K^*)$ shows the long-distance physics.

## Fixed point

In a RG transformation $R_s$, the correlation function transforms as $\xi(K(s)) = \xi(K)/s$. At the fixed point $K^*=R_s(K^*)$, we must have $\xi(K^*) = \xi(R_s(K^*))$ which implies that $\xi(K^*)$ is zero or infinity. $\xi=0$ is called trivial fixed point and $\xi=\infty$ is called critical fixed point. Critical fixed points describe the singular behavior at a second-order phase transition. Trivial fixed point points describe the various phases of the system.

The points of $K$ that could flow into the point $K^*$ are called critical manifold (critical space). For a point $K$ in the critical space, $\xi(K(s)) = \xi(K)/s < \xi(K)$, whereas $\lim_{s\rightarrow\infty}\xi(K(s))=\infty$, which implies that $\xi(K) = \infty$. All the points on the critical surface have infinite correlation length.

### Local behavior of RG flows near a fixed point

Near a fixed point $K^{*}$ the RG transformation $K' = R_s(K)$ can be linearized,
$$\begin{gathered}
K_i' \approx K_i^* + \sum_j \frac{\partial K_i'}{\partial K_j}|_{K*}(K_j - K_j^*) = K_i^* + \sum_jT_{ij}(s)(K_j-K_j^*),\\
T_{ij}(s) = \frac{\partial K_i'}{\partial K_j}|_{K*}.
\end{gathered}$$
Suppose $T_{ij}$ could be diagonalizable (this may not be true) and the eigenstates $\bm e^{(\alpha)}$ form a complete basis with real eigenvalues $\lambda_s^{(\alpha)}$. $R_{s_1s_2} = R_{s_1}R_{s_2}$ implies that $T(s)$ commute for different $s$ and $\lambda_s^{(\alpha)} = s^{y_\alpha}$. We can diagonalize $T$ in basis which is independent of $s$. Writing $\delta K_i = \sum_\alpha t_\alpha e_i^{(\alpha)}$ we can expand the action near the fixed point
$$
S[\bm \varphi;K] = S[\bm \varphi;K^*] + \sum_i\delta K_iA_i[\bm \varphi] = S[\bm \varphi;K^*] + \sum_\alpha t_\alpha O_\alpha[\bm \varphi],
$$
where $O_\alpha = \sum_i e_i^{\alpha}A_i$.