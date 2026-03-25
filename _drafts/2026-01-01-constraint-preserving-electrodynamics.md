---
title: "What Does \"Constraint-Preserving\" Actually Mean in Computational Electrodynamics?"
date: 2026-01-01
tags: [Maxwell's Equations, Numerical Methods, DG]
excerpt: "The divergence constraints in Maxwell's equations are not independent equations; they are consequences of the curl equations when the initial data is consistent. Yet numerically, they can drift. This post explains why that drift is physically problematic and what globally constraint-preserving schemes actually guarantee."
---

The divergence constraints in Maxwell's equations — *∇·B = 0* and *∇·D = ρ* — are not independent equations; they are consequences of the curl equations when the initial data is consistent. Yet numerically, they can drift. This post explains why that drift is physically problematic, what "globally constraint-preserving" schemes actually guarantee, and the geometric insight behind the Finite-Element Riemann-DG approach we developed.

*Full post coming soon.*
