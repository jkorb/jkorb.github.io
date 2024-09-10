document.getElementById("toggle-all").addEventListener("click", function() {
  var topLevelCollapses = document.querySelectorAll('[data-bs-target^="#collapse-"]');
  
  topLevelCollapses.forEach(function(toggle) {
    var collapseId = toggle.getAttribute('data-bs-target');
    
    if (collapseId) {
      try {
        // Separate the '#' from the actual ID and escape only the ID part
        var idWithoutHash = collapseId.slice(1); // Remove the '#' at the beginning
        var escapeId = '#' + CSS.escape(idWithoutHash); // Escape the ID and prepend the '#'

        var collapseElement = document.querySelector(escapeId);

        if (collapseElement) {
          var collapseInstance = bootstrap.Collapse.getOrCreateInstance(collapseElement);

          if (collapseElement.classList.contains('show')) {
            collapseInstance.hide();
          } else {
            collapseInstance.show();
          }
        } else {
          console.warn("Collapse element not found for ID:", escapeId);
        }
      } catch (e) {
        console.error("Error encountered with Bootstrap Collapse:", e);
      }
    } else {
      console.warn("Invalid data-bs-target attribute found:", toggle);
    }
  });
});

