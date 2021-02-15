Surrogate modelling
===================

Many experimental scenarios in science and engineering are expensive,
laborious, or both to perform, and therefore difficult or off-putting to
repeat. The ability to perform such an experiment with a specific set of
parameters may however be valuable.

While in engineering the difficulties of performing repeatative
experiments may relate to the nature of the experiment (which might, for
example, be destructive to a tested material), in astrophysics we are
more frequently hampered by the computational expense of running a
numerical simulation.

A number of techniques exist to perform interpolation between
experimentally measured data. If a well-defined physical theory is known
to explain the observations an appropriate function can be derived to
make predictions outwith the sampled parameter space for the experiment,
and this can be calibrated (fitted) to the data.

Surrogate models are often desirable in situations where little physical
intuition is available (or where the underlying physics is extremely
complicated). These attempt to model the observed data with limited
assumptions about the form of the generating function. This approach, of
making limited assumptions regarding the structure of the underlying
model often results in these techniques being considered a sub-division
of the nebulous field of *machine learning*.

Polynomial response surfaces
    Perhaps the most straight-forward means of producing a surrogate
    model is to assume that the generating process for measured data can
    be approximated by a polynomial function. In the case of many
    complex physical processes there may be a number of coefficients,
    leading to a polynomial (hyper-)surface. This method, formally
    introduced in 1951 cite:box1951, is often referred to in the
    literature as the abbr:rsm, and is suitable for approximating
    generating models which have smooth variation, and non-oscillatory
    behaviour.

Abbr:svr
    extend support vector machine classification to handle regression
    problems cite:drucker1996. This approach affords greater flexibility
    than polynomial model, as kernel methods can be used to perform
    non-linear fitting, projecting the data into a feature space.

Abbr:gp regression
    which will be the focus of this chapter, is a technique which
    possesses similarities to abbr:svr, in that it makes use of kernel
    functions to project the data into a feature space, however abbr:gpr
    is a fundamentally Bayesian regression model, and as such provides
    not only a regressor to data, but also a measure of the fit's
    uncertainty.

Artificial neural networks
    Neural network techniques, including the use of convolutional neural
    networks, and deep learning techniques, are capable of producing
    non-linear fits to data. See cite:Yeh19981797 for an example of this
    technique used as a surrogate model, in this case to evaluate the
    strength of various concrete mixes.

Gaussian Processes
==================

Consider a regression problem with a set of data

.. math::  \set{D} = \setbuilder{(\vec{x}_i, y_i), i \in 1, \dots, n} 

 which is composed of :math:`n` pairs of inputs, :math:`\vec{x}_i`,
which are vectors which describe the location of the datum in parameter
space, which are the inputs for the problem, and :math:`y_i`, the
outputs. The outputs may be noisy; in this work I will only consider
situations where the noise is additive and Gaussian, so

.. raw:: latex

   \begin{equation}
   \label{eq:gp:additive-noise}
    y_i(\vec{x}_i) = f(\vec{x}_i) + \epsilon_i, \quad \text{for} \quad \epsilon_i \sim \mathcal{N}(0, \sigma^2)
   \end{equation}

where :math:`\sigma` is the standard deviation of the data noise, and
:math:`f` is the (latent) generating function of the data.

This regression problem can be addressed using *Gaussian processes*:

.. raw:: html

   <div class="definition">

A gls:gaussian-process (GP) is a collection of random variables, any
finite number of which have a joint Gaussian distribution
cite:gpr.book.rw.

.. raw:: html

   </div>

Where it is more conventional to consider a prior over a set of, for
example, real values, such as a normal distribution, the Gaussian
process forms a prior over the functions, :math:`f`, from equation
ref:eq:gp:additive-noise, which might form the regression fit to any
observed data. This assumes that the values of the function :math:`f`
behave as

.. raw:: latex

   \begin{equation}
   \label{eq:gp:function-values}
   p(\vec{f} | \vec{x}_1, \vec{x}_2, \dots, \vec{x}_n) = \mathcal{N}(0, \mat{K})
   \end{equation}

where :math:`\mat{K}` is the covariance matrix of :math:`\vec{x_1}` and
:math:`\vec{x_2}`, which can be calculated with reference to some
*covariance function*, :math:`k`, such that
:math:`K_{ij} = k(\vec{x}_i, \vec{x}_j)`. Note that I have assumed that
the abbr:gp is a *zero-mean* process; this assumption is frequent within
the literature. While this prior is initially untrained it still
contains information about our preconceptions of the data through the
form of the covariance function. For example, whether or not we expect
the fit to be smooth, or periodic. Covariance functions will be
discussed in greater detail in section ref:sec:gp:covariance.

By providing training data we can use Bayes theorem to update the
Gaussian process, in the same way that the posterior distribution is
updated by the addition of new data in a standard Bayesian context, and
a posterior on the set of all possible functions to fit the data is
produced. Thus, for a vector of test values of the generating function
:math:`\vec{f}_\star`, the joint posterior
:math:`p(\vec{f}, \vec{f}_* | \vec{y})`, given the observed outputs
:math:`\vec{y}` can be found by updating the abbr:gp prior on the
training and test function values :math:`p(\vec{f}, \vec{f}_*)` with the
likelihood :math:`p(\vec{y}|\vec{f})`:

.. raw:: latex

   \begin{equation}
   \label{eq:gp:bayes}
   p(\vec{f}, \vec{f}_* | \vec{y}) = \frac{p(\vec{f}, \vec{f}_*) p(\vec{y}|\vec{f})}{p(\vec{y})}.
   \end{equation}

Finally the (latent) training-set function values, :math:`\vec{f}` can
be marginalised out:

.. raw:: latex

   \begin{equation}
   p(\vec{f}_* | \vec{y}) = \int p(\vec{f}, \vec{f}_* | \vec{y}) \dd{\vec{f}} = \frac{1}{p(\vec{y})} \int p(\vec{y} | \vec{f}) p(\vec{f}, \vec{f}_*) \dd{\vec{f}}
   \end{equation}

