---
layout: single
title: "Research Projects"
permalink: /research/
author_profile: true
---

<style>
.rp-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.4rem;
  margin: 1.6rem 0 2rem;
}
.rp-card {
  background: #1a2332;
  border: 1px solid #2d3f55;
  border-left: 3px solid #60a5fa;
  border-radius: 5px;
  padding: 1.2rem 1.3rem;
}
.rp-card.em  { border-left-color: #34d399; }
.rp-card.geo { border-left-color: #f59e0b; }
.rp-card.mri { border-left-color: #818cf8; }
.rp-card-header {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 0.7rem;
  flex-wrap: wrap;
}
.rp-card h3 {
  margin: 0;
  font-size: 1em;
  color: #e2e8f0;
  flex: 1 1 auto;
}
.badge {
  display: inline-block;
  font-size: 0.72em;
  font-weight: 600;
  letter-spacing: 0.04em;
  padding: 0.18em 0.6em;
  border-radius: 999px;
  white-space: nowrap;
  flex-shrink: 0;
}
.badge-active { background: #16a34a; color: #bbf7d0; }
.badge-past   { background: #334155; color: #94a3b8; }
.rp-card p {
  font-size: 0.88em;
  color: #cbd5e1;
  line-height: 1.65;
  margin: 0 0 0.8rem;
}
.rp-card h4 {
  margin: 0.8rem 0 0.3rem;
  font-size: 0.78em;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #7dd3fc;
}
.rp-card.em  h4 { color: #6ee7b7; }
.rp-card.geo h4 { color: #fcd34d; }
.rp-card.mri h4 { color: #a5b4fc; }
.rp-card ul {
  margin: 0;
  padding-left: 1.1rem;
  font-size: 0.86em;
  color: #d1d5db;
  line-height: 1.65;
}
.rp-card ul li { margin-bottom: 0.2rem; }
.rp-card a { color: #7dd3fc; }
.rp-card.em  a { color: #6ee7b7; }
.rp-card.geo a { color: #fcd34d; }
.rp-card.mri a { color: #a5b4fc; }
</style>

Our work sits at the intersection of computational science, engineering, and applied mathematics,  and runs in two directions. The first is the use of classical and physics-informed machine learning methods for inverse problems -- recovering what cannot be directly measured from what can -- with thermal and fluid systems as our primary ground, though the questions travel further. The second is the development of structure-preserving high-order numerical schemes for PDEs -- methods that respect the deep mathematical structure of the underlying physics.

<div class="rp-grid">

<div class="rp-card">
<div class="rp-card-header">
<h3>Inverse Problems and PDE-Constrained Optimization in Thermo-Fluid Systems: Classical and Data-Driven Approaches</h3>
<span class="badge badge-active">Active</span>
</div>
<p>
Our group develops and applies classical and physics-informed machine learning methods to recover unknown parameters, boundary conditions, and source terms from indirect measurements -- with the goal of understanding, monitoring, and predicting the behaviour of thermo-fluid and related engineering systems.
On the data-driven side, we work with PINNs, physics-informed neural operators (PINO) and related techniques. On the classical side, adjoint-based methods remain a primary tool when the problem demands it. Alongside parameter estimation and real-time monitoring, uncertainty quantification is a central target -- pursued through both data-driven and classical techniques. The longer ambition threading through all of this is the development of digital twins for complex engineering systems.
<br>
Our primary focus is on thermal and fluid systems, though we remain genuinely open to problems wherever the mathematics is interesting and the physics is hard.
</p>
<h4>Methods &amp; Tools</h4>
<ul>
<li>Deterministic & Bayesian inverse problem formulations</li>
<li>Tikhonov and total-variation regularisation</li>
<li>Adjoint-based sensitivity and gradient computation</li>
<li>Physics-informed neural networks (PINNs)</li>
<li>Physics-informed neural operators (PINO)</li>
<li>Variational autoencoders (VAE) and normalising flows for UQ</li>
</ul>
<h4>Students & Staff</h4>
<ul>
    <li>Pradipan Maitra -- MS student</li>
    <li>Abhishek Srivastava -- Postdoctoral fellow </li>
    <li>Jariful Hassan — Research Staff</li>
  </ul>
<h4>Collaborators</h4>
<ul>
    <li> Dr. Sourav Sarkar -- Assistant Professor, Mechanical Engineering, Jadavpur University </li>
  </ul>
<h4>Publications</h4>
<ul>
  <li><a href="/publication/2026-01-01-PINN-based-Estimation-of-Convective-Heat-Transfer-in-Jet-Impingement-Cooling">PINN-based Estimation of Convective Heat Transfer in Jet Impingement Cooling (2026)</a></li>
<li> 2 papers under preparation </li>
</ul>
</div>

<div class="rp-card em">
<div class="rp-card-header">
<h3>High-Order Structure-Preserving Schemes for Computational Electrodynamics and MHD</h3>
<span class="badge badge-active">Active</span>
</div>
<p>
A central interest of our group is the development of numerical schemes for partial differential equations that faithfully mimic the structure of the underlying physical laws -- not merely in accuracy, but in the preservation of fundamental mathematical and physical properties.</p>
<p>One direction where we have worked extensively is the preservation of curl-type constraints -- $\nabla \cdot \mathbf{B} = 0$ and $\nabla \cdot \mathbf{D} = \rho -- intrinsic to Maxwell's equations and ideal MHD. Violating these constraints numerically leads to unphysical solutions and long-time instability. We develop high-order Discontinuous Galerkin (DG) and Flux Reconstruction (FR) schemes that preserve these constraints globally -- not just in a weak or cell-averaged sense -- using multidimensional Riemann solvers and carefully constructed numerical fluxes. To extend these ideas further, we developed two-derivative Runge–Kutta time integrators and generalised multidimensional Riemann solvers as core building blocks.</p>
<p> A closely related interest is the development of low-dissipation, low-dispersion schemes for computational electrodynamics (CED) and related areas such as aeroacoustics. Achieving this requires careful attention at every level of the discretisation -- high-order methods to control dissipation, and structure-preserving time integrators such as symplectic schemes to control dispersion and maintain long-time fidelity. For realistic simulations, adaptive mesh refinement and the combination of artificial boundary conditions with high-order methods are equally important building blocks.
</p>
<h4>Methods &amp; Tools</h4>
<ul>
  <li>Discontinuous Galerkin (DG) and Flux Reconstruction (FR) schemes</li>
  <li>Globally divergence-free and curl-free evolution</li>
  <li>Multidimensional Riemann problem solvers (classical and generalised)</li>
  <li>Two-derivative Runge-Kutta time stepping</li>
  <li>von Neumann and dispersion–dissipation analysis</li>
</ul>
<h4>Collaborators</h4>
<ul>
    <li> Prof. Praveen Chandrashekar -- TIFR-Centre for Applicable Mathematics, Bengaluru </li>
    <li> Prof. Dinshaw S. Balsara -- University of Notre Dame, Department of Physics </li>
    <li> Dr. Sudip K. Garain -- IISER Kolkata, Department of Physics </li>
  </ul>
<h4>Selected Papers</h4>
<ul>
  <li><a href="/publication/2019-10-01-Globally-constraint-preserving-FRDG-scheme-for-Maxwells-equations-at-all-orders">Globally Constraint-Preserving FR-DG Scheme for Maxwell's Equations (2019)</a></li>
  <li><a href="/publication/2020-05-01-Optimal-globally-constraint-preserving-DGTD2-schemes-for-computational-electrodynamics-based-on-two-derivative-Runge-Kutta-timestepping-and-multidimensional-generalized-Riemann-problem-solvers-A-von-Neumann-stability-analysis">Optimal Globally Constraint-Preserving DGTD2 Schemes (2020)</a></li>
  <li><a href="/publication/2023-07-01-Multidimensional-Generalized-Riemann-Problem-Solver-for-Maxwells-Equations">Multidimensional Generalised Riemann Problem Solver for Maxwell's Equations (2023)</a></li>
</ul>
</div>

<!--
<div class="rp-card geo">
<div class="rp-card-header">
<h3>Deep Learning for Geophysical Inverse Problems</h3>
<span class="badge badge-past">Past / Continuing</span>
</div>
<p>
Borehole logging tools must infer subsurface formation properties from electromagnetic measurements taken while drilling. This project combined physics-based forward modelling of logging-while-drilling (LWD) instruments with deep neural networks trained to solve the resulting inverse problem in near-real time — enabling geosteering decisions that would otherwise require iterative forward solves. The data-driven framework learned a direct mapping from tool responses to formation parameters, significantly accelerating the inversion.
</p>
<h4>Methods &amp; Tools</h4>
<ul>
  <li>Finite-element forward modelling of LWD tools</li>
  <li>Deep fully-connected and convolutional networks</li>
  <li>Training on synthetic forward-model datasets</li>
  <li>Sensitivity &amp; uncertainty analysis</li>
</ul>
<h4>Selected Papers</h4>
<ul>
  <li><a href="/publication/2022-03-01-A-deep-learning-approach-to-design-a-borehole-instrument-for-geosteering">A Deep Learning Approach to Design a Borehole Instrument for Geosteering (2022)</a></li>
</ul>
</div>
-->
<!--
<div class="rp-card mri">
<div class="rp-card-header">
<h3>Real-Time MRI Simulation</h3>
<span class="badge badge-past">Past</span>
</div>
<p>
Real-time MRI of moving objects (flowing blood, beating hearts) requires accurate simulation of the Bloch equations in the presence of velocity fields. This project developed efficient numerical solvers for the Bloch equations that account for flow-induced phase effects, enabling faithful virtual prototyping of MRI pulse sequences. The methods were validated against experimental data and applied to dynamic reconstruction scenarios, providing quantitative insight into artefacts caused by motion and flow.
</p>
<h4>Methods &amp; Tools</h4>
<ul>
  <li>Numerical integration of the Bloch ODE system</li>
  <li>Flow-effect modelling (gradient moment nulling)</li>
  <li>Dynamic MRI reconstruction algorithms</li>
  <li>Validation against phantom &amp; in-vivo data</li>
</ul>
<h4>Selected Papers</h4>
<ul>
  <li><a href="/publication/2015-11-01-Numerical-simulation-of-flow-effects-for-real-time-MRI">Numerical Simulation of Flow Effects for Real-Time MRI (2015)</a></li>
  <li><a href="/publication/2016-01-01-Numerical-Simulation-of-Bloch-Equations-for-Dynamic-Magnetic-Resonance-Imaging">Numerical Simulation of Bloch Equations for Dynamic MRI (2016)</a></li>
  <li><a href="/publication/2018-01-01-Numerical-simulation-of-Bloch-equations-for-dynamic-magnetic-resonance-imaging">Numerical Simulation of Bloch Equations for Dynamic MRI (2018, journal)</a></li>
</ul>
</div>
-->

</div>
