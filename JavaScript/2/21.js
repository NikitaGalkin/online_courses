function my_function(n) {
    if (n != 1)
        n = my_function(n - 1) + " " + n;
    return n;
}