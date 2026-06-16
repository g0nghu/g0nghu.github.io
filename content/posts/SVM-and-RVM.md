---
title: SVM and RVM
date: '2025-07-25T20:47:48+08:00'
categories:
- notes
draft: true
---


# Support vector machine (SVM)

在一个空间中存在两类点, 这两类点我们使用$y = \pm 1$标记. 现在我们希望找到一个超平面, 使得这个超平面能在空间中分割这两类点, 并且到最近的点(称作支持向量)的距离最大, 这就是SVM的优化目标. 如果在空间有了新的点, 我们就可以根据这个超平面对于新的点做出分类.

我们使用$(w, b)$来参数化这个超平面:
$$
\Gamma(w, b) = \{x| w^T x + b = 0\}.
$$
空间中一点$x$到这个超平面的距离是
$$
\frac{|\omega^T x + b|}{||w||}.
$$
假设支持向量到超平面的距离是$d$, 那么对于两类点来说, 就有
$$
\frac{y(w^Tx + b)}{||w||} \geq d.
$$
对于支持向量$x_s$来说上式取等号. 令$\frac{w}{||w||d} \rightarrow w$, $\frac{b}{||w||d}\rightarrow b$, 就有
$$
y_i(w^T x_i + b) \geq 1.
$$
现在最大化$d$就是最小化$1/||w||$, 也就是最小化$||w||^2$. 我们得到这个优化问题的完整描述
$$
\min_{w, b} \frac{1}{2}||w||^2, \quad \text{s.t.}\quad y_i(w^T x_i + b)\geq 1.
$$

## 对偶方法

这是一个有不等式约束的凸二次规划问题, 可以使用Lagrangian乘子法得到其对偶问题.

首先定义
$$
L(w, b, \alpha) = \frac{1}{2}||w||^2 - \sum_i \alpha_i(y_i(w^Tx + b) - 1).
$$
并且令$\theta(w) = \max_{\alpha_i\geq 0}L(w, b, \alpha)$. 如果得到的样本不满足约束, 也就是$y_i(w^Tx + b) < 1$时, $\alpha_i$取无穷大, $\theta(w)$也是无穷大. 如果满足约束, 在$\theta(w)$中应该有$\alpha_i = 0$且$\theta(w) = \frac{1}{2}||w||^2.$ 那么原问题等价于
$$
\min_{w, b}\theta(w) = \min_{w, b}\max_{\alpha \geq 0}L(w, b, \alpha) = p^*.
$$
这里要先求函数的最大值再求最小值, 这个过程如果满足一些条件, 是可以交换顺序变成
$$
\max_i{\alpha_i}\min_{w, b}L(w, b, \alpha) = d^*.
$$
如果希望这两个问题是等价的, 需要满足:
- 优化问题是凸的;
- 满足KKT条件, 也就是要满足
  $$
  \begin{gathered}
  \alpha_i \geq 0,\\
  y_i(w^T x_i + b) - 1 \geq 0,\\
  \alpha_i(y_i(w^T x_i + b) - 1) = 0.
  \end{gathered}
  $$

现在先来求第一个最小值, 要求$\partial L / \partial b = \partial L / \partial w = 0$, 给出
$$\begin{gathered}
w = \sum_i^N \alpha_i y_i x_i,\\
\sum_i \alpha_i y_i = 0.
\end{gathered}$$ 
把这两个条件代回$L(w, b, \alpha)$中, 消去$w, b$, 得到
$$
-g(\alpha) = L(w^*, b^*, \alpha) = -\frac{1}{2}\sum_{ij}\alpha_i \alpha_j y_i y_j (x_i \cdot x_j) + \sum_i \alpha_i.
$$
现在问题变成求$g(\alpha)$的最小值(带有约束$\sum_i \alpha_i y_i = 0$和$\alpha_i \geq 0$).

## Sequential Minimal Optimization(SMO)

现在需要求解的是这样一个二次规划问题, 常用的算法是SMO, 大概想法是固定多余的参数, 每次只对一个参数进行优化. 但是在我们的问题中, 参数是有约束的, 不可能每次只变动一个参数, 所以每次选择两个参数$\alpha_i$和$\alpha_j$更新, 现在约束变成
$$
\alpha_i y_i + \alpha_j y_j = c, \quad \alpha_i \geq 0, \quad \alpha_j \geq 0,
$$
其中$c = -\sum_{k\neq i, j}\alpha_k y_k$. 现在得到$\alpha_j = (c - \alpha_i)/y_j$, 使用$\alpha_i$来表达$\alpha_j$, 现在问题变成一个一维的优化问题, 注意$\alpha_i \geq 0$, $\alpha_j \neq 0$的约束, 可以简单求出满足条件的$\alpha_i$, 然后得到$\alpha_j$.

