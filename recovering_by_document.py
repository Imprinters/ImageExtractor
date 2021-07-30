from lxml import etree as ET
import re
import requests
import click


@click.command("recup_img")
@click.argument("doc_orig", type=str)
def recup_img_doc(doc_orig):
    reponse = input("Où voulez-vous enregistrer vos images ? Entrez le chemin complet : ")
    file = ET.parse(doc_orig)
    root = file.getroot()
    facsimile = root[1]

    for surfaceGrp in facsimile:
        for surface in surfaceGrp:
            image_url = surface.get('facs')
            img_data = requests.get(image_url).content
            with open(reponse + re.sub('#', '', surface.get('corresp')) + ".jpg", 'wb') as handler:
                handler.write(img_data)


if __name__ == "__main__":
    recup_img_doc()
