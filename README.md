<h1>Welcome to the Movie Project</h1>

<h2>What is this program?</h2>
<p>The movie application is a Flask application that displays information from a csv file with more than 3000 movie information entries.</p>

<h2>What you should know first</h2>
<ul>
<li>Please make sure that you have downloaded the whole project to your local directory.</li>
<li>Refer to the "requirements.txt" file for environemnt requirements to successfully run the program.</li>
<li>This program imported code from "movies_tools.py" and "moviews_clean.csv", which are also in the folder. Please ensure the files are kept in the same directory as they are.</li>
</ul>

<h2>How to start the program?</h2>
<ol>
<li>If you're using the virtual environment in the project, type "venv\Scripts\activate" in the directory to activate the virtual environment.
<li>You should see a new "(proejct2-env)" in front of your directory now.</li>
<li>Type "python SI507_project_2.py runserver" to start the program.</li>
<li>Once the server runs, open your browser and navigate to http://127.0.0.1:5000.</li>
<li>You're reaching the homepage of the application, which should show number of entries of the movie data.</li>
</ol>

<h2>How to navigate to different paths?</h2>
<p>Aside from the homepage, there's only one other path that you can navigate to:</p>
<ol>
<li>The http://127.0.0.1:5000/movies/ratings/ page, which returns the first 5 movie names and their MPAA ratings.</li>
</ol>

<h2>Database Diagram</h2>
<p>Aside from the Flask application, a database diagram is also included in the project folder, which shows the organization of a prospective movie database. The file name is 'diagram.png'.</p>
