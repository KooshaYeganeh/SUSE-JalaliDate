
---

# openSUSE JalaiDate

`openSUSE JalaiDate` is a command-line tool that provides various date and time functionalities, including conversion between Gregorian and Jalali dates, current time, and system information. It also displays an ASCII art representation of the openSUSE logo.

## Features

- Display current date and time in human-readable and digit formats.
- Convert Gregorian dates to Jalali dates.
- Show system information.
- Print a custom message.
- Provide detailed help and usage information.

## Installation

To use `susejcal.py`, you'll need to have Python installed along with a few dependencies. You can install the necessary Python packages using `pip`.

### Requirements

- Python 3.x
- `persiantools`
- `pytz`
- `colorama`

### Installing Dependencies

You can install the required packages with the following command:

```bash
pip install persiantools pytz colorama
```

## Usage

The script can be run with various command-line arguments to perform different tasks. Here are the available options:

```bash
usage: susejcal.py [options]

Options:
  -h, --human              Show human-readable date
  -d, --digit              Show date in digits
  -v, --verbose            Show both human-readable and digit date
  -i, --info               Show developer information
  -t, --time               Show current time in 24-hour and 12-hour formats
  -w, --weekday            Show current weekday
  -c, --convert YYYY MM DD Convert Gregorian date to Jalali
  -m, --message [message]  Display a custom message
  -s, --system             Show system information
  --help                   Show this help message
```

### Examples

1. **Display the current date in human-readable format:**

   ```bash
   python susejcal.py -h
   ```

2. **Show the date in digits format:**

   ```bash
   python susejcal.py -d
   ```

3. **Convert a Gregorian date to Jalali:**

   ```bash
   python susejcal.py -c 2024 07 11
   ```

4. **Display system information:**

   ```bash
   python susejcal.py -s
   ```

5. **Show developer information:**

   ```bash
   python susejcal.py -i
   ```

## Developer Information

- **Developer:** Koosha Yeganeh
- **GitHub:** [KooshaYeganeh](https://github.com/KooshaYeganeh)
- **DockerHub:** [kooshakooshadv](https://hub.docker.com/u/kooshakooshadv)
- **GitBooks:** [kooshayeganeh.gitbook.io](https://kooshayeganeh.gitbook.io)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes. 

## Acknowledgments

- The ASCII art logo is inspired by the openSUSE project.
- The `persiantools` library is used for Jalali date functionalities.

---

