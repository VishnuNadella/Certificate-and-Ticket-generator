from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests

# add names {key value} names and emails
names = []

emails = [
    "theja2338@gmail.com",
    "Veggalamkranthi@gmail.com",
    "polishetti1031@gmail.com",
    "21951A0583@iare.ac.in",
    "Charanreddykunduru@gmail.com",
    "naredladeepakreddy@gmail.com",
    "pandirisaisrujan@gmail.com",
    "20951a6760@iare.ac.in",
    "roneymoon77@gmail.com",
    "ursgurucharan@gmail.com",
    "raghavareddy121212@gmail.com",
    "devarugved@gmail.com",
    "upagnareddy.duba@gmail.com",
    "vattikulasairam021@gmail.com",
    "bavandlasathwik@gmail.com",
    "sagunvarma25@gmail.com",
    "Kolukulapallipraveen412@gmail.com",
    "moulalidudekula181@gmail.com",
    "vamshiroyals146@gmail.com",
    "22951A6706@iare.ac.in",
    "20951a05e2@iare.ac.in",
    "21951a67b3@iare.ac.in",
    "mikkilishiva@gmail.com",
    "22951a1238@iare.ac.in",
    "tekumallaharshit@gmail.com",
    "kamtambharadwaj674@gmail.com",
    "neekunjchaturvedi3@gmail.com",
    "gopidisahithi@gmail.com",
    "maneesh.musunuru@gmail.com",
    "athreyakidambi2002@gmail.com",
    "SAICHARANCHOWHAN6666@GMAIL.COM",
    "gundavarapuharshithareddy@gmail.com",
    "mdasami.47@gmail.com",
    "2011cs020179@mallareddyuniversity.ac.in",
    "lahari2724@gmail.com",
    "20951A6214@iare.ac.in",
    "22951A0525@iare.ac.in",
    "sahithyadevineni02@gmail.com",
    "20951a6242@iare.ac.in",
    "gulgiaman568@gmail.com",
    "gandhamrishi21@gmail.com",
    "sravyareddie28@gmail.com",
    "2011cs020136@mallareddyuniversity.ac.in",
    "mankithareddy24@gmail.com",
    "a.rahulreddy2004@gmail.com",
    "ajjanpunitha@gmail.com",
    "yamjalamadhav@gmail.com",
    "surisettymanju31530@gmail.com",
    "pullurishreemayi@gmail.com",
    "ajayprince2003@gmail.com",
    "kashyapmitesh01@gmail.com",
    "21R21A0544@mlrinstitutions.ac.in",
    "mohdmubashir87@gmail.com",
    "gandhamrishi21@gmail.com",
    "22951A66A4@iare.ac.in",
    "ksvr0629@gmail.com",
    "anasjig4@gmail.com",
    "farhananwar784@gmail.com",
    "22951a05k7@iare.ac.in",
    "zeethisside@gmail.com",
    "rezwanali193@gmail.com",
    "potlapalliraviteja8@gmail.com",
    "junaidjaveedshaik@gmail.com",
    "Somanihemanthkumar30@gmail.com",
    "jalakamrohit@gmail.com",
    "2011cs020387@mallareddyuniversity.ac.in",
    "21951a3345@iare.ac.in",
    "21951a3304@iare.ac.in",
    "shivaganesh9108@gmail.com",
    "21951a6696@iare.ac.in",
    "vineethareddy185@gmail.com",
    "saichandunamani1234@gmail.com",
    "21951a66d1@iare.ac.in",
    "nikhithamalige@gmail.com",
    "21951A6633@iare.ac.in",
    "meghanamvss75@gmail.com",
    "pruthpirajus@gmail.com",
    "sv.nandee@gmail.com",
    "Anjusree1369@gmail.com",
    "kaavyannn@gmail.com",
    "shivani.annaldas@yahoo.com",
    "shreeyasolapuram@gmail.com",
    "Varunmaramreddy1@gmail.com",
    "sandeepsai575@gmail.com",
    "aparnapendyal@gmail.com",
    "21951A6603@iare.ac.in",
    "Asmitha262548@gmail.com",
    "upagnareddy.duba@gmail.com",
    "Theja2338@gmail.com",
    "bavandlasathwik@gmail.com",
    "vishwateja2684@gmail.com",
    "Sagunvarma25@gmail.com",
    "Pandirisaisrujan@gmail.com",
    "varshithamiriyala@gmail.com",
    "gopurishika1@gmail.com",
    "renu2002samuel@gmail.com",
    "20951a6621@iare.ac.in",
    "svnagaraju4457@gmail.com",
    "mahalaxmigajji@gmail.com",
    "manikaithi99@gmail.com",
    "aspmohan3@gmail.com",
    "20951A6622@iare.ac.in",
    "22951a6279@iare.ac.in",
    "sainikhilatham@gmail.com",
    "20951a6655@iare.ac.in",
    "satwikbharadwaj22@gmail.com",
    "21955a6604@iare.ac.in",
    "20951a04e9@iare.ac.in",
    "mdamaan023@gmail.com",
    "tejkonda@gmail.com",
    "Shivammbvk18@gmail.com",
    "20951a6751@iare.ac.in",
    "20951a6736@iare.ac.in",
    "20951a6723@iare.ac.in",
    "21951a66g7@iare.ac.in",
    "20951a2101@iare.ac.in",
    "20951A3346@iare.ac.in",
    "22951a66a4@iare.ac.in",
    "Chlrmanikanta@gmail.com",
    "charanyelimela@gmail.com",
    "22951a3354@iare.ac.in",
    "21951a1241@iare.ac.in",
    "21951A1241@iare.ac.in",
    "21951a1220@iare.ac.in",
    "dineshreddy70931@gmail.com",
    "22951a33a0@iare.ac.in",
    "22951A3380@iare.ac.in",
    "22951a3372@iare.ac.in",
    "22951a3365@iare.ac.in",
    "22951a3389@iare.ac.in",
    "22951a33c2@iare.ac.in",
    "22951A6644@iare.ac.in",
    "22951A66F6@iare.ac.in",
    "agrawalswapnil282005@gmail.com",
    "kiran.yuva4@gmail.com",
    "velmaruthwik@gmail.com",
    "22951A62A4@iare.ac.in",
    "21951a66j8@iare.ac.in",
    "20951a6249@iare.ac.in",
    "tejkonda@gmail.com",
    "vanugu47@gmail.com",
    "21951A67F2@iare.ac.in",
    "abhighna27kilaparthi@gmail.com",
    "Snehitha09.v@gmail.com",
    "shetiyamanasa@gmail.com",
    "21951A6687@iare.ac.in",
    "dsai9441695421@gmail.com",
    "lathamadhu499@gmail.com",
    "saisrujandasari@gmail.com",
    "22955a6709@iare.ac.in",
    "tafazularfa@gmail.com",
    "keerthisathvik20@gmail.com",
    "smerugu805@gmail.com",
    "rayinenirajkumar@gmail.com",
    "21951a1245@iare.ac.in",
    "yuvarajvasam03@gmail.com",
    "yuvarajvasam03@gmail.com",
    "21951a6796@iare.ac.in",
    "dattajaganpenumudi@gmail.com",
    "21951A6621@iare.ac.in",
    "srikanthkulkarni71@gmail.com",
    "ilapurampavan1729@gmail.com",
    "kjoga111@gmail.com",
    "barripatichandrika@gmail.com",
    "21951a6797@iare.ac.in",
    "22955a6707@iare.ac.in",
    "nikhil.singaraju5@gmail.com",
    "21951A3320@iare.ac.in",
    "devanshraj1734669@gmail.com",
    "dineshreddy1421@gmail.com",
    "dineshreddy70931@gmail.com",
    "22951a3301@iare.ac.in",
    "maneethgongalla@gmail.com",
    "dineshreddy1421@gmail.com",
    "22951A62B0@iare.ac.in",
    "21951a3353@iare.ac.in",
    "21951A0581@iare.ac.in",
    "21951a1220@iare.ac.in",
    "adithyareddy1242@gmail.com",
    "shivavinay1436@gmail.com",
    "brahmanandamreddy18@gmail.com",
    "srinuvarma0897@gmail.com",
    "Sannithrajmatta@gmail.com",
    "pavanchaitanya23@gmail.com",
    "evinay539@gmail.com",
    "ambatishivani24@gmail.com",
    "21951A05F1@iare.ac.in",
    "pranavreddykura@gmail.com",
    "raghavarapujethin@gmail.com",
    "21951a05g6@iare.ac.in",
    "Swathiboorla800@gmail.com",
    "ananyakanna358@gmail.com",
    "bavandlasathwik@gmail.com",
    "21951a05e1@iare.ac.in",
    "20951A0437@iare.ac.in",
    "21951a05n1@iare.ac.in",
    "21951a6610@iare.ac.in",
    "miss.priyagill@gmail.com",
    "vivek092004@gmail.com",
    "21951a1226@iare.ac.in",
    "kausthubsamavedam12@gmail.com",
    "Kanaparthinayan@gmail.com",
    "vishnunadella.7976@gmail.com",
]
emails = [email.lower() for email in emails]
app = Flask(__name__)


