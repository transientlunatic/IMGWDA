Short gamma-ray bursts and compact binary coalescences
======================================================

Glspl:grb are highly energetic astrophysical phenomena which were first
observed by the VELA nuclear proliferation monitoring satellites
cite:1973ApJ...182L..85K, and rapidly corroborated
cite:1975NYASA.262..145S, in the early 1970s. Twenty years of
observations of the events, which occur at around a daily cadence
cite:1995ARA&A..33..415F, with instruments such as abbr:batse on the
abbr:cgro had shown that the distribution of events was isotropic within
the sky, but not homogeneous, muddying the waters when trying to
identify the progenitor to these events cite:1993ApJ...407..126B.
Instead attempts to classify observed abpl:grb are based on their
duration cite:1993ApJ...413L.101K. This division, with events with a
duration in excess of two seconds designated an abbr:lgrb, while those
with a duration shorter than two seconds are designated abpl:sgrb, was
motivated by the bimodality in the distribution of abbr:grb durations.
This distribution, for the abpl:grb included in the gls:fermi catalogue
cite:2014ApJS..211...12G,2014ApJS..211...13V,2016ApJS..223...28N is
plotted in figure ref:fig:grb:distribution. The :math:`T_{90}` measure
represents the interval between when 5% of the fluence has been
detected, and when 95% of the fluence has been detected. By-eye the
distribution appears to have a single peak, with a lengthy tail of
short-duration events, but there is generally confidence that the
distribution in fact best described by a mixture of two Gaussian
distributions cite:2015A&A...581A..29T, which correspond to the short
and long-duration categories. This classification also demonstrates a
bimodality in the distribution of spectral hardness of the events.
abbr:sgrb were found to be harder, and abbr:lgrb softer.

.. raw:: latex

   \begin{figure}
   \includegraphics[width=\textwidth]{figures/grb/fermi-duration-hist.pdf}
   \caption[The $t_{90}$ distribution of gamma ray bursts]{A histogram of the $T_{90}$ duration of each abbr:grb in the gls:fermi abbr:grb catalogue \cite{2014ApJS..211...12G,2014ApJS..211...13V,2016ApJS..223...28N}. 
   \label{fig:grb:distribution}
   }
   \end{figure}

abbr:lgrb have come to be associated with abbr:ccsn. The observation of
SN 1998bw cite:1998Natur.395..670G, which was observed as an optical
transient within the localisation region of GRB 980425. This transient
was shown to be the result of a type Ic supernova. Subsequent numerical
modelling cite:1999ApJ...524..262M of core-collapse supernovae
corroborated the connection of the observed supernova and abbr:lgrb,
although SN 1998bw was unusual, likely through being closer than other
abbr:grb, and possibly with a weaker-than-average energy production,
allowing the optical transient to be observed. The observation of SN
2003dh, alongside a more normal abbr:grb, and subsequent potential
abbr:sn abbr:lgrb associations have added considerably to the evidence
of a connection between abbr:lgrb and abbr:ccsn.

While a connection between abbr:sn and abbr:lgrb seems plausible,
producing the quantity of energy required for an abbr:sgrb through this
mechanism is impractical in abbr:ccsn models. Predictions that an
entirely different mechanism may be responsible for these events were
made as early as 1984 cite:1984SvAL...10..177B: namely a abbr:bns or
abbr:nsbh system. While either of these systems are potentially capable
of producing the quantity of energy required to explain observed
abbr:sgrb, there is no strong evidence to suggest that all of them will;
indeed modelling suggests that a substantial fraction of abbr:nsbh
systems will be incapable of producing the required energy
cite:2014ApJ...791L...7P.

The association between abbr:sgrb and abbr:bns mergers (or at least, a
subset thereof) was cemented by the first observation of a abbr:grb
event, GRB 170817A cite:2017ApJ...848L..14G, which coincided with a
gravitational wave observation: gls:gw170817 cite:2017PhRvL.119p1101A.

Jet production
--------------

At the time of their discovery the properties of abpl:sgrb did not fit
any known astrophysical system. The requirement that the events be
distributed uniformly in the sky, and have a high observed gamma ray
flux emitted over a short period of time made the events difficult to
explain. The sharply-peaked nature of the gamma ray lightcurve implied
that the progenitors must be small (:math:`< \SI{e7}{\meter}`), moving
non-relativistically. A number of early theories included flare stars,
antimatter, and neutron star binaries as progenitors (see
cite:1975NYASA.262..164R for a review of these early theories [1]_). The
favoured theory (especially given the discovery of GRB 170817A,
discussed above) for abpl:sgrb is that they are a result of abbr:bns
merger events, which are expected to produce the required energy to
produce a abbr:grb, provided the emission is beamed.

The determination by abbr:batse that abbr:grb have a cosmological,
rather than Galactic, origin implied that the events must be extremely
luminous (and, indeed, the most electromagnetically luminous events
observed in the Universe). The fireball model cite:1999PhR...314..575P,
explains the production of energy by the abbr:bns through the kinetic
energy of ultra-relativistic particles (or through electromagnetic
Poynting flux) being converted to abbr:em emission in an optically thin
region of material surrounding the merger. This may be a result of
interaction with the ISM, or due to interactions within the outflowing
material from the merger. This model implies that the majority of
emission from the event should be highly beamed, which allows for their
extremely high observed luminosity.

Jet geometry
------------

Taking a simple "top-hat" model  [2]_ for the beam profile, which
assumes that the emission from an abbr:sgrb is concentrated into a
conical beam with a half opening angle :math:`\theta`:

.. raw:: latex

   \begin{equation}
   \label{eq:grb:tophat}
   L(\theta_{\text{v}}) = \begin{cases} L_{\text{uniform}} & \quad \text{if} \quad \theta_{\text{v}} < \theta \\
                                                       0  & \quad \text{otherwise}
                         \end{cases}
   \end{equation}

with :math:`\theta_{\text{v}}` the angle at which the event is viewed,
:math:`L` the luminosity at that angle, and :math:`L_{\text{uniform}}`
the luminosity within the beam.

More complex, *structured jet* models exist, such as the Gaussian beam
model (introduced for abpl:lgrb in cite:2002ApJ...571..876Z). This model
takes the form

.. raw:: latex

   \begin{equation}
   \label{eq:grb:gaussianbeam}
   L(\theta_{\text{v}}) = L_{\text{c}} \exp \left( - \frac{\theta_{\text{v}}^2}{2 \theta_{\text{c}}^2} \right)
   \end{equation}

where :math:`L_\text{c}` is the luminosity of the jet viewed along its
axis, and :math:`\theta_{\text{c}}` is the angle which characterises the
width of the beam.

