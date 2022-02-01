### Installation Instructions
- Clone repo: `git clone https://github.com/jacevan/rpi_gpio_flask`
- Change to working directory: `cd rpi_gpio_flask`
- Create a virtual environment: `python3 -m venv venv`
- Activate virtual environment: 
  - Mac/Linux: `source venv/bin/activate` 
  - Windows: `venv\Scripts\activate`
- Install requirements: `pip install -r requirements.txt`
- Copy hacked module to requirements: 
  - Mac/Linux: `cp mock.py venv/lib/python*/site-packages/gpiozero/pins/mock.py` 
  - Windows: `Copy-Item "mock.py" -Destination "venv/Lib/site-packages/gpiozero/pins/mock.py"`
- Set flask env variable: 
  - Mac/Linux: `export FLASK_APP=app` 
  - Windows: `set FLASK_APP=app`
- Run Flask: `flask run`
- Visit url in web browser: `127.0.0.1:5000` 
- In a separate terminal, same directory activate virtual environment and run: `python3 script.py`

### Notes
- `script.py` will run for 10 seconds. During this time the button will turn on the LED. 
- At anytime `l1.on()` or `l1.off()` will control the LED when `script.py` is run.
- Uncomment the `for` loop to make the LED blink.
