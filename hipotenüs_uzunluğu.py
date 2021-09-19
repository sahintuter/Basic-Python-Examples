
print("Hipotenüs uzunluğunu bulalım")

a  =  int ( input ( "a dik kenarı :" )) z#kullanıcıdan 1. dik kenarı istiyoruz

b  =  int ( input ( "b dik kenarı :" )) #kullanıcıdan 2. dik kenarı istiyoruz

c  =   ( a  **  2  +  b  **  2 )  **  0.5 #parantez içindeki işlem önce yapılır sonra kök içine alınır

baskı = ( "Hipotenüs değeri :"  , c )

print(baskı)
