"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
let arr = [
    { id: 1, name: "Gopi", age: 19, readings: [15, 25, 35], isAdmitted: false },
    { id: 2, name: "Jon", age: 21, readings: [40, 50, 60], isAdmitted: true },
    { id: 3, name: "Ram", age: 23, readings: [20, 20, 20], isAdmitted: true },
];
function summ(arr) {
    let avg = [];
    for (let i = 0; i < arr.length; i++) {
        let temp = 0;
        for (let j = 0; j < arr[i].readings.length; j++) {
            temp += arr[i].readings[j];
        }
        ;
        avg.push(temp / arr[i].readings.length);
    }
    return avg;
}
console.log(summ(arr));
