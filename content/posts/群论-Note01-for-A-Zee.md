---
title: 群论 Note01 for A.Zee.
date: '2025-03-02T17:52:13+08:00'
categories:
- notes
---



2025/2/22:
希望能结束数次翻开群论又合上的操作。

2025/3/2:
写太长了预览起来有点卡，分开写把。

---

## Groups: discrete or continuous, finite or infinite

### Symmetry and group

#### Cyclic subgroups

对于某个有限群$G$，可以被拆成一些循环群。

#### Lagrange's theorem

**Thm.** $|G| = n$, $H\subset G$, $|H| = m$ $\Rightarrow$ $n/m \in \mathbf Z^+$. 

假设$\exist g_1 \in G$, $g_1 \notin H$. 可以定义集合$Hg_1 = \{h_1g_1,\cdots,  h_mg_1\}$. 首先$Hg_1$不构成一个群，因为没有单位元，如果有的话，$g_1$就会成为某个$h$的逆，和$g\notin H$矛盾。第二，$Hg_1$中元素和$H$是一一对应的，并且$Hg_1 \cap H = \emptyset$，假设并非如此，那么一定有$hg_1 = h'$，和$g_1\notin H$矛盾。

现在可以找到某个$g_2\in G$, $g_2\notin H$, $g_2\notin Hg_1$。那么$Hg_2$应该有相似的性质，并且$Hg_2\cap Hg_1 = \emptyset$，假设并非如此，有$hg_2=h'g_1$，和$g_2\notin H_1$矛盾。这个过程可以不断做下去，得到对于$G$的分解，$G = \cup_{i=0}^{k}Hg_i$，称作陪集分解。

#### Multiplication table

对于有限群，表中的每一行或者每一列每个群元素出现且只出现一次。利用这一要求，对于$n=4$的有限群，我们可以写下所有的结果，它一定是$\mathrm Z_4$或者$\mathrm Z_2\otimes \mathrm Z_2$.

另一种方法是利用循环群，从Lagrange's Thm来看，一定有$A^2 = I$或者$A^4=I$。对于后者，这是$Z_4$。对于前者，接下来考虑另一个元素$B$，因为不是循环群，$B^2 = I$, 那么有$C = AB = BA$，这个群是$\mathrm Z_2 \otimes \mathrm Z_2$.

上面的讨论说明了对于阶是质数的有限群，一定是$n$阶循环群。

除了写下完整的乘法表，另一种是写下群元之间的生成关系:
$$\begin{gathered}
\mathrm Z_4: \langle A| A^4 = I\rangle \\
\mathrm Z_2 \otimes \mathrm Z_2: \langle A, B|A^2 = B^2 = I, AB = BA \rangle
\end{gathered}$$

#### Homomorphism and isomorphism

一个映射$f: G\rightarrow G'$被称为同态，如果$f$是保乘法关系的，$f(g_1)f(g_2) = f(g_1g_2)$。这里可以看出一个同态一定把单位元映射到单位元。如果一个同态本身是双射，称之为同构。

对于两个互质（并不要求都是质数）循环群$\mathrm Z_q$和$\mathrm Z_q$，它们同构于$\mathrm Z_{pq}$。

### Finite groups

#### Permutation groups and Cayley's theorem

**Cayley's Thm.** 任何阶为$n$的有限群同构于置换群$P_n$的一个子群。

证明可以考虑乘法表，左乘某个群元实际上是一个置换，这样就建立了从$G$到$P_n$的映射。这个映射是保乘法的，映射的像构成一个子群。

#### Cycles and transpose

任何置换$P$可以被拆成小的循环的乘积。

**Thm.** 任何置换可以写成$2$-循环的乘积。

对于$2$-循环我们可以写下一些乘积规则，重要的两条是
- 如果两个$2$-循环中没有相同的数，它们可以被交换；
- 两个$k$-循环中首位相接的数可以被删去，从而连接这两个循环（注意$2$-循环无所谓数的顺序）。

#### Square root of the identity

**Thm.*** 偶数阶的群$G$中一定有一个非单位元$g$使得$g^2 = 1$.

假设$|G| = n$为偶数，并且不满足上面的条件，这样我们可以成对的从$G$中删去一个群元和它的逆。到最后只剩下某个群元$g$和单位元，导致群$G$中找不到$g$的逆。

#### Equivalence classes

在群中我们可以定义等价关系，如果有某个群元$f$使得$g' = f^{-1}gf$，那么$g'\sim g$. 这个定义中不要求$f$是固定的。

一个例子是置换群$S_4$的子群$A_4$，可以被分成下面这些等价类，$\{I\}$, $\{(12)(34),(13)(24), (14)(23)\}$, $\{(123), (142), (134), (243)\}$, $\{(132), (124), (143), (234)\}$. 可以看出等价的两个置换应该有相同的循环结构。

