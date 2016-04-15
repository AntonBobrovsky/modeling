#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string.h>
#include <vector>
#define MAX 100000
#define a_ 0.8

using namespace std;

float func(float x) {
	float y;
	if (x >= 0.0 && x <= 1.0) {
		y = a_ * x;
	} else if (x > 1.0 && x < 2.0) {
		y = a_;
	} else {
		y = 0;
	}
	return y;
}

void implementation_method_reject() {
	float x1, x2;
	int hit[20];
	memset(hit, 0, sizeof(int) * 20);

	for (int i = 0; i < MAX; i++) {
		float a = 0, b = 2.4, c = 2.4;
		do {
			x1 = ((float) rand() / RAND_MAX);
			x2 = ((float) rand() / RAND_MAX);
		} while (func(a + (b - a) * x1) < c * x2);
		x2 *= c;
		x1 = a + (b - a) * x1;
		hit[(int)(x1 / 0.1)]++;
    }

	FILE *fp = fopen("out_reject", "w");
	for (int i = 0; i < 20; i++) {
		fprintf(fp, "%.d\n", hit[i]);
	}
	fclose(fp);
}

void with_repeat(int N) {
	float a = 1, mas[N], chance;
	int hit[N];
	memset(hit, 0, sizeof(int) * N);

	for (int i = 0; i < N - 1; i++)
	{
		mas[i] = abs(remainder((float) rand() / RAND_MAX, a));
		a -= mas[i];
	}

	mas[N - 1] = a;

	for (int i = 0; i < MAX; i++) {
		chance = (float) rand() / RAND_MAX;
		float sum = 0;
		for (int j = 0; j < N; j++) {
			sum += mas[j];
			if (chance < sum) {
				++hit[j];
				break;
			}
		}
	}

	FILE *fp = fopen("out_repeat", "w");
	for (int i = 0; i < N; i++) {
		fprintf(fp, "%d\t%.4f\t%.d\n", i, mas[i] * MAX, hit[i]);
	}

	fclose(fp);
}

void without_repeat(int N) {
	vector<int> nums, temp;
	int it, k = 3 * N / 4;
	int hit[N], part = MAX / k + 1;
	float p;

	memset(hit, 0, sizeof(int) * N);
	for(int number = 0; number < N; number++) {
		temp.push_back(number);
	}
	for(int j = 0; j < part; j++) {
		nums = temp;
		if (j == part - 1) k = MAX % k;
		for(int i = 0; i < k; i++) {
			p = 1.0 / (N - i);
			it = (float) rand() / RAND_MAX / p;
			++hit[nums[it]];
			nums.erase(nums.begin() + it);
		}
	}
	FILE *fp = fopen("out_no_repeat", "w");
	for(int number = 0; number < N; number++) {
		fprintf(fp, "%d\t%.d\n", number, hit[number]);
	}
	fclose(fp);
}

int main(int argc, char const *argv[])
{
	srand(time(NULL));

	implementation_method_reject();
	with_repeat(10);
	without_repeat(10);
	return 0;
}
