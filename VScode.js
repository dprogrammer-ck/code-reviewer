// Unused variable
var unusedVar = 123;

// Function too long and deeply nested
function complexFunction(a, b) {
    var result = 0;

    for (var i = 0; i < 10; i++) {
        if (a > 0) {
            if (b > 0) {
                if (a + b > 10) {
                    console.log("Nested too deep!");
                }
            }
        }
    }

    // Unused function
    function unusedFunction() {
        return "I do nothing";
    }

    return result;
}

// Duplicate code
function duplicate() {
    var message = "This is duplicate";
    console.log(message);
}

function duplicateAgain() {
    var message = "This is duplicate";
    console.log(message);
}
