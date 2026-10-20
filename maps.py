import numpy as np


# map generation
def empty_map() -> np.ndarray:
    map = np.zeros((20, 15))  

    # Always add border
    for x in range(20):
        map[x][0] = 1
        map[x][-1] = 1
    for y in range(15):
        map[0][y] = 1
        map[-1][y] = 1
        
    return map
    
def line_x(map: np.ndarray, x1: int, x2: int, y: int) -> np.ndarray:
    for x in range(x1, x2):
        map[x, y] = 1
    return map

def line_y(map: np.ndarray, y1: int, y2: int, x: int) -> np.ndarray:
    for y in range(y1, y2):
        map[x, y] = 1
    return map

def plus_map(map: np.ndarray) -> np.ndarray:
    map = line_x(map, 4, 16, 7)
    map = line_y(map, 3, 12, 9)
    map = line_y(map, 3, 12, 10)
    return map

def bars_map(map: np.ndarray) -> np.ndarray:
    map = line_y(map, 3, 12, 5)
    map = line_y(map, 3, 12, 15)
    return map

def rect_map(map: np.ndarray) -> np.ndarray:
    for y in range(4, 11):
        line_x(map, 4, 16, y)
    return map