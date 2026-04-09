import re

try:
    with open('data.js', 'r', encoding='utf-8') as f:
        data = f.read()

    election_str = "41,อุดรธานี,6,อดิศักดิ์ แก้วมุงคุณทรัพย์,ภูมิใจไทย,36722,77405,126400,80892\n"
    
    party_list_str = """41,อุดรธานี,6,0,ภูมิใจไทย,14088
41,อุดรธานี,6,0,เพื่อไทย,21021
41,อุดรธานี,6,0,ประชาชน,17891
41,อุดรธานี,6,0,กล้าธรรม,3476
41,อุดรธานี,6,0,เศรษฐกิจ,3426
41,อุดรธานี,6,0,ประชาธิปัตย์,1504
41,อุดรธานี,6,0,รวมไทยสร้างชาติ,880
41,อุดรธานี,6,0,เพื่อบ้านเมือง,29
41,อุดรธานี,6,0,ประชากรไทย,201
"""

    constituency_str = """41,อุดรธานี,6,0,อดิศักดิ์ แก้วมุงคุณทรัพย์,ภูมิใจไทย,36722
41,อุดรธานี,6,0,ธนอนันต์ เมนะสวัสดิ์,กล้าธรรม,15176
41,อุดรธานี,6,0,ประชาชาติ แสนแก้ว,เพื่อไทย,12386
41,อุดรธานี,6,0,สรวิชญ์ นาแพงสอน,ประชาชน,10595
41,อุดรธานี,6,0,ประกาศิต ปัญญาใส,เศรษฐกิจ,1487
41,อุดรธานี,6,0,บรรพต จิกจักร์,รวมไทยสร้างชาติ,487
41,อุดรธานี,6,0,มลิวรรณ แก้วสุข,ประชาธิปัตย์,341
41,อุดรธานี,6,0,สุริวรรณ คล้ายเพชร,เพื่อบ้านเมือง,147
41,อุดรธานี,6,0,ธนพล คำศรี,ประชากรไทย,64
"""

    new_data = data
    
    # Process electionCsvData
    match = re.search(r'(const electionCsvData = `.*?)(`;)', new_data, flags=re.DOTALL)
    if match:
        new_data = new_data[:match.start(2)] + election_str + new_data[match.start(2):]

    # Process partyListCsvData
    match = re.search(r'(const partyListCsvData = `.*?)(`;)', new_data, flags=re.DOTALL)
    if match:
        new_data = new_data[:match.start(2)] + party_list_str + new_data[match.start(2):]

    # Process constituencyCsvData
    match = re.search(r'(const constituencyCsvData = `.*?)(`;?)(\s*)$', new_data, flags=re.DOTALL)
    if match:
        new_data = new_data[:match.start(2)] + constituency_str + new_data[match.start(2):]

    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(new_data)
        
    print("Successfully added Udon Thani District 6 to data.js")

except Exception as e:
    print(f"Error: {e}")
