<!doctype html>
<html>
<head>
  <title>Madlibs</title>
</head>
<body>
  <h1>Madlibs</h1>
  <form action="/story">
    {% for prompt in prompts %}
      <p>{{ prompt }}:
        <input name="{{ prompt }}">
      </p>
    {% endfor %}
    <button>Submit</button>
  </form>
</body>
</html><!doctype html>
<html>
<head>
  <title>Madlibs</title>
</head>
<body>
  <h1>Madlibs</h1>
  <form action="/story">
    {% for prompt in prompts %}
      <p>{{ prompt }}:
        <input name="{{ prompt }}">
      </p>
    {% endfor %}
    <button>Submit</button>
  </form>
</body>
</html>