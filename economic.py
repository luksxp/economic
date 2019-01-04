from data import data_cpi
from data import data_inf


def calculate_inflation(start_year, end_year, amount):
	"""
	Returns the amount (in czk) adjusted for inflation.
	The amount parameter is the amount (in czk) on the start_year
	The return value is the adjusted amount on the end_year  
	"""
	cpi_start_year = data_cpi[start_year]
	cpi_end_year = data_cpi[end_year]    

	cpi_difference = cpi_end_year - cpi_start_year

	inflation_rate = cpi_difference / cpi_start_year

	adjusted_amount = amount * (1 + inflation_rate)

	return round(adjusted_amount)   


def minus_percent(start_year, end_year):
    """
    Returns the percent of devaluation.
    """
    cpi_start_year = data_cpi[start_year]
    cpi_end_year = data_cpi[end_year]

    cpi_difference = cpi_end_year - cpi_start_year

    inflation_rate = 100 * (cpi_difference / cpi_start_year)
    
    return round(inflation_rate)   

    
def yearly_inflation(start_year, end_year):
    """
    Returns rate of inflation for each year
    """
    if start_year < end_year and start_year in data_inf.keys() and end_year in data_inf.keys():
        for i in range(start_year, end_year+1):
            print("in",i,"cz inflation was",data_inf[i],"%")   

  