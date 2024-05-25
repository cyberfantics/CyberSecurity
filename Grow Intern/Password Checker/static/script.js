function hideResult () {
  const resultDiv = document.querySelector('.result')
  if (resultDiv) {
    resultDiv.style.display = 'none'
  }
}

document.addEventListener('click', function (event) {
  const resultDiv = document.querySelector('.result')
  const form = document.querySelector('form')
  if (resultDiv && !form.contains(event.target)) {
    hideResult()
  }
})

