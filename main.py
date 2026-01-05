import sys
import os

class PluginManager:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.plugins = []

    def load_plugins(self):
        # Check if directory exists
        if not os.path.exists(self.plugin_dir):
            print(f"❌ Error: Directory '{self.plugin_dir}' not found!")
            return []
        
        if self.plugin_dir not in sys.path:
            sys.path.insert(0, self.plugin_dir)
        
        print("Loading plugins...")
        for file in os.listdir(self.plugin_dir):
            if file.endswith('.py') and not file.startswith('__'):
                module_name = file[:-3]
                try:
                    plugin = __import__(module_name)
                    self.plugins.append(plugin)
                    print(f'  ✓ Loaded: {module_name}')
                except Exception as e:
                    print(f'  ✗ Failed to load {module_name}: {e}')
        
        return self.plugins

    def show_plugins(self, detailed=False):
        print("\n" + "=" * 50)
        print(f"Available Plugins ({len(self.plugins)} loaded)")
        print("=" * 50)
        
        for index, plugin in enumerate(self.plugins, 1):
            print(f'\n{index}. {plugin.__name__}')
            
            if hasattr(plugin, 'get_info'):
                print(f'   Info: {plugin.get_info()}')
            
            if detailed:
                functions = [func for func in dir(plugin) 
                            if not func.startswith('_') and callable(getattr(plugin, func))]
                if functions:
                    print(f'   Functions: {", ".join(functions)}')
    
    def test_all_plugins(self):
        print("\n" + "=" * 50)
        print("Testing All Plugins:")
        print("=" * 50)
        
        for plugin in self.plugins:
            print(f'\n--- Testing {plugin.__name__} ---')
            
            if hasattr(plugin, 'send'):
                plugin.send('Test Message')
            
            if hasattr(plugin, 'log'):
                plugin.log('Test Message')

# Main execution
if __name__ == "__main__":
    manager = PluginManager('./plugins')
    manager.load_plugins()
    
    # Show basic info
    manager.show_plugins()
    
    # Show detailed info
    manager.show_plugins(detailed=True)
    
    # Test all plugins
    manager.test_all_plugins()