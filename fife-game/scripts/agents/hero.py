from agent import Agent

_STATE_RUN = xrange(1)


class Hero(Agent):
    def run(self, location):
        self.state = _STATE_RUN
        self.agent.move('run', location, 4 * 1.2)

    def onInstanceActionFinished(self, instance, action):
        self.idle()

    def start(self):
        self.idle()

    def idle(self):
        self.state = _STATE_RUN
        self.agent.actOnce('run')
