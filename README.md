

# Media Renamer

Welcome to the Media Renamer project! This tool helps you rename media files (videos and subtitles) in a specified directory based on a format you provide. It also offers the option to delete obsolete files that aren't video or subtitle files. The renaming process utilizes the Gemini API to generate new names based on your specified format.


## Index

1. [Features](#features)
2. [Supported Formats](#supported-formats)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Example](#example)
6. [Compatibility](#compatibility)
7. [Contributing](#contributing)
8. [Acknowledgements](#acknowledgements)
9. [License](#license)

---

## Features

- **Rename Media Files**: Automatically rename video files in a directory based on your specified format.
- **Delete Obsolete Files**: Optionally delete files that are neither video nor subtitle files.
- **User-Friendly Prompts**: Interactive prompts guide you through the renaming process.
- **Gemini API Integration**: Utilizes Google Gemini API for accurate file renaming.

---

## Supported Formats

- **Video Formats**: `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.m4v`, `.mpg`, `.mpeg`, `.3gp`, `.3g2`, `.webm`, `.vob`, `.ogv`, `.ts`
- **Subtitle Formats**: `.srt`, `.vtt`, `.sbv`, `.sub`, `.ass/.ssa`, `.dfxp`

Feel free to adjust these formats to suit your needs. Simply modify the format tuples in the beginning of the python script.

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/media-renamer.git
   cd media-renamer
   ```

2. **Install Dependencies**

   ```bash
   pip install google-generativeai
   ```

3. **Set Up Gemini API Key**

   Obtain your API key from Google Gemini and set it as an environment variable.

   ```bash
   export GOOGLE_API_KEY='your_api_key_here'  # On Windows use `set GOOGLE_API_KEY=your_api_key_here`
   ```

---

## Usage

1. **Run the Program**

   ```bash
   python Automated.py
   ```

2. **Follow the Prompts**

   - Enter the directory containing the media files you want to rename.
   - Provide the format for renaming the files.
   - Give an example of a current file name and the desired output format for the new name.
   - Decide whether to delete obsolete files or not.

---

## Example

```
Welcome to Media Renamer!

Please enter the directory to be renamed: 
/path/to/your/directory

Please enter the format you would like the files to be renamed in: 
{show name} SXXEXX {title name}

Enter an example name to be changed: 
Thisshow.S1.EP20.ThisSource.1080pABC.mp4

Enter the accurate output desired for the given example: 
This Show S01E20 That Source.mp4

File with name Thisshow.S1.EP20.ThisSource.1080pABC.mp4 renamed to This Show S01E20 That Source.mp4 successfully.

Do you want to delete obsolete files in this directory? 
1. Yes 
2. No
1

X files in the directory /path/to/your/directory renamed and Y obsolete files deleted successfully.

Do you want to rename any other directory? 
1. Yes 
2. No
2

Thank you for using Media Renamer! :)
```

---

## Compatibility

- **Operating Systems**: Compatible with Windows, macOS, and Linux distributions.
- **Python Versions**: Supports Python 3.x and above.
- **Dependencies**: Requires `google-generativeai` library and Python standard libraries.

---

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions to enhance functionality or fix bugs are welcome.

---

## Acknowledgements

We thank the Google Gemini API for its powerful renaming capabilities and all users for their support and feedback. Happy renaming!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using Media Renamer! If you have any issues or suggestions, please open an issue on GitHub. ^-^