这样定义的等价类有一些性质
- 阿贝尔群每个元素自成一类，$f^{-1}gf = f^{-1}fg = g$；
- 单位元自成一类；
- 考虑一个类$c$，每个元素的逆也构成一个类，通过给$f^{-1}gf = g$两边取逆即可。

#### Cycle structure and partition of integers

一个置换群$S_n$的元素可以被写成$n_j$个$j$-循环的乘积，$n = \sum_j jn_j$. 我们希望知道当给出了这种循环结构，$S_n$中有几个元素满足特定结构。答案是$\mathcal N(n_1, \cdots, n_j, \cdots) = \frac{n!}{\prod_j j^{n_j}n_j!}$，分子通过对$n$个整数做全排列得到，同时每个$j$-cycle中顺序的置换不影响，贡献了因子$j$，一共有$n_j$个$j$-cycle，它们之间的置换也不影响结果。

#### The dihedral group $D_n$

二面体群通过旋转$R$和反射$r$生成。$D_n$有$2n$个元素，包括不同角度的旋转，以及它们和反射的乘积。
$$
D_n = \langle R, r|R^n = I, r^2 = I, Rr = rR^{-1}\rangle
$$

#### Conxeter groups

一个Conxeter group定义为
$$
\langle a_1, a_2, \cdots, a_k|(a_i)^2, (a_i a_j)^{n_{ij}} = I, \text{for a certain }n_{ij}\geq 2\rangle
$$
我们可以证明在$n_{ij} = n_{ji}$. Conxeter groups可以想象万花筒。

#### Invariant subgroups

$H\subset G$, $g\in G$. 对$g^{-1}h_1g, g^{-1}h_2g$， 有$(g^{-1}h_1g)^{-1}g^{-1}h_2g = g^{-1}h_1^{-1}h_2g$，所以$g^{-1}Hg$依然是$G$的子群。如果$g^{-1}Hg = H$对任意$g\in G$，我们说$H$是$G$的一个不变子群（正规子群），$H\triangleleft G$

一个例子是$A_4$, 有一个正规子群是$Z_2\otimes Z_2$. 此外$G = E\otimes F$, $E$和$F$都是$G$的不变子群。

#### Derived subgroup

$a, b\in G$, 考虑$\langle a, b\rangle = a^{-1}b^{-1}ab$，下面的性质
- $\langle a, a\rangle = I$;
- $\langle a, b\rangle = \langle b, a\rangle^{-1}$.

取$a, b$遍历$G$，所有的结果以及它们的乘积，构成$G$的一个子群$D$，称作derived subgroup. $D$可以被看做衡量$G$是否足够“阿贝尔”，如果$D$的阶很大，$G$就偏离阿贝尔群很远。作为一个例子，$S_4$的derived subgroup是$A_4$. 一个derived subgroup也一定是不变子群。

#### Simple group

一个群被称作单群，如果它没有非平凡的不变子群。

判断一个群是否是单群，可能要构造它的正规子群。一种方法是计算derived subgroup，另一种方法如下：

如果在$G$上构造一个同态$f$，它的kernel一定是$G$的正规子群。先说明$\ker(f)$是一个子群，取$g_1, g_2\in \ker(f)$, $f(1) = f(g_1^{-1})f(g_1) = f(g^{-1}_1)$, $g_1^{-1}\in \ker(f)$. $f(g_1^{-1}g_2) = f(g_1^{-1})f(g_2)=1$, i.e. $g_1^{-1}g_2\in \ker(f)$. $\ker(f)$是一个子群。考虑$g \in G$, $f(g^{-1}g_1g) = 1$，$g^{-1}g_1g\in \ker(f)$.

#### Invariant subgroup

$G \triangleright H$. 利用正规子群可以构造商群，考虑配陪集分解$\{g_aH, g_bH,\cdots\}$. $g_aH$和$g_bH$中两个元素的乘积一定会成为某个$g_cH$中的元素，由此我们可以在这些陪集的集合上定义乘法
$$
g_aH\cdot g_bH = g_ag_b H.
$$
这样就定义了一个商群$Q = G/H$，它的单位元就是$H$. 上面的定义中使用了左陪集，但对于正规子群来说，左右陪集没有区别。

### Rotations and the notion of Lie algebra

#### Act a little bit at a time

考虑在二维平面上的无限小旋转，$R = I + A$. 考虑$R^TR = I$的条件，
$$
R^TR = (I+A^T)(I+A) = I + A^T + A = I.
$$
要求$A$应该是反对称的。这限制$A$只能有$A = \theta \mathcal J$的形式，而
$$
\mathcal J = \begin{pmatrix}
0, & 1 \\ -1 & 0
\end{pmatrix}.
$$
$\mathcal J$称作$SO(2)$的生成元。现在考虑有限大的旋转
$$
R(\theta) = \lim_{N\rightarrow \infty}\left(R\left(\frac{\theta}{N}\right)\right)^{N} = e^{\theta \mathcal J}
$$
这确实是旋转矩阵。在分析中，我们可以给定一个函数在某一点的各阶导数来确定它，现在我们需要一阶导数来获得这个群，因为群本身已经加入了很多限制。

