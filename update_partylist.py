import re

try:
    with open('data.js', 'r', encoding='utf-8') as f:
        data = f.read()

    # The string to replace inside partyListCsvData
    old_str = "10,กรุงเทพมหานคร,15,0,ประชาชน,16276"
    new_str = "10,กรุงเทพมหานคร,15,0,ประชาชน,40784"
    
    if old_str in data:
        data = data.replace(old_str, new_str)
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(data)
        print("Successfully updated partylist votes for ประชาชน in data.js")
    else:
        print("Error: Could not find the exactly matching old string in data.js")

except Exception as e:
    print(f"Error: {e}")