We can take the mean of this posterior in the place of the \`\`best fit
line'' which other techniques produce, and then use the variance to
produce an estimate of the uncertainty of the prediction.

Both the prior :math:`p(\vec{f}, \vec{f}_*)` and the likelihood
:math:`p(\vec{y}|\vec{f})` are Gaussian:

.. raw:: latex

   \begin{equation}
   \label{eq:gp:prior-and-likelihood}
   p(\vec{f}, \vec{f}_*) = \mathcal{N}(\vec{0}, \mat{K}^+), \quad \text{and} \quad 
   p(\vec{y}|\vec{f}) = \mathcal{N}(\vec{f}, \sigma^2 \mat{I})
   \end{equation}

with

.. raw:: latex

   \begin{equation}
     \label{eq:blockK-plus-mat}
     \mat{K}^+ =
     \begin{bmatrix}
       \mat{K}_{\vec{f},\vec{f}} & \mat{K}_{\vec{f},\vec{f}_*} \\ \mat{K}_{\vec{f}_*,\vec{f}} & \mat{K}_{\vec{f}_*, \vec{f}_*}
     \end{bmatrix},
   \end{equation}

and :math:`\mat{I}` the identity matrix, and :math:`\sigma` is the
standard deviation of additive noise in the data.

This leaves the form of the marginalised posterior being analytical:

.. raw:: latex

   \begin{equation}
   \label{eq:gp:posterior}
   p(\vec{f}_* | \vec{y}) = \mathcal{N} (\vec{\mu}, \mat{\Sigma})
   \end{equation}

for

.. raw:: latex

   \begin{equation}
   \label{eq:gp:posterior-mean}
   \vec{\mu} = \mat{K}_{\vec{f}_*,\vec{f}} (\mat{K}_{\vec{f},\vec{f}} + \sigma^2 \mat{I})^{-1} \vec{y},
   \end{equation}

and

.. raw:: latex

   \begin{equation}
   \mat{\Sigma} = \mat{K}_{\vec{f}_*, \vec{f}_*} - \mat{K}_{\vec{f},\vec{f}_*}( \mat{K}_{\vec{f},\vec{f}}+\sigma^2 \mat{I})^{-1} \mat{K}_{\vec{f},\vec{f}_*}).
   \end{equation}

.. raw:: latex

   \begin{figure}
   \includegraphics{figures/gp/gp-training-data.pdf}
   \includegraphics{figures/gp/gp-example-prior-draws.pdf}
   \includegraphics{figures/gp/gp-example-posterior-draws.pdf}
   \includegraphics{figures/gp/gp-posterior-meancovar.pdf}
   \caption[A Gaussian process, step-by-step]{The conditioning of a Gaussian process, starting with data with additive Guassian noise generated from a sine function (grey line) [top row], and a Gaussian process prior [second row].
   Individual draws from the posterior distribution of the Gaussian process are shown in the third row, and the mean draw from the posterior is shown as the heavy red line in the bottom row, with the function which generated the data overlayed in grey, and the $1$, $2$, and $3$-sigma confidence regions plotted as shaded areas around the mean draw.
   \label{fig:gp:steps}}
   \end{figure}

Figure ref:fig:gp:steps shows visually how a one-dimensional regressor
can be created using an abbr:gp method, starting from a abbr:gp prior
and (noisy) data. The first step, depicted on the first row, is an
example of raw training data (containing additive Gaussian noise) which
is suitable for training a Gaussian process. In this example the input
data (:math:`x`-axis) are 1-dimensional, although abpl:gp are also
capable of handling multi-dimensional data. Here the generating function
is plotted as a grey line. Then we choose a covariance function for the
abbr:gp, in this case an exponential-quadratic covariance function
(covariance functions are discussed in detail in section
ref:sec:gp:covariance). The Gaussian process containing no data forms
our prior probability distribution. In the second row of figure
ref:fig:gp:steps 10 draws from the prior distribution are plotted. The
process of \`\`training'' the abbr:gp is discussed in detail in section
ref:sec:gp:training. A prior distribution is placed over the
:math:`\sigma` parameter (see equation ref:eq:gp:prior-and-likelihood),
and the abbr:gp is trained to find the most probable value for the
:math:`\sigma` parameter and the hyperparameters of the covariance
function. For this example the prior placed on :math:`\sigma` is
:math:`\mathcal{N}(0.5, 0.2)`, and the priors on the hyperparameters are
flat. The trained Gaussian process can then be sampled multiple times to
produce multiple different potential fitting functions. In the third row
of figure ref:fig:gp:steps 10 draws from the abbr:gp posterior are
displayed. We can also take the mean and the covariance of the abbr:gp,
and produce a single \`\`best-fit'' with confidence intervals, which is
depicted in the fourth row of figure ref:fig:gp:steps. Where, again, the
original generating function for the data is shown as a grey line. The
mean function produced by the abbr:gp manages to reproduce a function
which oscillates in a way similar to the generating sine function,
however the presence of a considerable amount of noise in the data,
which is accounted for through the :math:`\sigma` term in the abbr:gp,
prevents the function from being recovered completely faithfully.

The mean and variance of this posterior distribution can be used to form
a regressor for the data, :math:`\set{D}`, with the mean taking the role
of a \`\`line-of-best-fit'' in conventional regression techniques, while
the variance describes the goodness of that fit.

A graphical model of a abbr:gp is shown in figure
ref:fig:gp:chain-diagram which illustrates an important property of the
abpl:gp model: the addition (or removal) of any input point to the
abbr:gp does not change the distribution of the other variables. This
property allows outputs to be generated at arbitrary locations
throughout the parameter space.

.. raw:: latex

   \begin{figure}
   \begin{center}
   \begin{tikzpicture}

        \node[obs] (x1) {$\vec{x}_{1}$};       
        \node[latent, above = of x1] (f1) {$f_{1}$};
        \node[obs, above = of f1] (y1) {$y_{1}$};
        \edge{x1}{f1};
        \edge{f1}{y1};

        \node[obs, right = of x1] (x2) {$\vec{x}_{2}$};        
        \node[latent, above = of x2] (f2) {$f_{2}$};
        \node[obs, above = of f2] (y2) {$y_{2}$};
        \edge{x2}{f2};
        \edge{f2}{y2};

        \node[obs, right = of x2] (xstar) {$\vec{x}_{\star}$};     
        \node[latent, above = of xstar] (fstar) {$f_{\star}$};
        \node[latent, above = of fstar] (ystar) {$y_{\star}$};
        \edge{xstar}{fstar};
        \edge{fstar}{ystar};

        \node[obs, right = 2 of xstar] (xN) {$\vec{x}_{N}$};       
        \node[latent, above = of xN] (fN) {$f_{N}$};
        \node[obs, above = of fN] (yN) {$y_{N}$};
        \edge{xN}{fN};
        \edge{fN}{yN};

        \draw [black, line width=0.1cm] (f1) -- (f2) -- (fstar);
        \draw [black, dashed, line width=0.1cm] (fstar) -- (fN);
   \end{tikzpicture}
   \end{center}
   \caption[A graphical model of a Gaussian process]{A graphical model of a Gaussian process, represented as a chain graph. The inputs (on the bottom row) are all observed quantities, while outputs are observed only at the location of training points. The latent variables, $f$ from the Gaussian field (the heavy black line connecting these nodes indicates that they are fully connected) connect the two, and so any given observation is independent of all other nodes given its connected latent $f$ variable. Thus the marginalisation (removal) or addition of input nodes to the abbr:gp does not change the distribution of the other variables.
   \label{fig:gp:chain-diagram}}
   \end{figure}

Covariance Functions
====================

The covariance function defines the similarity of a pair of data points,
according to some relationship with suitable properties. The similarity
of input data is assumed to be related to the similarity of the output,
and therefore the more similar two inputs are the more likely their
outputs are to be similar.

As such, the form of the covariance function represents prior knowledge
about the data, and can encode understanding of effects such as
periodicity within the data.

.. raw:: html

   <div class="definition">

Given two points, :math:`\vec{x}` and :math:`\vec{x}'` in a parameter
space, a stationary covariance function is a function
:math:`f(\vec{x} - \vec{x}')`, and which is thus invariant to
translations in the input space.

