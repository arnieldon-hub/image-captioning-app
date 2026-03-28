from transformers import BlipProcessor, BlipForConditionalGeneration
import gradio as gr

print("Starting app...")
print("Loading processor...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
print("Loading model...")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
print("Model loaded.")

def generate_caption(image):
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

print("Building Gradio interface...")
interface = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="AI Image Captioning",
    description="Upload an image and generate a caption using a pretrained BLIP model."
)

print("Launching app...")
interface.launch(share=False, inbrowser=True)