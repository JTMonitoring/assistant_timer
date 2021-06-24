# assistant_timer
Timer for virtual assistants that can accept english strings

time.txt is where the english command will be stored, the timer can accept two english strings:

examples
set a timer for 5 seconds
or
remind me to wash the dishes in 10 minutes

string one
set a timer for x y

x = any number

y = [seconds, minutes, hours]

string two

remind me to x in y z

x = reminder name, can be any amount of words.

y = any number

z = [seconds, minutes, hours]


installation:
```
git clone https://github.com/JTMonitoring/assistant_timer
pip3 install gtts
```
usage:
type your command in time.txt. Later you can apply this to pull the string from your assistant. Use one of the examples if you aren't sure
save the file.
```
python3 timer.py
```
