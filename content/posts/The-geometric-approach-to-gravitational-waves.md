---
title: The geometric approach to gravitational waves
date: '2025-05-28T15:29:07+08:00'
categories:
- 广义相对论
featured_image: /images/b4e19854bd3249e183a1.jpg
---


A note for Chap 1-4, Vol 1 of Michele Maggioore's *Gravitational waves*.

---

# The geometric approach to GWs

## Expansion around flat space

一个引力系统的作用量是$S = S_E + S_M$, 其中
$$
S_E = \frac{c^3}{16\pi G} \int \mathrm d^4 x \sqrt{-g}R
$$
是Einstein作用量, $S_M$表示物质的作用量. 如果我们考虑度规的一个小变化, 这会导致$S_M$出现一个对应的小变化(关于下面的表达式: 实际上这是$T^{\mu\nu}$的定义),
$$
\delta S_M = \frac{1}{2c}\int \mathrm d^4 x \sqrt{-g} T^{\mu\nu}\delta g_{\mu\nu}.
$$
那么对于度规$g_{\mu\nu}$的变分给出Einstein场方程
$$
R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \frac{8\pi G}{c^4}T_{\mu\nu}.
$$
上面的理论有一个很大的规范对称性, 对应于任意一个坐标变换(应该是一个微分同胚)$x^\mu \rightarrow x'^{\mu}(x)$.

现在我们的目标是得到波动方程, 一个想法是**线性化**Einstein方程, 我们把度规在平直空间附近展开,
$$
g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}, \quad |h_{\mu\nu}| \ll 1. 
$$
实际上这一步意味着我们在问题所关心的一定区域里, 选取了一个很接近惯性系的参考系. 这种做法消除了一定的规范自由度, 但是还不能得到完全独立的变量, 为了验证这一点, 考虑如下的规范变换,
$$
x^\mu \rightarrow x'^\mu = x^\mu + \xi^\mu(x).
$$
这里$|\partial_\mu \xi_\nu|$最高和$|h_{\mu\nu}|$是一个量级. 这个坐标变换诱导了度规的变换,
$$
h_{\mu\nu} \rightarrow h'_{\mu\nu}(x') = h_{\mu\nu}(x) - (\partial_\mu \xi_\nu + \partial_\nu \xi_\mu).
$$
特别地, 考虑一个Lorentz变换, $x^\mu \rightarrow \Lambda^\mu_\nu x^\nu$, 满足$\Lambda_\mu^\rho \Lambda^\sigma_\nu \eta_{\rho\sigma} = \eta_{\mu\nu}$, 给出的度规的变换是
$$\begin{aligned}
g_{\mu\nu}(x) \rightarrow g'_{\mu\nu}(x') = & \Lambda_\mu^\rho \Lambda_\nu^\sigma g_{\rho\sigma}(x) \\
= & \Lambda_\mu^\rho \Lambda_\nu^\sigma (\eta_{\rho\sigma} + h_{\rho\sigma}(x))\\
= & \eta_{\mu\nu} + \Lambda_\mu^\rho \Lambda_\nu^\sigma h_{\rho\sigma}(x).
\end{aligned}$$
这样我们就得到在Lorentz变换下$h$的变换方式, 
$$
h'_{\mu\nu}(x') = \Lambda_{\mu}^{\rho}\Lambda_{\nu}^{\sigma} h_{\rho\sigma}(x).
$$
这说明$h$是一个在Lorentz变换下的张量, Lorentz变换不会破坏$|h_{\mu\nu}| \ll 1$的条件. 此外, 对于时空平移$x^\mu \rightarrow x'\mu = x^\mu + a^\mu$, $h_{\mu\nu}$不变. 这说明我们线性化的理论有着完整的有限Poincare变换对称性.

现在我们要把方程中剩下的量也线性化了, 首先是Riemann张量,
$$
R_{\mu\nu\rho\sigma} = \frac{1}{2}(\partial_\nu\partial_\rho h_{\mu\sigma} +
\partial_\mu\partial_\sigma h_{\nu\rho} -
\partial_\mu \partial_\rho h_{\nu\sigma} -
\partial_\nu\partial_\sigma h_{\nu\rho}
).
$$
能看出Riemann张量在$h_{\mu\nu}$的变换下是不变的.

我们可以把线性化的理论以一种更紧凑的方式写下来, 首先定义
$$
h = \eta^{\mu\nu} h_{\mu\nu}.
$$
然后令
$$
\bar{h}_{\mu\nu} = h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu}h.
$$
这给出$\bar{h} = -h$. 那么反过来也有
$$
h_{\mu\nu} = \bar{h}_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu}\bar{h}.
$$
可以注意到在线性化的理论中我们只需要平直时空度规$\eta_{\mu\nu}$. 那么现在我们可以写下线性化的Einstein方程,
$$
\partial_\rho\partial^\rho \bar{h}_{\mu\nu} +
\eta_{\mu\nu}\partial^{\rho}\partial^{\sigma}\bar{h}_{\rho\sigma} -
\partial^\rho\partial_\nu \bar{h}_{\mu\rho} - 
\partial^\rho \partial_\mu \bar{h}_{\nu\rho} =
-\frac{16\pi G}{c^4}T_{\mu\nu}.
$$
为了解这个方程, 我们需要彻底移除规范自由度, 为此我们还需要坐标条件. 这里我们使用Lorentz规范(或称Hilbert规范, 和谐规范, De Donder规范)
$$
\partial^\nu \bar{h}_{\mu\nu} = 0.
$$
上边的场方程能确定$6$个自由度(因为方程左边自动满足$\partial^\mu G_{\mu\nu} = 0$), 那么剩下的四个自由度就由坐标条件给出.

