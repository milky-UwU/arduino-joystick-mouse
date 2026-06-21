import serial
import time
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

SERIAL_PORT = 'COM17' 
BAUD_RATE = 115200

CENTER_X = 512
CENTER_Y = 512
DEADZONE = 40         
SPEED_MODIFIER = 0.05 

button_was_pressed = False
click_count = 0
last_click_time = 0
CLICK_DELAY = 0.3 

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.01)
    
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            try:
                x_val, y_val, btn_val = map(int, line.split(','))
                
                dx = x_val - CENTER_X
                dy = y_val - CENTER_Y
                
                move_x = 0
                move_y = 0
                
                if abs(dx) > DEADZONE:
                    move_y = int(-dx * SPEED_MODIFIER)
                if abs(dy) > DEADZONE:
                    move_x = int(-dy * SPEED_MODIFIER) 
                    
                if move_x != 0 or move_y != 0:
                    pyautogui.moveRel(move_x, move_y)
                
                if btn_val == 0 and not button_was_pressed: 
                    button_was_pressed = True
                    current_time = time.time()
                    
                    if current_time - last_click_time < CLICK_DELAY:
                        click_count = 2
                    else:
                        click_count = 1
                        
                    last_click_time = current_time
                    
                elif btn_val == 1 and button_was_pressed: 
                    button_was_pressed = False
                    
            except ValueError:
                pass
        
        if click_count == 1 and (time.time() - last_click_time) > CLICK_DELAY:
            pyautogui.click(button='left')
            click_count = 0
        elif click_count == 2:
            pyautogui.click(button='right')
            click_count = 0
            
        time.sleep(0.005)

except KeyboardInterrupt:
    pass
except Exception as e:
    pass