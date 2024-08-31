import commands.command_base as command_base

# Status command
class Command(command_base.Command):
    @property
    def info(self):
        return {
            "description": "Show current staging area status",
            "usage": "status",
            "aliases": ["st"]   
        }
        
    def run(self, *args):
        # Get the current branch
        with open(".kinto/HEAD", "r") as f:
            branch = f.read().strip()
            
        # Get the current commit
        with open(f".kinto/{branch}", "r") as f:
            commit = f.read().strip()
            
        # Get the current staging area
        with open(f".kinto/commits/{commit}", "r") as f:
            staging_area = f.read().strip().split("\n")
            
        if len(staging_area) == 0:
            print("No files in the staging area")
        else:
            print("Staging area:")
            for file in staging_area:
                print(f"  {file}")
        pass

    