$\bar{h}$的变换由下式给出
$$
\bar{h}_{\mu\nu} \rightarrow \bar{h}'_{\mu\nu} = \bar{h}_{\mu\nu} - (\partial_\mu \xi_\nu + \partial_\nu \xi_\mu - \eta_{\mu\nu}\partial_\rho\xi^\rho).
$$
那么
$$
\partial^\nu \bar{h}_{\mu\nu} \rightarrow (\partial^\nu \bar{h}_{\mu\nu})' = \partial^\nu \bar{h}_{\mu\nu} - \partial^\rho\partial_\rho \xi_\mu.
$$
如果某个坐标下, $\partial^\nu \bar{h}_{\mu\nu} = f_\mu(x)$, 我们只需要取坐标变换$\xi^\mu$满足$\partial_\nu\partial^\nu \xi_\mu = f_\mu(x)$即可使得$(\partial^\nu \bar{h}_{\mu\nu})' = 0$. 这说明**总是可以取合适的坐标变换以使度规满足和谐坐标条件**. 这在这个坐标条件下, 线性化的Einstein方程得以大大简化
$$
\partial^\rho \partial_\rho \bar{h}_{\mu\nu} = -\frac{16\pi G}{c^4}T_{\mu\nu}.
$$

## The transverse-traceless gauge

我们考虑无源引力波, 对应的波动方程是
$$
\square \bar{h}_{\mu\nu} = 0.
$$
类似于在电磁场中考虑平面波的解, 这时即使时和谐坐标条件也没有完全确定规范: 考虑坐标变换$x^\mu \rightarrow x^\mu + \xi^\mu$, 如果$\square \xi_\mu = 0$, 那么$\square \xi_{\mu\nu} = 0$, 这里$\xi_{\mu\nu}$被定义为
$$
\xi_{\mu\nu} \equiv \partial_\mu \xi_\nu + \partial_\nu\xi_\mu - \eta_{\mu\nu}\partial_\rho \xi^\rho.
$$
这说明我们可以任意地变换$\bar{h}_{\mu\nu} \rightarrow \bar{h}_{\mu\nu} - \xi_{\mu\nu}$, 依旧满足上面的波动方程. 为了方便起见, 我们使用这种规范: 首先, 选择$\xi^0$使得$\bar{h} = 0$, 这使得$\bar{h}_{\mu\nu} = h_{\mu\nu}$; 然后我们可以选取$\xi^{i}$使得$h^{0i} = 0$. 现在和谐坐标条件($\mu = 0$)给出
$$
\partial^0 h_{00} = 0.
$$
这说明$h_{00}$是不随时变的, 因为我们考虑的引力波是时变的, 所以取$h_{00} = 0$. 现在$h_{\mu\nu}$只剩下空间分量可能非零. 结合和谐坐标条件, 我们得到$h_{\mu\nu}$需要满足的要求
$$
h^{0\mu} = 0, \quad h^i_{\ i} = 0, \quad \partial^j h_{ij} = 0.
$$
上面的规范称作**横向无迹规范(transverse-traceless gauge)**, 或者简称TT规范, 满足TT规范的度规记作$h^{\mathrm{TT}}_{ij}$, 只有$2$个自由度. 如此少的自由度是无源方程的特性, 在有源的情况下$\square \bar{h}^{\mu\nu} \neq 0$, 在选取了和谐坐标条件之后, 我们还是可以选择$\square \xi^\mu=0$的坐标变换, 这并不影响波动方程, 但是不能使得通过坐标变换使得$\bar{h}^{\mu\nu}$中某些元素成为$0$.

现在来具体看波动方程解的形式, $h_{ij}^{\mathrm{TT}}(x) = e_{ij}(k)e^{ikx}$, 其中的$e_{ij}$称作极化张量. TT规范要求$k^j h_{ij} = 0$, 如果选取$\hat{n} = k / |k|$, $h^{\mathrm{TT}}_{ij}$应该有如下的形式
$$
h^{\mathrm{TT}}_{ij}(t, z) = \begin{pmatrix}
h_+ & h_\times & 0 \\
h_\times & -h_+ & 0 \\
0 & 0 & 0
\end{pmatrix}_{ij} \cos(\omega(t - z/c)).
$$
或者更紧凑地, 我们可以取$a, b = 1, 2$来表示非零分量. 现在线元表示为
$$\begin{aligned}
\mathrm ds^2 = & -c^2 \mathrm dt^2 + \mathrm dz^2 \\
& + (1 + h_+\cos(\omega(t - z/c)))\mathrm dx^2 + (1 - h_+\cos(\omega(t - z/c)))\mathrm dy^2 \\
& + 2h_\times \cos(\omega(t - z/c))\mathrm dx \mathrm dy.
\end{aligned}$$

