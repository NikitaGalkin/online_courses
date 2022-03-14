function testArray(a, b) {
    return sum(a) + sum(b);
}

function sum(a) {
    let summ = 0;

    for (let i = 0; i < a.length; ++i) {
        summ += a[i];
    }

    return summ;
}