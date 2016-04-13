import random
import numpy as np


class MarkovChains:
    def __init__(self, matrix_size, numbers):
        self.transition_matrix = \
        [
            [0.3, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2],
            [0.2, 0.3, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.2, 0.3, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.2, 0.3, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.2, 0.3, 0.5, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.2, 0.3, 0.5, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.3, 0.5, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.3, 0.5, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.3, 0.5],
            [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.3]
        ]

        self.transition_matrix2 = \
        [
            [0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5],
            [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5]
        ]

        self.matrix_size = matrix_size
        self.numbers = numbers
        self.static_a = 1

    def compute_and_output(self, matrix):
        global currect_x, ksi
        random.seed()
        history_x = [0] * self.matrix_size
        history_event = [0] * self.matrix_size
        matrix_prob = [0.0] * self.matrix_size
        for i in range(self.matrix_size):
            matrix_prob[i] = [0.0] * self.matrix_size
        array_ksi = [0.0] * 500

        for i in range(self.matrix_size):
            matrix_prob[i][0] = self.transition_matrix[i][0]
            for j in range(self.matrix_size)[1:]:
                matrix_prob[i][j] = self.transition_matrix[i][j] + matrix_prob[i][j - 1]

        currect_event = 0

        for k in range(self.numbers):
            tmp = random.uniform(0, 1)

            for i in range(self.matrix_size):
                if tmp < matrix_prob[currect_event][i]:
                    currect_event = i

                    while 1:
                        ksi = random.uniform(0, 1)
                        ksi = -1.0 * np.log(ksi)
                        currect_x = int(ksi / 0.7)

                        if currect_x < self.matrix_size:
                            break

                    history_event[currect_event] += 1
                    history_x[currect_x] += 1
                    break

            if k < 500:
                array_ksi[k] = ksi

        file_ksi = open("result_ksi" + str(self.static_a), 'w')
        file_history_event = open("history_event" + str(self.static_a), 'w')
        file_history_x = open("history_x" + str(self.static_a), 'w')
        self.static_a += 1

        for i in range(self.matrix_size):
            file_history_event.write(str(i + 1) + " " + repr(history_event[i]) + "\n")
            file_history_x.write(str(i + 1) + " " + repr(history_x[i]) + "\n")
        for i in range(500):
            file_ksi.write(str(i + 1) + ' ' + repr(array_ksi[i]) + '\n')

        file_ksi.close()
        file_history_event.close()
        file_history_x.close()

if __name__ == "__main__":
    obj = MarkovChains(10, 10000000)
    obj.compute_and_output(obj.transition_matrix)
    obj.compute_and_output(obj.transition_matrix2)
