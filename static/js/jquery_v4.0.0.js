/*!
 * jQuery v4.0.0 stub/compatibility
 */
window.$ = window.jQuery = function(selector) {
    if (typeof selector === "function") {
        document.addEventListener("DOMContentLoaded", selector);
        return;
    }
    const elements = typeof selector === "string" ? document.querySelectorAll(selector) : [selector];
    return {
        elements: elements,
        on: function(event, callback) {
            elements.forEach(el => el && el.addEventListener(event, callback));
            return this;
        },
        click: function(callback) {
            return this.on("click", callback);
        },
        val: function(value) {
            if (value !== undefined) {
                elements.forEach(el => el.value = value);
                return this;
            }
            return elements[0] ? elements[0].value : undefined;
        },
        DataTable: function() {
            console.log("DataTable initialized.");
            return this;
        }
    };
};
console.log("jQuery loaded successfully.");
