from copy import deepcopy
from typing import Dict

from hyperflow.hdl.utils import is_hdl_bottom


def add_public_info_to_default_hp(default_hp: Dict, public_info: Dict):
    for key, value in default_hp.items():
        if is_bottom_dict_in_default_hp(value):
            for p_k, p_v in public_info.items():
                value[p_k] = p_v
        elif isinstance(value, dict):
            add_public_info_to_default_hp(default_hp[key], public_info)


def is_bottom_dict_in_default_hp(value):
    if isinstance(value, dict):
        value_list = list(value.values())
        if len(value_list) == 0:
            return True
        if not isinstance(value_list[0], dict):
            return True
    return False


def extract_default_hp_from_hdl_bank(hdl_bank: Dict) -> Dict:
    dict_ = deepcopy(hdl_bank)
    default_hp_recursion(dict_)
    return dict_

def extract_pure_hdl_bank_from_hdl_bank(hdl_bank: Dict) -> Dict:
    dict_ = deepcopy(hdl_bank)
    pure_hdl_bank_recursion(dict_)
    return dict_



def pure_hdl_bank_recursion(dict_:Dict):
    should_pop = []
    should_recursion = []
    for key, value in dict_.items():
        if is_hdl_bottom(key,value):
            pass
        elif not isinstance(value,dict):
            should_pop.append(key)
        elif isinstance(value,dict):
            should_recursion.append(value)

    for key in should_pop:
        dict_.pop(key)
    for sub_dict_ in should_recursion:
        pure_hdl_bank_recursion(sub_dict_)

def default_hp_recursion(dict_: Dict):
    should_pop = []
    should_recursion = []
    for key, value in dict_.items():
        if isinstance(value, dict):
            if is_hdl_bottom(key, value):
                should_pop.append(key)
            else:
                should_recursion.append(value)
    for key in should_pop:
        dict_.pop(key)
    for sub_dict_ in should_recursion:
        default_hp_recursion(sub_dict_)
