Random Thoughts
#### Video Demo:  https://youtu.be/zJi9m_ysUbA
#### Description:
This is a simple website, made using flask for Back-end, sqlite3 for database and CSS & HTML for
Front-end.
So as you go to the website it says write your thoughts, and then you can write your thoughts,
once you write(or type) your thoughts and hit enter the thoughts will be shown in a table format, and then you can write another thought, each thought that is in the table can be removed using a remove button that is on top of every thought in the table.
Now for the techinical part we start with the index.html page that is asking you to write(or type)
your thoughts, its made using input type text, next the thoughts are stored in a database in a table called chats, next we display the thoughts using a for loop of jinja and the table tag of html, and there is a form in the for loop that is to remove the thought, it simply works by clicking on remove button, so as you click on the remove button it takes you to /remove route and the form also returns the chat(or thought) id so we can delete that specific thought form the database and redirect the user to the index page, so that's all, hope you liked the explanation.     