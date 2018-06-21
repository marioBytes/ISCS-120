'''
Mario Martinez
6/12/2018

'''

YEAR = 5  # the next five years of the college

semster = 8000  # the amount of tuition for each semseter for a full time student

for x in range(YEAR):
    # calculations for a 3 percent increase in tuition each year
    semster = (semster * 0.03) + semster
    print('Next years tuition estimation will be ${:.2f}'.format(semster))
