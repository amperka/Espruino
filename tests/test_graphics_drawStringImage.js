var g = Graphics.createArrayBuffer(64,8,8);
g.dump = _=>{
  var s = "";
  var b = new Uint8Array(g.buffer);
  var n = 0;
  for (var y=0;y<g.getHeight();y++) {
    s+="\n";
    for (var x=0;x<g.getWidth();x++) 
      s+=".#"[b[n++]?1:0];
  }
  return s;
}
g.print = _=>{
  print("`"+g.dump()+"`");
}
var ok = true;
function SHOULD_BE(a) {
  var b = g.dump();
  if (a!=b) {
    console.log("GOT :"+b+"\nSHOULD BE:"+a+"\n================");
    ok = false;
  }
}


function binImg(img) {
  var i = Graphics.createImage(img);
  return String.fromCharCode(i.width,i.height,1)+i.buffer;
}

var img = binImg(`
#     #
   #  
   # 
#     #
 #####`);

// Test single image draw
g.clear();
g.drawImage(img,0,0);
SHOULD_BE(`
#.....#.........................................................
...#............................................................
...#............................................................
#.....#.........................................................
.#####..........................................................
................................................................
................................................................
................................................................`);

// Test image draw within text
var str = "HI \0"+img+" WORLD";
g.clear();
g.drawString(str,0,0);
SHOULD_BE(`
#.#.###.....#.....#....#.#..#..##..#...##.......................
#.#..#.........#.......#.#.#.#.#.#.#...#.#......................
###..#.........#.......###.#.#.#.#.#...#.#......................
#.#..#......#.....#....###.#.#.##..#...#.#......................
#.#.###......#####.....#.#..#..#.#.###.##.......................
................................................................
................................................................
................................................................`);

var width = g.stringWidth(str);
if (width != 43) {
  console.log("INVALID WIDTH : "+width);
  ok = false;
}

// Test image draw within text *when rotated and clipped* - https://github.com/espruino/Espruino/issues/2435
var str = "HI \0"+img+" WORLD";
g.clear().setRotation(2);
g.setClipRect(0,0,63,5);
g.drawString(str,0,0);
SHOULD_BE(`
................................................................
................................................................
................................................................
.......................##.###.#.#..#..#.#.....#####......###.#.#
......................#.#...#..##.#.#.###....#.....#......#..#.#
......................#.#...#.#.#.#.#.###.......#.........#..###
......................#.#...#.#.#.#.#.#.#.......#.........#..#.#
.......................##...#..##..#..#.#....#.....#.....###.#.#`);


result = ok;
