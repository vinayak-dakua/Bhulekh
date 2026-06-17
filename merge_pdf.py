from pypdf import PdfWriter
import os

pdf_folder = r"C:\Users\vinay\Downloads\Merged_Bhulekh"

merger = PdfWriter()

pdf_files = [
    f for f in os.listdir(pdf_folder)
    if f.lower().endswith(".pdf")
]

pdf_files.sort()

print("PDF Count =", len(pdf_files))

for pdf in pdf_files:
    print("Adding:", pdf)

    merger.append(
        os.path.join(pdf_folder, pdf)
    )

output_file = os.path.join(
    pdf_folder,
    "Merged_Bhulekh_Final.pdf"
)

with open(output_file, "wb") as f:
    merger.write(f)

print("\nMerged PDF Created:")
print(output_file)