def generate(image_path, name, email, qr, font_size):
    print("\n\n\nParse QR Code:", qr, "\n\n\n")
    response = requests.get(qr)
    img = Image.open(BytesIO(response.content))

    im2 = Image.open(image_path)
    img = img.resize((213, 213))
    back_im = im2.copy()
    back_im.paste(img, (1111, 275))
    X, Y = (back_im.size)
    # Create a draw object
    draw = ImageDraw.Draw(back_im)
    draw1 = ImageDraw.Draw(back_im)
    # Define the font size and type
    font = ImageFont.truetype("TT Chocolates Regular.otf", font_size)

    draw.text((215, 312),
            name, fill = (25, 60, 102), font = font)

    draw1.text((564 ,312),
            email, fill = (25, 60, 102), font = font)

    image_io = BytesIO()
    back_im.save(image_io, format = "png", quality = 100)
    image_io.seek(0)

    return image_io

@app.route("/")
def home():
    return "Home"


@app.route("/get-ticket/")
def get_cert():
    qr = request.args.get("qr")
    print("\n\n\nQR Code:", qr, "\n\n\n")
    name = request.args.get("name").strip()
    email = request.args.get("email").strip()
    image_path = 'ticket.png'
    qr = qr.replace("---", "&")
    if qr != None and name != None and email != None and email.lower() in emails:
        return send_file(generate(image_path, name, email, qr, 30), mimetype='image/png')
    else:
        return "Invalid request"

if __name__ == '__main__':
    app.run(debug=True)
