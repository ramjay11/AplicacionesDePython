import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile
import os

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath: 
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open file: {filepath}")

def save_file(window, text_edit):
    file = asksaveasfile(filetypes=[("Text Files", "*.txt")])

    if not file:
        return
    filepath = file.name
    try:
        with open(filepath, "w") as f:
            content = text_edit.get(1.0, tk.END)
            f.write(content)
            print("Entered context manager")
        window.title(f"Saved file: {filepath}")
    except Exception as e:
        print(f"Error occurred while saving file: {e}")

class PruebaEditorDeTexto(unittest.TestCase):
    
    @patch('tkinter.filedialog.askopenfilename')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="Test data")
    def test_open_file(self, mock_open, mock_askopenfilename):
        mock_askopenfilename.return_value = "test.txt"
        window = tk.Tk()
        text_edit = tk.Text(window)
        open_file(window, text_edit)
        mock_open.assert_called_with(os.path.basename("test.txt"), "r")
        self.assertEqual(text_edit.get(1.0, tk.END), "Test data")

    @patch('tkinter.filedialog.asksaveasfile')
    def test_save_file(self, mock_asksaveasfile):
        mock_file = MagicMock()
        mock_file.__enter__.return_value.name = "test.txt"
        mock_asksaveasfile.return_value = mock_file
        window = tk.Tk()
        text_edit = tk.Text(window)
        text_edit.insert(tk.END, "Test data")
        save_file(window, text_edit)
        mock_file.__enter__.assert_called_once()
        mock_file.write.assert_called_once_with("Test data")

if __name__ == "__main__":
    unittest.main()