Clearly, if abbr:sgrb emission is constrained to a jet, the gamma ray
emission will be observed only if the observer is appropriately aligned
with the cone of the jet. Since the progenitor of these events is a
source of gravitational waves (in the form of a abbr:bns event), which
produce near-isotropic emission, it would be reasonable to expect to
make detections of abbr:bns events with abbr:gw detectors without making
coincident gamma ray observations of an associated abbr:sgrb. Knowledge
of the jet structure allows the construction of a *forward model* which
will allow the prediction of the observed rate of abbr:sgrb if the jet
angle distribution and the rate of abbr:bns events are known.

Understanding how this model might work is easiest by considering a
simple game.

#. Make a counter for the number of observed abbr:sgrb events,
   :math:`N_{\text{grb}}`, which is initially set to :math:`0`.
#. Now draw :math:`N_{\text{bns}}` values of the viewing angle from a
   distribution uniform over :math:`\cos(\theta_{\text{v}})`, between
   :math:`\ang{0}` and :math:`\ang{90}`.
#. For each observation draw a value for each of the variables of the
   luminosity distribution and source distance, :math:`D`, from
   appropriate distributions. In the case of the top-hat model this
   would involve drawing the angle from some distribution limited to the
   range :math:`\ang{0}` to :math:`\ang{90}` for example.
#. Determine if the observed luminosity,
   :math:`L(\theta_{\text{v}})/D^2` is greater than some threshold
   luminosity, below which the event cannot be observed. If it is,
   increment the abbr:grb counter, :math:`N_{\text{grb}}`.

.. raw:: latex

   \begin{figure}
   \includegraphics{figures/grb/game-tophat.pdf}
   \caption[Expected observed ratios of abbr:sgrb and abbr:bns events with the top hat model]{The expected ratios of observed abbr:sgrb to abbr:bns events from a variety of on the beaming angle of a top-hat model. Each distribution is a normal distributions truncated between $\ang{0}$ and $\ang{90}$; the $x$ axis represents the standard deviation of the distribution, while each line represents a different mean.
   \label{fig:grb:game:tophat}}
   \end{figure}

Figure ref:fig:grb:game:tophat shows the results of playing this game
while drawing the beaming angle from various normal distributions
truncated between :math:`0^{\circ}` and :math:`90^{\circ}`. This form of
the game is particularly simple; we can assume that all events which
originate within the volume of space which a abbr:gw detector can
observe are sufficiently luminous that we will detect their abbr:sgrb if
viewed along the beam, thus only the jet opening angle affects
detectability.

Given that it is possible to form a forward model for this scenario, it
follows that producing a reverse model, taking advantage of Bayesian
inference, should be possible as well.

Inferring the beaming angle from astrophysical rates
====================================================

In this section I will focus on the production of an inferential model
for the beaming angle in the top-hat jet model. Provided we assume that
all events are sufficiently luminous that we will detect them if we view
them along their beam, the simplicity of this model means we can relate
the rate at which gamma ray events will be detected, :math:`\grbrate`,
to the rate at which non-beamed abbr:gw events will be detected,
:math:`\cbcrate`, through the relation

.. raw:: latex

   \begin{equation}
   \label{eq:grb:rate2angle}
       \grbrate = \epsilon\cbcrate \left \langle 1-\cos \theta \right \rangle,
   \end{equation}

where we introduce an efficiency factor, :math:`\epsilon`, to allow for
some fraction of merger events to produce no gamma ray emission.

An overview of this approach is as follows:

#. Estimate the posterior probability distribution on the abbr:bns
   merger rate in the local universe from a number of observed
   gravitational wave signals and our knowledge of the sensitivity of
   the detectors. We construct a joint posterior distribution on the
   abbr:bns rate and the (unknown) probability :math:`\epsilon` that a
   given merger results in an abbr:sgrb.

#. Use equation ref:eq:grb:rate2angle, which relates the abbr:bns merger
   and abbr:sgrb rates via the geometry of the beaming angle, to
   transform the rate posterior probability to a posterior probability
   on the mean abbr:sgrb beaming angle. In this work I consider the
   observed rate of abpl:sgrb to be constant.

#. Marginalise over :math:`\epsilon`. I choose to consider
   :math:`\epsilon` a nuisance parameter because, to date, there is no
   accurate estimate of this parameter and it is not the main focus of
   our analysis.

In the case that :math:`\epsilon` is very small, and very few abpl:bns
produce a abbr:sgrb, then a much larger number of observations will be
needed to achieve the same confidence in the measurement of
:math:`\theta` than would be required if :math:`\epsilon` was large.

Constructing the abbr:bns rate posterior
----------------------------------------

In order to make any inference about the abbr:sgrb jet angle it is first
necessary to determine the rate of abbr:bns events, :math:`\cbcrate`.
Consequently, an inference step must be included to determine the
probability distribution on this rate, :math:`p(\cbcrate|D, I)`, given
data, :math:`D` on abbr:gw observations, and other prior information,
:math:`I`.

With the detection of gls:gw170817 in 2017 we now have access to an
event upon which to perform inference, however, it is still possible to
determine a plausible :math:`\cbcrate` in the absence of detections.
This was the scenario during the development of this technique, and I
present it here partly to demonstrate its robust nature, and partly to
demonstrate how the method may be useful in other multi-messenger
scenarios which involve beamed emission. I also present the probability
distributions on :math:`\cbcrate` based on the assumptions of observing
time and inspiral range presented in the advanced abbr:ligo *observing
scenarios* document cite:2018LRR....21....3A, which will later be used
to determine the future prospects for placing limits on the jet geometry
of abbr:sgrb events.

This work is not the first attempt to use a comparison of rate to infer
information about beam geometry; previously, a comparison of rates was
used to place a lower limit on the beaming angle in cite:Abbott:2016ymx.

abbr:gw data analysis glspl:search-pipeline designed to detect abbr:cbc
events, for example ``FINDCHIRP`` cite:2012PhRvD..85l2006A, or ``PyCBC``
cite:Canton:2014ena,2016CQGra..33u5004U,alex\ :sub:`nitz20193265452`
identify discrete glspl:trigger which are characterised by network
abbr:snr, :math:`\rho_c`, which, for the case of abbr:bns searches,
indicate the similarity between the detector data and a set of template
abbr:bns coalescence waveforms. The measured rate, :math:`r`, of these
events consists of two components: a population of true abbr:gw signals,
:math:`s`; and a background rate, :math:`b`, due to noise fluctuations
caused by instrumental and environmental disturbances.

.. raw:: latex

   \begin{equation}
   r = s + b
   \begin{cases}
   s = \text{signal rate} \\
   b = \text{background rate}.
   \end{cases}
   \label{eq:grb:signal:composition}
   \end{equation}

