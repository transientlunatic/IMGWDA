Probability
###########

In this work I consider \`\`probability'' as a measure of evidential
support for a given outcome or event (this is the so-called
*quasi-logical* interpretation). For example, a coin, when tossed, can
take one of two states when it lands, which I call *heads* or *tails*; I
denote these two states :math:`H` and :math:`T`. Assuming that I have no
knowledge of a reason why the coin would fall one way rather than the
other, I am forced to conclude that I have no more evidence to suggest
that the coin will fall heads, compared to it falling tails.

With this philosophy, it is possible to construct an axiomatic
mathematical model of probability. Here I will follow the approach taken
by Kolmogorov cite:kolmogorov, approaching from set theory principles.
By making some additional demands on this model, one of which is that an
event which is considered \`\`certain'' should have a probability of
:math:`1`, it is possible to maintain consistency with boolean logic.
Likewise, if an event is certain not to occur, it is assigned a
probability :math:`0`.

In order to make future discussions more concise I define two concepts
related to the configuration of a probabilistic system: *sample space*
and *state*.

.. raw:: html

   <div class="definition">

If a variable can take on a number of different values, then the set of
all its possible values is called the sample space. In any given
problem, the sample space composes the universe set, and is often
denoted :math:`\Omega`.

.. raw:: html

   </div>

The sample space is analogous to the *configuration space* of a
(classical) physical system, or the *state space* of a quantum
mechanical one.

.. raw:: html

   <div class="definition">

A state is any subset of zero or more elements from the sample space. A
state containing one element is a simple state, while one containing
more than one element is a compound state. The states form a
:math:`\sigma`-algebra on the sample space.

.. raw:: html

   </div>

Since the configuration of a probabilistic system is often
time-dependent it is often natural to refer to a given state as an
*event*.

Kolmogrov then postulates three axioms for probability
cite:sepprobabilityinterpret.

.. raw:: html

   <div class="definition">

Let :math:`x` be some variable which is capable of having a state
:math:`E \in \Omega` for :math:`\Omega` the *sample space* of the
variable. Probability :math:`P` is a mapping :math:`P: E \to [0,1]`
which assigns a real value between :math:`0` and :math:`1` to every
:math:`E \in \Omega`. We place three constraints on the form of this
mapping:

#. For every :math:`E \in \Omega`, :math:`P(E) \geq 0`.
#. :math:`P(\Omega) = \sum_{E \in \Omega} P(E) = 1`.
#. For two states, :math:`A, B \in \Omega` which are disjoint, such that
   :math:`A \cap B = \emptyset`, then :math:`P(A \cup B) = P(A) + P(B)`

.. raw:: html

   </div>

The first axiom ensures that all probabilities are positive, and that if
a state exists within the sample space it has a probability greater than
zero. It follows that states which do not exist (i.e. events which
cannot occur) have zero probability.

The second axiom fulfils the requirement that the total probability of
all possible states should be :math:`1`, and that the probability of the
system having taking one state from the sample space (i.e. of one of the
possible events occurring) is :math:`1`.

Finally, the third axiom defines how the probability of subsets within
the sample space should be calculated. Provided a set of states are
*mutually exclusive* (i.e. that they are disjoint in the sample space),
the probability of the states together is equal to the sum of their
individual probabilities.

Alternative axioms for probability also exist which do not attempt to
define the theory so strongly in terms of measure theory, for example,
*Cox's axioms* cite:2003prth.book.....J.

The basic logical operations can be extended to probabilities; the
equivalent of the **AND** operation becomes the probability of the
conjunction of two subsets of the sample space:

.. raw:: html

   <div class="definition">

Given two states, :math:`A,B \in \Omega`, the probability of both
states, :math:`P(A \cap B)` is termed their \`\`joint probability''. In
the case that these states are independent it is computed as

.. math::  P(A \cap B) = P(A) P(B). 

.. raw:: html

   </div>

Equally, the **OR** operation becomes the probability of the union of
subsets of sample space:

.. raw:: html

   <div class="definition">

Given two states :math:`A,B \in \Omega`, the probability of either
:math:`A` or :math:`B` is
:math:`P(A \cup B) = P(A) + P(B) - P(A \cap B)`.

.. raw:: html

   </div>

In the case that of two events which occur with some dependence between
them, we can form a \`\`conditional probability'', for example, if there
can be no smoke without fire, then the probability of smoke can be
conditional on the probability of fire.

.. raw:: html

   <div class="definition">

Given two events, :math:`A,B \in \Omega`, then the probability of
:math:`A` *given* :math:`B` is

.. math::  P(A | B) = \frac{ P(A,B) }{ P(B) }. 

 If :math:`P(B) = 0` then :math:`P(A)` is undefined.

.. raw:: html

   </div>

Given that :math:`P(A,B) = P(B,A)`, we have
:math:`P(A,B) = P(B,A) = P(B|A)P(A)`, which leads us to a powerful
result in probability: **Bayes Theorem** cite:bayesessay.

.. raw:: html

   <div class="theorem">

Given two events, :math:`A` and :math:`B`, we may represent the
probability of :math:`A` given :math:`B` in terms of the probability of
:math:`B` given :math:`A`:

.. raw:: latex

   \begin{equation}
       \label{eq:probability:bayes}
       P(A|B) = \frac{ P(A) P(B|A) }{ P(B) }. 
   \end{equation}

.. raw:: html

   </div>

A useful corollary in the case of two independent states :math:`A,B`
(i.e. states which are disjoint in the sample space),

.. math:: P(A|B) = \frac{P(A,B)}{P(B)} = \frac{(P(A)P(B))}{P(B)} = P(A).

There may also be situations where two variables become independent if
the state of a third variable is known, providing conditional
independence.

.. raw:: html

   <div class="definition">

Two states, :math:`A,B` are said to be conditionally independent given a
third state, :math:`C`, if

.. math::  P(A,B | C) = P(A|C)P(B|C).

 We can denote conditional independence as
:math:`A\!\perp\!\!\!\perp\!B\,|\,C`.

.. raw:: html

   </div>

From here on I will start to substitute the concept of a state or event
for a variable which represents that state, so the notation :math:`P(x)`
will represent the probability of a variable state :math:`x`. Since a
variable can represent a set of potential states, we can introduce a
function which maps from the variable to the probability.

In the case of a discrete sample space this function is the probability
mass function.

.. raw:: html

   <div class="definition">

For a discrete variable :math:`x`, the probability mass function,
:math:`p`, of the variable is the mapping :math:`p(x) = P(X=x)`

.. raw:: html

   </div>

In the case of a continuous sample space the mapping :math:`p` is known
as a abbr:pdf, which is defined

.. raw:: html

   <div class="definition">

For a continuous variable :math:`x`, the probability density function
:math:`p` of the variable is the mapping :math:`p_X` such that the
probability of a state between :math:`a` and :math:`b` is

.. raw:: latex

   \begin{equation}
    P(a \leq X \leq b) = \int_{a}^{b} p_X (x) \dd{x} 
   \end{equation}

.. raw:: html

   </div>

It is normal to use the short-hand notation :math:`p(x)` for the
probability of a value :math:`x` to represent
:math:`\int_{-\epsilon}^{\epsilon} p(x) \dd{x}` for a small value of
:math:`\epsilon`.

Information
===========

Understanding how informative an random variable, :math:`X` is can
provide insight into how well observations of that variable will inform
our knowledge of the probability distribution from which it is drawn.

.. raw:: html

   <div class="definition">

Given a abbr:pdf, :math:`p`, for a random variable, :math:`X`, which is
parameterised by a variable :math:`\theta`, the *score*, :math:`V` of
the abbr:pdf is defined

.. raw:: latex

   \begin{equation}
   \label{eq:probability:score}
   V(\theta, X) = \frac{\partial}{\partial X} \log p(X, \theta).
   \end{equation}

The variance of the score is the *Fisher information* of the
distribution:

.. raw:: latex

   \begin{equation}
   \label{eq:probability:fisher}
   I(\theta, X) = \mathbb{E}(V^{2} | \theta) = \int V^{2} p(X, \theta) \dd{x}.
   \end{equation}

.. raw:: html

   </div>

Knowledge of the Fisher information for a given distribution is
particularly valuable in selecting an *uninformative prior* (see section
ref:sec:probability:priors:uninformative) when designing a Bayesian
analysis, where it can be valuable for the prior probability
distribution to contribute no information to the inference.

.. raw:: html

   <div class="definition">

Given a abbr:pdf, :math:`p`, for a random variable :math:`X` the
*Shannon information content* of a given value :math:`x` of :math:`X` is
defined as

.. raw:: latex

   \begin{equation}
   \label{eq:probability:shannon}
   h(x) = \log_{2} p^{-1}(x)
   \end{equation}

where the information is measured in *bits* (assuming that a base-2
logarithm is used; if the natural logarithm is used the units are
*nats*, and the base-10 gives rise to the *dit*).

.. raw:: html

   </div>

.. raw:: html

   <div class="definition">

The entropy of a random variable :math:`X` with a abbr:pdf, :math:`p` is
the average Shannon information of the random variable across all its
possible values:

.. raw:: latex

   \begin{equation}
   H(X) = \int p(X) h(X) \dd X
   \end{equation}

taking :math:`0 \log (1/0) \equiv 0`.

.. raw:: html

   </div>

Comparing probability distributions
-----------------------------------

The information difference between two probability distributions, or
indeed the information gain of one relative to another can be an
important metric when producing inferential models.

\\begin{definition} [Kullback-Lieblier Divergence] For two probability
distributions, :math:`P` and :math:`Q` the Kullback-Liebler Divergence
characterises the relative information content of the two, and is
defined as

.. raw:: latex

   \begin{equation}
   \label{eq:probability:kl}
   D_{\text{KL}} (P, Q) = \int_{-\infty}^{\infty} \log \left[ \frac{p(x)}{q(x)} \right] p(x) \dd{x}
   \end{equation}

\\end{definition}

A related metric, the Shannon-Jensen divergence is symmetric and always
finite.

.. raw:: html

   <div class="definition">

For two probability distributions, :math:`P` and :math:`Q` the
Shannon-Jensen Divergence characterises the relative information content
of the two, and is defined as

.. raw:: latex

   \begin{equation}
   \label{eq:probability:kl}
   D_{\text{SJ}} (P, Q) = \frac{1}{2} D_{\text{KL}}(P,Q) + \frac{1}{2} D_{\text{KL}}(Q,P)
   \end{equation}

.. raw:: html

   </div>

Prior knowledge
===============

The *prior* probability distribution is perhaps the characterising
feature of the Bayesian approach to statistics, whereby the state of
belief prior to any observation being made is encoded in a probability
distribution. Bayes Theorem allows the *updating* of our state of
belief, with the prior distribution being updated by data collected from
observation or experiment.

The least informative priors
----------------------------

While the ability to incorporate prior knowledge into an inference is
valuable, there are clearly times when we have *no* prior knowledge of a
situation. In these situations we must turn to *least informative*
priors, which place the same probability on any possible event in the
sample space. The simplest approach to constructing such a prior is
through the *principle of indifference*, whereby equal probability is
assigned to every possible state. For example, if we wished to conduct
an experiment to determine the fairness of a 20-sided die, but had no
prior knowledge to assume that one side was more likely to be rolled
(which is the desirable state for a fair die) then we would assume each
side had a probability of :math:`1/20` of being rolled. In a continuous
system such an arrangement is represented as a uniform distribution.
Such an approach must be taken with care, however.

Consider the situation in which cube is hidden behind a curtain. We are
told that each edge of the cube is between 3 and 5 metres long. We have
no further information to indicate which length is most likely, so
assign uniform probability to each possibility. The mid-point of this
uniform distribution is then :math:`\SI{4}{\meter}`, so we might
conclude that to be the most likely length of each side, giving a cube
with :math:`\SI{16}{\meter^2}` faces, and a volume of
:math:`\SI{64}{\meter^3}`. We are then told that the surface area of
each face is between :math:`\SI{5}{\meter^2}` and
:math:`\SI{25}{\meter^2}`. Making similar assumptions we'd reach the
conclusion that the surface area of each face was
:math:`\SI{15}{\meter^2}`. This is clearly in tension with our estimate
from the edge lengths; clearly the choice of a uniform prior in one set
of variables implies a non-uniform one in another.

It is therefore desirable to work with a prior distribution which will
vary appropriately under a change of variables  [1]_; such a prior is
known as a *Jeffreys Prior*. A *Jeffreys Prior* which will be invariant
under reparameterisation of parameters :math:`\vec{\theta}` can be
determined from the Fisher information, :math:`I`:

.. raw:: latex

   \begin{equation}
   \label{eq:probability:jeffreys}
   p(\vec{\theta}) = \sqrt{\det{I(\vec{\theta})}}
   \end{equation}

Feature spaces and Kernels
==========================

A feature map is a projection from a lower-dimensional data space to a
higher-dimensional one, which can be represented by a mapping,
:math:`\phi`.

.. raw:: html

   <div class="definition">

For a :math:`D`-dimensional vector :math:`\vec{x}`, a feature map,
:math:`\phi : \mathbb{R}^{D} \to \mathbb{R}^{N}` is a mapping which
projects :math:`\vec{x}` into an :math:`N`-dimensional space, the
*feature space*.

.. raw:: html

   </div>

This can be a valuable technique in statistical regression and
classification, where data may become linearly separable in a higher
dimensional space, or can be described by a simpler function than in the
original data space. An example of such a mapping is
:math:`\phi : \mathbb{R} \to \mathbb{R}^{3}, \quad \phi(x) = (1, x, x^2)^{\transpose}`,
(where :math:`\cdot^{\transpose}` is the transpose operator) which can
be used to implement quadratic regression, as

.. raw:: latex

   \begin{equation}
   \label{eq:quadratic-regression}
   f(\vec{x}) = w_0 + w_{1} \vec{x} + w_{2} \vec{x} = \phi(\vec{x})^{\transpose} \cdot \vec{w}
   \end{equation}

which remains linear (and therefore analytically solvable) provided
:math:`\phi` is independent of :math:`\vec{w}`.

Once data is mapped from the data space into the feature space it is
desirable to have some notion of distance between the features (which we
might interpret as the *similarity* between pairs of data). We define a
function which computes such a quantity as a *kernel*:

.. raw:: html

   <div class="definition">

For all variables :math:`x` and :math:`x'` in the input space,
:math:`\set{X}` of a probability distribution, a mapping
:math:`k:  \set{X} \times \set{X} \to \mathbb{R}` is a kernel function.

