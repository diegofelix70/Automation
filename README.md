# Python Automation Script for Data Entry 🖥️🤖

This Python script automates the process of data entry into a web application using the **PyAutoGUI** library. It demonstrates my ability to automate repetitive tasks, handle data with **Pandas**, and interact with graphical user interfaces (GUIs).
**technology used: Selenium**
---

## 🚀 Key Features

- **Web Automation**: Automates browser navigation, form filling, and data submission.
- **Data Handling**: Reads data from a CSV file using **Pandas** and processes it for input.
- **Error Handling**: Includes a `try-except` block to manage potential errors when reading the CSV file.
- **Dynamic Interaction**: Handles dynamic fields (e.g., optional fields) and scrolls the page as needed.
- **Efficiency**: Uses `pyautogui.PAUSE` and `sleep()` to ensure smooth execution, even on slower systems.

---

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **PyAutoGUI**: For automating mouse and keyboard actions.
- **Pandas**: For reading and processing CSV data.
- **OpenPyXL**: For handling Excel files (not directly used in this script but imported for potential future use).
- **Time Module**: For adding delays to ensure proper execution timing.

---

## 📂 How It Works

1. **Browser Automation**:
   - Opens the browser and navigates to a specific URL.
   - Logs into the web application using predefined credentials.

2. **Data Processing**:
   - Reads product data from a CSV file (`produtos.csv`) using Pandas.
   - Iterates through each row of the CSV file to extract product details.

3. **Form Filling**:
   - Automatically fills out the web form with product details (e.g., code, brand, type, category, price, cost, and observations).
   - Handles optional fields dynamically (e.g., skips empty fields).

4. **Error Handling**:
   - Catches and displays errors if the CSV file cannot be read.

5. **Page Interaction**:
   - Scrolls the page to ensure all fields are accessible.

---

## 🧠 Skills Demonstrated

- **Web Automation**: Using PyAutoGUI to simulate user interactions with a web application.
- **Data Handling**: Reading and processing CSV files with Pandas.
- **Error Handling**: Implementing `try-except` blocks to manage exceptions gracefully.
- **Code Organization**: Writing clean, modular, and reusable code.
- **Problem Solving**: Dynamically handling optional fields and ensuring smooth execution with delays.

---

## 📌 Future Improvements

- Add **logging** to track script execution and errors.
- Implement **command-line arguments** for dynamic input (e.g., CSV file path, credentials).
- Use **Selenium** for more robust browser automation.
- Add **unit tests** to ensure reliability.

---

## 📫 How to Reach Me

If you found this project interesting or have any suggestions, feel free to reach out:

- 📧 Email: [diegofelix70@hotmail.com](mailto:diegofelix70@hotmail.com)
- 💼 LinkedIn: [Diego Felix](https://www.linkedin.com/in/diegofelix70)
- 🐦 Twitter: [@diegofelix70](https://twitter.com/diegofelix70)

---

⭐️ **Tip**: Explore the code to see how automation can simplify repetitive tasks and improve efficiency!