#### Lie in higher dimensions

对于3维来说，$A$中独立变量有三个，我们可以写下三个独立的反对称阵
$$\begin{gathered}
\mathcal J_x = \begin{pmatrix}0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0\end{pmatrix},\\
\mathcal J_y = \begin{pmatrix}0 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & 0\end{pmatrix},\\
\mathcal J_x = \begin{pmatrix}0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0\end{pmatrix},\\
\end{gathered}$$
$A$可以通过生成元写成$A = \sum \theta_i \mathcal J_i$. 类似的可以得到$R = e^{\sum_i \theta_i \mathcal J_i}$. 为了把它们和角动量联系起来，要把这些算符写成厄密的，$J_i = -i\mathcal J_i$，这样旋转成为$R = e^{i\theta\cdot J}$.

#### Lie algebra

考虑$R = I + A$和$R'$，在旋转变换下$R'$成为$RR'R^{-1} = R' + [A, R']$. $[A, R']$衡量了这两个操作之间不交换的程度。交换子本身是反对称的，所以本身也应该可以被写成生成元的线性组合，
$$
[J_i, J_j] = ic_{ijk}J_k.
$$
这里的因子$c_{ijk}$就是$\epsilon_{ijk}$.

#### Structure constants

一个群，它的群元可以被参数化为$g(\theta_1, \theta_2, \cdots)$，并且$g(0, 0, \cdots) = I$. 我们有如下步骤：
- 在单位元附近展开某个群元$g = I+ A$；
- $A$被表达成一些生成元的线性组合$A = i\sum_a\theta_aT_a$;
- 对于两个单位元附近的群元$g_1 = I + A$, $g_2 = I + B$, $g_1^{-1}g_2g_1 = I + B + [A, B]$，$[A, B]$描述了单位元附近群员的关系。
- $[A,B]$也是生成元的线性组合，特别地，$[T_a, T_b] = if_{abc}T_c$.

生成元之间的交换关系定义了一个李代数，$f_{abc}$称作这个代数的结构因子。

#### Rotations in higher-dimensional space

一个$N\times N$的反对称阵，在每个非对角元的位置会对应一个反对称阵$\mathcal J_{(mn)}$，也可以写下一个厄密的形式$J_{(mn)}$.
$$
J_{(mn)}^{ij} = -i (\delta^{mi}\delta^{nj} - \delta^{mj}\delta^{ni}).
$$
一共有$N(N-1)/2$个生成元。可以把任何一个反对称阵$A$写成$A = i\sum \theta_{(mn)}J_{(mn)}$，$\theta$和$J$对于指标$(mn)$是反对称的。

#### Rotations around an axis or rotation in a plane

在高维的情况下，讨论绕某个轴旋转不再是有意义的（3维下可以这么做），我们只能说在哪两个轴张成的平面中旋转。

#### The Lie algebra for SO($N$)

考虑交换子$[J_{(mn)}, J_{(pq)}]$，如果$(mn), (pq)$中没有共同的整数或者有两个共同的整数，结果是$0$。另一种情况是有一个共同的整数比如$m=p$，结果是$iJ_{(nq)}$.
$$
[J_{(mn)}, J_{(pq)}] = i(\delta_{mp}J_{(nq)} + \delta_{nq}J_{(mp)} - \delta_{np}J_{(mq)} - \delta_{mq}J_{(np)}).
$$

李代数反应的是李群在单位元附近的性质，通过在生成元的指数可以获得单位元附近的一些群元，但不一定可以覆盖整个群。

### How the SO($4$) algebra falls apart

SO($4$) 有六个生成元，可以分成两组，$J_{12}, J_{23}, J_{31}$是在前三个维度上的旋转，$J_{14}, J_{24}, J_{34}$是把前三个轴转到$4$-轴上的旋转，分别写成$J_i$和$K_i$，这个李代数可以写成
$$\begin{gathered}
[J_i, J_i] = i\epsilon_{ijk}J_k, \\
[J_i, K_j] = i\epsilon_{ijk}K_k, \\
[K_i, K_j] = i\epsilon_{ijk}J_k.
\end{gathered}$$

定义$J_{\pm, i} = \frac{1}{2}(J_i + K_i)$. 可以证明$[J_{+, j}, J_{-, i}] = 0$, 并且内部满足
$$
[J_{\pm, i}, J_{\pm, j}] = i\epsilon_{ijk}J_{\pm, k}.
$$
这样可以看出SO($4$)和SO$(3)\otimes$SO$(3)$在单位元附近是同构的，整体上差一个$\mathrm Z_2$.

## Representing group elements by matrices

### Representation theory

#### What is a representation

群$G$的$d$维表示是一个到$d$维矩阵空间上的同态$D: G\rightarrow \mathcal M_{d\times d}$. 

