<?php
error_reporting(0);
header('HTTP/1.1 404 Not Found');
header('Access-Control-Allow-Origin: *');
header('Cache-Control: private, no-cache, no-store, max-age=0');
//
// { Example API for IsAT }
//
define('JSON_DIR', 'listdata/');
//
//
if (!file_exists(JSON_DIR) || !file_exists(JSON_DIR . 'antitor_e.json'))
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
$got = @json_decode(file_get_contents(JSON_DIR . 'antitor_' . $fqdn[0] . '.json') , true);
if (!is_array($got))
{
    die('File Error');
}
echo (isset($got[$fqdn]) ? '[true,true]' : '[true,false]');