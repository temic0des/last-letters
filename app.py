from last_letters import LastLetter

def main():
    years = list(range(1880, 2022))
    files = [{'year': year, 'file': f'yob{year}.txt'} for year in years]

    last_letter = LastLetter()
    
    df = last_letter.read_all_files(files=files, folder_name='data')
    print(df.head())

    new_df = last_letter.create_last_name_letter(df)
    print(new_df.head())

    last_letter.letter_count_chart(new_df)

    last_letter.timeline_last_letter(new_df, 'a')

    cng = last_letter.count_name_group(new_df)
    print(cng)

    crosstable_conv = last_letter.crosstable_convert_ng(cng)
    print(crosstable_conv)

    last_letter_cols = ['d', 'a', 'y']
    last_letter.plot_converted_crosstable(crosstable_conv, last_letter_cols)

    df = last_letter.create_first_name_letter(new_df)
    print(df)

    crosstable_lfng = last_letter.crosstable_convert_lfng(df)
    print(crosstable_lfng)

    last_letter.get_crosstable_heatmap(crosstable_lfng)


if __name__ == '__main__':
    main()