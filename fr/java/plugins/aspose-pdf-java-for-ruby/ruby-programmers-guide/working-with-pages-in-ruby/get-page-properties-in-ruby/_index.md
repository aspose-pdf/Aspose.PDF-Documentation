---
title: Obtenir les propriétés de la page dans Ruby
linktitle: Obtenir les propriétés de la page dans Ruby
type: docs
weight: 50
url: /java/get-page-properties-in-ruby/
description: Découvrez comment récupérer les propriétés d'une page dans un fichier PDF à l'aide de Ruby avec Aspose.PDF pour gérer et manipuler efficacement vos documents.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtenir les propriétés de la page



Pour obtenir les propriétés de la page d'un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **GetPageProperties**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf_document = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get page collection

page_collection = pdf_document.getPages()

# get particular page

pdf_page = page_collection.get_Item(1)

#get page properties

puts "ArtBox : Height = " + pdf_page.getArtBox().getHeight().to_s + ", Width = " + pdf_page.getArtBox().getWidth().to_s + ", LLX = " + pdf_page.getArtBox().getLLX().to_s + ", LLY = " + pdf_page.getArtBox().getLLY().to_s + ", URX = " + pdf_page.getArtBox().getURX().to_s + ", URY = " + pdf_page.getArtBox().getURY().to_s

puts "BleedBox : Height = " + pdf_page.getBleedBox().getHeight().to_s + ", Width = " + pdf_page.getBleedBox().getWidth().to_s + ", LLX = " + pdf_page.getBleedBox().getLLX().to_s + ", LLY = " + pdf_page.getBleedBox().getLLY().to_s + ", URX = " + pdf_page.getBleedBox().getURX().to_s + ", URY = " + pdf_page.getBleedBox().getURY().to_s

puts "CropBox : Height = " + pdf_page.getCropBox().getHeight().to_s + ", Width = " + pdf_page.getCropBox().getWidth().to_s + ", LLX = " + pdf_page.getCropBox().getLLX().to_s + ", LLY = " + pdf_page.getCropBox().getLLY().to_s + ", URX = " + pdf_page.getCropBox().getURX().to_s + ", URY = " + pdf_page.getCropBox().getURY().to_s

puts "MediaBox : Height = " + pdf_page.getMediaBox().getHeight().to_s + ", Width = " + pdf_page.getMediaBox().getWidth().to_s + ", LLX = " + pdf_page.getMediaBox().getLLX().to_s + ", LLY = " + pdf_page.getMediaBox().getLLY().to_s + ", URX = " + pdf_page.getMediaBox().getURX().to_s + ", URY = " + pdf_page.getMediaBox().getURY().to_s

puts "TrimBox : Height = " + pdf_page.getTrimBox().getHeight().to_s + ", Width = " + pdf_page.getTrimBox().getWidth().to_s + ", LLX = " + pdf_page.getTrimBox().getLLX().to_s + ", LLY = " + pdf_page.getTrimBox().getLLY().to_s + ", URX = " + pdf_page.getTrimBox().getURX().to_s + ", URY = " + pdf_page.getTrimBox().getURY().to_s

puts "Rect : Height = " + pdf_page.getRect().getHeight().to_s + ", Width = " + pdf_page.getRect().getWidth().to_s + ", LLX = " + pdf_page.getRect().getLLX().to_s + ", LLY = " + pdf_page.getRect().getLLY().to_s + ", URX = " + pdf_page.getRect().getURX().to_s + ", URY = " + pdf_page.getRect().getURY().to_s

puts "Page Number :- " + pdf_page.getNumber().to_s

puts "Rotate :-" + pdf_page.getRotate().to_s
```

## 
Télécharger le code d'exécution



Téléchargez** Obtenir les propriétés de la page (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpageproperties.rb)