.. raw:: html

   </div>

If the kernel function can be written in the form of a dot-product
between two *feature maps*, :math:`\phi: \set{X} \to \set{V}`,

.. math::  k(x, x') = \langle \phi(x), \phi(x') \rangle v, 

 for :math:`\set{V}` some inner product space, then we can perform the
\`\`kernel trick'', allowing us to define the kernel in terms of the
inner products within the data, without resorting to an external
coordinate system.

Structured probability distributions
====================================

A complicated joint probability distribution can often be factorised
into lower-dimensional factor distributions if there are conditional
independences within the model which that distribution describes. For
example,

.. math::

    
   p(a,b,c) = p(a | b , c) p(b, c) = p(a | b, c) p (b | c) p(c).

 We can then represent these factorisations in the form of a directed
graph, with

.. math::  c \to b \to a 

 representing :math:`p(a,b,c)`. In such a graph we use the direction of
an arrow to imply a conditional relationship. When expressed in this
form we can call the probability distribution a belief network, or a
graphical model.

As a concrete (if rather naive) example, consider a situation in which
observations are made continuously over the whole sky with two
detectors. One is sensitive to abbr:gw emission, and the other to gamma
ray emission. An observing program is established to analyse transient
signals detected with one or both of these telescopes, with the belief
that abbr:gw bursts can be produced by either a abbr:bns coalescence, or
a abbr:bbh coalescence.

A simple model is constructed which contains four variables

#. :math:`\Gamma \in \{ 0, 1 \}` which takes the value :math:`1` iff a
   abbr:sgrb is detected,
#. :math:`G \in \{ 0, 1 \}` which takes the value :math:`1` iff a
   abbr:gw burst is detected,
#. :math:`B \in \{ 0, 1 \}` which takes the value :math:`1` iff a
   abbr:bbh coalescence has occurred, and
#. :math:`N \in \{ 0, 1 \}` which takes the value :math:`1` iff a
   abbr:bns coalescence has occurred.

The joint probability distribution of this model is then
:math:`p(\Gamma, G, B, N)`, however we can break this down into a
structured form by applying the definition of conditional probability
(definition ref:def:probability:conditional),

.. raw:: latex

   \begin{subequations}
   \begin{align}
   \label{probability:structured:example:breakdown}
   p ( \Gamma, G, B, N) &= p(\Gamma | G, B, N) p(G, B, N)\\
                        &= p(\Gamma | G, B, N) p(G | B, N) p(B, N) \\
                        &= p(\Gamma | G, B, N) p(G | B, N) p(B | N) p(N)
   \end{align}
   \end{subequations}

We can represent this model as a graph

.. raw:: latex

   \begin{center}
   \begin{tikzpicture}

        \node[obs] (gamma) {$\Gamma$};     
        \node[obs, right = of gamma] (G)     {$G$};

        \node[latent, above = of G] (B) {$B$};
        \node[latent, above = of gamma] (N) {$N$};

        \edge{B} {G};
        \edge{B} {gamma};
        \edge{G} {gamma};
        \edge{N} {G};
        \edge{N} {B};
        \edge{N} {gamma};

   \end{tikzpicture}
   \end{center}

Our observers have access to a number of up to date astrophysical
theories which they can use to further develop the model; these place
*conditional independence* constraints on the model.

-  abbr:bbh coalescences and abbr:bns coalescences are independent (one
   does not cause the other)

This statement implies that :math:`p(B | N) = p(B)`, and
:math:`p(N | B) = p(N)`, which we can represent in the graphical form of
the model by removing the edge connecting :math:`B` and :math:`N`.

.. raw:: latex

   \begin{center}
   \begin{tikzpicture}

        \node[obs] (gamma) {$\Gamma$};     
        \node[obs, right = of gamma] (G)     {$G$};

        \node[latent, above = of G] (B) {$B$};
        \node[latent, above = of gamma] (N) {$N$};

        \edge{B} {G};
        \edge{B} {gamma};
        \edge{G} {gamma};
        \edge{N} {G};
        \edge{N} {gamma};

   \end{tikzpicture}
   \end{center}

-  A abbr:bbh coalescence does not produce any electromagnetic emission
   (and therefore cannot produce a abbr:sgrb)

This statement implies that :math:`p(\Gamma | B) = p(\Gamma)`, which can
be represented in the graphical form of the model by removing the edge
connecting :math:`\Gamma` and :math:`B`.

.. raw:: latex

   \begin{center}
   \begin{tikzpicture}

        \node[obs] (gamma) {$\Gamma$};     
        \node[obs, right = of gamma] (G)     {$G$};

        \node[latent, above = of G] (B) {$B$};
        \node[latent, above = of gamma] (N) {$N$};

        \edge{B} {G};
        \edge{G} {gamma};
        \edge{N} {G};
        \edge{N} {gamma};

   \end{tikzpicture}
   \end{center}

These two constraints considerably simplify the model, and we are now
left with the distribution in the form

.. raw:: latex

   \begin{equation}
   \label{probability:structured:example:final}
   p ( \Gamma, G, B, N) = p(\Gamma | N, G) p(G | N, B) p(B) p(N),
   \end{equation}

which is easily interpreted from the graphical form of the model, but
could have been tedious to derive algebraically.

We can define a belief network more generally as follows.

.. raw:: html

   <div class="definition">

A belief network is a probability distribution of the form

.. raw:: latex

   \begin{equation}
   \label{eq:probability:structured:bn}
    p(x_{1}, \dots, x_{N}) = \prod_{i=1}^{N} p(x_{i} | \mathrm{pa}(x_{i})),
   \end{equation}

where :math:`\mathrm{pa}(x)` represents the parental set of the variable
:math:`x`; that is, the set of all variables in the graph which have a
directed edge ending at :math:`x`, or the set of all variables on which
:math:`x` is directly conditional.

.. raw:: html

   </div>

Equivalence of graphical models
-------------------------------

An important caveat with the use of graphical models is that two
graphically distinct models may be mathematically equivalent. The reason
for this becomes clear when considering the procedure used to factorise
the probability distribution starting at equation
ref:probability:structured:example:breakdown. If we had chosen to
re-arrange the variables such that the joint distribution was
:math:`p(N,B,G, \Gamma)` we would have been left with a factorised
distribution in which the arrows of the graph pointed in opposite
directions, yet this is clearly still the same probability distribution,
since probabilities are commutative. To overcome this problem we need to
have a definition of equivalence in the graph. A suitable definition is
that of *Markov equivalence* cite:barberBRML2012:

.. raw:: html

   <div class="definition">

Two graphs are Markov equivalent if they both represent the same set of
conditional independence statements.

.. raw:: html

   </div>

Clearly some method to determine this graphically is warranted. To do so
it is helpful to define a (rather judgmentally-named) property:

.. raw:: html

   <div class="definition">

Consider three nodes, :math:`A`, :math:`B`, and :math:`C` in a abbr:dag.
If :math:`C` is a child of both :math:`A` and :math:`B`, but :math:`A`
and :math:`B` are not directly connected, then the configuration
:math:`A \rightarrow C \leftarrow B` is denoted an immorality.

.. raw:: html

   </div>

In order to determine Markov equivalence we remove all of the
directionality from the edges of the graph, producing the skeleton
graph. Two graphs are Markov equivalent if they share the same skeleton,
and if they share the same set of immoralities.

Inference
=========

In section ref:sec:probability:structured I introduced a probabilistic
model which consisted of the joint probability of all of the model
parameters. Taking the example of joint abbr:gw and gamma ray
observations, if we know the probability that at any given time there
will be a abbr:bns event, we can infer the probability that a abbr:sgrb
and a abbr:gw burst will occur. A model of this form is often considered
a "forward model", in that it predicts the probability of an observable,
and calculation through the graph follows the arrows. While such forward
models are of considerable utility when attempting to make predictions
about unknown variables, often with pre-existing data, they are unable
to answer a question such as "given that I have seen a abbr:gw, but no
abbr:sgrb, what is the probability that I have observed a abbr:bbh
event?". In order to answer such a question we must traverse the
graphical model *backwards*, against the direction of the arrows. This
process is known as *inference*.

In order to produce the *reverse model* we can turn to Bayes Theorem
(theorem ref:the:probability:bayes-theorem). This allows us to derive an
expression for :math:`p(B = 1 | G = 1, \Gamma = 0)`, that is, the
probability that we observe a abbr:bbh given that we've observed a
abbr:gw but no abbr:sgrb.

.. raw:: latex

   \begin{align}
     \label{eq:probability:inference:bayes-example}
     p(B &= 1 | G = 1, \Gamma = 0) = \frac {p(B=1,G=1,\Gamma=0)}{p(G=1, \Gamma=0)} \\
                      &= \frac{\int_{N} p(B=1,G=1,\Gamma=0, N)}{ \int_{B,N} p(G=1, \Gamma=0, B, N)} \\
                      &= \frac{\int_{N} p(\Gamma=0 | G=1, B=1, N) p(G =1 | B=1, N) p(B=1 | N) p(N)} 
                          {\int_{B,N} p(\Gamma=0 | G=1, B, N) p(G =1 | B, N) p(B | N) p(N)}      \\
                      &= \frac{\int_{N} p(\Gamma=0 | G=1, B=1, N) p(G =1 | B=1, N) p(B=1 | N) p(N)}
                          {\int_{B,N} p(\Gamma=0 | G=1, B, N) p(G =1 | B, N) p(N)}
   \end{align}

the probability :math:`p(B = 1 | G = 1, \Gamma = 0)` is called the
*posterior probability of $B$*.

Inference which is based on Bayes Theorem, is a method of statistical
inference which is well-suited to situations where a body of evidence
grows over time, with new results updating previous understanding of
some phenomenon, and as such is well suited to the analysis of
experimental data. It is well suited to the analysis of abbr:gw data,
where measurements are frequently made at different sensitivities during
different observing runs.

If we have some hypothesis, some parameters of the hypothesis, :math:`I`
(also called hyperparameters), and some experimental data, we can
determine the probability of the hypothesis via

.. raw:: latex

   \begin{equation}
       \label{eq:probability:inference:bayes-theorem-hypothesis}
       p(\text{hypothesis} | \text{data}, I) \propto p( \text{data} | \text{hypothesis}) \times p(\text{hypothesis}, I)
   \end{equation}

where :math:`p(\text{data} | \text{hypothesis})` represents the
likelihood; the probability that a given datum would be observed given
the hypothesis, and :math:`p(\text{hypothesis}|I)` represents the
*prior* probability, which represents the understanding of the
probability of the hypothesis before the experiment was conducted.
:math:`p(\text{hypothesis} | \text{data}, I)` is the *posterior*
probability of the hypothesis cite:Sivia2006.

Bayesian inference can then be used as a powerful method for *model
selection*, where the posterior probabilities of two competing models
are compared, with a greater posterior probability indicating greater
support for a given model.

Stochastic processes
====================

A stochastic process is some collection of random variables which can be
indexed by a set, the *index set*. When a stochastic process is used to
describe a physical system the indexing set is often taken to be time
(represented as either a real or natural number), for example for
Brownian motion. Each random variable takes values from its own sample
space, :math:`\Omega`. Since each random variable will have a different
value each time the process is evaluated, the value of the process as a
whole, across all indices, will be different each time. An individual
draw from such a process is a *realisation*, or a sample function.

A stochastic process is represented as the set
:math:`\setbuilder{X(t) | t \in \mathsf{T}}` for :math:`X(t)` the random
variable drawn indexed by the value :math:`t` from the index set
:math:`T`.

A simple example of a stochastic process is the **Bernoulli process**,
in which each random variable is the result of a Bernoulli test, for
example, flipping a (potentially biased) coin. In such a process each
:math:`X(t) \in \{0,1\}`, and :math:`P(X(t) = 1) = p`, with :math:`p`
taking the same value for all :math:`t`. Because each Bernoulli trial is
independent, and all of the trials are equally distributed, the process
is abbr:iid.

The **Poisson process** extends the concept of a Bernoulli process to
the continuous case. Where the Bernoulli process models a discrete state
of a system at some given index, the Poisson process models the number
of times the system has taken that state in the interval between two
indices.

A **Markov process** can be either a discrete or continuous stochastic
process where the probability of moving to the next state depends only
on the current state of the process, and none of the previous ones.
These processes are of considerable importance in Bayesian statistics
thanks to their use in various sampling algorithms.

Approximate inference methods
=============================

In many problems the posterior probability distribution which we need to
evaluate will not be analytical. As a result identifying regions of the
distribution where the probabilities are large (therefore the areas of
interest within the distribution) is likely to require evaluating the
function over its entire parameter space, which may be large. This
problem is further complicated if the distribution is multi-modal, or
contains narrow peaks which may be difficult to find. Further, the
evidence term for the posterior is not normally known. The combination
of these issues for many distributions makes drawing samples from an
arbitrary posterior probability distribution difficult.

For inference, we have two problems which must be solved: how to
generate independent samples from a given probability distribution, and
how to estimate the expectation of functions under the distribution.

If we are able to solve the first problem the second can be estimated by
using :math:`R` random samples,
:math:`\setbuilder{\vec{x}_r | r \in 1, \dots, R}`, drawn from the
distribution, giving an estimator for the expectation,
:math:`\hat{\expect}(\phi)` for the function :math:`\phi`,

.. raw:: latex

   \begin{equation}
   \label{eq:probability:mcmc:expectation}
   \hat{\expect}(\phi) = \frac{1}{R} \sum_{r} \phi(\vec{x}_r)
   \end{equation}

Given that evaluating a continuous system at every location in its state
space is not possible we need a means of producing samples from the
distribution which are representative of the distribution. A
straight-forward approach is to uniformly sample the state space (one
strategy to do this would be to devise a grid and take samples at each
grid point), however such an approach will work only for the simplest
distributions (see chapters 4 and 29 of cite:2003itil.book.....M for a
detailed information theoretic discussion on this).

If sampling from the distribution is difficult, but evaluating it at a
specific location in its parameter space is possible, a number of
sampling methods are possible. The simplest of these, *importance
sampling*, and *rejection sampling* rely on sampling from a tractable
distribution, such as a Gaussian distribution, and then correcting the
samples in some way based on the evaluation of the target distribution.

.. raw:: latex

   \begin{figure}

   % Gauss function, parameters mu and sigma
   \centering
   \begin{tikzpicture}
       \begin{scope}%[xshift=1cm,]
       \begin{axis}[every axis plot post/.append style={
         mark=none,domain=-5:9,samples=50,smooth},
       clip=false,
       %xscale=0.3,
       %yscale=0.2,
       axis y line=none,
       axis x line=bottom,
       ymin=0,
       xtick=\empty,
       ]
       \addplot[thick]{0.5*\complicated};
       \addplot[dashed] {2*\gauss{1.5}{2}};
       
       \node (x1) [text badly centered] at (axis cs:9.5,0) {$x$};
       \end{axis}
       \end{scope}

   \end{tikzpicture}
   \caption[Cartoon of importance sampling]{In importance sampling the arbitrarily complicated distribution, $P^*(x)$ [depicted as a solid line], is not directly sampled, but instead a simpler distribution, $Q^*(x)$ [depicted as a dashed line], such as a normal distribution, is sampled. 
   In regions where $Q^*(x) > P^*(x)$ the samples will \emph{over-represent} $P^*(x)$, and vice versa in regions where $Q^*(x) < P^*$.
   As a result the relative \emph{importance} of each sample needs to be taken into account, by weighting each sample.
   }
   \label{fig:probability:importance-sampling}
   \end{figure}

With *importance sampling*, rather than sampling from the complicated
distribution, :math:`P`, (the *target distribution*), we instead sample
from a distribution, :math:`Q`, which we do know how to sample from,
such as a normal or a uniform distribution (see figure
ref:fig:probability:importance-sampling for a cartoon illustrating this
arrangement). Since we do not necessarily know the normalisation of
:math:`P` or :math:`Q` we can instead sample and evaluate within a
scalar multiple, :math:`Z`, such that :math:`ZP^*(x) = P(x)`. We then
draw the samples :math:`\setbuilder{\vec{x}_r | r \in 1, \dots, R}` from
:math:`Q`, and evaluate :math:`Q(x)` and :math:`P(x)` for each sample.
In regions where :math:`Q(x)` is greater than :math:`P(x)` the samples
will over-represent :math:`P(x)` (and vice versa when :math:`Q(x)` is
smaller than :math:`P(x)`). To account for this each sample is
re-weighted to adjust its importance by the ratio

.. math::  w_r = \frac{P^*(x_r)}{Q^*(x_r)} 

 so then equation ref:eq:probability:mcmc:expectation becomes

.. math::  \hat{\expect}(\phi) = \frac{ \sum_r w_r \phi(x_r) }{\sum_r w_r} 

While importance sampling is an improvement over uniform sampling, it
will fail to converge in situations where the target distribution
contains many separated peaks, and will struggle to explore a
high-dimensional space efficiently.

*Rejection sampling* uses a similar principle to importance sampling,
using a *proposal distribution*, :math:`Q(x)`, which can be sampled
directly, to generate the samples (see figure
ref:fig:probability:rejection-sampling for an illustration of how
:math:`P` and :math:`Q` relate). The method assumes we know the value of
a constant, :math:`c` such that :math:`cQ^*(x) > P^*(x) \forall x`.

.. raw:: latex

   \begin{figure}
   \providecommand\gauss[2]{1/(#2*sqrt(2*pi))*exp(-((x-#1)^2)/(2*#2^2))} 
   \providecommand\complicated{ 0.5*( 1/(.2*sqrt(2*pi))*exp(-((x-1)^2)/(.2*2^2))) +  0.5*(1/(.5*sqrt(2*pi))*exp(-((x-5)^2)/(.5*2^2)) ) } 
   \centering
   \begin{tikzpicture}
       \begin{scope}%[xshift=1cm,]
       \begin{axis}[every axis plot post/.append style={
         mark=none,domain=-5:9,samples=50,smooth},
       clip=false,
       %xscale=0.3,
       %yscale=0.2,
       axis y line=none,
       axis x line=bottom,
       ymin=0,
       xtick=\empty,
       ]
       \addplot[thick]{0.5*\complicated};
       \addplot[dashed] {5*\gauss{2.5}{3}};
       
       \node (x1) [text badly centered] at (axis cs:9.5,0) {$x$};
       \end{axis}
       \end{scope}

   \end{tikzpicture}
   \caption[Cartoon of rejection sampling]{Similarly to importance sampling, in rejection sampling the arbitrarily complicated distribution, $P^*(x)$ [depicted as a solid line], is not directly sampled, but instead a simpler distribution, the proposal distribution, $Q^*(x)$ [depicted as a dashed line], such as a normal distribution, is sampled. In contrast to importance sampling a constraint is placed on $Q^*(x)$ such that for a constant $c$ $cQ^*(x) > P(x) \forall x$. 
   }
   \label{fig:probability:rejection-sampling}
   \end{figure}

This method requires two random numbers to be generated: a sample
:math:`x` is drawn from :math:`Q(x)`, and :math:`cQ(x)` is calculated.
Then a variable :math:`u` is drawn from the uniform distribution
:math:`U(0, cQ^*(x))`. If :math:`u > P^*(x)` --- that is, it lies in the
region between :math:`P^*(x)` and :math:`Q^*(x)`---it is rejected, and
discarded. Otherwise, it is accepted, and kept. This method ensures that
only points which lie within :math:`P^*(x)` are retained, preventing
over-representation, and also that the density of samples is
proportional to :math:`P^*(x)` thanks to the uniform distribution of
samples under :math:`P^*(x)`.

Rejection sampling is fundamentally similar to *Buffon's Needle
Problem*, in which needles dropped on floorboards can be used to
estimate the value of :math:`\pi`, and can be used to evaluate complex
integrals outwith probability problems.

Rejection sampling will struggle to converge if the target and proposal
distributions are not similar, as the region :math:`[P^*(x), Q^*(x)]`
between the two functions will be large, so the probability of
generating samples with :math:`u<P^*(x)` will be small. The method is
also impractical in more than one-dimension, as similarly, the
probability of generating a point within the volume described by
:math:`P^*(x)` will diminish with growing dimensionality.

The deficiencies of these two methods lead to the development of a more
sophisticated approach: abbr:mcmc.

Markov-Chain Monte Carlo
------------------------

As noted previously, rejection sampling struggles to efficiently sample
a distribution if the proposal and target distributions are not similar.
In order to address this failing, the *Metropolis-Hastings* algorithm
constructs a proposal distribution which depends on the sampling
location (or more precisely, the current *state* of the sampler). This
proposal distribution will often be something simple, like a Normal
distribution centred on the current :math:`x_t` being considered.

As with rejection sampling, a tentative state, :math:`x'` is drawn from
a proposal distribution, :math:`Q^*(x', x_t)`, given the current state,
:math:`x_t`. The ratio

