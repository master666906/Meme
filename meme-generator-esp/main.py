from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':

        selected_image = request.form.get('image-selector')

        # Asignación #2
        textTop = request.form.get('textTop')
        textBottom = request.form.get('textBottom')

        # Asignación #3
        selected_color = request.form.get('color-selector')

        # Posición del texto
        textTop_y = request.form.get('textTop_y')
        textBottom_y = request.form.get('textBottom_y')

        return render_template(
            'index.html',
            selected_image=selected_image,
            textTop=textTop,
            textBottom=textBottom,
            selected_color=selected_color,
            textTop_y=textTop_y,
            textBottom_y=textBottom_y
        )

    else:
        return render_template(
            'index.html',
            selected_image='logo.svg',
            textTop='',
            textBottom='',
            selected_color='white',
            textTop_y='50',
            textBottom_y='350'
        )


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
