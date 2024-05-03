class WBSPlanner:
    def __init__(self):
        self.wbs = {}

    def add_task(self, path, task_name):
        levels = path.split('/')
        current_level = self.wbs
        
        for level in levels:
            if level not in current_level:
                current_level[level] = {}
            current_level = current_level[level]
        
        current_level[task_name] = {}

    def display_wbs(self, wbs=None, indent=0):
        if wbs is None:
            wbs = self.wbs
        for key, value in wbs.items():
            print('    ' * indent + key)
            self.display_wbs(value, indent + 1)
def main():
    planner = WBSPlanner()
    
    # Add tasks and subtasks to the WBS
    # Example: planner.add_task('Project/Phase 1', 'Task 1')
    planner.add_task('Project', 'Planning')
    planner.add_task('Project/Planning', 'Budget Estimation')
    planner.add_task('Project/Planning', 'Resource Allocation')
    planner.add_task('Project', 'Execution')
    planner.add_task('Project/Execution', 'Task 1')
    planner.add_task('Project/Execution/Task 1', 'Subtask 1')
    planner.add_task('Project/Execution/Task 1', 'Subtask 2')
    
    # Display the complete WBS
    print("Work Breakdown Structure:")
    planner.display_wbs()

if __name__ == "__main__":
    main()