现在如果有一个沿着$\hat{n}$方向传播的平面波$h_{\mu\nu}(x)$, 满足和谐坐标条件, 但是并不满足TT规范, 我们可以把它投影到满足TT规范的波上. 首先构造如下的投影算符
$$
P_{ij}(\hat{n}) = \delta_{ij} - n_in_j, 
$$
这个算符是对称的, 并且是横向的($n^i P_{ij}(\hat{n}) = 0$), 它的迹是$P_{ii} = 2$. 然后可以构造另一个投影算符
$$
\Lambda_{ij, kl}(\hat{n}) = P_{ik}P_{jl} - \frac{1}{2}P_{ij}P_{kl}.
$$
具有如下的性质
- 投影算符: 满足$\Lambda_{ij, kl}\Lambda_{kl, mn} = \Lambda_{jl, mn}$;
- 在所有指标上都是横向的: $n^{i}\Lambda_{ij, kl} = 0$;
- 它的$(i, j)$和$(k, l)$的偏迹都是$0$: $\Lambda_{ii, kl} = \Lambda_{ij, kk} = 0$;
- 在指标交换$(i, j) \leftrightarrow (k, l)$下是对称的.

这个投影算符叫做Lambda张量, 具体地把它用$\hat{n}$写下的形式为
$$\begin{aligned}
\Lambda_{ij, kl}(\hat{n}) = & \delta_{ik}\delta_{jl} - \frac{1}{2}\delta_{ij}\delta_{kl} - n_jn_l\delta_{ik} - n_in_k\delta_{jl}  \\
& + \frac{1}{2}n_kn_l\delta_{ij} + \frac{1}{2}n_in_j\delta_{kl} + \frac{1}{2}n_in_jn_kn_l.
\end{aligned}$$

Lambda的作用是把一个平面波投影到TT规范上, 
$$
h^{\mathrm{TT}}_{ij} = \Lambda_{ij, kl}h_{kl}.
$$
根据$\Lambda_{ij, kl}$的性质, 可以明显地看出来, 方程的右边是无迹且横向的, 并且也满足波动方程.

把一般的满足$\square h^{\mathrm{TT}}_{ij} = 0$的$h^{\mathrm{TT}}_{ij}$按照平面波展开得到
$$
h^{\mathrm{TT}}_{ij}(x) = \int \frac{\mathrm d^3 k}{(2\pi)^3}
\left(\mathcal A_{ij}(k)e^{ikx} + \mathcal A^*_{ij}(k)e^{-ikx}\right).
$$
用频率$f$表示$k$的模长, $\hat{n}$表示方向, 上式写成
$$
h^{\mathrm{TT}}_{ij}(x) = \frac{1}{c^3} \int_0^\infty \mathrm df f^2 \int \mathrm d^2 \hat{n}
\left(\mathcal A_{ij}(f, \hat{n})e^{-2\pi i f(t - \hat{n}\cdot x/c)} + h.c.\right)
$$
TT规范中的横向条件给出$k^i \mathcal A_{ij}(k) = 0$. 对于多个平面波叠加的解来说, $h_{ij}$并不会约化成$2\times 2$矩阵. 但是当观察远方信号源发出的引力波的时候, $\hat{n}$对于不同成分是确定的, 我们可以取
$$
\mathcal A_{ij}(k) = A_{ij}(f)\delta^{(2)}(\hat n - \hat n_0).
$$
在这种情况下, $h_{ij}$又会约化成$2\times 2$矩阵, 
$$\begin{gathered}
h_{ab}(t, x) = \int_0^\infty \mathrm df
\left(\tilde{h}_{ab}(f, x)e^{-2\pi i ft} + h.c.\right), \\
\tilde{h}_{ab}(f, x) = \frac{f^2}{c^3}\mathcal A_{ab}(f)e^{2\pi i f \hat n_0 \cdot x/c}.
\end{gathered}$$

对于地面上的**单一**探测器来说, 其线度远小于引力波的波长, 在这种情况下可以忽略引力波对于$x$的依赖.

另一种常见的表示方式是利用极化张量$e^{A}_{ij}(\hat{n})$, 
$$
e^+_{ij}(\hat{n}) = \hat{u}_i\hat{u}_j - \hat{v}_i\hat{v}_j, \quad
e^\times_{ij}(\hat{n}) = \hat{u}_i\hat{v}_j + \hat{v}_i\hat{u}_j.
$$
上面的$\hat{u}, \hat{v}, \hat{n}$构成一组正交坐标架. 极化张量有如下的归一化关系
$$
e^A_{ij}(\hat{n})e^{A', ij}(\hat{n}) = 2\delta^{AA'}.
$$
最简单的情况是$\hat{n} = \hat{z}$, 那么就取$\hat{u} = \hat{x}$, $\hat{v} = \hat{y}$. 这样$e^+ = \sigma^z$, $e^\times = \sigma^x$. 我们可以定义$\tilde{h}_A(f, \hat n)$,
$$
\frac{f^2}{c^3}\mathcal A_{ij}(f, \hat n) = \sum_{A}\tilde{h}_A(f, \hat n)e^A_{ij}(\hat n).
$$
完整的波动可以利用此写成
$$
h_{ab}(t, x) = \sum_A \int \mathrm df \int \mathrm d^2 \hat n
\tilde{h}_A(f, \hat n)e^A_{ab}(\hat n)e^{-2\pi i f(t - \hat n \cdot x/c)}.
$$