作为一个例子，考虑置换群$S_4$，我们可以写下$e_i$，$S_4$置换这几个单位矢量，这样一个元素$(2413)$可以被表示成
$$
D(2413) = \begin{pmatrix}
0 & 0 & 0 & 1\\
0 & 0 & 1 & 0 \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0
\end{pmatrix}.
$$

#### Introduction to representation

我们在上面已经给出了置换群的表示，对于任何一个$n$阶的有限群，它同构于$S_n$的某个子群，所以有限群一定是可以被表示的。

加法群可以被表示成$D(u) = e^{u}$或者$D(u) = \begin{pmatrix}1 & 0 \\ u & 1\end{pmatrix}$. 洛伦兹群（同一个方向上）也是加法群的一个表示$D(\phi_1)D(\phi_2) = D(\phi_1 + \phi_2)$.

对任何群都有平凡表示$D(g) = 1$. 如果表示本身是一个同构，称作忠实表示。对于像SO$(3)$这种通过矩阵定义的群，它本身被称作定义表示(defining representation)或者基本表示。

$Z_n$有$n$个一维表示$e^{i2\pi \frac{kj}{n}}$.

#### Character is a function of class

我们可以标记一个群不同的表示为$D^{(r)}(g)$，并且定义特征标$\chi^{(r)}(g) = \mathrm{Tr}D^{(r)}(g)
$. 对于两个共轭等价的元素$g_2 = f^{-1}g_1f$，它们的表示之间差一个相似变换，所以特征标也是相同的。

#### Equivalent representations

如果对用一个群的两个表示，对于任意群元，差一个相似变换，就说这两个表示是等价的。这两个表示对于同一个类的特征标如果有不同，它们一定不等价，如果对所有类的特征标都相同，并不一定说明等价，只是一种强烈的信号。

#### Reducible or irreducible representation

如果$D(g)$有不变子空间，或者说他是分块对角的，称作可约表示$D(g) = D^{(1)}(g) \oplus D^{(2)}(g)\cdots$. 反之则是不可约表示。

对于任何群都有平凡表示$D(g) = I_k$，只有在$k=1$时才是不可约的。

#### Restriction to a subgroup

可以把群$G$的表示限制在子群$H$上，但普遍的说，这个表示不确定是否可约。

#### Unitary representations

酉表示，如果一个表示是酉的（那我问你）。有限群一定有酉表示，我们可以证明这一点：

假设群$G$有表示$D'(g)$，可以定义
$$
H = \sum_g D'(g)^\dagger D'(g).
$$
对于任何$g'\in G$，
$$
D'(g')^\dagger H D'(g') = H
$$
$H$是一个正定，厄密的矩阵，可以作特征值分解$H = W\rho^2 W^\dagger$.

定义$D(g) = \rho W^\dagger D'(g)W\rho^{-1}$. 可以证明$D(g)$是酉表示。并且这个构造的过程说明了通过一个相似变换，有限群的表示一定成为一个酉表示。

#### product representation

对于两个维度分别是$d_r, d_s$的表示$D^{(r)}$和$D^{(s)}$，可以通过直积构造他们的乘积表示$D(g) = D^{(r)}(g)\otimes D^{(s)}(g)$. 一般的乘积表示是可约的，并且特征标是两个构成的表示特征标的乘积。

### Schur's lemma and the great orthogonality theorem

#### Schur's lemma

**Lemma.** 如果$D$是有限群$G$的一个不可约表示，并且存在矩阵$A$使得对任何$g\in G$，$AD(g) = D(g)A$，一定有$A  =\lambda I$.

证明中只需要考虑$A$是厄密的情况，理由如下。有限群的表示一定等价于一个酉表示，对$AD(g) = D(g)A$取共轭，$D(g)^{-1}A^\dagger = A^\dagger D(g)^{-1}$. 如果$A$满足上面的条件，它的共轭转置也一定满足。这样就有两个厄密的矩阵$A + A^\dagger$和$i(A - A^\dagger)$.

对于厄密阵$H$作特征值分解$H = W^\dagger H' W$. 在这组基下写出$D(g) = W^\dagger D'(g)W$. 在这组新的基下$H'$和$D'$也交换。这样我们甚至只需要考虑对角的$H$.

考虑$D(g)H - HD(g)$的$ij$元，有$(H_i^i-H^j_j)D^i_j = 0$（这里没有求和）。这样，只要对于某一个$g$有$D^i_j\neq 0$，就有$H_{ii}=H_{jj}$. 因为表示是不可约的，所以实际上不存在总有$D^{ij} = 0$的情况。

上面的证明我们可以看出，如果表示是可约的，那么在两个不变子空间上，各自是一个纯量阵。

#### The great orthogonality theorem

**Thm**. 一个有限群$G$的$d$维不可约表示$D$一定满足
$$
\sum_{g\in G} D^\dagger(g)^i_j D(g)^k_l = \frac{|G|}{d}\delta^i_l\delta^k_j.
$$

