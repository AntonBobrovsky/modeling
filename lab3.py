import random
import numpy as np


class QueuingSystem:
    def __init__(self, max_size):
        self.max_size = max_size

    def uniform_distribution(self, math_exp):
        x = []
        for i in range(self.max_size):
            x.insert(i, random.uniform(0, 1) * math_exp)
        return x

    def exponential_distribution(self, math_exp):
        lambd = 1 / math_exp
        x = []
        for i in range(self.max_size):
            x.insert(i, (-1 * np.log(1 - random.uniform(0, 1))) / lambd)
        return x

    def const_distribution(self, math_exp):
        x = [math_exp] * self.max_size
        return x

    def gen_array(self, math_exp, type):
        if type == 1:
            x = self.exponential_distribution(math_exp)
        elif type == 2:
            x = self.uniform_distribution(math_exp)
        elif type == 3:
            x = self.const_distribution(math_exp)
        else:
            raise ValueError("Incorrect type !")
        return x

    def compute(self, d_type_tau, d_type_sigma, math_exp_step):
        res_full = []
        math_exp_tau = math_exp_step

        while math_exp_tau < 1.00:
            tau = self.gen_array(math_exp_tau, d_type_tau)
            math_exp_sigma = math_exp_step
            res = []

            while math_exp_sigma < 1.00:
                sigma = self.gen_array(math_exp_sigma, d_type_sigma)
                omega = [0] * self.max_size
                math_exp_omega = 0

                for i in range(self.max_size)[1:]:
                    omega[i] = max(0, sigma[i - 1] + omega[i - 1] - tau[i])
                    math_exp_omega += omega[i]

                math_exp_omega /= self.max_size
                res.append(math_exp_omega)
                math_exp_sigma += math_exp_step

            math_exp_tau += math_exp_step
            res_full.append(res)

        return res_full

    def run_implementation_queuing_system(self):
        types = {1: "exponential", 2: "uniform", 3: "const"}
        step = 0.1

        for i in types:
            for j in types:

                result = self.compute(i, j, step)
                file = open(types[i] + "-" + types[j] + ".out", 'w')
                n_str = len(result[0])
                count = 0.0

                for line in range(n_str):
                    count += step
                    out = repr(count)

                    for column in range(len(result)):
                        s = repr(float(result[column][line]))
                        out = out + "\t" + s

                    file.write(out + '\n')

                file.close()
                print(types[i] + "-" + types[j] + " Done")


if __name__ == "__main__":
    system = QueuingSystem(10000)
    system.run_implementation_queuing_system()
