---
title: Metropolis algorithm for classical Ising model
date: '2024-11-24T10:34:55+08:00'
categories:
- notes
---


## Metropolis-Hasting algorithm

### Algorithm

Metroplis-Hasting algorithm is to get an equilibrium probability distribution using a Markov chain.

The transition matrix $W(x\rightarrow y)$ defines a Markov chain and it's the probability that the state goes to state $y$ in the next state when it's in the state $x$. The Markov chain finally becomes the equilibrium state with a distribution $P(x)$.

Equilibrium condition need to be satisfied: $\sum_y P(x)W(x\rightarrow y) = \sum_y P(y)W(y\rightarrow x)$
- $\sum_y W(x\rightarrow y) = 1$


The question is that **if we want to get the equilibrium, what markov chain should we construct**. The transition matrix need to be satisfy the following conditions(not necessary):
- $\sum_y W(x\rightarrow y) = 1$
- ergodicity: it should be possible to reach any state from any other state
- detailed balance: $P(x)W(x\rightarrow y) = P(y)W(y\rightarrow x)$

Now we start to construct the transition matrix. Break the transition probability into two parts, $W(x\rightarrow y) = Q(x\rightarrow y)A(x\rightarrow y)$. So the transition is done in two steps(suppose the state is now in $x$): 1. first generate a new state $y$ according to a probability distribution $Q(x\rightarrow y)$(this distribution is decided by us so it may not satisfy the detailed balance condition); 2. decide whether we accept the transition according to $A(x\rightarrow y)$, then the total transition probability satisfies the detailed balance probability.

Then the problem changes to how to find $A(x\rightarrow y)$ according to a given $Q(x\rightarrow y)$. We choose 
$$A(x\rightarrow y) = \min(1, \frac{P(y)Q(y\rightarrow x)}{P(x)Q(x\rightarrow y)})$$

If $Q(x\rightarrow y)$ is symmetric, it can be simplified and is called Metropolis algorithm,
$$A(x\rightarrow y) = \min(1, \frac{P(y)}{P(x)})$$

By now we have constructed the markov chain $W(x\rightarrow y)$. By iteration, we can get the distribution we want.

### Application to classical Ising model

#### Ising model

The classical Ising model
$$\mathcal{H} = -J\sum_{<i, j>}\sigma_i\sigma_j+H\sum_i \sigma_i$$

The average energy
$$\langle E \rangle = \frac{1}{Z}\sum_{\{\sigma_i\}}E(\{\sigma_i\})e^{-\beta E(\{\sigma_i\})}$$

The specific heat
$$
\begin{aligned}
C = & \frac{\partial E}{\partial T} = -\frac{1}{kT^2}\frac{\partial E}{\partial \beta} \\
= & -\frac{1}{kT^2}(-\frac{\frac{\partial Z}{\partial \beta}}{Z}\langle E\rangle - \frac{1}{Z}\sum_{\{\sigma_i\}}E(\{\sigma_i\})^2 e^{-\beta E(\{\sigma_i\})}) \\
= & \frac{1}{kT^2}(\langle E^2\rangle - \langle E\rangle^2)
\end{aligned}
$$

The average magnetization
$$\langle M\rangle = \frac{1}{Z}\sum_{\{\sigma_i\}}m(\{\sigma_i\})e^{-\beta E(\{\sigma_i\})}$$

The magnetic susceptibility
$$
\begin{aligned}
\chi = &  \frac{\partial \langle M\rangle}{\partial H} \\
= & -\frac{1}{Z}\langle M \rangle \frac{\partial Z}{\partial H} + \frac{1}{Z} \sum_{\{\sigma_i\}}m(\{\sigma_i\})\frac{\partial e^{-\beta E(\{\sigma_i\})}}{\partial H} \\
= & -\frac{1}{Z}\langle M \rangle \sum_{\{\sigma_i\}}\frac{\partial Z}{\partial E(\{\sigma_i\})}\frac{\partial E(\{\sigma_i\})}{\partial H} \\
 & + \frac{1}{Z} \sum_{\{\sigma_i\}}m(\{\sigma_i\})\frac{\partial e^{-\beta E(\{\sigma_i\})}}{\partial E(\{\sigma_i\})}\frac{\partial E(\{\sigma_i\})}{\partial H} \\
= & \frac{1}{Z}\langle M\rangle \sum_{\{\sigma_i\}}\beta m(\{\sigma_i\})e^{-\beta E(\{\sigma_i\})} \\
& - \frac{1}{Z}\sum_{\{\sigma_i\}}\beta m(\{\sigma_i\})^2e^{-\beta E(\{\sigma_i\})} \\
= & -\frac{1}{kT}(\langle M^2\rangle - \langle M\rangle^2)
\end{aligned} 
$$

