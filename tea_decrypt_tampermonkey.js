// ==UserScript==
// @name         tarea3
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Script que capta y descifra un mensaje con el algortimo TEA.
// @author       Javier Urzua Ahumada
// @match        https://lineamingu.github.io/cripto-y-seguridad-2-2020/
// @grant        none
// ==/UserScript==

(function TEA_decrypt() {
    'use strict';

    function strToLongs(s) {
        var l = new Array(Math.ceil(s.length/4));
        for (let i=0; i<l.length; i++) {
            l[i] = s.charCodeAt(i*4) + (s.charCodeAt(i*4+1)<<8) +
                (s.charCodeAt(i*4+2)<<16) + (s.charCodeAt(i*4+3)<<24);
        }
        return l;
    }


    function longsToStr(l) {
        let str = '';
        for (let i=0; i<l.length; i++) {
            str += String.fromCharCode(l[i] & 0xff, l[i]>>>8 & 0xff, l[i]>>>16 & 0xff, l[i]>>>24 & 0xff);
        }
        return str;
    }

    function utf8Encode(str) {
        return unescape(encodeURIComponent(str));
    }

    function utf8Decode(utf8Str) {
        try {
            return decodeURIComponent(escape(utf8Str));
        } catch (e) {
            return utf8Str;
        }
    }

    function base64Encode(str) {
        if (typeof btoa != 'undefined') return btoa(str);
        if (typeof Buffer != 'undefined') return new Buffer(str, 'binary').toString('base64');
        throw new Error('No Base64 Encode');
    }

    function base64Decode(b64Str) {
        if (typeof atob == 'undefined' && typeof Buffer == 'undefined') throw new Error('No base64 decode');
        try {
            if (typeof atob != 'undefined') return atob(b64Str);
            if (typeof Buffer != 'undefined') return new Buffer(b64Str, 'base64').toString('binary');
        } catch (e) {
            throw new Error('Invalid ciphertext');
        }
    }

    function decode(v, k) {
        var n = v.length;
        var delta = 0x9e3779b9;
        var q = Math.floor(6 + 52/n);
        let z = v[n-1], y = v[0];
        let mx, e, sum = q*delta;

        while (sum != 0) {
            e = sum>>>2 & 3;
            for (let p = n-1; p >= 0; p--) {
                z = v[p>0 ? p-1 : n-1];
                mx = (z>>>5 ^ y<<2) + (y>>>3 ^ z<<4) ^ (sum^y) + (k[p&3 ^ e] ^ z);
                y = v[p] -= mx;
            }
            sum -= delta;
        }

        return v;
    }

    function decrypt(ciphertext, password) {
        ciphertext = String(ciphertext);
        password = String(password);

        if (ciphertext.length == 0) return '';

        var v = strToLongs(base64Decode(ciphertext));

        var k = strToLongs(utf8Encode(password).slice(0, 16));

        var plain = decode(v, k);

        var plaintext = longsToStr(plain);

        var plainUnicode = utf8Decode(plaintext.replace(/\0+$/, ''));

        return plainUnicode;
    }

    function get_msg(){
        return document.getElementsByClassName("TEA")[0].id;
    }

    setTimeout(get_msg,500);
    var msg = get_msg();
    var key = "0123456789abcdef"
    var output = decrypt(msg, key)

    console.log(output)

})();
