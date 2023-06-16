import time
import problem_answer_1
import problem_answer_2
import problem_answer_3
import problem_answer_4

solutions = [
    problem_answer_1,
    problem_answer_2,
    problem_answer_3,
    problem_answer_4,
]


def benchmark(func):
    # 100 (cem) números
    one_hundred = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10
    # 1.000 (mil) números
    one_thousand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 100
    # 10.000 (dez mil) números
    ten_thousand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 1_000
    # 100.000 (cem mil) números
    # hundred_thousand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10_000

    start_time = time.time()
    func(one_hundred)
    print(f"Cem: {(time.time() - start_time):.4f} segundos")

    start_time = time.time()
    func(one_thousand)
    print(f"Mil: {(time.time() - start_time):.4f} segundos")

    start_time = time.time()
    func(ten_thousand)
    print(f"Dez mil: {(time.time() - start_time):.4f} segundos")

    # start_time = time.time()
    # func(hundred_thousand)
    # print(f"Cem mil: {(time.time() - start_time):.4f} segundos")


if __name__ == "__main__":
    for answer in solutions:
        print("=" * 70)
        print(
            f"* {answer.DESCRIPTION}. Tempo: {answer.TIME_COMPLEXITY} / Espaço: {answer.SPACE_COMPLEXITY}"
        )
        benchmark(answer.number_substitution)
        print()