现在来证明这一定理，对于任意矩阵$X$，考虑$A = \sum_g D^\dagger(g)XD(g)$. 对任何$g$，$D^\dagger(g)AD(g) = A$（对于所有群元求和是一种常见的构造不变量的方法）. 根据Schur's lemma，$A = \lambda I_d$，通过取迹来确定$\lambda$，$\mathrm{Tr} A = \lambda d = |G|\mathrm{Tr} X$. 我们选择$X$为$jk$元为$1$，其他元全是$0$的阵，这样$\mathrm{Tr}X = \delta^k_j$. 最后
$$
A^i_l = \sum_{g\in G} D^\dagger(g)^i_j X^j_k D(g)^k_l = \sum_{g\in G} D^\dagger(g)^i_j D(g)^k_l = \lambda \delta^i_l = \frac{|G|}{d}\delta^i_l\delta^k_j.
$$

这个定理有一个推论，如果$r$和$s$在两个不同的等价类中，$\sum_{g\in G} D^{(r)\dagger}(g)^i_j D^{(s)}(g)^k_l = 0$.

这样总的就有
$$
\sum_{g\in G} D^{(r)\dagger}(g)^i_j D^{(s)}(g)^k_l = \frac{|G|}{d_r}\delta^{rs}\delta^i_l\delta^k_j.
$$

#### Character orthogonality

对于上面的定理，取$i = j, k = l$就有$\sum_g (\chi^{(r)}(g))^*\chi^{(s)}(g) = \sum_c n_c (\chi^{(r)}(c))^*\chi^{(s)}(c) = |G|\delta^{rs}$.

可以对于$\mathrm Z_N$的不同表示验证这一点。

#### Character table

自己看书好吗，不想画表了。

对于每个表示$s$，我们可以写下一个$N(C)$维的向量$(n_c)^{1/2}\chi^{(s)}(c)$，它们彼此之间是正交的，但是在$N(C)$维的向量空间中，正交的矢量最多不能超过维度，因此对于有限群来说，不可约表示的个数不超过群元等价类的个数，实际上是相等的。

此外，如果固定指标$s, k, l$，$D^{(s)}(g)^k_l$成为一个$|G|$维的向量空间中的向量，并且彼此是正交的，基于同样的理由，可以写下
$$
\sum_s d_s^2 \leq N(G).
$$
这个不等式其实是等式，我们可以利用有限群的regular representation证明这一点。

#### A test for reducibility

考虑一个可约的表示，其中不可约表示$D^{(r)}$出现$n_r$次，相应的特征标是$\chi(c) = \sum_r n_r\chi^{(r)}(c)$. 根据特征标的正交性有
$$
\sum_c n_c \chi^*(c)\chi(c) = \sum_c n_c\sum_{r, s}n_r n_s \chi^{*(r)}(c)\chi^{(s)}(c) = |G|\sum_{r, s}n_rn_s\delta^{rs} = |G|\sum_r n_r^2.
$$

如此，我们只要计算一个表示的特征标$\chi(c)$，然后按照上面的等式求和，如果结果是$1$，这个表示就是不可约的。反之则是不可约的，并且我们能看出来这个表示如何被拆开成一些不可约的表示。

另外如果我们选择在和一个不可约表示求内积，
$$
\sum_c n_c \chi^{*(r)}(c)\chi(c) = \sum_c n_c\sum_s n_s\chi^{*(r)}(c)\chi^{(s)}(c) = |G|n_r.
$$
这样我们可以知道对于某个特定的不可约表示到底出现几次。

#### The characters of the regular representation are ridiculously easy to compute

对一个有限群，群元的乘法看成是对于群的一个重排，这样这个群同构于$S_n$的一个子群，并且这个子群中所有元素表示的置换都涉及所有元素。这种方式直接这出一个表示，维数是$|G|$，称作regular representation，除了单位元所有的表示矩阵特征标都是$0$，这样就有$\sum_c n_c\chi^{*}(c)\chi(c) = \chi(I)^2 = |G|^2 = |G|\sum_r n_r^2$，从而$\sum_r n_r^2 = |G|$. 所以regular representation一定是可约的，

此外考虑$\sum_c n_c \chi^{*(r)}(g)\chi(g) = |G|n_r$, 这样就有$d_r = n_r$. 同样的$\sum_r d_r^2 = |G|$. 这样我们就得到了有限群的所有不可约表示的维度和群的阶的关系。

#### The character table is square

