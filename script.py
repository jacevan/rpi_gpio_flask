from time import sleep
from gpiozero import LED, Button, PWMLED, RGBLED

# Temporary
from os import environ
environ["GPIOZERO_PIN_FACTORY"] = "mock"
# The below Environment Variable is needed to use PWM pins
# environ["GPIOZERO_MOCK_PIN_CLASS"] = "mockpwmpin"

l1 = LED(1)
l1.off()
b6 = Button(6)

b6.when_pressed = l1.on
b6.when_released = l1.off

# for i in range(5):
#   l1.on()
#   sleep(0.75)
#   l1.off()
#   sleep(0.75)

# l3 = LED(3)
# p7 = PWMLED(7)
# p7.value = 0.0



