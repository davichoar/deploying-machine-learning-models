import os
import pathlib

import regression_model

import pandas as pd


pd.options.display.max_rows = 10
pd.options.display.max_columns = 10


PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_models'
DATASET_DIR = PACKAGE_ROOT / 'datasets'

# data
TESTING_DATA_FILE = 'test.csv'
TRAINING_DATA_FILE = 'train.csv'
TARGET = 'TARGET'


# variables
FEATURES = ['POLIZA','FECHA_EMISION','PROD_AGRUPADO','SEXO',
            'ESTADO_CIVIL','DEP_AGRUP','CAL_GRAL','NUM_TC_SBS','NUM_VEHIC_SBS',
            'NUM_HIPOT_SBS','NUM_PP_SBS','SALDO_SBS','LINEA_TCMAX','SALDO_TC_SBS',
            'SALDO_VEH_SBS','SALDO_HIP_SBS','SALDO_PP_SBS','NSE_RIMAC','EDAD','NUM_DOC']


# this variable is to calculate the temporal variable,
# can be dropped afterwards
DROP_FEATURES = ['POLIZA', 'FECHA_EMISION', 'PROD_AGRUPADO','NUM_DOC']

# numerical variables with NA in train set
NUMERICAL_VARS_WITH_NA = ['SALDO_VEH_SBS','NSE_RIMAC']

# categorical variables with NA in train set
CATEGORICAL_VARS_WITH_NA = ['ESTADO_CIVIL','DEP_AGRUP']

TEMPORAL_VARS = 'FECHA_EMISION'

# categorical variables to encode
CATEGORICAL_VARS = ['ESTADO_CIVIL','DEP_AGRUP']

NUMERICAL_NA_NOT_ALLOWED = [
    feature for feature in FEATURES
    if feature not in CATEGORICAL_VARS + NUMERICAL_VARS_WITH_NA
]

CATEGORICAL_NA_NOT_ALLOWED = [
    feature for feature in CATEGORICAL_VARS
    if feature not in CATEGORICAL_VARS_WITH_NA
]


PIPELINE_NAME = 'scoring_journey'
PIPELINE_SAVE_FILE = f'{PIPELINE_NAME}_output_v'

# used for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