Searches for abbr:bns events are generally conducted as part of an
*all-sky* analysis over all of the two-detector coincident data in a
given observing run. For these searches, such as those used in
cite:2016PhRvX...6d1015A,2018arXiv181112907T, the significance of a
gls:trigger is determined empirically, by comparing the signal to noise
sampled close to its time. A detection requires this significance to be
above some predetermined threshold (for example :math:`5\sigma` for
gls:gw150914 and gls:gw151226
cite:2016PhRvL.116f1102A,2016PhRvL.116x1103A). I follow the method in
cite:Aasi:2013wya, which defines a detection as a candidate with an
abbr:snr :math:`\rho_c \geq 12`, corresponding approximately to
:math:`b=\SI{e-2}{\year^{-1}}`. Since the background rate :math:`b` is
defined, only the signal rate, :math:`s`, needs to be inferred. In this
study I do not consider sub-threshold events (i.e. those with
:math:`\rho_{\text{c}} < 12`), and assume that the probability of
abbr:gw detection from abbr:bns events is not dependent upon the
orientation of the source. By not considering sub-threshold events the
total volume of space which is observed is effectively reduced, in
exchange for maintaining a low background rate of false events,
:math:`b`. In reality there is a greater probability of detecting a
face-on abbr:bns event compared to an edge-on abbr:bns event. A face-on
abbr:bns event is more likely to have an observable abbr:sgrb beam,
which may introduce a bias in this method towards broader beam
geometries.

By assuming a uniform prior on :math:`s` and a Poisson process
underlying the events, it may be shown (for example in
cite:2010blda.book.....G) that the posterior for the signal rate, given
a known background rate :math:`b` and :math:`n` events observed over a
time period :math:`T` is

.. raw:: latex

   \begin{equation}
   p(s|n,b,I) = C \frac{ T\left[(s+b)T\right]^n e^{-(s+b)T}}{n!},
   \label{eq:grb:poissonwithbackground}
   \end{equation}

where,

.. raw:: latex

   \begin{eqnarray}
   C^{-1} & = &\frac{e^{-bT}}{n!} \int_0^{\infty}\diff(sT)(s+b)^n T^n e^{-sT}\\
   & = & \sum_{i=0}^n \frac{ (bT)^i e^{-bT}}{i!}.
   \end{eqnarray}

Finally, we can transform the posterior on the *signal* rate to the
underlying *coalescence* rate via our knowledge of the sensitivity of
the abbr:gw analysis. In particular, the signal detection rate is simply
the product of the intrinsic coalescence rate :math:`\cbcrate` and the
number of abbr:bns mergers which would result in a abbr:gw signal with
:math:`\rho_c\geq12`. Expressing the binary coalescence rate in terms of
the number of mergers per gls:mweg, per year then we require the number
of galaxies :math:`N_{\mathrm{G}}` which may be probed by the abbr:gw
analysis. At large distances, this is well approximated by
cite:2018LRR....21....3A:

.. raw:: latex

   \begin{equation}
       N_G = \frac{4}{3} \pi \left( \frac{\dhor}{\mpc} \right)^3 (2.26)^{-3} (0.0116),
       \label{eq:grb:numbermweg}
   \end{equation}

where :math:`\horizonDistance` is the gls:horizon-distance (defined as
the distance at which an optimally-oriented abbr:bns merger yields
:math:`\rho_c\geq12`), the factor of 2.26 results from averaging over
sky-locations and orientations, and
:math:`\SI{1.16e-2}{\mega \parsec^{-3}}` is the extrapolated density of
abbr:mweg in space.

Finally, the posterior on the binary coalescence rate :math:`\cbcrate`
is obtained from a trivial transformation of the posterior on the signal
rate :math:`s`,

.. raw:: latex

   \begin{eqnarray}
       p(\cbcrate|n,T,b,\dhor) & = & p(s|n,T,b) \left|\frac{\diff s}{\diff \cbcrate}\right| \\
                                      & = & N_G(\dhor)p(s|n,T,b).
   \end{eqnarray}

We see that in this approach, the rate posterior depends only on the
number of signal detections :math:`n`, the observation time :math:`T`,
the background rate :math:`b`, and the horizon distance of the search
:math:`\dhor`. It is precisely these quantities that comprise the
detection scenarios outlined in cite:Aasi:2013wya. Before constructing
expected rate posteriors, we outline the transformation from rate to
beaming angle.

The abbr:sgrb rate
------------------

In this work I do not place a prior distribution on the abbr:sgrb rate,
but assume a fiducial rate,
:math:`\grbrate = \SI{10}{\giga\parsec^{-3}\year^{-1}}`. A more
extensive investigation could attempt to account for the uncertainty in
the abbr:sgrb rate by placing an astrophysically motivated prior
distribution over this quantity.

Constructing the beaming angle posterior
----------------------------------------

Inferences of the abbr:sgrb beaming angle are made from the posterior
probability density on the beaming angle :math:`p(\theta|D,I)` where, as
usual, :math:`D` indicates some set of observations and :math:`I`
unenumerated prior knowledge. Our goal is to transform the measured
posterior probability density on the rate :math:`\cbcrate` to a
posterior on the beaming angle.

It is possible to transform the joint distribution
:math:`p(\theta, \epsilon|D,I)` using a Jacobian transformation of the
joint distribution :math:`p(\cbcrate, \epsilon|D,I)`:

.. raw:: latex

   \begin{equation}
   \label{eq:grb:ratejacobian}
   p(\theta,\epsilon) = p(\cbcrate,\epsilon)
   \left\lvert\left\lvert
   \frac{\partial(\cbcrate,\epsilon)}{\partial(\theta,\epsilon)}
   \right\rvert\right\rvert,
   \end{equation}

(NB, for notational simplicity I will omit the :math:`I` term herein).

The Jacobian determinant can be computed from equation
ref:eq:grb:rate2angle. It is then straightforward to marginalize over
the efficiency term, :math:`\epsilon`, in order to yield the posterior
on :math:`\theta` itself:

.. raw:: latex

   \begin{eqnarray}
       \label{eq:grb:jet:posterior}
       p(\theta) & = & \int_{\epsilon} p(\theta,\epsilon) \dd{\epsilon}\\
                 & = & \int_{\epsilon} p(\cbcrate,\epsilon)
       \left\lvert\left\lvert
       \frac{\partial(\cbcrate,\epsilon)}{\partial(\theta,\epsilon)}
       \right\rvert\right\rvert \dd{\epsilon} \\
                 & = & \frac{2\grbrate \sin
   \theta~p(\cbcrate)}{(\cos\theta-1)^2}\int_{\epsilon}
   \frac{p(\epsilon)}{\epsilon} ~\dd{\epsilon},
   \end{eqnarray}

assuming that :math:`\epsilon` and :math:`\cbcrate` are logically
independent such that,

