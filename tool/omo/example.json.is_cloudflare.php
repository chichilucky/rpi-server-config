<?php
/*

How to use json file

1. Download .json files: /cloudflare_users/domains
2. Edit path: "/path/to/jsonfiles/"

*/


/*
	is_listed_cf(string Domain)
	return
		[false, false]: file error
		[true, true]: is cloudflare
		[true, false]: not listed
*/
function is_listed_cf($domain)
{
    if (!in_array($domain[0], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], true)) {
        return [false, false];
    }
    $got = @json_decode(file_get_contents('/path/to/jsonfiles/cloudflare_' . $domain[0] . '.json'), true);
    if (!is_array($got)) {
        return [false, false];
    }
    return isset($got[$domain]) ? [true, true] : [true, false];
}

/*
	is_cloudflare_cached(string Domain)
	return
		true: is cloudflare
		false: not listed
*/
function is_cloudflare_cached($f)
{
    global $tmpCacheCFlist;
    if (!isset($tmpCacheCFlist)) {
        $tmpCacheCFlist = [];
    }
	$d = $f;
    //$d = get_domainname($f)[1];
    if (isset($tmpCacheCFlist[$d])) {
        return $tmpCacheCFlist[$d];
    }
    $tmpCacheCFlist[$d] = is_listed_cf($d)[1] ? true : false;
    return $tmpCacheCFlist[$d];
}


// example

var_dump(is_cloudflare_cached('codeberg.org'));// false

