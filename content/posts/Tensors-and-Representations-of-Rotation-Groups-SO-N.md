---
title: Tensors and Representations of Rotation Groups SO(N)
date: '2024-11-13T11:45:15+08:00'
description: notes for IV.1 of *Group theory in a nutshell for physicists*
categories:
- notes
---



### Representing the rotation groups

**def.** SO(N) group is all $N$-by$N$ matrices $R$ satisfying
$$R^T R = I$$
$$\mathrm{det}R = 1$$
A column of number $V$ is a vector if under rotation it becomes $V'^i = R^{ij}V^j$.

### Several questions and some flying guesses

The finite group $Z_N$, generating rotation of angle $2\pi/N$, has $N$ $1$-dimensional irreducible representations, labeled by $k=0, \cdots, N-1$. The group element $e^{i2\pi j/N}$ is represented by $D^{(k)}(e^{i2\pi j/N}) = e^{i2\pi kj/N}$. As $N\rightarrow \infty$, the finite group $Z_N$ turn into the continuous group $SO(2)$. So $SO(2)$ should have an infinite number of irreducible representations corresponding to $k=0,\cdots,\infty$. The rotation is represented by $e^{ik\theta}$.

This is indeed a representation for $SO(2)$, because $D^{(k)}(\theta)D^{(k)}(\theta')=D^{k}(\theta+\theta')$ and $D^{(k)}(2\pi) = 1$. 

We hope to find that $SO(3)$ has an infinite number of irreducible representations labeled by an integer.

### Constructing the irreducible representations of $SO(N)$

A set of number $T$ is a tensor if under rotation it become $T'^{ij} = R^{ik}R^{jl}T^{kl}$.

A tensor in shape $[3, 3]$ can be written in a column(reshaped in shape $[9]$). The linear transformation on the tensor can be represented by $9$-by-$9$ matrix $D(R)$ acting on this column(here we do not use the term "vector" as they are used for a more strict definition). $D(R)$ gives a 9-dimensional representation of $SO(3)$.

The problem is that the representation is **reducible** or **irreducible**.

Consider such a tensor $A^{ij} = T^{ij} - T^{ji}$. Under a rotation,
$$
\begin{aligned}
A^{ij}\rightarrow A'^{ij} =  & R^{ik}R^{jl}T^{kl} - R^{jk}R^{il}T^{kl} \\
= & R^{ik}R^{jl}T^{kl} - R^{jl}R^{ik}T^{lk} \\
= &  R^{ik}R^{jl}(T^{kl}-T^{lk}) = R^{ik}R^{jl}A^{kl}
\end{aligned}
$$
$A^{ij}$ transforms like a tensor and is thus a tensor. Such a $N$-dim antisymmetric rank-$2$ tensor has $N(N-1)/2$ independent components.

We can also construct symmetric tensor $S^{ij} = T^{ij} + T^{ji}$, which has $N(N-1)/2$ independent components.

$A$ and $S$ are two invariant subspace of $T$. In $3$-D case, they have $3$ and $6$ components, respectively. So the $9$-by-$9$ dimensional matrix must break into a $3$-by-$3$ and $6$-by-$6$ dimensional block. 

The work should continue for the $6$-dimensional representation is also reducible. Note that
$$
\begin{aligned}
S^{ii}\rightarrow S'^{ii} = & R^{ik}R^{il}S^{kl} = \delta^{kl}S^{kl} = S^{kk}
\end{aligned}
$$
the trace of $S$ transforms into itself(in fact under any similarity transformation the trace does not change). So the $6$-by$6$ matrix describing the linear transformation of $S$ breaks up into a $1$-by-$1$ block and a $5$-by-$5$ block.

