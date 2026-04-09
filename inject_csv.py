import re

try:
    with open('data.js', 'r', encoding='utf-8') as f:
        data = f.read()

    election_str = "10,กรุงเทพมหานคร,15,วิทวัส ติชะวาณิชย์,ประชาชน,37321,88172,127758,92121\n"
    
    party_list_str = """10,กรุงเทพมหานคร,15,0,ประชาชน,16276
10,กรุงเทพมหานคร,15,0,เพื่อไทย,10972
10,กรุงเทพมหานคร,15,0,ภูมิใจไทย,16276
10,กรุงเทพมหานคร,15,0,ประชาธิปัตย์,8780
10,กรุงเทพมหานคร,15,0,รวมไทยสร้างชาติ,2554
"""

    constituency_str = """10,กรุงเทพมหานคร,15,0,วิทวัส ติชะวาณิชย์,ประชาชน,37321
10,กรุงเทพมหานคร,15,0,พลภูมิ วิภัติภูมิประเทศ,เพื่อไทย,21523
10,กรุงเทพมหานคร,15,0,ถนอม อ่อนเกตุพล,ภูมิใจไทย,12943
10,กรุงเทพมหานคร,15,0,ฐิตยากร พรโรจนากูร,ประชาธิปัตย์,7971
10,กรุงเทพมหานคร,15,0,ชัญญาพัชญ์ ธนโชติสวัสดิพร,รวมไทยสร้างชาติ,1688
10,กรุงเทพมหานคร,15,0,นรชัย ไชยสังข์,เศรษฐกิจ,1014
10,กรุงเทพมหานคร,15,0,ปวริศา คุณาวรนนท์,กล้าธรรม,664
10,กรุงเทพมหานคร,15,0,สุวัจชัย พิมพ์สุภาพร,ไทยสร้างไทย,635
10,กรุงเทพมหานคร,15,0,ณอร จิรกรภิรมย์,ไทยก้าวใหม่,501
10,กรุงเทพมหานคร,15,0,กิตติพงศ์ ท่าพิกุล,พลังประชารัฐ,459
10,กรุงเทพมหานคร,15,0,สัญชัย บัตรตรา,รักชาติ,297
10,กรุงเทพมหานคร,15,0,สงกรานต์ พงษ์พันนา,โอกาสใหม่,273
10,กรุงเทพมหานคร,15,0,กรกฤษณ์ วงศ์คุณหยก,ปวงชนไทย,259
10,กรุงเทพมหานคร,15,0,นันทวัชร์ กูลเกื้อศิประไพ,วิชชั่นใหม่,185
"""

    # In data.js, find the end of each template string
    # Replace the FIRST ` that comes AFTER "const electionCsvData ="
    
    # We will split the file based on the definitions
    parts = re.split(r'(const partyListCsvData = `.*?\n)(.*?)(`;)', data, flags=re.DOTALL)
    
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
        
    print("Successfully updated data.js")

except Exception as e:
    print(f"Error: {e}")