.. raw:: html

   </div>

That is, the function depends on the separation of the points, and not
their position.

.. raw:: html

   <div class="definition">

Given two points, :math:`\vec{x}` and :math:`\vec{x}'` in a parameter
space, if a covariance function is a function of the form
:math:`f(|\vec{x} - \vec{x}'|)` then it is isotropic, and invariant
under all rigid motions.

.. raw:: html

   </div>

Thus such a covariance function depends only on the separation between
the points, and not the direction between them.

A covariance function which is both stationary and isotropic has the
property that it can be expressed as a function of a single variable,
:math:`r = | \vec{x} - \vec{x}' |` is known as a abbr:rbf. Functions of
the form :math:`k : (\vec{x}, \vec{x}') \to \mathbb{C}`, for two vectors
:math:`\vec{x}, \vec{x}' \in \mathcal{X}` are often known as *kernels*,
and I will frequently refer interchangably to covariance functions and
kernels where the covariance function has this form.

For a set of points :math:`\setbuilder{ \vec{x}_{i} | i = 1, \dots, n }`
a kernel, :math:`k` can be used to construct the gram matrix,
:math:`K_{i,j} = k(x_{i}, x_{j})`. If the kernel is also a covariance
function then :math:`K` is known as a *covariance matrix*.

For a kernel to be a valid covariance function for a abbr:gp it must
produce a positive semidefinite covariance matrix :math:`\mat{K}`. Such
a matrix, :math:`\mat{K} \in \mathbb{R}^{n \times n}` must satisfy
:math:`\vec{x}^{\transpose} \mat{K} \vec{x} \geq 0` for all
:math:`\vec{x} \in \mathbb{R}^{n}`.

Example covariance functions
----------------------------

One of the most frequently encountered covariance functions in the
literature is the abbr:se covariance functions cite:gpr.book.rw. Perhaps
as a result of its near-ubiquity this kernel is known under a number of
similar, but confusing names (which are often inaccurate). These include
the *exponential quadratic*, *quadratic exponential*, *squared
exponential*, and even *Gaussian* covariance function.

The reason for this is its form, which closely resembles that of the
Gaussian function:

.. raw:: latex

   \begin{equation}
      \label{eq:gp:kernels:se}
     k_{\mathrm{SE}}(r) = \exp \left( - \frac{r^2}{2 l^2} \right),
   \end{equation}

for :math:`r` the Euclidean distance of a datum from the centre of the
parameter space, and :math:`l` is a scale factor associated with the
axis along which the data are defined.