We now want to find the five objects that furnish the representation $5$ of $SO(3)$. We define such a traceless symmetric tensor
$$\tilde{S}^{ij} = S^{ij} - \delta^{ij}(S^{kk}/3)$$
The five object are $\tilde{S}^{11}$, $\tilde{S}^{22}$, $\tilde{S}^{12}$, $\tilde{S}^{13}$ and $\tilde{S}^{23}$. The linear transformation can be written in a $5$-by-$5$ matrix.

We say that in $SO(3)$, $9 = 5 \oplus 3 \oplus 1$. It is similar for the $N^2$-dim representation of $SO(N)$, $N^2 = \frac{1}{2}N(N-1) \oplus (\frac{1}{2}N(N+1)-1) \oplus 1$.

### Invariant symbols

In $N$-d space, the antisymmetric symbol $\epsilon$ is an array in shape `[N] * N` defined by $\epsilon^{\cdots l \cdots m \cdots} = - \epsilon^{\cdots m \cdots l \cdots}$ and $\epsilon^{12\cdots N} = 1$ with other components vanishing. It can be related to the determinant, for any matrix $R$,
$$\epsilon^{ijk\cdots n}R^{ip}R^{jq}R^{kr}\cdots R^{ns} = \epsilon^{pqr\cdots s}\mathrm{det} R$$
For rotation matrix $\mathrm{det} R = 1$, we have
$$\epsilon^{ijk\cdots n}R^{ip}R^{jq}R^{kr}\cdots R^{ns} = \epsilon^{pqr\cdots s}$$

$\delta^{ij}$ and $\epsilon^{ijk\cdots n}$ are invariant symbols as they turn into themselves under rotation. When the antisymmetric symbol is contracted with any symmetric tensor, the result vanish.

### Dual tensors

Given a **antisymmetric**(why need antisymmetric?) tensor $A^{ij}$, we can define $B^{k\cdots n} = \epsilon^{ijk\cdots n}A^{ij}$. This is a antisymmetric tensor, 
$$B^{k\cdots n}\rightarrow \epsilon^{jkl\cdots n}R^{ip}R^{jq}A^{pq} = \epsilon^{pqr\cdots s}R^{kr}\cdots R^{ns}A^{pq} = R^{kr}\cdots R^{ns}B^{r\cdots s}$$

We have written the $9$-D representation as $9 = 5 \oplus 3 \otimes 1$. The $1$ is the trivial representation. The $3$ is just the defining representation. The $5$ is nontrivial.

### Constructing larger irreducible representations of $SO(N)$

We hope to construct larger irreducible representations from the transform of higher rank tensor $T^{ijk\cdots n}$. The transform does not change the symmetry or anti-symmetry on several of its indices. The partial trace transforms like a lower-rank tensor.

### Why $SO(3)$ is special?

$3 - 2 = 1$, we can treat a pair of antisymmetric indices as a single index. Consider a rank-$3$ tensor $T^{ijk}$, we can first symmetrize and antisymmetrize in the first two indices. For the antisymmetric part, it's just a rank-$2$ tensor, $B^{lk} = \epsilon^{ijl}T^{[ij]k}$, of which the representation can be written as $9 = 5 \oplus 3 \oplus 1$ as we already know.

For the symmetric part $T^{\{ij\}k}$, we can write it symmetric in all three indices by force. $3T^{\{ij\}k} = (T^{\{ij\}k} + T^{\{jk\}i} + T^{\{ki\}j}) + (T^{\{ij\}k} - T^{\{jk\}i}) + (T^{\{ij\}k} - T^{\{ki\}j})$. In the first bracket there is a totally symmetric part. The other two bracket are antisymmetric for indices $ik$ and $jk$, and can be seen as rank-$2$ tensors by multiplying $\epsilon$.

So now there is only the totally symmetric part $\tilde{S}'^{ijk}$. We remove its partial trace(the traced indices are arbitrary, for it's totally symmetric) $\delta^{ij}\tilde{S}^{ijk}$. 

### Dimension of the irreducible representations of $SO(3)$

