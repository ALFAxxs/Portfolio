function toggleText(button) {
  const parent = button.closest('.p-4'); // Get the parent container
  const truncatedText = parent.querySelector('.truncated-text');
  const fullText = parent.querySelector('.full-text');

  if (fullText.classList.contains('hidden')) {
    // Show full text and hide truncated text
    fullText.classList.remove('hidden');
    truncatedText.classList.add('hidden');
  } else {
    // Show truncated text and hide full text
    fullText.classList.add('hidden');
    truncatedText.classList.remove('hidden');
  }
}




