from ultralytics import YOLO
import torch

# torch.cuda.set_device(0)  # Set to your desired GPU number

device = 'gpu' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

model = YOLO('models/best.pt')
#
results = model.predict('videos/video1.mp4', save=True, device='0')
print(results[0])

print('+++++++++++++++')

for box in results[0].boxes:
    print(box)
