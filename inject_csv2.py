import re

try:
    with open('data.js', 'r', encoding='utf-8') as f:
        data = f.read()

    election_str = "25,ปราจีนบุรี,2,ชยุต ภุมมะกาญจนะ,ภูมิใจไทย,44037,100450,141803,108244\n"
    
    party_list_str = """25,ปราจีนบุรี,2,0,ภูมิใจไทย,21834
25,ปราจีนบุรี,2,0,ประชาชน,36603
25,ปราจีนบุรี,2,0,เพื่อไทย,13415
25,ปราจีนบุรี,2,0,ประชาธิปัตย์,4064
25,ปราจีนบุรี,2,0,ไทยภักดี,698
25,ปราจีนบุรี,2,0,เสรีรวมไทย,813
"""

    constituency_str = """25,ปราจีนบุรี,2,0,ชยุต ภุมมะกาญจนะ,ภูมิใจไทย,44037
25,ปราจีนบุรี,2,0,ศิริรัตน์ ศิริรักษ์,ประชาชน,33650
25,ปราจีนบุรี,2,0,สมเกียรติ คำดำ,เพื่อไทย,19484
25,ปราจีนบุรี,2,0,พรทิพย์พา ฤทธิ์ประเสริฐ,ประชาธิปัตย์,1441
25,ปราจีนบุรี,2,0,กันพิเชฐษ์ มลิเกตุ,ไทยภักดี,1102
25,ปราจีนบุรี,2,0,สุรศักดิ์ หร่ำเดช,เสรีรวมไทย,736
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
        
    print("Successfully added Prachinburi District 2 to data.js")

except Exception as e:
    print(f"Error: {e}")