重复这个过程, 我们最终得到合适的解$\alpha^*$.

## 优化结果

现在根据$w = \sum_i \alpha_i y_i x_i$就可以得到$w$, 此外, 那些$\alpha_i > 0$对应的点都是支持向量, 我们可以随意选择一个支持向量, 根据$y_s(w^T x_s + b) - 1 = 0$, $y_s^2(w^T x_s + b) = w^T x_s + b = y_s$, 得到$b = y_s - w^Tx_s$, 也可以对所有的支持向量求对应的均值.

现在有了$w$和$b$, 这个超平面就被完全确定下来, 最终的决策函数是
$$
f(x) = \mathrm{sgn}(w^T x + b).
$$

## 软间隔

有时候问题可能不是线性可分的, 但相差并不大, 我们允许少量的点跑到超平面的另一侧去. 现在优化目标写成
$$
\min_{w}\frac{1}{2}||w||^2 + C\sum_i \xi_i, \quad
g_i(w, b) = 1 - y_i(w^T x_i + b) - \xi_i \leq 0, \quad \xi_i \geq 0.
$$
其中$\xi_i$是一个松弛变量, 表示对于每个样本超出了支持向量的程度. 我们使用和硬件个类似的优化过程, 最终到SMO的时候优化的函数是相同的, 只是多了一个额外的约束$C - \alpha_i - \mu_i = 0$, $\mu_i$是在Lagrangian函数中$\xi_i$的Lagrangian乘子. 其余的计算过程是类似的.

## 核函数

对于线性不可分的样本来说, 如果它偏离线性可分的程度比较大, 那么软间隔的方法也不能使用了. 一种考虑是将原本的样本映射到更高维的空间中, 使得样本变成线性可分的, 之后进行上述的计算, 这就是非线性SVM.

假设把原本样本空间的点$x$映射到$\phi(x)$上, 那么这个非线性SVM的对偶问题变成了
$$\begin{gathered}
\min_\alpha \left[ \frac{1}{2}\sum_{ij}\alpha_i\alpha_j y_i y_j (\phi(x_i)\cdot \phi(x_j)) \right],\\
\sum_i \alpha_i y_i = 0,  \alpha_i \geq 0, C - \alpha_i - \mu_i = 0.
\end{gathered}$$
区别只在$(x_i\cdot x_j)$变成了$(\phi(x_i)\cdot \phi(x_j)) = k(x_i, x_j)$, 称作核函数, 其实只是希望可以在原本的空间中计算$\phi(x)$之间的点积, 而不需要在更高维的空间中计算. 最终的预测结果是$\sum_i w_i k(x, x_i) + b$.

总的来说SVM是一个比较适用于小样本量的方法.

# Relevance vector machine (RVM)

## 多核RVM

RVM是一种稀疏线性模型, 它的基函数通过在不同样本处给出的核函数$k(x, x_i)$给出:
$$
y(x) = \sum_{i = 1}^N w_i k(x - x_i).
$$
多核RVM是RVM的简单扩展, 允许适用不同种类的核函数:
$$
y_(x) = \sum_{i = 1}^N\sum_{m = 1}^M w_{mi}k_m(x - x_i).
$$
这种拟设允许在不同的样本上选用不同的核函数, 当然也可能是多个核函数都存在.

## Sparse Bayesian prior

对于权重$w_i$的分布, 我们先验地假设其服从高斯分布, 并且每个$w_i$有不同的方差参数$\alpha_i$,
$$
p(w|\alpha) = \prod_{i = 1}^M N(w_i|0, \alpha_i^{-1}).
$$
其中超参数$\alpha_i$被假设服从Gamma分布
$$
p(\alpha_i) = \Gamma(a, b).
$$
在积掉超参数$\alpha$之后, 我们得到权重的分布$p(w) = \int \mathrm d\alpha p(w|\alpha)p(\alpha)\mathrm d\alpha$.

## Bayesian inference