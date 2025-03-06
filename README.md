# **📌 Python Code with Tests**
🚀 A well-structured Python repository demonstrating how to write **clean, testable code** with **unit tests** using `pytest`.

---

## **📁 Project Structure**
```
.
├── src/               # Source code (business logic)
│   ├── calculator.py  # Basic calculator operations
│   ├── fibonacci.py   # Fibonacci sequence generator
│   ├── palindrome.py  # Palindrome checker
│   ├── __init__.py    # Package initializer
│
├── tests/             # Unit tests
│   ├── test_calculator.py  # Tests for calculator
│   ├── test_fibonacci.py   # Tests for Fibonacci function
│   ├── test_palindrome.py  # Tests for palindrome function
│   ├── __init__.py
│
├── draft/             # Configuration & testing utilities
│   ├── conftest.py    # Pytest configuration
│   ├── pytest.ini     # Pytest settings
│
├── requirements.txt   # Project dependencies
├── .github/workflows  # GitHub Actions for CI/CD (automated testing)
└── README.md          # Project documentation
```

---

## **⚙️ Setup & Installation**
Ensure you have **Python 3.13.2** installed. Then, clone the repo and install dependencies:
```bash
git clone https://github.com/eaedk/code-with-test.git
cd code-with-test
pip install -r requirements.txt
```

---

## **🧪 Running Tests**
This project follows **Test-Driven Development (TDD)** with `pytest`.  
To run tests, use:
```bash
pytest
```
Or, if you want detailed output:
```bash
pytest -v
```

---

## **🛠 Features**
✅ **Calculator** - Addition, subtraction, multiplication, division  
✅ **Fibonacci** - Generate the first `n` Fibonacci numbers  
✅ **Palindrome** - Check if a string is a palindrome  

Each feature is tested to ensure **code reliability** and **maintainability**.

---

## **📌 CI/CD: GitHub Actions**
This project includes **GitHub Actions** to run tests on every push and pull request.  
You can find the workflow in:
```
.github/workflows/test.yml
```
✅ Automatic testing on **push** & **PR**  
✅ Runs with **Python 3.13.2**  
✅ Status Badge : ![Test Status](https://github.com/eaedk/code-with-test/actions/workflows/test.yml/badge.svg)
```

---

## **📜 License**
This project is **open-source** under the MIT License.

---

## **🤝 Contributing**
🚀 Want to contribute? Follow these steps:  
1. Fork the repo  
2. Create a new branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Add feature XYZ"`)  
4. Push to your branch (`git push origin feature-name`)  
5. Open a **Pull Request** 🎉  

---

## **📩 Contact**
For questions, feel free to reach out:  
📧 **Email:** [emmanuelkoupoh@gmail.com]  
🐙 **GitHub:** [github.com/eaedk]  