.. raw:: latex

   \begin{equation}
   p(\epsilon,\cbcrate) = p(\epsilon|\cbcrate)p(\cbcrate) = p(\epsilon)p(\cbcrate).
   \end{equation}

It is important to note that the entire procedure of deriving the jet
angle posterior is completely independent of the approach used to derive
the rate posterior. In the preceding section we adopted a
straightforward Bayesian analysis of a Poisson rate which is amenable to
a simple application of plausible future detection scenarios; there is
no inherent requirement to use that method to derive the rate posterior.

Given the posterior on the rate, :math:`p(\cbcrate)`, the final
ingredient in this approach is the specification of some prior
distribution for :math:`\epsilon`. Given the lack of information on the
value and distribution of :math:`\epsilon`, three plausible priors were
selected, and the distributions on the jet opening angle were inferred
under each assumed prior.

The three priors considered are

Delta-function
    :math:`p(\epsilon) = \delta(\epsilon=0.5)`; which represents the
    probability that abbr:bns mergers yield abpl:sgrb is known to be 50%
    exactly.
Uniform
    :math:`p(\epsilon)=U(0,1)`; representing the probability that
    abbr:bns mergers yield abpl:sgrb may lie anywhere
    :math:`\epsilon \in (0,1]` with equal support in that range.
