# Ex.04 Design a Website for Server Side Processing
## Date:24/05/2026

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
MATH.HTML:

<!DOCTYPE html>
<html>
<head>
    <title>GST Calculator</title>

    <style>

        body{
            background-color:#f2f2f2;
            font-family:Arial;
        }

        .box{
            width:400px;
            margin:auto;
            margin-top:100px;
            background:white;
            padding:30px;
            text-align:center;
            border-radius:10px;
            box-shadow:0px 0px 10px gray;
        }

        input[type=number]{
            width:90%;
            padding:10px;
        }

        input[type=submit]{
            background-color:blue;
            color:white;
            border:none;
            padding:10px 20px;
        }

    </style>

</head>

<body>

    <div class="box">

        <h2>GST Bill Calculator</h2>

        <form method="post">

            {% csrf_token %}

            <label>Enter Price :</label><br><br>

            <input type="number" name="price" step="0.01" required>

            <br><br>

            <label>Enter GST Percentage :</label><br><br>

            <input type="number" name="gst" step="0.01" required>

            <br><br>

            <input type="submit" value="Calculate">

        </form>

        {% if bill %}

            <h3>Entered Details</h3>

            <p>Price : {{ price }}</p>

            <p>GST Percentage : {{ gst_per }}%</p>

            <p>Total Bill Amount : {{ bill }}</p>

        {% endif %}

    </div>

</body>
</html>

VIEWS.PY:

from django.shortcuts import render

def gst(request):

    price = ""
    gst_per = ""
    bill = ""

    if request.method == "POST":

        price = request.POST['price']
        gst_per = request.POST['gst']

        total = float(price) + (float(price) * float(gst_per) / 100)

        bill = total

    return render(request, 'math.html', {
        'price': price,
        'gst_per': gst_per,
        'bill': bill
    })

URLS.PY:

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.gst),
]

```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2026-05-24 115825.png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2026-05-24 115253.png>)

## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
