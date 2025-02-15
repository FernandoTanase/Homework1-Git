class Solution:
    def shortest_path(self, map: list[list[int]]) -> list[tuple[int, int]]:
        # Define global variables
        ROAD = 0
        DOOR = 1
        WALL = 2
        KEY = 3
        EXIT = 4
        PLAYER = 5
        
        # Find player's initial position on the map
        player_position = None
        for r, row in enumerate(map):
            for c, column in enumerate(row):
                if column == PLAYER:
                    player_position = (r, c)
                    break
            if player_position is not None:
                break
                
        # If there is no player on the map, game can't be played
        if player_position is None:
            return None

        # Use BFS to search the map
        parent = {}  # Keep track of how we got to each position
        queue = []
        visited_cells = set()
        
        queue.append(player_position)
        visited_cells.add(player_position)
        
        exit_found = False
        exit_position = None
        
        while queue and not exit_found:
            current_position = queue.pop(0)
            
            if map[current_position[0]][current_position[1]] == EXIT:
                exit_found = True
                exit_position = current_position
                break
                
            for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
                new_row = current_position[0] + direction[0]
                new_col = current_position[1] + direction[1]
                
                # Stay within map bounds
                if 0 <= new_row < len(map) and 0 <= new_col < len(map[0]):
                    next_position = (new_row, new_col)
                    
                    # Check if the cell is not a wall and add it to our tree if it hasn't been visited
                    if map[new_row][new_col] != WALL and next_position not in visited_cells:
                        queue.append(next_position)
                        visited_cells.add(next_position)
                        parent[next_position] = current_position

        # If exit wasn't found, return None
        if not exit_found:
            return None

        # Reconstruct path from exit back to start
        path = []
        current = exit_position
        while current != player_position:
            path.append(current)
            current = parent[current]
        path.append(player_position)
        
        # Reverse path to get start-to-exit order
        return path[::-1]