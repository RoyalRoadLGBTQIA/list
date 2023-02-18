var $filterCheckboxes = $('input[type="checkbox"]');
var filterFunc = function() {
  
  var selectedFilters = {};
  $filterCheckboxes.filter(':checked').each(function() {

    if (!selectedFilters.hasOwnProperty(this.name)) {
      selectedFilters[this.name] = [];
    }

    selectedFilters[this.name].push(this.value);
  });

  var $filteredResults = $('.entry');
  $.each(selectedFilters, function(name, filterValues) {
    $filteredResults = $filteredResults.filter(function() {

      var matched = false,
        currentFilterValues = $(this).data('category').split(' ');
      $.each(currentFilterValues, function(_, currentFilterValue) {
        if ($.inArray(currentFilterValue, filterValues) != -1) {
          matched = true;
          return false;
        }
      });
      return matched;

    });
  });
  $('.entry').hide().filter($filteredResults).show();
}

$(document).ready(function() {
  // main menu toggle
  var toggleButton = document.getElementById("menu-toggle");
  var menu = document.getElementById("primary-nav");

  if (toggleButton && menu) {
    toggleButton.addEventListener("click", function() {
      menu.classList.toggle("js-menu-is-open");
    });
  }

  // initialize smooth scroll
  $("a").smoothScroll({ offset: -20 });

  // add lightbox class to all image links
  $("a[href$='.jpg'], a[href$='.png'], a[href$='.gif']").attr("data-lity", "");
  filterFunc();
  $filterCheckboxes.on('change', filterFunc);
});