
# Exceller

Exceller is a web-based tool for summarizing Excel sheets using Google Generative AI. Users can upload Excel files (.xls, .xlsx, .csv), and Exceller will generate a concise summary of the sheet's content using a natural language processing model.


## Features

- Excel to JSON Conversion: Converts uploaded Excel sheets into JSON format.
- Generative AI Summary: Uses Google's Generative AI to generate a human-readable summary of the sheet data.
- Markdown Support: Displays the generated summary in a proper Markdown format.
- User Interaction:
  - Displays the chosen file's name for confirmation.
  - Allows users to copy the generated summary directly with a button click.
- API Key Configuration: Configurable API key via environment variable for security.


## Tech Stack

**Backend:** Flask

**Frontend:** HTML, CSS, JavaScript

**Libraries:** pandas,
google.generativeai,
marked.js,
dotenv.



## Contributing

Contributions are always welcome!
Feel free to contribute to this project by submitting pull requests, reporting issues, or suggesting improvements!


## License

This project is licensed under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for more details.

## Screenshots

![App Screenshot](https://github.com/prathmesh796/Exceller/blob/main/img/Screenshot%202024-10-02%20174443.png)

![App Screenshot](https://github.com/prathmesh796/Exceller/blob/main/img/Screenshot%202024-10-02%20174514.png)