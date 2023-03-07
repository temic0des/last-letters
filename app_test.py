from last_letters import LastLetter

years = list(range(1880, 2022))
files = [{'year': year, 'file': f'data/yob{year}.txt'} for year in years]

last_letter = LastLetter()

def test_load_file():
    df = last_letter.load_file('data/yob2002.txt')
    assert df.columns[0] == 'name'

def test_failed_load_file():
    df = last_letter.load_file('')
    assert df == None

def test_read_all_files():
    combined_df = last_letter.read_all_files(files=files)
    assert len(combined_df.columns) == 4
    assert combined_df.columns[-1] == 'year'
