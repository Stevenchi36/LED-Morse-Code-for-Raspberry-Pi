<h1 align="center">LED Morse Code for Raspberry Pi</h1>

<h2>About this project</h2>
This project turns text that you input into morse code by flashing an LED light. Below is a tutorial to show you how to set everything up! The morseCodeGen.py file is also commented pretty well, so it should be decently easy to understand for beginners!

<h2>Materials Needed</h2>
<ol>
  <li>Raspberry Pi - I am using a Pi 3 but any version will work</li>
  <li>Breadboard</li>
  <li>Jumper Wires</li>
  <li>LED Light</li>
  <li>Resistor - I am using a 220 Ω Resistor</li>
</ol>

<h2>Getting Set Up</h2>
<h3>Step 1: Clone the repository</h3>
Open your terminal on the Raspberry Pi or use SSH and navigate to the directory you want to program to be. Next, you will need to type: 
<pre><code>git clone https://github.com/Stevenchi36/LED-Morse-Code-for-Raspberry-Pi</code></pre>
<h3>Step 2: Setting up the breadboard</h3>
<img src="https://i.imgur.com/U0Lip4g.jpg?2" alt="">
<p>Refer to the image above for assistance with the next 3 steps.
I am using a cobbler for this project but you can connect the wires directly to the pins on the Pi. You can find the pin layout by searching for "Raspberry Pi GPIO layout"</p>
<ol>
  <li>Connect a jumper wire from pin 26 to the longer connection(anode) on the LED.(The blue wire in the picture above).</li>
  <li>Connect a wire from a ground pin to a different row on the breadboard.(The green wire in the picture above).</li>
  <li>Connect the resistor from the ground connection to the shorter end(cathode) of the LED</li>
  Now you should be all set up to run the program!
</ol>
<h3>Step 3: Run the program!</h3>
<ol>
  <li>In your terminal or SSH, navigate to the LED-Morse-Code-for-Raspberry-Pi directory that you cloned earlier. This folder contains the python program that you will be running.</li>
  <li>Input this code into the terminal:<pre><code>python morseCodeGen.py</code></pre> The program should now start and prompt you for input.</li>
  <li>Now enter anything you want. The program can handle letters in the English Alphabet, numbers, and a good amount of punctuation.</li>
  <li>To stop the program, just type "quit" or press CTRL+C.</li>
</ol>
<h3>You are now finished! Congrats!</h3>
 <h2>Simple Changes</h2>
 <h3>Here are a few simple changes you can easily make to the program:</h3>
 <ol>
  <li>Change the pin that is used for the output current. On line 7, you will see:
  <pre><code>led = LED(26)</code></pre>
  To change the pin you use, all you have to do is switch the number to whatever pin you would like to use.</li>
  <li>Change the speed of the morse code. On line 8, you will see the speed variable as a percent
  <pre><code>speedPercent = 100</code></pre>
  To change the speed, just lower the number. To get half speed, use 50. If you want quarter speed, use 25.</li>
  
