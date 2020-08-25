from django.http import HttpResponse
import requests
from django.shortcuts import render

def index(request):
  html = ("""

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: "Lato", sans-serif;
}

.sidenav {
  height: 100%;
  width: 160px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #111;
  overflow-x: hidden;
  padding-top: 20px;
}

.sidenav a {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: block;
}

.sidenav a:hover {
  color: #f1f1f1;
}

.main {
  margin-left: 160px; /* Same as the width of the sidenav */
  font-size: 28px; /* Increased text to enable scrolling */
  padding: 0px 10px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<div class="sidenav">
  <a class="active" style="color:white" href="/">Home</a><a href="contact">Contact</a> 
  <a href="about">About</a>
  <a href="archive">Archive</a>
</div>
  
</div>

<div class="main">
  <h1 style="color:blue; font-size:42px ;font-family: helvetica;">Chimera Archival Society Hub</h1>
<hr />
<h2>Home</h2>
<p style="font-family:helvetica">Welcome to the Hub.</p><p> Here is where you will access our great collection. </p><p>Thank you for visiting and supporting us.</p>
  
   
</body>
</html> 
""")
  return HttpResponse(html)

def contact(request):
  contactpage = 'chimerahub/contact.html'
  return render(request, contactpage)

def about(request):
  aboutpage = 'chimerahub/about.html'
  return render(request, aboutpage)

def archive(request):
  archivepage = 'chimerahub/archive.html'
  return render(request, archivepage)

def twentychunka(request):
  twentychunk = 'chimerahub/20chunk-a.html'
  return render(request, twentychunk)

def zombocom(request):
  zombo = 'chimerahub/zombocom/index.html'
  return render(request, zombo)
