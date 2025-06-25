#!/usr/bin/env python3
"""
PDF Structure Analyzer
Extracts text positions and page structure for form mapping
"""
import fitz

class PDFAnalyzer:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.doc = None
    
    def analyze_all_pages(self):
        """Analyze all pages and extract text positions"""
        self.doc = fitz.open(self.pdf_path)
        
        print(f"📄 PDF has {self.doc.page_count} pages")
        
        for page_num in range(self.doc.page_count):
            page = self.doc[page_num]
            print(f"\n--- PAGE {page_num + 1} ---")
            
            # Get text with positions
            text_dict = page.get_text("dict")
            
            for block in text_dict["blocks"]:
                if "lines" in block:
                    for line in block["lines"]:
                        for span in line["spans"]:
                            text = span["text"].strip()
                            if text and len(text) > 3:  # Only show meaningful text
                                bbox = span["bbox"]
                                print(f"Text: '{text}' at x={bbox[0]:.0f}, y={bbox[1]:.0f}")
        
        self.doc.close()
    
    def get_page_dimensions(self, page_num=0):
        """Get dimensions of a specific page"""
        self.doc = fitz.open(self.pdf_path)
        page = self.doc[page_num]
        rect = page.rect
        self.doc.close()
        
        return {
            'width': rect.width,
            'height': rect.height
        }

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python pdf_analyzer.py your_file.pdf")
        sys.exit(1)
    
    analyzer = PDFAnalyzer(sys.argv[1])
    analyzer.analyze_all_pages()
