# Static PDF Form Filler 📋

> Precise coordinate-based PDF form filling for static PDFs using Python + PyMuPDF. No Adobe Acrobat required!

## Problem Solved

Most PDF forms are static (not interactive) and can't be filled programmatically without expensive software like Adobe Acrobat Pro. This tool solves that by:

- ✅ **Analyzing PDF text positions** to find exact coordinates
- ✅ **Mapping form fields** to precise x,y positions
- ✅ **Filling forms accurately** without guesswork
- ✅ **Working with any static PDF** 
- ✅ **100% free and open source**

## Quick Start

### Install Dependencies
```bash
pip install PyMuPDF
```

### Basic Usage
```python
from pdf_form_filler import PDFFormFiller

# Analyze your PDF first
analyzer = PDFAnalyzer('your_form.pdf')
analyzer.analyze_all_pages()

# Fill the form
filler = PDFFormFiller('your_form.pdf')
data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'date': '06/25/2025'
}
filler.fill_form('output.pdf', data)
```

### Real-World Example: Floor Warden Form

See `examples/floor_warden_filler.py` for a complete implementation that fills a multi-page floor warden registration form.

## How It Works

1. **PDF Analysis**: Extract text positions and page structure
2. **Coordinate Mapping**: Map form fields to exact x,y coordinates  
3. **Precise Filling**: Insert text at calculated positions
4. **Quality Control**: Verify alignment and adjust as needed

## Features

- 🎯 **Precise positioning** - No more text floating randomly
- 📄 **Multi-page support** - Handle complex forms across pages
- ☑️ **Checkbox handling** - Place checkmarks exactly where needed
- 📝 **Comments & signatures** - Support for long-form text fields
- 🔧 **Customizable** - Easy to adapt for any PDF form

## File Structure

```
static-pdf-form-filler/
├── README.md
├── requirements.txt
├── pdf_analyzer.py          # PDF structure analysis
├── pdf_form_filler.py       # Main form filling class
├── examples/
│   ├── floor_warden_filler.py
│   └── sample_forms/
└── utils/
    └── coordinate_finder.py  # Interactive coordinate finding
```

## Use Cases

- 📋 **Employment forms** - Job applications, tax forms
- 🏢 **Building management** - Floor warden, maintenance requests
- 📄 **Government forms** - Applications, registrations
- 📊 **Survey forms** - Automated response filling
- 🔄 **Batch processing** - Fill hundreds of forms at once

## Advanced Features

### Interactive Coordinate Finding
```bash
python utils/coordinate_finder.py your_form.pdf
```
Click on the PDF to get exact coordinates for fine-tuning.

### Batch Processing
```python
from pdf_form_filler import BatchProcessor

processor = BatchProcessor('template.pdf')
processor.fill_multiple(data_list, output_dir)
```

## Contributing

1. Fork the repository
2. Add your PDF form template to `examples/`
3. Create a corresponding filler script
4. Submit a pull request

## License

MIT License - feel free to use in commercial projects!

## Credits

Built with love by [Bchan](https://github.com/anix-lynch) using PyMuPDF.

---

⭐ **Star this repo** if it saved you from buying Adobe Acrobat Pro!
