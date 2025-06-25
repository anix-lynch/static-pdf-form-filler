#!/usr/bin/env python3
"""
PRECISION Floor Warden Form Filler v3
Fixed coordinates based on actual form analysis - no more northeast drift!
"""
import fitz

def fill_floor_warden_form_precision(input_pdf, output_pdf, form_data):
    """
    PRECISION version with proper coordinate alignment
    Based on actual PDF text positions - fixes the 45° northeast issue
    """
    
    doc = fitz.open(input_pdf)
    
    # PAGE 4 - Main form fields (PRECISION COORDINATES)
    page4 = doc[3]  # Page 4 (0-indexed)
    
    # FIXED positioning - no more northeast drift
    if 'date' in form_data:
        # Position right after "Date:" at proper baseline
        page4.insert_text((95, 225), form_data['date'], fontsize=11, color=(0, 0, 0))
    
    if 'full_name' in form_data:
        # Position on the actual baseline after label
        page4.insert_text((72, 270), form_data['full_name'], fontsize=11, color=(0, 0, 0))
    
    if 'floor_unit' in form_data:
        # Aligned with form field baseline
        page4.insert_text((72, 297), form_data['floor_unit'], fontsize=11, color=(0, 0, 0))
    
    if 'phone' in form_data:
        # Proper baseline alignment
        page4.insert_text((72, 323), form_data['phone'], fontsize=11, color=(0, 0, 0))
    
    # Handle floor warden choices - precise checkbox placement
    if 'floor_warden_choice' in form_data:
        choice = form_data['floor_warden_choice']
        floor_num = form_data.get('floor_number', '')
        
        if choice == 'primary':
            page4.insert_text((60, 470), "X", fontsize=12, color=(0, 0, 0))
            page4.insert_text((450, 470), str(floor_num), fontsize=11, color=(0, 0, 0))
            
        elif choice == 'alternate':
            page4.insert_text((60, 505), "X", fontsize=12, color=(0, 0, 0))
            page4.insert_text((80, 539), str(floor_num), fontsize=11, color=(0, 0, 0))
            
        elif choice == 'either':
            page4.insert_text((60, 574), "X", fontsize=12, color=(0, 0, 0))
            page4.insert_text((120, 608), str(floor_num), fontsize=11, color=(0, 0, 0))
            
        elif choice == 'decline':
            page4.insert_text((60, 643), "X", fontsize=12, color=(0, 0, 0))
    
    # PAGE 5 - Comments and signature (PRECISION)
    page5 = doc[4]  # Page 5 (0-indexed)
    
    if 'comments' in form_data:
        comments = form_data['comments']
        lines = comments.split('\\n')
        y_positions = [188, 222, 257, 291]
        
        for i, line in enumerate(lines[:4]):
            if i < len(y_positions):
                page5.insert_text((75, y_positions[i]), line, fontsize=10, color=(0, 0, 0))
    
    if 'signature' in form_data:
        page5.insert_text((75, 485), form_data['signature'], fontsize=11, color=(0, 0, 0))
    
    doc.save(output_pdf)
    doc.close()
    print(f"✅ PRECISION filled form saved to: {output_pdf}")

if __name__ == "__main__":
    # Example usage
    FORM_DATA = {
        'date': '06/25/2025',
        'full_name': 'Bchan',
        'floor_unit': 'Floor 3, Unit 301',
        'phone': '555-0123',
        'floor_warden_choice': 'primary',
        'floor_number': '3',
        'comments': 'Available for emergency training.\\nHave first aid certification.',
        'signature': 'Bchan'
    }
    
    fill_floor_warden_form_precision(
        'input_form.pdf',
        'precision_filled_form.pdf',
        FORM_DATA
    )