Consider a traceless and totally symmetric rank-$j$ tensor $S^{i_1 \cdots i_j}$. First suppose the indices can take only two values, $1$ and $2$. The independent components are $S^{22\cdots 2}$, $S^{22\cdots 1}$, $S^{22\cdots 11}$. Depending on the number of $1$s, we have $j+1$ independent components. Then we allow the indices to take value $3$, the possibilities are $S^{33\dots 3xx\cdots x}$. If there are $k$ $x$s, the number of possible configurations for $x$ is $k+1$. So the total number of independent components is
$$\sum_{k = 0}^{j}(k+1) = \frac{1}{2}(j+1)(j+2)$$

The partial trace $\delta^{ij}S^{i_1i_2\cdots i_j}$ is a rank-$(j-2)$ totally symmetric tensor. If we need $S$ to be traceless, the total number of independent components is 
$$\frac{1}{2}(j+1)(j+2) - \frac{1}{2}j(j-1) = 2j+1$$

### The tensors of $SO(2)$

The number of independent components for a $2$-D rank-$j$ tensor is $j+1$. Considering the traceless condition, the actual number is $d = (j+1) - (j-1) = 2$. The $2$-by-$2$ matrix is still reducible($SO(2)\leftrightarrow U(1)$).

### Rotations in higher-dimensional space

For a rank-$5$ $3$-D tensor $T^{hijkl}$ that is symmetric in $hij$ and antisymmetric in $kl$. Contracting with $\epsilon^{klm}$, it becomes a rank-$4$ tensor. If it's in $4$-D, contracting with the antisymmetric symbol $\epsilon^{klmn}T^{hijkl}$, a tensor with the same number of indices. So for $N > 3$, we have to confront tensors with complicated symmetry patterns on interchanges of indices.

### Self-dual and anti-self-dual

That's the feature of $SO(2n)$. Consider the antisymmetric tensor with $n$ indices $A^{i_1 i_2 \cdots i_n}$ with $C^{n}_{2n} = \frac{(2n)!}{(n!)^2}$ independent components(select $n$ different values (no same value) in the given $2n$ values).

$A$'s dual tensor $B^{i_1i_2\cdots i_n} = \frac{1}{n!}\epsilon^{i_1i_2\cdots i_{2n}}A^{i_{n+1}\cdots i_{2n}}$. $A$ is also dual $B$, $A^{i_{n+1}\cdots i_{2n}} = \frac{1}{n!}\epsilon^{i_1i_2\cdots i_{2n}}B^{i_1i_2\cdots i_n}$.

So there are two tensor $T_{\pm}^{i_1i_2\cdots i_n} = (A^{i_1i_2\cdots i_n}\pm B^{i_1i_2\cdots i_n})$, that are self-dual and anti-self-dual. $\epsilon T_{\pm} \sim \epsilon (A\pm B) \sim B\pm A \sim \pm (A \pm B) \sim \pm T_{\pm}$. This two tensors correspond to two irreducible representations with dimension $\frac{(2n)!}{(2(n!)^2)}$.

### Restriction to a subgroup

Consider an irreducible representation of some group $G$. For a subgroup $H \subset G$, the irreducible representation of $G$ breaks into several irreducible representations of $G$.

Let $G = SO(4)$, $H = SO(3)$. The $4$-D representation of $SO(3)$ breaks into a $3$-D representation and a $1$-D representation of $SO(3)$.

The $6$-D representation of $SO(4)$ furnished by antisymmetric tensor $A^{ij}$ breaks up as $6 = 3 \oplus 3$. The $9$-D representation of $SO(4)$ is furnished by the traceless symmetric tensor $A^{ij}$. The element $S^{44}$ is unchanged under $SO(3)$ and it furnishes a $1$-D representation. The column $S^{a4}(a = 1, 2, 3)$ furnishes a $3$-D representation. Then there is just a traceless $3$-D rank-$2$ tensor, furnishing the irreducible $5$-D representation of $SO(3)$.