可以利用群代数来证明这个小标题，简单的说明要往后看看。首先对一个类定义
$$
\mathcal D(c) = \frac{1}{n_c}\sum_{g\in c}D(g).
$$
对于任意$g'\in G$，有$D(g'{-1})\mathcal D(c)D(g) = \mathcal D(c)$. 根据Schur's lemma，有$\mathcal D(c) = \lambda(c)I$. 两边取迹有$\lambda(c) = \chi(c)/\lambda(I)$. 利用类代数我们有
$$\begin{gathered}
\mathcal D(c)\mathcal D(d)  = \sum_e \Gamma(c, d; e)\mathcal D(e), \\
\chi(c)\chi(d) = \chi(I)\sum_e \Gamma(c, d; e)\chi(e).
\end{gathered}$$
对所有的不可约表示求和
$$
\sum_r \chi^{(r)}(c)\chi^{(r)}(d) = \sum_e \Gamma(c, d; e)\chi^{(r)}(I)\chi^{(r)}(e) = |G|\Gamma(c, d; I).
$$
尽管我们到这里还没有证明不同的类之间也正交，但是单位元和其他类正交这一点是直接的，$\chi^{\text{reg}}(c\neq I) = \sum d_r \chi^{(r)}(c) = \sum \chi^{(r)}(c) \chi^{(r)}(c) = 0$. 
此外根据$K$的定义有$\Gamma(c, \bar{c}; I) = \frac{1}{n_c}$，这里$\bar{c}$表示由$c$中元素的逆组成的类。并且当$d\neq \bar{c}$时，$K(c, d; I) = 0$. 结合$\chi(\bar{c}) = \chi(c)^*$就可以得到
$$
\sum_r \chi^{(r)}(c)^*\chi^{(r)}(c') = |G|\delta^{cc'}/n_c.
$$
这个等式说明有$N(C)$个相互正交的矢量在$N(R)$维空间中，这样$N(R)\geq N(C)$，结合前面的$N(R)\leq N(C)$，就有$N(C) = N(R)$.

我们有$N(C) = N(R)$，给出了不可约表示的个数，结合上面的$\sum_r d_r^2 = |G|$限制，对于一些阶数小的群来说，我们可以以由此完全确定每个不可约表示的维数。

现在我们已经说明了character table应该是一个方阵的形状，那么不同不可约表示之间的正交性，也会导致不同群元等价类之间的正交。具体地说，可以定义$U^c_s = \sqrt{\frac{n_c}{|G|}}\chi^{(s)}(c)$，我们知道对于不同$r$是正交的，那么对于不同列$c$也是正交的，有$\sum_r \chi^{(r)}(c)^*\chi^{(r)}(c') = |G|\delta^{cc'}/n_c$.

#### Different irreducible representations are orthogonal

后面的一部分内容在书里是附录。

考虑两个维数不同$d_r \neq d_s$的不可约表示，定义$A = \sum_g D^{(r)(g)\dagger}XD^{(r)}(g)$, 仍有$D^{(r)\dagger}(g)A D^{(r)}(g) = A$. 这样就有$AD^{(s)} = D^{(r)}A$，可以取共轭转置得到$A^\dagger D^{(r)}(g)^\dagger = D^{(s)}(g)^\dagger A^\dagger$. 左右同乘$A$，有
$$
AA^\dagger D^{(r)}(g^{-1}) = AD^{(s)}(g^{-1})A^\dagger = D^{(r)}(g^{-1})AA^\dagger.
$$
根据Schur's lemma，$AA^\dagger = \lambda I_{d_r}$. 可以把$A$补成方阵，这样会多几行或者几列零，两边取行列式可以得到$\lambda = 0$.

接下来考虑维数相同的两个不可约表示，如果$\det A = 0$，我们有$\lambda = 0$. 如果$\det A \neq 0$, 可以把$AD^{(s)} = D^{(r)}A$写成$D^{(s)} = A^{-1}D^{(r)}A$，说明$r, s$其实是同一个表示。

#### Frobenius algebra, group algebra, and class algebra

可以定义像这样的代数结构$\sum_i a_i g_i$，称作Frobenius algebra或者群代数。考虑一个群元的等价类$c = \{g_1^{(c)}, \cdots, g_{n_c}^{(c)}\}$. 我们定义类平均，
$$
K(c) = \frac{1}{n_c}\sum_i g_i^{(c)}.
$$
对于两个不同的类$c, d$，$K(c)K(d) = n_c^{-1}n_d^{-1}\sum_{ij}g_i^{(c)}g_j^{(d)}$. 对于任意$g\in G$，
$$
g^{-1}(\sum_{ij}g_i^{(c)}g_j^{(d)})g = \sum_{ij}g_i^{(c)}g_j^{(d)}.
$$
这说明$K(c)K(d)$一定是一些类平均的线性组合，
$$
K(c)K(d) = \sum_e \Gamma(c, d; e)K(e).
$$
我们得到了群代数的一个子代数，称作类代数。上面的这些$\Gamma$一定是正的。

### Character is a function of class

#### From the character table to the representation matrices

The great orthogonality theorem show that
$$
\sum_g D^{(r)}(g)^i_j = 0.
$$
取其中一个表示为平凡表示。可以把求和限制在子群上，或者子群的陪集上。

#### Link between group theory and geometry: fixed points

对于一个可约表示，利用可约表示的特征标是不可约表示的线性组合，我们可以写下线性方程组来求解一个可约表示被分成哪些不可约表示。

#### The class of inverses: real and complex characters

