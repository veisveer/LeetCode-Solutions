const DIRECTIONS = [[0, 1, "North"], [1, 0, "East"], [0, -1, "South"], [-1, 0, "West"]] as const;

class Robot {
    direction: number;
    x: number;
    y: number;
    width: number;
    height: number;

    constructor(width: number, height: number) {
        this.direction = 1;
        this.x = 0;
        this.y = 0;
        this.width = width;
        this.height = height;
    }

    step(num: number): void {
        let steps_taken = 0;

        // reduce looparounds
        const perimeter = 2 * (this.width - 1) + 2 * (this.height - 1);
        let steps_to_take = num % perimeter;

        if (num > 0 && steps_to_take === 0) {
            steps_to_take = perimeter;
        }

        let dx: number = DIRECTIONS[this.direction][0];
        let dy: number = DIRECTIONS[this.direction][1];

        while (steps_taken < steps_to_take) {
            const next_x = this.x + dx;
            const next_y = this.y + dy;

            if (next_x < this.width && next_x >= 0 && next_y < this.height && next_y >= 0) {
                this.x = next_x;
                this.y = next_y;
                steps_taken++;
            } else {
                this.direction = ((this.direction + 3) % 4)
                dx = DIRECTIONS[this.direction][0];
                dy = DIRECTIONS[this.direction][1];
            }
        }
    }

    getPos(): number[] {
        return [this.x, this.y];
    }

    getDir(): string {
        return DIRECTIONS[this.direction][2];
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * var obj = new Robot(width, height)
 * obj.step(num)
 * var param_2 = obj.getPos()
 * var param_3 = obj.getDir()
 */