function testDateTime(a, b) {
    var daysOfWeek = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'];

    var myDate1 = new Date();
    myDate1.setTime(Date.parse(a))

    var myDate2 = new Date();
    myDate2.setTime(Date.parse(b))

    myDate1.toLocaleString();
    myDate2.toLocaleString();

    return daysOfWeek[(+myDate1 > +myDate2)?(myDate1.getDay()):(myDate2.getDay())];
}
