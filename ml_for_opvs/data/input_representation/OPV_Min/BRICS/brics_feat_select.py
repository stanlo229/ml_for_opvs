import pandas as pd
import numpy as np
import pkg_resources
from cmath import nan

# OPV data after pre-processing
MASTER_BRICS_DATA = pkg_resources.resource_filename(
    "ml_for_opvs", "data/input_representation/OPV_Min/BRICS/master_brics_frag.csv"
)

# create lists of groups of selected features
none = ['Unnamed: 0', 'Donor', 'Acceptor', 'PCE_percent', 'calc_PCE_percent', 'Voc_V', 'Jsc_mA_cm_pow_neg_2', 'FF_percent', 'Donor_BRICS', 'Acceptor_BRICS', 'DA_pair_BRICS', 'DA_tokenized_BRICS']
electronic = ['Unnamed: 0', 'Donor', 'Acceptor', 'HOMO_D_eV', 'LUMO_D_eV', 'HOMO_A_eV', 'LUMO_A_eV', 'PCE_percent', 'calc_PCE_percent', 'Voc_V', 'Jsc_mA_cm_pow_neg_2', 'FF_percent', 'Donor_BRICS', 'Acceptor_BRICS', 'DA_pair_BRICS', 'DA_tokenized_BRICS']
electronic_only = ['Unnamed: 0', 'HOMO_D_eV', 'LUMO_D_eV', 'HOMO_A_eV', 'LUMO_A_eV', 'PCE_percent', 'calc_PCE_percent', 'Voc_V', 'Jsc_mA_cm_pow_neg_2', 'FF_percent']
device = ['Unnamed: 0', 'Donor', 'Acceptor', 'D_A_ratio_m_m', 'solvent', 'total_solids_conc_mg_mL', 'solvent additive', 'solvent_additive_conc_v_v_percent', 'active_layer_thickness_nm', 'annealing_temperature', 'hole_contact_layer', 'electron_contact_layer', 'hole_mobility_blend', 'electron_mobility_blend', 'PCE_percent', 'calc_PCE_percent', 'Voc_V', 'Jsc_mA_cm_pow_neg_2', 'FF_percent', 'Donor_BRICS', 'Acceptor_BRICS', 'DA_pair_BRICS', 'DA_tokenized_BRICS']
device_solvent = ['Unnamed: 0', 'Donor', 'Acceptor', 'D_A_ratio_m_m', 'total_solids_conc_mg_mL', 'solvent additive', 'solvent_additive_conc_v_v_percent', 'active_layer_thickness_nm', 'annealing_temperature', 'hole_contact_layer', 'electron_contact_layer', 'hole_mobility_blend', 'electron_mobility_blend', 'PCE_percent', 'calc_PCE_percent', 'Voc_V', 'Jsc_mA_cm_pow_neg_2', 'FF_percent', 'BP', 'MP', 'Density', 'Dielectric', 'Dipole', 'log_Pow', 'Hansen_Disp', 'Hansen_H_Bond', 'Hansen_Polar', 'Donor_BRICS', 'Acceptor_BRICS', 'DA_pair_BRICS', 'DA_tokenized_BRICS']
fabrication = ['Unnamed: 0', 'Donor', 'Acceptor', 'D_A_ratio_m_m', 'solvent', 'total_solids_conc_mg_mL', 'solvent additive', 'solvent_additive_conc_v_v_percent', 'active_layer_thickness_nm', 'annealing_temperature', 'PCE_percent', 'calc_PCE_percent', 'Voc_V', 'Jsc_mA_cm_pow_neg_2', 'FF_percent', 'Donor_BRICS', 'Acceptor_BRICS', 'DA_pair_BRICS', 'DA_tokenized_BRICS']
fabrication_solvent = ['Unnamed: 0', 'Donor', 'Acceptor', 'D_A_ratio_m_m', 'total_solids_conc_mg_mL', 'solvent additive', 'solvent_additive_conc_v_v_percent', 'active_layer_thickness_nm', 'annealing_temperature', 'PCE_percent', 'calc_PCE_percent', 'Voc_V', 'Jsc_mA_cm_pow_neg_2', 'FF_percent', 'BP', 'MP', 'Density', 'Dielectric', 'Dipole', 'log_Pow', 'Hansen_Disp', 'Hansen_H_Bond', 'Hansen_Polar', 'Donor_BRICS', 'Acceptor_BRICS', 'DA_pair_BRICS', 'DA_tokenized_BRICS']
device_solvent_only = ['Unnamed: 0', 'Donor', 'Acceptor', 'D_A_ratio_m_m', 'total_solids_conc_mg_mL', 'solvent additive', 'solvent_additive_conc_v_v_percent', 'active_layer_thickness_nm', 'annealing_temperature', 'hole_contact_layer', 'electron_contact_layer', 'hole_mobility_blend', 'electron_mobility_blend', 'PCE_percent', 'calc_PCE_percent', 'Voc_V', 'Jsc_mA_cm_pow_neg_2', 'FF_percent', 'BP', 'MP', 'Density', 'Dielectric', 'Dipole', 'log_Pow', 'Hansen_Disp', 'Hansen_H_Bond', 'Hansen_Polar']
fabrication_solvent_only = ['Unnamed: 0', 'Donor', 'Acceptor', 'D_A_ratio_m_m', 'total_solids_conc_mg_mL', 'solvent additive', 'solvent_additive_conc_v_v_percent', 'active_layer_thickness_nm', 'annealing_temperature', 'PCE_percent', 'calc_PCE_percent', 'Voc_V', 'Jsc_mA_cm_pow_neg_2', 'FF_percent', 'BP', 'MP', 'Density', 'Dielectric', 'Dipole', 'log_Pow', 'Hansen_Disp', 'Hansen_H_Bond', 'Hansen_Polar']
fabrication_solvent_minus_active_layer = ['Unnamed: 0', 'Donor', 'Acceptor', 'D_A_ratio_m_m', 'total_solids_conc_mg_mL', 'solvent additive', 'solvent_additive_conc_v_v_percent', 'annealing_temperature', 'PCE_percent', 'calc_PCE_percent', 'Voc_V', 'Jsc_mA_cm_pow_neg_2', 'FF_percent', 'BP', 'MP', 'Density', 'Dielectric', 'Dipole', 'log_Pow', 'Hansen_Disp', 'Hansen_H_Bond', 'Hansen_Polar', 'Donor_BRICS', 'Acceptor_BRICS', 'DA_pair_BRICS', 'DA_tokenized_BRICS']

