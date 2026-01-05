---
title: "Math Rendering Demo"
date: 2025-01-01
description: "A demonstration of LaTeX math rendering capabilities"
tags: ["demo", "math"]
math: true
draft: true
---

This page demonstrates the math rendering capabilities using KaTeX.

## Inline Math

You can write inline math like $E = mc^2$ or $\vec{F} = m\vec{a}$ directly in your text.

The quadratic formula is $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.

## Block Equations

For display equations, use double dollar signs:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

## Matrices

$$
R = \begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

## Fractions and Summations

$$
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
$$

## Greek Letters

Common symbols: $\alpha$, $\beta$, $\gamma$, $\delta$, $\omega$, $\Omega$, $\theta$, $\phi$, $\psi$

## Calculus

The derivative:
$$
\frac{d}{dx}\left( x^n \right) = nx^{n-1}
$$

Partial derivatives:
$$
\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}
$$

## Physics Examples

Newton's Second Law:
$$
\vec{F} = m\frac{d\vec{v}}{dt} = m\vec{a}
$$

Schrödinger Equation:
$$
i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi
$$

Euler-Lagrange Equation:
$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}}\right) - \frac{\partial L}{\partial q} = 0
$$

## Control Theory

State-space representation:
$$
\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}
$$
$$
\mathbf{y} = C\mathbf{x} + D\mathbf{u}
$$

Transfer function:
$$
G(s) = \frac{Y(s)}{U(s)} = C(sI - A)^{-1}B + D
$$

## How to Use Math in Your Posts

1. Add `math: true` to your front matter
2. Use `$...$` for inline math
3. Use `$$...$$` for block equations

That's it! No complex setup required.
