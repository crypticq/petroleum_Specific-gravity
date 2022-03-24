#!/usr/bin/env python3


        
def api_denisty(api):
        
    x = (141.5 / ( api + 131.5))
    API_gravity = ((141.5/x) - 131.5)
    if API_gravity >= 35:
        return "Specific gravity for  {} and it's Light crude Oil".format(api)
    if API_gravity >= 45:
        return "Specific gravity for {} and it's Extra light oil".format(api)
    if API_gravity <= 35:
        return "Specific gravity for {} and it's medium crude".format(api)
    if API_gravity <= 25:
        return "Specific gravity for {} and it's heavy crude".format(api)
    if API_gravity < 15:
        return "Specific gravity for {} and it's very heavy oil".format(api)


if __name__ == '__main__':
    print('This Script convert API for petroleum to Density .. ')
    print('Coded By Eng Yazeed')
    
    api = int(input(' Your API .. : '))
    density = api_denisty(api)
    print(density)
    
  
    
    
    
