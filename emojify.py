"""
emojify.py

A simple script that replaces certain words in a user-input sentence with their corresponding emojis.
Supported categories: Food & Drink, Animals & Nature, Smileys & Feelings, Objects & Symbols, Actions & Activities.

Usage:
    Run the script and enter a sentence. Words matching keys in the emoji_dict will be replaced by emojis.
"""


emoji_dict = {
    # Food & Drink
    "pizza": "🍕",
    "burger": "🍔", "fries": "🍟", "taco": "🌮", "sushi": "🍣",
    "cake": "🎂", "icecream": "🍦", "coffee": "☕", "apple": "🍎",
    "banana": "🍌", "grapes": "🍇", "lemon": "🍋", "doughnut": "🍩",
    "popcorn": "🍿", "chocolate": "🍫", "cookie": "🍪",

    # Animals & Nature
    "cat": "🐱", "dog": "🐶", "lion": "🦁", "tiger": "🐯",
    "pig": "🐷", "cow": "🐮", "fish": "🐟", "butterfly": "🦋",
    "snake": "🐍", "chicken": "🐔", "frog": "🐸", "bear": "🐻",
    "penguin": "🐧", "panda": "🐼", "elephant": "🐘",
    "tree": "🌳", "flower": "🌸", "sun": "☀️", "moon": "🌙",

    # Smileys & Feelings
    "happy": "😊", "sad": "😢", "laugh": "😂", "love": "❤️",
    "angry": "😠", "surprised": "😮", "wink": "😉",
    "cool": "😎", "cry": "😭", "kiss": "😘", "sweat": "😅",
    "party": "🥳", "sleep": "😴", "thinking": "🤔",

    # Objects & Symbols
    "phone": "📱", "computer": "💻", "cake": "🎂", "car": "🚗",
    "bicycle": "🚲", "airplane": "✈️", "book": "📚", "light": "💡",
    "music": "🎵", "star": "⭐", "fire": "🔥", "rain": "🌧️",
    "snow": "❄️", "ball": "🏀", "flag": "🏳️",

    # Actions & Activities
    "run": "🏃", "dance": "💃", "swim": "🏊", "eat": "🍴",
    "drink": "🥤", "sleep": "🛌", "write": "✍️", "read": "📖",
}

sentence=input("Enter a text: ")

words=sentence.lower().split()

output=[]

for word in words:
    if word in emoji_dict:
        output.append(emoji_dict[word])
        
    else:
        output.append(word)

print(" ".join(output))