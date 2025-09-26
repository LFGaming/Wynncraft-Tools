// ==UserScript==
// @name         Wynncraft Fandom Redirect
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Redirect wynncraft.fandom.com to wynncraft.wiki.gg
// @match        *://wynncraft.fandom.com/*
// @run-at       document-start
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    window.location.replace(
        window.location.href.replace("wynncraft.fandom.com", "wynncraft.wiki.gg")
    );
})();