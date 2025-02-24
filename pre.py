import torch
from transformers import pipeline

# 🔹 Load Pretrained Zero-Shot Classification Model
def download_model():
    """Loads the Zero-Shot Classification Model."""
    global classifier
    print("Downloading model, please wait...")
    try:
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Model download failed: {e}")
        exit(1)

# 🔹 Predict Email Intent
def predict_email_intent(email_text):
    """Uses AI to classify email intent dynamically."""
    labels = ["Interested", "Not Interested", "Confused", "Need More Information"]
    try:
        result = classifier(email_text, candidate_labels=labels)
        return result["labels"][0]  # Returns highest confidence label
    except Exception as e:
        return f"Error in prediction: {e}"

# 🔹 Main Function
def main():
    """Runs Email Intent Prediction System."""
    download_model()
    
    print("\nEmail Intent Prediction System")
    print("Type 'exit' to quit.")

    while True:
        email_text = input("\nEnter email text: ")
        if email_text.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break

        prediction = predict_email_intent(email_text)
        print(f"Prediction: {prediction}")

# Run the script
if __name__ == "__main__":
    main()
