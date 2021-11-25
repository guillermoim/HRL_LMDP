
# Configuration 3x3 with lambda=1
echo "3x3 rooms grid, lambda=1"
#python main_nrooms.py --version 1 --config_name 3x3_goal@0-0_rooms5x5.dict --seed 0 --save_path grid_3_3_v1_0
#python main_nrooms.py --version 2 --config_name 3x3_goal@0-0_rooms5x5.dict --seed 0 --save_path grid_3_3_v2_03
#python main_nrooms.py --version 3 --config_name 3x3_goal@0-0_rooms5x5.dict --seed 0 --save_path grid_3_3_v3_0
python main_nrooms.py --version flat --config_name 3x3_goal@0-0_rooms5x5.dict --seed 0 --save_path grid_3_3_flat_0

#python main_nrooms.py --variant 2 --config_name  3x3_goal@0-0_rooms5x5.dict --seed 0 --save_path grid_3_3_v2_0
#python main_nrooms.py --variant 3 --config_name  3x3_goal@0-0_rooms5x5.dict --seed 0 --save_path grid_3_3_v3_0
#python main_nrooms.py --variant flat --config_name  3x3_goal@0-0_rooms5x5.dict --seed 0 --save_path grid_3_3_flat_0

# Configuration 6x6 with lambda=1
#echo "6x6 rooms grid, lambda=1"
#python main_nrooms.py --variant 1 --config_name 6_6_1.dict --seed 333 --save_path grid_6_6_1_v1_333
#python run_gridworld.py --variant 2 --config_name 6_6_1.dict --seed 333 --save_path grid_6_6_1_v2_333
#python run_gridworld.py --variant 3 --config_name 6_6_1.dict --seed 333 --save_path grid_6_6_1_v3_333
#python run_gridworld.py --variant flat --config_name 6_6_1.dict --seed 333 --save_path grid_6_6_1_flat_333

# Configuration 3x3 with lambda=10
#echo "3x3 rooms grid, lambda=10"
#python run_gridworld.py --variant 1 --config_name 3_3_10.dict --seed 666 --save_path grid_3_3_10_v1_666
#python run_gridworld.py --variant 2 --config_name 3_3_10.dict --seed 666 --save_path grid_3_3_10_v2_666
#python run_gridworld.py --variant 3 --config_name 3_3_10.dict --seed 666 --save_path grid_3_3_10_v3_666
#python run_gridworld.py --variant flat --config_name 3_3_10.dict --seed 666 --save_path grid_3_3_10_flat_666

# Configuration 6x6 with lambda=10
#echo "6x6 rooms grid, lambda=10"
#python run_gridworld.py --variant 1 --config_name 6_6_10.dict --seed 333 --save_path grid_6_6_10_v1_333
#python run_gridworld.py --variant 2 --config_name 6_6_10.dict --seed 333 --save_path grid_6_6_10_v2_333
#python run_gridworld.py --variant 3 --config_name 6_6_10.dict --seed 333 --save_path grid_6_6_10_v3_333
#python run_gridworld.py --variant flat --config_name 6_6_10.dict --seed 333 --save_path grid_6_6_10_flat_333