## Interaction of GWs with test masses

接下来我们考虑引力波和有质量物体的相互作用, 作为探测引力波的手段. 考虑到在TT规范下, 引力波的形式很简单, 我们希望知道TT规范对应于什么坐标系.

### Geodesic equation and geodesic deviation

考虑两条近邻的测地线
$$\begin{gathered}
\frac{\mathrm d u^\mu}{\mathrm d\tau} + \Gamma_{\nu \rho}^{\mu}u^\nu u^\rho = 0,\\
\frac{\mathrm d^2 (x^\mu + \xi^\mu)}{\mathrm d\tau^2} + \Gamma_{\nu \rho}^{\mu}(x + \xi)\frac{\mathrm d(x^\nu + \xi^\nu)}{\mathrm d\tau} \frac{\mathrm d(x^\rho + \xi^\rho)}{\mathrm d\tau} = 0.
\end{gathered}$$
上面的两条测地线有各自的$\tau$, $\xi^\mu$把两条测地线上有相同$\tau$的点对应起来. 如果$\xi$很小, 得到
$$
\frac{\mathrm d^2 \xi^\mu}{\mathrm d\tau^2} + 2\Gamma^\mu_{\nu\rho}\frac{\mathrm dx^\nu}{\mathrm d\tau}\frac{\mathrm d\xi^\rho}{\mathrm d\tau} + 
\xi^\sigma \partial_\sigma \Gamma^\mu_{\nu\rho}\frac{\mathrm d x^\nu}{\mathrm d\tau} \frac{\mathrm dx^\rho}{\mathrm d\tau} = 0
$$
这就是测地微分方程, 如果引入协变导数
$$
\frac{\mathrm D V^\mu}{\mathrm D\tau} \equiv \frac{\mathrm dV^\mu}{\mathrm d\tau} + \Gamma^\mu_{\nu\rho}V^\nu\frac{\mathrm dx^\rho}{\mathrm d\tau},
$$
可以以更简洁的方式写出
$$
\frac{\mathrm D^2 \xi^\mu}{\mathrm D\tau^2} = -R^\mu_{\ \ \nu\rho\sigma}\xi^\rho\frac{\mathrm dx^\nu}{\mathrm d\tau}\frac{\mathrm d x^\sigma}{\mathrm d\tau}.
$$

### Local inertial frames and freely falling frames

在时空中的一点$P$, 总存在一个坐标变换, 使得$\Gamma^\mu_{\nu\rho}(P) = 0$, 在这样的坐标下, 点$P$处的测地微分方程成为
$$
\left.\frac{\mathrm d^2 x^\mu}{\mathrm d\tau^2}\right|_P = 0.
$$
这样的坐标系就是局域惯性系(local inertial frame, LIF).

对于这种坐标, 显示的构造是如下. 在$P$处, 选择一组局部正交基$e_\alpha$, $\eta_{\mu\nu}e^\mu_\alpha e^\nu_\beta = \eta_{\alpha\beta}$. 考虑一条在$P$处切方向是$n$的类空测地线, 以及这条测地线上距离$P$为$s$的一点$Q$. 可以把$Q$的坐标写成$x_Q = (sn^0, sn^1, sn^2, sn^3)$. 类似地, 如果是一条类时测地线, $Q$的坐标参数化为$(\tau n^0, \tau n^1, \tau n^2, \tau n^3)$. 我们现在可以把整个时空使用类时的或者类空的测地线填满, 在$P$的附近的一个小区域中, 测地线之间并不相交(bananice!), 这样在这个小区域中, 每个点都有且只有一条测地线经过, 在这个小区域中我们可以通过上面的方法参数化每个点. 这样的坐标叫做Riemann正规坐标(Riemann normal coordinates), 给出了局域惯性系的一个实现:

首先$\eta_{\mu\nu}e^\mu_{\alpha}e^\nu_\beta = \eta_{\alpha\beta}$给出了$g_{\mu\nu} = \eta_{\mu\nu}$. 此外Riemann正规坐标, 对于固有时间(长度)是线性的, $\frac{\mathrm dx^\mu}{\mathrm d\tau} = n^\mu$, 这样测地线方程是
$$
\Gamma^\mu_{\nu\rho}(P)n^\nu n^\rho = 0.
$$
上面的结果对于任意$n$都成立, 说明$\Gamma^\mu_{\nu\rho} = 0$. 这说明Riemann正规坐标提供了一个局域惯性系.

