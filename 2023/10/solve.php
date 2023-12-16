<?php

$lines = file('input.txt', FILE_IGNORE_NEW_LINES);

// parse the input
$map = array();
foreach ($lines as $i => $line) {
    foreach (str_split($line) as $j => $s) {
        $map[$i][$j] = array($s, PHP_INT_MAX);
        if($s == 'S')
            $pos_start = array($i, $j);
    }
}

// part 1
$elem = array($pos_start);
$map[$pos_start[0]][$pos_start[1]] = array('S', 0);
$x = count($lines);
while(count($elem) > 0) {
    $e = array_pop($elem);
    $s = $map[$e[0]][$e[1]][0];
    $v = $map[$e[0]][$e[1]][1];
    if($s == 'S') {
        if($e[0] > 0 && ($map[$e[0]-1][$e[1]][0] == '|' || $map[$e[0]-1][$e[1]][0] == 'F' || $map[$e[0]-1][$e[1]][0] == '7') && $map[$e[0]-1][$e[1]][1] > ($v + 1)) {
            $map[$e[0]-1][$e[1]][1] = $v + 1;
            $elem[] = array($e[0]-1, $e[1]);
        }
        if($e[0] < $x && ($map[$e[0]+1][$e[1]][0] == '|' || $map[$e[0]+1][$e[1]][0] == 'L' || $map[$e[0]+1][$e[1]][0] == 'J') && $map[$e[0]+1][$e[1]][1] > ($v + 1)) {
            $map[$e[0]+1][$e[1]][1] = $v + 1;
            $elem[] = array($e[0]+1, $e[1]);
        }
        if($e[1] > 0 && ($map[$e[0]][$e[1]-1][0] == '-' || $map[$e[0]][$e[1]-1][0] == 'F' || $map[$e[0]][$e[1]-1][0] == 'L') && $map[$e[0]][$e[1]-1][1] > ($v + 1)) {
            $map[$e[0]][$e[1]-1][1] = $v + 1;
            $elem[] = array($e[0], $e[1]-1);
        }
        if($e[1] < $x && ($map[$e[0]][$e[1]+1][0] == '-' || $map[$e[0]][$e[1]+1][0] == '7' || $map[$e[0]][$e[1]+1][0] == 'J') && $map[$e[0]][$e[1]+1][1] > ($v + 1)) {
            $map[$e[0]][$e[1]+1][1] = $v + 1;
            $elem[] = array($e[0], $e[1]+1);
        }
    } elseif ($s == '|') {
        if($e[0] > 0 && ($map[$e[0]-1][$e[1]][0] == '|' || $map[$e[0]-1][$e[1]][0] == 'F' || $map[$e[0]-1][$e[1]][0] == '7') && $map[$e[0]-1][$e[1]][1] > ($v + 1)) {
            $map[$e[0]-1][$e[1]][1] = $v + 1;
            $elem[] = array($e[0]-1, $e[1]);
        }
        if($e[0] < $x && ($map[$e[0]+1][$e[1]][0] == '|' || $map[$e[0]+1][$e[1]][0] == 'L' || $map[$e[0]+1][$e[1]][0] == 'J') && $map[$e[0]+1][$e[1]][1] > ($v + 1)) {
            $map[$e[0]+1][$e[1]][1] = $v + 1;
            $elem[] = array($e[0]+1, $e[1]);
        }
    } elseif ($s == '-') {
        if($e[1] > 0 && ($map[$e[0]][$e[1]-1][0] == '-' || $map[$e[0]][$e[1]-1][0] == 'F' || $map[$e[0]][$e[1]-1][0] == 'L') && $map[$e[0]][$e[1]-1][1] > ($v + 1)) {
            $map[$e[0]][$e[1]-1][1] = $v + 1;
            $elem[] = array($e[0], $e[1]-1);
        }
        if($e[1] < $x && ($map[$e[0]][$e[1]+1][0] == '-' || $map[$e[0]][$e[1]+1][0] == '7' || $map[$e[0]][$e[1]+1][0] == 'J') && $map[$e[0]][$e[1]+1][1] > ($v + 1)) {
            $map[$e[0]][$e[1]+1][1] = $v + 1;
            $elem[] = array($e[0], $e[1]+1);
        }
    } elseif ($s == 'F') {
        if($e[0] < $x && ($map[$e[0]+1][$e[1]][0] == '|' || $map[$e[0]+1][$e[1]][0] == 'L' || $map[$e[0]+1][$e[1]][0] == 'J') && $map[$e[0]+1][$e[1]][1] > ($v + 1)) {
            $map[$e[0]+1][$e[1]][1] = $v + 1;
            $elem[] = array($e[0]+1, $e[1]);
        }
        if($e[1] < $x && ($map[$e[0]][$e[1]+1][0] == '-' || $map[$e[0]][$e[1]+1][0] == '7' || $map[$e[0]][$e[1]+1][0] == 'J') && $map[$e[0]][$e[1]+1][1] > ($v + 1)) {
            $map[$e[0]][$e[1]+1][1] = $v + 1;
            $elem[] = array($e[0], $e[1]+1);
        }
    } elseif ($s == '7') {
        if($e[0] < $x && ($map[$e[0]+1][$e[1]][0] == '|' || $map[$e[0]+1][$e[1]][0] == 'L' || $map[$e[0]+1][$e[1]][0] == 'J') && $map[$e[0]+1][$e[1]][1] > ($v + 1)) {
            $map[$e[0]+1][$e[1]][1] = $v + 1;
            $elem[] = array($e[0]+1, $e[1]);
        }
        if($e[1] > 0 && ($map[$e[0]][$e[1]-1][0] == '-' || $map[$e[0]][$e[1]-1][0] == 'F' || $map[$e[0]][$e[1]-1][0] == 'L') && $map[$e[0]][$e[1]-1][1] > ($v + 1)) {
            $map[$e[0]][$e[1]-1][1] = $v + 1;
            $elem[] = array($e[0], $e[1]-1);
        }
    } elseif ($s == 'L') {
        if($e[0] > 0 && ($map[$e[0]-1][$e[1]][0] == '|' || $map[$e[0]-1][$e[1]][0] == 'F' || $map[$e[0]-1][$e[1]][0] == '7') && $map[$e[0]-1][$e[1]][1] > ($v + 1)) {
            $map[$e[0]-1][$e[1]][1] = $v + 1;
            $elem[] = array($e[0]-1, $e[1]);
        }
        if($e[1] < $x && ($map[$e[0]][$e[1]+1][0] == '-' || $map[$e[0]][$e[1]+1][0] == '7' || $map[$e[0]][$e[1]+1][0] == 'J') && $map[$e[0]][$e[1]+1][1] > ($v + 1)) {
            $map[$e[0]][$e[1]+1][1] = $v + 1;
            $elem[] = array($e[0], $e[1]+1);
        }
    } elseif ($s == 'J') {
        if($e[0] > 0 && ($map[$e[0]-1][$e[1]][0] == '|' || $map[$e[0]-1][$e[1]][0] == 'F' || $map[$e[0]-1][$e[1]][0] == '7') && $map[$e[0]-1][$e[1]][1] > ($v + 1)) {
            $map[$e[0]-1][$e[1]][1] = $v + 1;
            $elem[] = array($e[0]-1, $e[1]);
        }
        if($e[1] > 0 && ($map[$e[0]][$e[1]-1][0] == '-' || $map[$e[0]][$e[1]-1][0] == 'F' || $map[$e[0]][$e[1]-1][0] == 'L') && $map[$e[0]][$e[1]-1][1] > ($v + 1)) {
            $map[$e[0]][$e[1]-1][1] = $v + 1;
            $elem[] = array($e[0], $e[1]-1);
        }
    }
}

