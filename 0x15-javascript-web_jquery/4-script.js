$(document).ready(function() {
    const toggleDiv = $('DIV#toggle_header');
    const headerElement = $('header');
    toggleDiv.click(function () {
        headerElement.toggleClass('red green');
    });
});
