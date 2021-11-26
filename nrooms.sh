# Configuration 3x3 with lambda=1
echo "3x3 rooms nroom, lambda=1, seed=0"
python main_nrooms.py --version 1 --config_name 3x3_goal@0-0_rooms5x5.dict --seed 0 --save_path nroom_3_3_v1_0
python main_nrooms.py --version 2 --config_name 3x3_goal@0-0_rooms5x5.dict --seed 0 --save_path nroom_3_3_v2_0
python main_nrooms.py --version 3 --config_name 3x3_goal@0-0_rooms5x5.dict --seed 0 --save_path nroom_3_3_v3_0
python main_nrooms.py --version flat --config_name 3x3_goal@0-0_rooms5x5.dict --seed 0 --save_path nroom_3_3_flat_0

echo "3x3 rooms nroom, lambda=1, seed=333"
python main_nrooms.py --version 1 --config_name 3x3_goal@0-0_rooms5x5.dict --seed 333 --save_path nroom_3_3_v1_333
python main_nrooms.py --version 2 --config_name 3x3_goal@0-0_rooms5x5.dict --seed 333 --save_path nroom_3_3_v2_333
python main_nrooms.py --version 3 --config_name 3x3_goal@0-0_rooms5x5.dict --seed 333 --save_path nroom_3_3_v3_333
python main_nrooms.py --version flat --config_name 3x3_goal@0-0_rooms5x5.dict --seed 333 --save_path nroom_3_3_flat_333

echo "3x3 rooms nroom, lambda=1, seed=777"
python main_nrooms.py --version 1 --config_name 3x3_goal@0-0_rooms5x5.dict --seed 777 --save_path nroom_3_3_v1_777
python main_nrooms.py --version 2 --config_name 3x3_goal@0-0_rooms5x5.dict --seed 777 --save_path nroom_3_3_v2_777
python main_nrooms.py --version 3 --config_name 3x3_goal@0-0_rooms5x5.dict --seed 777 --save_path nroom_3_3_v3_777
python main_nrooms.py --version flat --config_name 3x3_goal@0-0_rooms5x5.dict --seed 777 --save_path nroom_3_3_flat_777

# Configuration 5x5 (ROOM_SIZE=3X3) with lambda=1
echo "5x5 rooms nroom, lambda=1, seed=0"
python main_nrooms.py --version 1 --config_name 5x5_goal@0-0_rooms3x3.dict --seed 0 --save_path nroom_5_5_v1_0
python main_nrooms.py --version 2 --config_name 5x5_goal@0-0_rooms3x3.dict --seed 0 --save_path nroom_5_5_v2_0
python main_nrooms.py --version 3 --config_name 5x5_goal@0-0_rooms3x3.dict --seed 0 --save_path nroom_5_5_v3_0
python main_nrooms.py --version flat --config_name 5x5_goal@0-0_rooms3x3.dict --seed 0 --save_path nroom_5_5_flat_0

echo "5x5 rooms nroom, lambda=1, seed=333"
python main_nrooms.py --version 1 --config_name 5x5_goal@0-0_rooms3x3.dict --seed 333 --save_path nroom_5_5_v1_333
python main_nrooms.py --version 2 --config_name 5x5_goal@0-0_rooms3x3.dict --seed 333 --save_path nroom_5_5_v2_333
python main_nrooms.py --version 3 --config_name 5x5_goal@0-0_rooms3x3.dict --seed 333 --save_path nroom_5_5_v3_333
python main_nrooms.py --version flat --config_name 5x5_goal@0-0_rooms3x3.dict --seed 333 --save_path nroom_5_5_flat_333

echo "5x5 rooms nroom, lambda=1, seed=777"
python main_nrooms.py --version 1 --config_name 5x5_goal@0-0_rooms3x3.dict --seed 777 --save_path nroom_5_5_v1_777
python main_nrooms.py --version 2 --config_name 5x5_goal@0-0_rooms3x3.dict --seed 777 --save_path nroom_5_5_v2_777
python main_nrooms.py --version 3 --config_name 5x5_goal@0-0_rooms3x3.dict --seed 777 --save_path nroom_5_5_v3_777
python main_nrooms.py --version flat --config_name 5x5_goal@0-0_rooms3x3.dict --seed 777 --save_path nroom_5_5_flat_777

# Configuration 8x8 (ROOM_SIZE=5x5) with lambda=1
echo "8x8 rooms nroom, lambda=1, seed=0"
python main_nrooms.py --version 1 --config_name 8x8_goal@0-0_rooms5x5.dict --seed 0 --save_path nroom_8_8_v1_0
python main_nrooms.py --version 2 --config_name 8x8_goal@0-0_rooms5x5.dict --seed 0 --save_path nroom_8_8_v2_0
python main_nrooms.py --version 3 --config_name 8x8_goal@0-0_rooms5x5.dict --seed 0 --save_path nroom_8_8_v3_0
python main_nrooms.py --version flat --config_name 8x8_goal@0-0_rooms5x5.dict --seed 0 --save_path nroom_8_8_flat_0

echo "8x8 rooms nroom, lambda=1, seed=333"
python main_nrooms.py --version 1 --config_name 8x8_goal@0-0_rooms5x5.dict --seed 333 --save_path nroom_8_8_v1_333
python main_nrooms.py --version 2 --config_name 8x8_goal@0-0_rooms5x5.dict --seed 333 --save_path nroom_8_8_v2_333
python main_nrooms.py --version 3 --config_name 8x8_goal@0-0_rooms5x5.dict --seed 333 --save_path nroom_8_8_v3_333
python main_nrooms.py --version flat --config_name 8x8_goal@0-0_rooms5x5.dict --seed 333 --save_path nroom_8_8_flat_333

echo "8x8 rooms nroom, lambda=1, seed=777"
python main_nrooms.py --version 1 --config_name 8x8_goal@0-0_rooms5x5.dict --seed 777 --save_path nroom_8_8_v1_777
python main_nrooms.py --version 2 --config_name 8x8_goal@0-0_rooms5x5.dict --seed 777 --save_path nroom_8_8_v2_777
python main_nrooms.py --version 3 --config_name 8x8_goal@0-0_rooms5x5.dict --seed 777 --save_path nroom_8_8_v3_777
python main_nrooms.py --version flat --config_name 8x8_goal@0-0_rooms5x5.dict --seed 777 --save_path nroom_8_8_flat_777