现在我们可以进一步在一整条测地线上都定义局域惯性系. 考虑一个自由物体(比如陀螺仪), 其运动满足
$$
\frac{\mathrm ds^\mu}{\mathrm d\tau} + \Gamma^\mu_{\nu\rho}s^\nu\frac{\mathrm dx^\rho}{\mathrm d\tau} = 0,
$$
其中$s$是一个自旋4-矢量(spin four-vector), 在静止系中约化成$s^\mu = (0, \bm s)$, 上面的方程是$\mathrm ds^\mu/ \mathrm d\tau = 0$的协变形式. 我们先在$P$点处构建一个局域惯性系, 然后根据3个陀螺仪, 可以确定空间方向. 然后可以沿着测地线移动参考系, 空间方向始终指向陀螺仪. 这样定义的一组坐标中$\mathrm ds^\mu / \mathrm d\tau = 0$, 这种定义下$\Gamma^\mu_{\nu\rho}$的值始终为零. 这样的坐标称作自由落体系, 或者Fermi正规坐标.

### TT frame and proper detector frame

#### The TT frame

如果一个质点在$\tau = 0$时是静止的, 它的运动由测地线方程给出
$$
\left.\frac{\mathrm d^2 x^i}{\mathrm d\tau^2}\right|_{\tau=0} = -
\left[\Gamma^i_{\nu\rho}(x)\frac{\mathrm dx^\nu}{\mathrm d\tau}\frac{\mathrm dx^\rho}{\mathrm d\tau}\right]_{\tau=0} = -\left[\Gamma^i_{00}\left(\frac{\mathrm d x^0}{\mathrm d\tau}\right)^2\right]_{\tau = 0}.
$$

把上面的方程展开到线性阶, 联络展开到线性阶是
$$
\Gamma^\mu_{\nu\rho} = \frac{1}{2}\eta^{\mu\sigma}(\partial_\nu h_{\rho\sigma} + \partial_\rho h_{\nu\sigma} - \partial_\sigma h_{\nu\rho}).
$$
那么
$$
\Gamma^{i}_{00} = \frac{1}{2}\left(2\partial_0 h_{0i} - \partial_i h_{00}\right).
$$
在TT规范下, $h_{00} = h_{i0} = 0$, 那么$\Gamma^i_{00} = 0$. 那么在TT规范下, 一个静止质点的$\mathrm d^2 x^i / \mathrm d\tau^2 = 0$, 因此它将永远静止. 这意味这在TT规范下, 在引力波到达之前静止的粒子, 在引力波到达之后仍然是静止的, 起码到线性阶是如此. 这样我们可以在使用质点, 作为TT规范下空间坐标的标记, 它们在有引力波的情况下, 也是不动的.

我们还可以利用测地线微分方程说明, 在TT参考系下, 两个静止质点之间的距离$\xi^i$是不变的:
$$
\left.\frac{\mathrm d^2 \xi^2}{\mathrm d\tau^2}\right|_{\tau = 0} = - \left[2c\Gamma^i_{0\rho}\frac{\mathrm d\xi^\rho}{\mathrm d\tau} + c^2\xi^\sigma \partial_\sigma \Gamma^i_{00}\right].
$$
考虑到在$TT$规范下$\Gamma^i_{00} = 0$, 以及$\Gamma^i_{0j} = \frac{1}{2}\partial_0 h_{ij}$, 上面的方程变成:
$$
\left.\frac{\mathrm d^2 \xi^i}{\mathrm d\tau^2}\right|_{\tau = 0} = -\left[ \dot{h}_{ij}\frac{\mathrm d\xi^i}{\mathrm d\tau}\right],
$$
只要在$\tau = 0$时$\mathrm d\xi^i / \mathrm d\tau = 0$, 那么这个值将永远都是零.

在TT规范下, 我们能说的, 只是自由质点的位置, 以及相对位置不变, 但是它们之间的固有时间(长度)并非如此. 两个质点, 坐标差$x_2 - x_1 = L$保持不变. 但是如果有一个沿$z$轴传播的引力平面波, 它们之间的固有长度变成
$$
s = (x_2 - x_1)[1 + h_+\cos\omega t]^{1/2} \approx L(1 + \frac{1}{2}h_+\cos\omega t).
$$
作为一个更普遍的讨论, 如果两个点之间的相对位置是$\bm L$, 那么它们之间的固有长度是
$$
s^2 = L^2 + h_{ij}(t)L_iL_j.
$$
如果展开到线性项就是
$$
\ddot{s} \approx \frac{1}{2L}\ddot h_{ij}L_iL_j.
$$
可以定义$L_i / L$以及$s = n_i s_i$, 就有
$$
\ddot s_i \approx \frac{1}{2}\ddot h_{ij} L_j \approx \frac{1}{2}\ddot h_{ij}s_j.
$$
这就是测地线方程在固有长度下的表达方式.

#### The proper detector frame

TT坐标系在实验中是难以运用的. 利用Fermi正规坐标, 我们可以写下在一整条测地线上都是惯性系的坐标. 在此附近, 起码在$x^i$的线性阶, 不需要对于度规$\mathrm d s^2 \approx -c^2 \mathrm dt^2 + \delta_{ij}\mathrm dx^i \mathrm dx^j$的修正. 如果展开到二阶(利用$P$点的联络是零), 得到
$$
\mathrm ds^2 \approx -c^2 \mathrm dt^2 (1 + R_{0i0j}x^ix^j) -
2c\mathrm dt\mathrm dx^i \left(\frac{2}{3}R_{0ijk}x^jx^k\right) +
\mathrm dx^i \mathrm dx^j \left(\delta_{ij} - \frac{1}{3}R_{ikjl}x^kx^l\right).
$$

