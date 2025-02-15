class Solution:
    def shortest_path(self, map: list[list[int]]) -> list[tuple[int, int]]:
        ROAD, DOOR, WALL, KEY, EXIT, PLAYER = 0, 1, 2, 3, 4, 5
        
        # Find player position
        player_position = None
        for r, row in enumerate(map):
            for c, col in enumerate(row):
                if col == PLAYER:
                    player_position = (r, c)
                    break
            if player_position:
                break
                
        if not player_position:
            return None

        # BFS with state tracking
        queue = [(player_position, 0)]  # (position, keys)
        visited = {(player_position, 0)}
        parent = {}
        map_copy = [row[:] for row in map]
        
        while queue:
            current, keys = queue.pop(0)
            
            if map_copy[current[0]][current[1]] == EXIT: #When exit is founnd, compute path and return it
                # Reconstruct path
                path = []
                state = (current, keys)
                while state in parent:
                    path.append(state[0])
                    state = parent[state]
                path.append(player_position)
                return path[::-1]
            
            # Check neighboring possible directions
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                new_x, new_y = current[0] + dx, current[1] + dy
                #Check if new position is within bounds
                if 0 <= new_x < len(map_copy) and 0 <= new_y < len(map_copy[0]):
                    cell = map_copy[new_x][new_y]
                    new_keys = keys
                    
                    # Handle different cell types, and update the map when coming across a key or door
                    if cell == WALL:
                        continue
                    if cell == KEY:
                        new_keys += 1
                        map_copy[new_x][new_y] = ROAD
                    if cell == DOOR:
                        if keys == 0:
                            continue
                        new_keys -= 1
                        map_copy[new_x][new_y] = ROAD
                    #If new state is not visited, add it to the queue                  
                    new_state = ((new_x, new_y), new_keys)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
                        parent[new_state] = (current, keys)
        
        return None