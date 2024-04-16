let _my_windowId = -1,
   _my_tabId = -1,
   _my_token = '',
   _currentTest = [0, '', ''],
   acGL = new AbortController(),
   acUL = new AbortController(),
   sgGL = acGL.signal,
   sgUL = acUL.signal;
const _apiurl = 'https://karma.crimeflare.eu.org:1984',
   selfActionURL = browser.runtime.getURL('screenshot/action.html');
function sleep(ms) {
   return new Promise((resolve) => {
      setTimeout(resolve, ms);
   });
}
function clean_all() {
   _my_windowId = -1;
   _my_tabId = -1;
   _my_token = '';
   _currentTest = [0, '', ''];
   acGL.abort();
   acGL = new AbortController();
   sgGL = acGL.signal;
   acUL.abort();
   acUL = new AbortController();
   sgUL = acUL.signal;
}
function iquery_issue(_a, _f, _j = '') {
   return new Promise((g, b) => {
      fetch(_apiurl + '/api/mypdns/issue/', {
         signal: sgGL,
         method: 'POST',
         mode: 'cors',
         headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
         },
         body: 'act=' + _a + '&k=' + _my_token + '&f=' + _f + (_j == '' ? '' : '&jdata=' + encodeURIComponent(JSON.stringify(_j)))
      }).then(r => r.json()).then(r => {
         g(r);
      }).catch(e => {
         console.log('Error!', e);
         g([])
      });
   });
}
function iquery_upload(_f, _b) {
   return new Promise((g, b) => {
      fetch(_apiurl + '/api/mypdns/issue/', {
         signal: sgUL,
         method: 'POST',
         mode: 'cors',
         headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
         },
         body: 'act=upload&for=replace&k=' + _my_token + '&f=' + _f + '&body=' + encodeURIComponent(_b)
      }).then(r => r.json()).then(r => {
         g(r);
      }).catch(e => {
         console.log('Error!', e);
         g([])
      });
   });
}
function ui_showmsg(s, ending = false) {
   if (_my_tabId > 0) {
      browser.tabs.update(_my_tabId, {
         url: selfActionURL + '?' + (ending ? 'fin=1&' : '') + 'msg=' + encodeURI(s),
         muted: true
      });
   }
   if (ending) {
      if (_my_windowId > 0) {
         browser.windows.update(_my_windowId, {
            drawAttention: true
         });
      }
      clean_all();
   }
}
browser.browserAction.onClicked.addListener(() => {
   if (_my_windowId < 0) {
      browser.windows.getAll({
         windowTypes: ['popup'],
         populate: true
      }).then(wa => {
         for (let wai of wa) {
            if (wai['tabs'].length > 0) {
               if (wai['tabs'][0]['url'].startsWith(selfActionURL)) {
                  browser.windows.remove(wai['id']);
               }
            }
         }
      });
      clean_all();
      browser.windows.create({
         allowScriptsToClose: false,
         focused: true,
         width: 1000,
         height: 800,
         incognito: true,
         type: 'popup',
         url: 'about:blank'
      }).then(w => {
         _my_windowId = w.id;
         _my_tabId = w['tabs'][0]['id'];
         browser.tabs.update(_my_tabId, {
            muted: true,
            url: selfActionURL
         });
      }, e => {
         console.log('open error! ', e);
      });
   } else {
      browser.windows.update(_my_windowId, {
         focused: true
      });
   }
});
browser.windows.onRemoved.addListener(w => {
   if (_my_windowId > 0 && _my_windowId == w) {
      clean_all();
   }
});
async function checkWinSize() {
   return new Promise((g, b) => {
      if (_my_windowId < 0) {
         g(false);
      } else {
         browser.windows.get(_my_windowId).then(n => {
            if (n.width < 1500 && n.height < 1500) {
               g(true);
            } else {
               g(false);
            }
         }, e => {
            g(false);
         });
      }
   });
}
function get_screenshot() {
   return new Promise((g, b) => {
      if (_my_tabId > 0) {
         browser.tabs.captureTab(_my_tabId, {
            format: 'jpeg',
            quality: 100
         }).then(ss => {
            g([true, ss]);
         }, x => {
            g([false, '']);
         });
      } else {
         g[false, ''];
      }
   });
}
async function step0_tryout() {
   let got;
   got = await checkWinSize();
   if (!got) {
      ui_showmsg('Big screenshot is not allowed.', true);
      return;
   }
   if (_my_tabId < 0) {
      return;
   }
   got = await iquery_issue('badss', 'mypdns.org');
   if (got.length != 2) {
      ui_showmsg('Client Connection Error', true);
      return;
   }
   if (!got[0]) {
      ui_showmsg(got[1], true);
      return;
   }
   if (_my_tabId < 0) {
      return;
   }
   _currentTest = [got[1]['iid'], got[1]['domain'], got[1]['url']];
   step1_loadsite(_currentTest[2]);
}
let isSiteLoaded = false,
   isSiteFinalU = '';
