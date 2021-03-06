from orangewidget import widget, gui
from orangewidget.settings import Setting


class OWProduct(widget.OWBaseWidget):
    name = "Product"
    description = ""
    icon = "icons/Unknown.svg"
    priority = 10
    category = ""
    keywords = ["list", "of", "keywords"]
    outputs = [("Product", int)]
    inputs = [("First factor", int, "get_first"),
              ("Second factor", int, "get_second")]

    want_main_area = False

    def __init__(self):
        super().__init__()

        self.first = self.second = None
        self.product = None

        self.result = gui.label(self.controlArea, self,
                                "%(first)s times %(second)s is %(product)s",
                                box="Result")
        self.result.hide()

    def get_first(self, n):
        self.first = n
        self.do_multiply()

    def get_second(self, n):
        self.second = n
        self.do_multiply()

    def do_multiply(self):
        if self.first and self.second is None:
            self.result.hide()
            self.send("Product", None)
        else:
            self.result.show()
            self.product = self.first * self.second
            self.send("Product", self.product)
