from flask import Flask, flash, request, redirect, url_for, render_template, send_file, send_from_directory
import os
from werkzeug.utils import secure_filename
import cv2
from PIL import Image
import segno
import io
import qrcode

app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/upload/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/basic')
def basic():
    return render_template('basic.html')

@app.route('/basic', methods=['GET','POST'])
def basic_qr():
    name = request.form['url']
    link = request.form['url']
    if '//' in name and '.' in name:
        name = name.split('//')[1]
        name = name.split('.')[0]
    if len(name) > 6:
        filename = name[2:5]
    else:
        filename = name
    filename = f'{filename}.png'
    qrCode = segno.make(link, error='h')
    qrCode.save(f'static/created/{filename}')
    qr = Image.open(f'static/created/{filename}')
    qr = qr.resize((200,200))
    qr.save(f'static/created/{filename}')
    return render_template('basic.html', filename=filename)

@app.route('/basic/display/<filename>')
def display_image_basic(filename):
    path = 'static/created/' + filename
    img = Image.open(path)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')    
    file_object.seek(0)
    os.remove(path)
    return send_file(file_object, mimetype='image/PNG')

@app.route('/colour')
def colour():
    return render_template('colour.html')

@app.route('/colour', methods=['GET','POST'])
def colour_qr():
    name = request.form['url']
    link = request.form['url']
    dark = request.form['corner-color']
    data_dark = request.form['main-color']
    data_light = request.form['bg-color']
    if '//' in name and '.' in name:
        name = name.split('//')[1]
        name = name.split('.')[0]
    if len(name) > 6:
        filename = name[2:5]
    else:
        filename = name
    filename = f'{filename}.png'
    qrCode = segno.make(link, error='h')
    qrCode = qrCode.to_pil(scale=8, dark = dark, data_dark = data_dark, data_light = data_light)
    qrCode.save(f'static/created/{filename}')
    qr = Image.open(f'static/created/{filename}')
    qr = qr.resize((200,200))
    qr.save(f'static/created/{filename}')
    return render_template('colour.html', filename=filename)

@app.route('/colour/display/<filename>')
def display_image_colour(filename):
    path = 'static/created/' + filename
    img = Image.open(path)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')    
    file_object.seek(0)
    os.remove(path)
    return send_file(file_object, mimetype='image/PNG')

@app.route('/sm')
def sm():
    return render_template('social-media.html')

@app.route('/sm/facebook')
def facebook():
    return render_template('facebook.html')

@app.route('/sm/facebook', methods=['GET','POST'])
def facebook_qr():
    name = request.form['url']
    link = request.form['url']
    if '//' in name and '.' in name:
        name = name.split('//')[1]
        name = name.split('.')[0]
    if len(name) > 6:
        filename = name[2:5]
    else:
        filename = name
    filename = f'{filename}.png'
    logo = Image.open('./static/sample-images/fb-try.jpg')
    basewidth = 100
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    QRcode.add_data(link)
    QRcode.make()
    QRcolor = '#3b5998'
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    QRimg.save(f'./static/created/{filename}')
    qr = Image.open(f'static/created/{filename}')
    qr = qr.resize((200,200))
    qr.save(f'static/created/{filename}')
    return render_template('facebook.html', filename=filename)

@app.route('/sm/facebook/display/<filename>')
def display_image_fb(filename):
    path = 'static/created/' + filename
    img = Image.open(path)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')    
    file_object.seek(0)
    os.remove(path)
    return send_file(file_object, mimetype='image/PNG')

@app.route('/sm/telegram')
def telegram():
    return render_template('telegram.html')

@app.route('/sm/telegram', methods=['GET','POST'])
def telegram_qr():
    name = request.form['url']
    link = request.form['url']
    if '//' in name and '.' in name:
        name = name.split('//')[1]
        name = name.split('.')[0]
    if len(name) > 6:
        filename = name[2:5]
    else:
        filename = name
    filename = f'{filename}.png'
    logo = Image.open('./static/sample-images/te-try.jpg')
    basewidth = 100
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    QRcode.add_data(link)
    QRcode.make()
    QRcolor = '#00bfff'
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    QRimg.save(f'./static/created/{filename}')
    qr = Image.open(f'static/created/{filename}')
    qr = qr.resize((200,200))
    qr.save(f'static/created/{filename}')
    return render_template('telegram.html', filename=filename)