Jeffreys
    :math:`p(\epsilon)=\beta(\frac{1}{2},\frac{1}{2})`; treating the
    outcome of a abbr:bns merger as a Bernoulli trial in which an
    abbr:sgrb constitutes \`success' and :math:`\epsilon` is the
    probability of that success, the least informative prior (see
    ref:sec:probability:priors:uninformative). For the Bernoulli
    distribution, this (Jeffreys) prior is a :math:`\beta`-distribution
    with shape parameters :math:`\alpha=\beta=\frac{1}{2}`.

Prospects for beaming angle constraints with advanced LIGO
==========================================================

In this section I will demonstrate the ability of this technique to
provide constraints on the beaming angle under a number of plausible
observing scenarios for the network of advanced abbr:gw detectors. These
observing scenarios are derived from the scenarios outlined in
cite:2018LRR....21....3A which correspond approximately to both the
first two observing runs, and planned future observing runs of the
network. . An observing scenario essentially consists of an epoch of
advanced abbr:ligo operation, which defines an expected search
sensitivity (that is, the abbr:bns horizon distance, :math:`\dhor`) and
the total observation time :math:`T`; as well as an assumption on the
rate of abbr:bns coalescence in the local universe :math:`\cbcrate`.
Each observing scenario ultimately results in an expectation for the
number of observed abpl:gw from abbr:bns coalescences. For this study,
this \`realistic rate' for :math:`\cbcrate` was taken from the method
described in cite:rates\ :sub:`paper`.

Determining the expected number of observations
-----------------------------------------------

Given the observation time and horizon distance of the observation epoch
we first compute the 4-volume accessible to the analysis,

.. raw:: latex

   \begin{equation}
       \label{eq:grb:searchvolume}
       V_{\mathrm{search}} = \frac{4}{3}\pi \left(\frac{\dhor}{2.26}\right)^3 \times \gamma T,
   \end{equation}

where the factor 2.26 arises from averaging over source sky location and
orientation, :math:`T` is the observation time and :math:`\gamma` is the
*duty cycle* for the science run. Following cite:2018LRR....21....3A, we
take :math:`\gamma=0.5`. For comparison, during the first observing run
of advanced gls:ligo, the two interferometers observed in coincidence
achieving a gls:duty-cycle :math:`\gamma_{\mathrm{coinc}} = 0.41`. Where
there is a range in the horizon distances quoted in
cite:2018LRR....21....3A to account for uncertainty in the sensitivity
of the early configuration of the detectors, the arithmetic mean of the
lower and upper bounds is used when computing the search volume. Table
ref:tab:grb:scenarios lists the details of each observing scenario. The
2015-2016 and 2016-2017 scenarios correspond approximately to the first
two advanced LIGO observing runs. The 2018-2019 scenario corresponds to
the third observing run, however, since the work in this chapter was
prepared, O3 has been extended to a total run-time of 12 months. The
2020+ scenario corresponds to a year of observation with both of the
advanced gls:ligo detectors and gls:virgo at design sensitivity, with
the 2024+ scenario extending this to include a third advanced gls:ligo
detector in India. The increase in the size of the network will lead to
an increase in the network duty cycle, and a corresponding increase in
the total search volume per year.

.. raw:: latex

   \begin{table}
   \centering
   \begin{tabular}{lccccc}
     \toprule
     Epoch &  $T$ & $\inspiralDistance$ & $V_{\text{search}}$ & Est. abbr:bns \\
           &   [yr] & [Mpc] & [$\ee{6} \mpc³\,\yr^{-1}$] & Detections \\
     \midrule
     2015--2016 & 0.25 & 40--80   & 0.05--0.4 & 0.0005--4 \\
     2016--2017 & 0.5 & 80--120 & 0.6--2.0 & 0.006-20\\
     2018--2019 & 0.75 & 120--170 & 3--10 & 0.04--100\\
     2020+      & 1    & 200 & 20 & 0.2--200 \\
     2024+      & 1    & 200 & 40 & 0.4--400 \\
     \bottomrule
   \end{tabular}
   \caption[Advanced detector era observing scenarios]{Advanced detector era observing scenarios considered in this work.  
     $T$ is the expected duration of the science run and $\inspiralDistance$ is the abbr:bns inspiral distance for the sensitivity expected to be achieved at the given epoch, which is equal to $\horizonDistance / 2.26$.
     $V_{\text{search}}$ is the sensitive volume of the search, defined by equation~\ref{eq:grb:searchvolume}; the final column contains the estimated range of the number of abbr:gw detections.
     Note that the quoted search volume accounts for a network duty cycle of $\sim 80\%$ per detector.
     These scenarios are derived from those detailed in~\cite{2018LRR....21....3A}.
     While the 2020+ and 2024+ scenarios appear identical in terms of the sensitivity of the detectors, the 2024+ scenario includes a third advanced LIGO detector in India.
     This expansion of the network is expected to lead to an increase in the network duty cycle, and a corresponding increase in the area of the sky which the network is sensitive to, resulting in a greater volume being searched per year.
     \label{tab:grb:scenarios}}
   \end{table}

Posterior Results
-----------------

Having developed a framework in which to infer first the expected
abbr:bns rate, and from that the distribution of the jet opening angle,
it makes sense to consider how the method is likely to perform as the
sensitivity and observing time of the advanced abbr:ligo detectors
improves.

Figure ref:fig:grb:aligo:cbcrate shows the abbr:bns rate posteriors
resulting from the observations in the scenarios in table
ref:tab:grb:scenarios generated using the procedure described in section
ref:sec:grb:rate2beam. A number of scenarios have a range of potential
inspiral distances, and in each case the median value is used in the
analysis, so for the 2015--2016 scenario :math:`\dinsp` is taken to be
:math:`\SI{60}{\mega\parsec}`, for example. Likewise an illustrative
value of :math:`n`, the number of expected abbr:gw detections, is
selected from each range; these are listed in table
ref:tab:grb:rateposteriors.

These posteriors, together with the prior distributions described in
section ref:sec:grb:rateposterior and the observed rate of abpl:sgrb (as
described in section ref:sec:grb:sgrbs the rate
:math:`\grbrate = \SI{10}{\giga\parsec^{-3} \year^{-1}}`
cite:Nakar:2007yr,Dietz:2010eh) is used to derive the corresponding
beaming angle posteriors.

.. raw:: latex

   \begin{figure}
   \centering
   {\includegraphics[width=\linewidth]{figures/grb/rate_posteriors_violin.pdf}}
   \caption[Posterior probability distributions on BNS rate]{Posterior probability distribution for the rate of abbr:bns coalescence assuming the scenarios in table~\ref{tab:grb:scenarios}.
       The 95\% credible interval is represented with a horizontal line through the centre of the plot, with vertical lines delineating the lower and upper limits; the median is represented by a square marker, and the abbr:map value is denoted by a diamond. A summary of these values is given in table~\ref{tab:grb:rateposteriors}.
       \label{fig:grb:aligo:cbcrate} }
   \end{figure}

.. raw:: latex

   \begin{table}
   \begin{center}
     \begin{tabular}{lrrrrr}
       \toprule
       Scenario &    $n$ & Lower       & MAP             & Median          & Upper\\
                &        & [$\yr^{-1}$] & [$\yr^{-1}$]    & [$\yr^{-1}$]    & [$\yr^{-1}$]  \\
       \midrule
       2015--2016 & 0   & 0.00  & 0.45  & 2.80  & 11.98    \\
       2016--2017 & 1   & 0.17  & 4.07  & 6.74  & 19.13    \\
       2017--2018 & 3 & 1.37    & 5.88  & 6.99  & 15.26 \\ 
       2020+ & 10 &7.30     & 14.47     & 15.25     & 25.25    \\
       2024+ & 20 & 12.42   & 20.35     & 20.65     & 30.09    \\
       \bottomrule
   \end{tabular}
   \end{center}
   \caption[BNS rate posterior distributions]{Summary of the abbr:bns rate posteriors for each of the observing
     scenarios which are considered in this work; these posteriors are plotted
     in figure~\ref{fig:grb:aligo:cbcrate}. Here $n$ is the number of abbr:gw events which were assumed to be observed in each scenario, chosen from the ranges in table~\ref{tab:grb:scenarios}.
     \label{tab:grb:rateposteriors}
   }
   \end{table}

Validation
==========

This method is validated by first selecting values of the beaming angle,
the abbr:sgrb efficiency, and the rate of abbr:bns coalescence. Choosing
:math:`\theta=10^{\circ}`, :math:`\epsilon = 1`, and the \`realistic'
abbr:bns rate
:math:`\cbcrate = \SI{e-6}{\mega \parsec^{-3} \year^{-1}}`, the value of
the abbr:sgrb rate that would correspond to these parameter choices is
computed. This *artificial* value for :math:`\grbrate` is used in
equation ref:eq:grb:jet:posterior when computing the posterior on the
beaming angle, with the understanding that the resulting posterior
should yield an inference consistent with the \`true' value
:math:`\theta=10^{\circ}`.

.. raw:: latex

   \begin{figure}
   \centering
   \includegraphics[width=\linewidth]{figures/grb/O1_injections_violin.pdf}
   \caption[Posterior distributions of the validation procedure described in section \ref{sec:grb:validation}]{The posterior probability distributions resulting from the validation analysis described in section~\ref{sec:grb:validation}, using the observing time and horizon distance for the 2015--2016 observing scenario (see table~\ref{tab:grb:scenarios}). In order to validate the algorithm an artificial scenario was constructed with a known beaming angle by artificially setting an observed \gls{sgrb} event rate of $\SI{36.7}{\giga \parsec^{-3} \year^{-1}}$ to induce a beaming angle of $\theta \approx 10^{\circ}$. 
     \label{fig:grb:validation:results:2015}}
   \end{figure}

.. raw:: latex

   \begin{table}
     \centering
     \begin{tabular}{lrrrr}
       \toprule
       Prior & Lower & MAP & Median & Upper\\
             & [$^\circ$] & [$^\circ$]& [$^\circ$]& [$^\circ$] \\
       \midrule
       $\delta(1.0)$ & 3.68     & 5.88  & 8.45          & 39.44     \\
       $\delta(0.5)$ & 5.24     & 8.59  & 11.89     & 50.51     \\
       Jeffreys      & 4.38     & 7.69  & 13.23     & 69.74     \\
       U(0,1)        & 4.62     & 8.14  & 13.23     & 63.81     \\
       \bottomrule
   \end{tabular}
   \caption[Beaming angle posteriors for the 2015--2016 observing scenario]{Summary of the beaming angle posteriors from figure~\ref{fig:grb:validation:results:2015}, for the 2015--2016 observing scenario, with an artificial abbr:sgrb rate imposed to produce a target beaming angle of $\theta = 10^{\circ}$.
     \label{tab:grb:validation:results:2015}}
   \end{table}

.. raw:: latex

   \begin{figure}
   \centering
   \includegraphics[width=\linewidth]{figures/grb/O2_injections_violin.pdf}
   \caption[Beaming angle posteriors for the 2016--2017 observing scenario]{The posterior probability distributions resulting from the validation analysis described in section~\ref{sec:grb:validation}, using the observing time and horizon distance for the 2016--2017 observing scenario (see table~\ref{tab:grb:scenarios}). The procedure used to produce figure~\ref{fig:grb:validation:results:2015} was repeated for the observing time and the horizon distance of the 2016--2017 observing scenario, with an observed abbr:sgrb event rate of $\SI{28.0}{\giga \parsec^{-3} \year^{-1}}$ used to induce a beaming angle of $\theta \approx 10^{\circ}$.
   The observed abbr:sgrb event rate in this scenario is lower than that used for the 2015--2016 scenario in order to induce the same opening angle despite the greater sensitivity and abbr:bns event rate of this scenario.
     \label{fig:grb:validation:results:2016}}
   \end{figure}

.. raw:: latex

   \begin{table}
     \centering
     \begin{tabular}{lrrrr}
       \toprule
       Prior & Lower & MAP & Median & Upper\\
             & [$^\circ$] & [$^\circ$]& [$^\circ$]& [$^\circ$] \\
       \midrule
       $\delta(1.0)$ & 4.15     & 6.78  & 7.62  & 21.17     \\
       $\delta(0.5)$ & 6.11     & 9.50  & 10.88     & 27.88     \\
       Jeffreys & 5.05  & 9.05  & 12.21     & 62.72     \\
       U(0,1) & 5.12    & 9.05  & 11.29     & 51.04     \\
       \bottomrule
   \end{tabular}
   \caption[Beaming angle posteriors for the 2016--2017 observing scenario]{Summary of the beaming angle posteriors from figure
     \ref{fig:grb:validation:results:2016}, for the 2016--2017 observing scenario,
     with an artificial abbr:sgrb rate imposed to produce a target beaming
     angle of $\theta \approx 10^{\circ}$.}
     \label{tab:grb:validation:results:2016}
   \end{table}

Figures ref:fig:grb:validation:results:2015 and
ref:fig:grb:validation:results:2016 show the beaming angle posteriors
which result from this analysis for the 2015--2016 and 2016--2017
scenarios respectively for each choice of prior distribution on the
efficiency parameter. Unsurprisingly, the most accurate constraints
arise with the tightest possible constraints on the abbr:sgrb
efficiency, :math:`\epsilon`. That is, the beaming angle posterior
arising from the :math:`\delta`-function prior on :math:`\epsilon` is
the narrowest, yielding the shortest possible credible interval. It is
worth remembering, however, that an incorrect value of :math:`\epsilon`
when using the :math:`\delta`-function prior, would result in a
significantly biased posterior, and the inference of the beaming angle
would be incorrect. This highlights the necessity of building a suitable
representation of ignorance into the analysis.

The similarity of the posteriors which result from the uniform and
Jeffreys priors is worth noting, demonstrating that the choice between
the least-informative and the indifferent priors leads to only a small
difference in the posterior distributions.

Results for the advanced LIGO observing scenarios
=================================================

.. raw:: latex

   \begin{figure}
   \centering
   {\includegraphics[width=\linewidth]{figures/grb/O1_beaming_posteriors_violin.pdf}}
   \caption[Beaming angle posteriors for the 2015--2016 observing scenario]{Beaming angle posteriors using different priors on abbr:sgrb efficiency $\epsilon$ in the 2015--2016 observing scenario.
       \label{fig:grb:results:2016}
   }
   \end{figure}

.. raw:: latex

   \begin{figure}
   \centering
   {\includegraphics[width=\linewidth]{figures/grb/O2_beaming_posteriors_violin.pdf}}
   \caption[Beaming angle posteriors for the 2016--2017 observing scenario]{Beaming angle posteriors using different priors on abbr:sgrb efficiency $\epsilon$ in the 2016--2017 observing scenario.
       \label{fig:grb:results:2017}}
   \end{figure}

.. raw:: latex

   \begin{figure}
   \centering
   {\includegraphics[width=\linewidth]{figures/grb/o5_violins.pdf}}
   \caption[Beaming angle posteriors for the 2024+ observing scenario]{Beaming angle posteriors using different priors on abbr:sgrb efficiency $\epsilon$ in the 2024+ observing scenario.
       \label{fig:grb:results:2024}}
   \end{figure}

.. raw:: latex

   \begin{table}
   \centering
   \begin{tabular}{llrrrr}
     \toprule
     Scenario & Prior & Lower & MAP & Median & Upper \\
     && [$^{\circ}$] & [$^{\circ}$]    & [$^{\circ}$]    & [$^{\circ}$]  \\
     \midrule
     2015--2016 & U(0,1)    & 2.00  & 5.43 & 9.24  & 40.17  \\
   & Jeffreys   & 1.90  & 5.43 & 9.50  & 49.71  \\
   & $\delta(1)$    & 1.76  & 4.07 & 5.83  & 21.04  \\
   & $\delta(0.5)$      & 2.51  & 5.88 & 8.22  & 28.35  \\
   \midrule
     2016--2017 & U(0,1)    & 3.09  & 6.78 & 9.91  & 34.23  \\
   & Jeffreys   & 2.85  & 6.78 & 9.91  & 46.93  \\
   & $\delta(1)$    & 2.88  & 5.43 & 6.40  & 14.15  \\
   & $\delta(0.5)$      & 4.06  & 7.69 & 9.07  & 20.05  \\
   \midrule
     2018--2019 & U(0,1)    & 6.64  & 12.66    & 16.36 & 46.96  \\
   & Jeffreys   & 6.31  & 11.76    & 15.88 & 57.48  \\
   & $\delta(1)$    & 6.36  & 9.95 & 10.97 & 18.35  \\
   & $\delta(0.5)$      & 8.98  & 14.02    & 15.55 & 26.15  \\
   \midrule
     2020+    
   & U(0,1)     & 8.20  & 12.66    & 16.04 & 44.73  \\
   & Jeffreys   & 7.82  & 12.21    & 15.35 & 56.99  \\
   & $\delta(1)$    & 8.10  & 10.85    & 11.12 & 14.95  \\
   & $\delta(0.5)$      & 11.47     & 14.92    & 15.75 & 21.17  \\
   \midrule
     2024+    
   & U(0,1)     & 9.05  & 13.12    & 16.07 & 45.10  \\
   & Jeffreys   & 8.58  & 12.21    & 15.28 & 56.30  \\
   & $\delta(1)$    & 9.09  & 11.31    & 11.30 & 14.02  \\
              & $\delta(0.5)$   & 12.82     & 15.83    & 16.00 & 19.82  \\
     \bottomrule
   \end{tabular}
   \caption[Summary of beaming angle inferences for a number of observing scenarios between 2015 and design sensitivity for advanced LIGO]{Summary of the beaming angle inferences for each prior in each of the observing scenarios detailed in table \ref{tab:grb:scenarios}.
       The lower and upper values correspond to the lower and upper bounds of the 95\% Bayesian credible interval for each scenario.
       \label{tab:grb:results}}
   \end{table}

The posterior distributions on the beaming angle for the first two
observing scenarios from table ref:tab:grb:scenarios are plotted as
violin plots in figures ref:fig:grb:results:2016 and
ref:fig:grb:results:2017. These observing scenarios are described in
table ref:tab:grb:scenarios, with the inferred abbr:bns rates for each
scenario detailed in table ref:tab:grb:rateposteriors. A fiducial
abbr:sgrb rate of
:math:`\grbrate = \SI{10}{\giga\parsec^{-3}\year^{-1}}` was used for
each scenario. These show the beaming angle posteriors obtained with the
various prior distributions listed in section
ref:sec:grb:beamingposterior  [3]_ [4]_.

Since it is a common assumption in related literature, a prior on the
abbr:sgrb efficiency which dictates that all abbr:bns produce an
abbr:sgrb, :math:`p(\epsilon|I)=\delta(\epsilon=1)`, is also considered
in addition to the previous strong :math:`\delta`-function prior.

The 2015-2016 scenario, which corresponds to a three-month observing
period in which no abbr:bns signals were detected, provides the least
information of the scenarios under consideration, with none of the
efficiency priors producing a clear result (the posterior distribution
for each of the four efficiency situations is broad). In the 2016-2017
scenario the inference of the beaming angle are also somewhat weak, due
to the singular abbr:gw detection, and small :math:`VT` the
uncertainties are large enough that the results from each prior are
broadly consistent. Both of the posteriors of each of these scenarios
are plotted in figures ref:fig:grb:results:2016 and
ref:fig:grb:results:2017 respectively.

In the 2024+ scenario, where the posterior is more peaked, it is clear
that the strong :math:`\delta`-function priors lead to inconsistent
inferences on the abbr:sgrb beaming angle. This can be seen in the plots
of each posterior distribution in figure ref:fig:grb:results:2024. The
much weaker uniform and :math:`\beta` distributions, by contrast, are
again largely consistent with each other yielding more conservative and
robust results, as well as being a more representative expression of our
state of knowledge. The inferences drawn from each scenario and each
prior are summarised in terms of the abbr:map measurement and the 95%
credible interval around the maximum in table ref:tab:grb:results.

One noteworthy feature of these results is the apparent discontinuity in
the inferred beaming angle between the 2016--2017 scenario, and the
2018--2019 scenario. Consulting table ref:tab:grb:rateposteriors we can
see that the median abbr:sgrb rate which is inferred for both scenarios
is similar, despite the considerable increase in :math:`VT` between the
two scenarios. While this could be taken to imply that the estimate of
:math:`n=3` abbr:bns events is an underestimate (this corresponds to
around half the rate of events that :math:`n=1` implies for the
2016--2017 observing scenario), it might equivalently be taken to imply
that the observation of one event during the 2016--2017 was simply
fortunate. As a result the 2016-2017 observing scenario implies a
smaller opening angle to correspond to the larger ratio of abbr:bns rate
to abbr:sgrb rate. Similarly, the 2015-2016 scenario, in which no
abbr:bns events are detected, implies a comparable rate of observed
abbr:bns per unit :math:`VT` to the 2016-2017 scenario, leading to a
broadly comparable estimate of the median opening angle in both
scenarios.

It is clear from the results presented in table ref:tab:grb:results that
under the common assumption that all abbr:bns events should launch a
abbr:grb jet that this method allows the most restrictive limits to be
placed on the beaming angle; the lower limit placed on the beaming angle
from this assumption is comparable in the most sensitive scenario
(2024+) for the uniform and Jeffreys priors, however both of these
priors produce posterior distributions on the beaming angle which has a
long tail, and consequently large upper limits on the beaming angle.

Sensitivity beyond the advanced era
===================================

.. raw:: latex

   \begin{figure}
   \centering
   \includegraphics[width=\linewidth]{figures/volume_v_nevents.pdf}
   \caption[The upper-bound on the beaming angle assuming a Jeffreys prior on the probability of jet production]{
   \label{fig:grb:results:volume:EJ:upper} 
   The upper-bound of the 95\% credible interval on the beaming angle as a function of the rate of observed gravitational wave abbr:bns events and the observed search 4-volume, taking a Jeffreys prior on the efficiency of abbr:sgrb
     production from abbr:bns events. The search volumes corresponding to
     observing scenarios are marked as vertical lines on the plot, with
     each line assuming that observations are carried out over the period
     of one year, achieving the search volume outlined in table
     \ref{tab:grb:scenarios}.}
   \end{figure}

.. raw:: latex

   \begin{figure}
   \centering
   \includegraphics[width=\linewidth]{figures/volume_v_nevents_e1.pdf}
   \caption[The upper-bound on the beaming angle assuming all BNS events produce sGRBs] {
   \label{fig:grb:results:volume:E1:upper} 
   The upper-bound of the 95\% credible interval on the beaming angle as a function of the rate of observed gravitational wave abbr:bns events and the observed search 4-volume, assuming that all abbr:bns events produce an abbr:sgrb. 
   The search volumes corresponding to observing scenarios are marked as vertical lines on the plot, with each line assuming that observations are carried out over the period of one year, achieving the search volume outlined in table~\ref{tab:grb:scenarios}.}
   \end{figure}

.. raw:: latex

   \begin{figure}
   \centering
   \includegraphics[width=\linewidth]{figures/volume_v_nevents_lower.pdf}
   \caption[The lower-bound on the beaming angle assuming a Jeffreys prior on the probability of jet production]{
   \label{fig:grb:results:volume:EJ:lower} 
   The lower-bound of the 95\%
     credible limit on the beaming angle as a function of the observed
     number of events and the observed search 4-volume, taking a Jeffreys
     prior on the efficiency of abbr:sgrb production from abbr:bns
     events. The search volumes corresponding to observing scenarios
     are marked as vertical lines on the plot.}
   \end{figure}

.. raw:: latex

   \begin{figure}
   \centering
   \includegraphics[width=\linewidth]{figures/volume_v_nevents_lower_e1.pdf}
   \caption[The lower-bound on the beaming angle assuming all BNS events produce sGRBs]{
   \label{fig:grb:results:volume:E1:lower} 
   The lower-bound of the 95\%
     credible limit on the beaming angle as a function of the observed
     number of events and the observed search 4-volume, assuming that
     every gravitational wave abbr:bns event produces an abbr:sgrb. The search
     volumes corresponding to observing scenarios are marked as vertical
     lines on the plot.}
   \end{figure}

Conclusions
===========

The development of this hierarchical Bayesian method for jet angle
inference has allowed limits to be placed on the credible region of the
abbr:sgrb jet beaming angle posterior as a function of the observed
number of events and the observed search 4-volume, under a variety of
different efficiency conditions. Thanks to the observations of the
advanced gls:ligo detector network during its 2016-2017 observing run,
with a single abbr:bns detection, it is possible to place a lower limit
of :math:`\ang{2.85}`, and an upper limit of :math:`\ang{46.93}` on the
jet beaming angle, given an uninformative prior on the efficiency at
which abbr:bns events produce observable abpl:sgrb. Assuming that all
abbr:bns events produce an observable abpl:sgrb limits narrow to between
:math:`\ang{2.88}` and :math:`\ang{14.15}`. When advanced gls:ligo
design sensitivity is achieved around 2020 the observation of 10
abbr:bns events in abbr:gw is sufficient to place an upper-limit of
:math:`\ang{56.99}` on the jet beaming angle, and can establish the
limit on the beaming angle to be between :math:`\ang{7.82}` and
:math:`\ang{56.99}`, assuming an uninformative prior on the abpl:sgrb
production efficiency. These limits narrow to between :math:`\ang{8.10}`
and :math:`\ang{14.95}` if perfect efficiency is assumed.

In contrasts to previous work, this method incorporates uncertainty in
the event rate of abbr:bns signals detected by a abbr:gw detector, and
also includes uncertainty in the efficiency with which abbr:sgrb are
produced by these merger events. The limits found from this method are
consistent with results using the rates based approach outlined in
cite:Abbott:2016ymx which finds a lower limit of
:math:`\ang{2.3}^{+{1.7}}_{-{1.1}}` after analysis of the first gls:ligo
observing run data, under the assumption that all abpl:sgrb are the
result of a abbr:bns. Previous methods have included uncertainty in the
abbr:bns rate, but none have performed the analysis using this
hierarchical approach. I also believe this is the first work which has
attempted to account for the potential efficiency factor, and has
presented opening angle estimates using different priors on this
quantity.

The work presented in this chapter used a fixed event rate for abbr:sgrb
in the local universe. This number is, however, uncertain, and it is
possible this rate varies outside the immediate vicinity of the Earth.
Future work could incorporate this uncertainty by placing an appropriate
prior on the abbr:sgrb rate, and potentially incorporating
considerations based on the abbr:sgrb distance into the hierarchical
analysis.

The estimates of abbr:bns rate used to demonstrate this method were
based on rate posteriors constructed assuming Poisson-distributed
events. Given that observational data from abbr:gw detectors is now
available it is possible to compute rate posteriors using mock data
challenges and real detector noise, allowing for the effects of
non-stationarity in the detector noise to be taken into account in the
calculation of the rate posterior.

While abpl:grb are one of the most prominent examples of a beamed
emission process in multi-messenger astrophysics, where event rates can
be determined through two separate channels, they are by no means
unique. This method could be extended easily to situations where beamed
particle emission is present, such as high-energy neutrinos, for
example. In addition, there are a number of directions this work can be
taken in the future. The "top-hat" model has become less favoured since
the multimessenger observations associated with gls:gw170817. The
abbr:sgrb associated with this event was less luminous than would have
been expected had the top-hat model been correct
cite:2017ApJ...848L..13A. It would therefore be valuable to consider the
implication of more complicated "structured" jets on the analysis, and
whether it is still possible to make statements using this or a
comparable method about the geometrical parameters of those models.

In the analysis presented in this chapter an abbr:sgrb rate was chosen
and fixed. This was done partly due to the difficulty in determining a
suitable prior on this rate at the time the research was conducted,
however there has been much work in this area in the last two years
cite:2019ApJ...880...55M,2018ApJ...857..128J and it would be interesting
to revisit this assumption, and place a suitable prior distribution on
the abbr:sgrb rate in order to understand the effect of the uncertainty
in this quantity on the inference of the beaming angle.

Additionally, the abbr:bns event rates used in the analysis presented in
this chapter are based on anticipated detector sensitivities. The
advanced gls:ligo and gls:virgo detectors have now completed two
observing runs, and the event rate based on the true detector
sensitivity and duty cycle can be determined using mock data challenges
 [5]_; this would allow the beaming angle estimate to be based on
observational results rather than purely theoretical arguments.

Given the joint observation of abbr:gw from a abbr:bns event, and an
abbr:sgrb during the second observing run of the advanced detectors the
prospect of joint abbr:gw and abbr:em observations is now a reality. The
knowledge that a single event is the source of both abbr:gw and abbr:bns
provides additional information which the technique presented in this
paper is not currently capable of incorporating. Development of the
hierarchical analysis to take this into account would likely improve the
results of the inference, however this is not likely to be a
straight-forward change, since it introduces an additional input datum,
the joint-event rate.

The challenges and opportunities which are presented by the arrival of
observational multi-messenger results for abbr:bns events make
hierarchical analyses such as the one presented in this chapter all the
more useful. This modelling technique allows very complex analyses to be
built in simpler sections and then connected together, allowing
additional effects to be taken into account without a major re-working
of the model's implementation in code, for example. The model presented
in this chapter is clearly incomplete, but provides one of these
sections; a more ambitious project would involve connecting this with
analyses of observational abbr:gw data and observations from abbr:sgrb
observatories. Indeed, there is scope to add observations of other
abbr:em effects into a much expanded model, including for example,
observations in the ultra violet and visible spectra of the kilonova
resulting from interactions within the ejecta from the abbr:bns event;
and observations across the entire abbr:em spectrum.

.. [1]
   And also a rather satirical commentary on the state of contemporary
   astrophysics!

.. [2]
   Following the observation of the unusual GRB170817A the efficacy of
   the top-hat model has been called into question. The top-hat model
   is, however, easy to work with.

.. [3]
   A note on implementation: rather than directly evaluating the beaming
   angle posterior in equation ref:eq:grb:jet:posterior we choose to
   sample points from the posterior using an abbr:mcmc algorithm,
   implemented using the python package ``PyMC3`` cite:Salvatier2016.

.. [4]
   While we present the entire posterior for only these two observing
   scenarios in this section, we provide an overview of all of the
   observing scenarios in section ref:sec:grb:beyond.

   While the advanced detectors, such as advanced gls:ligo are likely to
   observe a number of abbr:bns events, and a considerable 4-volume of
   spacetime, the scenarios in ref:tab:grb:scenarios are limited to
   anticipated sensitivities and event rates within the next decade.

   Figures ref:fig:grb:results:volume:EJ:upper and
   ref:fig:grb:results:volume:EJ:lower show the upper and lower limits
   of the 95% confidence region, assuming a Jeffreys prior on the
   efficiency, as a function of the observed :math:`VT` and number of
   abbr:bns events. Similarly, figures
   ref:fig:grb:results:volume:E1:upper and
   ref:fig:grb:results:volume:E1:lower show the upper and lower limits
   of the 95% confidence region assuming all abbr:bns events launch an
   abbr:sgrb. These plots have heavy black lines overlaid to represent
   the anticipated :math:`VT` which will be observed by the advanced
   gls:ligo network in the 2020+ and 2024+ scenarios.

   Similarly to the behaviour seen in the observing scenarios of section
   ref:sec:grb:jetposterior the upper- and lower-bounds on the beaming
   angle converge much more rapidly under the assumption that all
   abbr:bns produce an abbr:sgrb compared to when a Jeffreys prior is
   assumed over the efficiency.

.. [5]
   See section ref:sec:sources:mdc on page
   :raw-latex:`\pageref{sec:sources:mdc}` for an overview of this
   technique, in the context of burst searches. The same principles can
   be applied to other transient signals, in this case using abbr:bns
   waveforms rather than burst signals in order to calculate the
   sensitivity of the detector, taking into account noise
   non-stationarity and the evolution of the sensitivity through the
   observing run.
