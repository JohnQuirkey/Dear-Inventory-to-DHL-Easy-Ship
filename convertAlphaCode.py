import pycountry

#Test file to convert full name countries to 2 alpha Code names e.g. IE
input_countries = ['Denmark', "United Kingdom", "China", "AU", "Ireland"]

def changeCountryCode(country):
    for code in input_countries:
        if len(code) > 2:
            CodeAlpha = pycountry.countries.get(name=code).alpha_2
            print(CodeAlpha)


changeCountryCode(input_countries)
