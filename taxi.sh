echo "5x5 taxi-grid, lambda=1, seed=0"
python main_taxi.py --version 1 --config_name taxi_5_1.dict --seed 0 --save_path taxi_5_v1_0
python main_taxi.py --version 2 --config_name taxi_5_1.dict --seed 0 --save_path taxi_5_v2_0
python main_taxi.py --version 3 --config_name taxi_5_1.dict --seed 0 --save_path taxi_5_v3_0
python main_taxi.py --version flat --config_name taxi_5_1.dict --seed 0 --save_path taxi_5_flat_0

echo "5x5 taxi-grid, lambda=1, seed=333"
python main_taxi.py --version 1 --config_name taxi_5_1.dict --seed 333 --save_path taxi_5_v1_333
python main_taxi.py --version 2 --config_name taxi_5_1.dict --seed 333 --save_path taxi_5_v2_333
python main_taxi.py --version 3 --config_name taxi_5_1.dict --seed 333 --save_path taxi_5_v3_333
python main_taxi.py --version flat --config_name taxi_5_1.dict --seed 333 --save_path taxi_5_flat_333

echo "5x5 taxi-grid, lambda=1, seed=777"
python main_taxi.py --version 1 --config_name taxi_5_1.dict --seed 777 --save_path taxi_5_v1_777
python main_taxi.py --version 2 --config_name taxi_5_1.dict --seed 777 --save_path taxi_5_v2_777
python main_taxi.py --version 3 --config_name taxi_5_1.dict --seed 777 --save_path taxi_5_v3_777
python main_taxi.py --version flat --config_name taxi_5_1.dict --seed 777 --save_path taxi_5_flat_777

echo "10x10 taxi-grid, lambda=1, seed=0"
python main_taxi.py --variant 2 --config_name taxi_10_1.dict --seed 0 --save_path taxi_5_10_v2_0
python main_taxi.py --variant 1 --config_name taxi_10_1.dict --seed 0 --save_path taxi_5_10_v1_0
python main_taxi.py --variant 3 --config_name taxi_10_1.dict --seed 0 --save_path taxi_5_10_v3_0
python main_taxi.py --variant flat --config_name taxi_10_1.dict --seed 0 --save_path taxi_5_10_flat_0

echo "10x10 taxi-grid, lambda=1, seed=333"
python main_taxi.py --variant 2 --config_name taxi_10_1.dict --seed 333 --save_path taxi_5_10_v2_333
python main_taxi.py --variant 1 --config_name taxi_10_1.dict --seed 333 --save_path taxi_5_10_v1_333
python main_taxi.py --variant 3 --config_name taxi_10_1.dict --seed 333 --save_path taxi_5_10_v3_333
python main_taxi.py --variant flat --config_name taxi_10_1.dict --seed 333 --save_path taxi_5_10_flat_333

echo "10x10 taxi-grid, lambda=1, seed=777"
python main_taxi.py --variant 2 --config_name taxi_10_1.dict --seed 777 --save_path taxi_5_10_v2_777
python main_taxi.py --variant 1 --config_name taxi_10_1.dict --seed 777 --save_path taxi_5_10_v1_777
python main_taxi.py --variant 3 --config_name taxi_10_1.dict --seed 777 --save_path taxi_5_10_v3_777
python main_taxi.py --variant flat --config_name taxi_10_1.dict --seed 777 --save_path taxi_5_10_flat_777