.. raw:: latex

   \begin{equation}
   \label{eq:probability:metropolis:acceptance}
   a = \frac{P^*(x')}{P*(x_t)} \frac{Q^*(x_t, x')}{Q^*(x', x_t)}
   \end{equation}

is evaluated. If :math:`a \geq 1` the new state is accepted; otherwise
the new state is accepted with a probability :math:`a`. If the new state
is accepted it becomes the current state (i.e. :math:`x_{t+1} = x'`); if
it is rejected the current state is retained, so :math:`x_{t+1} = x_t`.

In the case that a symmetrical proposal distribution is chosen, such as
a normal distribution, the second ratio in equation
ref:eq:probability:metropolis:acceptance will always be equal to
:math:`1`, providing a simpler expression for :math:`a`, which will be
consequently faster to evaluate. The behaviour of the
Metropolis-Hastings algorithm produces a stochastic process with the
Markov property.

In order to improve the computational efficiency of an abbr:mcmc
algorithm the gradient information of the problem can be taken into
account, which will guide the process to the regions of high
probability. These methods, known as *Hamiltonian* MCMC methods can
allow faster convergence, and therefore reduce the number of
computations required to perform Bayesian inference. The No-U-Turns
sampler cite:2011arXiv1111.4246H is an example of such a method which
includes various algorithmic refinements to allow the sampler to work
efficiently in hierarchical models (see section
ref:sec:probability:hierarchical) without requiring manual tuning.

Hierarchical modelling
======================

Structured probability distributions, as introduced in section
ref:sec:probability:structured have the useful property that the
posterior distribution can be constructed as the product of a set of
independent probability distributions. This structure is frequently
useful when describing physical systems, where, for example, we wish to
infer the properties of an underlying physical system from a set of
individual observations.

An example of such a hierarchical model, used to determine the mean jet
opening angle (beaming angle) of abpl:sgrb is presented in chapter
:raw-latex:`\ref{cha:gamma-ray-burst}` and in Williams *et al.*
cite:dwsgrbbayesianconstraint, in which a hierarchical approach is taken
to determining the probability distribution of the beaming angle via the
rates at which observations of abpl:sgrb and abbr:bns events are
observed. These are themselves determined from observed quantities, such
as the number of observed events, the time over which detections were
made, and the false alarm rate of the detection process. A model such as
this, which has two layers of inference, is comparatively easy to
extend; the inferred beaming angle could, for example, be used as part
of the inference of the generating phenomenon.

Hierarchical models are gaining popularity in other areas of abbr:gw
research, principally black hole population inference
cite:2017MNRAS.471.2801S,2012PhRvD..86l4032A.

.. [1]
   It is worth noting that in probability and statistics this property
   is known as *invariance*, but in other areas of mathematics and
   physics is more likely to be called *covariance*, for example in
   general relativity.
