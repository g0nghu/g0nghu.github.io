---
title: Transport in mesoscopic systems
date: '2026-01-18T11:23:23+08:00'
categories:
- notes
featured_image: /images/d82dc8d615db47fda35c.png
---




Ref: *Many-body Quantum Theory in Condensed Matter Physics*, Henrik Bruus & Karsten Flensberg. Chap 7.

---

我们在这里考虑的介观系统, 是在低温下($50\mathrm{mK}\sim 4\mathrm{K}$), 满足如下尺度关系的系统:
$$
a_0 \ll \lambda_F \lesssim l_0 < \mathcal L < l_\phi < l_\text{in},
$$
从左到右分别表示Bohr半径, 费米波长, 碰撞平均自由程, 系统线度, 相干长度, 能量弛豫长度. 这种系统可以在二维电子气 (2DEG) 或者分子系统中通过加上不同的栅极电压实现.

## The S-matrix and scattering states

我们考虑这样的系统: 一块小样品, 两边接电极形成桥 (lead), 桥两边各自接大的电子源, 电子源很大, 负责为系统提供热化好的电子, 两个电子源之间加上一定的电压. 对于这样的系统, 我们将给出 *Landauer-Buttiker* 公式.

### Definition of the S-matrix

把左右桥分别记作$\alpha = L, R$. 每个桥有着处处相同的截面$\Omega$, 对应的截面是$\partial \Omega$. 在桥中, 我们使用坐标$(x, \bm r_\perp)$ 表示坐标. 桥中的电子波函数本征态$\phi^{\pm}_{\alpha n E}$应该满足下面这一组方程:
$$\begin{gathered}
H_\alpha = \frac{1}{2m}p_x^2 + \frac{1}{2m}p_\perp^2,\\
\phi^{\pm}_{\alpha n E}(x, \bm r_\perp) = \frac{1}{\sqrt{k_n(E)}}\chi_n(\bm r_\perp)e^{\pm ik_n(E)x},\\
\frac{1}{2m}p_\perp^2 \chi_n(\bm r_\perp) = \varepsilon_n \chi_n(\bm r_\perp),\\
\chi_n(\bm r_\perp) = 0, \quad \text{for}\ \bm r_\perp \in \partial \Omega,\\
E = \frac{1}{2m}k_n^2 + \varepsilon_n, \quad \text{i.e.}, \quad k_n(E) = \sqrt{2m(E - \varepsilon_n)}.
\end{gathered}$$

桥的形状也可以是缓变的, 只要足够缓慢使得$\partial_x \chi_n$可以被忽略即可. 每个量子数$n$代表了一个从左向右输运的信道, 我们取一个截断$N$.

我们通过流而不是概率来归一化波函数, 使得它们在左右两边携带有相同的概率流:
$$
\int_\Omega \mathrm d\bm r_\perp
\left(\phi_{\lambda}^{\pm}(x, \bm r_\perp)\right)^*\frac{p_x}{m}\left(\phi_\lambda^\pm(x, \bm r_\perp)\right) = \pm\frac{1}{m}.
$$

