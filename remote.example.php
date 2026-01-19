<?php declare(strict_types=1);

// try to get ip from post data ...
$ip = $_POST['ip'] ?? null;

if (!$ip) {
    // got no ip
    http_response_code(response_code: 400);
}
else {
    // do something with $ip ...

    // return status code 200 when all good ...
    http_response_code(response_code: 200);
}
