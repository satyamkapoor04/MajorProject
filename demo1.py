#!/usr/bin/python3
#


import cgi
import cgitb
cgitb.enable()


print ("Content-type:text/html\r\n\r\n")

import sys
import majorproject as mp
import requests
import nltk
import os
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

result = []
resultLength = 0
stopwords = set()

print ("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="wordcloud2.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
    <title>Major Project</title>


    <script language="JavaScript">
        function myFunction1() {
              var e = document.getElementById("b11");
              if (e.style.display == 'block') {
                   e.style.display = 'none';
                   document.getElementById("b1").style.backgroundColor = "#0399f3"
              } else {
                   e.style.display = 'block';
                   document.getElementById("b1").style.backgroundColor = "green"
              }
        }
        function myFunction2() {
              var e = document.getElementById("b12");
              if (e.style.display == 'block') {
                   e.style.display = 'none';
                   document.getElementById("b2").style.backgroundColor = "#0399f3"
              } else {
                   e.style.display = 'block';
                   document.getElementById("b2").style.backgroundColor = "green"
              }
        }
        function myFunction3() {
              var e = document.getElementById("b13");
              if (e.style.display == 'block') {
                   e.style.display = 'none';
                   document.getElementById("b3").style.backgroundColor = "#0399f3"
              } else {
                   e.style.display = 'block';
                   document.getElementById("b3").style.backgroundColor = "green"
              }
        }
        function myFunction4() {
              var e = document.getElementById("b14");
              if (e.style.display == 'block') {
                   e.style.display = 'none';
                   document.getElementById("b4").style.backgroundColor = "#0399f3"
              } else {
                   e.style.display = 'block';
                   document.getElementById("b4").style.backgroundColor = "green"
              }
        }
        function myFunction5() {
              var e = document.getElementById("b15");
              if (e.style.display == 'block') {
                   e.style.display = 'none';
                   document.getElementById("b5").style.backgroundColor = "#0399f3"
              } else {
                   e.style.display = 'block';
                   document.getElementById("b5").style.backgroundColor = "green"
              }
        }
        function myFunction6() {
              var e = document.getElementById("b16");
              if (e.style.display == 'block') {
                   e.style.display = 'none';
                   document.getElementById("b6").style.backgroundColor = "#0399f3"
              } else {
                   e.style.display = 'block';
                   document.getElementById("b6").style.backgroundColor = "green"
              }
        }
        function myFunction7() {
              var e = document.getElementById("b17");
              if (e.style.display == 'block') {
                   e.style.display = 'none';
                   document.getElementById("b7").style.backgroundColor = "#0399f3"
              } else {
                   e.style.display = 'block';
                   document.getElementById("b7").style.backgroundColor = "green"
              }
        }
        function myFunction8() {
              var e = document.getElementById("b18");
              if (e.style.display == 'block') {
                   e.style.display = 'none';
                   document.getElementById("b8").style.backgroundColor = "#0399f3"
              } else {
                   e.style.display = 'block';
                   document.getElementById("b8").style.backgroundColor = "green"
              }
        }
        function myFunction9() {
              var e = document.getElementById("b19");
              if (e.style.display == 'block') {
                   e.style.display = 'none';
                   document.getElementById("b9").style.backgroundColor = "#0399f3"
              } else {
                   e.style.display = 'block';
                   document.getElementById("b9").style.backgroundColor = "green"
              }
        }
        function myFunction10() {
              var e = document.getElementById("b110");
              if (e.style.display == 'block') {
                   e.style.display = 'none';
                   document.getElementById("b10").style.backgroundColor = "#0399f3"
              } else {
                   e.style.display = 'block';
                   document.getElementById("b10").style.backgroundColor = "green"
              }
        }
        function doSomething() {

        }

        function setImage1() {
        	//document.getElementById("keywordImage").src="../images/image1.png";
        	document.getElementById("keywords").style.backgroundImage = "url('../images/image1.png')";
        	document.getElementById("keywords").style.backgroundRepeat = "no-repeat";
        	document.getElementById("keywords").style.backgroundSize = "100% 100%";
        	document.getElementById("keywords").style.border = "1px solid black";
        	document.getElementById("relatedDocuments").style.border = "1px solid black";
        	document.getElementById("relatedDocuments").style.display = "block";

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file0.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button1").innerHTML = json_string[0].substring(0,n) + "...";
        	document.getElementById ("b11").innerHTML = json_string[0];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file0.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button2").innerHTML = json_string[1].substring(0,n) + "...";
        	document.getElementById ("b12").innerHTML = json_string[1];
        	
        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file0.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button3").innerHTML = json_string[2].substring(0,n) + "...";
        	document.getElementById ("b13").innerHTML = json_string[2];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file0.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button4").innerHTML = json_string[3].substring(0,n) + "...";
        	document.getElementById ("b14").innerHTML = json_string[3];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file0.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button5").innerHTML = json_string[4].substring(0,n) + "...";
        	document.getElementById ("b15").innerHTML = json_string[4];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file0.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button6").innerHTML = json_string[5].substring(0,n) + "..."
        	document.getElementById ("b16").innerHTML = json_string[5];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file0.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button7").innerHTML = json_string[6].substring(0,n) + "...";
        	document.getElementById ("b17").innerHTML = json_string[6];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file0.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button8").innerHTML = json_string[7].substring(0,n) + "...";
        	document.getElementById ("b18").innerHTML = json_string[7];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file0.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button9").innerHTML = json_string[8].substring(0,n) + "...";
        	document.getElementById ("b19").innerHTML = json_string[8];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file0.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button10").innerHTML = json_string[9].substring(0,n) + "...";
        	document.getElementById ("b110").innerHTML = json_string[9];

        }

        function setImage2() {
        	document.getElementById("keywords").style.backgroundImage = "url('../images/image2.png')";
        	document.getElementById("keywords").style.backgroundRepeat = "no-repeat";
        	document.getElementById("keywords").style.backgroundSize = "100% 100%";
        	document.getElementById("keywords").style.border = "1px solid black";
        	document.getElementById("relatedDocuments").style.border = "1px solid black";

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file1.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button1").innerHTML = json_string[0].substring(0,n) + "...";
        	document.getElementById ("b11").innerHTML = json_string[0];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file1.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button2").innerHTML = json_string[1].substring(0,n) + "...";
        	document.getElementById ("b12").innerHTML = json_string[1];
        	
        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file1.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button3").innerHTML = json_string[2].substring(0,n) + "...";
        	document.getElementById ("b13").innerHTML = json_string[2];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file1.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button4").innerHTML = json_string[3].substring(0,n) + "...";
        	document.getElementById ("b14").innerHTML = json_string[3];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file1.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button5").innerHTML = json_string[4].substring(0,n) + "...";
        	document.getElementById ("b15").innerHTML = json_string[4];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file1.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button6").innerHTML = json_string[5].substring(0,n) + "...";
        	document.getElementById ("b16").innerHTML = json_string[5];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file1.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button7").innerHTML = json_string[6].substring(0,n) + "...";
        	document.getElementById ("b17").innerHTML = json_string[6];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file1.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button8").innerHTML = json_string[7].substring(0,n) + "...";
        	document.getElementById ("b18").innerHTML = json_string[7];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file1.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button9").innerHTML = json_string[8].substring(0,n) + "...";
        	document.getElementById ("b19").innerHTML = json_string[8];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file1.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button10").innerHTML = json_string[9].substring(0,n) + "...";
        	document.getElementById ("b110").innerHTML = json_string[9];


        }

        function setImage3() {
        	document.getElementById("keywords").style.backgroundImage = "url('../images/image3.png')";
        	document.getElementById("keywords").style.backgroundRepeat = "no-repeat";
        	document.getElementById("keywords").style.backgroundSize = "100% 100%";
        	document.getElementById("keywords").style.border = "1px solid black";
        	document.getElementById("relatedDocuments").style.border = "1px solid black";

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file2.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button1").innerHTML = json_string[0].substring(0,n) + "...";
        	document.getElementById ("b11").innerHTML = json_string[0];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file2.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button2").innerHTML = json_string[1].substring(0,n) + "...";
        	document.getElementById ("b12").innerHTML = json_string[1];
        	
        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file2.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button3").innerHTML = json_string[2].substring(0,n) + "...";
        	document.getElementById ("b13").innerHTML = json_string[2];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file2.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button4").innerHTML = json_string[3].substring(0,n) + "...";
        	document.getElementById ("b14").innerHTML = json_string[3];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file2.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button5").innerHTML = json_string[4].substring(0,n) + "...";
        	document.getElementById ("b15").innerHTML = json_string[4];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file2.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button6").innerHTML = json_string[5].substring(0,n) + "...";
        	document.getElementById ("b16").innerHTML = json_string[5];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file2.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button7").innerHTML = json_string[6].substring(0,n) + "...";
        	document.getElementById ("b17").innerHTML = json_string[6];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file2.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button8").innerHTML = json_string[7].substring(0,n) + "...";
        	document.getElementById ("b18").innerHTML = json_string[7];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file2.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button9").innerHTML = json_string[8].substring(0,n) + "...";
        	document.getElementById ("b19").innerHTML = json_string[8];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file2.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button10").innerHTML = json_string[9].substring(0,n) + "...";
        	document.getElementById ("b110").innerHTML = json_string[9];


        }

        function setImage4() {
        	document.getElementById("keywords").style.backgroundImage = "url('../images/image4.png')";
        	document.getElementById("keywords").style.backgroundRepeat = "no-repeat";
        	document.getElementById("keywords").style.backgroundSize = "100% 100%";
        	document.getElementById("keywords").style.border = "1px solid black";
        	document.getElementById("relatedDocuments").style.border = "1px solid black";

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file3.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button1").innerHTML = json_string[0].substring(0,n) + "...";
        	document.getElementById ("b11").innerHTML = json_string[0];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file3.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button2").innerHTML = json_string[1].substring(0,n) + "...";
        	document.getElementById ("b12").innerHTML = json_string[1];
        	
        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file3.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button3").innerHTML = json_string[2].substring(0,n) + "...";
        	document.getElementById ("b13").innerHTML = json_string[2];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file3.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button4").innerHTML = json_string[3].substring(0,n) + "...";
        	document.getElementById ("b14").innerHTML = json_string[3];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file3.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button5").innerHTML = json_string[4].substring(0,n) + "...";
        	document.getElementById ("b15").innerHTML = json_string[4];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file3.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button6").innerHTML = json_string[5].substring(0,n) + "...";
        	document.getElementById ("b16").innerHTML = json_string[5];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file3.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button7").innerHTML = json_string[6].substring(0,n) + "...";
        	document.getElementById ("b17").innerHTML = json_string[6];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file3.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button8").innerHTML = json_string[7].substring(0,n) + "...";
        	document.getElementById ("b18").innerHTML = json_string[7];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file3.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button9").innerHTML = json_string[8].substring(0,n) + "...";
        	document.getElementById ("b19").innerHTML = json_string[8];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file3.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button10").innerHTML = json_string[9].substring(0,n) + "...";
        	document.getElementById ("b110").innerHTML = json_string[9];


        }

        function setImage5() {
        	document.getElementById("keywords").style.backgroundImage = "url('../images/image5.png')";
        	document.getElementById("keywords").style.backgroundRepeat = "no-repeat";
        	document.getElementById("keywords").style.backgroundSize = "100% 100%";
        	document.getElementById("keywords").style.border = "1px solid black";
        	document.getElementById("relatedDocuments").style.border = "1px solid black";

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file4.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button1").innerHTML = json_string[0].substring(0,n) + "...";
        	document.getElementById ("b11").innerHTML = json_string[0];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file4.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button2").innerHTML = json_string[1].substring(0,n) + "...";
        	document.getElementById ("b12").innerHTML = json_string[1];
        	
        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file4.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button3").innerHTML = json_string[2].substring(0,n) + "...";
        	document.getElementById ("b13").innerHTML = json_string[3];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file4.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button4").innerHTML = json_string[3].substring(0,n) + "...";
        	document.getElementById ("b14").innerHTML = json_string[3];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file4.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button5").innerHTML = json_string[4].substring(0,n) + "...";
        	document.getElementById ("b15").innerHTML = json_string[4];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file4.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button6").innerHTML = json_string[5].substring(0,n) + "...";
        	document.getElementById ("b16").innerHTML = json_string[5];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file4.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button7").innerHTML = json_string[6].substring(0,n) + "...";
        	document.getElementById ("b17").innerHTML = json_string[6];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file4.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button8").innerHTML = json_string[7].substring(0,n) + "...";
        	document.getElementById ("b18").innerHTML = json_string[7];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file4.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button9").innerHTML = json_string[8].substring(0,n) + "...";
        	document.getElementById ("b19").innerHTML = json_string[8];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file4.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button10").innerHTML = json_string[9].substring(0,n) + "...";
        	document.getElementById ("b110").innerHTML = json_string[9];


        }

        function setImage6() {
        	document.getElementById("keywords").style.backgroundImage = "url('../images/image6.png')";
                document.getElementById("keywords").style.backgroundRepeat = "no-repeat";
        	document.getElementById("keywords").style.backgroundSize = "100% 100%";
        	document.getElementById("keywords").style.border = "1px solid black";
        	document.getElementById("relatedDocuments").style.border = "1px solid black";

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file5.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button1").innerHTML = json_string[0].substring(0,n) + "...";
        	document.getElementById ("b11").innerHTML = json_string[0];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file5.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button2").innerHTML = json_string[1].substring(0,n) + "...";
        	document.getElementById ("b12").innerHTML = json_string[1];
        	
        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file5.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button3").innerHTML = json_string[2].substring(0,n) + "...";
        	document.getElementById ("b13").innerHTML = json_string[2];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file5.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button4").innerHTML = json_string[3].substring(0,n) + "...";
        	document.getElementById ("b14").innerHTML = json_string[3];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file5.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button5").innerHTML = json_string[4].substring(0,n) + "...";
        	document.getElementById ("b15").innerHTML = json_string[4];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file5.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button6").innerHTML = json_string[5].substring(0,n) + "...";
        	document.getElementById ("b16").innerHTML = json_string[5];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file5.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button7").innerHTML = json_string[6].substring(0,n) + "...";
        	document.getElementById ("b17").innerHTML = json_string[6];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file5.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button8").innerHTML = json_string[7].substring(0,n) + "...";
        	document.getElementById ("b18").innerHTML = json_string[7];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file5.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button9").innerHTML = json_string[8].substring(0,n) + "...";
        	document.getElementById ("b19").innerHTML = json_string[8];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file5.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button10").innerHTML = json_string[9].substring(0,n) + "...";
        	document.getElementById ("b110").innerHTML = json_string[9];


        }

        function setImage7() {
        	document.getElementById("keywords").style.backgroundImage = "url('../images/image7.png')";
                document.getElementById("keywords").style.backgroundRepeat = "no-repeat";
        	document.getElementById("keywords").style.backgroundSize = "100% 100%";
        	document.getElementById("keywords").style.border = "1px solid black";
        	document.getElementById("relatedDocuments").style.border = "1px solid black";

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file6.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button1").innerHTML = json_string[0].substring(0,n) + "...";
        	document.getElementById ("b11").innerHTML = json_string[0];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file6.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button2").innerHTML = json_string[1].substring(0,n) + "...";
        	document.getElementById ("b12").innerHTML = json_string[1];
        	
        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file6.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button3").innerHTML = json_string[2].substring(0,n) + "...";
        	document.getElementById ("b13").innerHTML = json_string[2];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file6.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button4").innerHTML = json_string[3].substring(0,n) + "...";
        	document.getElementById ("b14").innerHTML = json_string[3];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file6.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button5").innerHTML = json_string[4].substring(0,n) + "...";
        	document.getElementById ("b15").innerHTML = json_string[4];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file6.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button6").innerHTML = json_string[5].substring(0,n) + "...";
        	document.getElementById ("b16").innerHTML = json_string[5];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file6.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button7").innerHTML = json_string[6].substring(0,n) + "...";
        	document.getElementById ("b17").innerHTML = json_string[6];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file6.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button8").innerHTML = json_string[7].substring(0,n) + "...";
        	document.getElementById ("b18").innerHTML = json_string[7];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file6.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button9").innerHTML = json_string[8].substring(0,n) + "...";
        	document.getElementById ("b19").innerHTML = json_string[8];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file6.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button10").innerHTML = json_string[9].substring(0,n) + "...";
        	document.getElementById ("b110").innerHTML = json_string[9];


        }

        function setImage8() {
        	document.getElementById("keywords").style.backgroundImage = "url('../images/image8.png')";
                document.getElementById("keywords").style.backgroundRepeat = "no-repeat";
        	document.getElementById("keywords").style.backgroundSize = "100% 100%";
        	document.getElementById("keywords").style.border = "1px solid black";
        	document.getElementById("relatedDocuments").style.border = "1px solid black";

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file7.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button1").innerHTML = json_string[0].substring(0,n) + "...";
        	document.getElementById ("b11").innerHTML = json_string[0];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file7.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button2").innerHTML = json_string[1].substring(0,n) + "...";
        	document.getElementById ("b12").innerHTML = json_string[1];
        	
        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file7.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button3").innerHTML = json_string[2].substring(0,n) + "...";
        	document.getElementById ("b13").innerHTML = json_string[2];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file7.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button4").innerHTML = json_string[3].substring(0,n) + "...";
        	document.getElementById ("b14").innerHTML = json_string[3];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file7.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button5").innerHTML = json_string[4].substring(0,n) + "...";
        	document.getElementById ("b15").innerHTML = json_string[4];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file7.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button6").innerHTML = json_string[5].substring(0,n) + "...";
        	document.getElementById ("b16").innerHTML = json_string[5];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file7.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button7").innerHTML = json_string[6].substring(0,n) + "...";
        	document.getElementById ("b17").innerHTML = json_string[6];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file7.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button8").innerHTML = json_string[7].substring(0,n) + "...";
        	document.getElementById ("b18").innerHTML = json_string[7];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file7.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button9").innerHTML = json_string[8].substring(0,n) + "...";
        	document.getElementById ("b19").innerHTML = json_string[8];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file7.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button10").innerHTML = json_string[9].substring(0,n) + "...";
        	document.getElementById ("b110").innerHTML = json_string[9];


        }

        function setImage9() {
        	document.getElementById("keywords").style.backgroundImage = "url('../images/image9.png')";
                document.getElementById("keywords").style.backgroundRepeat = "no-repeat";
        	document.getElementById("keywords").style.backgroundSize = "100% 100%";
        	document.getElementById("keywords").style.border = "1px solid black";
        	document.getElementById("relatedDocuments").style.border = "1px solid black";

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file8.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button1").innerHTML = json_string[0].substring(0,n) + "...";
        	document.getElementById ("b11").innerHTML = json_string[0];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file8.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button2").innerHTML = json_string[1].substring(0,n) + "...";
        	document.getElementById ("b12").innerHTML = json_string[1];
        	
        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file8.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button3").innerHTML = json_string[2].substring(0,n) + "...";
        	document.getElementById ("b13").innerHTML = json_string[2];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file8.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button4").innerHTML = json_string[3].substring(0,n) + "...";
        	document.getElementById ("b14").innerHTML = json_string[3];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file8.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button5").innerHTML = json_string[4].substring(0,n) + "...";
        	document.getElementById ("b15").innerHTML = json_string[4];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file8.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button6").innerHTML = json_string[5].substring(0,n) + "...";
        	document.getElementById ("b16").innerHTML = json_string[5];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file8.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button7").innerHTML = json_string[6].substring(0,n) + "...";
        	document.getElementById ("b17").innerHTML = json_string[6];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file8.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button8").innerHTML = json_string[7].substring(0,n) + "...";
        	document.getElementById ("b18").innerHTML = json_string[7];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file8.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button9").innerHTML = json_string[8].substring(0,n) + "...";
        	document.getElementById ("b19").innerHTML = json_string[8];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file8.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button10").innerHTML = json_string[9].substring(0,n) + "...";
        	document.getElementById ("b110").innerHTML = json_string[9];


        }

        function setImage10() {
        	document.getElementById("keywords").style.backgroundImage = "url('../images/image10.png')";
                document.getElementById("keywords").style.backgroundRepeat = "no-repeat";
        	document.getElementById("keywords").style.backgroundSize = "100% 100%";
        	document.getElementById("keywords").style.border = "1px solid black";
        	document.getElementById("relatedDocuments").style.border = "1px solid black";

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file9.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button1").innerHTML = json_string[0].substring(0,n) + "...";
        	document.getElementById ("b11").innerHTML = json_string[0];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file9.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button2").innerHTML = json_string[1].substring(0,n) + "...";
        	document.getElementById ("b12").innerHTML = json_string[1];
        	
        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file9.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button3").innerHTML = json_string[2].substring(0,n) + "...";
        	document.getElementById ("b13").innerHTML = json_string[2];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file9.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button4").innerHTML = json_string[3].substring(0,n) + "...";
        	document.getElementById ("b14").innerHTML = json_string[3];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file9.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button5").innerHTML = json_string[4].substring(0,n) + "...";
        	document.getElementById ("b15").innerHTML = json_string[4];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file9.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button6").innerHTML = json_string[5].substring(0,n) + "...";
        	document.getElementById ("b16").innerHTML = json_string[5];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file9.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button7").innerHTML = json_string[6].substring(0,n) + "...";
        	document.getElementById ("b17").innerHTML = json_string[6];


        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file9.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button8").innerHTML = json_string[7].substring(0,n) + "...";
        	document.getElementById ("b18").innerHTML = json_string[7];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file9.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button9").innerHTML = json_string[8].substring(0,n) + "...";
        	document.getElementById ("b19").innerHTML = json_string[8];

        	var result = null;
        	var xmlhttp = new XMLHttpRequest();
        	xmlhttp.open ("GET","../images/file9.txt",false);
        	xmlhttp.send();
        	if (xmlhttp.status == 200) {
        	     result = xmlhttp.responseText;
        	}
        	var json_string = JSON.parse (result);
        	var n = json_string.length;
        	if (n>40) {
        	     n = 40;
        	}
        	document.getElementById("button10").innerHTML = json_string[9].substring(0,n) + "...";
        	document.getElementById ("b110").innerHTML = json_string[9];


        }
        
    </script>
    <style>
        .container1 {
            display: flex;
            flex-direction: column;
        }

        .loader {
          border: 16px solid #f3f3f3;
          border-radius: 50%;
          border-top: 16px solid #3498db;
          height: 120px;
          width: 120px;
          -webkit-animation: spin 2s linear infinite; /* Safari */
          animation: spin 2s linear infinite;
          position: fixed;
          top: 50%;
          left: 50%;
          margin-top: -3em;
          margin-left: -9em;
        }

        @-webkit-keyframes spin {
          0% { -webkit-transform: rotate(0deg); }
          100% { -webkit-transform: rotate(360deg); }
        }

        @keyframes spin {
           0% { transform: rotate(0deg); }
           100% { transform: rotate(360deg); }
        }

        .header {
            color: #ffffff;
            position: fixed;
            top : 0;
            height : 80px;
            justify-content: center;
            align-items: center;
            width: 100vw;
            background-color: #0399f3;
        }

        .query {
            display: flex;
            width: 100vw;
            margin-top: 90px;
            flex-direction: row;
            flex-wrap : wrap;
            justify-content: center;
        }
        .container2 {
            display: flex;
            margin-top: 10px;
            flex-direction: row;
            justify-content: space-between;
        }
        .searchResult {
            display: flex;
            width: 60vw;

        }
        .container3 {
            margin-top: 30px;
            display: flex;
            flex-direction: column;
            width: 40vw;
            align-self: flex-start;
        }
        .keywords {
             display: flex;
             margin-top: 10px;
             width: 35vw;
             height: 33.5vh;
             align-self: flex-end;
        }
        .center {
           display: block;
           width: 100%;
         }
        .relatedDocuments {
             background-color: black;
             display: none;
             align-self: flex-end;
             width: 68.5vh;
             height: 30vh;
        }
        .t-table {
        margin-top: 30px;
        font-family: verdana;
        margin-left: 30px;
        color: #0399f3;
        }
        .t-table tr{
        border: 1px solid black;
        line-height: 20px;
        height: 35px;
        }
        .dropdown-content1 {
        display: none;
        position: absolute;
        max-width: 57.5%;
        background-color: #f1f1f1;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        .dropdown1:hover .dropdown-content1 {display: block;}
        .dropdown-content2 {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        max-width: 57.5%;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        .dropdown2:hover .dropdown-content2 {display: block;}
        .dropdown-content3 {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        max-width: 57.5%;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        .dropdown3:hover .dropdown-content3 {display: block;}
        .dropdown-content4 {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        max-width: 57.5%;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        .dropdown4:hover .dropdown-content4 {display: block;}
        .dropdown-content5 {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        max-width: 57.5%;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        .dropdown5:hover .dropdown-content5 {display: block;}
        .dropdown-content6 {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        max-width: 57.5%;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        .dropdown6:hover .dropdown-content6 {display: block;}
        .dropdown-content7 {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        max-width: 57.5%;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        .dropdown7:hover .dropdown-content7 {display: block;}
        .dropdown-content8 {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        max-width: 57.5%;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        .dropdown8:hover .dropdown-content8 {display: block;}
        .dropdown-content9 {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        max-width: 57.5%;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        .dropdown9:hover .dropdown-content9 {display: block;}
        .dropdown-content10 {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        max-width: 57.5%;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        .dropdown10:hover .dropdown-content10 {display: block;}
        
        #b1:active .b11 {display: block;}

        .goto {
            display: flex;
            justify-content: center;
            align-items: center;
         }

        .previous {
                text-decoration: none;
                display: inline-block;
                padding: 6px 10px;
                background-color: #f1f1f1;
                color: black;
        }
        .next {
                margin-left: 5px;
                text-decoration: none;
                display: inline-block;
                padding: 6px 10px;
                background-color: #0399f3;
                color: white;
        }

        .button {
             background-color: #0399f3;
             border: none;
             color: white;
             padding-top: 5px;
             text-align: center;
             text-decoration: none;
             display: inline-block;
             font-size: 16px;
             margin: 4px 2px;
             cursor: pointer;
             border-radius: 8px;
             width: 46%;
             height: 15%;
        }
        
        #b11 {
        display: none;
        position: absolute;
        background-color: #DCDCDC;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        
        #b12 {
        display: none;
        position: absolute;
        background-color: #DCDCDC;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        
        #b13 {
        display: none;
        position: absolute;
        background-color: #DCDCDC;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        
        #b14 {
        display: none;
        position: absolute;
        background-color: #DCDCDC;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        
        #b15 {
        display: none;
        position: absolute;
        background-color: #DCDCDC;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        
        #b16 {
        display: none;
        position: absolute;
        background-color: #DCDCDC;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        
        #b17 {
        display: none;
        position: absolute;
        background-color: #DCDCDC;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        
        #b18 {
        display: none;
        position: absolute;
        background-color: #DCDCDC;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        
        #b19 {
        display: none;
        position: absolute;
        background-color: #DCDCDC;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }
        
        #b110 {
        display: none;
        position: absolute;
        background-color: #DCDCDC;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }

    </style>
    <script>

        function getPreviousUrl() {
               var url = new URL(window.location.href);
               var position = url.searchParams.get("position");
               position = parseInt(position)-1;
               var query = url.searchParams.get("query");
               var source = 1;
               var newUrl = "demo1.py?query=" + query+"&position=" + position + "&source=" + source;
               var res = encodeURI(newUrl);
               window.location.href = res;
        }

        
    	function getNextUrl() {
    		var url = new URL(window.location.href);
    		var position = url.searchParams.get("position");
    		position = parseInt(position)+1;
    		var query = url.searchParams.get("query");
    		var source = 1;
    		var newUrl = "demo1.py?query=" + query+"&position=" + position + "&source=" + source;
    		var res = encodeURI(newUrl);
    		window.location.href = res;
    	}
    </script>
</head>

""")

print ('<body>')

print ("""
<div class="container1">
   <div class="header">
       <h1 style="text-align: center;"> Major Project </h1>
   </div>
  <div class="query">
    <form action="demo1.py" method="GET">
            <input name="query" type="text" id="query" placeholder="Type query here" style="width: 70vw;">
                    <input type="submit" value="Submit" onclick="doSomething()" style="margin-left: 5px">
                    <input type="hidden" value="0" name="position" id="position">
                    <input type="hidden" value="0" name="source" id="hidden">
     </form>

  </div>
""")

form = cgi.FieldStorage()

try:
    query = form["query"].value
    position = form["position"].value
    source = int(form["source"].value)
    position = int(position)
    query = str(query)
    word0 = ""
    word1 = ""
    word2 = ""
    word3 = ""
    word4 = ""
    word5 = ""
    word6 = ""
    word7 = ""
    word8 = ""
    word9 = ""
    
    if (len(query) != 0 and position == 0 and source == 0):
        print ("""
        <div class="loader" id="loader"></div>
        """)
        sys.stdout.flush()
        #print (query)
        result = mp.mainFunction(query)
        with open ("listfile.txt",'wb') as f:
            pickle.dump (result,f)
        resultLength = len(result)
        i = 0
        print ("""
        <script>
        document.getElementById('loader').style.display='none';
        </script>
        """)

        print ("""

  <div class="container2">
       <div class="searchResult">
    """)
        print ("""<table margin="20px" class="t-table">""")
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown1">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section1"><a href='javascript:setImage1();'>""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content1">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word0 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=500,height=480,margin=0,stopwords=stopwords,min_font_size=15).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image1.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown2">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section2"><a href="javascript:setImage2();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content2">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)

            words = result[i][5].split("; ")
            word1 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image2.png')
            
            print ("""</div></th></tr>""")
        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown3">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section3"><a href="javascript:setImage3();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content3">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word2 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image3.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown4">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section4"><a href="javascript:setImage4();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content4">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word3 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image4.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown5">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section5"><a href="javascript:setImage5();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content5">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word4 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image5.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown6">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section6"><a href="javascript:setImage6();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content6">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word5 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image6.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown7">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section7"><a href="javascript:setImage7();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content7">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word6 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image7.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown8">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section8"><a href="javascript:setImage8();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content8">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word7 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image8.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown9">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section9"><a href="javascript:setImage9();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content9">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word8 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image9.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown10">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section10"><a href="javascript:setImage10();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content10">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)

            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word9 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image10.png')

        print ("""</table>""")
        print ("""
       </div>


       <div class="container3">

              <div class="relatedDocuments" id="relatedDocuments">
                        <button class="button button1" id="b1" onclick="myFunction1()" style="margin-left: 5px;"><p id="button1"></p></button>
                        <p id="b11"></p>    
                        <button class="button button2" id="b2" onclick="myFunction2()" style="margin-left: 5px;"><p id="button2"></p></button>
                        <p id="b12"></p>
                        <button class="button button3" id="b3" onclick="myFunction3()" style="margin-left: 5px;"><p id="button3"></p></button>
                        <p id="b13"></p>
                        <button class="button button4" id="b4" onclick="myFunction4()" style="margin-left: 5px;"><p id="button4"></p></button>
                        <p id="b14"></p>
                        <button class="button button5" id="b5" onclick="myFunction5()" style="margin-left: 5px;"><p id="button5"></p></button>
                        <p id="b15"></p>
                        <button class="button button6" id="b6" onclick="myFunction6()" style="margin-left: 5px;"><p id="button6"></p></button>
                        <p id="b16"></p>
                        <button class="button button7" id="b7" onclick="myFunction7()" style="margin-left: 5px;"><p id="button7"></p></button>
                        <p id="b17"></p>
                        <button class="button button8" id="b8" onclick="myFunction8()" style="margin-left: 5px;"><p id="button8"></p></button>
                        <p id="b18"></p>
                        <button class="button button9" id="b9" onclick="myFunction9()" style="margin-left: 5px;"><p id="button9"></p></button>
                        <p id="b19"></p>
                        <button class="button button10" id="b10" onclick="myFunction10()" style="margin-left: 5px;"><p id="button10"></p></button>
                        <p id="b110"></p>
               </div>

               <div class="keywords" id="keywords">
                  <!--<img src="#" alt="" class="left" id="keywordImage" width="100%" height="100%"></img>-->
               </div>

       </div>
  </div>
</div>

<!--<div class="loader">
</div>
-->

""")

        if (position == 0):
            print ("""<br><div class="goto"><div class="previous" margin-left="100px">&laquo; Previous</div>""")
        else:
            print ("""<br><div class="goto"><a href="javascript:void(0);" onclick="getPreviousUrl();" class="previous" margin-left="100px">&laquo; Previous</a>""")

        if (resultLength <= 10*(position+1)):
            print ("""<div class="goto"><div class="next">Next &raquo;</div></div>""")
        else:
            print ("""<a href="javascript:void(0);" onclick="getNextUrl();" class="next">Next &raquo;</a></div>""")






    else:
        with open ("listfile.txt",'rb') as f:
            result = pickle.load (f)
        resultLength = len(result)
        i = 10*position
        print ("""

  <div class="container2">
       <div class="searchResult">
    """)
        print ("""<table margin:20px;" class="t-table">""")
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown1">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section1"><a href="javascript:setImage1();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content1">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")


            words = result[i][5].split("; ")
            word0 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image1.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown2">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section2"><a href="javascript:setImage2();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content2">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word1 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image2.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown3">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section3"><a href="javascript:setImage3();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content3">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word2 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image3.png')


        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown4">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section4"><a href="javascript:setImage4();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content4">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word3 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image4.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown5">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section5"><a href="javascript:setImage5();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content5">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word4 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image5.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown6">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section6"><a href="javascript:setImage6();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content6">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word5 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image6.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown7">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section7"><a href="javascript:setImage7();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content7">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word6 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image7.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown8">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section8"><a href="javascript:setImage8();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content8">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word7 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image8.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown9">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section9"><a href="javascript:setImage9();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content9">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)
            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word8 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image9.png')

        i = i+1
        if (i<resultLength):
            print ("""<tr>
        <th style="padding:2px" class="dropdown10">""")
            stringLen = len(result[i][6])
            print ("""
    <div class="dropdown-section10"><a href="javascript:setImage10();">""")
            print (result[i][6][0:170] + "...") if stringLen>170 else print (result[i][6] + "...")
            print ("""</a></div>
        <div class="dropdown-content10">
        """)
            print (result[i][6])
            print ("""
        </div>

        """)

            print ("""</div></th></tr>""")

            words = result[i][5].split("; ")
            word9 = words
            word_cloud_dict = Counter(words)
            wordcloud = WordCloud(width=480,height=480,margin=0,stopwords=stopwords,min_font_size=10).generate_from_frequencies(word_cloud_dict)
            wordcloud.to_file('../images/image10.png')

            
        print ("""</table>""")
        print ("""
       </div>

       <div class="container3">

              <div class="relatedDocuments" id="relatedDocuments">
                        <button class="button button1" id="b1" onclick="myFunction1()" style="margin-left: 5px;"><p id="button1"></p></button>
                        <p id="b11"></p>    
                        <button class="button button2" id="b2" onclick="myFunction2()" style="margin-left: 5px;"><p id="button2"></p></button>
                        <p id="b12"></p>
                        <button class="button button3" id="b3" onclick="myFunction3()" style="margin-left: 5px;"><p id="button3"></p></button>
                        <p id="b13"></p>
                        <button class="button button4" id="b4" onclick="myFunction4()" style="margin-left: 5px;"><p id="button4"></p></button>
                        <p id="b14"></p>
                        <button class="button button5" id="b5" onclick="myFunction5()" style="margin-left: 5px;"><p id="button5"></p></button>
                        <p id="b15"></p>
                        <button class="button button6" id="b6" onclick="myFunction6()" style="margin-left: 5px;"><p id="button6"></p></button>
                        <p id="b16"></p>
                        <button class="button button7" id="b7" onclick="myFunction7()" style="margin-left: 5px;"><p id="button7"></p></button>
                        <p id="b17"></p>
                        <button class="button button8" id="b8" onclick="myFunction8()" style="margin-left: 5px;"><p id="button8"></p></button>
                        <p id="b18"></p>
                        <button class="button button9" id="b9" onclick="myFunction9()" style="margin-left: 5px;"><p id="button9"></p></button>
                        <p id="b19"></p>
                        <button class="button button10" id="b10" onclick="myFunction10()" style="margin-left: 5px;"><p id="button10"></p></button>
                        <p id="b110"></p>
              </div>


               <div class="keywords" id="keywords">
                <!--<img src="#" id="keywordImage"></img>-->
               </div>

       </div>
  </div>
</div>

<!--<div class="loader">
</div>
-->

""")

        if (position == 0):
            print ("""<br><div class="goto"><div class="previous" margin-left="100px">&laquo; Previous</div>""")
        else:
            print ("""<br><div class="goto"><a href="javascript:void(0);" onclick="getPreviousUrl();" class="previous" margin-left="100px">&laquo; Previous</a>""")

        if (resultLength <= 10*(position+1)):
            print ("""<div class="goto"><div class="next">Next &raquo;</div></div>""")
        else:
            print ("""<a href="javascript:void(0);" onclick="getNextUrl();" class="next">Next &raquo;</a></div>""")

    print ('</body>')
    print ('</html>')

    sys.stdout.flush();
    mp.retrieveRelatedDocuments(word0,0)
    mp.retrieveRelatedDocuments(word1,1)
    mp.retrieveRelatedDocuments(word2,2)
    mp.retrieveRelatedDocuments(word3,3)
    mp.retrieveRelatedDocuments(word4,4)
    mp.retrieveRelatedDocuments(word5,5)
    mp.retrieveRelatedDocuments(word6,6)
    mp.retrieveRelatedDocuments(word7,7)
    mp.retrieveRelatedDocuments(word8,8)
    mp.retrieveRelatedDocuments(word9,9)


except:
    print ("""
    </body>
    </head>
    """)
