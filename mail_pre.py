import torch
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

def check_libraries():
    """Check if required libraries are installed."""
    try:
        import torch
        import transformers
        print(" Required libraries are installed.")
    except ImportError as e:
        print(f" Missing libraries: {e}")
        print("Please install them using: pip install torch transformers")
        exit(1)

def download_model():
    """Load Pretrained Zero-Shot Classification Model with retry mechanism."""
    print(" Downloading model, please wait...")  
    global classifier

    for attempt in range(2):  # Try twice
        try:
            classifier = pipeline(
                "zero-shot-classification",
                model="facebook/bart-large-mnli"
            )
            print(" Model loaded successfully!")
            return
        except Exception as e:
            print(f" Attempt {attempt + 1} failed: {e}")
    
    print(" Model download failed. Check your internet connection and try again.")
    exit(1)

def predict_email_intent(email_text):
    """Predicts whether an email shows interest in purchasing or not."""
    labels = ["Interested in purchasing", "Not interested"]
    try:
        result = classifier(email_text, candidate_labels=labels)
        return result["labels"][0]  # Returns the highest confidence label
    except Exception as e:
        return f" Error in prediction: {e}"

def main():
    """Main function to run the email intent prediction system."""
    check_libraries()
    download_model()

    print("\n Email Intent Prediction System")
    print("Type 'exit' to quit.")

    while True:
        email_text = input("\n Enter email text: ")
        if email_text.lower() == 'exit':
            print(" Exiting program. Goodbye!")
            break
        
        prediction = predict_email_intent(email_text)
        print(f" Prediction: {prediction}")

if __name__ == "__main__": 
    main()
