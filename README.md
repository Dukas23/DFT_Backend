# Implementación de la Transformada Rápida de Fourier (FFT) en el backend

## Índice

1. [Implementación utilizando series de Taylor](#implementación-utilizando-series-de-taylor)
2. [Implementación del algoritmo "divide y vencerás"](#implementación-del-algoritmo-divide-y-vencerás)
3. [Integración en el servidor](#integración-en-el-servidor)

## Implementación utilizando series de Taylor

Una manera de calcular las funciones seno y coseno las cuales son necesarias para el calculo de
la FFT es mediante las aproximaciones por series de Taylor y estas se puede expresar como:

$$
\text{\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \ldots \\ \\
\sin(x) = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}\\ \\
\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \ldots} \\ \\
\cos(x) = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!}
$$

Al aproximar estas serie mediante el número finito de términos, podemos obtener valores
cercanos a los senos y cosenos de los ángulos necesarios en la FFT

## Implementación del algoritmo "divide y vencerás"

El algoritmo "divide y vencerás" es utilizado en la FFT para dividir la señal en subproblemas más pequeños y
luego combinar los resultados para obtener la transformada final. El algoritmo consta de los siguientes pasos:

1. Si la longitud de la señal es 1, retornar la señal como está.
2. Dividir la señal en dos partes iguales.
3. Recursivamente calcular la FFT de cada una de las partes.
4. Combinar los resultados de las partes para obtener la FFT completa.

## Integración en el servidor

En el servidor, la biblioteca de la FFT se está llamando desde la siguiente ruta: '/home/ubuntu/Proyectos/dft.so'. Sin embargo, es importante tener
en cuenta que en el repositorio los archivos se subieron con el propósito de mantener la consistencia, pero están ubicados en otro lugar en el servidor, que no es directamente
dentro del repositorio.
