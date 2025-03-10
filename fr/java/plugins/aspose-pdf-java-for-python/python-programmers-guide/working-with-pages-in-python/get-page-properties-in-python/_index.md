---
title: Obtenir les propriétés de la page en Python
type: docs
weight: 50
url: /fr/java/get-page-properties-in-python/
lastmod: "2021-06-05"
---

Pour obtenir les propriétés de la page du document Pdf en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **GetPageProperties**.

```Python
doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# obtenir la collection de pages
page_collection = pdf_document.getPages();

# obtenir une page particulière
pdf_page = page_collection.get_Item(1);

# obtenir les propriétés de la page
print "ArtBox : Hauteur = " + pdf_page.getArtBox().getHeight() + ", Largeur = " + pdf_page.getArtBox().getWidth() + ", LLX = " + pdf_page.getArtBox().getLLX() + ", LLY = " + pdf_page.getArtBox().getLLY() + ", URX = " + pdf_page.getArtBox().getURX() + ", URY = " + pdf_page.getArtBox().getURY()
print "BleedBox : Hauteur = " + pdf_page.getBleedBox().getHeight() + ", Largeur = " + pdf_page.getBleedBox().getWidth() + ", LLX = " + pdf_page.getBleedBox().getLLX() + ", LLY = " + pdf_page.getBleedBox().getLLY() + ", URX = " + pdf_page.getBleedBox().getURX() + ", URY = " + pdf_page.getBleedBox().getURY()
print "CropBox : Hauteur = " + pdf_page.getCropBox().getHeight() + ", Largeur = " + pdf_page.getCropBox().getWidth() + ", LLX = " + pdf_page.getCropBox().getLLX() + ", LLY = " + pdf_page.getCropBox().getLLY() + ", URX = " + pdf_page.getCropBox().getURX() + ", URY = " + pdf_page.getCropBox().getURY()
print "MediaBox : Hauteur = " + pdf_page.getMediaBox().getHeight() + ", Largeur = " + pdf_page.getMediaBox().getWidth() + ", LLX = " + pdf_page.getMediaBox().getLLX() + ", LLY = " + pdf_page.getMediaBox().getLLY() + ", URX = " + pdf_page.getMediaBox().getURX() + ", URY = " + pdf_page.getMediaBox().getURY()
print "TrimBox : Hauteur = " + pdf_page.getTrimBox().getHeight() + ", Largeur = " + pdf_page.getTrimBox().getWidth() + ", LLX = " + pdf_page.getTrimBox().getLLX() + ", LLY = " + pdf_page.getTrimBox().getLLY() + ", URX = " + pdf_page.getTrimBox().getURX() + ", URY = " + pdf_page.getTrimBox().getURY()
print "Rect : Hauteur = " + pdf_page.getRect().getHeight() + ", Largeur = " + pdf_page.getRect().getWidth() + ", LLX = " + pdf_page.getRect().getLLX() + ", LLY = " + pdf_page.getRect().getLLY() + ", URX = " + pdf_page.getRect().getURX() + ", URY = " + pdf_page.getRect().getURY()
print "Numéro de la page :- " + pdf_page.getNumber()
print "Rotation :-" + pdf_page.getRotate()

```


**Télécharger le code en cours d'exécution**

Téléchargez **Obtenir les propriétés de la page (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetPageProperties/GetPageProperties.py)