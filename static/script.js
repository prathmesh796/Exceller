document.getElementById('copyButton').addEventListener('click', function() {
    var summaryText = document.getElementById('summary').innerText;

    if (summaryText) {
        // Create a temporary textarea element to hold the text
        var tempTextArea = document.createElement('textarea');
        tempTextArea.value = summaryText;
        document.body.appendChild(tempTextArea);

        // Select the text and copy it to the clipboard
        tempTextArea.select();
        document.execCommand('copy');

        // Remove the temporary element
        document.body.removeChild(tempTextArea);

        // Provide feedback to the user
        alert('Summary copied to clipboard!');
    } else {
        alert('No summary to copy.');
    }
});

document.getElementById('fileInput').addEventListener('change', function(event) {
    var fileInput = event.target;
    var fileNameDisplay = document.getElementById('fileName');

    if (fileInput.files.length > 0) {
        // Display the name of the first selected file
        fileNameDisplay.textContent = 'Selected file: ' + fileInput.files[0].name;
    } else {
        // If no file is selected, clear the display
        fileNameDisplay.textContent = '';
    }
});

document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Clear previous summary
    document.getElementById('summary').innerHTML = '';
    
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
            // Convert the markdown to HTML using Marked.js
            const htmlContent = marked.parse(data.summary);
            // Display the HTML content in the 'summary' section
            document.getElementById('summary').innerHTML = htmlContent;
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
