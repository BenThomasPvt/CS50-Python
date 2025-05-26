from fpdf import FPDF


class ShirtificatePDF(FPDF):
    def header(self):
        # Set font for the header
        self.set_font('Arial', 'B', 24)
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')  # Centered title

    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'CS50 - Harvard University', 0, 0, 'C')  # Footer text

    def create_shirtificate(self, user_name):
        self.add_page()

        # Add the shirt image (make sure shirtificate.png exists in the working directory)
        self.image('shirtificate.png', x=50, y=50, w=110)  # Adjust coordinates for the image

        # Set font for the name
        self.set_font('Arial', 'B', 24)
        self.set_text_color(255, 255, 255)  # Set text color to white

        # Add the user name (centered above the shirt)
        self.set_y(80)  # Position for the name
        self.cell(0, 20, f"{user_name} took CS50", 0, 1, 'C')

# Main program logic


def main():
    # Prompt for the user's name
    user_name = input("Enter your name: ")

    # Create PDF
    pdf = ShirtificatePDF()
    pdf.create_shirtificate(user_name)

    # Output the PDF to a file
    pdf.output('shirtificate.pdf')


if __name__ == "__main__":
    main()
