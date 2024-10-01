document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Clear previous summary
    document.getElementById('summary').textContent = '';
    
    // Show loading message
    document.getElementById('loading').style.display = 'block';

    // Disable the upload button to prevent multiple submissions
    const uploadButton = document.querySelector('.upload-btn');
    uploadButton.disabled = true;

    var formData = new FormData();
    var fileInput = document.getElementById('fileInput');
    formData.append('file', fileInput.files[0]);

    fetch('/summarize', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Hide loading message
        document.getElementById('loading').style.display = 'none';

        if (data.summary) {
            // Display the summary in the pre element
            document.getElementById('summary').textContent = data.summary;
        } else {
            // Handle the error and display it to the user
            document.getElementById('summary').textContent = 'Error: ' + data.error;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('summary').textContent = 'An error occurred during the request.';
    })
    .finally(() => {
        // Re-enable the upload button after the process completes
        uploadButton.disabled = false;
    });
});
