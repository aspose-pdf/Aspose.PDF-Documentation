---
title: Obtenir les Propriétés de la Page en Ruby
type: docs
weight: 50
url: fr/java/get-page-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtenir les Propriétés de la Page

Pour obtenir les propriétés de la page d'un document Pdf en utilisant **Aspose.PDF Java pour Ruby**, invoquez simplement le module **GetPageProperties**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Créer un document PDF

pdf_document = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# obtenir la collection de pages

page_collection = pdf_document.getPages()

# obtenir une page particulière

pdf_page = page_collection.get_Item(1)

#obtenir les propriétés de la page

puts "ArtBox : Hauteur = " + pdf_page.getArtBox().getHeight().to_s + ", Largeur = " + pdf_page.getArtBox().getWidth().to_s + ", LLX = " + pdf_page.getArtBox().getLLX().to_s + ", LLY = " + pdf_page.getArtBox().getLLY().to_s + ", URX = " + pdf_page.getArtBox().getURX().to_s + ", URY = " + pdf_page.getArtBox().getURY().to_s

puts "BleedBox : Hauteur = " + pdf_page.getBleedBox().getHeight().to_s + ", Largeur = " + pdf_page.getBleedBox().getWidth().to_s + ", LLX = " + pdf_page.getBleedBox().getLLX().to_s + ", LLY = " + pdf_page.getBleedBox().getLLY().to_s + ", URX = " + pdf_page.getBleedBox().getURX().to_s + ", URY = " + pdf_page.getBleedBox().getURY().to_s

puts "CropBox : Hauteur = " + pdf_page.getCropBox().getHeight().to_s + ", Largeur = " + pdf_page.getCropBox().getWidth().to_s + ", LLX = " + pdf_page.getCropBox().getLLX().to_s + ", LLY = " + pdf_page.getCropBox().getLLY().to_s + ", URX = " + pdf_page.getCropBox().getURX().to_s + ", URY = " + pdf_page.getCropBox().getURY().to_s

puts "MediaBox : Hauteur = " + pdf_page.getMediaBox().getHeight().to_s + ", Largeur = " + pdf_page.getMediaBox().getWidth().to_s + ", LLX = " + pdf_page.getMediaBox().getLLX().to_s + ", LLY = " + pdf_page.getMediaBox().getLLY().to_s + ", URX = " + pdf_page.getMediaBox().getURX().to_s + ", URY = " + pdf_page.getMediaBox().getURY().to_s

puts "TrimBox : Hauteur = " + pdf_page.getTrimBox().getHeight().to_s + ", Largeur = " + pdf_page.getTrimBox().getWidth().to_s + ", LLX = " + pdf_page.getTrimBox().getLLX().to_s + ", LLY = " + pdf_page.getTrimBox().getLLY().to_s + ", URX = " + pdf_page.getTrimBox().getURX().to_s + ", URY = " + pdf_page.getTrimBox().getURY().to_s

puts "Rect : Hauteur = " + pdf_page.getRect().getHeight().to_s + ", Largeur = " + pdf_page.getRect().getWidth().to_s + ", LLX = " + pdf_page.getRect().getLLX().to_s + ", LLY = " + pdf_page.getRect().getLLY().to_s + ", URX = " + pdf_page.getRect().getURX().to_s + ", URY = " + pdf_page.getRect().getURY().to_s

puts "Numéro de Page :- " + pdf_page.getNumber().to_s

puts "Rotation :-" + pdf_page.getRotate().to_s
```


## Télécharger le code en cours d'exécution

Téléchargez **Obtenir les propriétés de la page (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpageproperties.rb)