@app.route('/sm/telegram/display/<filename>')
def display_image_te(filename):
    path = 'static/created/' + filename
    img = Image.open(path)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')    
    file_object.seek(0)
    os.remove(path)
    return send_file(file_object, mimetype='image/PNG')

@app.route('/sm/youtube')
def youtube():
    return render_template('youtube.html')

@app.route('/sm/youtube', methods=['GET','POST'])
def youtube_qr():
    name = request.form['url']
    link = request.form['url']
    if '//' in name and '.' in name:
        name = name.split('//')[1]
        name = name.split('.')[0]
    if len(name) > 6:
        filename = name[2:5]
    else:
        filename = name
    filename = f'{filename}.png'
    logo = Image.open('./static/sample-images/yo-try.png')
    basewidth = 100
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    QRcode.add_data(link)
    QRcode.make()
    QRcolor = 'red'
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    QRimg.save(f'./static/created/{filename}')
    qr = Image.open(f'static/created/{filename}')
    qr = qr.resize((200,200))
    qr.save(f'static/created/{filename}')
    return render_template('youtube.html', filename=filename)

@app.route('/sm/youtube/display/<filename>')
def display_image_yt(filename):
    path = 'static/created/' + filename
    img = Image.open(path)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')    
    file_object.seek(0)
    os.remove(path)
    return send_file(file_object, mimetype='image/PNG')

@app.route('/sm/instagram')
def instagram():
    return render_template('instagram.html')

@app.route('/sm/instagram', methods=['GET','POST'])
def instagram_qr():
    name = request.form['url']
    link = request.form['url']
    if '//' in name and '.' in name:
        name = name.split('//')[1]
        name = name.split('.')[0]
    if len(name) > 6:
        filename = name[2:5]
    else:
        filename = name
    filename = f'{filename}.png'
    logo = Image.open('./static/sample-images/in-try.jpeg')
    basewidth = 100
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    QRcode.add_data(link)
    QRcode.make()
    QRcolor = '#c13584'
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    QRimg.save(f'./static/created/{filename}')
    qr = Image.open(f'static/created/{filename}')
    qr = qr.resize((200,200))
    qr.save(f'static/created/{filename}')
    return render_template('instagram.html', filename=filename)

@app.route('/sm/instagram/display/<filename>')
def display_image_in(filename):
    path = 'static/created/' + filename
    img = Image.open(path)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')    
    file_object.seek(0)
    os.remove(path)
    return send_file(file_object, mimetype='image/PNG')

@app.route('/sm/whatsapp')
def whatsapp():
    return render_template('whatsapp.html')

@app.route('/sm/whatsapp', methods=['GET','POST'])
def whatsapp_qr():
    name = request.form['url']
    link = request.form['url']
    if '//' in name and '.' in name:
        name = name.split('//')[1]
        name = name.split('.')[0]
    if len(name) > 6:
        filename = name[2:5]
    else:
        filename = name
    filename = f'{filename}.png'
    logo = Image.open('./static/sample-images/wh-try.png')
    basewidth = 100
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    QRcode.add_data(link)
    QRcode.make()
    QRcolor = '#25d366'
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    QRimg.save(f'./static/created/{filename}')
    qr = Image.open(f'static/created/{filename}')
    qr = qr.resize((200,200))
    qr.save(f'static/created/{filename}')
    return render_template('whatsapp.html', filename=filename)

@app.route('/sm/whatsapp/display/<filename>')
def display_image_wh(filename):
    path = 'static/created/' + filename
    img = Image.open(path)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')    
    file_object.seek(0)
    os.remove(path)
    return send_file(file_object, mimetype='image/PNG')


@app.route('/sm/twitter')
def twitter():
    return render_template('twitter.html')

@app.route('/sm/twitter', methods=['GET','POST'])
def twitter_qr():
    name = request.form['url']
    link = request.form['url']
    if '//' in name and '.' in name:
        name = name.split('//')[1]
        name = name.split('.')[0]
    if len(name) > 6:
        filename = name[2:5]
    else:
        filename = name
    filename = f'{filename}.png'
    logo = Image.open('./static/sample-images/tw-try.jpg')
    basewidth = 100
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    QRcode.add_data(link)
    QRcode.make()
    QRcolor = '#1da1f2'
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    QRimg.save(f'./static/created/{filename}')
    qr = Image.open(f'static/created/{filename}')
    qr = qr.resize((200,200))
    qr.save(f'static/created/{filename}')
    return render_template('twitter.html', filename=filename)