对于一个在地表的探测器, 情况要复杂很多, 一方面它不是自由落体的, 另一方面相对地面上的陀螺仪会旋转. 通过直接写出从局域惯性系到地面的坐标变换, 我们可以写下展开到二阶的度规
$$\begin{aligned}
\mathrm ds^2 \approx & -c^2 \mathrm dt^2\left[1 + \frac{2}{c^2}\bm a \cdot \bm x + \frac{1}{c^4}(\bm a \cdot \bm x)^2 - \frac{1}{c^2}(\bm \Omega \times \bm x)^2 + R_{0i0j}x^ix^j\right] \\ &+
2c\mathrm dt\mathrm dx^i \left[\frac{1}{c}\epsilon_{ijk}\Omega^j x^k - \frac{2}{3}R_{0jik}x^jx^k\right] \\& +
\mathrm dx^i \mathrm dx^j \left[\delta_{ij} - \frac{1}{3}R_{ikjl}x^kx^l\right].
\end{aligned}$$

具有上面形式度规的参考系称作固有探测器参考系(proper detector frame), 实际上在地面实验中使用的总是这种参考系. 如果规定$L_B$是度规变化的尺度, $r$是我们所关心的尺度, 那么$R_{ijkl} \sim 1/L_B^2$, 在$r \ll L_B$的范围内, 上面的度规退化成平直时空中的牛顿度规.

在这个度规下, 测地线方程的线性部分成为地表粒子的运动方程
$$
\frac{\mathrm d^2 x^i}{\mathrm d\tau} = -a^i - 2(\bm \Omega \times v)^i + \frac{f_i}{m} + O(x^i).
$$
$O(x^i)$项中包含了离心力. 引力波的探测限制在一定频率范围内, 过低的频率受到地表的其他作用影响过大, 过高的频率受到仪器噪声的影响太大. 在这样的频率范围内, 我们可以忽略Newton力学下给出的项, 只关心那些涉及Riemann张量的项, 也就是说我们又回到了自由落体系的度规.

分析引力波的影响, 我们可以使用测地线微分方程, 考虑到仪器的运动是非相对论性的, 一阶导中我们只需要考虑时间方向导数项, 这给出
$$
\frac{\mathrm d^2 \xi^i}{\mathrm d\tau^2} + \xi^\sigma \partial_\sigma \Gamma^i_{00} \left(\frac{\mathrm dx^0}{\mathrm d \tau}\right)^2 = 0
$$
度规中只含有空间坐标的修正, 这给出$\partial_0\Gamma^i_{0j} = 0$. 利用$R^i_{\ \ 0j0} = \partial_j \Gamma^i_{00} - \partial_0 \Gamma^{i}_{0j} = \partial_j \Gamma^{i}_{00}$, 上面的方程改写成
$$
\frac{\mathrm d^2 \xi^i}{\mathrm d \tau^2} = - R^i_{\ \ 0j0}\xi^j\left(\frac{\mathrm dx^0}{\mathrm d\tau}\right)^2.
$$
假如有一个质点开始静止, 在引力波经过之后获得了$\mathrm dx^i /\mathrm d\tau \sim cO(1)$的速度, 那么
$$
\mathrm dt^2 = \mathrm d\tau^2\left(1 + \frac{1}{c^2}\frac{\mathrm dx^i}{\mathrm d\tau}\frac{\mathrm dx^i}{\mathrm d\tau}\right) \sim \mathrm d\tau^2(1 + O(h^2)).
$$
这说明我们可以在线性阶忽略$\mathrm d\tau$和$\mathrm dt$的区别, 并且$\mathrm dx^0 /\mathrm d\tau = c$, 这给出
$$
\frac{\mathrm d^2 \xi^i}{\mathrm d \tau^2} = -c^2 R^i_{\ \ 0j0}\xi^j.
$$
现在需要计算Riemann张量, 根据我们之前的讨论, 只到线性阶, 坐标变换不影响Riemann张量的值, 我们可以在TT规范下计算:
$$
R^{i}_{\ \ 0j0} = R_{i0j0} = -\frac{1}{2c^2}\ddot h^{\mathrm{TT}}_{ij},
$$
现在测地线微分方程是
$$
\ddot \xi^i = \frac{1}{2}\ddot h^{\mathrm{TT}}_{ij}\xi^j.
$$
说明引力波的影响是给地面上的质点带来一个等效作用力, $F^i = \frac{m}{2}\ddot h^{TT}_{ij}\xi^j$. 如果我们关心固有长度的分量$s^i$, 那么上式在TT规范下也成立. 注意到$\partial_i F^i = \frac{m}{2}\ddot h^{\mathrm{TT}}_{ij}\delta_{ij}$, 由于$h^{\mathrm{TT}}_{ij}$是无迹的, 所以$\partial_i F^i = 0$, 它是一个无源场.

## The energy of GWs

