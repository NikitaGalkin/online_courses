function testWhile(a) {
    var x=0;
    let k = 0;
    
    while (k <= a) {
        if (k%2 == 0)
            x += k;
        ++k;
    }

    return x;
}