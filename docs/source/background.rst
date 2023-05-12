##########
Background
##########

********************
Why build a web app?
********************
The core problem that a web app solves is that allows the user to send and receive information quickly and easily.
This information - or data - could be about anything and can be conveniently processed in a multitude of ways depending on what you want to do.


On the smaller scale, you could have a simple web app (i.e. a basic website) that acts as a small personal space.
For example, you are a freelance photographer and want to showcase your work publicly for career opportunities.
You app would only consist of a few pages: say an about page, a gallery and a contact page.
Such an app would be relatively easy to put together; you could easily get by without using a database and would not need a login system.

On the other hand, a web app could entail much more complex calculations where users can submit data.
For example, you could build an app to 


The takeaway is that the complexity of the web app is on a spectrum and can be as simple or complex as you like.

Below are listed the advantages a web app has, which can make it more attractive than other typical solutions.


Performance
===========
One of the main advantages is that programming our web app means that operations in general run faster relative to "off-the-shelf" software.
Tailoring a web app to perform only the tasks we want ensures that we do not have the overhead of unused features.
Since the web app will run remotely, it is not consuming resources - i.e. memory or storage - on your local computer.
Moreover, the use of optimised packages - such as `pandas` for data manipulation in Python - are exponentially faster than something like Excel.

Scalability
===========
Not only can web apps can handle large number of requests, but if these requests grow, the web app can scale sustainably.
For example, if queries are written efficiently, the web app will be able to handle manipulation to the data as it increases in size over time.
Also, in terms of computing power, it is easy to scale the resources (e.g. memory, storage, CPU options) via your cloud manager.
So the web app starts getting more traffic, alter the options for your instance from your account with your cloud provider: such changes should take effect almost immediately.
This is in contrast to an Excel workbook, which will become exponentially slower to run as it grows.

Inexpensive
===========
Since the languages, dependencies and software to develop a web app are free, the overall cost is extremely low.
The main source of cost is running it in production - i.e. paying a company (e.g. AWS, Railway) to host it.
In contrast, a lot of software would cost relatively more money to

Dependencies
============
As a web app runs in its own environment, it means that users can interact with the app without having to install anything on their computer.
For example, if we build our app using Django and use a PostgreSQL database, the user does not need to install Python or any software on their machine: they simply use their web browser.
If we were developing a simple Python script instead and wanted to run it on multiple machines,
then each machine has to be configured beforehand with the correct dependencies to ensure the script runs properly.

Usability
=========
Crucially, using a web app provides a friendly user interface to interact with.
This feature allows users to quickly interact and perform their jobs faster.
With a good user interface, a web app allows it use to be expanded to individuals not well-versed in technical details.
If we were using a command-line tool, it can be uninviting to operate and dissuades users from using it, even if it runs perfectly fine.

Control
=======
Although it requires learning, building and maintaining a web app is empowering to the developer as they have almost complete control over it.
You the developer(s) can decide on what features to implement and when or how the app will look like.
Having this direct control means that you do not need to contend with a third-party to communicate and put in place your ideas.

Persistent
==========
Once deployed and working correctly, web apps will run continuously and be accessible via the browser 24/7.
This means that whatever tool it provides will always be present, rather than say a workbook or script
that needs to be manually started before it can be used. 

**********************
How does the web work?
**********************



****************************
How are web apps structured?
****************************

We can breakdown the web app into its main components.

The 3 basic components are:

* Database
* Backend
* Frontend

The database stores the web app's data as records where they can be created, read, updated and deleted.

The backend is responsible for facilitating modifications to the database and business logic.
Such tasks are performed on the server and therefore out-of-view of the user:
hence, the back end activities are commonly referred to as being "server-side".

The front end is what the end user (referred to usually as the client) sees
and interacts with through their web browser (e.g. using buttons, forms etc.). The front end activities are commonly referred to as being “client-side”.

Here is a simple overview of the web app's stack in development:

=========  =============  ===================
Component  Choice         Framework(s)
=========  =============  ===================
Frontend   HTML, CSS, JS  Bootstrap 5
Backend    Python         Django
Database   PostgreSQL     
=========  =============  ===================







For a complete description of the web stack, please view this section to see the preferred setup in production.


*************************************
What will I need to start developing?
*************************************

You will need to install certain languages / software onto your computer.
Here is the list of used by this guide:

* Text Editor (`Visual Studio Code`_)
* Backend Language (`Python`_)

The frontend languages (i.e. HTML/CSS/JS) do not need to be installed on your computer.

When it comes to deploying the app, we will end up using the `Railway`_ platform.
To do this task easily, we need to have an online account where we can "upload" our code to the cloud.
And to do that, we need version control software on our computer.

* Version Control Software (`GitHub Desktop`_)
* Cloud Version Control Account (`GitHub`_)


.. _Railway: https://railway.app/
.. _Visual Studio Code: https://code.visualstudio.com/
.. _Python: https://www.python.org/
.. _GitHub Desktop: https://desktop.github.com/
.. _GitHub: https://github.com/
