class Solution:
    def shortest_path(self, map: list[list[int]]) -> list[tuple[int, int]]:
        ROAD, DOOR, WALL, KEY, EXIT, PLAYER = 0, 1, 2, 3, 4, 5
        
        # Find player position and positions of each individual key & door on the map.
        player_position = None
        key_positions = []
        door_positions = []
        for r, row in enumerate(map):
            for c, col in enumerate(row):
                if col == PLAYER:
                    player_position = (r, c)
                elif col == KEY:
                    key_positions.append((r, c))
                elif col == DOOR:
                    door_positions.append((r, c))
        
        if not player_position:
            return None

        # BFS with state tracking.
        #Initialize all keys and doors as False for the root node (i.e. the initial state).
        initial_keys = tuple(False for _ in key_positions) #Keep track of which keys have been collected, for each new state in the queue/tree.
        initial_doors = tuple(False for _ in door_positions)#Keep track of which doors have been opened, for each state in the queue/tree.
        queue = [(player_position, initial_keys, initial_doors, [player_position])] #2nd player_position in the tuple is used so that we can later build the path as we pop states from the queue.
        visited = {(player_position, initial_keys, initial_doors)}
        
        while queue:
            current, keys, doors, path = queue.pop(0)
            
            if map[current[0]][current[1]] == EXIT:
                return path
            #Checking new possible states (unexplored)
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                new_x, new_y = current[0] + dx, current[1] + dy
                if 0 <= new_x < len(map) and 0 <= new_y < len(map[0]):
                    cell = map[new_x][new_y]
                    
                    # Skip walls immediately
                    if cell == WALL:
                        continue
                        
                    # Create new states (new_keys and new_doors just keeps track of the keys and doors for the new state)
                    new_keys = list(keys)
                    new_doors = list(doors)
                    can_move = True
                    
                    if cell == KEY:
                        key_idx = key_positions.index((new_x, new_y))
                        new_keys[key_idx] = True
                    
                    elif cell == DOOR:
                        door_idx = door_positions.index((new_x, new_y))
                        if doors[door_idx]:  # Door already open (in the current state, so don't need to open it again for the new state)
                            continue
                        # Try to find an unused key (from the current state) to open the door.
                        key_found = False
                        for i, has_key in enumerate(keys):
                            if has_key:
                                new_keys[i] = False
                                new_doors[door_idx] = True
                                key_found = True
                                break
                        if not key_found:
                            continue
                    #We can add the new state to the queue, and update the path.
                    new_state = ((new_x, new_y), tuple(new_keys), tuple(new_doors))
                    if new_state not in visited:
                        visited.add(new_state)
                        new_path = path + [(new_x, new_y)]
                        queue.append((new_state[0], new_state[1], new_state[2], new_path))
        
        return None