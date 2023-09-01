//initialise my canvas
var canvas = document.getElementById("mycanvas");
var context = canvas.getContext('2d');
// centre coordinates
var x = 450;
var y = 440;
// colors
var yellow1 = "rgb(247, 205, 52)";
var yellow2 = "rgb(250, 184, 27)";
var pink1 = "rgb(247, 52, 182)";
var pink2 = "rgb(247, 82, 192)";
var black = "rgb(63, 60, 60)";
var white = "rgb(250, 245, 245)";
var orange1 = "rgb(245, 134, 49)";
var orange2 = "rgb(245, 154, 49)";
var purple = "rgb(186, 49, 245)";
function toRadians(angle) {
    return angle * (Math.PI / 180);
}
var r = 0;
// ====================================================================
// ------------------- outer design with squares and circles-------------------
r = 340;
for (var i = 0 + 5; i < 360 + 5; i = i + 10) {
    // purple dots on triangle point
    var newx = r * Math.cos(toRadians(i)) + x;
    var newy = r * Math.sin(toRadians(i)) + y;
    // outermost border of dots
    context.beginPath();
    context.arc(newx, newy, 35, 0, 2 * Math.PI, true);
    context.fillStyle = yellow1;
    context.fill();
    context.beginPath();
    context.arc(newx, newy, 25, 0, 2 * Math.PI, true);
    context.fillStyle = orange1;
    context.fill();
    context.beginPath();
    context.arc(newx, newy, 18, 0, 2 * Math.PI, true);
    context.fillStyle = pink1;
    context.fill();
    context.beginPath();
    context.arc(newx, newy, 10, 0, 2 * Math.PI, true);
    context.fillStyle = purple;
    context.fill();
    // white squares
    var x1 = r * Math.cos(toRadians(i)) + x;
    var y1 = r * Math.sin(toRadians(i)) + y;
    var x2 = r * Math.cos(toRadians(i + 90)) + x;
    var y2 = r * Math.sin(toRadians(i + 90)) + y;
    var x3 = r * Math.cos(toRadians(i + 180)) + x;
    var y3 = r * Math.sin(toRadians(i + 180)) + y;
    var x4 = r * Math.cos(toRadians(i + 270)) + x;
    var y4 = r * Math.sin(toRadians(i + 270)) + y;
    context.beginPath();
    context.moveTo(x1, y1);
    context.lineTo(x2, y2);
    context.lineTo(x3, y3);
    context.lineTo(x4, y4);
    context.lineTo(x1, y1);
    context.strokeStyle = "rgb(63, 60, 60)";
    context.fillStyle = white;
    context.fill();
}
// paint yellow squares
r = 320;
for (var i = 0; i < 360; i = i + 10) {
    var x1 = r * Math.cos(toRadians(i)) + x;
    var y1 = r * Math.sin(toRadians(i)) + y;
    var x2 = r * Math.cos(toRadians(i + 90)) + x;
    var y2 = r * Math.sin(toRadians(i + 90)) + y;
    var x3 = r * Math.cos(toRadians(i + 180)) + x;
    var y3 = r * Math.sin(toRadians(i + 180)) + y;
    var x4 = r * Math.cos(toRadians(i + 270)) + x;
    var y4 = r * Math.sin(toRadians(i + 270)) + y;
    context.beginPath();
    context.moveTo(x1, y1);
    context.lineTo(x2, y2);
    context.lineTo(x3, y3);
    context.lineTo(x4, y4);
    context.lineTo(x1, y1);
    context.strokeStyle = "rgb(63, 60, 60)";
    context.fillStyle = yellow1;
    context.fill();
}
// dark yellow squares
r = 300;
for (var i = 0 + 5; i < 360 + 5; i = i + 10) {
    var x1 = r * Math.cos(toRadians(i)) + x;
    var y1 = r * Math.sin(toRadians(i)) + y;
    var x2 = r * Math.cos(toRadians(i + 90)) + x;
    var y2 = r * Math.sin(toRadians(i + 90)) + y;
    var x3 = r * Math.cos(toRadians(i + 180)) + x;
    var y3 = r * Math.sin(toRadians(i + 180)) + y;
    var x4 = r * Math.cos(toRadians(i + 270)) + x;
    var y4 = r * Math.sin(toRadians(i + 270)) + y;
    context.beginPath();
    context.moveTo(x1, y1);
    context.lineTo(x2, y2);
    context.lineTo(x3, y3);
    context.lineTo(x4, y4);
    context.lineTo(x1, y1);
    context.strokeStyle = "rgb(63, 60, 60)";
    context.fillStyle = yellow2;
    context.fill();
}
// orange squares
r = 280;
for (var i = 0; i < 360; i = i + 10) {
    var x1 = r * Math.cos(toRadians(i)) + x;
    var y1 = r * Math.sin(toRadians(i)) + y;
    var x2 = r * Math.cos(toRadians(i + 90)) + x;
    var y2 = r * Math.sin(toRadians(i + 90)) + y;
    var x3 = r * Math.cos(toRadians(i + 180)) + x;
    var y3 = r * Math.sin(toRadians(i + 180)) + y;
    var x4 = r * Math.cos(toRadians(i + 270)) + x;
    var y4 = r * Math.sin(toRadians(i + 270)) + y;
    context.beginPath();
    context.moveTo(x1, y1);
    context.lineTo(x2, y2);
    context.lineTo(x3, y3);
    context.lineTo(x4, y4);
    context.lineTo(x1, y1);
    context.strokeStyle = "rgb(63, 60, 60)";
    context.fillStyle = orange1;
    context.fill();
}
// pink squares
r = 260;
for (var i = 0 + 5; i < 360 + 5; i = i + 10) {
    var x1 = r * Math.cos(toRadians(i)) + x;
    var y1 = r * Math.sin(toRadians(i)) + y;
    var x2 = r * Math.cos(toRadians(i + 90)) + x;
    var y2 = r * Math.sin(toRadians(i + 90)) + y;
    var x3 = r * Math.cos(toRadians(i + 180)) + x;
    var y3 = r * Math.sin(toRadians(i + 180)) + y;
    var x4 = r * Math.cos(toRadians(i + 270)) + x;
    var y4 = r * Math.sin(toRadians(i + 270)) + y;
    context.beginPath();
    context.moveTo(x1, y1);
    context.lineTo(x2, y2);
    context.lineTo(x3, y3);
    context.lineTo(x4, y4);
    context.lineTo(x1, y1);
    context.strokeStyle = "rgb(63, 60, 60)";
    context.fillStyle = pink2;
    context.fill();
}
// ----------------pink round above 8 orange dots -----------------
r = 230;
context.beginPath();
context.arc(x, y, r, 0, 2 * Math.PI, true);
context.fillStyle = pink2;
context.fill();
// purple border
for (var i = 0; i < 360; i = i + 5) {
    var newx = r * Math.cos(toRadians(i)) + x;
    var newy = r * Math.sin(toRadians(i)) + y;
    context.beginPath();
    context.arc(newx, newy, 10, 0, 2 * Math.PI, true);
    context.fillStyle = purple;
    context.fill();
}
// yellow dots in purple
for (var i = 0; i < 360; i = i + 5) {
    var newx = (r - 5) * Math.cos(toRadians(i)) + x;
    var newy = (r - 5) * Math.sin(toRadians(i)) + y;
    context.beginPath();
    context.arc(newx, newy, 4, 0, 2 * Math.PI, true);
    context.fillStyle = yellow1;
    context.fill();
}
//-----------------6 big orange circles-----------------
r = 150;
var small_r = 55;
for (var i = 0; i < 8; i++) {
    var newx = r * Math.cos(toRadians(45 * i)) + x;
    var newy = r * Math.sin(toRadians(45 * i)) + y;
    context.beginPath();
    context.arc(newx, newy, small_r, 0, 2 * Math.PI, true);
    context.fillStyle = orange1;
    context.fill();
    // yellow border flowers on orange circles
    for (var j = 0; j < 460; j = j + 10) {
        var xx = small_r * Math.cos(j) + newx;
        var yy = small_r * Math.sin(j) + newy;
        context.beginPath();
        context.arc(xx, yy, 10, 0, 2 * Math.PI, true);
        context.fillStyle = yellow1;
        context.fill();
    }
}
// yellow inside yellow - design
for (var i = 0; i < 8; i++) {
    var newx = r * Math.cos(toRadians(45 * i)) + x;
    var newy = r * Math.sin(toRadians(45 * i)) + y;
    // faint ywllow in dark yellow
    for (var j = 0; j < 460; j = j + 10) {
        var xx = small_r * Math.cos(j) + newx;
        var yy = small_r * Math.sin(j) + newy;
        context.beginPath();
        context.arc(xx, yy, 6, 0, 2 * Math.PI, true);
        context.fillStyle = yellow2;
        context.fill();
    }
    // pink
    for (var j = 0; j < 600; j = j + 10) {
        var xx = (small_r - 10) * Math.cos(j) + newx;
        var yy = (small_r - 10) * Math.sin(j) + newy;
        context.beginPath();
        context.arc(xx, yy, 3, 0, 2 * Math.PI, true);
        context.fillStyle = pink1;
        context.fill();
    }
}
// ----------------- white dots in 8 big orange-------------
r = 130;
var small_r = 33;
for (var i = 0; i < 8; i++) {
    var newx = r * Math.cos(toRadians(45 * i)) + x;
    var newy = r * Math.sin(toRadians(45 * i)) + y;
    context.beginPath();
    context.arc(newx, newy, small_r, 0, 2 * Math.PI, true);
    context.fillStyle = white;
    context.fill();
    for (var j = 0; j < 480; j = j + 10) {
        var xx = small_r * Math.cos(j) + newx;
        var yy = small_r * Math.sin(j) + newy;
        context.beginPath();
        context.arc(xx, yy, 5, 0, 2 * Math.PI, true);
        context.fillStyle = white;
        context.fill();
    }
    // yellow circle mala in white dot
    for (var j = 0; j < 490; j = j + 10) {
        var xx = (small_r - 5) * Math.cos(j) + newx;
        var yy = (small_r - 5) * Math.sin(j) + newy;
        context.beginPath();
        context.arc(xx, yy, 4, 0, 2 * Math.PI, true);
        context.fillStyle = yellow2;
        context.fill();
    }
    // pink circle inside yellow
    for (var j = 0; j < 490; j = j + 10) {
        var xx = (small_r - 8) * Math.cos(j) + newx;
        var yy = (small_r - 8) * Math.sin(j) + newy;
        context.beginPath();
        context.arc(xx, yy, 2, 0, 2 * Math.PI, true);
        context.fillStyle = pink2;
        context.fill();
    }
}
// pink dot with purple border in white dot
r = 110;
var small_r = 20;
for (var i = 0; i < 8; i++) {
    var newx = r * Math.cos(toRadians(45 * i)) + x;
    var newy = r * Math.sin(toRadians(45 * i)) + y;
    context.beginPath();
    context.arc(newx, newy, small_r + 5, 0, 2 * Math.PI, true);
    context.fillStyle = purple;
    context.fill();
    context.beginPath();
    context.arc(newx, newy, small_r, 0, 2 * Math.PI, true);
    context.fillStyle = pink1;
    context.fill();
}
// ====================================================================
// -------------purple-----------------
r = 95;
context.beginPath();
context.arc(x, y, r, 0, 2 * Math.PI, true);
context.fillStyle = purple;
context.fill();
// pink border above alternate yellow orange flowers
for (var i = 0; i < 1000; i = i + 10) {
    var newx = (r + 10) * Math.cos(i) + x;
    var newy = (r + 10) * Math.sin(i) + y;
    context.beginPath();
    context.arc(newx, newy, 5, 0, 2 * Math.PI, true);
    context.fillStyle = pink1;
    context.fill();
}
// orange yellow alternate flowers
var f = true;
for (var i = 0; i < 360; i = i + 10) {
    var newx = r * Math.cos(toRadians(i)) + x;
    var newy = r * Math.sin(toRadians(i)) + y;
    context.beginPath();
    context.arc(newx, newy, 9, 0, 2 * Math.PI, true);
    if (f == true) {
        context.fillStyle = yellow1;
        f = false;
    }
    else {
        context.fillStyle = orange1;
        f = true;
    }
    context.fill();
}
// ====================================================================
// -------------------white in inner circle-------
context.beginPath();
context.arc(x, y, 55, 0, 2 * Math.PI, true);
context.fillStyle = white;
context.fill();
// yellow circle dots with 6 orange dots on white
r = 60;
for (var i = 0; i < 270; i = i + 10) {
    var newx = r * Math.cos(i) + x;
    var newy = r * Math.sin(i) + y;
    context.beginPath();
    context.arc(newx, newy, 10, 0, 2 * Math.PI, true);
    context.fillStyle = yellow1;
    context.fill();
}
//6 orange on yellow line
for (var i = 0; i < 6; i++) {
    var newx = r * Math.cos(toRadians(60 * i)) + x;
    var newy = r * Math.sin(toRadians(60 * i)) + y;
    context.beginPath();
    context.arc(newx, newy, 15, 0, 2 * Math.PI, true);
    context.fillStyle = orange1;
    context.fill();
}
// ====================================================================
// ------------smallest pink----------------
context.beginPath();
context.arc(x, y, 30, 0, 2 * Math.PI, true);
context.fillStyle = pink1;
context.fill();
//yellow dots on pink
r = 33;
for (var i = 0; i < 300; i = i + 20) {
    var newx = r * Math.cos(i) + x;
    var newy = r * Math.sin(i) + y;
    context.beginPath();
    context.arc(newx, newy, 8, 0, 2 * Math.PI, true);
    context.fillStyle = yellow1;
    context.fill();
}
// ---------------inner yellow smallest -----------------
context.beginPath();
context.arc(x, y, 15, 0, 2 * Math.PI, true);
context.fillStyle = yellow1;
context.fill();
//# sourceMappingURL=pokalam.js.map