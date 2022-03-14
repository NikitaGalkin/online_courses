function testRegExp(s, sub_s) {
    var ans = new Array();
    let re = new RegExp(sub_s, 'g');
    let found;

    do {
        found = re.exec(s);

        if (found != null)
            ans.push(found);
    } while (found != null);

    return ans.join(",");
}