import win32com.client

class PowerPointController:
    def __init__(self, ppt_path):
        self.powerpoint = win32com.client.Dispatch("PowerPoint.Application")
        self.powerpoint.Visible = True
        self.presentation = self.powerpoint.Presentations.Open(ppt_path)
        self.is_active = False

    def start_presentation(self):
        if not self.is_active:
            self.presentation.SlideShowSettings.Run()
            self.is_active = True
            print("Presentation started")

    def stop_presentation(self):
        if self.is_active and self.presentation.SlideShowWindow:
            self.presentation.SlideShowWindow.View.Exit()
            self.is_active = False
            print("Presentation stopped")

    def next_slide(self):
        if self.is_active and self.presentation.SlideShowWindow:
            self.presentation.SlideShowWindow.View.Next()
            print("Next slide")

    def previous_slide(self):
        if self.is_active and self.presentation.SlideShowWindow:
            self.presentation.SlideShowWindow.View.Previous()
            print("Previous slide")

    def close(self):
        self.presentation.Close()
