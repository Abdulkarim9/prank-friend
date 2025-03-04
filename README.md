# 🤡 Are You Dumb? - The Impossible "No" Button Prank

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Evil Level](https://img.shields.io/badge/evil%20level-maximum-red)

A hilariously evil Python prank that creates a window asking "Are you Dumb?" with Yes/No buttons. The twist? The "No" button runs away from the cursor whenever someone tries to click it, making it impossible to click! Your victims will eventually have to click "Yes" to close the window, essentially admitting they're dumb.

![Demo Screenshot](https://i.imgur.com/placeholder-add-your-screenshot.png)

## 😈 Features

- **Impossible "No" Button**: Dodges the mouse cursor whenever it gets close
- **Taunting Messages**: Displays increasingly frustrating messages as they try to deny
- **Attempt Counter**: Tracks how many times they've tried to click "No"
- **Color-Changing UI**: Background changes colors randomly to add to the frustration
- **Stats Screen**: Shows a final screen with attempt count and time spent when they finally give up
- **Modern UI**: Clean, attractive interface with smooth animations

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes with Python installation)

### Setup

1. Clone this repository or download the ZIP file:
   ```bash
   git clone https://github.com/yourusername/are-you-dumb-prank.git
   ```

2. Navigate to the project directory:
   ```bash
   cd are-you-dumb-prank
   ```

3. Run the prank:
   ```bash
   python enhanced_prank_window.py
   ```

## 💻 Usage

### Basic Usage

Simply run the script and watch your friend's frustration grow:

```bash
python enhanced_prank_window.py
```

### Creating an Executable

For extra sneakiness, you can convert the script to an executable so your friends don't see the Python code:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Create the executable:
   ```bash
   pyinstaller --onefile --windowed enhanced_prank_window.py
   ```

3. Find the executable in the `dist` folder

4. Rename it to something innocent like "awesome_game.exe" or "must_see.exe"

## 🔧 Customization Options

Want to make the prank even more personal or evil? Here are some customization options:

### Changing the Question

To change the "Are you Dumb?" text to something else, find this line:
```python
question_label = tk.Label(
    question_frame, 
    text="Are you Dumb?", 
    font=("Arial", 24, "bold"),
    bg="#FFFFFF"
)
```

Change the `text` parameter to whatever question you want.

### Customizing Taunting Messages

You can edit the taunting messages that appear when someone tries to click "No". Find this array:

```python
messages = [
    "Nice try!",
    "Too slow!",
    "Not even close!",
    # ... other messages
]
```

Add, remove, or change messages to your liking!

### Adjusting Difficulty

To make the "No" button even harder (or easier) to click, you can modify these settings:

1. **Button Movement Speed**: Adjust the randomization range in the `move_button` function:
   ```python
   new_x = random.randint(margin, max_x)
   new_y = random.randint(margin, max_y)
   ```

2. **Window Size**: Change the size of the window by modifying:
   ```python
   root.geometry("500x400")
   ```

## 🎮 Prank Ideas

Here are some devious ways to use this prank:

1. **"Check out my new game!"**: Send it to friends claiming it's a cool game you made
2. **Office Prank**: Install it on a coworker's computer during their lunch break
3. **Screen Share Trap**: During a video call, share your screen and ask for help with a "program issue"
4. **Make a Bet**: Bet someone they can't click the "No" button in under 30 seconds

## ⚠️ Disclaimer

This prank is meant for harmless fun. Please use responsibly and consider the person you're pranking. Some people might not appreciate being forced to admit they're dumb, so know your audience!

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♀️ Contributing

Contributions are welcome! Feel free to submit pull requests or open issues if you have ideas for improvements or new features.

1. Fork the repository
2. Create a feature branch: `git checkout -b new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin new-feature`
5. Submit a pull request

## 🌟 Show Your Support

If you found this prank useful or hilarious, please give it a star on GitHub and consider sharing it with friends!

## 📞 Contact

If you have any questions or suggestions, feel free to reach out:

- GitHub: [Your GitHub Profile](https://github.com/yourusername)
- Email: your.email@example.com
- Twitter: [@YourTwitterHandle](https://twitter.com/yourtwitterhandle)

---

Made with ❤️ and a bit of 😈 by [Your Name] 