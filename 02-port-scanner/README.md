# 🔎 Port Scanner

A multi-threaded TCP port scanner built in Python. This tool allows scanning single ports or ranges, listing open ports, and performing basic banner grabbing for service identification.
> ⚠️ **Ethical Use Warning**
> This tool is intended for **educational and authorized use only**. Unauthorized port scanning may be illegal.

## 🚀 Features

* Scan a single port or a range/list of ports (e.g., `22`, `20-100`, or `22,80,443,1000-2000`)
* Multi-threaded scanning for improved performance (`--threads`)
* Optional banner grabbing for basic service fingerprinting (`--banner`)
* Safety cap on maximum ports to prevent accidental large scans
* Graceful error handling (timeouts, DNS issues, keyboard interrupts)
* Beginner-friendly and easy to extend

## 📦 Requirements

* Python **3.9+** (tested on 3.10/3.11)
* Uses only the Python standard library

Optional for development:
* `pytest` for testing
* `ruff` or `flake8` for linting
* `black` for code formatting

## ⚡ Usage

```bash
# Scan a single port
python port_scanner.py --target 127.0.0.1 --port 22
# Scan a range of ports
python port_scanner.py --target example.com --ports 20-1024
# Scan multiple ranges/ports
python port_scanner.py --target 192.168.1.10 --ports 22,80,443,8000-8100
# Enable banner grabbing
python port_scanner.py --target example.com --ports 21-25 --banner
# Adjust performance parameters
python port_scanner.py --target localhost --ports 1-1024 --threads 200 --timeout 0.5
```

## 🧪 Testing

```bash
# Install dev dependencies (if applicable)
pip install -r requirements-dev.txt
# Run tests
pytest
```
Includes sample tests for port parsing and scanning against a local test server.

## 🛠 Development

* Lint code: `ruff check .` or `flake8 .`
* Format code: `black .`
* Continuous Integration: GitHub Actions workflow runs linting and tests on every push


## 🏗 Future Improvements

* Asyncio implementation for non-blocking scans
* Enhanced protocol probes (e.g., HTTP HEAD, SMTP EHLO)
* Export results to JSON/CSV
* Docker containerization for portability


## ⚠️ Legal Disclaimer

This tool should only be used on networks and systems you own or are explicitly authorized to test. The author is not responsible for misuse or damage caused by this tool.
