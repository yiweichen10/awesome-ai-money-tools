(async () => {
  const btn = document.querySelector('[data-testid="tweetButton"]');
  if (btn) {
    btn.click();
    return { success: true };
  } else {
    return { success: false, message: 'Button not found by selector' };
  }
})()