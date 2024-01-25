import numpy as np


def predict_lr_steps(lr, lr_threshold, factor):
    lr_steps = []
    while lr >= lr_threshold:
        lr_steps.append(lr)
        lr *= factor
    return lr_steps


def predict_lr_step_no(lr, lr_threshold, factor):
    return len(predict_lr_steps(lr, lr_threshold, factor))


def lr_factor_step_no_dict(lr, lr_threshold, lr_scheduler_factors):

    lr_factors_dict = dict()
    for lr_scheduler_factor in lr_scheduler_factors:
        lr_factors_dict[lr_scheduler_factor] = predict_lr_step_no(lr, lr_threshold, lr_scheduler_factor)
        print(f"factor {lr_scheduler_factor}: {lr_factors_dict[lr_scheduler_factor]} lr steps")

    return lr_factors_dict


# def lr_factors_extrema_for_step_no(lr_factors):
#
#     lr_steps = np.unique([value for value in lr_factors.values()])
#     lr_stepno_factors_dict = {}
#     factor_min = 0
#     factor_max = 0
#     for lr_step in lr_steps:


def main():

    lr_scheduler_factors = np.linspace(0.00000000001, 0.7685, 1000)
    lr_0 = 2e-4
    lr_threshold = 1e-6
    lr_factors = lr_factor_step_no_dict(lr_0, lr_threshold, lr_scheduler_factors)

    lr_steps = np.unique([value for value in lr_factors.values()])
    print(lr_steps)
    # lr_factors_extrema = lr_factors_extrema_for_step_no(lr_factors)


if __name__ == "__main__":

    main()
