function testErrorFunc(a, func) {         
    var x;
    try {
        func(a);
    } catch (ex) {
        x = ex.name;
    }
    return x;
}