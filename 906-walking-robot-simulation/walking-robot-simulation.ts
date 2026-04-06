// North 0, East 1, South 2, West 3
const DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]];

function robotSim(commands: number[], obstacles: number[][]): number {
    let x = 0, y = 0;
    let direction: number = 0;
    let max_distance = 0;

    for (let command of commands) {
        if (command === -2) {
            direction = (((direction - 1) % 4) + 4) % 4;
        } else if (command === -1) {
            direction = (((direction + 1) % 4) + 4) % 4;
        } else if (command >= 1 && command <= 9) {
            for (let i = 1; i <= command; i++) {
                const next_x = x + DIRECTIONS[direction][0];
                const next_y = y + DIRECTIONS[direction][1];

                if (obstacles.some(obstacle => obstacle[0] === next_x && obstacle[1] == next_y)) {
                    break;
                }
                
                x = next_x;
                y = next_y;
                
                const new_distance = x**2 + y**2;
                if (max_distance < new_distance) {
                    max_distance = new_distance;
                }
            }
        } else {
            //ignore false command
        }

    }
    return max_distance;
};