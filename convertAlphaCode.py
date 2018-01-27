import pycountry


input_countries = ['Denmark', "United Kingdom", "China", "AU", "Ireland"]

def changeCountryCode(country):
    for code in input_countries:
        if len(code) > 2:
            CodeAlpha = pycountry.countries.get(name=code).alpha_2
            print(CodeAlpha)


changeCountryCode(input_countries)
