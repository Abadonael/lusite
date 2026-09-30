// Verify browser-storage side effects and usable appearance when storage fails.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync('hugo-site/static/js/theme-toggle.js', 'utf8');

function scenario(saved, systemDark, blocked = false) {
  let theme = null, click;
  const writes = [];
  const storage = {
    getItem(key) { assert.equal(key, 'site-theme'); if (blocked) throw Error('blocked'); return saved; },
    setItem(key, value) { if (blocked) throw Error('blocked'); writes.push([key, value]); },
    removeItem() { throw Error('Unexpected storage deletion'); }
  };
  const html = {
    setAttribute(key, value) { assert.equal(key, 'data-theme'); theme = value; },
    removeAttribute() { theme = null; },
    getAttribute() { return theme; }
  };
  const button = {addEventListener(event, fn) {assert.equal(event, 'click'); click = fn;}};
  vm.runInNewContext(source, {
    document: {documentElement: html, querySelector() {return button;}, addEventListener(_, fn) {fn();}},
    localStorage: storage, window: {matchMedia() {return {matches: systemDark};}}
  });
  assert.deepEqual(writes, [], 'Page load must not write storage');
  assert.equal(theme, saved === 'dark' || saved === 'light' ? saved : null);
  click();
  const currentDark = saved === 'dark' || (saved !== 'light' && systemDark);
  assert.equal(theme, currentDark ? 'light' : 'dark');
  assert.deepEqual(writes, blocked ? [] : [['site-theme', theme]]);
  click();
  assert.equal(theme, currentDark ? 'dark' : 'light');
}
for (const dark of [false, true]) {
  for (const saved of [null, 'dark', 'light', 'invalid']) scenario(saved, dark);
  scenario(null, dark, true);
}
console.log('Theme: 10 scenarios passed (no initial writes, system/saved theme, blocked storage).');
