fs = require('fs')

let t = JSON.parse(fs.readFileSync('taxonomy-all.json'))

let out = Object.keys(t).map((v) => {
    return v + '|' + t[v]
}).join('\n')

fs.writeFileSync('all.txt', out)
