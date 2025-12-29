# How to Add Images to Your Code Journal

This guide explains how to properly add images to your journal entries on GitHub.

## Method 1: Upload Images to the Repository (Recommended for Simple Images)

1. **Add the image file to your repository:**
   ```bash
   git add image-name.png
   git commit -m "Add image for journal entry"
   git push
   ```

2. **Reference the image using GitHub raw URL:**
   ```markdown
   ![alt text](https://github.com/n1t5ua5/code-journal/raw/main/image-name.png)
   ```
   
   Replace:
   - `n1t5ua5` with your GitHub username
   - `code-journal` with your repository name
   - `main` with your branch name (if different)
   - `image-name.png` with your image filename

## Method 2: Upload Images via GitHub Issue (Recommended for Screenshots)

1. **Go to GitHub Issues:**
   - Navigate to any issue or create a new one
   - You can also edit your markdown file directly in GitHub's web interface

2. **Drag and drop or paste your image:**
   - GitHub will automatically upload it and generate a URL like:
   ```markdown
   ![image](https://github.com/user-attachments/assets/86d7e78b-d0ee-4dd7-8c13-0660ee6c8676)
   ```

3. **Copy the generated URL and use it in your journal**

## Method 3: Using HTML img tag (When You Need Size Control)

```html
<img width="940" height="448" alt="image" src="https://github.com/user-attachments/assets/56cadbfa-0436-4810-a992-0a5db5142196" />
```

This method allows you to specify exact dimensions for your images.

## ❌ What NOT to Do

**Don't use relative paths like this:**
```markdown
![alt text](image.png)
```

This will only work locally and won't display on GitHub when others view your repository.

## Examples from Your Journal

Looking at your existing entries, you've successfully used:

- **GitHub raw URLs:**
  ```markdown
  ![alt text](https://github.com/n1t5ua5/code-journal/raw/main/image-1.png)
  ```

- **GitHub asset URLs (from Issue upload):**
  ```markdown
  ![image](https://github.com/user-attachments/assets/86d7e78b-d0ee-4dd7-8c13-0660ee6c8676)
  ```

- **HTML with size specifications:**
  ```html
  <img width="940" height="448" alt="image" src="https://github.com/user-attachments/assets/56cadbfa-0436-4810-a992-0a5db5142196" />
  ```

All three methods work great on GitHub!