在这种形式下, 对本征态的积分需要重新考虑($\tilde \phi_k = \frac{1}{\sqrt \mathcal L'}e^{ikx}$是正常归一化的平面波, 而$\phi_k = \frac{1}{\sqrt k}e^{ikx}$是这里使用流归一化的平面波):
$$\begin{aligned}
\sum_{k > 0}\langle \tilde \phi_k|A|\tilde \phi_k\rangle & \rightarrow
\mathcal L' \int_0^\infty \frac{\mathrm dk}{2\pi}\langle \tilde \phi_k | A | \tilde \phi \rangle \\
& = \int_0^\infty \frac{\mathrm dk}{2\pi} k \langle \phi_k | A | \phi_k \rangle\\
& = \int_0^\infty \frac{\mathrm dE}{2\pi} \frac{k}{\mathrm dE / \mathrm dk}\langle \phi_k |A|\phi_k \rangle \\
& = \frac{m}{2\pi} \int_0^\infty\mathrm dE \langle \phi_k | A | \phi_k \rangle.
\end{aligned}$$
这里暗含了平面波假设, 但在1D系统中态密度和速度总是抵消的, 出于这个原因, 我们使用能量$E$而不是$x$方向的动量来表示量子态. 

现在考虑整个系统整体的一个具有能量$E$的波函数, 在左右的桥上, 其可以被表示成$\phi^+_{LnE}, \phi^-_{LnE}, \phi^+_{RnE}, \phi^-_{RnE}$的线性组合, 系数记作$\bm a^+, \bm a^{-}, \bm b^{+}, \bm b^-$. 整个波函数在边界上依据波函数及其导数的连续性连接在一起, 通过对本征值积分积掉中间样品M的自由度, 可以得到系数$\bm a^{\pm}, \bm b^{\pm}$满足的线性方程组. 由此可以定义这个系统的S矩阵:
$$
\bm c_\text{out} \equiv \begin{pmatrix}\bm a^- \\ \bm b^+\end{pmatrix} =
\begin{pmatrix}\bm r & \bm t' \\ \bm t & \bm r'\end{pmatrix} \begin{pmatrix}\bm a^+ \\ \bm b^-\end{pmatrix} \equiv
\bm S\begin{pmatrix}\bm a^+ \\ \bm b^-\end{pmatrix} \equiv \bm S\bm c_\text{in}.
$$
表示在经过样品之后, 两侧的波函数中平面波组分之间的关系.

### Definition of scattering states

我们在这里定义散射态$\psi_{\alpha n E}$, 表示的是具有$\alpha n$入射波的整体波函数.
$$
\psi_{LnE} = \begin{cases}
\phi^+_{LnE} + \sum_{n'} r_{n'n}\phi^{-}_{Ln'E}, & (x, \bm r_\perp) \in L,\\
\psi_{M, E}, & (x, \bm r_\perp) \in M, \\
\sum_{n'}t_{n'n}\phi_{Rn'E}^+, & (x, \bm r_\perp) \in R.
\end{cases}
$$
$$
\psi_{RnE} = \begin{cases}
\sum_n' t'_{n'n}\phi_{Ln'E}^{-}, & (x, \bm r_\perp) \in L, \\
\psi_{M, E}, & (x, \bm r_\perp) \in M, \\
\phi_{RnE}^- + \sum_{n'}r'_{n'n}\phi^+_{Rn'E}, & (x, \bm r_\perp) \in R.
\end{cases}
$$

### Unitarity of the S-matrix

因为要求两侧的概率流是守恒的, 因此有$|\bm c_\text{in}|^2 = |\bm c_\text{out}|^2$, 要求$\bm S$必须是幺正的. 展开这一条件会得到:
$$\begin{gathered}
1 = \bm r^\dagger \bm r + \bm t^\dagger \bm t = \bm r'^\dagger \bm r' + \bm t'^\dagger \bm t', \\
0 = \bm r^\dagger \bm t' + \bm t^\dagger \bm r' = \bm t'^\dagger \bm r + \bm r'^\dagger \bm t, \\
1 = \bm r' \bm r'^\dagger + \bm t \bm t^\dagger = \bm r \bm r^\dagger + \bm t' \bm t'^\dagger,\\
0 = \bm r \bm t^\dagger + \bm t' \bm r'^\dagger = \bm t \bm r^\dagger + \bm r' \bm t'^\dagger.
\end{gathered}$$

这一性质也可以通过显式地写下电流看出来:
$$
I(x) = \int_\Omega \mathrm d \bm r_\perp \Psi^*(x, \bm r_\perp)\overleftrightarrow{J_x}\Psi(x, \bm r_\perp), \quad \overleftrightarrow{J_x} = \frac{1}{2mi}\left(\overrightarrow{\partial_x} - \overleftarrow{\partial_x}\right).
$$
通过稳态下的电荷守恒方程$\partial_x J = - \dot{\rho} = 0$, 可以知道$I(x)$实际上是和$x$无关的, 我们在$L$或者$R$上计算的电流可以用到另一边.

左侧电流:
$$\begin{aligned}
I_L(x) = & \int_\Omega \mathrm d\bm r_\perp 
\left(\bm a^+ \cdot \bm \phi^+_{L, E} + \bm a^- \cdot \bm \phi^-_{L, E}\right)^* \overleftrightarrow{J_x} \left(\bm a^+ \cdot \bm \phi^+_{L, E} + \bm a^- \cdot \bm \phi^-_{L, E}\right)\\
= & \frac{1}{m}\left(|\bm a^+|^2 - |\bm a^-|^2\right), \\
= & \frac{1}{m}\left(|\bm a^+|^2 - |\bm r \bm a^+ + \bm t'\bm b^-|^2\right).
\end{aligned}$$
右侧电流:
$$
I_R(x) = \frac{1}{m}\left(-|\bm b^-|^2 + |\bm t \bm a^+ + \bm r'\bm b^-|^2\right).
$$
利用$I_L(x) = I_R(x)$也可以得到上面的关系.

### Time-reversal symmetry

具有时间反演对称性的Hamiltonian满足$H = H^*$, 这给出$\bm S^T = \bm S$.

如果系统中有磁场$\bm B = \nabla \times \bm A$, $-\frac{1}{2m}\nabla^2 \rightarrow -\frac{1}{2m}(\nabla + ie \bm A)^2$. Hamiltonian满足$H_{\bm B} = H^*_{-\bm B}$. 如果$\Psi_{\bm B}(\bm r)$是一个本征态, $\Psi_{-\bm B}^*(\bm r)$也是有相同能量的本征态. 一个直观的理解是: 当考虑包含磁场的时间反演的时候, 应该把产生磁场的电流反向, 也就是取相反方向的磁场.

考虑一个本征态$\Psi_{\bm B} = (\bm c_\text{in}\phi_\text{in}, \bm c_\text{out} \phi_\text{out})$, 自然有另一个态$\Psi^\text{new}_{-\bm B} = \Psi^*_{\bm B}$是磁场反向的系统中的相同能量的本征态. 这里相当于两个时间反演的系统, 考虑时间反演会给出相反的流的方向, $\bm c^\text{new}_\text{in} = \bm c^*_\text{out}$, $\bm c^\text{new}_\text{out} = \bm c^*_\text{in}$. 那么
$$
\bm c^\text{new}_\text{out} = \bm c^*_\text{in}  = \bm S_{-\bm B} \bm c^*_\text{out} = \bm S_{-\bm B}\bm S_{\bm B}^* \bm c^*_\text{in},
$$
由此可以得到
$$
\bm S_{\bm B} = \bm S_{-\bm B}^T.
$$

## Conductance and transmission coefficients

我们将从直观的以及基于线性响应的两种方法得到上述介观系统的零温电导
$$
G(\mu) = \frac{2e^2}{h}\sum_n\mathcal T_n(\mu) = \frac{2e^2}{h}\mathrm{Tr}(\bm t(\mu)^\dagger \bm t(\mu)),
$$
其中$\mathcal T_n$是$\bm t^\dagger \bm t$的特征值.

### The Landauer formula, heuristic derivation

两边的电子源出射的电子都已经热化, 服从费米分布, 考虑到介观系统的线度小于能量弛豫长度, 我们认为散射态$\psi_{\alpha nE}$也按照$f_\alpha(\varepsilon) = n_F(\varepsilon - \mu_\alpha)$分布.

考虑一个左散射态$\psi_{LnE}$, 满足$(\bm a^+(\psi_{LnE}))_{n'} = \delta_{nn'}$和$(\bm b^-(\psi_{RnE}))_{n'} = 0$, 可以很轻松地得到电流
$$
I_{LnE} = \frac{1}{m}\left[1 - (\bm r^\dagger(E)\bm r(E))_{nn}\right] = \frac{1}{m}(\bm t^\dagger(E)\bm t(E))_{nn},
$$
一个右散射态给出电流
$$
I_{RnE} = - \frac{1}{m}(\bm t'^\dagger(E)\bm t'(E))_{nn} = \frac{1}{m}\left[-1 + (\bm r'^\dagger(E)\bm r(E))_{nn}\right].
$$

从电流就是这些不同散射态的电流叠加 (已经考虑了电子自旋的二重简并)
$$\begin{aligned}
I_e & = -2e \sum_{\alpha n E}I_{\alpha n E}f_\alpha(E) \\
& = \frac{-2e}{2\pi} \sum_n \int_{0}^\infty \mathrm dE
\left[(\bm t^\dagger \bm t)_{nn}n_F(E - \mu_L) - (\bm t'^\dagger \bm t')_{nn}n_F(E - \mu_R)\right] \\
& = \frac{-e}{\pi} \sum_n \int_{0}^\infty \mathrm d E\ (\bm t^\dagger(E)\bm t(E))_{nn}
\left[n_F(E - \mu + eV_L) - n_F(E - \mu  + eV_R)\right]\\
& \approx \frac{2e^2}{h} \int_0^\infty \mathrm dE \ \mathrm{Tr}(\bm t^\dagger(E) \bm t(E))
\left(-\frac{\partial n_F}{\partial E}(V_L - V_R)\right) \quad \text{(low voltage)}\\
& \approx \frac{2e^2}{h} \int_0^\infty \mathrm dE \ \mathrm{Tr}(\bm t^\dagger(E) \bm t(E))
\delta(E - \mu)(V_L - V_R) \quad \text{(low temperature)} \\
& = \frac{2e^2}{h}(V_L - V_R) \mathrm{Tr}(\bm t^\dagger(\mu) \bm t(\mu)).
\end{aligned}$$

由此得到零温下的电导
$$
G(\mu, 0) = \frac{2e^2}{h}\sum_n\mathcal T_n(\mu).
$$
这就是 Landauer 公式. 如果不考虑电子自旋的简并, 取迹时需要包括自旋自由度.

### The Landauer formula, linear response derivation

电导可以通过计算流-流关联函数得到:
$$
G(\omega) = - \frac{2e^2}{\omega}\mathrm{Im}
\int_{-\infty}^\infty \mathrm dt e^{i(\omega + i\eta)}(-i)\theta(t)\langle [I(x, t), I(x, 0)] \rangle_0.
$$
电流算符是:
$$\begin{gathered}
I(x) = \sum_{\lambda \lambda'} j_{\lambda\lambda'}(x)c_{\lambda}^\dagger c_{\lambda'}, \\
\begin{aligned}
j_{\lambda\lambda'}(x) = &\frac{1}{2mi}\int_\Omega \mathrm d\bm r_\perp \psi^*_{\lambda}(x, \bm r_\perp)\left(\overrightarrow{\partial_x} - \overleftarrow{\partial_x}\right)\psi_{\lambda'}(x, \bm r_\perp). \\
\end{aligned}
\end{gathered}$$
首先计算对易子:
$$\begin{aligned}
\langle [I(x', t), I(x', 0)] \rangle_0 & = \sum_{\nu\nu'\lambda\lambda'}j_{\nu\nu'}(x)j_{\lambda\lambda'}(x')e^{i(E_\lambda - E_{\lambda'})t}
\langle [c_\lambda^\dagger c_{\lambda'}, c_{\nu}^\dagger c_{\nu'}]\rangle_0 \\
& = \sum_{\lambda\lambda'\nu\nu'}j_{\nu\nu'}(x)j_{\lambda\lambda'}(x')e^{i(E_\lambda - E_{\lambda'})t} \langle c_\lambda^\dagger c_{\lambda'} c_{\nu}^\dagger c_{\nu'} - c_{\nu}^\dagger c_{\nu'}c_{\lambda}^\dagger c_{\lambda'} \rangle_0 \\
& = \sum_{\lambda\lambda'\nu\nu'}j_{\nu\nu'}(x)j_{\lambda\lambda'}(x')e^{i(E_\lambda - E_{\lambda'})t} 
\langle \delta_{\lambda \nu'}\delta_{\lambda' \nu}n_F E_\lambda(1 - n_F(E_\lambda')) - \delta_{\lambda \nu'}\delta_{\lambda' \nu}n_F E_\lambda'(1 - n_F(E_\lambda)) \rangle_0 \\
& = \sum_{\lambda\lambda'}|j_{\lambda\lambda'}(x)|^2e^{i(E_\lambda - E_{\lambda'})t}(n_F(E_\lambda) - n_F(E_{\lambda'})).
\end{aligned}$$
这样就得到
$$
G(\omega) = \frac{2e^2}{\omega} \mathrm{Im}\sum_{\lambda\lambda'}
\frac{|j_{\lambda\lambda'}(x)|^2}{\omega + i\eta + E_\lambda - E_\lambda'}\left[n_F(E_\lambda) - n_F(E_\lambda')\right],
$$
在直流极限下
$$
G(0) = 2e^2\pi\sum_{\lambda\lambda'}|j_{\lambda\lambda'}(x)|^2\left(-\frac{\partial n_F(E)}{\partial E}\right)\delta(E_\lambda - E_{\lambda'}) = 2e^2 \pi (m/2\pi)^2\sum_{nn', \alpha\alpha'}|j_{\alpha n\mu, \alpha' n'\mu}(x)|^2.
$$
可以写下连续性方程
$$
\langle \lambda | \nabla\cdot \bm J | \lambda'\rangle = - \langle \lambda | \dot \rho | \lambda' \rangle = -i \langle \lambda|[H, \rho]|\lambda' \rangle = -i(E_\lambda - E_{\lambda'})\langle \lambda | \rho |\lambda' \rangle = 0, \quad \text{with }E_\lambda = E_{\lambda'}.
$$
由此得到$j_{\alpha n\mu, \alpha' n'\mu}(x)$不随$x$变化, 可以得到
$$
j_{\alpha n\mu, \alpha' n' \mu}(x') = \frac{1}{m}\begin{pmatrix}
(\bm t^\dagger \bm t)_{nn'} & (\bm t^\dagger \bm r')_{nn'} \\
-(\bm t'\dagger \bm r)_{nn'} & -(\bm t'^\dagger \bm t')_{nn'}
\end{pmatrix} \equiv \frac{1}{m}\bm j,
$$
其中行列的指标是$\alpha, \alpha' = L, R$. 进一步有
$$
\sum_{nn', \alpha\alpha'}|j_{\alpha n\mu, \alpha' n' \mu}(x')|^2 = \frac{2}{m^2}\mathrm{Tr}(\bm t^\dagger \bm t).
$$
我们再次得到了 Landauer 公式:
$$
G(0) = \frac{2e^2}{h}\mathrm{Tr}(\bm t^\dagger \bm t).
$$

### The Landauer-Buttiker formalism for multiprobe systems

前面考虑的是两个电极的情况,
$$\begin{aligned}
I(V_L, V_R) = & \frac{2e^2}{h} \int_0^\infty \mathrm dE \ \mathrm{Tr}(\bm t^\dagger \bm t)
\left(-\frac{\partial n_F}{\partial E}(V_L - V_R)\right) \\
= & \frac{2e^2}{h}\sum_{nn'}\int_0^\infty \mathrm dE \left(-\frac{\partial n_F}{\partial E}\right)
\left(|t_{n'n, RL}|^2 V_L - |t_{nn', LR}|^2 V_R\right).
\end{aligned}$$
两项分别对应从左到右和从右到左的不同通道之间的散射. 

现在可以简单地推广到多极的情况, $\alpha$表示不同的电极, 某个电极上通过的电流是
$$
I_\alpha = \frac{2e^2}{h}\sum_{\alpha' \neq \alpha}\int_0^\infty \mathrm dE\left(-\frac{\partial n_F}{\partial E}\right)(T_{\alpha'\alpha}V_\alpha - T_{\alpha\alpha'}V_{\alpha'}),
$$
其中$T_{\alpha'\alpha} = \sum_{nn'}|t_{n'n, \alpha\alpha'}|^2$.

## Electron wave guides

### Quantum point contact and conductance quantization

在2DEG的两边加一定的电势, 可以精确地控制2DEG在一定范围内的宽度, 从而精确地操控电导.

考虑2DEG的形状, 随着电流方向在缓变, 要求其曲率半径总是远大于电子的波长. 更具体地, 考虑
$$
\left[- \frac{1}{2m} (\partial_x ^2 + \partial_y^2) + V_\text{conf}(x, y)\right]\Psi(x, y) = E\Psi(x, y).
$$
要求限制势$V(x, y)$在$x$方向是光滑且缓变的. 这样我们可以近似地分离变量$\Psi(x, y) = \sum_n \phi_n(x)\chi_{nx}(y)$ (其实是按照本征函数$\chi_{nx}$展开, 这就是Born-Oppenheimer近似的步骤). $y$部分的波函数满足
$$
\left[-\frac{1}{2m} \partial_y^2 + V_{conf}(x, y)\right]\chi_{nx}(y) = \varepsilon_n(x)\chi_{nx}(y).
$$
可以得到$\phi_n(x)$满足的方程 
$$
\left[-\frac{1}{2m}\partial_x^2 + \varepsilon_n(x)\right]\phi_n(x) = E\phi_n(x) + \delta n,
$$
其中
$$
\delta_n = \frac{1}{m}\int \mathrm dy \chi^*_{nx}(y)
\left[\partial_x \phi_{n'}(x)\partial_x \chi_{n'x}(y) + \frac{1}{2}\phi_{n'}(x)\partial_x^2 \chi_{n'x}(y)\right].
$$
我们之前考虑缓变的势, 因此有$\partial_x \chi_{nx} \approx 0$, $\delta_n$可以忽略.

特别地考虑这样的势
$$
V_\text{conf}(x, y) = \begin{cases}
0,\quad \text{for } y \in [-d(x)/2, d(x)/2],\\
\infty, \quad \text{otherwise}.
\end{cases}
$$
这给出在$y$方向的特征值$\varepsilon_n(x) = \frac{\pi^2n^2}{2m[d(x)]^2}$. $\varepsilon_n(x)$在$x$方向上实际上充当了势垒, 当$E > \varepsilon_n^{\max}$时, 电子可以通过, 这时前$n$个通道都是开放的. 在实验上增加电压, 相当于调节势垒的高度, 每个可以通过的势垒 (通道) 会给出$\frac{2e^2}{h}$的电导.