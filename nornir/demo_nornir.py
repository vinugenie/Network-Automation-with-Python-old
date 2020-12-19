from nornir import InitNornir
#from nornir.plugins.tasks.networking import napalm_get
from nornir_napalm.plugins.tasks import napalm_get
# from nornir.plugins.functions.text import print_result
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
result = nr.run(task=napalm_get, getters=['get_facts'])

print_result(result)