Fractal Set Image Generator
===================

Introduction
------------

The objective of this library is to create an image generator for the Mandelbrot and Julia fractal sets. The Mandelbrot set is defined as the set of complex numbers $c$ for which the sequence $z_{n+1} = z_{n}^{2}+c$ is bounded, with $z_{0} = 0$. The Julia set, on the other hand, uses the same sequence but with $z_{0}≠0$. Thus, the Julia set for a fixed complex $c$ consists of all complex $z_{0}$ for which $z_{n+1} = z_{n}^{2}+c$ converges.

Usage
------------

To visualize fractal images, you need to call plot_mandelbrot and plot_julia, specifying the region of the complex plane of interest, the value of $z_{0}$ for Julia, the value of $c$, the desired precision (via the max number of iterations), the desired pixel size, and the name of the image to save.

These two functions determine, using `is_in_julia` or `is_in_mandelbrot`, whether the points in the chosen complex plane region belong to the sets or not. For each point, we calculate the first max_iter terms of the sequence and check if all terms are within the circle of radius 2 in the complex plane. If they are, the point is black; otherwise, it is white.

To generate the Julia and Mandelbrot sequences, I have created the generators `suite_mandelbrot` and `suite_julia`.

Help
------------

-The project was created using Python 3.11.

-The libraries used are numpy and matplotlib.
    
-To modify the image save path, change the argument in plt.savefig on the last line of the functions plot_mandelbrot (line 158) and plot_julia (line 201).

-The functions plot_julia and plot_mandelbrot are located in: mon_module/tp_final.py
