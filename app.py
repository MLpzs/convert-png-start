from flask import Flask, render_template_string, request, send_file
from PIL import Image
import io

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head><title>Convert PNG Start ⭐</title></head>
<body>
<h2>Convert PNG Start ⭐ (.webp ➜ .png)</h2>
<form method="post" enctype="multipart/form-data">
    <input type="file" name="file" accept=".webp" required>
    <button type="submit">Converter</button>
</form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            imagem = Image.open(file.stream)
            buffer = io.BytesIO()
            imagem.save(buffer, format="PNG")
            buffer.seek(0)
            return send_file(buffer, as_attachment=True,
                             download_name="convertido.png",
                             mimetype='image/png')
    return render_template_string(HTML)
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

