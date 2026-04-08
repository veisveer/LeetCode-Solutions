function xorAfterQueries(nums: number[], queries: number[][]): number {
    let idx: number;

    for (let query of queries) {
        idx = query[0];
        while (idx <= query[1]) {
            nums[idx] = (nums[idx] * query[3] % (10**9 + 7));
            idx += query[2];
        }
    }

    let result: number;
    for (let num of nums) {
        result ^= num;
    }
    return result;
};