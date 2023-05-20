///////////////////
////// JavaScript for Twitter page
//////////////////



$(function() {
    $('.js-option-icon').click(function() {
        /// $(this) : self element, namely div.js-option-icon
        /// next() : next to div.js-option-icon, namely div.option
        /// toggle() : switch show and hide
        $(this).next().toggle();
    })
})