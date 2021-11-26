from DOMAIN_TAXI import *
import argparse
import pickle
import numpy
import random

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Hierarchical Taxi')
    parser.add_argument('--version', type=str)
    parser.add_argument('--config_name', type=str)
    parser.add_argument('--save_path', type=str)
    parser.add_argument('--seed', type=int, default=100)

    args = parser.parse_args()
    version = args.version
    config_path = args.config_name
    save_path = args.save_path
    seed = args.seed

    numpy.random.seed(seed)
    random.seed(seed)

    execution = pickle.load(open(f'configs/taxi/{config_path}', 'rb'))

    c0s = [5000, 10000]
    c1s = [500, 1000, 5000]

    cs = [1000, 10000, 30000, 50000]

    if version in ('1', '2', '3'):
        print(f'Executing version {version}')
        results = {}
        for c0 in c0s:
            for c1 in c1s:
                res1 = HRL(f'V{version}', c0, c1, **execution)
                results[c0, c1] = res1

        pickle.dump(results, open(f'results/{save_path}.pkl', 'wb'))

    elif version == 'flat':
        print('Executing flat version')
        results = {}
        for c in cs:
            res = flat_Z_learning(c, **execution)
            results[c] = res

        pickle.dump(results, open(f'results/{save_path}.pkl', 'wb'))