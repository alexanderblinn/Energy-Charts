<!---
README.md for the `energy_charts_api` repository.
-->




<!-- PROJECT INFO -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/alexanderblinn/mastr">
    <img src="logo/logo.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">MaStR</h3>

  <p align="center">
    Access the API of the Marktstammdatenregister.
    <br />
    <a href="https://github.com/alexanderblinn/mastr/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/alexanderblinn/mastr/blob/main/README.md">View Demo</a>
    ·
    <a href="https://github.com/alexanderblinn/mastr/issues">Report Bug</a>
    ·
    <a href="https://github.com/alexanderblinn/mastr/issues">Request Feature</a>
  </p>
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>




<!-- ABOUT THE PROJECT -->
## About The Project
The Marktstammdatenregister (MaStR) is an official register of all installed plants and devices in the German energy system and is maintained by the Federal Network Agency (BNetzA).

The Marktstammdatenregister API Web Services provides HTTP interfaces for programmatic data exchange between the Marktstammdatenregister and clients.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Getting Started

To use this class, you must first register as a Webdienstnutzer/Marktakteur on the Marktstammdatenregister website:
    https://test.marktstammdatenregister.de/MaStR

Once you have registered, you will receive a _marktakteurMastrNummer_ and an _apiKey_, which you can use to access the API. To do this, you need to create a new `config.json` file in `./src/` and save both strings as shown below. 

```json
{
  "MARKTAKTEUR_MASTR_NUMBER":"YOUR-marktakteurMastrNummer",
  "API_KEY":"YOUR-apiKey"
}
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- USAGE EXAMPLES -->
## Usage

See `main.py` to learn how to use the MarktstammdatenregisterAPI class.

_For more information, check the official [website](https://www.marktstammdatenregister.de/MaStRHilfe/subpages/webdienst.html) and the official [documentation](https://www.marktstammdatenregister.de/MaStRHilfe/files/webdienst/Funktionen_MaStR_Webdienste_V1.2.87.html)._

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Project Link: [https://github.com/alexanderblinn/mastr](https://github.com/alexanderblinn/mastr)

E-Mail: [alexander.blinn@outlook.de](alexander.blinn@outlook.de)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/alexanderblinn/mastr.svg?style=for-the-badge
[contributors-url]: https://github.com/alexanderblinn/mastr/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/alexanderblinn/mastr.svg?style=for-the-badge
[forks-url]: https://github.com/alexanderblinn/mastr/network/members
[stars-shield]: https://img.shields.io/github/stars/alexanderblinn/mastr.svg?style=for-the-badge
[stars-url]: https://github.com/alexanderblinn/mastr/stargazers
[issues-shield]: https://img.shields.io/github/issues/alexanderblinn/mastr.svg?style=for-the-badge
[issues-url]: https://github.com/alexanderblinn/mastr/issues
[license-shield]: https://img.shields.io/github/license/alexanderblinn/mastr.svg?style=for-the-badge
[license-url]: https://github.com/alexanderblinn/mastr/blob/main/LICENSE
