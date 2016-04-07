\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{kentigern}[2016/04/06 v.0 A LaTeX document class for nice documents.]

\PassOptionsToClass{\CurrentOption}{kentigern}
\LoadClass[a4paper, openleft, 10pt]{memoir}

 \usepackage{everypage}
 \usepackage{afterpage}
 \usepackage{titlesec}
 \usepackage{calc}
 \usepackage{microtype}
 \RequirePackage{xparse}

 %%%% Allow complex maths
 \usepackage{amsmath}
 \usepackage{amsthm}
 \usepackage{mathtools}

 %%%% Box Environments
 \usepackage{color}					% Coloured Text
 \usepackage[usenames,dvipsnames]{xcolor}


 \ifdefined\HCode 
 %\usepackage{hyperref}
  \else
 \usepackage[pdfusetitle]{hyperref}
 %%%% Hyperref Settings
 \hypersetup{
     colorlinks,
     pdfborder={0 0 0},
     linkcolor={muted-blue},
     citecolor={blue!50!black},
     urlcolor={blue!80!black}
 }
 \fi
 

% % 

% %%%% Colours what'll be useful
% \definecolor{muted-blue}{HTML}{195073}
\definecolor{muted-green}{HTML}{7F8C1F}
% \definecolor{muted-orange}{HTML}{EE913F}
% \definecolor{muted-cream}{HTML}{F2E5BD}
% \definecolor{muted-egg}{HTML}{9FD7C7}


% %%% The big derivation float
% \newfloat[chapter]{bigderiv}{lod}{Derivation}
% %\setfloatadjustment{bigderiv}{\hrule}

% % %%%% Counters
% % \renewcommand{\fnum@bigderiv}{\textbf{Derivation~\thebigderiv}}
% % \renewcommand{\fnum@figure}{\textbf{\figurename~\thefigure}}
% % \renewcommand{\fnum@table}{\textbf{\tablename~\thetable}}
% % \renewcommand\@memmain@floats{%
% %   \counterwithin{figure}{section}
% %   \counterwithin{table}{section}
% %   \counterwithin{bigderiv}{section}
% % }
% % \captiondelim{: }

% %%%% Fonts

\usepackage[T1]{fontenc}
 \ifdefined\HCode 
  \else
  \usepackage[tikz]{mdframed}
  \usepackage{gillius}
  \usepackage{garamondx}
 \fi




%%%% Declare some macros which get replaced later
\let\Chaptername\null


%%%% Page open commands

\usepackage{ifthen}
% \newcommand{\clearevenside}{
%   \ifthenelse{\isodd{\thepage}}
%   {
%     \ifx\@currenvir{parcol}
%        \switchcolumn*[1]
%     \fi
%     \clearpage
%   }{
%     \ifx\@currenvir{parcol}
%        \switchcolumn*[1]
%     \fi
%     \clearpage
%     This page was left blank intentionally.
%     \phantom{placeholder}
%     \thispagestyle{empty}
%     \newpage
%   }
% }



