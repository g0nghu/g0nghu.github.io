---
title: Born-Markov Approximation
date: '2024-10-07T23:31:57+08:00'
categories:
- 开放系统
---



## 相互作用表象

$$H = H_S + H_R + g H_{int}$$
The evolution for the full system is
$$\frac{\mathrm{d}\sigma(t)}{\mathrm{d}t}=-i[H,\sigma(t)]$$
In the interaction picture
$$\sigma_I(t) = e^{i(H_S+H_R)t} \sigma(t) e^{-i(H_S+H_R)t}$$

$$V(t) = e^{i(H_S+H_R)t} H_{int} e^{-i(H_S+H_R)t}$$
The evolution in the interaction system is controlled by Liouville equation
$$
\begin{aligned}
\frac{\mathrm{d}\sigma_I(t)}{\mathrm{d}t} = & ie^{i(H_S+H_R)t} [H_s+H_R, \sigma(t)] e^{-i(H_S+H_R)t} - ie^{i(H_S+H_R)t} [H, \sigma(t)] e^{-i(H_S+H_R)t} \\
= & - ie^{i(H_S+H_R)t} [g H_{int}, \sigma(t)] e^{-i(H_S+H_R)t} \\
= & - i e^{i(H_S+H_R)t} (g H_{int}\sigma(t) - \sigma(t)g H_{int}) e^{-i(H_S+H_R)t} \\
= & -i[gV, \sigma_I]
\end{aligned}
$$

## 约化环境
$\rho(t) = \mathrm{Tr}_R(\sigma(t))$, $\rho_I(t) = e^{iH_St}\rho(t)e^{-iH_St} = \mathrm{Tr}_R(\sigma_I(t))$.
For small $g$, we write the lowest order by assuming $\mathrm{Tr}_R([V(t), \sigma_I(0)])=0$
$$\begin{aligned}
\frac{\mathrm{d}\rho_I(t)}{\mathrm{d}t} = & -i \mathrm{Tr}_R([gV(t),\sigma_I(t)]) \\
= & -i \mathrm{Tr}_R([gV(t), -i \int_0^t \mathrm{s}[gV(s), \sigma_I(s)]]) \\
= & -g^2 \int_0^t \mathrm{d}s \mathrm{Tr}_R([V(t),[V(s),\sigma_I(s)]]) 
\end{aligned}$$

## 近似

### Born Approximation(weak coupling approximation)
The reservoir is large enough and is unaffected by the system
$$\sigma(t) \simeq \rho(t) \otimes \varrho_R$$

### Markov Approximation
The evolution of the system does not depends on the history, $\rho_I(s)\rightarrow\rho_I(t)$. We also know that the integrand will vanish as $s \gg \tau_R$, where $\tau_R$ is the timescale for the time correlation function of the reservoir decaying. The integral can be written as
$$\begin{aligned}
\frac{\mathrm{d}\rho_I(t)}{\mathrm{d}t} = -g^2 \int_0^\infty \mathrm{d}s \mathrm{Tr}_R([V(t),[V(t-s),\rho_I(t) \otimes \varrho_R]]) 
\end{aligned}$$
**Why not use $\rho_I(s)\rightarrow\rho_I(t)$?** In the interaction picture, the density operator varies slower than in the Schrodinger picture.

By now we have written a markovian form linear map. If the map is positive, it can be written in a Lindblad form.