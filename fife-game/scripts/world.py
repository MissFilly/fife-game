from fife import fife

from .common.eventlistenerbase import EventListenerBase
from agents.hero import Hero
from fife.extensions.fife_settings import Setting

TDS = Setting(app_name='zombies', settings_file='settings.xml')


class MapListener(fife.MapChangeListener):
    def __init__(self, map):
        fife.MapChangeListener.__init__(self)
        map.addChangeListener(self)


class World(EventListenerBase):
    def __init__(self, engine):
        super(World, self).__init__(engine, regKeys=True)
        self.engine = engine
        self.eventmanager = engine.getEventManager()
        self.model = engine.getModel()
        # self.filename = ''
        # self.pump_ctr = 0  # for testing purposis
        # self.ctrldown = False
        # self.instancemenu = None
        self.instance_to_agent = {}
        # self.dynamic_widgets = {}

    def load(self, filename):
        self.filename = filename
        # self.reset()
        loader = fife.MapLoader(self.engine.getModel(),
                                self.engine.getVFS(),
                                self.engine.getImageManager(),
                                self.engine.getRenderBackend())

        if loader.isLoadable(filename):
            self.map = loader.load(filename)

        # self.initCameras()
        self.initAgents()

        # Set background color
        self.engine.getRenderBackend().setBackgroundColor(80, 80, 255)

    def initAgents(self):
        self.agentlayer = self.map.getLayer('MapGroundObjectLayer')
        self.hero = Hero(TDS, self.model, 'hero', self.agentlayer)
        self.instance_to_agent[self.hero.agent.getFifeId()] = self.hero
        self.hero.start()

