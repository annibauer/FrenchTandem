import difflib
from .db_management import save_message


def analyze_reply(reply, user_message, session_id):
    save_message("user", user_message, session_id)
    
    #if no correction is sent
    if reply.find("CORRECTION: ") != -1:
        reply_text = reply.split('CORRECTION: ')[0]
        correction_text = reply.split('CORRECTION: ')[1]
        highlighted_text = highlight_text_differences(user_message, correction_text)

        save_message("correction", highlighted_text, session_id)
        
    else: 
        reply_text = reply
        
    save_message("tandem", reply_text, session_id)

    
def highlight_text_differences(original_text, corrected_text):
        matcher = difflib.SequenceMatcher(None, original_text, corrected_text)
        result = []

        for opcode, a0, a1, b0, b1 in matcher.get_opcodes():
            if opcode == 'equal':
                result.append(corrected_text[b0:b1])
            elif opcode in ('replace', 'insert'):
                result.append(f"*{corrected_text[b0:b1]}*")
                
            elif opcode == 'delete':
                continue

        return ''.join(result)