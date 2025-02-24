# Email Intent Prediction System  

## 🔹 Overview  
This Python script utilizes a **Zero-Shot Classification Model** from **Hugging Face Transformers** to analyze and predict the intent behind email text.  

## 🔹 How It Works  
1. **Downloads a Pretrained Model** → `facebook/bart-large-mnli`
2. **Classifies Email Intent** → Based on predefined labels:  
   - **Interested**  
   - **Not Interested**  
   - **Confused**  
   - **Need More Information**  
3. **Interactive CLI** → Users can enter email text and receive intent predictions in real time.  

## 🔹 Requirements  
Ensure you have **Python 3.8+** installed.  

### Install Dependencies:  
```bash
pip install torch transformers
🔹 How to Run
bash
Copy
Edit
python script_name.py
Replace script_name.py with the actual filename.

🔹 Usage
Type or paste an email message when prompted.
The AI will predict the intent of the email.
Type exit to close the program.
🔹 Example Run
bash
Copy
Edit
Email Intent Prediction System  
Type 'exit' to quit.  

Enter email text: Hello, I'm interested in your product.  
Prediction: Interested  

Enter email text: I don't think this is a good fit.  
Prediction: Not Interested  

Enter email text: exit  
Exiting program. Goodbye!  
🔹 Notes
Requires an internet connection to download the model.
If the model fails to load, check your network or reinstall dependencies.
🔹 Author
Developed using Hugging Face Transformers and PyTorch
Open-source and modifiable for personal or commercial use.
vbnet
Copy
Edit

Let me know if you want any modifications! 🚀







