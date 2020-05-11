from .module import Module


class Gate(Module):

    def __init__(self, id, alias, device):
        Module.__init__(self, 'Gate', id, alias, device)

    def _update(self, new_state):
        Module._update(self, new_state)

    def control(self):
        def delay(delay):
            self._value = delay

        return interact(delay, delay=(0, 100, 1))