考虑到引力波在固有探测器系中表现处类似于牛顿重力的形式, 我们可以考虑定义引力波的能量, 并且考虑两种不同的路径:
- 引力波自身携带有能量, 它自己是否也是时空曲率的源头;
- 把线性化的引力波按经典场论处理, 使用Noether定理得到守恒流.

在这里我们先关注第一种

### Separation of GWs from the background

在之前的部分中, 我们考虑引力波是把它的看作在平直时空中的涨落. 但是如果要分析它对于背景时空的影响, 我们需要把背景时空也考虑成动力学的:
$$
g_{\mu\nu}(x) = \bar g_{\mu\nu}(x) + h_{\mu\nu}(x)
$$
现在的问题是把度规分成背景和涨落两个部分, 一种是把依赖于$x$的部分全部放进其中一项里, 这就是我们在线性化理论中的处理方式. 另一种处理方式是根据不同的尺度, 把大尺度$L_B$的部分放进背景中, 小尺度$\lambda$的部分放进引力波中. 这样我们把引力波看作是静态或者缓变的时空背景中的高频扰动.

### How GWs curve the background

我们把Einstein方程
$$
R_{\mu\nu} = \frac{8\pi G}{c^4}\left(T_{\mu\nu} - \frac{1}{2}g_{\mu\nu}T\right)
$$
在$\bar g_{\mu\nu}$附近展开到二阶$R_{\mu\nu} = \bar R_{\mu\nu} + R^{(1)}_{\mu\nu} + R^{(2)}_{\mu\nu}$. $\bar R_{\mu\nu}$就是由$g_{\mu\nu}$贡献的低频部分, $R^{(1)}_{\mu\nu}$是由$h_{\mu\nu}$贡献的线性阶, 是高频贡献, $R^{(2)}_{\mu\nu}$是$h_{\mu\nu}$的二次型, 同时有高频和低频部分. 现在我们针对高频和低频部分写下Einstein方程
$$\begin{gathered}
    \bar R_{\mu\nu} = - [R^{(2)}_{\mu\nu}]^{\text{Low}} + \frac{8\pi G}{c^4}\left(T_{\mu\nu} - \frac{1}{2}g_{\mu\nu}T\right)^{\text{Low}}    \\
    R^{(1)}_{\mu\nu} = - [R^{(2)}_{\mu\nu}]^{\text{High}} + \frac{8\pi G}{c^4}\left(T_{\mu\nu} - \frac{1}{2}g_{\mu\nu}T\right)^{\text{High}}  
\end{gathered}
$$
我们可以具体地写出$R_{\mu\nu}$对于$h_{\mu\nu}$的展开
$$
R^{(1)}_{\mu\nu} = \frac{1}{2}\left(\bar{\mathrm D}^\alpha \bar{\mathrm D}_\mu h_{\nu\alpha} + \bar{\mathrm D}^\alpha \bar{\mathrm D}_\nu h_{\mu\alpha} - \bar{\mathrm D}^\alpha\bar{\mathrm D}_\alpha h_{\mu\nu} - \bar{\mathrm D}_\nu \bar{\mathrm D}_\mu h\right),
$$
$$\begin{aligned}
R^{(2)}_{\mu\nu} = & \frac{1}{2}\bar g^{\rho\sigma} \bar g^{\alpha\beta}\left[
    \frac{1}{2}\bar{\mathrm D}_\mu h_{\rho\alpha}\bar{\mathrm D}_\nu h_{\sigma \beta} +
    (\bar{\mathrm D}_\rho h_{\nu \alpha})(\bar{\mathrm D}_{\sigma}h_{\mu\beta} - \bar{\mathrm D}_{\beta}h_{\mu\sigma}) \right.\\
    & + h_{\rho\alpha}(\bar{\mathrm D}_{\nu}\bar{\mathrm D}_{\mu} h_{\sigma\beta} + \bar{\mathrm D}_\beta\bar{\mathrm D}_\sigma h_{\mu\nu} - \bar{\mathrm D}_\beta \bar{\mathrm D}_\nu h_{\mu\sigma} - \bar{\mathrm D}_\beta \bar{\mathrm D}_\mu h_{\nu\sigma})\\
    & + \left.(\frac{1}{2}\bar{\mathrm D}_{\alpha}h_{\rho\sigma} - \bar{\mathrm D}_{\rho}h_{\alpha\sigma})(\bar{\mathrm D}_\nu h_{\mu\beta} + \bar{\mathrm D}_\mu h_{\nu\beta} - \bar{\mathrm D}_\beta h_{\mu\nu}) \right].
\end{aligned}$$
其中的$\bar{\mathrm D}$表示相对于$\bar{g}_{\mu\nu}$的协变微分. 这里$R^{(1)}_{\mu\nu}$包含了引力波的能动量张量, $R^{(2)}_{\mu\nu}$包含了引力波如何在背景时空中传播的信息.