某个类的特征标满足$\chi(\bar{c}) = \chi(c)^*$，如果一个类中包含它的逆，那么特征标是实的。

### Real, pseudoreal, complex representations, and the number of square root

#### Conjugate representations

一个表示的共轭也构成一个表示$D(g)^*$. 对应的特征标也互为共轭$\chi^{(r^*)}(c) = \chi^{(r)}(c)^*$.

如果一个表示和它的共轭表示是等价的，有$S^{-1}D(g)S = D(g)^*$，那么它们的特征标相同，也就是说，特征标是实数。当然这个结论反过来不一定成立。这样我们把不可约表示分类成复的和非复的。

#### A restriction on the similarity transformation $S$: real versus pseudoreal

对于一个非复的不可约表示，$SD(g)S^{-1} = D(g)^*$，两边取转置$S^{-T}D(g)^TS^T = D(g)^\dagger = D(g^{-1})$. 一个非复的不可约表示中，每个元素的和它的逆的表示矩阵相差一个相似变换。

把这个关系用两次，我们得到$D(g) = S^{-T}D(-g)^TS^T = S^{-T}D(g)^*S^T = S^{-T}SD(g)S^{-1}S^T$. 说明$S^{-1}S^T$和所有的表示矩阵交换，根据Schur's lemma，$S^{-1}S^T = \eta I$，$S^T = \eta S$. 两边的行列式相等给出$\eta = \pm 1$，要求$S$是对称或者反对称的。

现在可以对非复的不可约表示可以继续分类，如果$S$是对称的，就说这个表示是实的，如果是反对称的，就说是伪实的(pseudoreal)。

因为奇数阶的反对称矩阵的行列式是$0$（$\det S = \det S^T = \det -S = (-)^n\det S$），所以伪实的表示都是偶数阶的。

还可以证明$S$是某个幺正矩阵的常数倍：$SD(g) = D(g)^*S = D(g)^{-T}S$，$S = D(g)^T S D(g)$，取共轭转置有$S^\dagger = D(g)^\dagger S^\dagger D(g)^*$，$S^\dagger S = D(g)^T S D(g) D(g)^\dagger S^\dagger D(g)^* = D(g)\dagger S^\dagger S D(g)$，根据Schur's lemma, $S^\dagger S = \lambda I$，实际上我们总可以缩放$S$来使得它是幺正的。

#### Real representation is really real

一个对称的幺正矩阵一$S$定有平方根：$W^2 = S$. $W^2 D(g) W^{-2} = D(g)^*$, $W D(g) W^{-1} = W^{-1}D(g)^* W = (W D(g) W{-1})^*$. 一个实表示经过相似变换，元素全是实数。

#### An invariant bilinear for a noncomplex representation

**Thm.** 对于$d_r$维的不可约的实或伪实的表示，$y^T S x$在变换$x\rightarrow D(g) x$下不变。

Proof: 由于表示是非复的，$\exist S$, s.t. $S D(g)S^{-1} = D(g)^* \Rightarrow S D(g)^\dagger S^{-1} = D(g)^T$. 所以考虑上面的变换
$$
y^T S x \rightarrow y^T  D(g)^T S D(g) x = y^T  S D(g)^\dagger S^{-1} S D(g) x = y^T S x.
$$

这一定理的逆定理也成立，如果$y^T S x$在群变换下不变，那么有$D^TSD = S$. 这就说明表示是非复的。

#### The reality checker

现在的问题是我们如何知道一个表示是实的，伪实的，还是复的？

定义$S = \sum_{g\in G} D(g)^T X D(g)$，有$D(g)^T S D(g) = S$，但根据上一节我们知道这意味这$D(g)$是非复的，哪怕开始并没有对于表示性质的要求。这说明对于复表示$S = \sum_{g\in G} D(g)^T X D(g) = 0$.

对于复表示来说，我们可以取$X = X(i, j=l)$表示在$i, l$元$1$，其他元是$0$的矩阵，这样有
$$
\sum_g D(g)^{ij}D(g)^{lk} = 0.
$$
令$j = l$并求和，$\sum_g D(g^2) = 0$，取迹得到$\sum_g \chi(g^2) = 0$.

对于非复的表示来说，有$S^T = \eta S$，$S^T = \sum_g D(g)^T X^T D(g) = \eta \sum_g D(g)^T X D(g)$，同样的令$X = X(i, l)$得到$\sum_g D(g)^{lj} D(g)^{ik} = \eta \sum_g D(g)^{ij}D(g)^{lk}$，令$i = j, k = l$求和，可以得到
$$
\sum_g \chi(g^2) = \eta |G|.
$$
上面对群元的求和可以变成对于对等价类的。

#### The number of square roots