async function step1_loadsite(url) {
   if (_my_tabId < 0) {
      return;
   }
   if (!/^http(|s):\/\//.test(url)) {
      ui_showmsg('Issue ' + _currentTest[0] + ', URL is invalid. Please fix the issue.', true);
      return;
   }
   ui_showmsg('Begin Screenshot<br>Issue ' + _currentTest[0] + '<br>' + _currentTest[1]);
   await sleep(1900);
   isSiteLoaded = false;
   isSiteFinalU = '';
   if (_my_tabId < 0) {
      return;
   }
   browser.tabs.update(_my_tabId, {
      url: _currentTest[2],
      muted: true
   }).then(() => {
      step2_destloaded();
   }, () => {
      ui_showmsg('Firefox Error', true);
   });
}
async function step2_destloaded() {
   if (_my_tabId < 0) {
      return;
   }
   for (i = 0; i < 60; i++) {
      await sleep(500);
      if (isSiteLoaded) {
         //console.log('site loaded! waiting 15s for complete shot');
         await sleep(15000);
         break;
      }
   }
   if (_my_tabId < 0) {
      return;
   }
   let got;
   got = await checkWinSize();
   if (!got) {
      ui_showmsg('Big screenshot is not allowed.', true);
      return;
   }
   if (isSiteLoaded) {
      got = await get_screenshot();
      if (!got[0]) {
         ui_showmsg('Firefox ScreenshotTake error', true);
         return;
      }
      ui_showmsg('Issue ' + _currentTest[0] + ': Uploading Screenshot...');
      got = await iquery_upload(_currentTest[1], got[1]);
      if (got.length != 2) {
         ui_showmsg('Client Connection Error', true);
         return;
      }
      if (!got[0]) {
         ui_showmsg(got[1], true);
         return;
      }
      if (_my_tabId < 0) {
         return;
      }
      got = await iquery_issue('badissuefix', _currentTest[1], [_currentTest[2], isSiteFinalU]);
      if (got.length != 2) {
         ui_showmsg('Client Connection Error', true);
         return;
      }
      if (!got[0]) {
         ui_showmsg(got[1], true);
         return;
      }
      if (_my_tabId < 0) {
         return;
      }
   } else {
      ui_showmsg('Issue ' + _currentTest[0] + ': Reporting...');
      got = await iquery_issue('badissueurl', _currentTest[1]);
      if (got.length != 2) {
         ui_showmsg('Client Connection Error', true);
         return;
      }
      if (!got[0]) {
         ui_showmsg(got[1], true);
         return;
      }
      if (_my_tabId < 0) {
         return;
      }
   }
   _currentTest = [0, '', ''];
   ui_showmsg('Finding Job...');
   step0_tryout();
}
browser.webRequest.onCompleted.addListener(r => {
   if (_my_tabId < 0 || r.tabId != _my_tabId) {
      return;
   }
   isSiteLoaded = true;
   isSiteFinalU = r.url;
   return;
}, {
   types: ['main_frame'],
   urls: ["http://*/*", "https://*/*"]
});
browser.runtime.onMessage.addListener((r, s, sr) => {
   if (r[0] == 'token') {
      _my_token = r[1];
      browser.storage.local.set({
         token: r[1]
      });
      ui_showmsg('Connecting...');
      step0_tryout();
   }
   sr(true);
   return true;
});
