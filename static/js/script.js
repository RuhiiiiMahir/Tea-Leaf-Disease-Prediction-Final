document.getElementById('fileInput').addEventListener('change', function(event) {
  const files = event.target.files;
  if (files.length > 0) {
      const formData = new FormData();
      formData.append('file', files[0]);

      fetch('/predict', {
          method: 'POST',
          body: formData
      })
      .then(response => response.json())
      .then(data => {
          if (data.error) {
              document.getElementById('predictionResults').innerText = `Error: ${data.error}`;
          } else {
              document.getElementById('predictionResults').innerText = `Prediction: ${data.prediction}`;
          }
      })
      .catch(error => {
          document.getElementById('predictionResults').innerText = `Error: ${error.message}`;
      });
  }
});
