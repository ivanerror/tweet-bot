var removeDuplicates = function(nums) {
    let i = 0
    
    let pointer1 = nums[0]
    let pointer2 = nums[1]

    while(i < nums.length){   
        if(pointer1 == pointer2) {
            nums.splice(i,1)
        } else {
            pointer1 = pointer2
        }
        pointer2[i+1]
        i++
    }
    return nums
};

console.log(removeDuplicates([0,1,1,1,2,2,3,3,4]))
