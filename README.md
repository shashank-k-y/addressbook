# addressbook

Address book helps to:
----------------------------
1. add address of the location to addressbook.
2. view all the locations that you have added.
3. get specific location address.
4. delete the existing location address.
5. update the location address.
6. find the available location addresses from the book within the given distance :)


Installation:
-------------

**step1:**

create directory ```mkdir <directory-name>```

**step2: (optional)**


  **create virtual environment:**
  
  for mac ```pip3 install virtualenv```
  
  for linux and windows ```pip install virtualenv```
  
  refer link https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/
  
  
  create virtual environment
  
  ```virtualenv <virtualenv-name>```
  
  activate virtual environment
  
  ```source <virtualenv-name>/bin/activate```

**step3:**
  
  clone the repo using command ```https://github.com/shashank-k-y/addressbook.git```

**step4:**
  Install dependencies:
  
  in terminal:
  
  ```cd addressbook```
  
  ```pip install -r requirements.txt``` for mac use ```pip3 install -r requirements.txt```
  
**step5:**
  
  Run Local server:
  
  using command ```uvicorn address_book.main:app --reload```
  
  server starts like below ->
  
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [45935] using statreload
INFO:     Started server process [45937]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
^CINFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [45937]
INFO:     Stopping reloader process [45935]
```
**step6:**
  
  open http://127.0.0.1:8000/docs in browser it will display something like ->
  <img width="1436" alt="Screenshot 2022-05-14 at 12 43 59 AM" src="https://user-images.githubusercontent.com/74789167/168374492-07329c64-464e-4b8f-ac43-1db1e503bed0.png">
  
  
  addressbook is now ready to use :) cheers!!
  
  
