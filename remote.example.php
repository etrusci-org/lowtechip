<?php declare(strict_types=1);


// The `secret` is used to authenticate the request.
// Without it, everyone could send random IP's here.
// The value here must be the same as the value from `notify_secret` in your conf.json file.
$notify_secret = 'change_me';


// Get `ip` and `secret` from post data:
$ip = $_POST['ip'] ?? null;
$secret = $_POST['secret'] ?? null;


// Do nothing if either `ip` or `secret` are missing:
if (!$ip || !$secret)
{
    http_response_code(response_code: 400);
    exit;
}


// Do nothing if `secret` values don't match:
if ($secret != $notify_secret)
{
    http_response_code(response_code: 401);
    exit;
}


// We got an ip and a valid secret if we reach this line.


// Do something with ip.


// Return status code 200 when all good:
http_response_code(response_code: 200);


// Or a code that is not 200 if something went wrong:
// http_response_code(response_code: 400);
