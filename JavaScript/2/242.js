function testArray(a, b) {
    var myArray = new Array();

    for (let i = 0; i < a.length; ++i) {
        myArray.push(a[i]);
    }

    for (let i = 0; i < b.length; ++i) {
        myArray.push(b[i]);
    }
    myArray.unshift("Иванов");
    myArray.reverse();

    return myArray.join("");
}