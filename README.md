# RUBY-Desktop-Assistant-GUI
A context-aware GUI desktop assistant named as "Ruby" using python and python-tkinter for UI listens to the commands only if the location is **Puducherry**, otherwise requests to go to Puducherry first.

# Prerequisites

You must have pyttsx3, numpy, opencv, pillow, pyowm(openWeatherMap API), speech-recognition and wikipedia installed.

Install requirements using : pip install -r requirements.txt

# Project Structure

First of all the project gets the location of the system using the IP address and checks whether the system is located in Puducherry or not. If Yes, it takes the voice command from the user and responds accordingly, and if not it tells the user where the system is currently and asks the user to go to Puducherry first.

The Commands to which Ruby responds are :

  1. Open Youtube
  2. Open Google
  3. Email to 'name'
  4. What's the weather?
  5. Who created you?
  6. Say hello.
  7. Play music/ Change music.
  8. What's the time?
  9. What's the date?
  10. What's your name?
  11. According to wikipedia ("any term", say Pondicherry University)
  12. Open Stackoverflow.
  13. Click Photo.
  14. Record Video.
  15. What can you do for me?
  16. How old are you?
  17. Open Media Player.
  18. Open Codeblocks.
  19. Open Anaconda.
  20. Thank You.
  
# Running the project

   1. Ensure that you are in the project home directory. Start the Desktop-Voice assistant by running below command -

          python ruby-main.py
          
      If everything goes well, you should be able to see the tkinter window as below.
      
      ![Untitled](https://user-images.githubusercontent.com/41967963/79081335-232dca00-7d3a-11ea-9416-8fda04f36a17.png)

      
      
