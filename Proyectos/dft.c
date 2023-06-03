
#include <stdio.h>
#include <stdlib.h>

unsigned long long factorial(int n){
	if(n== -1 || n== 1){
		return 1;
	}

	unsigned long long fact = 1;

	for (int i = 2; i <= n; i++){
		fact*=i;	
	}

	return fact;
}

long double powl(long double base, long double exponent) {
	if (exponent == 0) {
		return 1.0;
	}

	if (exponent == 1) {
		return base;
	}
				   
	long double result = powl(base * base, exponent / 2);

	if ((long)exponent % 2 == 1) {
		result *= base;
	 }

	return result;
}


double taylor_seno(double x, int n){
	double sen = 0.0;
	for(int i = 0; i < n; i++){
		sen += powl(-1,i) * powl(x,2*i+1) / factorial(2*i+1);
	}
	return sen;
}

double taylor_coseno(double x, int n){
	double cos = 0.0;
	for(int i = 0; i < n; i++){
		cos += powl(-1,i) * powl(x,2*i) / factorial(2*i);
	}
	return cos;
}
/*typedef struct define una estructura llamada complex
 *esto es una estructura que permite agrupar varios elementosde diferentes tipos en una
 sola entidad que luego seran llamadas por el seudo nombre que se le dio es cual es
 COMPLEX.
 * */
typedef struct {
	double real;
	double imag;
} Complex;

/*malloc: se usa para asignar un bloque de memoria dinamica mientras se ejecuta. Este recibe como 
 * argumento el tamano en bytes que se desea reservar y devuelve el puntero al inicio de la memoria
 * asignada.
 *
 * free: se usa para liberar el espacio en memoria que fue previamente asignada con malloc.
 *
 * sizeof: se usa para determinar el tamano en bytes de un tipo de dato o una variable.
 * En el codigo se usa para determinar el tamano adecuado para asignar en memoria dinamica.
*/
Complex *dft(double *lista, int n) {
	Complex *vect = (Complex *) malloc(sizeof(Complex) * n);

	if (n == 1) {
		vect[0].real = lista[0];
		vect[0].imag = 0;
		return vect;
	}

	double *par = (double *) malloc(sizeof(double) * (n / 2));
	double *impar = (double *) malloc(sizeof(double) * (n / 2));

	int par_index = 0;
	int impar_index = 0;

	for (int i = 0; i < n; i++) {
		if (i % 2 == 0) {
		par[par_index++] = lista[i];
		} else {		
		impar[impar_index++] = lista[i];							            }
	}

	Complex *par_dft = dft(par, n / 2);
	Complex *impar_dft = dft(impar, n / 2);

	double pi = 3.1415926535897932384;

	for (int m = 0; m < n / 2; m++) {
		double theta = 2 * pi * m / n;
		double w_re = taylor_coseno(theta, n);
		double w_im = -taylor_seno(theta, n);
		
		double z_re = w_re * impar_dft[m].real - w_im * impar_dft[m].imag;
		double z_im = w_re * impar_dft[m].imag + w_im * impar_dft[m].real;

		vect[m].real = par_dft[m].real + z_re;
		vect[m].imag = par_dft[m].imag + z_im;        
		vect[m + n / 2].real = par_dft[m].real - z_re;
		vect[m + n / 2].imag = par_dft[m].imag - z_im;
        }

	        free(par);
		free(impar);
		free(par_dft);
		free(impar_dft);

	        return vect;
}