The phase transition happens at $T_c = \frac{2J}{\ln(1+\sqrt{2})}$ for $2$D Ising model.

#### Monte Carlo simulation

We choose the transition to change states as flipping a spin. We choose $Q(x\rightarrow y)$ to be uniform. Then
$$A(x\rightarrow y) = \min(1, \frac{P(\{\sigma_{\text{trival}}\})}{P(\{\sigma_{\text{old}}\})})$$

We evaluate the number
$$\alpha = \frac{P(\{\sigma_{\text{trival}}\})}{P(\{\sigma_{\text{old}}\})} = \exp(-\beta \Delta E)$$

$$\Delta E = 2\sigma_j(J\sum \sigma_{\text{near}} - H)$$

By now we get how to do iteration. The algorithm is 
- 1. initialization a configuration
- 2. take some steps to warm up and get to the equilibrium then the state is indeed in the probability distribution as stat. mech. shows
- 3. sparse averaging

## Code

```python
def InitSpin(L):
    'Initialization of an arbitrary configuration'

    return np.random.choice([1, -1], size=[L, L])

def Acceptation(Sigma, pos, args, beta):
    '''
    Judge whether a flip can happen
    Sigma: the initial configuration
    pos = (x, y), where the flip happens
    args = (J, H), parameters for the Hamiltonian
    beta: the inverse temperature
    '''

    L = Sigma.shape[0]
    (J, H) = args

    # energy change for the flip
    deltaE = 2 * Sigma[pos] * (
        - H + J * (Sigma[np.mod(pos[0]-1, L), pos[1]] + Sigma[np.mod(pos[0]+1, L), pos[1]] + 
                   Sigma[pos[0], np.mod(pos[1]-1, L)] + Sigma[pos[0], np.mod(pos[1]+1, L)])
    )

    alpha = np.exp(-beta * deltaE) # the acceptation probability
    r = np.random.random()

    if_goon = False
    if deltaE < 0 or r < alpha:
        if_goon = True
    
    return if_goon

def Sample(L, args, beta, n_sample, n_iter, n_get):
    '''
    A whole algorithm including initialization, warming up and sampling
    L: system size
    args: parameters of the Ising model
    beta: inverse temperature
    n_sample: the size of sample we want to get
    n_iter: the time of iteration for warming up
    n_get: after `n_get` steps of Markov chain we take up a sample
    '''

    # initialization
    Sigma = InitSpin(L)

    SampleList = np.empty([n_sample, L, L])

    iter = 0
    n_sample_getten = 0
    while n_sample_getten < n_sample:
        # trival move
        pos = (np.random.randint(0, L), np.random.randint(0, L))

        if_goon = Acceptation(Sigma, pos, args, beta)
        if if_goon:
            Sigma[pos] = -Sigma[pos]
        iter = iter + 1

        if iter > n_iter and iter % n_get == 0:
            SampleList[n_sample_getten] = Sigma
            n_sample_getten += 1

    return SampleList

if __name__ == '__main__':
    
    args = (1, 0) # (J, H)
    L = 10

    n_iter = 100000 # n for warming up
    n_sample = 10000 # sample size
    n_get = 100 # steps to get a new size

    N = 2**7
    TList = np.linspace(1.0, 3.5, N)
    BetaList = 1 / TList

    Tc = 2 * args[0] / np.log(1+np.sqrt(2))

    EnergyList = np.empty(N)
    SpecificHeatList = np.empty(N)
    MList = np.empty(N)
    SusceptibilityList = np.empty(N)

    for i in tqdm(range(N)):
        beta = BetaList[i]

        sample_list = Sample(L, args, beta, n_sample, n_iter, n_get)
        m_list = np.sum(sample_list, axis=(1, 2))
        energy_list = np.sum(sample_list * np.roll(sample_list, 1, axis=1), axis=(1, 2)) +\
                      np.sum(sample_list * np.roll(sample_list, 1, axis=2), axis=(1, 2))
        energy_list = args[1] * m_list - args[0] * energy_list

        EnergyList[i] = np.mean(energy_list) / L**2
        MList[i] = np.mean(m_list) / L**2
        SpecificHeatList[i] = (np.mean(energy_list ** 2) / L**2 - EnergyList[i]**2 * L**2) * beta**2
        SusceptibilityList[i] = (np.mean(m_list**2) / L**2 - MList[i]**2 * L**2) * beta

    with open('data.pkl', 'wb') as opt:
        pickle.dump((TList, EnergyList, MList, SpecificHeatList, SusceptibilityList), opt)

    print('Done')
```