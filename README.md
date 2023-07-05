  <h3 align="center">Readability-Index-Calculator</h3>

  <p align="center">
    Simple readability index and readability score calculator for English and Russian texts.
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

This Readability Index Calculator is a Python program that calculates various readability indexes for both English and Russian texts. The calculator includes the following readability indexes:

- Gunning Fog Index
- Flesch Readability Score
- Coleman Liau Index
- Automated Readability Index
- Dale–Chall Readability Score

Gunning Fog Index and Flesch Readability Score have separate formulas for English and Russian texts. The program detects language of the input text automatically and applies an appropriate formula. Dale–Chall Score can be calculated only for English texts since it heavily relies on Dale-Chall Word List which is made specifically for English language.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- STRUCTURE -->
## Project Structure

The project consists of 3 modules: stats.py, formulas.py and GUI.py.

### stats.py

This module contains functions that calculate quantitative text characteristics required to calculate a readability index using different formulas. These characteristics include:

- Number of sentences in a given text
- Number of words in a given text
- Average sentence length in words
- Average word length in syllables
- Number of long words
- Number of difficult words according to the Dale-Chall list
- Average number of characters per 100 words
- Average number of sentences per 100 words

### formulas.py

This module contains different formulas that calculate a readability index based on the quantitative text characteristics calculated in the `stats.py` module. Function for each formula returns the readability index of the given texts. Functions returning data (specifically, age or education level required to understand the given text) on different readability indexes are presenthere as well.

### GUI.py

This module contains code for the graphical user interface (GUI) that allows users to easily input their text into the program and choose the desired readability formula for score calculation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

To use the Readability Index Calculator, follow these steps:

1. Install the required packages: spaCy, textstat, and langdetect;
2. Run GUI.py module;
3. Enter your text into an input box;
4. Press the button with the name of the desired index.

![изображение](https://github.com/Shinju-M/Readability-Index-Calculator/assets/120586885/b4841053-8e20-4871-a412-547976aeac91)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions to this project are welcome! If you have any suggestions and improvements, please fork the repo and create a pull request. You can also simply open an issue.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Margarita Soloveva - [@Shinju_M](https://t.me/Shinju_M) - flyingadelie@gmail.com

Project Link: [https://github.com/Shinju-M/Readability-Index-Calculator/](https://github.com/Shinju-M/Readability-Index-Calculator/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
