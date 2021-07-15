# Privado_Hitesh

Please make sure of all the imports being installed on the system beforehand, imports.txt contains a list of all such imports required.

Execute the following command from the directory containing "manage.py" :  (Note: WINDOWS terminal command)
                                                                           python manage.py runserveraaaa
                                                                a          
Now that we have the localserver running, browsing to the homepage would load all the (3) templates into the database.
aa
We can now give in POST or GET requests by executing a curl command as:  (I just used "Postman" instead. Really handy)
                                                                         curl --location --request POST 'http://127.0.0.1:8000/te/customer/#customer_id_goes_here#/templates/'

"test.py" :
This file contains some unit test cases.
The project can be tested by executing:
                                        python manage.py test Privado_Hitesh

firstName first_name