令$\sigma_f$表示群元$f$的平方根的个数。我们已经知道偶数阶的有限群一定有单位元的平方根，这里首先考虑单位元的平方根，
$$
\sum_f \sigma_f \chi^{(r)}(f) = \eta^{(r)}|G|.
$$
这里$\sigma_f$和表示无关，这样可以对不同的表示求和
$$\begin{aligned}
\sum_r (\sum_f \sigma_f \chi^{(r)}(f))\chi^{(r)*}(f') = & \sum_r \eta^{(r)}|G|\chi^{(r)*}(f') \\
= & \sum_f \sigma_f \frac{|G|}{n_c}\delta_{cc'} = \sigma_{f'}|G|.
\end{aligned}$$
同一个等价类中的元素平方根的个数应该相同，这样我们得到
$$
\sigma_f = \sum_r \eta^{(r)}\chi^{(r)}(f).
$$

#### Sum of the representation matrices of squares

定义$A = \sum_g D(g^2)$满足Schur's lemma的条件，$A = cI$，两边取迹得到
$$
\sum_g \mathrm{Tr} D^{(r)}(g^2) = cd_r = \sum_g \chi^{(r)}(g^2) = \eta^{(r)}|G|.
$$
这样就有
$$
\sum_g D(g^2) = \eta^{(r)}\frac{|G|}{d_r}I.
$$

#### How many ways can a group element be written as a product of two squares

对上面的式子乘以$D(f^2)$，$\sum_g D(f^2 g^2) = \eta^{(r)}\frac{|G|}{d_r}D^{(r)}(f^2)$，取迹得到
$$
\sum_g \chi^{(r)}(f^2 g^2) = \eta^{(r)}\frac{|G|}{d_r}\chi^{(r)}(f^2).
$$
对$f$也求和得到
$$
\sum_g \chi^{(r)}(f^2 g^2) = \frac{(\eta^{(r)}|G|)^2}{d_r}.
$$
可以使用类似的方法得到问题的答案，如果$\tau_h$是满足$f^2 g^2 = h^2$可能乘积的个数，有$\sum_h \tau_h \chi^{(r)}(h) = \frac{(\eta^{(r)}|G|)^2}{d_r}$，接下来对不同的表示求和
$$\begin{aligned}
\sum_r\sum_h \tau_h \chi^{(r)}(h)\chi^{(r)*}(h') = & |G|^2\sum_r (\frac{(\eta^{(r)})^2}{d_r})\chi^{(r)*}(h') \\
= & \sum_h \frac{|G|}{n_c}\delta^{cc'} = \tau_{h'}|G|.
\end{aligned}$$
这样就得到
$$
\tau_h  = |G|\sum_r \frac{\eta^{(r)2}\chi^{(r)}(h)}{d_r}.
$$

### Euler's $\varphi$-function, Fermat's little theorem, and Wilson's Theorem

#### The group $G_n$

考虑这样的集合$G_n = \{m|1\leq n-1\}$, $m$和$n$互致，这个集合在模$n$的乘法下构成群。单位元的存在是显然的，先考虑乘法的封闭性。假设$m_1m_2 (\mathrm{mod} n)$和$n$有共同的的因子$d > 1$. 这样$n = kd, m_1m_2 (\mathrm{mod} n) = jd$，$m_1m_2 = jd + ln = (j + lk)d$，这样$m_1m_2$也和$n$有超过$1$公因子，矛盾。

之后考虑逆的存在，有如下的引理：
**Lemma.** 对两个互质的整数$a, b$，存在一组整数$x, y$使得$xa + yb = 1$.
这样对于$m, n$，存在$xm + by = 1$，给出$xm = 1(\mathrm{mod}\ n)$. 这样$x$就是$m$逆。$G_n$是一个阿贝尔群。

#### Euler's $\varphi$-function

定义Euler's $\varphi$-function $\varphi(n) = |G_n|$. 有如下的定理：如果$a$和$n$互质，那么$a^{\varphi(n)} = 1(\mathrm{mod}\ n)$. 考虑$g\in G$，$g^{|G|} = I$，假设$a = nk + m$，那么$m$和$n$是互质的，$m\in G_n$并且$m^{\varphi(n)} = 1(\mathrm{mod}\ n)$。这样就有$a^{\varphi(n)} = (nk+m)^{\varphi(n)}$，按二项式展开得到$a^{\varphi(n)} = 1(\mathrm{mod}\ n)$.

这样就有费马小定理：如果$p$是质数，$a$不是$p$的倍数，$a^{p-1} = 1(\mathrm{mod}\ p)$.

#### Wilson's theorem

**Thm.** $(n-1)! + 1$能被$n$整除当且仅当$n$是质数。

Proof: 如果$n$不是质数，它的因子可以存在于$\{1, \cdots, n-1\}$中，这样$(n-1)!$的阶乘被$n$整除，$(n-1)! = 0(\mathrm{mod}\ n)$.

如果$n$是质数，这样$\{1, \cdots, n-1\}$构成群$G_n$，其中$1$的逆是$1$，$n-1$的逆是$n-1$，剩下$n-3$个元素的逆都在这$n-3$个元素里，这样$(n-1)! = -1 (\mathrm{mod}\ n)$.