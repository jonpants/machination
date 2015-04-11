from machination.constants import  MACHINATION_USERINSTANCESDIR
from machination.constants import MACHINATION_USERTEMPLATESDIR
from machination.constants import MACHINATION_DEFAULTTEMPLATESDIR

from machination.registries import MachineInstanceRegistry
from machination.registries import  MachineTemplateRegistry


MACHINE_INSTANCE_REGISTRY = MachineInstanceRegistry([MACHINATION_USERINSTANCESDIR])
MACHINE_TEMPLATE_REGISTRY = MachineTemplateRegistry([MACHINATION_DEFAULTTEMPLATESDIR, MACHINATION_USERTEMPLATESDIR])
