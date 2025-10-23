<h1>To run the this test.</h1>
<ul>
  <li>Download the repository.</li>
  <li>Extract it.</li>
  <li>Add the project to your IDE (I recommend PyCharm).</li>
  <li>Install Pytest using the command in your IDE's terminal: pip install pytest</li>
  <li>Install Selenium: pip install selenium</li>
  <li>While in the project directory, enter the command: python -m pytest -s -v</li>
</ul>

<h2>This test automates the order placement process:</h2>
<ul>
  <li>It navigates to the website.</li>
  <li>Selects the required product.</li>
  <li>Parses the product price and compares it with the amount in the cart.</li>
  <li>Proceeds to the checkout page.</li>
  <li>Fills in the necessary details.</li>
  <li>Completes the order.</li>
</ul>
