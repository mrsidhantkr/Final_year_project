import I2C_LCD_driver

lcd = I2C_LCD_driver.lcd()

def display_message(message, duration=5):
    """Display a message on the LCD."""
    lcd.lcd_clear()
    lcd.lcd_display_string(message, 1)
    time.sleep(duration)
    lcd.lcd_clear()
