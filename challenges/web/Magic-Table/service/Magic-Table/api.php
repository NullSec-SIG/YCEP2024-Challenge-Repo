<?php
if (isset($_GET['element1']) && isset($_GET['element2'])) {
    $element1 = $_GET['element1'];
    $element2 = $_GET['element2'];

    if (($element1 !== $element2) && ($element1 == $element2)) {
        echo "YCEP24{php_w34k_7yp3_c0mp4r150n5}";
    } else {
        echo "The elements are not equal";
    }
} else {
    echo "Not enough elements selected";
}
?>
