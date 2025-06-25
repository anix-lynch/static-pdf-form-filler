#!/usr/bin/env python3
"""
Floor Warden Form Filler - Real-world example
Fills a multi-page floor warden registration form with precise coordinate mapping
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import fitz

def fill_floor_warden_form(input_pdf, output_pdf, form_data):
    """
    Fill the floor warden form on pages 4 & 5
    
    form_data should contain:
    - date: Date
    - full_name: Full name
    - floor_unit: Floor and unit number  
    - phone: Telephone number
    - floor_warden_choice: 'primary', 'alternate', 'either', or 'decline'
    - floor_number: Floor number for warden assignment
    - comments: Comments section
    - signature: Name for signature
    """
    
    doc = fitz.open(input_pdf)
    
    # PAGE 4 - Main form fields (precise coordinates)
    page4 = doc[3]  # Page 4 (0-indexed)
    
    if 'date' in form_data:
        page4.insert_text((105, 225), form_data['date'], fontsize=11, color=(0, 0, 0))
    
    if 'full_name' in form_data:
        page4.insert_text((205, 252), form_data['full_name'], fontsize=11, color=(0, 0, 0))
    
    if 'floor_unit' in form_data:
        page4.insert_text((225, 279), form_data['floor_unit'], fontsize=11, color=(0, 0, 0))
    
    if 'phone' in form_data:
        page4.insert_text((185, 305), form_data['phone'], fontsize=11, color=(0, 0, 0))
    
    # Handle floor warden choices with checkboxes
    if 'floor_warden_choice' in form_data:
        choice = form_data['floor_warden_choice']
        floor_num = form_data.get('floor_number', '')
        
        if choice == 'primary':
            page4.insert_text((55, 470), "☑", fontsize=12, color=(0, 0, 0))
            page4.insert_text((435, 470), str(floor_num), fontsize=11, color=(0, 0, 0))
            
        elif choice == 'alternate':
            page4.insert_text((55, 505), "☑", fontsize=12, color=(0, 0, 0))
            page4.insert_text((75, 539), str(floor_num), fontsize=11, color=(0, 0, 0))
            
        elif choice == 'either':
            page4.insert_text((55, 574), "☑", fontsize=12, color=(0, 0, 0))
            page4.insert_text((115, 608), str(floor_num), fontsize=11, color=(0, 0, 0))
            
        elif choice == 'decline':
            page4.insert_text((55, 643), "☑", fontsize=12, color=(0, 0, 0))
    
    # PAGE 5 - Comments and signature
    page5 = doc[4]  # Page 5 (0-indexed)
    
    if 'comments' in form_data:
        comments = form_data['comments']
        lines = comments.split('\\n')
        y_positions = [188, 222, 257, 291]
        
        for i, line in enumerate(lines[:4]):
            if i < len(y_positions):
                page5.insert_text((75, y_positions[i]), line, fontsize=10, color=(0, 0, 0))
    
    if 'signature' in form_data:
        page5.insert_text((75, 495), form_data['signature'], fontsize=11, color=(0, 0, 0))
    
    doc.save(output_pdf)
    doc.close()
    print(f"✅ Floor warden form filled: {output_pdf}")

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
    
    fill_floor_warden_form(
        'input_form.pdf',
        'filled_floor_warden_form.pdf',
        FORM_DATA
    )