对于平直的背景时空$T_{\mu\nu} = 0$, $\bar R_{\mu\nu}$的全部来自于$R^{(2)}_{\mu\nu}$(由形如$(\partial h)^2$以及$h\partial^2 h$的项组成), 这两项对于低频部分的贡献在同一个数量级$\bar R_{\mu\nu} \sim (\partial h)^2 \sim (h/\lambda)^2$, 另一方面, 考虑到$R$来源于度规的二阶导, $\bar R \sim 1/ L_B^2$, 这样我们得到
$$
\frac{1}{L_B} \sim \frac{h}{\lambda}.
$$
这说明对于引力波主导的曲率, 应该满足上面的关系. 如果$T_{\mu\nu} \neq 0$, 那么曲率应该是物质主导的, 上面的关系变成$h \ll \frac{\lambda}{L_B}$. 具体考虑如何把场方程投影到低频的自由度上, 我们可以取一个中间的尺度$\bar l$满足$\lambda \ll \bar l \ll L_B$, 然后在尺度为$\bar l$的体积内取平均, 得到
$$
\bar R_{\mu\nu} = - \langle R^{(2)}_{\mu\nu} \rangle + \frac{8\pi G}{c^4}\langle T_{\mu\nu} - \frac{1}{2}g_{\mu\nu}T\rangle.
$$
这种投影可以看成是一种RG. 现在定义$\bar T^{\mu\nu}$, 满足$\bar T_{\mu\nu} - \frac{1}{2}\bar g_{\mu\nu}\bar T$, 其中$\bar T = \bar{g_{\mu\nu}}\bar T^{\mu\nu}$, 此外定义
$$
t_{\mu\nu} = -\frac{c^4}{8\pi G}\langle R^{(2)}_{\mu\nu} - \frac{1}{2}\bar g_{\mu\nu}R^{(2)}\rangle
$$
以及它的迹$t = \bar{g}^{\mu\nu}t_{\mu\nu} = \frac{c^4}{8\pi G} \langle R^{(2)} \rangle$. 使用$t$重写$\langle R^{(2)}\rangle$:
$$
\ - \langle R^{(2)}_{\mu\nu} \rangle = \frac{8\pi G}{c^4}\left(t_{\mu\nu} - \frac{1}{2}\bar g_{\mu\nu}t\right).
$$
现在我们可以重写Einstein场方程的低频部分
$$
\bar{R}_{\mu\nu} - \frac{1}{2}\bar g_{\mu\nu}\bar R = \frac{8\pi G}{c^4}(\bar T_{\mu\nu} + t_{\mu\nu}).
$$
注意其中正比于$g_{\mu\nu}$的项既可以出现在方程左边作为曲率, 也可以出现在方程右边作为能量, 类似于Einstein方程的两种写法. 很显然我们能看出$t_{\mu\nu}$就是引力波的能动量张量, 它以平均的形式出现, 因为要把引力波从时空背景中区分出来, 我们很自然要引入某种"粗粒化".

### The energy-momentum tensor of GWs

考虑足够平坦的时空, 我们可以使用$\partial^\mu$替换$\bar{\mathrm D}^\mu$. 取平均的时候, 我们可以使用分部积分, 利用TT规范下的条件, 以及作为一种更严格的和谐坐标条件给出的运动方程$\square^2 h_{ij} = 0$, 可以得到(为什么可以使用$TT$规范? 因为我们只关心物理自由度.)
$$
\langle R^{((2))}_{\mu\nu} \rangle = -\frac{1}{4}\langle \partial_\mu h_{\alpha\beta} \partial_\nu h^{\alpha \beta}\rangle.
$$
进一步可以可以得到
$$
t_{\mu\nu} = \frac{c^4}{32\pi G}\langle \partial_\mu h_{\alpha\beta} \partial_\nu h^{\alpha \beta}\rangle.
$$
在规范变换$x^\mu \rightarrow x^\mu + \xi^\mu$下, $t_{\mu\nu}$的变化是
$$
\delta t_{\mu\nu} = \frac{c^4}{16\pi G}\left[\langle \partial_\mu h_{\alpha\beta} \partial_\nu\partial^\alpha \xi^\beta \rangle + (\mu\leftrightarrow \nu)\right].
$$
通过对于$\partial^\alpha$的分部积分, 能看出$\delta t_{\mu\nu} = 0$. 这说明我们得到的结果确实是仅依赖于物理自由度的. 具体地写下能量密度是
$$
t^{00} = \frac{c^2}{32\pi G}\langle \dot h^{\mathrm{TT}}_{ij} \dot h^{\mathrm{TT}}_{ij} \rangle = \frac{c^2}{16\pi G}\langle \dot h_{+}^2 + \dot h_{\times}^2 \rangle.
$$
对于沿$z$方向传播的平面波来说, $h^{\mathrm{TT}}_{ij}$仅依赖于$t - z/c$, 这样得到$t^{01} = t^{02} = 0$, 而利用$\partial_z h^{\mathrm{TT}}_{ij} = -\partial_0 h^{\mathrm{TT}}_{ij}$, 可以得到$t^{03} = t^{00}$.

## Propagation in curved space-time

在弯曲时空中引力波的传播和我们在平直时空中的线性化处理得到的结果是相同的, 只是波动方程和和谐坐标条件都需要改成协变形式, $h_{\mu\nu}$需要使用$\bar h_{\mu\nu}$代替. 引力波的传播是横向的, 并且沿着类光曲线传播.