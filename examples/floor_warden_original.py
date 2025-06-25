#!/usr/bin/env python3
"""
Original Floor Warden Form Filler - Working baseline version
This version works but positioning needs fine-tuning
"""
import fitz

def fill_floor_warden_form_original(input_pdf, output_pdf, form_data):
    """
    Original working version - fills Pages 4 & 5
    """
    
    doc = fitz.open(input_pdf)
    
    # PAGE 4 - Main form fields (ORIGINAL COORDINATES)
    page4 = doc[3]  # Page 4 (0-indexed)
    
    # Original coordinate mapping 
    if 'date' in form_data:
        page4.insert_text((110, 225), form_data['date'], fontsize=11, color=(0, 0, 0))
    
    if 'full_name' in form_data:
        page4.insert_text((190, 252), form_data['full_name'], fontsize=11, color=(0, 0, 0))
    
    if 'floor_unit' in form_data:
        page4.insert_text((190, 279), form_data['floor_unit'], fontsize=11, color=(0, 0, 0))
    
    if 'phone' in form_data:
        page4.insert_text((160, 305), form_data['phone'], fontsize=11, color=(0, 0, 0))
    
    # Handle floor warden choices - place X in appropriate boxes
    if 'floor_warden_choice' in form_data:
        choice = form_data['floor_warden_choice']
        floor_num = form_data.get('floor_number', '')
        
        if choice == 'primary':
            page4.insert_text((62, 470), "X", fontsize=12, color=(0, 0, 0))
            page4.insert_text((430, 470), str(floor_num), fontsize=11, color=(0, 0, 0))
            
        elif choice == 'alternate':
            page4.insert_text((62, 505), "X", fontsize=12, color=(0, 0, 0))
            page4.insert_text((62, 539), str(floor_num), fontsize=11, color=(0, 0, 0))
            
        elif choice == 'either':
            page4.insert_text((62, 574), "X", fontsize=12, color=(0, 0, 0))
            page4.insert_text((110, 608), str(floor_num), fontsize=11, color=(0, 0, 0))
            
        elif choice == 'decline':
            page4.insert_text((62, 643), "X", fontsize=12, color=(0, 0, 0))
    
    # PAGE 5 - Comments and signature
    page5 = doc[4]  # Page 5 (0-indexed)
    
    if 'comments' in form_data:
        comments = form_data['comments']
        lines = comments.split('\n')
        y_position = 188
        for line in lines[:4]:  # Max 4 lines
            page5.insert_text((72, y_position), line, fontsize=10, color=(0, 0, 0))
            y_position += 34  # Move to next line
    
    if 'signature' in form_data:
        page5.insert_text((72, 495), form_data['signature'], fontsize=11, color=(0, 0, 0))
    
    doc.save(output_pdf)
    doc.close()
    print(f"✅ Original filled form saved to: {output_pdf}")

if __name__ == "__main__":
    # Test data
    FORM_DATA = {
        'date': '06/25/2025',
        'full_name': 'Bchan',
        'floor_unit': 'Floor 3, Unit 301',
        'phone': '555-0123',
        'floor_warden_choice': 'primary',
        'floor_number': '3',
        'comments': 'Available for emergency training.\nHave first aid certification.',
        'signature': 'Bchan'
    }
    
    fill_floor_warden_form_original(
        'input_form.pdf',
        'filled_floor_warden_original.pdf',
        FORM_DATA
    )
