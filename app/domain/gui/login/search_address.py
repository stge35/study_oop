import tkinter as tk

class SearchAddress:

    def __init__(self, window):
        self.window = window
        self.window.title("주소 검색")
        self.window.geometry("800x400")
        self.window.resizable(False, False)

        self._create_header_frame()
        self._create_body_frame()
        self._create_bottom_frame()

    def _create_header_frame(self):
        header_frame = tk.Frame(self.window, bg = "white", height = 30)
        header_frame.pack(fill = "x", side = "top")
        header_frame.pack_propagate(False)

        title_label = tk.Label(
            header_frame,
            text = "주소 검색",
            font = ("맑은 고딕",  11, "bold"),
            fg = "#666666"
        )
        title_label.pack(side = "left", padx = 20)

    def _create_body_frame(self):
        body_frame = tk.Frame(self.window, bg = "#F8FAFC", padx = 15, pady = 15)
        body_frame.pack(fill = "both", expand = True)

        search_input_frame = tk.Frame(body_frame, bg = "#F8FAFC")
        search_input_frame.pack(fill = "x", pady = (0, 10))

