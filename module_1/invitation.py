def print_sample_invite(mother, father, child, teacher, event):
    sample_text = f'''

Dear {mother} and {father},

{teacher} and I would like to see you both as well as {child} at our {event} tomorrow evening.
    
Kind regards,
R. Waterbridge
Headmaster
'''
    print(sample_text)

print_sample_invite(mother='Mrs. Smith', father='Mr. Smith', child='Conna', teacher='Ms Cole', event='End of Year Party')