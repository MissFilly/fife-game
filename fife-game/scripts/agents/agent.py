from fife import fife


class Agent(fife.InstanceActionListener):
    def __init__(self, settings, model, agent_name, layer, uniqInMap=True):
        fife.InstanceActionListener.__init__(self)
        self.settings = settings
        self.model = model
        self.agentName = agent_name
        self.layer = layer
        if uniqInMap:
            self.agent = layer.getInstance(agent_name)
            self.agent.addActionListener(self)

    def onInstanceActionFinished(self, instance, action):
        raise Exception('No OnActionFinished defined for Agent')

    def start(self):
        raise Exception('No start defined for Agent')
