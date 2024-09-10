function copyContent(idSuffix) {
  const spanId = 'copy-' + idSuffix;
  const spanElement = document.getElementById(spanId);
  if (spanElement) {
    const textToCopy = spanElement.textContent || spanElement.innerText;
    navigator.clipboard.writeText(textToCopy).then(function() {
    }, function(err) {
      });
  }
}
