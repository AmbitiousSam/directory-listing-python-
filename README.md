# directory-listing-using-python-scripting
# code explanation
This script takes the URL and Wordlist as input and rest everything is done by the script. In the above script the first class is the color variables that I have used to print a colorful output instead of the boring plain output.
The next part contains the full logic of how this script is getting the valid directories.
I have included the whole code in a try except block because if the user hits control c it will come out of the script.
I have imported the system modules for the system argument(input) and system exit. Next is the socket module which is used for connecting to the URL and A TSL/SSL wrapper for socket objects.
Next is the requests module is used to send HTTP requests and
  Request Object with all the response data (content, encoding, status, etc).
The HTTP request returns a
 After getting the URL and Wordlist from the input we check the URL using the socket
 objects.
 
AF.INET is used to check the IPv4 address and SOCK_STREAM is used get a TCP connection
 to the URL.
 Next we get the status if the URL checking whether it is dead or alive, if dead returns an
 error if alive then it prints done.
 After that the wordlist file that’s has been taken as input is opened and each line is split and
 then we get the total numbers of paths to be checked.
 After that we begin the scan to find the valid directories. And loop the output by calling the
 function.
 The function checkpath() takes the path as the argument and it tries to add it at the end of
 the URL
  Ex : www.example.com/path
  If there is some error after adding the path then it exit the script, if no error then the script
checks the response (here I have taken the condition that the response should not be equal
to 500). If the condition is matched then the output is printed (url/path/).
Below are the screen shots how the working tool :
 
![WhatsApp Image 2020-12-26 at 9 56 01 AM](https://user-images.githubusercontent.com/54389032/106547312-04036180-6533-11eb-9f5c-f32180f06d2a.jpeg)
