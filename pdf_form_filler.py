#!/usr/bin/env python3
"""
PDF Form Filler - Main class for filling static PDF forms
"""
import fitz

class PDFFormFiller:
    def __init__(self, input_pdf_path):
        self.input_pdf_path = input_pdf_path
    
    def fill_form(self, output_pdf_path, field_mapping, page_mappings=None):
        """
        Fill PDF form with provided data
        
        Args:
            output_pdf_path: Where to save filled PDF
            field_mapping: Dict of {field_name: value}
            page_mappings: Dict of {field_name: {'page': int, 'x': int, 'y': int, 'font_size': int}}
        """
        doc = fitz.open(self.input_pdf_path)
        
        if page_mappings:
            for field_name, field_data in page_mappings.items():
                if field_name in field_mapping:
                    page = doc[field_data['page']]
                    page.insert_text(
                        (field_data['x'], field_data['y']),
                        str(field_mapping[field_name]),
                        fontsize=field_data.get('font_size', 11),
                        color=(0, 0, 0)
                    )
        
        doc.save(output_pdf_path)
        doc.close()
        print(f"✅ Form filled and saved to: {output_pdf_path}")
    
    def add_checkbox(self, page_num, x, y, checked=True):
        """Add a checkbox mark at specific coordinates"""
        doc = fitz.open(self.input_pdf_path)
        page = doc[page_num]
        
        symbol = "☑" if checked else "☐"
        page.insert_text((x, y), symbol, fontsize=12, color=(0, 0, 0))
        
        doc.close()

class BatchProcessor:
    """Process multiple forms with different data"""
    
    def __init__(self, template_pdf_path):
        self.template_pdf_path = template_pdf_path
    
    def fill_multiple(self, data_list, output_dir, page_mappings=None):
        """Fill multiple forms from a list of data"""
        for i, data in enumerate(data_list):
            filler = PDFFormFiller(self.template_pdf_path)
            output_path = f"{output_dir}/filled_form_{i+1}.pdf"
            filler.fill_form(output_path, data, page_mappings)
