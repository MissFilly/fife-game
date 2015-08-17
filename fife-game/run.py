import os, sys

fife_path = os.path.join('..', 'fifengine', 'engine', 'python')
if os.path.isdir(fife_path) and fife_path not in sys.path:
    sys.path.insert(0, fife_path)

from fife.extensions.fife_settings import Setting
from fife.extensions.basicapplication import ApplicationBase

from scripts.common import eventlistenerbase
from scripts.world import World

settings = Setting(app_name="zombies", settings_file='settings.xml')


class ApplicationListener(eventlistenerbase.EventListenerBase):
    def __init__(self, engine, world):
        super(ApplicationListener, self).__init__(engine, regKeys=True)
        self.engine = engine
        self.world = world


class ZombiesApplication(ApplicationBase):
    def __init__(self, settings):
        super(ZombiesApplication, self).__init__(settings)
        self.world = World(self.engine)
        self.listener = ApplicationListener(self.engine, self.world)
        self.world.load('maps/country.xml')


def main():
    app = ZombiesApplication(settings)
    app.run()


if __name__ == '__main__':
        main()