### The adjoint representation and the Jacobi identity

The three matrices
$$J_x = -i
\begin{pmatrix}
0 & 0 & 0 \\
0 & 0 & 1 \\
0 & -1 & 0 \\
\end{pmatrix}
$$
$$J_y = -i
\begin{pmatrix}
0 & 0 & -1 \\
0 & 0 & 0 \\
1 & 0 & 0 \\
\end{pmatrix}
$$
$$J_z = -i
\begin{pmatrix}
0 & 1 & 0 \\
-1 & 0 & 0 \\
0 & 0 & 0 \\
\end{pmatrix}
$$
representing the Lie algebra of $SO(3)$ and obtain the commutation  relation
$$[J_a, J_b] = i\epsilon_{abc}J_c$$

Is it a coincidence that we have $(J_a)_{bc} = -i \epsilon_{abc}$, i.e. the generators are given by the structure constant? First it cannot be general. The defining representation of $SO(N)$ is $N$-D, while the indices on the structure constants $f^{abc}$ range over $(N-1)N/2$(generators for $SO(N)$, the antisymmetric part) values. It is only for $N = 3$ that $N = (N-1)N/2$.

However, the structure constants indeed furnish a representation, the adjoint representation. We have the Jacobi identity,
$$[[A, B], C] + [[B, C], A] + [[C, A], B] = 0$$

A Lie algebra is defined by 
$$[T_a, T_b] = if_{abc}T_c$$
in which the indices run over $1, \cdots, n$ and $n$ is the number of generators of the algebra. Now apply the relation into the Jacobi identity,
$$f^{abc}f^{dcg}+f^{bcd}f^{dag}+f^{cad}f^{dbg} = 0$$
Define a set of matrices $(T^{b})_cd = -if^{abc}$. These are the matrices representing $T^{b}$ in the adjoint representation. We need to prove that it is indeed a representation. $f^{abd}f^{dcg} = i f^{abc} (T^d)^{cg}$. $f^{bcd}f^{dag}+f^{cad}f^{dbg} = -(T^{b})^{cd}(-T^a)^{dg} - (-T^{a})^{cd}(-T^b)^{dg} = -([T_a, T_b])^{cg}$. So we have $([T^a, T^b])^{cg} = i f^{abd}(T^d)^{cg}$.

**Is this a circular argument?**

### The adjoint of $SO(N)$

The generators represented in the defining $N$-D representation of $SO(N)$ are antisymmetric matrices
$$\mathcal{J}^{ij}_{(mn)} = (\delta^{mi}\delta^{nj} - \delta^{mj}\delta^{ni})$$
For any antisymmetric $N$-by-$N$ matrix $T^{ij}$, we can regard it as a linear combination of $\mathcal{J}^{ij}_b$,
$$T^{ij} = \sum_{a=1}^{\frac{1}{2}N(N-1)}A_a\mathcal{J}^{ij}_{a}$$
In other words, we can treat $T^{ij}$ as $A_a$ and vice versa. We want to know how $A_a$ transform. $T' = RTR^T$. For an infinitesimal rotation, $R \approx I + \theta_a \mathcal{J}_a$.
$$T' \approx T + \theta_a [\mathcal{J}_a, T]$$
The variation of $T$ under rotation is given by $\delta T = \theta_a [\mathcal{J}_a, T] = \theta_a A_b [\mathcal{J}_a, \mathcal{J}_b]$. $\delta T = \delta A_c \mathcal{J}_c = i f_{abc}\theta_a A_b \mathcal{J}_c$.
$$\delta A_c = i f_{abc}\theta_a A_b$$
$A_a$ furnish the adjoint representation. For $SO(3)$, the above is just $\delta \vec{A} = \vec{\theta} \otimes \vec{A}$.

---

什么是adjoint representation没有搞得很明白。但书是好书，之后可以多看一点。