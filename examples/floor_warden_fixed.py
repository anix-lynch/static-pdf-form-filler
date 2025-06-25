#!/usr/bin/env python3
"""
PROPERLY FIXED Floor Warden Form Filler v4
Text positioned to the RIGHT of labels (not below/northeast)
"""
import fitz

def fill_floor_warden_form_fixed(input_pdf, output_pdf, form_data):
    """
    PROPERLY FIXED version - text goes to the RIGHT of labels
    Fixes the northeast positioning issue by placing text correctly
    """
    
    doc = fitz.open(input_pdf)
    
    # PAGE 4 - Main form fields (RIGHT-SIDE POSITIONING)
    page4 = doc[3]  # Page 4 (0-indexed)
    
    # Position text to the RIGHT of each label, not below
    if 'date' in form_data:
        # "Date:" is at x=72, so put text at x=110 (to the right)
        page4.insert_text((110, 225), form_data['date'], fontsize=11, color=(0, 0, 0))
    
    if 'full_name' in form_data:
        # "Print your full name:" ends around x=180, so put text at x=190
        page4.insert_text((190, 252), form_data['full_name'], fontsize=11, color=(0, 0, 0))
    
    if 'floor_unit' in form_data:
        # "Floor and unit number:" ends around x=220, so put text at x=230
        page4.insert_text((230, 279), form_data['floor_unit'], fontsize=11, color=(0, 0, 0))
    
    if 'phone' in form_data:
        # "Telephone number:" ends around x=170, so put text at x=180
        page4.insert_text((180, 305), form_data['phone'], fontsize=11, color=(0, 0, 0))
    
    # Handle floor warden choices with proper checkbox placement
    if 'floor_warden_choice' in form_data:
        choice = form_data['floor_warden_choice']
        floor_num = form_data.get('floor_number', '')
        
        if choice == 'primary':
            page4.insert_text((60, 470), "X", fontsize=12, color=(0, 0, 0))
            # Floor number in the blank after "floor number _______"
            page4.insert_text((460, 470), str(floor_num), fontsize=11, color=(0, 0, 0))
            
        elif choice == 'alternate':
            page4.insert_text((60, 505), "X", fontsize=12, color=(0, 0, 0))
            # Floor number in the blank line
            page4.insert_text((85, 539), str(floor_num), fontsize=11, color=(0, 0, 0))
            
        elif choice == 'either':
            page4.insert_text((60, 574), "X", fontsize=12, color=(0, 0, 0))
            # Floor number after "floor _______"
            page4.insert_text((125, 608), str(floor_num), fontsize=11, color=(0, 0, 0))
            
        elif choice == 'decline':
            page4.insert_text((60, 643), "X", fontsize=12, color=(0, 0, 0))
    
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
        page5.insert_text((75, 485), form_data['signature'], fontsize=11, color=(0, 0, 0))
    
    doc.save(output_pdf)
    doc.close()
    print(f"✅ PROPERLY FIXED filled form saved to: {output_pdf}")

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
    
    fill_floor_warden_form_fixed(
        'input_form.pdf',
        'properly_fixed_form.pdf',
        FORM_DATA
    )
