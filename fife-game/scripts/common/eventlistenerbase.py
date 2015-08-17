from fife import fife


class EventListenerBase(fife.IKeyListener):
    def __init__(self, engine, regKeys=True):
        self.eventmanager = engine.getEventManager()

        fife.IKeyListener.__init__(self)
        self.eventmanager.addKeyListener(self)
