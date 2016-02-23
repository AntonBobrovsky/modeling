#include <stdio.h>
#include <iostream>
#include <ctime>
#include <cmath>
#include <random>

using namespace std;

#define NUM 1000000
#define INTERVAL 100
#define T_SIZE 4

int64_t xi_2 (double *mas)
{
	int64_t V = 0;
	int64_t Y[INTERVAL] = {0};

	double x = 1.0 / INTERVAL;

	for (int i = 0; i < NUM; ++i)
	{
		Y[(int)(mas[i] / x)]++;
	}

	for (int i = 0; i < INTERVAL; ++i)
	{
		V += (Y[i] * Y[i] / (double)x);
	}

	return (V / NUM - NUM);
}

void autocorrelation (double *mas)
{
	double Dx = 0.0, Mx = 0.0;
	double sumMx = 0.0, sumDx = 0.0;
	double cor = 0.0;

	for (int i = 0; i < NUM; ++i)
	{
		sumMx += mas[i];
		sumDx += mas[i] * mas[i];
	}

	Mx = (sumMx / NUM) * (sumMx / NUM);
	Dx = (sumDx / NUM) - Mx;
	
	for (int a = 1; a < T_SIZE; a++)
	{	
		for (int j = 0; j < NUM - a; ++j)
		{
			cor += mas[j] * mas[j + a];
		}

		cor /= NUM - a;
		cor -= Mx;
		cor /= (Dx - Mx);
		printf("autocorrelation = %lf\n", fabs(cor));
	}
}

void test_boost_random()
{
	cout << "C++11 BOOST RANDOM" << endl;
	cout << "============" << endl;
	double mas[NUM];
	std::random_device rd;
	std::mt19937 mt(rd());
	std::uniform_real_distribution<double> dist(0.0, 1.0);

	for (int i = 0; i < NUM; ++i)
	{
		mas[i] = dist(mt);
	}

	autocorrelation(mas);
	cout << "x^2 = " << xi_2(mas) << endl;
	cout << "============" << endl;
}

void test_random()
{
	cout << "RAND()" << endl;
	cout << "============" << endl;
	double mas2[NUM];

	for (int i = 0; i < NUM; ++i)
	{
		mas2[i] = (double)rand() / RAND_MAX;;
	}

	autocorrelation(mas2);
	cout << "x^2 = " << xi_2(mas2) << endl;
	cout << "============" << endl;
}

int main(int argc, char const *argv[])
{
	srand(time(NULL));
	test_boost_random();
	test_random();

	return 0;
}