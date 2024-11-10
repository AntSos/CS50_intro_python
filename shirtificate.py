from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf_shirt = PDF(name)
    pdf_shirt.save("shirtificate.pdf")


class PDF:
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 60)
        self._pdf.cell(
            0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C"
        )
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(txt=f"{name} took CS50", x=47.5, y=140)

    def save(self, name):
        self._pdf.output(name)


if __name__ == "__main__":
    main()
