from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    members = [
        {
            'name': 'Jesen Tanamas',
            'nim': '22.83.0920',
            'education': 'Amikom Yogyakarta',
            'about': 'Mahasiswa keturunan China dari Bangka',
            'image': 'profile2.jpg'
        }
    ]
    return render_template('index.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)
