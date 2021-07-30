from lxml import etree as ET
import re
import requests
import click


@click.command("recup_img")
@click.argument("path", type=str)
def recup_img_imp(path):
    reponse = input("Où voulez-vous enregistrer vos images ? Entrez le chemin complet : ")
    file = ET.parse(path)
    root = file.getroot()
    for balise in root:
        if balise.tag == "{http://www.tei-c.org/ns/1.0}TEI":
            for surfaceGrp in balise[1]:
                for surface in surfaceGrp:
                    image_url = surface.get('facs')
                    img_data = requests.get(image_url).content
                    with open(reponse + re.sub('#', '', surface.get('corresp')) + ".jpg", 'wb') as handler:
                        handler.write(img_data)


if __name__ == "__main__":
    recup_img_imp()
