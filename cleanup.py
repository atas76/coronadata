CURRENT_DATE = "210313"


def cleanup(fileidentifier):
    with open('worldometer_' + fileidentifier + 'raw.jl', 'r') as f:
        country_data = f.readlines()
        cleaned_data = country_data[8:229]

    f.close()

    with open('worldometer_' + fileidentifier + CURRENT_DATE + '.jl', 'w') as f:
        f.write("[\n")
        for country_record in cleaned_data[:-1]:
            f.write(country_record + ",")
        f.write(cleaned_data[-1])
        f.write("]")

    f.close()


cleanup('')
cleanup('tests_')