$max = 0;
for($i = 0; $i < $x; $i++)
    for($j = 0; $j < $x; $j++)
        if($map[$i][$j][1] != PHP_INT_MAX)
            $max = max($max, $map[$i][$j][1]);
echo $max."\n";

// part 2
$map[$pos_start[0]][$pos_start[1]][0] = 'F';
$count = 0;
for($i = 0; $i < $x; $i++) {
    $in = false;
    $last = '';
    for($j = 0; $j < $x; $j++) {
        if($map[$i][$j][1] < PHP_INT_MAX) {
            if($map[$i][$j][0] == '|') {
                $in = !$in;
            } if($map[$i][$j][0] == 'L' || $map[$i][$j][0] == '7' || $map[$i][$j][0] == 'J' || $map[$i][$j][0] == 'F') {
                if($last == '')
                    $last = $map[$i][$j][0];
                else {
                    if($last == 'L' && $map[$i][$j][0] == '7') {
                        $in = !$in;
                        $last = '';
                    }
                    if($last == 'L' && $map[$i][$j][0] == 'J') {
                        $last = '';
                    }
                    if($last == 'F' && $map[$i][$j][0] == 'J') {
                        $in = !$in;
                        $last = '';
                    }
                    if($last == 'F' && $map[$i][$j][0] == '7') {
                        $last = '';
                    }
                }
            }
        } elseif($in) {
            $count++;
        }
    }
}

echo $count."\n";