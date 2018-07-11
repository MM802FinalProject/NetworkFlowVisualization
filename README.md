<snippet>
  <content>
  
# Final Project of MM802 
  Web APP to record and visualize network data flow.<br />
  Team members: Xuping Fang, Ke Gong.
 
## Installation
    TODO: Download the components and save to <Project_Root> and prepare required environments:

### virtualenv
    virtualenv creates a isolated Python environment, which can help avoid package issue.
  ```make
  # In command window
  $ sudo apt install virtualenv
  $ cd <Project_Root>
  # adapt the environment
  $ virtualenv venv
  $ source venv/bin/activate
  ```
    to leave the virtual environment:
  ```make
  $ deactivate
  ```
  
#### Packages need to be installed *WITHIN* virtualenv:
##### Django
    Django is an open source, high-level Python web framework.
  ```make
  $ pip install django
  ```

## Usage
  ```make
  #in venv
  $ cd <Project_Root>
  $ python manage.py runserver
  ```
  
    Keep the command running and open[this page](http://127.0.0.1:8000) in your browser.
    Hit "Starting Record" to start the network usage recording, in default, it will last 5 mins.
    Otherwise you can hit "Stop Recording" to interrupt the Recording.
    
    Then you can name the measurement and save the record.
    
    To view the result, hit "view saved result" to see our result page.
    
    The result page contains the max/min/average upload/download, total upload/download and runtime.
    
## Contributing

Implement the basic function of network flow recording web app with Django: Xuping Fang<br />
Refine the UI of the web app with CSS: Ke Gong<br />
Python script to record network usage: Ke Gong<br />
Generate dataset during live streaming: BOTH<br />
Write Project PPT: Ke Gong<br />
Anaylsis Dataset and reach conclusion: BOTH<br />
Write the description of presentation: Ke Gong<br />
Record Demo Video: Ke Gong<br />

</content>
  <tabTrigger></tabTrigger>
</snippet>
