import sys
import os

from plugins import email_plugin, logger_plugin, sms_plugin

class PluginManager:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.plugins = []

    def load_plugins(self):
        if self.plugin_dir not in sys.path:
            sys.path.insert(0, self.plugin_dir)
        
        for file in os.listdir(self.plugin_dir):
            #print(f'\n File Name: {file}')

            if file.endswith('.py') and not file.startswith('__'):
                module_name = file[:-3]
                plugin = __import__(module_name)
                self.plugins.append(plugin)
                #print(f'\n Module Name: module_name')
        return self.plugins

    def show_plugins(self):
        print("\n" + "=" * 50)
        print(f"\nShowing {len(self.plugins)} plugins:")
        print("\n" + "=" * 50)
        
        for plugin in self.plugins:
            if hasattr(plugin, 'get_info'):
                info = plugin.get_info()
                print(f'{plugin.__name__}:{info}')
            else:
                print(f'{plugin.__name__}')



manager = PluginManager('./plugins')
manager.load_plugins()
manager.show_plugins()

print("\n" + "=" * 50)
print("Testing Plugins:")
print("=" * 50)

for plugin in manager.plugins:
    if hasattr(plugin,'send'):
        plugin.send('Test Message')
    if hasattr(plugin, 'log'):
        plugin.log('Test Mesage')







