# Hand-gesture-presentation

This project uses hand gestures to control a PowerPoint presentation in real-time. The implementation leverages **MediaPipe**, **OpenCV**, and **win32com.client** for gesture recognition and PowerPoint automation.

---

## **Features**
- **Start/Stop Presentation**:
  - Open hand gesture: Start the presentation.
  - Closed fist gesture: Stop the presentation.
- **Slide Navigation**:
  - Move the index finger left: Go to the previous slide.
  - Move the index finger right: Advance to the next slide.
- **Real-Time Display**:
  - Visualize detected gestures with hand landmarks.

---

## **Requirements**

### **Software/Environment**
- Python 3.7 or later
- Windows OS (required for PowerPoint control)

### **Python Libraries**
- opencv-python
- mediapipe
- pywin32