% %%%% Change how Parts be made
% \let\printpartname\relax
% \let\printpartnum\relax
% \let\beforepartskip\relax
% %\renewcommand\printparttitle{\null}
% \let\Part\part
%  \renewcommand\part[2][]{{%
% %     \newpage
% %     \let\clearpage\relax
%      \cftaddtitleline{toc}{part}{#2}{}
% %     \addtocontents{toc}{\protect\mbox{}\protect\hrulefill\par}
%      %\addcontentsline{toc}{part}{#2}
%      \providecommand{\Partname}{#2}
% %     \if@twocolumn% true if twocolumn was being used
% %     \twocolumn[
% %     %\begin{minipage}{8cm}
% %     \thispagestyle{part}
% %     \ifx\relax#1\relax\Part{#2}
% %     \vskip1cm
% %     ]
% %     \else
% %        \Part[#1]{#2}
% %     \fi%
% %     %\end{minipage}
% %     %\twocolumn
% %     \else
% %         \ifx\relax#1\relax\Part{#2}
% %     \else
% %        \Part[#1]{#2}
% %     \fi%
% %     \fi
%  }
%  }
% \makeatletter
% \newcommand{\beforepartskip}{\newpage\null}
% \renewcommand*{\afterpartskip}{\par\@afterindentfalse\@afterheading}
% \makeatother
% \nopartblankpage
% \renewcommand{\partnamefont}{\color{muted-green}\normalfont\huge\sffamily\raggedright}
% \renewcommand{\partnumfont}{\color{muted-green}\normalfont\huge\sffamily\raggedright}
% \renewcommand{\parttitlefont}{\color{muted-green}\normalfont\Huge\sffamily\raggedright}

\let\Chaptermark\chaptermark
\def\chaptermark#1{\def\Chaptername{#1}}
% \let\Partmark\partmark
% \def\partmark#1{\def\Partname{#1}\Partmark{#1}}


%%%%% Epigraph
\setlength{\epigraphwidth}{7cm}

%%%% Margins

%\setstocksize{12in}{12in}
%\settrimmedsize{6in}{12in}{*}

\marginparmargin{inner}
\sidebarmargin{inner}
\setsidebars{1cm}{1.4\marginparwidth}{\onelineskip}%
{0pt}{\normalsize\normalfont }{\textheight}

\settypeblocksize{8.75in}{4in}{*}

\setlrmargins{*}{2cm}{*}
\setulmarginsandblock{4cm}{*}{*}

\setheadfoot{2cm}{2cm}
\setheaderspaces{*}{1.5cm}{*}
\setmarginnotes{1.5cm}{6cm}{1cm}


\checkandfixthelayout

%%%% Headers & Footers
\makeevenhead{headings}%
    {\sffamily \color{Maroon} \Chaptername}{}{}
\makeoddhead{headings}%
    {}{}{\sffamily \color{Maroon} \Chaptername}
\makeevenfoot{headings}%
    {\thepage \quad \vrule}{}{}
\makeoddfoot{headings}%
    {}{}{\vrule \quad \thepage}
\makeevenfoot{plain}%
    {\thepage \quad \vrule}{}{}
\makeoddfoot{plain}%
    {}{}{\vrule \quad \thepage}
\makeevenhead{plain}%
    {\sffamily \color{Maroon} \phantom{Hello}}{}{}
\makeoddhead{plain}%
    {}{}{\sffamily \color{Maroon} \phantom{Hello}}
\copypagestyle{title}{plain}
\makeevenhead{title}%
    {\null}{}{}
\makeoddhead{title}%
    {}{}{\null}
\makeoddfoot{title}%
    {\null}{\null}{\null}%\vrule \quad \thepage}
\makeevenfoot{title}%
     {\null}{\null}{\null}%\vrule \quad \thepage}

%%%% Automatic Title Generation Settings.


% \setlength\droptitle{-1cm}

% % Hook A appears above the title.
% %\def\maketitlehooka{
% %
% %}

% % Hook B appears below the title
% %\def\maketitlehookb{
% %
% %}

% % The Pre-title hook changes the behaviour 
% % of the rendering engine prior to setting the title.

\pretitle{
       \begingroup
       \fontsize{2cm}{3.5cm}\selectfont
 }

 \posttitle{
       \endgroup

 }

% \preauthor{
%   \vspace*{-.1cm}
%    \hfill
%    \begin{minipage}{0.18\textwidth}
%    \hfill
%  }
%  \postauthor{
%    \end{minipage}
%  }
% \predate{
%    \begin{minipage}{\textwidth}
%    \hfill
%  }
% \postdate{
%   \end{minipage}
%   \vspace*{0.2cm}
%   \hrule
%   \vspace*{0.2cm}
%  }

% %%%% Part Headings

% %\renewcommand{\beforepartskip}{\null}
% \renewcommand{\afterpartskip}{\null}


%%%% Chapter Headings
\makechapterstyle{minimalist}{%
  \renewcommand*{\chapnamefont}{}
  \renewcommand*{\chaptitlefont}{\fontsize{.75cm}{1cm}\selectfont \sffamily \scshape}
  \renewcommand*{\chapnumfont}{\fontsize{5cm}{5.5cm}\selectfont \color{Maroon}\sffamily}
  \renewcommand*{\printchaptername}{}
  \setlength{\chapindent}{0pt}
  \renewcommand*{\afterchapternum}{}
  \addtolength{\chapindent}{0pt}
  \renewcommand*{\printchapternum}{\chapnumfont \thechapter\space}
  \renewcommand{\printchaptertitle}[1]{%
    \\[2cm]
    \chaptitlefont
    \scshape ##1
  }
}

\chapterstyle{minimalist}
\setlength\beforechapskip{1cm}
\setlength{\prechapterprecisshift}{1cm}
\def\prechapterprecis{\vspace*{\prechapterprecisshift}}
\def\postchapterprecis{\newpage}

\def\afterchaptertitle{
  %\newpage
  %\vspace{1cm}
}
\def\clearforchapter{
  \newpage
}

% %%%% Lower-level headings
% \renewcommand{\secheadstyle}{\sffamily\color{muted-blue}\Large\bfseries}%\color{muted-blue}}
% \renewcommand{\subsecheadstyle}{\sffamily\large\bfseries\color{muted-orange}}
% \renewcommand{\subsubsecheadstyle}{\sffamily\bfseries\color{muted-orange}}
% \renewcommand{\paraheadstyle}{\sffamily\bfseries\color{muted-orange}}
% \renewcommand{\paraheadstyle}{\sffamily\bfseries\color{muted-orange}}


% %%%%% Theorem-like environments
% \theoremstyle{definition}
% \newtheorem{definition}{Definition}
% \numberwithin{definition}{chapter} % important bit
% \newtheorem{postulate}{Postulate}
% \numberwithin{postulate}{chapter} % important bit
% \newtheorem{lemma}{Lemma}
% \numberwithin{lemma}{chapter} % important bit
% \newtheorem{theorem}{Theorem}
% \numberwithin{theorem}{chapter} % important bit
% %\newtheorem{proof}{Proof}
% %\numberwithin{proof}{theorem} % important bit
% \newtheorem{subtheorem}{}
% \numberwithin{subtheorem}{theorem} % important bit
% \newtheorem{corollary}{Corollary}
% \numberwithin{corollary}{chapter} % important bit
% \newtheorem{algorithm}{Algorithm}
% \numberwithin{algorithm}{chapter} % important bit
% \newtheorem{property}{Property}
% \numberwithin{property}{chapter} % important bit
% \newtheorem{properties}{Properties}
% \numberwithin{properties}{chapter} % important bit
% \numberwithin{equation}{chapter}

% %%%%% The Example Environment
% %%% EXAMPLE-LIKE ENVIRONMENTS


% \ifdefined\HCode 

% \NewDocumentEnvironment{example}{o}{
%   \IfNoValueTF {#1}
%   {}
%   {\textbf{#1}} \par
% }
% {

% }

% \else

% \mdfdefinestyle{theoremstyle}{
%   backgroundcolor=muted-green!10,
%   middlelinewidth=0pt,
%   frametitlerule=false,
%   roundcorner=4pt,
%   apptotikzsetting={\tikzset{mdfframetitlebackground/.append style={%
%         shade, left color= muted-green!20, right color=muted-green!20
%       }}
%   },
%   innertopmargin=\topskip,
% }
% \mdfdefinestyle{equationstyle}{
%   backgroundcolor=muted-orange!10,
%   middlelinewidth=0pt,
%   frametitlerule=false,
%   roundcorner=0pt,
%   apptotikzsetting={\tikzset{mdfframetitlebackground/.append style={%
%         shade, left color= muted-orange!20, right color=muted-orange!20
%       }}
%   },
%   innertopmargin=\topskip,
% }
% \mdtheorem[style=theoremstyle]{example}{Example}
% \newmdenv[style=equationstyle]{namedequation}

% \fi

% \ifdefined\HCode 
% \NewDocumentEnvironment{fequation}{o}{
% %\begin{namedequation}
%   \IfNoValueTF {#1}
%   {}
%   { {\color{muted-orange} \small\textbf{#1}} }
%   \begin{equation}
% }
% {
%   \end{equation}
% %\end{namedequation}
% }

% \NewDocumentEnvironment{falign}{o}{
% %\begin{namedequation}
%   \IfNoValueTF {#1}
%   {}
%   { {\color{muted-orange} \small\textbf{#1}} }
%   \begin{align}
% }
% {
%   \end{align}
% %\end{namedequation}
% }

% \newcommand\mybox[2][]{%
%   \tikz[overlay]
%   \draw node (A) [fill=muted-orange!25,inner sep=2pt, anchor=text, rectangle]  {$#2$};
%   \phantom{#2}
% }
% \else
% \NewDocumentEnvironment{fequation}{o}{
% \begin{namedequation}
%   \IfNoValueTF {#1}
%   {}
%   { {\color{muted-orange} \small\textbf{#1}} }
%   \begin{equation}
% }
% {
%   \end{equation}
% \end{namedequation}
% }

% \NewDocumentEnvironment{falign}{o}{
% \begin{namedequation}
%   \IfNoValueTF {#1}
%   {}
%   { {\color{muted-orange} \small\textbf{#1}} }
%   \begin{align}
% }
% {
%   \end{align}
% \end{namedequation}}

% \newcommand\mybox[2][]{%
%   \tikz[overlay]
%   \draw node (A) [fill=muted-orange!25,inner sep=2pt, anchor=text, rectangle]  {$#2$};
%   \phantom{#2}
% }
% \fi

% \newcommand\eqnote[3][]{%
%   \underbracket[0pt][2pt]{
%     \hspace{2pt}\mybox{#2} \hspace{2pt}}
%   _{\text{#3}}
% }

% \makeatletter
% \renewcommand\tableofcontents{%
%   \vskip5mm
%   \@starttoc{toc}%
%   \vskip1cm
%   \hrule
%   \vskip1cm
% }
% \makeatother

% \makeatletter
% \NewDocumentCommand{\qgraph}{o m m}{
%   \IfNoValueTF{#1}
%      {\def\linecolor{muted-orange}}
%      {\def\linecolor{#1}}
% \begin{tikzpicture} 
%   \begin{axis}[ width=\linewidth,
%                 minor tick num=1, 
%                 axis x line=middle, 
%                 axis y line=middle, 
%                 every inner x axis line/.append style= {|->>, draw=black!30, help lines}, 
%                 every inner y axis line/.append style= {|->>, draw=black!30, help lines}, 
%                 xlabel=$x$,ylabel=$#2$ ] 
%      \addplot[\linecolor,domain=#3] {#2}; 
%    \end{axis} 
% \end{tikzpicture}}
% \makeatother

% \makeatletter
% \NewDocumentCommand{\tinygraph}{o m m}{
%   \IfNoValueTF{#1}
%      {\def\linecolor{muted-orange}}
%      {\def\linecolor{#1}}
% \vspace{5mm}
% \noindent
% \begin{tikzpicture} 
%   \begin{axis}[ width=\linewidth+15pt,
%                 height=30mm,
%                 thick,
%                 font=\scriptsize,
%                 minor tick num=0, 
%                 axis x line=middle, 
%                 axis y line=middle, 
%                 every inner x axis line/.append style= {|->>, draw=black!30, help lines}, 
%                 every inner y axis line/.append style= {|->>, draw=black!30, help lines}, 
%                  ] 
%      \addplot[\linecolor,domain=#3] {#2}; 
%    \end{axis} 
% \vspace{5mm}
% \end{tikzpicture}}
% \makeatother


% % %%% Fancy columns stuff
% % \NewDocumentEnvironment{derivhigh}{m}{
% %   \vspace{.5cm}
% %   \marginparthreshold{0}
% %   \columnratio{0.65}
% %   \twosided[cb]
% %   \begin{paracol}[2]{2}
% %     \marginparthreshold{0}
% %     \backgroundcolor{c[1](0.5\columnsep,10pt)(100pt, 4pt)}[rgb]{0.98,0.98, 0.98}
% %     %\backgroundcolor{c[1](0.5\columnsep,10pt)(100pt, 4pt)}[rgb]{0.98,0.93,0.87}
% %     \backgroundcolor{s(100,10pt)(0.5\columnsep, 4pt)}[rgb]{1,1,1}
% %     \begin{nthcolumn}{1} 
% %       \vfill
% %       #1
% %       \vfill
% %     \end{nthcolumn}
% %     \begin{nthcolumn}{0}
% %       \vfill
% % }
% % {     
% %       \vfill
% %     \end{nthcolumn} 
% % \end{paracol}
% %   \vspace{.5cm}
% % }

% % \NewDocumentEnvironment{expl}{}{
% %   \onecolumn \twosided \openany
% %   \vspace{.5cm}
% %   \marginparthreshold{0}
% %   \columnratio{0.7,0.3}
% %   \begin{paracol}{2}
% %     \backgroundcolor{s}[rgb]{1,1,1}
% %     %\backgroundcolor{c[1](5pt,16pt)(1000pt, 100pt)}[rgb]{0.99,0.99, 0.99}
% %     \switchcolumn[0]
% % }
% % {     
% %   \end{paracol}
% %   \vspace{.5cm}
% % }


% % \NewDocumentEnvironment{highlight}{}{
% %   \edef\eqcount{\the\value{equation}}
% %   \switchcolumn[0]
% %   \setcounter{equation}{\eqcount}
% % }
% % {  
% %   \edef\eqcount{\the\value{equation}}
% %   \switchcolumn[1]
% %   \setcounter{equation}{\eqcount}
% % }

% \usepackage{environ}
% \NewEnviron{derivation}{
%   \BODY
% }


% % \NewDocumentEnvironment{aroundderivation}{}{
% %   \twocolumn[
% %   \noindent
% %   \begingroup
% %   \small \indent
  
% % }
% % {
% %   \endgroup

% % }

% % \NewDocumentEnvironment{illustration}{}{
% %   \edef\eqcount{\the\value{equation}}
% %   \color{gray}
% %   %\vspace{0.6cm}
% %   \sffamily \raggedright
% % }
% % {
% %   \rmfamily
% %   \color{black}
% % }