Gravitational waves
###################

14 September 2015 will likely be remembered as one of the most
significant in the history of astronomy, and of astrophysics. Early in
the morning of this autumn day, at 09:50 UTC, a abbr:gw passed through
the Earth, and on its way produced a sufficiently large movement in the
mirrors and test masses of the detectors of gls:ligo, as to be detected.

Over five months of data analysis, detector characterisation, and
detection verification were conducted by a global team of scientists, in
the abbr:lvc. This process resulted in a slew of journal papers being
written, vast quantities of data produced, and the launch of an enormous
public outreach effort. Eventually, the collaboration found itself in a
position to make the announcement of the first direct detection of
abpl:gw, gls:gw150914, on 11 February 2016.

Further discoveries2 were made during the first observing run of the
advanced abbr:ligo facilities, gls:lvt151012  [1]_, observed in October,
and gls:gw151226, observed in December, added to the collection of
directly detected black hole binaries (although the significance of the
former was insufficient to garner its own press release and announcement
publication). The majority of 2016 was dedicated to introducing upgrades
to the two gls:ligo interferometers, and to commissioning a third
second-generation interferometric observatory, gls:virgo, located in
Italy. The second observation run of gls:advanced-ligo, which was
scheduled to be longer and more sensitive than its first lead to the
observation of three further binary black hole coalescences during the
run: gls:gw170104, gls:gw170608, and gls:gw170814, the latter observed
by a network of three detectors, gls:virgo having joined the observing
run a short time before. These events are summarised in table
ref:tab:eventlist, alongside detections which were made \`\`offline'' in
the archival data.

Great excitement was also to be had during the second observing run,
with the detection of gls:gw170817, the first detection of a coalescing
abbr:bns system, which was also the first occasion on which
gravitational waves had contributed to a multi-messenger observation.
This event is discussed in greater detail in section
ref:sec:detections:gw170817.

gls:gw150914 is not the first evidence for abpl:gw, with the
Hulse-Taylor pulsar cite:1975ApJ...195L..51H,2005ASPC..328...25W having
provided compelling indirect evidence which lead to its discoverers
receiving the 1993 Nobel Prize.

This chapter serves as a brief overview of the mathematical and physical
motivation for the search for abpl:gw, the current network of abbr:gw
detectors, and a synopsis of the first abbr:gw detections. In addition a
primer on the conventions used in the description of abbr:gw signals is
included later in this chapter (in section ref:sec:gw:strain).

Gravitational waves and general relativity
==========================================

abpl:gw are one of the predictions of Einstein's 1915 General Theory of
Relativity cite:1915SPAW.......844E, with the first theoretical
prediction of their existence being proposed by Einstein in 1916
cite:1937FrInJ.223...43E,1918SPAW.......154E, less than a year after the
publication of the general theory. Einstein's original wave solution
proposes three different forms of abbr:gw, which Hermann Weyl denoted
*longitudinal-longitudinal*, *transverse-longitudinal*, and
*transverse-transverse* waves cite:1970rzmv.book.....W. However, the
approximation made by Einstein, to find the weak-field limit of the
abpl:gw, was considered debatable. In 1922 Arthur Eddington showed that
two of the wave solutions were artefacts of the choice of coordinate
system cite:1922RSPSA.102..268E, and threw the existence of the
remaining transverse-transverse waves into doubt. The confusion over the
existence of abpl:gw continued, with one bizarre incident in 1936
serving to further muddy the waters. Einstein and Rosen submitted a
paper entitled \`\`Are there any gravitational waves?'' to *Physical
Review*, allegedly concluding that they do not. The anonymous referee of
that paper (who would later transpire to have been the cosmologist
Howard P Robertson) disagreed with the paper's conclusion (that abpl:gw
did *not* exist). Einstein's fury at the journal's editor for having
sent the paper for peer review led to him withdrawing the publication,
allowing him the time to be persuaded of the mistake which resulted in
the work's erroneous conclusion.

The confused situation with the existence of abpl:gw dogged the subject
for several decades, with little progress made until Felix Pirani's work
on describing abpl:gw with respect to the gls:riemann-tensor
cite:1956AcPP...15..389P, a quantity which is, crucially, observable,
and provides a coordinate-free description.

A wave solution to the field equations
--------------------------------------

The behaviour of gravitational fields in the presence of mass is
modelled, in abbr:gr, by the Einstein field equations,

.. raw:: latex

   \begin{equation}
   \label{eq:einsteinfieldequations}
    R_{\mu \nu} - \frac{1}{2} R g_{\mu \nu} = \frac{8 \pi G}{c^{4}} T_{\mu \nu}.
   \end{equation}

Here :math:`R_{\mu \nu}` is the gls:ricci-tensor, which represents the
amount by which a sphere is distorted at a point in spacetime  [2]_;
:math:`R` the gls:ricci-scalar  [3]_, the trace of the Ricci tensor;
:math:`g_{\mu \nu}` is the metric tensor, which describes the local
geometry of spacetime at any given point; and :math:`T_{\mu \nu}` the
stress-energy tensor, which encapsulates the density and time-variation
of energy and momentum at any given point in spacetime.

Contracting equation ref:eq:einsteinfieldequations with a timelike unit
vector allows a reduction to a situation with a defined direction of
time. This contraction leads to the revelation that spacetime curvature,
:math:`R`, is produced by the mass-energy density, since the contraction
of a timelike vector with the stress-energy tensor returns simply the
mass-energy density, :math:`\rho`, in a dust of non-interacting masses.
We then find

.. math::  R = - 4 \pi G \rho, 

 which leads to the second-half of the famous aphorism,

    \`\`Spacetime tells matter how to move; matter tells spacetime how
    to curve.'' ---John Archibald Wheeler cite:geonsblackholes

Despite their apparent simplicity the Einstein Field Equations are
highly non-linear in the metric, :math:`g_{\mu \nu}`, and only a few
exact solutions are known. While some of these solutions, which include
the Schwarzchild solution (for the behaviour of spacetime close to a
non-spinning singularity), and the Kerr solution (for the spacetime
close to a rotating singularity) are exact and tractable, the majority
of scenarios lead to non-analytical solutions which must be explored
numerically. While the Einstein equations provide this valuable insight
into the behaviour of a static system, it is more often of interest to
consider dynamic systems, and the time-evolution of the system. One
approach to dealing with the non-linearity of the field equations is to
\`\`linearise'' the theory, by assuming first a known solution of the
field equations, :math:`\eta_{\mu\nu}`, and then producing a small
perturbation on that solution, :math:`h_{\mu\nu}`. This approach is
introduced in, for example, cite:mtw, and provided that the size of the
perturbation is sufficiently small, provides a means of investigating
the model in \`\`weak-field'' scenarios. Such an approach is suitable
for the study of the evolution of the weak-field. The metric in such a
scenario takes the form

.. raw:: latex

   \begin{equation}
   \label{eq:linearised-metric}
   g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}.
   \end{equation}

Allowing :math:`\bar{h} \gets h`, representing a rescaling  [4]_ of the
perturbation,
:math:`\bar{h} = h_{\mu \nu} - \frac{1}{2}\, \eta_{\mu \nu} h`. We can
then make a choice of gauge, the Lorentz (or Hilbert) gauge, by
specifying :math:`\bar{h}\indices{^{\mu\nu}_{,\nu}} = 0`.

For convenience it is normal to work in \`\`geometrised units'', where
the speed of light, :math:`c = 1`. Doing so does, however, require care
to include a :math:`c^{-1}` factor in the value of :math:`x^0` when
converting to natural units.

The derivative of the metric then describes the propagation of the
perturbation,

.. raw:: latex

   \begin{equation}
   \label{eq:wave-equation-gw}
   \dalembert \barh \equiv \bar{h}\indices{_{\mu\nu,\alpha}^{\alpha}} = 0,
   \end{equation}

where :math:`\dalembert` is the d'Alembertian box operator. This has
plane-wave solutions of the form

.. raw:: latex

   \begin{equation}
      \label{eq:planewavegw}
      \barh = \real \left[ A_{\mu\nu} \exp\left(\ii k_{\alpha}x^{\alpha}\right) \right]
   \end{equation}

for a null wavevector, :math:`\vec{k}`, orthonormal to an amplitude
:math:`\ten{A}`. Provided a transverse, traceless [5]_ gauge is chosen,
the amplitude tensor takes the form

.. raw:: latex

   \begin{equation}
   \label{eq:ttamplitudetensor}
   \ten{A} = 
      \begin{bmatrix}
      0 & 0 & 0 & 0\\
      0 & A_{xx} & A_{xy} & 0\\
      0 & A_{xy} & -A_{xx} & 0\\
      0 & 0 & 0 & 0
      \end{bmatrix}.
   \end{equation}

It is clear from the form of the plane-wave solution in equation
ref:eq:planewavegw that a wave propagates in spacetime in a manner quite
different from a wave on, for example, the surface of a loch: rather
than a vector perturbation, a abbr:gw propagates as a tensor
perturbation. The conventional method used to visualise this effect
involves considering the effect of a abbr:gw travelling perpendicular to
a ring of test particles. For such a wave, propagating along the
:math:`z`-axis, in the transverse-traceless gauge, the only
non-vanishing components of the strain are (returning to natural units
by including :math:`c` as a factor)

.. math::  h_{xx} = - h_{yy} = \real[ A_{xx} \exp(- \ii \omega (ct-z) ], 

 and

.. math::  h_{xy} = h_{yx} = \real[ A_{xy} \exp(- \ii \omega(ct-z) ]. 

 The propagation can then be described as the superposition of two
linearly-polarised components; the unit polarisation tensors can be
derived from the coordinate basis as

.. raw:: latex

   \begin{align}
   \label{eq:gwpolarisationbasis}
    \ten{e}_{+} &= \ten{e}_{x} \otimes \ten{e}_{x} - \ten{e}_{y} \otimes \ten{e}_y\\
    \ten{e}_{\times} &= \ten{e}_{x} \otimes \ten{e}_{y} + \ten{e}_{y} \otimes \ten{e}_{x}
   \end{align}

As the wave passes orthogonally through the circular ring of test
particles they will be distorted into an ellipse. For the
:math:`+`-polarisation the circle is stretched into an ellipse with
semi-major axis first extending along the :math:`x`-axis, relaxing back
to a circle, and then again with a semi-major axis extending along the
:math:`y`-axis. This behaviour is depicted as a cartoon in figure
ref:fig:intro:gw:prop-plus.

\\begin{figure}[h] \\begin{tikzpicture}[xscale=0.45, yscale=0.45]
:raw-latex:`\def`:raw-latex:`\w{1.5}` :raw-latex:`\foreach`iin
{0,...,18}{ :raw-latex:`\def`:raw-latex:`\a{-90+30*\i}`
:raw-latex:`\draw[domain=0:360, thick] `plot (
{:raw-latex:`\w*`i+0.5\*(cos(:raw-latex:`\x`)\*(1+0.4\*cos(:raw-latex:`\a`)))
}, {0.5\*(sin(:raw-latex:`\x`)\*(1-0.4\*cos(:raw-latex:`\a`)))}); };
\\end{tikzpicture} \\caption[The effect of a propagating
:math:`+`-polarised abbr:gw on a ring of test particles.]{The effect of
a :math:`+`-polarised abbr:gw on a circle of test particles as it
propogates through the page (orthogonal to the ring). Time progresses
horizontally along the :math:`x`-axis from left to right. }
\\end{figure}

Equivalently, the :math:`\times`-polarisation produces a deformation
rotated :math:`45^{\circ}` relative to the :math:`+`-polarisation; this
is depicted in figure ref:fig:intro:gw:prop-cross.

\\begin{figure}[h] \\begin{tikzpicture}[xscale=0.27, yscale=0.27]
:raw-latex:`\def`:raw-latex:`\w{2.5}` :raw-latex:`\foreach`iin
{0,...,18}{ :raw-latex:`\def`:raw-latex:`\a{90+30*\i}`
:raw-latex:`\draw[domain=0:360, thick] `plot ({:raw-latex:`\w*`i+
cos(:raw-latex:`\x`) +
0.25\*sin(:raw-latex:`\x`)\*0.5\*cos(:raw-latex:`\a`) },
{sin(:raw-latex:`\x`)
+0.25\*cos(:raw-latex:`\x`)\*0.5\*cos(:raw-latex:`\a`) }); };
\\end{tikzpicture} \\caption[The effect of a propagating
:math:`\times`-polarised abbr:gw on a ring of test particles.]{The
effect of a :math:`\times`-polarised abbr:gw on a circle of test
particles as it propogates through the page (orthogonal to the ring).
Time progresses horizontally along the :math:`x`-axis from left to
right. } \\end{figure}

The behaviour of \`\`strong-field gravity'', which is essential to
understanding the production of abpl:gw can only be practically probed
using observed abpl:gw from strong-field sources, such as abbr:bbh
coalescences. Systems such as these, which involve an accelerating mass,
are capable of producing abpl:gw according to the quadrupole formula,
with the abbr:gw at a given time described by the three-dimensional
tensor

.. raw:: latex

   \begin{equation}
   \label{eq:intro:gr:quadrupole2strain}
     h_{jk} = \frac{2G}{r} \frac{\dd^2 Q_{jk}}{\dd t^2}
   \end{equation}

where :math:`G` is the gravitational constant, and :math:`Q_{jk}`, the
moment of inertia tensor, is defined as

.. raw:: latex

   \begin{equation}
   \label{eq:intro:gr:mass-quadrupole}
   Q_{jk} = \int \dd^3 x \rho(\vec{x}) \left( x_i x_j - \frac{1}{3} r^2 \delta_{ij} \right)
   \end{equation}

for a mass density :math:`\rho`, and coordinates :math:`x_j` and
:math:`x_k`.

Strain
======

The propagation of a abbr:gw will cause a relative displacement between
test masses in spacetime. As a result, a abbr:gw will produce a relative
strain, perturbing the normal metric. In the far-field approximation the
metric, :math:`g_{\mu\nu}`, can thus be described by

.. math::


   g_{\mu \nu} = \eta_{\mu \nu} + h_{\mu \nu},

as first defined in equation ref:eq:linearised-metric, with the strain,
:math:`h_{\mu\nu}` perturbing the underlying (potentially flat) metric
:math:`\eta_{\mu\nu}`.

The strain, as measured by a abbr:gw detector, can have two polarisation
states, the :math:`+` state and the :math:`\times`-polarisation state,
which combine linearly, so that

.. raw:: latex

   \begin{equation}
   \label{eq:gw-polarisations-strain}
   h = || \mat{A}_{+} {h}_{+} + \mat{A}_{\times} {h}_{\times} ||,
   \end{equation}

with :math:`h_{+}` being the amplitude of the strain in the
:math:`\mat{A}_{+}` polarisation basis, and :math:`h_{\times}` the
amplitude in the :math:`\mat{A}_{\times}` polarisation.

Finally, the overall measured strain in a detector will be the
superposition of both the strain signal and noise (which is usually
produced by movement of the detector's test masses due to effects other
than spacetime perturbations). As such, the measured signal timeseries,
:math:`h(t)`, added to the noise timeseries :math:`n(t)` provides us
with the total measured strain, :math:`s(t)`,

.. raw:: latex

   \begin{equation}
   \label{eq:intro:signalcomp}
   s(t) = n(t) + h(t). 
   \end{equation}

A similar quantity, the characteristic strain, is intended to account
for integrating an inspiralling signal, leading to a straight-forward
relationship between the characteristic strain and the gls:snr.

.. raw:: html

   <div class="definition">

The characteristic strain is a quantity which is intended to account for
the effect of observing an inspiralling signal over the full period of
the inspiral, thus integrating over a number of cycles of the signal.
For a source with strain :math:`\tilde{h}(f)` as a function of frequency
:math:`f` it is defined as

.. raw:: latex

   \begin{equation}
   \label{eq:intro:characteristic-strain}
    [h_{\text{c}}(f)]^{2} = 4 f^{2} \left| \tilde{h}(f) \right|^{2}.
   \end{equation}

.. raw:: html

   </div>

If we consider only the noise component of the recorded data,
:math:`n(t)` from equation ref:eq:intro:signalcomp, then we can define
the (one-sided) abbr:psd of the noise, :math:`S_{n}(f)`, such that

.. raw:: latex

   \begin{equation}
   \label{eq:intro:psd}
   \langle \tilde{n}(f) \tilde{n}^{*}(f) \rangle = \frac{1}{2} \delta(f - f') S_{\text{n}}(f)
   \end{equation}

where :math:`\tilde{n}(f)` is the Fourier transform of the time-domain
noise measurement :math:`n(t)`, :math:`f` is the frequency, and
:math:`\delta` is the Kronecker delta function. The angle bracket
notation :math:`\langle \tilde{n}(f) \tilde{n}^{*}(f) \rangle`
represents an average over many instances of the noise power, which is
required in order to achieve a good estimate of the abbr:psd. This
representation of the noise makes the assumption that it is stationary.
In reality, this is not strictly true, but they are reasonable
approximations for many applications; non-stationarities in the noise
can become a problem for abbr:gw detection algorithms however, and these
are discussed in more detail in section ref:sec:detectors:noise:glitch.

In analogy to the characteristic strain from definition
ref:def:intro:characteristic-strain, we can define the *characteristic
noise*:

.. raw:: latex

   \begin{equation}
   \label{eq:intro:characteristic-noise}
   \left[ h_{\text{n}}(f) \right]^{2} = f S_{\text{n}}(f).
   \end{equation}

As noted by cite:strain.conventions this allows the integration of the
strain compared to the noise budget of a given detector to be estimated
\`\`by eye'', when displayed on a log-log plot.

The ability to detect a signal in a noisy data stream requires that the
signal has sufficient power to be distinguished from the underlying
noise. In abbr:gw analysis it is normal to express the strength of such
a signal by reference to its abbr:snr. This is defined with reference to
the optimum filter for the signal, which is the Weiner filter (see
cite:strain.conventions for a discussion of this). This filter gives an
expression for the abbr:snr, :math:`\rho`  [6]_, in terms of the signal
strain in the frequency-domain, :math:`\tilde{h}(f)`, and the noise
abbr:psd, :math:`S_{\text{n}}(f)`:

.. math::

   \begin{equation}
   \label{eq:intro:snr}
   \rho^{2} = \int_{0}^{\infty} 4 \frac{ | \tilde{h}(f) |^{2} }{S_{\text{n}}(f)} \dd f = \int_{-\infty}^{\infty} \left[ \frac{h_{\text{c}}(f)}{h_{\text{n}}(f)} \right]^2 \dd(\log f).
   \end{equation}

Detecting gravitational waves
#############################

Despite Pirani's work simplifying the description of abpl:gw in abbr:gr,
it would take until 1957 for his arguments to gain prominence. The
Chapel Hill Conference of 1957 brought together around 40 physicists at
the University of North Carolina, Chapel Hill, with discussions focussed
around gravitation and abbr:gr cite:2016Univ....2...22C. It was during a
session of this meeting chaired by Hermann Bondi that Richard Feynman is
credited with developing the "sticky bead" argument. Feynman used
Pirani's formulation to argue that a device could be constructed which
would measure the energy carried by a abbr:gw.

Consider two beads on rigid rod, which are free to slide along the rod,
experiencing some friction. As a abbr:gw moves along the rod the length
of the rod will remain fixed thanks to inter-atomic forces, but the
proper distance between the two beads will change. This will result in
the beads rubbing on the rod, generating friction, and thus heat, which
can be measured cite:1957Natur.179.1072B.

One of the attendees of the meeting was Joseph Weber. Weber was the
first person to propose a practical abbr:gw detector
cite:PhysRev.117.306 while at the University of Maryland. He later went
on to construct a resonant bar detector (see section
ref:sec:detectors:resonant-bar) from which he claimed the first
detection of signals originating in the centre of the Galaxy, in 1969
cite:1969PhRvL..22.1320W,1970PhRvL..24..276W,1970PhRvL..25..180W.

Numerous attempts to confirm his findings were unsuccessful, including
searches in Ronald Drever's group at the University of Glasgow
cite:1973Natur.246..340D in the United Kingdom; at Bell Labs
cite:1973PhRvL..31..173L,1973PhRvL..31..176G,1974PhRvL..33..794L in the
United States; at Munich cite:1975NCimL..12..111B in Germany; at Moscow
cite:1973PhLA...45..271B in Russia; and at Tokyo
cite:1975PhRvL..35..890H in Japan. While Weber's original detections
were soundly refuted by the community there is little doubt that the
announcement led to a flurry of activity in the field. This ultimately
lead to the development of modern cryogenic resonant bars, such as
gls:altair cite:1992NCimC..15..943B, gls:allegro
cite:2000IJMPD...9..229M, gls:nautilus cite:1997APh.....7..231A, and
gls:explorer cite:1993PhRvD..47..362A; and laser interferometers.

Laser interferometers, of which advanced gls:ligo is an implementation,
were the result of a quest for both higher sensitivities and greater
bandwidth. The possibility of using a Michelson interferometer to
measure the distance between test masses in order to detect
gravitational radiation originated in
Moscow:raw-latex:`\cite{1963JETP...16..433G}` in 1963, and again in 1966
cite:1966SvPhU...8..513B.

Robert Forward, a former student of Weber, who had been involved in the
construction of the original Weber Bar, was the first to work on the
development of an interferometric detector, at Hughes Research
Laboratory in the early 1970s, with the development of a \`\`laser
transducer'' cite:1971ApOpt..10.2495M in 1971. This lead to the
development of an 8.5-metre detector cite:1978PhRvD..17..379F, which
failed to show any signal correlation with the bar detectors at Argonne,
Glasgow, Friscati, or Maryland.

This approach was followed early-on by Scottish and German groups as a
means of improving on resonant bar sensitivities, with a 3-meter and
later a 30-meter prototype detector constructed at Garching in the late
1970s cite:1979JPhE...12.1043B,1988PhRvD..38..423S which used optical
delay lines, and a 1-meter prototype, and later a 10-meter instrument
was built at Glasgow in the early 1980s
cite:1979RSPSA.368...11D,1995RScI...66.4447R, which used Fabry-Perot
cavities. The Glasgow detector was the spiritual predecessor to the
CalTech 40-meter prototype cite:1996PhLA..218..157A.

The increasing maturity of technology developed by these prototypes lead
to the construction of the first generation of long-baseline detectors.
The group at Glasgow had aspirations to construct such a detector in
Scotland cite:Hough:1986bi, while the group in Garching had similar
plans for a German detector. While neither detector came to fruition, a
smaller-scale, joint German-UK detector, gls:geo600
cite:1997CQGra..14.1471L was constructed near Hannover. The gls:tama
detector was built in Tokyo cite:1996JKASS..29..279K. These would be
joined by the three kilometre-scale joint Caltech-MIT initial gls:ligo
detectors cite:1992Sci...256..325A, located at two sites in the USA, and
the joint Italian-French detector gls:virgo cite:1990NIMPA.289..518B,
near Cascina. These detectors were operated during the 2000s, and while
none of them made a detection of abpl:gw, they provided valuable
astrophysical results by placing astrophysical limits on the strength of
the stochastic abbr:gw background cite:2014PhRvL.113w1101A, production
of abpl:gw by pulsars cite:2014ApJ...785..119A and gamma ray bursts
cite:2012ApJ...760...12A, and the rate of compact binary coalescence in
the local universe cite:2012PhRvD..85h2002A,2013PhRvD..87b2002A.

Figure ref:fig:detectors:interferometers:firstgen is a plot of the noise
abbr:asd of the first generation of interferometric detectors, which
demonstrates the wide range of frequencies which detectors of this type
are capable of measuring abbr:gw strain over.

.. raw:: latex

   \begin{figure}
   \includegraphics{figures/intro/first-gen-asd.pdf}
   \caption[The ASDs of the first generation of large-scale interferometers]{The approximate abpl:asd for the first generation of large-scale interferometers: initial gls:ligo (red), and gls:virgo (blue), derived from the fits in table 1 of \cite{2009LRR....12....2S}.
   \label{fig:detectors:interferometers:firstgen}}
   \end{figure}

\\begin{figure}[t] |image| \\caption[The noise curves of the Advanced
LIGO detectors]{The predicted abbr:asd of the gls:advanced-ligo
detectors within their sensitive band, at design sensitivity (from the
fit in table 1 of :raw-latex:`\cite{2009LRR....12....2S}`), relative to
the estimated sensitivity of the two interferometers in their first
observing run (O1)~:raw-latex:`\cite{ligo-t1200307}`. } \\end{figure}

The initial-generation of detectors were upgraded during the first half
of the 2010s, leading to Advanced gls:ligo cite:2015CQGra..32g4001L
which resumed observations in September 2015, with the Advanced
gls:virgo detector cite:2015CQGra..32b4001A joining in summer 2017 to
conduct joint observations with its counterparts in the USA. The
gls:geo600 detector was the first of the initial detectors to be fully
upgraded as part of the gls:geo-hf project cite:2006CQGra..23S.207W,
with improved sensitivity at high frequencies. Japanese efforts have
focused on the development of gls:kagra (formerly abbr:lcgt), a
cryogenic interferometer located deep underground in the Kamioka mine
cite:1999IJMPD...8..557K, which is expected to join the third observing
run of advanced gls:ligo. The construction of a third gls:ligo
interferometer in India using the mothballed second detector from the
Washington site has now moved into its initial stages, with the prospect
of this detector joining the network by the mid-2020s. Figure
ref:fig:detectors:aligo-asd depicts the anticipated abb:asd of the
advanced gls:ligo detectors once they have reached their design
sensitivity, which is expected within the next five years.

The second-generation detectors, specifically the two advanced gls:ligo
detectors responsible for the first discovery of abpl:gw
cite:2016PhRvL.116m1103A, have successfully demonstrated the ability of
interferometry to observe the gravitational universe. This said, future
improvements in sensitivity are highly desirable, but are likely to be
even more technically challenging than the transition from resonant bars
to laser interferometers.

In order to improve the bandwidth of detectors a location of minimal
*Newtonian noise* (see ref:sec:detectors:noise:newtonian), which results
from variation in the local gravitational field, must be found, which
ultimately mandates the placement of an interferometer in space. The
earliest proposals for a space-based detector came in the form of
gls:lagos, which originated as a concept at the University of Colorado
under Jim Faller and Peter Bender cite:1989AdSpR...9..107F. These
proposals would develop into gls:lisa cite:2013GWN.....6....4A, which is
likely to launch in the 2030s. The technology demonstration mission for
gls:lisa, *LISA Pathfinder* was launched in December 2015, and its main
mission was completed successfully in early 2016
cite:2016PhRvL.116w1101A. The gls:lisa detector will be sensitive in the
milli-hertz region of the abbr:gw spectrum, and will be capable of
observing binary inspirals at a much earlier stage in their evolution
than the advanced ground-based detectors, as well as the galactic
population of low-mass binaries, such as binary white dwarfs. A Japanese
proposal, gls:decigo cite:2011CQGra..28i4011K, would observe in the
decihertz regime using a complex arrangement of six spacecraft in a
star-of-David configuration.

There are also plans for more sensitive detectors on the ground. The
Einstein telescope is a European proposal for an underground
kilometre-scale detector in a triangular configuration, using a
\`\`xylophone'' configuration to improve broadband sensitivity compared
to the second-generation of detectors; its scientific aims include
providing more sensitive tests of abbr:gr than are possible with the
advanced detectors cite:2012CQGra..29l4013S. The prospect also exists
for larger surface-based detectors, such as gls:cosmic-explorer, which
would have an arm-length of 40-km cite:2015PhRvD..91h2001D, initially
using technology currently under development for the upgrade of advanced
gls:ligo, but later incorporating cryogenic technology, such as those
under development for gls:kagra cite:2019arXiv190704833R. There are also
proposals for upgrades of the advanced detectors to use squeezed light
to reduce quantum noise cite:2015PhRvD..91f2005M, the use of speedmeters
cite:2014MUPB...69..519V,2002gr.qc....11088K, or atom interferometry
cite:2013PhRvL.110q1102G,2016PhRvD..93b1101C,2008PhRvD..78l2002D.

At the very low-frequency limit of the abbr:gw spectrum the bulk of
detection efforts are based around pulsar timing arrays, which promise
the detection of abpl:gw by precision measurements of pulse arrival
times from a number of pulsars distributed across the sky. By observing
correlated delays cite:1983ApJ...265L..39H in arrival times the presence
of a very long wavelength abbr:gw can be inferred. There are a number of
collaborations actively producing pulsar observations with the aim of
detecting abpl:gw: the abbr:epta cite:2013CQGra..30v4009K, gls:nanograv
cite:2009arXiv0909.1058J, the abbr:ppta cite:2013PASA...30...17M, and
the abbr:ipta collaboration cite:2013CQGra..30v4010M.

Resonant bar detectors
----------------------

The original abbr:gw detectors developed by Weber in the 1960s were an
early example of a category of detector now known as a *resonant bar*.
These detectors work on the principal that variations in the
gls:riemann-tensor will drive oscillations between two masses. If the
Riemann tensor inside a crystal varies, the stress tensor of the crystal
will also vary, and if the crystal is piezoelectric, this will in turn
produce a change in the polarisation in the material. In Weber's
earliest design cite:PhysRev.117.306 the change in the electric field in
a piezoelectric crystal would be monitored through changes in the
voltage across the crystal with a low-noise radio receiver. Such an
arrangement relied on a single instrument; the rotation of the Earth
would produce a variation in the strength of what was expected to be a
continuous abbr:gw signal measured by the instrument, allowing its
direction to be determined. Alternatively Weber proposed an arrangement
of two instruments with cross-correlated outputs which he imagined would
remove the need for diurnal variation in this process. A major
complication of this approach was the need to have low-noise
amplification of the measured electric field from the crystal, which
Weber had hoped (in 1960) would be realised through the use of masers.
By 1966 Weber's detector, which consisted of an aluminium bar weighing
approximately :math:`\sim \SI{1360}{\kilogram}`, fitted with quartz
piezoelectric strain gauges, was capable of making strain measurements
around :math:`h \sim 10^{-16}`, with the pre-amplifier cooled with
liquid-helium.

The 1990s brought a second generation of resonant detector design, and
an international network of five detectors, which were cooled to
cryogenic temperatures to reduce thermal Nyquist noise within the bar. A
mechanical resonator, which was tuned to a specific frequency was then
attached elastically to one face of the bar. The displacement between
this resonator and the bar face was measured via the capacitance between
the bar face and the secondary resonator. The cryogenic generation of
detectors were capable of reducing the noise strain in the detector to
around :math:`\SI{e-22}{\hertz^{-1/2}}`.

While the sensitivity of bar detectors was much improved over three
decades of development, the narrow bandwidth (around
:math:`\SI{1}{\hertz}` centred around the resonance frequency of the
detector) substantially reduced the quantity of the abbr:gw signal which
can be measured from most plausible astrophysical sources. This has
caused resonant bar technology to struggle to compete with detectors
based around laser interferometry (see section
ref:sec:detectors:interferometric) which typically have bandwidths on
the order of :math:`\SI{e3}{\hertz}`.

Despite this, development of resonant mass antennas is ongoing. In
addition to both gls:nautilus and gls:auriga, there are two spherical
cryogenic detectors, gls:minigrail cite:2007PhRvD..76j2005G, and
gls:mario-schenberg cite:2016BrJPh..46..596O, which hope to be able to
make abb:gw measurements at higher frequencies than the current
generation of interferometric detectors through cooling to
:math:`\SI{50}{\micro\kelvin}`.

Interferometric detectors
-------------------------

Gravitational-wave detectors which use beams of light, such as
interferometers and pulsar timing arrays rely on measuring the the
travel time of a beam of electromagnetic radiation between two points,
and the effect that a abbr:gw has on this time. A full treatment of this
is given in cite:2009LRR....12....2S, but in summary, if a abbr:gw is
not present within a detector, the travel time of a beam in the detector
will be constant. A beam of light is generated at a proper time
:math:`t`, and is received by a sensor at a proper time :math:`\tau`.
With no abbr:gw the proper distance between the two clocks is :math:`L`.
If the beam of light is generated with some sort of time-stamp, then the
receiving sensor can measure the time of arrival of these time-stamps.
If no abbr:gw is present the rate will be constant, and we can choose a
unit of time in which this rate is unity.

If a abbr:gw is introduced, which produces a strain, :math:`h_+(t)`, in
the plane of the beam, the change in the arrival time of the beam will
be changed. If a beam leaves the transmitter at time :math:`t`, when the
abbr:gw strain will be :math:`h(t)`, it is received at a time
:math:`\tau`, when the abbr:gw strain will be
:math:`h(t + (1-\cos(\theta)) L)`, with :math:`\theta` the angle between
the direction of the beam and the direction of abbr:gw propagation. This
means that the arrival rate is changed compared to the emission rate by

.. raw:: latex

   \begin{equation}
       \label{eq:detectors:interferometric:theory:arrival-times-gw}
       \frac{\dd \tau}{\dd t} = 1 + \frac{1}{2} (1 + \cos \theta) \left\{ 
       h_+\left( t + [1- \cos \theta ] L \right) - h_+(\tau) 
         \right\}.
   \end{equation}

By arranging the detector to reflect the beam back to the originating
clock, it is possible to measure the round-trip time using only one
clock. In this arrangement we must account for the abbr:gw having a
different strength one the return trip, and so equation
ref:eq:detectors:interferometric:theory:arrival-times-gw becomes

.. raw:: latex

   \begin{align}
      \label{eq:detectors:interferometric:theory:three-term}   
      \frac{\dd t_{\text{round}}}{\dd t} = 1 + \frac{1}{2} \Big[  (& 1-\cos \theta )h_+ (t+2L) - (1+\cos \theta )h_+(t) \nonumber \\ & + 2 \cos \theta \ h_+ \left(t+L[1 - \cos \theta]\right) \Big],
   \end{align}

which is often called the *three-term* relation.

Operation of a Michelson interferometer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: latex

   \begin{figure}
    \begin{minipage}[c]{0.28\textwidth}
      \begin{tikzpicture}
        \draw [thick, red] (0,0.25) -- (3,0.25);
        \draw [thick, red] (1.1, 0.25) -- (1.1, 2.15);
        \draw [thick, red, dashed] (1.1, 0.25) -- (1.1, -1.0);
        \fill (0,0) rectangle (0.5, 0.5);
        \draw [ultra thick] (0.95, 0.1) -- +(45:.4);
        \draw [ultra thick] (3, 0) rectangle (3.2, .5);
        \draw [ultra thick] (0.8, 2.15) rectangle (1.4, 2.35);
      \end{tikzpicture}
    \end{minipage}
    \begin{minipage}[c]{0.35\textwidth}
      \begin{tikzpicture}
        \draw [ultra thick, red] (0,0.25) -- (3,0.25);
        \draw [ultra thick, red] (1.1, 0.25) -- (1.1, 2.15);
        \draw [ultra thick, red] (-1,0.25) -- (0, 0.25);
        \draw [thick, red, dashed] (1.1, 0.25) -- (1.1, -1.0);
        \fill (-1,0) rectangle (-0.5, 0.5);
        \draw [ultra thick] (0.95, 0.1) -- +(45:.4);
        \draw [ultra thick] (3, 0) rectangle (3.2, .5);
        \draw [ultra thick] (0.8, 2.15) rectangle (1.4, 2.35);
        \draw [ultra thick] (-0.25, 0) rectangle (-0, 0.5);
      \end{tikzpicture}
    \end{minipage}
    \begin{minipage}[c]{0.32\textwidth}
      \begin{tikzpicture}
        \draw [thick, red] (0,0.25) -- (3,0.25);
        \draw [thick, red] (1.1, 0.25) -- (1.1, 2.15);
        \draw [thick, red] (-1,0.25) -- (0, 0.25);
        \draw [thick, red, dashed] (1.1, 0.25) -- (1.1, -1.0);
        \fill (-1,0) rectangle (-0.5, 0.5);
        \draw [ultra thick] (0.95, 0.1) -- +(45:.4);
        \draw [ultra thick] (3, 0) rectangle (3.2, .5);
        \draw [ultra thick] (0.8, 2.15) rectangle (1.4, 2.35);
        \draw [ultra thick] (0.9, -0.5) rectangle (1.3, -0.7);
      \end{tikzpicture}
    \end{minipage}

    \caption[Diagrams of the various components of a dual-recycled cavity-enhanced Michelson interferometer.]{\textbf{Left}: A simple Michelson interferometer, composed of a light source (black box), a beam splitter (heavy black line), and two end mirrors (white boxes). 
    \textbf{Centre}: A Michelson interferometer with an additional power recycling mirror, placed between the beam source and the beam splitter. 
    \textbf{Right}: A Michelson interferometer with a signal recycling mirror, placed between the beam splitter and the output port.  \label{fig:detectors:michelson}}
   \end{figure}

A Michelson interferometer is an optical device which is capable of
measuring the difference in length between two optical paths to
sub-wavelength precision. A Michelson interferometer can be constructed
using a beam splitter and two mirrors, in the configuration presented in
the left panel of figure ref:fig:detectors:michelson. The input beam is
split along the :math:`x` and :math:`y` directions, and reflected back
to the beam splitter. At the beam splitter the two beams will interfere:
in the standard Michelson setup this will result in constructive
interference if the arms have identical lengths, and a beam will be
produced at the output (the dashed red line). If the arms' relative
lengths change a pattern of interference fringes will be visible at the
output of the interferometer.

This means that we can consider an interferometer with two arms to
consist of one arm which acts as the time standard, against which the
variations of the other can be measured. However, such an arrangement
also means that if the effect of a abbr:gw is the same on both arms it
will not be detectable, and will be most detectable if one arm is
extended while the other is contracted by the same amount.

Power recycling
~~~~~~~~~~~~~~~

The optimal signal-to-noise ratio can be achieved from an interferometer
when the arm lengths are configured so that when no abbr:gw is present
in the interferometer the interferometer beams interfere destructively
cite:1978JPhE...11..710E. If the mirrors absorb little energy, the light
will then be reflected back towards the laser, and by placing a mirror
between the laser and the beam splitter a resonant cavity can be formed
(see the middle panel of figure ref:fig:detectors:michelson), allowing
the power in the interferometer to build up. This allows a less powerful
laser to be used as the input for the interferometer, with a laser
capable of providing several kilowatts of power inside the
interferometer cite:2011LRR....14....5P.

Signal recycling
~~~~~~~~~~~~~~~~

Signal recycling can be used to tune the bandwidth of an interferometer,
and to increase its sensitivity by re-injecting the interferometer's
output signal to the interferometer, achieving resonance, which
increases the signal-to-noise ratio of the signal. This is possible
thanks to the sidebands on the beam which are produced by the abbr:gw
not interfering destructively.

To perform signal recycling a mirror is added between the beam splitter
and the readout port of the interferometer
cite:1988PhRvD..38.2317M,2008OExpr..1610018A, with this configuration
illustrated in the right panel of figure ref:fig:detectors:michelson.

Fabry-Perot cavities
~~~~~~~~~~~~~~~~~~~~

For a ground-based interferometer, which has an arm-length of
:math:`4`-kilometres, the light travel time within the arm is of the
order :math:`\SI{E-5}{\second}`. The period of a abbr:gw which the
detector is sensitive to, around :math:`\SI{E-2}{\second}`, is much
greater than this travel time cite:2007QuEle..37.1137T. As a result it
is advantageous to allow the beam to remain within the arm for longer
than one round-trip. By setting the arm up as a cavity the effective
length of the arm can be increased; a finesse of 100 will then increase
the effective length of the arm 100-fold. This in turn increases the
apparent change in the arm length by a factor of 100, and substantially
aids the sensitivity of the detector.

In Advanced gls:ligo, for example, the main arms form a Fabry-Perot
cavity, with a finesse of 450 cite:2015CQGra..32g4001L. This is formed
by placing a mirror between the beam-splitter and the end mirror in each
arm.

Antenna response of the detector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The arrangement described in section
ref:sec:detectors:interferometric:michelson, whereby one arm is used as
the timing reference causes the detector to be incapable of detecting
signals if both arms are affected equally by a abbr:gw. The angle
between the propagation of the abbr:gw and the detector (in addition to
the polarisation of the abbr:gw) will determine the effect on each arm.
This results in an interferometric detector having a varying sensitivity
to sources across the sky, which is conventionally treated as an antenna
pattern, in analogy to the similar concept in radio astronomy. For a
abbr:gw approaching the detector from an azimuth (relative to one of the
arms) and altitude (relative to the plane of the detector),
:math:`(\alpha, \delta)` on the sky these patterns for the :math:`+`-
and :math:`\times`-polarisations, :math:`F_{+}` and :math:`F_{\times}`,
will be

.. raw:: latex

   \begin{align}
       \label{eq:detectors:antennapattern:plus}
       F_{+} &= \frac{1}{2} (1 + \sin^{2}\delta) \cos 2\alpha \cos 2\psi - \sin\delta\sin 2 \alpha \sin 2 \psi \\
       F_{\times} &=  \frac{1}{2} (1 + \sin^{2}\delta) \cos 2\phi \sin 2\psi - \sin\delta\sin 2 \phi \cos 2 \psi 
   \end{align}

for :math:`\psi` the polarisation angle of the abbr:gw, which
corresponds to the rotation of the basis vectors defining the
polarisations of the abbr:gw compared to the detector
cite:2009LRR....12....2S. The :math:`+`-polarised response is plotted in
figure ref:fig:detectors:interferometers:antennapattern, which clearly
depicts the four regions of low sensitivity.

.. raw:: latex

   \begin{figure}
       \includegraphics{figures/intro/aligo-antenna-pattern.pdf}
       \caption[The antenna pattern for an interferometric abbr:gw detector.]
       {The normalised antenna pattern, in response to $+$-polarised abpl:gw, of a signle two-armed interferometric detector with a $90^{\circ}$ arm separation, with axes in the $x$-$y$ plane.
       Here the azimuth positions assume that one of the arms is oriented north-to-south (along the $y$-axis) and the other east-to-west (along the $x$-axis); an appropriate rotation should be added to account for alternative orientations.
       \label{fig:detectors:interferometers:antennapattern}}
   \end{figure}

The overall measured strain, :math:`h(t)` in a detector from a abbr:gw
with components :math:`(h_{+}, h_{\times})` will then be

.. raw:: latex

   \begin{equation}
       \label{eq:detectors:interferometers:measuredstrain}
       h(t) = F_{+}(t) h_{+}(t) + F_{\times} (t) h_{\times}(t)
   \end{equation}

While this antenna pattern has the effect of reducing the sensitivity of
the detector to some areas of the sky, it provides additional
information relating to the direction of the abbr:gw. This information
can be utilised if a network of detectors is available, as if a signal
is detected in similar detectors located elsewhere, but not (or barely)
detected by another, it may be possible to infer that the signal
originated in the direction of the one of the non-detecting detector's
\`\`blind spots''. Such an inference was valuable in the localisation of
the source of gls:gw170817 cite:2017PhRvL.119p1101A, which had a
noticeably weak signal in the gls:virgo detector.

Localising a gravitational wave signal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a network of at least two geographically separated detectors observes
a signal it is possible to ascertain the location in the sky,
:math:`\hat{\vec{\Omega}}`, from the difference in arrival times between
the two sites. For a detector at a position, :math:`\vec{r}_{D}`, and an
arbitrary reference location, :math:`\vec{r}_{0}`, this time delay,
:math:`\delta t`, will be

.. raw:: latex

   \begin{equation}
       \label{eq:intro:detectors:timedelay}
       \delta t (\hat{\vec{\Omega}}) = \frac{1}{c} (\vec{r}_{0} - \vec{r}_{D}) \cdot \hat{\vec{\Omega}}
   \end{equation}

This allows the location of the signal to be confined to a ring on the
sky corresponding to constant :math:`\Delta t`. Timing uncertainty in
the signal, which arises both from clock uncertainties and uncertainties
in defining a reference point in the received signal increase the area
of this region. As more detectors are added to the network it is
possible to reduce this area, as increasing the number of detector pairs
works to reduce the sky area compatible with the observed delay times.

Additional localisation information can be attained from the observed
amplitude of the signal in each detector. The signal will be convolved
with the antenna pattern (see section
ref:sec:detectors:antennaresponse); as each detector is insensitive to
some regions of the sky, the total plausible localisation of the signal
is reduced.

Ground-based interferometers
----------------------------

While there are attractions to being able to place an interferometric
abbr:gw observatory in space, practical concerns have so-far constrained
these detectors to being placed on the ground (or, in the case of
gls:kagra, under it). Fortunately, a considerable amount of science is
possible with ground-based detectors, within the acoustic band of
frequencies (above around 10-hertz). As a result considerable effort has
been put into the development of detectors which can overcome the noisy
environment which these detectors experience, which has so-far
culminated in the construction of the advanced gls:ligo observatories,
and the advanced gls:virgo observatory. In the near future these are
likely to be joined by gls:kagra and an additional gls:ligo detector in
India.

Future developments in ground-based interferometry are likely to force
the detectors underground in order to mitigate seismic and Newtonian
noise (see section ref:sec:detectors:noise); gls:kagra has already been
located in a mine, while a plan for a future subterranean detector is
the gls:einstein-telescope.

Advanced LIGO
~~~~~~~~~~~~~

The Advanced gls:ligo detectors are considered second-generation
interferometric abbr:gw detectors, located at two observatories in the
United States of America. gls:llo is located in woodland outside the
town of Livinston in Louisiana, while gls:lho is located on the Hanford
Reservation in the State of Washington.

The advanced gls:ligo detectors replaced the first-generation Initial
gls:ligo detectors, and share the same facilities as their
predecessors [7]_, and like them are 4-kilometre long interferometers
with a gls:fabry-perot-cavity in each arm, with a finesse of 450. The
detectors improve their sensitivity compared to the initial generation
detectors through the use of signal recycling, a technology pioneered in
the gls:geo600 detector, and have quadruple mirror suspensions which use
fused silica fibres to provide seismic islolation
cite:2002CQGra..19.4043R,2012CQGra..29w5004A. Combined, the improvements
to the design of the detectors allowed a ten-fold improvement in
sensitivity in the most sensitive frequency region (around
:math:`\SI{100}{\hertz}`) compared to the initial gls:ligo detectors, as
can be seen in the difference between the sensitivity curves in figures
fig:detectors:interferometers:firstgen and fig:detectors:aligo-asd.

The first continuous observations with the advanced detectors started in
September 2015. During the first observing run [8]_ the detectors made
three detections of coalescing abbr:bbh.

.. raw:: latex

   \begin{table}
   \centering
   \begin{tabular}{ll}
   \toprule
    Parameter        & Value                   \\
   \midrule
   Arm length       & $\SI{3994.5}{\meter}$   \\
   Arm finesse      & $\SI{450}{}$            \\
   Laser wavelength & $\SI{1064}{\nano\meter}$ \\
   Input power      & $\SI{125}{\watt}$       \\
   Test-mass mass   & $\SI{40}{\kilogram}$     \\
   \bottomrule
   \end{tabular}
   \caption{The basic parameters of the advanced \gls{ligo} detectors, from \cite{2015CQGra..32g4001L}.
   \label{tab:detectors:aligo-parameters}}
   \end{table}

Advanced Virgo
~~~~~~~~~~~~~~

Similarly to advanced gls:ligo, the advanced gls:virgo detector is a
second-generation interferometric detector which replaced a
first-generation detector. Located in Cascina, Italy, this detector has
a number of design choices which are distinct compared to the gls:ligo
detectors, choosing, for example to use \`\`super attenuators'' rather
than the quadruple suspension system of gls:ligo to provide seismic
isolation. Additionally, the detector's arm cavities are shorter than
those of advanced gls:ligo, extending 3-kilometres compared to
gls:ligo's four.

Kagra
~~~~~

The final \`\`advanced era'' detector design which is under development
is that of gls:kagra (previously known under the moniker abbr:lcgt)
cite:2018arXiv181108079A. abbr:kagra has claim to bridge the
technological divide between the second and third generation of abbr:gw
detectors, as it is expected to be the first interferometric detector to
employ cryogenic technology. The use of cryogenically-cooled mirrors is
designed to reduce thermal noise originating in the mirror coatings (see
ref:sec:detectors:noise:thermal), but presents a number of technological
challenges which ambient-temperature detectors avoid. Additionally, in
contrast to gls:ligo and gls:virgo, gls:kagra will be located
underground (in a disused part of the Kamioka mine complex). This
principle is expected to be used for the gls:einstein-telescope, and
reduces the impact of some forms of Newtonian noise (see section
ref:sec:detectors:noise:newtonian) on the detector, and thus improves
its low-frequency sensitivity. Unlike planned third-generation
detectors, however, gls:kagra will have an arm length of 3-km, around an
order of magnitude smaller than future subterranean detectors are
anticipated to be.

Einstein Telescope and Cosmic Explorer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The two plans for third-generation detectors which are currently under
consideration are gls:cosmic-explorer, which is likely to be located in
the USA, and gls:einstein-telescope, likely to be located in Europe. A
number of technological advances are anticipated which will allow a
considerable increase in sensitivity over the current generation of
detectors, in addition to increased arm cavity lengths (40-kilometres in
the case of gls:cosmic-explorer, and 30-kilometres for
gls:einstein-telescope). The sensitivity improvements in this generation
of detectors should allow the detection of abbr:cbc events to very high
(:math:`z>10`) redshifts at high abbr:snr
cite:detectors.thirdgen.cosmicexplorer.sensitivity. In addition to
having longer arm cavities than current detectors,
gls:einstein-telescope will be placed underground in an attempt to
mitigate Newtonian noise (see section
ref:sec:detectors:noise:newtonian).

Space-based interferometers
---------------------------

While ground-based interferometers have the advantage of accessibility,
and consequently fairly affordable construction costs, great advantage
is to be had in placing an interferometer in space. Some noise sources
which detectors such as abbr:ligo must contend with, such as seismic
noise, are completely absent, and greater freedom is afforded in the
size of the interferometer, with the absence of a need to purchase and
prepare land for the observatory. In exchange for these advantages
space-based interferometers present a number of technological hurdles,
such as maintaining sufficiently stable orbital configuration to allow
interferometry to be carried-out, and reduced sensitivity, as
constructing a Fabry-Perot cavity in the comparatively poor vacuum
around the L1 point is not feasible.

Despite these difficulties, space-based detectors represent the majority
of feasible concepts for detectors sensitive to low frequency emission.
The following sections contain further details of the gls:lisa and
gls:decigo mission proposals, but numerous other proposals for
space-based detectors exist, including gls:glisa
cite:\ doi:10.1063/1.4904862,glisaorbit, which proposes using
off-the-shelf satellites to form a detector constellation in
geostationary (rather than heliocentric) orbit. The gls:tianqin mission
proposal cite:2016CQGra..33c5010L also uses such a technique, with the
aim to have a shorter development time than rival concepts such as
gls:lisa.

Laser Interferometer Space Antenna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: latex

   \begin{figure}
    \includegraphics{figures/intro/space-asd.pdf}
    \caption[The noise curves for LISA and DECIGO]{The abbr:asd of the gls:lisa and gls:decigo detectors within their sensitive band, at design sensitivity. The curve for gls:lisa is based on the prediction outlined in~\cite{2019CQGra..36j5011R}, while the gls:decigo curve is based on the approach in~\cite{2011PhRvD..83d4011Y}.
    \label{fig:detectors:space}
    }
   \end{figure}

Abbr:lisa is a planned space-based abbr:gw observatory, under
development by the European Space Agency, which would be placed in a
heliocentric orbit at the L1 Lagrange point. In comparison to the
kilometre-scale arms of second-generation ground-based detectors such as
abbr:ligo, abbr:lisa is proposed to have arms which are 2.5 million
kilometres long, giving the detector much greater sensitivity at low
frequencies than is possible with ground-based detectors. The abbr:asd
of abbr:lisa is plotted in figure ref:fig:detectors:space.

The abbr:lisa mission was preceeded by abbr:lisa Pathfinder, a
technology demonstration mission, launched in December 2015.

DECIGO
~~~~~~

gls:decigo cite:2011CQGra..28i4011K is a proposed space-based abbr:gw
observatory which is designed to observe the deci-hertz abbr:gw regime.
Ground-based detectors are sensitive to frequencies above around
:math:`\SI{10}{\hertz}`, and the gls:lisa mission is designed to observe
frequencies below :math:`\SI{1}{\hertz}`. This leaves a region which is
unobserved, centred approximately around :math:`\SI{10}{\hertz}`, which
overlaps with less sensitive regions of the gls:lisa and ground-based
detectors passbands. The abbr:asd of gls:decigo is plotted in figure
ref:fig:detectors:space.

A gls:decigo cluster will consist of three spacecraft in a triangular
configuration, forming three gls:fabry-perot-cavity cavities with
lengths around :math:`\SI{1000}{\kilo\meter}`. Four of these clusters,
placed in heliocentric orbits, will form the entire observatory
constellation, with two of the clusters arranged in a nearly-overlapping
\`\`Star-of-David'' geometrical configuration cite:2017JPhCS.840a2010S.

Pulsar timing
-------------

Pulsar timing relies on observations made of the arrival times of pulses
from millisecond pulsars. In comparison to an interferometer, where the
measurement of the detector's arm is made by observing the phase of the
laser beam over a scale of a few kilometres (in the case of a
ground-based detector such as gls:ligo), or even a few gigametres (in
the case of gls:lisa), pulsar timing arrays provide an arm length on the
scale of parsecs. Accordingly, they are sensitive to much lower
frequencies than man-made detectors.

If a pulsar is treated as a clock which produces pulses at predictable
intervals, any discrepancy between the predicted arrival time and the
observed arrival time may be attributed to some effect along the line of
sight. The phase, :math:`\phi`, of the signal from a pulsar which has a
rotation frequency and phase at a time, :math:`t_{0}`, of respectively
:math:`\nu_{0}` and :math:`\phi_{0}`, and a spin-down rate,
:math:`\dot{\nu}`, can be found as

.. raw:: latex

   \begin{equation}
    \label{eq:pulsar-phase}
    \phi = \phi_{0} + \nu_{0}(t-t_{0}) + \frac{1}{2} \dot{\nu} (t-t_{0})^{2},
   \end{equation}

at time :math:`t`. By setting the observational epoch to begin with the
first observation (so that :math:`t_{0}` = 0), the time of arrival,
:math:`t` of the :math:`N`-th can be related as

.. raw:: latex

   \begin{equation}
    \label{eq:pulsar-toa}
    N = \nu_{0} t + \frac{1}{2} \dot{\nu} t^{2} + \epsilon,
   \end{equation}

for :math:`\epsilon` a noise term which results from any effects along
the line of sight.

The effect of a abbr:gw on the arrival time of a specific phase can be
found from equation
ref:eq:detectors:interferometric:theory:arrival-times-gw; the presence
of a abbr:gw along the line of sight between the pulsar and the observer
(conventionally located at solar system barycentre to remove various
timing effects related to the movement of the Earth in the solar system)
will be seen in the amplitude of the :math:`\epsilon` term of equation
ref:eq:pulsar-toa. abpl:gw are not the only potential source of
additional \`\`timing noise'' however, as any variation in the
gravitational field in the vicinity of either the pulsar or the observer
will contribute to variation in :math:`\epsilon`. In order to detect
abpl:gw it is therefore necessary to observe a number of pulsars, and
compare correlations in the :math:`\epsilon` data (known as \`\`timing
residuals'') for each of them.

The correlation between pulsars is dependent upon their angular
separation, :math:`\zeta`, in the sky cite:1983ApJ...265L..39H, and
given by the \`\`Hellings-Downs curve'', which provides the sky- and
polarisation-averaged response of a pair of pulsar lines-of-sight to a
plane abbr:gw, and has analytical form

.. raw:: latex

   \begin{equation}
    \label{eq:hellings-downs}
    \chi(\zeta) = \frac{1}{2} - \frac{1}{4} \left( \frac{1 - \cos\zeta}{2} \right) + \frac{3}{2} \left(\frac{1 - \cos\zeta}{2} \right) \log \left(\frac{1-\cos\zeta}{2}\right),
   \end{equation}

for :math:`\zeta` the angular separation of the Earth-pulsar baselines
for each pulsar. This relationship is plotted in figure
ref:fig:intro:detectors:hellingsdowns.

.. raw:: latex

   \begin{figure}
   \includegraphics{./figures/intro/hellings-downs.pdf}
   \caption[The Hellings and Downs curve]{The Hellings and Downs curve giving the expected correlation between a pair of Earth-pulsar baselines with a given angular separation.}
   \label{fig:intro:detectors:hellingsdowns}
   \end{figure}

In the case of a pulsar timing array there will be numerous pulsars; the
Hellings-Downs correlations for each can be calculated as a pairwise
matrix, :math:`\chi_{ij} = \chi(\zeta_{ij})` for :math:`\zeta_{ij}` the
angular separation between pulsars :math:`i` and :math:`j` within the
array of :math:`M` pulsars, with :math:`i, j \in {1, ..., M}`. These
correlations, along with the timing noise of each pulsar, can be used to
construct the abbr:psd of the array.

Other approaches
----------------

A number of other techniques have been used to place limits on various
forms of abbr:gw emission, including Doppler ranging of spacecraft
cite:Armstrong2006, astrometry using GAIA observations
cite:2018CQGra..35d5005K, the measurement of the Earth's normal modes
cite:2014PhRvD..90d2005C. Proposals for alternatives to light-based
interferometry also exist in the form of atom interferometers
cite:2017ogw..book..285G,2018CoTPh..69...37G.

Noise sources
=============

Given the small strain amplitudes of abpl:gw, and the correspondingly
small displacements they produce in a detector, the detector data is
normally dominated by noise. This noise limits the range over which a
detector is sensitive to abpl:gw, so understanding the sources of noise,
and mitigating them is the most effective means of improving their
sensitivity to astrophysical sources.

Noise sources are split broadly into two categories: instrumental
sources, and facilities source. The former includes noise sources which
are due to the equipment used to construct the detector, the latter are
a result of physical properties of the observatory's site and
infrastructure.

Quantum noise
-------------

.. raw:: latex

   \begin{figure}
      \includegraphics{./figures/intro/quantum-noise.pdf}
      \caption[Quantum noise in Advanced LIGO]{The contribution to the advanced gls:ligo abbr:asd from quantum noise. These curves were calculated using the \texttt{pygwinc} library \cite{pygwinc}.}
      \label{fig:detectors:noise:quantum}
   \end{figure}

One of the major sources of instrumental noise in detectors such as
advanced gls:ligo is from quantum fluctuations in the intensity of the
photon field in the detector arms. This manifests itself through two
processes. The first is as radiation pressure noise; a change in the
photon flux reflecting off the mirror will lead to a fluctuation in the
radiation pressure exerted on the mirror (and hence the test mass). The
abbr:psd of this noise, given a power :math:`P` circulating in the arm
cavities, with a wavelength :math:`\lambda`, and with the mass of the
test mass :math:`m` is

.. math::

   \begin{equation}
   \label{eq:intro:noise:radpressure}
   S(f) = \frac{1}{m f^{2} L} \sqrt{ \frac{ \hbar P }{ 2 \pi^{3} c \lambda} },
   \end{equation}

at a given frequency :math:`f` (with :math:`\hbar` the reduced Planck
constant), for a detector with arm-length :math:`L`
:raw-latex:`\cite{2011LRR....14....5P}`.

Radiation pressure can be mitigated by increasing the power circulating
in the arms, however this must be balanced against the increased shot
noise introduced by the increased power.

Shot noise results from quantum fluctuations in the photodiode which
measures the output signal from the interferometer. For the same
interferometer properties listed for the radiation pressure noise in
equation ref:eq:intro:noise:radpressure this is

.. raw:: latex

   \begin{equation}
   \label{eq:intro:noise:shotnoise}
   S(f) = \frac{1}{L} \sqrt{ \frac{  \hbar c \lambda }{2 \pi P} }.
   \end{equation}

As a result increasing the laser power will increase the shot noise at
high frequencies.

The combined quantum noise for advanced gls:ligo is shown, alongside the
total noise budget of the detector in figure
ref:fig:detectors:noise:quantum.

Thermal noise
~~~~~~~~~~~~~

Thermal noise primarily affects the low-frequency sensitivity of a
ground-based interferometer. This noise source is a result of the
thermal vibration of both the mirror suspensions and coatings.

The estimated abbr:psd of thermal noise contributions from the
suspensions and mirror coatings in the advanced gls:ligo detectors is
plotted in figure ref:fig:detectors:noise:thermal. The behaviour of the
abbr:psd for the suspension has noticeable structure, with numerous
peaks arising from upconversion of the resonant frequency of the
suspension into higher harmonics.

.. raw:: latex

   \begin{figure}
       \includegraphics{./figures/intro/thermal-noise.pdf}
       \caption[Thermal noise in Advanced LIGO]{The contribution to the advanced gls:ligo abbr:psd from thermal noise. These curves were calculated using the \texttt{pygwinc} library \cite{pygwinc}.}
       \label{fig:detectors:noise:thermal}
   \end{figure}

Seismic noise
~~~~~~~~~~~~~

Seismic noise is the result of strain introduced into the interferometer
through movement of the ground, which can be the result of geophysical
activity, tidal activity, or anthropogenic sources of seismic noise,
such as road traffic or railways. In a seismically quiet location the
spectrum of seismic noise follows the relation cite:2011LRR....14....5P

.. raw:: latex

   \begin{equation}
   \label{eq:detectors:noise:seismic:spectrum}
   s(f) \approx 10^{-7} f^{-2}\, \si{\meter\per\square\hertz},
   \end{equation}

for a frequency :math:`f`.

However, the seismic environment of the detector can have a considerable
effect on this noise source. Consequently, of the important
considerations in choosing a site for an interferometer is the presence
of seismic noise, and for this reason they are normally located far from
urban areas. Table ref:tab:detectors:noise:seismic summarises the
approximate frequency ranges for various sources of seismic noise, and
the approximate distance range over which these sources affect an
interferometer. Despite this, both of the Advanced LIGO sites are
affected by the presence of loud anthropogenic noise sources (gls:lho is
affected by a nearby Department of Energy site; gls:llo is affected by
logging activity and a nearby railway track) cite:2004CQGra..21.2255D.
gls:llo is also strongly affected by severe storms due to its proximity
to the Gulf of Mexico, especially in the microseismic band.

.. raw:: latex

   \begin{table}
   \centering
   \begin{tabular}{rrl}
   \toprule
   $f$ / Hz    & $D$ / km   & Sources                                   \\
   \midrule 
   0.01--1.0   & 1000       & Earthquakes, microseism                   \\
   1--3        & 10         & Anthropogenic, nearby earthquakes, wind   \\
   3--10       & 1          & Anthropogenic, wind                       \\
   10--100     & 0.1        & Nearby Anthropogenic noise                \\
   \bottomrule
   \end{tabular}
   \caption[Seismic noise frequency bands for ground-based detectors.]{The principle seismic noise frequency bands, $f$, which affect ground-based detectors, their sources, and the distance, $D$, over which the band affects advanced-generation detectors. \label{tab:detectors:noise:seismic}}
   \end{table}

Seismic noise limits the sensitivity of the second generation detectors
at low frequencies (:math:`f < \SI{50}{\hertz}`), but it is present as a
noise source across the passband of the detector. The seismic noise
contains a pair of notable peaks below the :math:`\SI{1}{\hertz}` level,
one caused by ocean swell, which has a period around 4 to 30 seconds,
and a second caused by standing seismic modes in the Earth which spans
the range of 30 to 1000 seconds. The presence of seismic noise below
:math:`\SI{30}{\hertz}` is still problematic for ground-based
interferometers, depsite this being outside the design frequency range,
due to *upconversion*, where low-frequency noise couples non-linearly
into higher frequency noise.

Seismic isolation is used in detectors to reduce the noise level due to
seismic activity. This takes two forms: active isolation, and passive
isolation. The former is accomplished by mounting optical components on
hydraulic pre-isolator systems which are controlled, via a feed-forward
system, by the measurements of a seismometer. The latter is reduced by
suspending the optics as a component in a pendulum system. Above the
resonance of a single-stage pendulum the transfer of horizontal motion
falls off as :math:`1/f`, and vertical motion can be reduced by
suspending the pendulum on a spring.

Advanced gls:ligo makes use of a four-stage suspension system to reduce
the movement of the test mass, with the test mass forming the second
stage of a two-stage pendulum which is itself suspended off two stages
of cantilevered steel blades. This entire suspension system for each
optic (and indeed, the entire vacuum tank containing the suspension) is
placed on an isolator platform. The suspension system of gls:virgo
follows similar principles, but involves seven stages of vertical
suspension to form its super attenuators.

Seismic noise is also a source of Newtonian noise (see section
ref:sec:detectors:noise:newtonian) due to local mass density
fluctuations as the seismic wave passes through the ground. Both the
abbr:psd of seismic and Newtonian noise are plotted in figure
ref:fig:detectors:noise:gravity for the advanced gls:ligo detectors.

Newtonian Noise
~~~~~~~~~~~~~~~

Newtonian noise, or gravitational gradient noise, is the strain produced
by gravitational coupling between local mass density variations and the
test masses in the interferometer. The major source of such noise comes
from density fluctuations in the material surrounding the test mass, the
ground below the detector. Seismic waves, especially surface waves, can
produce measurable density changes which in turn affect the strength of
the gravity field local to the test mass.

The spectrum of this noise is given by cite:1998PhRvD..58l2002H as

.. raw:: latex

   \begin{equation}
   \label{eq:detectors:noise:newtonian:spectrum}
    s(f) = \begin{cases} 
              \frac{\beta}{0.6} \frac{6\ee{-23}}{\sqrt{\si{\hertz}}} \left( \frac{\SI{10}{\hertz}}{f} \right)^{2} & \SI{3}{\hertz} \lesssim f < \SI{10}{\hertz} \\
          \frac{\beta}{0.6} \frac{6\ee{-23}}{\sqrt{\si{\hertz}}} \left( \frac{\SI{10}{\hertz}}{f} \right)^{4} & \SI{10}{\hertz} \lesssim f < \SI{30}{\hertz} 
   \end{cases}
   \end{equation}

where the :math:`\beta` factor is site-dependent, estimated at quiet
times to be :math:`0.35` to :math:`0.45` at gls:llo, and :math:`0.35` to
:math:`0.60` at gls:lho.

While variations in the density of the ground are the major contribution
to Newtonian noise, atmospheric and surface effects also impact the
detector sensitivity. These can include the movement of clouds and
aircraft in the vicinity of the detector.

.. raw:: latex

   \begin{figure}
       \includegraphics{./figures/intro/gravity-noise.pdf}
       \caption[Seismic and Newtonian noise in advanced LIGO]{The contribution to the advanced gls:ligo abbr:psd from seismic and Newtonian noise. These curves were calculated using the \texttt{pygwinc} library \cite{pygwinc}.}
       \label{fig:detectors:noise:gravity}
   \end{figure}

Glitches
--------

In addition to the sources of instrumental noise which are continuously
present in interferometer data, the advanced era detectors suffer from
transient non-Gaussian noise events which are known as gls:glitch
events. These can be caused by environmental phenomena, such as
lightning strikes in the vicinity of the detector, or due to
instrumental effects, such as fluctuations in laser power, or
reflections within the beam tube. Due to their transient nature these
noise events are a particular difficulty for data analysis techniques
designed to identify signals from both abbr:cbc systems and so-called
\`\`burst'' events (discussed in section ref:sec:sources:burst). There
are two major ways of addressing this problem: identifying the cause of
the gls:glitch, and making changes to the detector to reduce or
eliminate their occurrence; or to produce a *veto*, a specific datum
which identifies time periods where glitching is likely due to a
combination of measurements from other data sources.

In order to identify the cause of any given glitch it is normally
necessary to classify it; different glitch-causing phenomena will
produce events with specific time-frequency morphologies. When a number
of similar glitches are identified it may be possible to infer their
cause with reference to the numerous sensors which monitor each detector
and its site (these number on the order of :math:`10^{5}` for each
advanced gls:ligo detector). Attempts to perform this classification
using a combination of human volunteers and machine learning techniques
have been fruitful to date through the *GravitySpy* project
cite:2017CQGra..34f4003Z. Once the cause is understood either detector
alteration can be planned, or a veto can be constructed with reference
to data channels which *witness* the phenomena correlated with glitch
production.

A network of detectors
======================

.. raw:: latex

   \begin{figure}
   \includegraphics{figures/intro/gw-spectrum.pdf}
   \caption[The spectrum coverage of a range of current and future gravitational wave detectors.]{The gravitational wave spectrum, with a number of current and future detectors' sensitivity curves overlaid.
   The background colours show the regime in which each region of the spectrum can be observed, with green being the frequencies where pulsar timing is necessary, blue where space-based interferometry may be used, and pink where ground-based interferometry is currently used.
   }
   \label{fig:intro:network:spectrum}
   \end{figure}

Generally, in order to make a confident detection of a abbr:gw the event
must be observed in at least two detectors; this is principally due to
the need to exclude noise sources as the source of the signal. A true
abbr:gw event should be coincident (within the wave travel-time between
any pair of detectors) in two or more detectors, whereas locally
produced noise will appear only in the observations of a single
detector, or with a time-lag which is not physically consistent with a
abbr:gw. The largely omnidirectional sensitivity of interferometric
detectors further motivates the need for multiple detectors which can be
used to triangulate the source of the signal in the sky.

At the time of writing the world-wide network of abbr:gw detectors was
made-up of four interferometric detectors: the gls:geo600 detector in
Germany, the advanced gls:virgo detector in Italy, and two advanced
gls:ligo detectors, located in the USA states of Washington and
Louisiana. The normal operation of the network omits the less sensitive
gls:geo600 detector, and is capable of operating as a network containing
all three detectors, or two detectors during periods of time where one
detector is not observing.

Additional detectors are currently either being planned or are under
construction which will see an increase both in the number of detectors
and their geographical spread. Such an increased network should provide
both an increased duty cycle (leading to a decrease in the total time
when no observations are being made), and improved sky-localisation
capability (improving the prospects of successful electromagnetic
follow-up of abbr:gw events).

In addition to adding to the network of terrestrial detectors working in
high frequencies, figure ref:fig:intro:network:spectrum demonstrates the
need for detectors, such as gls:lisa and gls:decigo to be placed in
space in order to observe at lower frequencies than is possible on the
Earth with detectors such as advanced gls:ligo, in addition to the
development of pulsar timing arrays to make abbr:gw observations at
extremely low frequencies.

Gravitational wave detections
=============================

Having discussed the means by which abpl:gw may be detected, it would be
remiss not to discuss the detections which occurred during the first two
observing runs of the advanced detector era.

Observing run 1 and GW150914
----------------------------

.. raw:: latex

   \begin{figure}
    \label{fig:gw:gw150914}
    \includegraphics{figures/intro/gw150914-waveform.pdf}
    \caption[The data containing GW150914 from the two Advanced LIGO detectors.]{The data from the advanced gls:ligo detectors at the Livingston (L1) and Hanford (H1) observatories, which has been band-passed between $\SI{50}{\hertz}$ and $\SI{250}{\hertz}$, and a comb filter has been applied to remove the $\SI{60}{\hertz}$ line and its higher harmonics.
    The data from the Livingston detector has had a time-delay filter applied to introduce a $\SI{6.9}{\milli\second}$ delay, representing the travel time between the detectors, and has been inverted to account for the relative orientation of the two detectors.
   This plot was produced using the \texttt{gwpy} library~\cite{gwpy0d14d2}.
    }
   \end{figure}

The first detection of abpl:gw was made on 14 September 2015 by the
Advanced abbr:ligo detectors cite:2016PhRvL.116f1102A when a signal from
a abbr:bbh coalescence was detected, first by the abbr:cwb burst search
pipeline (which is discussed briefly in section
ref:sec:sources:burst:pipelines), and subsequently by a number of
matched-filtering pipelines designed for abbr:cbc detection.
gls:gw150914 was remarkable not only for being the first viable trigger
to be detected by advanced gls:ligo, but also for having sufficiently
high statistical significance (with a false alarm rate less than
1-in-\ :math:`203\,000` years) that there was no reasonable doubt that
it constituted a genuine abbr:gw detection; indeed, as can be seen in
figure ref:fig:gw:gw150914, the signal can be seen clearly in the
whitened data without the use of matched filtering.

The detection was made at both the gls:llo and gls:lho observatories,
with a joint abbr:snr of around :math:`24`. The event itself, a gls:bbh
coalescence between a :math:`36^{+5}_{-4} \msolar` black hole and a
:math:`29^{+4}_{-4} \msolar` black hole was unexpected. Observations of
black hole binaries in x-ray had not previously suggested that
stellar-mass black holes this massive would exist. As a result models of
stellar formation struggled to explain the evolution of black holes with
these masses cite:2016ApJ...818L..22A.

Two further abbr:bbh events were observed in the first observing run.
gls:gw151012, (the \`\`second Monday event''), was initially announced
as a candidate event, as it failed to exceed the :math:`5\sigma`
significance threshold which was set for events prior to the publication
of the ``GWTC-1`` catalogue cite:2018arXiv181112907T. The more
significant gls:gw151226 (the \`\`Boxing Day event'') was the second
confirmed detection from the advanced gls:ligo detectors, corresponding
to a merger between much less massive black holes than gls:gw150914
(around 14 and 8 solar masses). Unlike the first detection, gls:gw151226
may have involved an asymmetrical system, with one black hole about
twice as massive as the other. The lower masses resulted in a
substantially greater amount of the inspiral waveform being in-band for
the detectors, and consequently was capable of providing more stringent
tests on abbr:gr than its predecessor cite:2016PhRvL.116x1103A.

Observing run 2 and GW170817
----------------------------

The second advanced gls:ligo observing run (O2) started on 30 November
2016, and finished on 25 August 2017. The advanced gls:virgo detector
joined the run on 1 August 2017, allowing three-detector observations
from kilometre-scale detectors for the first time in the advanced era.
Nine detections were made during O2. These are summarised in table
ref:tab:eventlist. Of these, eight were abbr:bbh events, and one was a
gls:bns event. The most important observation to be made during this run
was of gls:gw170817, the first detection of a binary neutron star
coalescence. This event, which occurred on 17 August, was the second
three-detector event (preceded only by gls:gw170814 three days earlier),
which left the community in the serendipitous situation of being able to
determine the location in the sky from which the abbr:gw originated to
much greater precision than previous two-detector events.

The detection of gls:gw170817 cite:2017PhRvL.119p1101A was coincident
with the detection of a short gamma ray burst by the Fermi spacecraft
cite:gw170817.fermi.gbm.gcn. This parallel detection of the event made
gls:gw170817 / GRB170817A the first multi-messenger abbr:gw event.
Within hours of the publication of the gls:ligo / gls:virgo sky
localisation an optical counterpart to the event was identified in NGC
4993 by the SWOPE Supernova Survey cite:2017Sci...358.1556C, gaining the
designation AT2017gfo. The optical emission was later followed by
observation of emission across the electromagnetic spectrum, including
the observation of optical and ultra-violet emission (a kilonova) from
the event cite:2017ApJ...848L..12A.

.. raw:: latex

   \begin{landscape}
   \begin{table}
   \begin{tabular}{lllllllllll}
   \toprule
               & $E_{\text{rad}}$    & $L_{\text{peak}}$   & $a_{\text{final}}$     & $\chi_{\text{eff}}$     & $D_{\text{L}}$                          & $M_{1}$                & $M_{2}$               & $\mathcal{M}$        & $M_{\text{rem}}$       & $z$                    \\ 
               & $/\solMass$    & $/\SI{E56}{erg \per \second}$ &   &    & $/\SI{}{\mega\parsec}$                          & $/\solMass$                & $/\solMass$               & $/\solMass$        & $/\solMass$       &                     \\ 
   \midrule
      GW150914 & $3.1^{+0.4}_{-0.4}$ & $3.6^{+0.4}_{-0.4}$ & $0.69^{+0.05}_{-0.04}$ & $-0.01^{+0.12}_{-0.13}$ & $430.0^{+150.0}_{-170.0}$    & $35.6^{+4.8}_{-3.0}$   & $30.6^{+3.0}_{-4.4}$  & $28.6^{+1.6}_{-1.5}$ & $63.1^{+3.3}_{-3.0}$   & $0.09^{+0.03}_{-0.03}$ \\
     GW151012  & $1.5^{+0.5}_{-0.5}$ & $3.2^{+0.8}_{-1.7}$ & $0.67^{+0.13}_{-0.11}$ & $0.04^{+0.28}_{-0.19}$  & $1060.0^{+540.0}_{-480.0}$   & $23.3^{+14.0}_{-5.5}$  & $13.6^{+4.1}_{-4.8}$  & $15.2^{+2.0}_{-1.1}$ & $35.7^{+9.9}_{-3.8}$   & $0.21^{+0.09}_{-0.09}$ \\
     GW151226  & $1.0^{+0.1}_{-0.2}$ & $3.4^{+0.7}_{-1.7}$ & $0.74^{+0.07}_{-0.05}$ & $0.18^{+0.2}_{-0.12}$   & $440.0^{+180.0}_{-190.0}$    & $13.7^{+8.8}_{-3.2}$   & $7.7^{+2.2}_{-2.6}$   & $8.9^{+0.3}_{-0.3}$  & $20.5^{+6.4}_{-1.5}$   & $0.09^{+0.04}_{-0.04}$ \\
     \midrule   
     GW170104  & $2.2^{+0.5}_{-0.5}$ & $3.3^{+0.6}_{-0.9}$ & $0.66^{+0.08}_{-0.1}$  & $-0.04^{+0.17}_{-0.2}$  & $960.0^{+430.0}_{-410.0}$    & $31.0^{+7.2}_{-5.6}$   & $20.1^{+4.9}_{-4.5}$  & $21.5^{+2.1}_{-1.7}$ & $49.1^{+5.2}_{-3.9}$   & $0.19^{+0.07}_{-0.08}$ \\
     GW170608  & $0.9^{+0.0}_{-0.1}$ & $3.5^{+0.4}_{-1.3}$ & $0.69^{+0.04}_{-0.04}$ & $0.03^{+0.19}_{-0.07}$  & $320.0^{+120.0}_{-110.0}$    & $10.9^{+5.3}_{-1.7}$   & $7.6^{+1.3}_{-2.1}$   & $7.9^{+0.2}_{-0.2}$  & $17.8^{+3.2}_{-0.7}$   & $0.07^{+0.02}_{-0.02}$ \\
     GW170729  & $4.8^{+1.7}_{-1.7}$ & $4.2^{+0.9}_{-1.5}$ & $0.81^{+0.07}_{-0.13}$ & $0.36^{+0.21}_{-0.25}$  & $2750.0^{+1350.0}_{-1320.0}$ & $50.6^{+16.6}_{-10.2}$ & $34.3^{+9.1}_{-10.1}$ & $35.7^{+6.5}_{-4.7}$ & $80.3^{+14.6}_{-10.2}$ & $0.48^{+0.19}_{-0.2}$  \\
     GW170809  & $2.7^{+0.6}_{-0.6}$ & $3.5^{+0.6}_{-0.9}$ & $0.7^{+0.08}_{-0.09}$  & $0.07^{+0.16}_{-0.16}$  & $990.0^{+320.0}_{-380.0}$    & $35.2^{+8.3}_{-6.0}$   & $23.8^{+5.2}_{-5.1}$  & $25.0^{+2.1}_{-1.6}$ & $56.4^{+5.2}_{-3.7}$   & $0.2^{+0.05}_{-0.07}$  \\
     GW170814  & $2.7^{+0.4}_{-0.3}$ & $3.7^{+0.4}_{-0.5}$ & $0.72^{+0.07}_{-0.05}$ & $0.07^{+0.12}_{-0.11}$  & $580.0^{+160.0}_{-210.0}$    & $30.7^{+5.7}_{-3.0}$   & $25.3^{+2.9}_{-4.1}$  & $24.2^{+1.4}_{-1.1}$ & $53.4^{+3.2}_{-2.4}$   & $0.12^{+0.03}_{-0.04}$ \\
     GW170817 & $> 0.04$            & $> 0.1$            & $< 0.89$             & $0.0^{+0.02}_{-0.01}$   & $40.0^{+10.0}_{-10.0}$       & $1.46^{+0.12}_{-0.1}$  & $1.27^{+0.09}_{-0.09}$ & $1.186^{+0.001}_{-0.001}$ & $< 2.8$                & $0.01^{+0.0}_{-0.0}$ \\
     GW170818 & $2.7^{+0.5}_{-0.5}$ & $3.4^{+0.5}_{-0.7}$ & $0.67^{+0.07}_{-0.08}$ & $-0.09^{+0.18}_{-0.21}$ & $1020.0^{+430.0}_{-360.0}$   & $35.5^{+7.5}_{-4.7}$   & $26.8^{+4.3}_{-5.2}$   & $26.7^{+2.1}_{-1.7}$      & $59.8^{+4.8}_{-3.8}$   & $0.2^{+0.07}_{-0.07}$ \\
      GW170823 & $3.3^{+0.9}_{-0.8}$ & $3.6^{+0.6}_{-0.9}$ & $0.71^{+0.08}_{-0.1}$  & $0.08^{+0.2}_{-0.22}$  & $1850.0^{+840.0}_{-840.0}$   & $39.6^{+10.0}_{-6.6}$  & $29.4^{+6.3}_{-7.1}$   & $29.3^{+4.2}_{-3.2}$      & $65.6^{+9.4}_{-6.6}$   & $0.34^{+0.13}_{-0.14}$ \\
   \bottomrule
   \end{tabular}
   \caption[GWTC-1 : Summary of O1 and O2 Events]{The events from the first two advanced-era observing runs. The data in this table is derived from the first gravitational wave transient catalogue, GWTC-1 \cite{2018arXiv181112907T}.
       $E_{\text{rad}}$ is the total abbr:gw energy radiated as a result of the event; $L_{\text{peak}}$ is the event's peak abbr:gw luminosity; $a_{\text{final}}$ is the total spin of the remnant black hole;  $\chi_{\text{eff}}$ is the gls:effective-spin of the abbr:cbc system; $D_{\text{L}}$ is the luminosity distance to the source;  $M_{1}$ and $M_{2}$ are the masses of the two compact objects;  $\mathcal{M}$ is the gls:chirp-mass of the system;  $M_{\text{rem}}$  is the mass of the remnant, and  $z$ is the redshift of the source.
   \label{tab:eventlist}
   }
   \end{table}
   \end{landscape}

Future observing scenarios
==========================

The work in this thesis will consider the state of abbr:gw detection in
the observational era, starting in the early observational period: the
first two observing runs of the advanced gls:ligo detectors, and the
first observing run of the advanced gls:virgo detector; looking ahead to
future observing runs involving a larger network of abbr:gw detectors,
including gls:kagra and an additional advanced gls:ligo detector located
in India.

.. raw:: latex

   \begin{table}
   \centering
   \begin{tabular}{llll}
   \toprule
      Epoch  & LIGO  (Mpc) & Virgo (Mpc) & KAGRA (Mpc) \\
   \midrule
      Early  & 40 - 80     & 20 - 65     & 8 - 25      \\
      Mid    & 80 - 120    & 68 - 85     & 25 - 40     \\
      Late   & 120 - 170   & 85 - 155    & 40 - 140    \\
      Design & 190         & 125         & 140         \\
   \bottomrule
   \end{tabular}
   \label{tab:intro:rangescenarios}
   \caption[Anticipated sensitivities of advanced era detectors during their development]{The anticipated sensitivities of the various second-generation detectors throughout their development, measured in terms of the \gls{bns} \gls{horizon-distance}, which represents the average maximal distance at which the signal from a binary neutron star coalesence could be observed. This table was adapted from the information in~\cite{2018LRR....21....3A}.}
   \end{table}

The development of the advanced detectors is still on-going; sensitivity
improvements are normally made incrementally during periods when the
detectors are taken offline for extended periods of time. This phased
approach means that the sensitivity of the detectors, and consequently
the detector network, will improve in subsequent observing runs. In
table ref:tab:intro:rangescenarios these are summarised; the *early*
scenario equates approximately to the O1 run for advanced gls:ligo, and
the O2 run for advanced gls:virgo. Similarly, the *mid* and *late*
scenarios correspond approximately to O2 and O3 for advanced gls:ligo.

The first two observing runs have provided some information about the
rate of the events which produce detectable abpl:gw, allowing better
constraints to be placed on anticipated observed event rates as the
detectors continue to develop over the next decade.

.. [1]
   The designation \`\`LVT'', or \`\`abbr:ligo / gls:virgo transient''
   was used during the first two observing runs for events which were
   significant, but which did not surpass a threshold of :math:`5\sigma`
   for that significance. This event was eventually upgraded to the
   status of a confident event with the publication of the second
   observing run results cite:2018arXiv181112907T, and is now known as
   gls:gw151012.

.. [2]
   More precisely, the gls:ricci-tensor, which is the trace of the
   Riemann tensor, describes how the distance between the points within
   a volume varies as the entire volume is parallel-transported over a
   curved manifold, compared to the same movement over a flat manifold.

.. [3]
   The gls:ricci-scalar is the trace of the gls:ricci-tensor, and
   represents the deviation in the area of an :math:`(N-1)`-dimensional
   sphere in a curved :math:`N`-dimensional space compared to a flat
   :math:`N`-dimensional space.

.. [4]
   This rescaling of the metric has no physical consequence, but
   substanitally simplifies the number of quantities composing the
   Einstein tensor.

.. [5]
   The transverse-traceless gauge is convenient, since the metric
   perturbation is perpendicular to the wavevector in this gauge.

.. [6]
   Note here that :math:`\rho` is routinely used to represent an
   abbr:snr in signal processing, but this does introduce a confusing
   multiplicity, given the frequent use of :math:`\rho` for the mass
   density in physics.

.. [7]
   With the exception of the 2-kilometre detector at the gls:lho site,
   which was not upgraded; the unusued infrastructure from this detector
   is earmarked for a future gls:ligo detector in India.

.. [8]
   The standard nomenclature for advanced-era observing runs is of the
   form \`\`O<number>'', so the first observing run was \`\`O1''. These
   are independent of the actual detectors involved in the run, so when
   advanced gls:virgo started observations concurrently with the
   advanced gls:ligo detectors during its second observing run, the run
   was known universally as \`\`O2''.

.. |image| image:: ./figures/intro/aligo-asd.pdf

