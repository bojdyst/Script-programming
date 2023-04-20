/**
 * Simple class with one method - sum()
 * @class Operation
 * @param {Number} x - The first value
 * @param {Number} y - The second value
 */

export class Operation { //when CommonJS remove export statement
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Get a sum of two variables
     * @method sum
     * @returns {Number} The sum of this.x + this.y
     */
 
    sum() {
        return this.x + this.y;
    }
}

// exports.Operation = Operation