<?php
error_reporting(0);
header('HTTP/1.1 404 Not Found');
header('Access-Control-Allow-Origin: *');
header('Cache-Control: private, no-cache, no-store, max-age=0');
//
// { Example API for IsMM }
//
define('JSON_DIR', 'listdata/');
//
//
if (!file_exists(JSON_DIR) || !file_exists(JSON_DIR . 'cloudflare_e.json'))
{
    die('File Not Found');
}
elseif ($_SERVER['REQUEST_METHOD'] != 'POST')
{
    echo ('OK');
    exit;
}
header('Content-Type: application/json');
$fqdn = htmlspecialchars($_POST['f']);
if (!preg_match("/^([a-z0-9]{1})([a-z0-9.-]{0,254})\.([a-z]{2,50})$/", $fqdn))
{
    echo ('[false,false]');
    exit;
}
$domains = [];
$fqdnP = array_reverse(explode('.', $fqdn));
$domains[] = $fqdnP[1] . '.' . $fqdnP[0];
if (isset($fqdnP[2]))
{
    $domains[] = $fqdnP[2] . '.' . $fqdnP[1] . '.' . $fqdnP[0];
}
foreach ($domains as $domain)
{
    $got = @json_decode(file_get_contents(JSON_DIR . 'cloudflare_' . $domain[0] . '.json') , true);
    if (!is_array($got))
    {
        echo ('[false,false]');
        exit;
    }
    if (isset($got[$domain]))
    {
        echo ('[true,true]');
        exit;
    }
}
echo ('[true,false]');