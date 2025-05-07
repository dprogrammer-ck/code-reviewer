// AvoidWithStatement violation
with (Math) {
    x = cos(2); // PMD should flag this
}

// ConsistentReturn violation
function checkStatus(val) {
    if (val === "ok") {
        return;
    }
    return true;
}

// GlobalVariable violation
function someFunc() {
    accidentalGlobal = 42; // Missing 'var', will be global
    var localVar = 10;
}

// ScopeForInVariable violation
function scopeLeak() {
    var result = {};
    var data = { a: 1, b: 2 };
    for (key in data) { // No 'var' – scope pollution
        result[key] = data[key];
    }
    return result;
}

// UseBaseWithParseInt violation
function parseBad() {
    var num = parseInt("077"); // Missing radix
    return num;
}
