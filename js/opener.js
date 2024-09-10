document.addEventListener("DOMContentLoaded", function() {
  function expandParents(element) {
    if (!element) return;
    var collapseParent = element.closest('.collapse');
    if (collapseParent) {
      var bsCollapseParent = new bootstrap.Collapse(collapseParent, {
        toggle: false
      });
      bsCollapseParent.show();
      expandParents(collapseParent.parentElement);
    }
  }

  var urlFragment = window.location.hash;

  if (urlFragment) {
    var fragmentId = urlFragment.substring(1);
    
    var collapseElement = document.getElementById("collapse-" + fragmentId);
    
    if (collapseElement) {
      var bsCollapse = new bootstrap.Collapse(collapseElement, {
        toggle: false
      });
      bsCollapse.show();
      
      expandParents(collapseElement);

      var headingElement = document.getElementById("heading-" + fragmentId);
      if (headingElement) {
        headingElement.scrollIntoView();
      }
    }
  }
});
