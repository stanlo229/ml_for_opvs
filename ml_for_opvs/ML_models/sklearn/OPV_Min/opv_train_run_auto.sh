python ../train.py --train_path ../../../data/input_representation/OPV_Min/aug_SMILES/processed_augment_full/KFold/input_train_[0-9].csv --test_path ../../../data/input_representation/OPV_Min/aug_SMILES/processed_augment_full/KFold/input_test_[0-9].csv --input_representation DA_pair_aug --target_name calc_PCE_percent --model_type RF --hyperparameter_optimization True --hyperparameter_space_path ./opv_hpo_space.json --results_path ../../../training/OPV_Min/aug_SMILES/processed_augment_full --random_state 22

python ../train.py --train_path ../../../data/input_representation/OPV_Min/BRICS/master_brics_frag/KFold/input_train_[0-9].csv --test_path ../../../data/input_representation/OPV_Min/BRICS/master_brics_frag/KFold/input_test_[0-9].csv --input_representation DA_pair_BRICS --target_name calc_PCE_percent --model_type RF --hyperparameter_optimization True --hyperparameter_space_path ./opv_hpo_space.json --results_path ../../../training/OPV_Min/BRICS/master_brics_frag --random_state 22

python ../train.py --train_path ../../../data/input_representation/OPV_Min/fingerprint/master_fingerprint/KFold/input_train_[0-9].csv --test_path ../../../data/input_representation/OPV_Min/fingerprint/master_fingerprint/KFold/input_test_[0-9].csv --input_representation DA_FP_radius_3_nbits_512 --target_name calc_PCE_percent --model_type RF --hyperparameter_optimization True --hyperparameter_space_path ./opv_hpo_space.json --results_path ../../../training/OPV_Min/fingerprint/master_fingerprint --random_state 22

python ../train.py --train_path ../../../data/input_representation/OPV_Min/manual_frag/master_manual_frag/KFold/input_train_[0-9].csv --test_path ../../../data/input_representation/OPV_Min/manual_frag/master_manual_frag/KFold/input_test_[0-9].csv --input_representation DA_manual --target_name calc_PCE_percent --model_type RF --hyperparameter_optimization True --hyperparameter_space_path ./opv_hpo_space.json --results_path ../../../training/OPV_Min/manual_frag/master_manual_frag --random_state 22

python ../train.py --train_path ../../../data/input_representation/OPV_Min/manual_frag/KFold/input_train_[0-9].csv --test_path ../../../data/input_representation/OPV_Min/manual_frag/KFold/input_test_[0-9].csv --input_representation DA_manual_aug --target_name calc_PCE_percent --model_type RF --hyperparameter_optimization True --hyperparameter_space_path ./opv_hpo_space.json --results_path ../../../training/OPV_Min/manual_frag_aug --random_state 22

python ../train.py --train_path ../../../data/input_representation/OPV_Min/manual_frag/KFold/input_train_[0-9].csv --test_path ../../../data/input_representation/OPV_Min/manual_frag/KFold/input_test_[0-9].csv --input_representation DA_SMILES --target_name calc_PCE_percent --model_type RF --hyperparameter_optimization True --hyperparameter_space_path ./opv_hpo_space.json --results_path ../../../training/OPV_Min/SMILES --random_state 22

python ../train.py --train_path ../../../data/input_representation/OPV_Min/manual_frag/KFold/input_train_[0-9].csv --test_path ../../../data/input_representation/OPV_Min/manual_frag/KFold/input_test_[0-9].csv --input_representation DA_SELFIES --target_name calc_PCE_percent --model_type RF --hyperparameter_optimization True --hyperparameter_space_path ./opv_hpo_space.json --results_path ../../../training/OPV_Min/SELFIES --random_state 22

python ../train.py --train_path ../../../data/input_representation/OPV_Min/manual_frag/KFold/input_train_[0-9].csv --test_path ../../../data/input_representation/OPV_Min/manual_frag/KFold/input_test_[0-9].csv --input_representation DA_BigSMILES --target_name calc_PCE_percent --model_type RF --hyperparameter_optimization True --hyperparameter_space_path ./opv_hpo_space.json --results_path ../../../training/OPV_Min/BigSMILES --random_state 22
