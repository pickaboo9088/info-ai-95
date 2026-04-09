import re

try:
    with open('data.js', 'r', encoding='utf-8') as f:
        data = f.read()

    election_str = "55,น่าน,1,เชาว์วิชญ์ อินน้อย,ประชาชน,34546,95619,139889,107125\n"
    
    party_list_str = """55,น่าน,1,0,ประชาชน,38359
55,น่าน,1,0,กล้าธรรม,5764
55,น่าน,1,0,ภูมิใจไทย,10406
55,น่าน,1,0,เพื่อไทย,18728
55,น่าน,1,0,ไทยก้าวใหม่,618
55,น่าน,1,0,พลังประชารัฐ,460
55,น่าน,1,0,ประชาธิปัตย์,4083
55,น่าน,1,0,ทางเลือกใหม่,530
55,น่าน,1,0,รวมไทยสร้างชาติ,1412
"""

    constituency_str = """55,น่าน,1,0,เชาว์วิชญ์ อินน้อย,ประชาชน,34546
55,น่าน,1,0,ณัฐ เธียรสูตร,กล้าธรรม,21279
55,น่าน,1,0,สักก์สีห์ พลสันติกุล,ภูมิใจไทย,15211
55,น่าน,1,0,ทรงยศ รามสูต,เพื่อไทย,13779
55,น่าน,1,0,เอกชัย อินทะนันท์,ไทยก้าวใหม่,2906
55,น่าน,1,0,สันติภาพ อินทรพัฒน์,พลังประชารัฐ,1999
55,น่าน,1,0,เสกสรรค์ คันทะมูล,ประชาธิปัตย์,1985
55,น่าน,1,0,ประยุทธ กุตตะนันท์,ทางเลือกใหม่,1570
55,น่าน,1,0,ปรีชาพล ยะราช,รวมไทยสร้างชาติ,1357
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
        
    print("Successfully added Nan District 1 to data.js")

except Exception as e:
    print(f"Error: {e}")
