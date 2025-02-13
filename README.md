# Türkiye Ulusal Adres Veritabanı (TR UAVT) 🇹🇷

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
![Odoo v18.0](https://img.shields.io/badge/Odoo-v18.0-brightgreen.svg)

Odoo module for managing Turkish National Address Database (UAVT - Ulusal Adres Veritabanı).

## Features ✨

- Manage Turkish administrative divisions:
  - Cities (İl) Mapped to Odoo's `res.country.state` model. These represent the 81 cities/provinces (iller) of Türkiye in the address management system.
  - Counties (İlçe/Semt)
  - Districts (Mahalle & Köyler)
  - Streets (Sokak/Cadde)
- Integration with Odoo's base localization
- Support for Turkish characters
- XML data import for administrative regions
- Compatible with Odoo 18.0

## Installation 🛠️

1. Clone this repository into your Odoo addons directory:

```bash
git clone https://github.com/ufuktogay/tr_uavt.git
```

2. Restart your Odoo server to recognize the new module.

3. Install the module from the Odoo Apps menu.

## Usage 📚

### Managing Counties (İlçe)

- Navigate to `TR UAVT > Address Management > Counties`
- View, create, edit or delete county records
- Link counties with corresponding cities

## Development 🚀

To contribute to this module:

1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request

## Data Sources 📊

The address data used in this module is sourced from:
https://github.com/letreset/UAVT

## License 📄

This project is licensed under LGPL-3 - see the LICENSE file for details.

## Support 💬

For support, please contact:

- Website: https://fimeltd.com
- Email: support@fimeltd.com

## Author 👤

Ufuk Togay

## Contributing 🤝

Contributions, issues, and feature requests are welcome!

## Footer

Thank you for using the Türkiye Ulusal Adres Veritabanı (TR UAVT) module!

Please support my country's efforts to ensure the global use of its official name, Türkiye.