.. raw:: latex

   \begin{figure}
   \includegraphics{figures/gp/covariance-se-overview.pdf}
   \caption[The squared exponential covariance function]{The \textbf{squared exponential} covariance function (defined in equation~\ref{eq:gp:kernels:se}). The panel on the left depicts the value of the kernel as a function of $r = (|\vec{x} - \vec{x}'|)$, at a number of different length scales ($l = 0.25, 0.5, 1.0$) while the panel on the right contains draws from Gaussian processes using gls:se covariance with the same length scales as the left panel.
   \label{fig:gp:covariance:overviews:se}}
   \end{figure}

The abbr:se function imposes strong smoothness constraints on the model,
as it is infinitely differentiable. This covariance function is
therefore well-suited to modelling data which is generated by smooth
processes without discontinuities.

The scale factor, :math:`l` in equation ref:eq:gp:kernels:se, also known
as its *scale-length* defines the size of the effect within the process.
This characteristic length-scale can be understood
cite:adler1976,gpr.book.rw in terms of the number of times the abbr:gp
should cross some given level (for example, zero). Indeed, for a abbr:gp
with a covariance function :math:`k` which has well-defined first and
second derivatives the expected number of times, :math:`N_{u}` the
process will cross a value :math:`u` is cite:gpr.book.rw

.. raw:: latex

   \begin{equation}
   \label{eq:gp:kernels:crossings}
   \mathbb{E}(N_{u}) = \frac{1}{2 \pi} \sqrt{ - \frac{ k''(0) }{k(0)} } \exp \left( - \frac{u²}{2k(0)} \right)
   \end{equation}

A zero-mean abbr:gp which has an abbr:se covariance structure will then
cross zero :math:`1/(2 \pi l)` times on average.

Examples of the abbr:se covariance function, and of draws from a
Gaussian process prior which uses this covariance function are plotted
in figure ref:fig:gp:covariance:overviews:se for a variety of different
scale lengths.

.. raw:: latex

   \begin{figure}
   \includegraphics{figures/gp/covariance-ex-overview.pdf}
   \caption[The exponential covariance function]{The \textbf{exponential} covariance function (defined in equation~\ref{eq:gp:kernels:exp}). The panel on the left depicts the value of the kernel as a function of $r = (|\vec{x} - \vec{x}'|)$, at a number of different length scales ($l = 0.25, 0.5, 1.0$) while the panels on the right contain draws from Gaussian processes using an exponential covariance with the same length scales as the left panel.
   \label{fig:gp:covariance:overviews:ex}}
   \end{figure}

For data which is not generated by a smooth function a suitable
covariance function may be the exponential covariance function,
:math:`k_{\mathrm{EX}}`, which is defined

.. raw:: latex

   \begin{equation}
   \label{eq:gp:kernels:exp}
   k_{\mathrm{EX}} = \exp\left( - \frac{r}{l} \right),
   \end{equation}

where :math:`r` is the pairwise distance between data and :math:`l` is a
length scale, as in equation ref:eq:gp:kernels:se.

In contrast to the abbr:se covariance function, the exponential
covariance function's value drops-off rapidly near zero (as can be seen
in the left panel of figure ref:fig:gp:covariance:overviews:ex),
allowing it to model rapid variation over short scales, making it suited
to modelling data generated by non-smooth functions.

Examples of the exponential covariance function, and of draws from a
Gaussian process prior which uses this covariance function are plotted
in figure ref:fig:gp:covariance:overviews:ex for a variety of different
scale lengths. The behaviour of this kernel is strongly affected by the
covariance function's rapid drop-off close to zero; compared to the
other examples of covariance function in this section.

For data generated by functions which are smooth, but not necessarily
infinitely differentiable, as in the case of the abbr:se covariance
function, we may turn to the Matérn family of covariance functions,
which take the form

.. raw:: latex

   \begin{equation}
   \label{eq:gp:kernels:mat}
   k_{\mathrm{Mat}}(r) = \frac{1}{2^{\nu - 1} \Gamma{\nu}} 
   \left( \frac{\sqrt{2 \nu}}{l} \right)^{\nu} K_{\nu} 
   \left( \frac{\sqrt{2 \nu}}{l} r \right),
   \end{equation}

for :math:`K_{\nu}` the modified Bessel function of the second kind, and
:math:`\Gamma` the gamma function. As with the previous two covariance
functions :math:`l` is a scale length parameter, and :math:`r` the
distance between two data. A abbr:gp which has a Matérn covariance
function will be :math:`(\lceil x \rceil - 1)`-times differentiable.

While determining an appropriate value of :math:`\nu` during the
training of the abbr:gp is possible, it is common to select a value *a
priori* for this quantity. :math:`\nu=3/2` and :math:`\nu=5/2` are
common choices as :math:`K_{\nu}` can be determined simply, and the
covariance functions are analytic.

The case with :math:`\nu=3/2`, commonly referred to as a
Matérn-\ :math:`3/2` kernel, then becomes

.. raw:: latex

   \begin{equation}
   k_{\mathrm{M32}}(r) = \left(1+\frac{\sqrt{3}d}{l}\right) \exp\left( - \frac{\sqrt{3}d}{l} \right).
   \end{equation}

Examples of this covariance function, and example draws from a abbr:gp
using it as a covariance function are plotted in figure
ref:fig:gp:kernels:m32.

Similarly, the Matérn-\ :math:`5/2` is the case where :math:`\nu = 5/2`,
taking the form

.. raw:: latex

   \begin{equation}
   k_{\mathrm{M52}}(r) = 
   \left( 1+\frac{\sqrt{5}d}{l} + \frac{5d^2}{3l^2} \right) 
   \exp \left( - \frac{\sqrt{5}d}{l} \right).
   \end{equation}

Again, examples of this covariance function, and example draws from a
abbr:gp using it as a covariance function are plotted in figure
ref:fig:gp:kernels:m52.

.. raw:: latex

   \begin{figure}
   \includegraphics{figures/gp/covariance-mat32-overview.pdf}
   \caption[The Matérn-$3/2$ covariance function]{The \textbf{Matérn-$3/2$} covariance function (defined in equation~\ref{eq:gp:kernels:mat}, with $\nu = 3/2$). The panel on the left depicts the value of the kernel as a function of $r = (|\vec{x} - \vec{x}'|)$, at a number of different length scales ($l = 0.25, 0.5, 1.0$) while the panels on the right contain draws from Gaussian processes using a Matérn-$3/2$ covariance with the same length scales as the left panel.
   \label{fig:gp:kernels:m32}}
   \end{figure}

.. raw:: latex

   \begin{figure}
   \includegraphics{figures/gp/covariance-mat52-overview.pdf}
   \caption[The Matérn-$5/2$ covariance function]{The \textbf{Mat\'{e}rn-$5/2$} covariance function (defined in equation~\ref{eq:gp:kernels:mat}, with $\nu=5/2$). The panel on the left depicts the value of the kernel as a function of $r = (|\vec{x} - \vec{x}'|)$, at a number of different length scales ($l = 0.25, 0.5, 1.0$) while the panels on the right contain draws from Gaussian processes using Mat\'{e}rn-$5/2$ covariance functions with the same length scales as the left panel.
   \label{fig:gp:kernels:m52}}
   \end{figure}

Data may also be generated from functions with variation on multiple
scales. One approach to modelling such data is to use a abbr:gp with
**rational quadratic** covariance. This covariance function represents a
scale mixture of abbr:rbf covariance functions, each with a different
characteristic length scale. The rational quadratic covariance function
is defined as

.. raw:: latex

   \begin{equation}
   \label{eq:gp:kernels:rq}
   k_{\mathrm{RQ}}(r)  =\left( 1 + \frac{r^2}{2 \alpha l^2} \right)^{-\alpha},
   \end{equation}

where :math:`\alpha` is a parameter which controls the weighting of
small-scale compared to large-scale variations, and :math:`l` and
:math:`r` are the overall length scale of the covariance and the
distance between two data respectively. Examples of this function, at a
variety of different length scales and :math:`\alpha` values, and draws
from abpl:gp which use these functions are plotted in figure
ref:fig:gp:kernels:rq.

.. raw:: latex

   \begin{figure}
   \includegraphics{figures/gp/covariance-rq-overview.pdf}
   \caption[The rational quadratic covariance function]{The \textbf{rational quadratic} covariance function (defined in equation~\ref{eq:gp:kernels:rq}). The panel on the left depicts the value of the kernel as a function of $r = (|\vec{x} - \vec{x}'|)$, at a number of different length scales ($l = 0.25, 0.5, 1.0$) while the panel on the right contains draws from Gaussian processes using rational quadratic covariance with the same length scales as the left panel.
   \label{fig:gp:kernels:rq}}
   \end{figure}

This summary of potential covariance functions for use with a abbr:gp is
far from complete (see cite:gpr.book.rw for a more detailed list).
However, these four can be used or combined to produce highly flexible
regression models, as they can be added and multiplied as normal
functions.

Kernel algebra
--------------

It is possible to define new kernels from the standard set through a
series of defined operations.

Consider two covariance functions, :math:`f_1` and :math:`f_2`, then

.. raw:: html

   <div class="definition">

If :math:`f_{1}` and :math:`f_{2}` are both kernels, then
:math:`f = f_{1} + f_{2}` is also a kernel.

.. raw:: html

   </div>

.. raw:: html

   <div class="definition">

If :math:`f_{1}` and :math:`f_{2}` are both kernels, then
:math:`f = f_{1} \times f_{2}` is also a kernel.

.. raw:: html

   </div>

We can think of the sum of two kernels as representing the possibility
that the data be described by one component kernel or another. As such
addition represents the logical OR operation. Similarly the product of
two kernels represents the logical AND operation between the two.

We can use these two operations to form an arbitrarily complicated
kernel structure, and to allow inference to be conducted over multiple
dimensions. Different kernels can be used to model different aspects of
the variation within the input data. For example, the training data may
be known to be periodic in one dimension, or to have white noise
properties in another. Here I adopt the convention from
cite:duvenaud.thesis.2014 and omit the hyperparameters from the
description of the kernel. I also extend the notation to allow kernels
with multiple input dimensions to be described, with superscript indices
indicating the dimensions of the training data which the kernel applies
to.

As a concrete example, for a kernel function in which the zeroth
dimension is described by a abbr:se kernel, but the first, second, and
third dimensions are described by a rational quadratic kernel the kernel
could be described as

.. raw:: latex

   \begin{equation}
   \label{eq:example-kernel-notation}
   k = \SE^{(0)} \times \RQ^{(1,2,3)}
   \end{equation}

A list of the symbols for each covariance function is given in table
ref:tab:gp:kernels, and definitions of the kernels are given at the end
of the chapter.

.. raw:: latex

   \begin{table}
   \centering
   \begin{tabular}{lcl}
   \toprule
   Kernel & Symbol & Properties \\
   \midrule
    Exponential-quadratic & $\SE$    & $C^\infty$-smooth local variation.             \\
    Matérn-3/2          & $\kernel{M32}$   & $C^3$-smooth local-variation               \\
    Matérn-5/2          & $\kernel{M52}$   & $C^5$-smooth local-variation.                                    \\
    Periodic            & $\Per$   & Smooth global periodic variation.   \\
    Linear              & $\Lin$   & Global continuous linear variation. \\
    Rational Quadratic  & $\RQ$    & Variation on multiple scales.       \\
    Constant            & $\Con$   & Scaling factor.                     \\
   \bottomrule
   \end{tabular}
   \caption[Frequently used kernels]{Frequently used and encountered kernels used as covariance functions for abbr:gpr problems. The second column contains the abbreviation by which these kernels are referred in this work, and the third column lists properties of each function which affect its utility in a variety of problems.
   \label{tab:gp:kernels}
   }
   \end{table}

For example, we may be able to model a yearly growing trend which
contains a seasonal variation with a combination of a linear and a
periodic kernel, :math:`\Lin \times \SE`.

Training the model
==================

When defining the covariance function for a abbr:gp it may be desirable
to specify a number of free hyperparameters, :math:`\theta`, which allow
the properties of the GP to be altered. Since the functional form of the
covariance function defines the abbr:gp model, this allows the
techniques of Bayesian model selection to be employed, in order to
select the specific abbr:gp model which optimally describes the data.
The log-probability that a given set of strain values were drawn from a
Gaussian process with zero mean and a covariance matrix
:math:`\mat{K} = K_{ij} = k(x, x'; \theta)` is

.. raw:: latex

   \begin{equation}
   \label{eq:logevidencegp}
     \log p(\vec{f} | x) = - \frac{1}{2} \mat{K}^{-1} \vec{f} - \frac{1}{2} \log |\mat{K}| - \frac{n}{2} \log 2\pi.
   \end{equation}

This quantity is normally denoted the *log-evidence* or the
*log-hyperlikelihood*. The model which best describes the training data
may then be found by maximising the log-hyperlikelihood with respect to
the hyperparameters, :math:`\theta` of the covariance function,
:math:`k(x, x'; \theta)`.

This optimisation may be conducted using either a hill-climbing based
optimisation algorithm, or in a hierarchical Bayesian framework, with
prior probability distributions assigned to each hyperparameter, and the
optimal hyperparameters then found using an abbr:mcmc algorithm.

Dealing with computational complexity and large data sets
=========================================================

One severe disadvantage of Gaussian Processes as a data analysis tool
are their high computational complexity. Producing a prediction from a
GP requires inverting the covariance matrix; matrix inversion is an
:math:`\mathcal{O}(N^3)` process in time, and scales with
:math:`\mathcal{O}(N^2)` in memory use. This effectively limits the
number of training points which can be input to a GP to fewer than
:math:`10^4`.

A number of approaches have been developed in the literature to address
this short-coming by utilising computationally tractable approximations
to either the matrix inversion or the Gaussian process. These approaches
can be grouped into three broad categories; sparse Gaussian processes,
which use a modified covariance function to force the covariance matrix
to have a near-diagonal structure; hierarchical approaches, which do not
modify the covariance function, but approximate the off-diagonal terms'
influence on the inversion; and local expert approaches, in which the
parameter space is divided into many sub-spaces, and each sub-space is
modelled using an independent abbr:gp.

Sparse Gaussian processes
-------------------------

Sparse abbr:gpr approaches work by modifying the form of the joint prior
distribution from equation ref:eq:gp:prior-and-likelihood to include an
additional :math:`m` latent variables,

.. math::  \vec{u} = [u_1, \dots, u_m]^{\transpose}, 

 which are termed \`\`inducing variables''. These correspond to values
of the Gaussian process at inputs :math:`X_{\vec{u}}`, which are the
inducing inputs. These inducing variables can be chosen in various
different ways, but their effect on the abbr:gp is the same.

The original abbr:gp can be recovered by marginalising over
:math:`\vec{u}`:

.. raw:: latex

   \begin{equation}
   \label{eq:gp:marginal-inducing}
   p(\vec{f}_*, \vec{f}) = \int p(\vec{f}_*, \vec{f}, \vec{u}) \dd{\vec{u}} = \int p(\vec{f}_*, \vec{f} | \vec{u}) p(\vec{u}) \dd{\vec{u}}
   \end{equation}

with
:math:`p(\vec{u}) = \mathcal{N}(\vec{0}, \mat{K}_{\vec{u},\vec{u}})`.

Sparse abbr:gp approaches make the assumption that :math:`\vec{f}` and
:math:`\vec{f_*}` are conditionally independent given :math:`\vec{u}`.
This is depicted as a graphical model in figure
ref:fig:gp:chain-diagram-sparse.

.. raw:: latex

   \begin{figure}
   \begin{center}
   \begin{tikzpicture}

        \node[obs] (x1) {$\vec{x}_{1}$};       
        \node[latent, above = of x1] (f1) {$f_{1}$};
        \edge{x1}{f1};

        \node[obs, right = of x1] (x2) {$\vec{x}_{2}$};        
        \node[latent, above = of x2] (f2) {$f_{2}$};
        \edge{x2}{f2};

        \node[obs, right = 2 of x2] (xN) {$\vec{x}_{N}$};      
        \node[latent, above = of xN] (fN) {$f_{N}$};
        \edge{xN}{fN};

        \node[latent, above = of f2] (u) {$\vec{u}$};

        \node[obs, right = 2 of xN] (xstar) {$\vec{x}_{\star}$};       
        \node[latent, above = of xstar] (fstar) {$f_{\star}$};
        \edge{xstar}{fstar};

        \draw [black, line width=0.1cm] (f1) -- (f2);
        \draw [black, dashed, line width=0.1cm] (f2) -- (fN);
        \edge{fN}{u};   \edge{f1}{u};   \edge{f2}{u};
        \edge{u}{fstar};
   \end{tikzpicture}
   \end{center}
   \caption[A graphical model of a sparse Gaussian process]{A graphical model of a sparse Gaussian process, represented as a chain graph. The inputs (on the bottom row) are all observed quantities. For the sake of clarity the outputs have been omitted from this diagram. The latent variables, $f$ from the Gaussian field (the heavy black line connecting these nodes indicates that they are fully connected) connect the two, and so any given observation is independent of all other nodes given it connected latent $f$ variable. 
   In contrast to the fully-connected situation depicted in \ref{fig:gp:chain-diagram}, the values of the Gaussian process for the training data are taken to be conditionally independent from the values for test inputs.
   \label{fig:gp:chain-diagram-sparse}}
   \end{figure}

| This allows the construction of two conditional posterior probability
  distributions, for the training data and the test inputs
  cite:sparsegp.unifying: \\begin{subequations}
| *training*:

.. raw:: latex

   \begin{equation}
   p(\vec{f}|\vec{u}) = \mathcal{N}(\mat{K}_{\vec{f},\vec{u}} \mat{K}^{-1}_{\vec{u},\vec{u}} \vec{u},
                                    \mat{K}_{\vec{f},\vec{f}} - Q_{\vec{f},\vec{f}})
   \end{equation}

*test (predictive)*:

.. raw:: latex

   \begin{equation}
   p(\vec{f_*}|\vec{u}) = \mathcal{N}(\mat{K}_{\vec{f}_*,\vec{u}} \mat{K}^{-1}_{\vec{u},\vec{u}} \vec{u},
                                    \mat{K}_{\vec{f}_*,\vec{f}_*} - Q_{\vec{f}_*,\vec{f}_*})
   \end{equation}

\\end{subequations} letting
:math:`Q_{\vec{a},\vec{b}} = \mat{K}_{\vec{a},\vec{u}} \mat{K}_{\vec{u},\vec{u}}^{-1} \mat{K}_{\vec{u},\vec{b}}`.

There are a number of approaches to choosing the inducing points, and
further simplifying assumptions which can be applied to the sparse
abbr:gp approach which are discussed in depth in cite:sparsegp.unifying.
Thanks to the smaller matrix which must be inverted for the predictive
case, formed only from the inducing points, this sparse approach is
capable of handling much larger quantities of data than the direct,
exact approach.

Hierarchical matrix solvers
---------------------------

An alternative approach to introducing an inducing set is to take
advantage of the structure of the covariance matrix, :math:`\mat{K}`,
which is produced by a number of covariance functions. Covariance
functions will typically assign a small covariance to points which are
distantly spaced in the data space; as a result, if the covariance
matrix is suitably sorted, it is possible to conside the whole
covariance matrix as a block matrix. Hierarchical solving methods such
as cite:2014arXiv1405.0223A,2019JOSS....4.1167A produce an arrangement
of low-rank matrices as off-diagonal components in the block matrix. The
on-diagonal sub-matrices are still treated as full rank matrices, and
are solved using conventional methods, while the inverses of the
off-diagonal components are found using a Chebyshev polynomial
interpolation and :math:`LU`-decomposition. This allows for inversion of
the matrix in :math:`\mathcal{O}(n \log^2 n)` rather than
:math:`\mathcal{O}(n^3)` time. This technique has been successfully
applied to abpl:gp in the ``George`` library cite:hodlr.

Gaussian process local experts
------------------------------

Local expert approaches attempt to improve the computational performance
of GPs by diving the parameter space of the model into multiple
sub-spaces. In a conventional GP the training data

is used in its entirity to train a single GP. If these data were instead
divided into :math:`M` subsets, of size :math:`K`, we can train
:math:`M` separate GPs, which will each provide an independent
prediction for any given point in the parameter space. The network
structure which is established by this subdivision of the parameter
space is known as a *gating network*.

Early approaches to using local experts in GPs used kd-trees
cite:shen2005fast to sub-divide the parameter space, and then modelled
each subspace with its own GP. The GPs were trained together, with each
having the same kernel hyper-parameters. Final predictions were then
produced as a weighted sum of the individual GPs' predictions. While
this approach was somewhat effective, it enforced a stationary structure
on the covariance matrix, and the paper does not treat the combination
of the prediction uncertainties.

Approaches which follow the work of cite:Jacobs:1991:AML:1351011.1351018
on mixtures of local experts have had some more promise, allowing each
GP to have its own set of hyper-parameters, allowing greater freedom in
modelling heteroskedastic and non-stationary data.

Deciding on the number of sub-models is a non-trivial problem; one
approach is to model the parameter space using an abbr:imm
cite:rasmussen2002infinite, in which the gating network is effectively a
Dirichlet process over the training data. The predictions from each
sub-model are then summed to find the global prediction. While this
approach offers greater flexibility for modelling more complex
underlying functions, it does little to improve the speed of GP
predictions. Additional abbr:imm approaches are proposed by
cite:meeds2006alternative, and a comparable, variational approach is
taken by cite:yuan2009variational.

All of these approaches have the difficulty of requiring the gating
network to assign a weight (often called a *responsibility* to each
sub-model's prediction when calculating the global prediction, adding an
additional layer of inference, which normally requires an MCMC sampler
to perform. *Product-of-experts* models avoid this complication by
multiplying the sub-model predictions, but these models have either
turned out to be excessively confident cite:2014arXiv1412.3078N, or
excessively conservative cite:2014arXiv1410.7827C.

These problems have lead to the development of the Bayesian Committee
Machine (BCM) cite:tresp2000bayesian, which assigns a weight to each
sub-model's prediction which is equal to the inverse of the prediction's
covariance, in order that sub-models which better observe the predicted
region are given a greater weight in the global prediction. This
approach can suffer as a result of models which contains week experts,
and so the *robust Bayesian Committee Machine*
cite:deisenroth2015distributed has been proposed to provide a more
robust framework for Gaussian process regression with many experts. This
approach also allows for the computation of the model's prediction to be
highly-parallelised, with the potential for each sub-model being
evaluated on separate compute nodes, and combined together by another
process running on another node.

Stochastic Variational Inference
--------------------------------

The abbr:svi algorithm is designed to allow inference to be carried out
in situations where very large quantities of data are available.

Variational inference, whereby a posterior distribution over some set of
latent variables :math:`\set{Z}`, given data :math:`\set{D}` is
approximated with a *variational distribution*:

.. raw:: latex

   \begin{equation}
   \label{eq:gp:svi:variational-posterior}
   P(\set{Z}|\set{D}) \approx Q(\set{Z}) 
   \end{equation}

where the distribution :math:`Q(\set{Z})` is restricted to be simpler
than the form of the exact posterior. The similarity between :math:`Q`
and :math:`P` can be measured with the Kullback-Liebler divergence (see
definition ref:def:probability:kl); as such, finding a suitable
approximation of the posterior distribution becomes a standard
optimisation problem, in which the KL divergence must be minimised.

Stochastic optimisation is designed to find the maximum of an objective
function by following noisy estimates of the function's gradient; these
gradients must be unbiased. Variational inference has the attractive
property that the objective function can be decomposed into additive
terms, with one term for each datum in :math:`\set{D}`. Noisy estimates
of the gradient can be obtained by taking a subsample of :math:`\set{D}`
and using it to compute a scaled gradient on that subsample. If sampled
independently the gradient of the noisy gradient will be equal to the
true gradient cite:2012arXiv1206.7051H.

This combination of stochastic optimisation and variational inference is
suitable for models which have a set of global variables which factorise
the observable and latent variables of the model, however, the graphical
model of a abbr:gp, as depicted in ref:fig:gp:chain-diagram makes it
clear that these models do not possess such a structure. However,
*sparse* abbr:gp models do possess a structure with global variables,
thanks to the existence of the set of inducing points. The structure of
these models, depicted in figure ref:fig:gp:chain-diagram-sparse is
close to the requirement for abbr:svi, as the global variables factorise
the observable variables.

For a abbr:gp model to use abbr:svi a variational distribution is
introduced over the inducing variables: :math:`q(\vec{u})`. This
distribution is Gaussian, and can be parameterised as
:math:`q(\vec{u}) = \mathcal{N}(\vec{u} | \vec{m}, \vec{S})`. A lower
bound can be set on the distribution (see equation 4 of
cite:2013arXiv1309.6835H) by Jensen's inequality. This lower bound can
be expressed as a sum of terms which correspond to single pairs
:math:`(\vec{x}, y)` from the training set, which allows stochastic
optimisation to be carried-out.

The use of a posterior approximated by variational inference in this way
allows for much larger datasets to be used in the conditioning of the
abbr:gp than other methods, since only a subset (or \`\`minibatch'' of
the training data must be used in any given training iteration).

Assessing Gaussian process regression models
============================================

Having produced a statistical regression model it is crucial that its
efficacy is assessed. There are broadly two scenarios under which such
testing can occur. In situations where a large amount of data is
available to condition the model it is often appropriate to partition
the data into a \`\`training set'' and a \`\`test set''; the latter is
held-aside, and not used to condition the model, and can then be used
after the model is trained to compare against the model predictions.

Alternatively scenarios may arise where there is insufficient data to
form such a test set without adversely affecting the model's predictive
power. Examples of such a scenario include timeseries modelling, where
the predictions of the model may represent future (an therefore
inaccessible) observations, or computational experiments, where the
acquisition of training data is sufficiently costly that producing a
test set is not viable.

In the case where test data is available two straight-forward metrics
are available: the root-mean-squared error, and the correlation.

Let :math:`\vec{x}_*` and :math:`\vec{y}_*` be respectively the test
inputs and test outputs from the test set, then let
:math:`\hat{\vec{y}}` be the set of model predictions drawn from the
Gaussian Process with inputs :math:`\vec{x}_*`.

The abbr:rmse gives an estimate of the total deviation between the mean
prediction of the model and the true value from the test data:

.. raw:: latex

   \begin{equation}
   \label{eq:gp:testing:rmse}
   \mathrm{RMSE} = \sqrt{
       \frac{
         \sum_{i=0}^{n_i} (y_*^{(i)} - \hat{y}^{(i)})^2
       }
       { n_t },
     }
   \end{equation}

for :math:`n_t` the size of the test set. While the abbr:rmse can
represent a good metric for conventional regression methods, it does not
consider the estimate of the variance which is provided by Gaussian
process models; as such it is an insufficient measure on its own of
these models.

It is possible to use the abbr:gp variance to form a metric of the
efficacy by considering the correlation between the test data and the
prediction

.. raw:: latex

   \begin{equation}
   \label{eq:gp:correlation}
       \rho^2 = \left(
         \frac{ \cov(y^*, \hat{y})} { \sqrt{ \vary(y) \vary(\hat{y}) } } 
       \right)^2
   \end{equation}

These two metrics, together, allow the model to be assessed either
during the training of the model (or indeed, they can be used as
training metrics if using a cross validation approach while determining
the model hyperparameters) given a judicious partitioning of the
available data.

Forrester cite:forrester2008engineering suggests that a
:math:`\rho^2 \geq 0.8` provides a surrogate model with good global
predictive abilities, which corresponds to an abbr:rmse of around
:math:`0.1`.

In situations where test data is not available such straightforward
tests are often impractical. In the case of timeseries forecasting it
may be possible to assess the forecast by forming a test set from the
most recent observations, and comparing these to the output of the
model, however, if only a small number of past observations are
available the predictive capability of the model may be sufficiently
poor to render this test almost meaningless.

In situations where more data is available it may be possible to assess
a abbr:gpr model using *leave-one-out* cross validation, in which a
single point is omitted from the training set, and used as test data.
The testing can then be repeated multiple times, leaving different
points from the sample in order to form a comprehensive test statistic.

Estimating contours: an example GPR problem
===========================================

While figure ref:fig:gp:steps showed the process of constructing a
abbr:gp regressor for data generated from a single-dimensional function,
in this section I demonstrate how a higher-dimensional problem can be
treated with abbr:gp regression. For the sake of clarity I have chosen a
two-dimensional function; anything with more dimensions is likely to be
hard to represent on paper, and the same concepts can be extended to
higher-dimensional models.

In figure ref:fig:gp:examples:mountainspoints a number of spot-heights
are plotted for hills in the *Arrochar Alps*, a region of the Scottish
Highlands around 50-kilometres north of the City of Glasgow. Each point
corresponds to the summit of a hill (derived from the *Database of
British and Irish Hills* cite:hilldb). In order to interpolate a
\`\`landscape'' based on these measurements I trained a abbr:gp with a
rational quadratic kernel on the latitude and the longitude. The
:math:`\alpha` parameter of the kernel was set to be the same in both
dimensions, and a :math:`\Gamma`-function prior was placed on it with
shape parameters :math:`(\alpha_\Gamma = 5, \beta_\Gamma = 0.5)`. A
normal distribution prior was placed on the lengthscale of each
dimension, each with :math:`(\mu=0.012, \sigma=1)`. It is worth noting
that applying a constraint on a abbr:gp is difficult, and as such,
despite providing the peak heights in the landscape, the abbr:gp is free
to interpolate larger height values throughout the landscape. Finally,
the covariance function was multiplied by a constant kernel scaling
factor (:math:`\Con`), the amplitude of which was drawn from a normal
distribution prior with parameters :math:`(\mu = 1, \sigma=1)`.

The abbr:gp was implemented using the ``PyMC3`` python library
cite:Salvatier2016.

.. raw:: latex

   \begin{figure}
   \includegraphics{figures/gp/arrochar-heights.pdf}
   \caption[Summit heights in the Arrochar Alps]{The location of summits within the \emph{Arrochar Alps}, an uplands region of Western Scotland. These will be used as the training data for a abbr:gp regression model designed to emulate the landscape.
   \label{fig:gp:examples:mountainspoints}}
   \end{figure}

In order to determine the appropriate hyperparameter values the
log-evidence was maximised using a Newtonian optimiser, in order to
determine the abbr:map estimate of the hyperparameters. The resulting
abbr:map estimate of the mean landscape is shown in figure
ref:fig:gp:examples:mountains1. A number of *irregularities* can be
spotted with a map produced using this technique, rather than a more
standard method. The first is the absence of a flat region of land
occupied by a large reservoir between *Ben Vane*
:math:`(56.249786^{\circ},-4.781639^{\circ})` and *Ben Vorlich*
:math:`(56.274021^\circ,-4.755046^\circ)`; as the map is informed only
by summits this surrogate model for the landscape is bound to struggle
to find low points like this in the landscape. The second is the very
smooth nature of the landscape, for example the near-conical shape of
*Beinn Ìme* :math:`(56.236812^\circ,-4.817142^\circ)`; this is a result
of the choice of a smooth kernel (the :math:`\RQ` kernel). The behaviour
of the abbr:gp far from any of the training data is mostly obscured in
this figure thanks to the clipping of the boundary box; the abbr:gp will
eventually revert to the mean of the abbr:gp prior (which was chosen to
be zero in this example); this behaviour can be seen to some extent in
the upper-left corner of the plot.

In figure ref:fig:gp:examples:mountains2 I show the same landscape
created using abpl:gp with a variety of covariance functions which show
how drastically this choice affects the model.

.. raw:: latex

   \begin{figure}
   \makebox[\textwidth][c]{\includegraphics{figures/gp/arrochar-alps.pdf}}
   \caption[A ``landscape'' created by GPR for the Arrochar Alps]{The mean abbr:gp output for a abbr:gp trained with summit heights in the Arrochar Alps, an upland area north of Glasgow, Scotland. Here the smoothness conditions placed on the abbr:gp by the form of the covariance function become clear with a number of the peaks being lost as a result. In this example a rational-quadratic covariance function was used.
   \label{fig:gp:examples:mountains1}
   }
   \end{figure}

Four different covariance functions are shown; constructed from the
rational quadratic (:math:`\RQ`), Matérn-5/2 (:math:`\kernel{M52}`),
exponential quadratic (:math:`\SE`), and the exponential kernels
respectively. The variance of the predictions from each abbr:gp are
shown in figure ref:fig:gp:examples:mountainsvar.

.. raw:: latex

   \begin{figure}
   \includegraphics{figures/gp/arrochar-kernels.pdf}
   \caption[GPR-derived landscapes for the Arrochar Alps using a selection of covariance functions]{The \gls{gp} derived mean landscape, with a variety of different covariance functions used to produce the interpolated topology. 
   The upper-left panel is generated from a \gls{gp} with a rational quadratic kernel (this is a repeat of figure~\ref{fig:gp:examples:mountains1}); then the upper right is generated using a Matérn-5/2 kernel, lower left an exponential quadratic kernel, and lower right an exponential kernel.
   Each panel also contains the training points marked as black dots.
   \label{fig:gp:examples:mountains2}}
   \end{figure}

.. raw:: latex

   \begin{figure}
   \includegraphics{figures/gp/arrochar-kernels-var.pdf}
   \caption[The variance of GPR-derived landscapes for the Arrochar Alps.]{The variance of the landscapes from figure~\ref{fig:gp:examples:mountains2}, with the uncertainty underlaid as a colourmap, which runs from dark in regions of low variance, generally close to the peaks, where the training data was provided to the \gls{gp}, to light in regions of high variance (and hence high uncertainty).
   \label{fig:gp:examples:mountainsvar}}
   \end{figure}

Each of these predictions show behaviour created by the choice of
covariance function. The rational quadratic covariance function infers a
smooth, rolling landscape between the peaks, but still produces
pronounced peaks. The prediction with this covariance kernel is
confident throughout the area of the plot, as seen from the low variance
in the upper-left panel of figure ref:fig:gp:examples:mountainsvar.

The behaviour of the abpl:gp which use Matérn-5/2 and exponential
quadratic covariance function are broadly comparable, favouring much
steeper slopes than the rational quadratic abbr:gp, and providing
low-confidence predictions in regions outside the training data. This
effect is moderately more pronounced for the abbr:gp using the
exponential quadratic than the Matérn-5/2.

Similarly to the rational quadratic kernel, the abbr:gp using the
exponential kernel produces a landscape with smoothly-varying
large-scale structure, but allows for steeper gradients close to
training points, and produces lower-confidence estimates than the
abbr:gp using the rational quadratic covariance function outside of the
parameter space spanned by the training data.

While this is clearly not a practical method for use in cartography, the
behaviour of the four abpl:gp shown in figures
ref:fig:gp:examples:mountains2 and ref:fig:gp:examples:mountainsvar is
helpful to understand the behaviour of abbr:gp in higher-dimensional
spaces.
