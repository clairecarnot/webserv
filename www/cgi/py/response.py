import os
import urllib.parse

query = os.environ.get('QUERY_STRING', '')

params = urllib.parse.parse_qs(query)

color = params.get('color', [''])[0]
meal = params.get('meal', [''])[0]
season = params.get('season', [''])[0]

content = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="../../style.css" rel="stylesheet">
        <title>Form response (php)</title>
    </head>
    <body>
        <div class="title1">Response</div>
        <div class="response">
            <div class="tag">Your favorite color is <span class="value">{color}</span></div>
            <div class="tag">Your favorite meal is <span class="value">{meal}</span></div>
            <div class="tag">Your favorite season is <span class="value">{season}</span></div>
			<br><br>
			You have very good taste :-)
        </div>
		<div class="index">
            <a class="indexButton" href="/">go back to home page</a>
        </div>
    </body>
</html>"""

print(content)