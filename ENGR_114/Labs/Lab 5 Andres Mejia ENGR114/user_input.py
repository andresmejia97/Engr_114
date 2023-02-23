def user_input():
    w_type = input('Which weather type (temperature, humidity, rainfall, or pressure) ?')
    print('the users input is: ', w_type)
    
    n_data_pts = input('how many data points (maximum 8000) ?')
    print('the users input is: ', n_data_pts)
    return [w_type, n_data_pts]