# create a dictionary with feature group's name as the key and the feature list as the value 
feature_dict = {'none' : none,'electronic': electronic,'electronic_only': electronic_only, 'device': device, 'device_solvent': device_solvent, 'fabrication': fabrication, 'fabrication_solvent': fabrication_solvent, 'device_solvent_only': device_solvent_only, 'fabrication_solvent_only': fabrication_solvent_only, 'fabrication_solvent_minus_active_layer': fabrication_solvent_minus_active_layer}

class FeatureSelection:
    """
    Class that contains functions to create new csv files with selected features for model training.
    The output csv files will have no null value.
    """

    def __init__(self, data):
        """
        Function that reads the csv data file into pandas dataframe for later data cleaning
        Args:
            file path of the original csv file
        Returns:
            pandas dataframe
        """
        self.data = pd.read_csv(data)
    def feat_select(self, feat_list):
        """
        Function that creates a csv files where (1) only selected features are included and (2) all null entries are excluded
        Args:
            the name of the group of feature
        Returns:
            csv file with only selected features and no empty entry
        """
        # create a list of all features' names
        feat_full = self.data.columns.tolist()
        # create a list of features that will not be included in training
        feat_to_drop = list(set(feat_full ) - set(feature_dict[feat_list]))
        # create a dataframe where unselected features are dropped
        df_full = self.data.drop(columns = feat_to_drop)
        # delete all rows that have at least 1 empty entry
        df = df_full.dropna(how = 'any')
        # save the processed dataframe to a new csv file whose name includes the group of features that are included
        df.to_csv('processed_brics_frag_{x}.csv'.format(x = feat_list), index=False)

fs = FeatureSelection(MASTER_BRICS_DATA)

fs.feat_select('electronic_only')

