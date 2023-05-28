import spidev
from OrangePi_ws2812 import ws2812

spi = spidev.SpiDev()
spi.open(0,0)

#write 4 WS2812's, with the following colors: red, green, blue, yellow
ws2812.write2812(spi, [[0,0,0], [10,0,0], [0,20,0], [0,0,30], [40, 40, 0]])