@app.route('/sm/twitter/display/<filename>')
def display_image_tw(filename):
    path = 'static/created/' + filename
    img = Image.open(path)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')    
    file_object.seek(0)
    os.remove(path)
    return send_file(file_object, mimetype='image/PNG')

@app.route('/sm/reddit')
def reddit():
    return render_template('reddit.html')

@app.route('/sm/reddit', methods=['GET','POST'])
def reddit_qr():
    name = request.form['url']
    link = request.form['url']
    if '//' in name and '.' in name:
        name = name.split('//')[1]
        name = name.split('.')[0]
    if len(name) > 6:
        filename = name[2:5]
    else:
        filename = name
    filename = f'{filename}.png'
    logo = Image.open('./static/sample-images/re-try.png')
    basewidth = 100
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    QRcode.add_data(link)
    QRcode.make()
    QRcolor = '#ff4500'
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    QRimg.save(f'./static/created/{filename}')
    qr = Image.open(f'static/created/{filename}')
    qr = qr.resize((200,200))
    qr.save(f'static/created/{filename}')
    return render_template('reddit.html', filename=filename)

@app.route('/sm/reddit/display/<filename>')
def display_image_rd(filename):
    path = 'static/created/' + filename
    img = Image.open(path)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')    
    file_object.seek(0)
    os.remove(path)
    return send_file(file_object, mimetype='image/PNG')

@app.route('/sm/github')
def github():
    return render_template('github.html')

@app.route('/sm/github', methods=['GET','POST'])
def github_qr():
    name = request.form['url']
    link = request.form['url']
    if '//' in name and '.' in name:
        name = name.split('//')[1]
        name = name.split('.')[0]
    if len(name) > 6:
        filename = name[2:5]
    else:
        filename = name
    filename = f'{filename}.png'
    logo = Image.open('./static/sample-images/gi-try.png')
    basewidth = 100
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    QRcode.add_data(link)
    QRcode.make()
    QRcolor = 'black'
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    QRimg.save(f'./static/created/{filename}')
    qr = Image.open(f'static/created/{filename}')
    qr = qr.resize((200,200))
    qr.save(f'static/created/{filename}')
    return render_template('github.html', filename=filename)

@app.route('/sm/github/display/<filename>')
def display_image_gi(filename):
    path = 'static/created/' + filename
    img = Image.open(path)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')    
    file_object.seek(0)
    os.remove(path)
    return send_file(file_object, mimetype='image/PNG')

@app.route('/sm/spotify')
def spotify():
    return render_template('spotify.html')

@app.route('/sm/spotify', methods=['GET','POST'])
def spotify_qr():
    name = request.form['url']
    link = request.form['url']
    if '//' in name and '.' in name:
        name = name.split('//')[1]
        name = name.split('.')[0]
    if len(name) > 6:
        filename = name[2:5]
    else:
        filename = name
    filename = f'{filename}.png'
    logo = Image.open('./static/sample-images/sp-try.png')
    basewidth = 100
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    QRcode.add_data(link)
    QRcode.make()
    QRcolor = '#1ed760'
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    QRimg.save(f'./static/created/{filename}')
    qr = Image.open(f'static/created/{filename}')
    qr = qr.resize((200,200))
    qr.save(f'static/created/{filename}')
    return render_template('spotify.html', filename=filename)

@app.route('/sm/spotify/display/<filename>')
def display_image_sp(filename):
    path = 'static/created/' + filename
    img = Image.open(path)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')    
    file_object.seek(0)
    os.remove(path)
    return send_file(file_object, mimetype='image/PNG')

@app.route('/image')
def image():
    return render_template('image.html')
 
@app.route('/image', methods=['POST'])
def upload_image():
    link = request.form["url"]
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        target = f'./static/created/{filename}'
        qrcode = segno.make(link, error='h')
        qrcode.to_artistic(background=os.path.join(app.config['UPLOAD_FOLDER'], filename), target=target, scale=8)
        qr = Image.open(f'static/created/{filename}')
        qr = qr.resize((200,200))
        qr.save(f'static/created/{filename}')
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('image.html', filename=filename)
        
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    path = './static/created/' + filename
    img = Image.open(path)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')    
    file_object.seek(0)
    os.remove(path)
    return send_file(file_object, mimetype='image/PNG')

if __name__ == "__main__":
    app.run()

@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])