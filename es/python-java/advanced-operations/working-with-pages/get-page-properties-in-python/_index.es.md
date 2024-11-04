---
title: Obtener Propiedades de la Página en Python
type: docs
weight: 50
url: /python-java/get-page-properties-in-python/
---

Para obtener las propiedades de la página del documento Pdf usando **Aspose.PDF Java para Python**, simplemente invoque la clase **GetPageProperties**.

**Código Python**
```
doc = self.Document()
pdf_document = self.Document()
pdf_document = self.dataDir + 'input1.pdf'

# obtener colección de páginas
page_collection = pdf_document.getPages();

# obtener página particular
pdf_page = page_collection.get_Item(1);

# obtener propiedades de la página
print "ArtBox : Altura = " + pdf_page.getArtBox().getHeight() + ", Ancho = " + pdf_page.getArtBox().getWidth() + ", LLX = " + pdf_page.getArtBox().getLLX() + ", LLY = " + pdf_page.getArtBox().getLLY() + ", URX = " + pdf_page.getArtBox().getURX() + ", URY = " + pdf_page.getArtBox().getURY()
print "BleedBox : Altura = " + pdf_page.getBleedBox().getHeight() + ", Ancho = " + pdf_page.getBleedBox().getWidth() + ", LLX = " + pdf_page.getBleedBox().getLLX() + ", LLY = " + pdf_page.getBleedBox().getLLY() + ", URX = " + pdf_page.getBleedBox().getURX() + ", URY = " + pdf_page.getBleedBox().getURY()

 pdf_page.getBleedBox().getURY()
print "CropBox : Altura = " + pdf_page.getCropBox().getHeight() + ", Ancho = " + pdf_page.getCropBox().getWidth() + ", LLX = " + pdf_page.getCropBox().getLLX() + ", LLY = " + pdf_page.getCropBox().getLLY() + ", URX = " + pdf_page.getCropBox().getURX() + ", URY = " + pdf_page.getCropBox().getURY()
print "MediaBox : Altura = " + pdf_page.getMediaBox().getHeight() + ", Ancho = " + pdf_page.getMediaBox().getWidth() + ", LLX = " + pdf_page.getMediaBox().getLLX() + ", LLY = " + pdf_page.getMediaBox().getLLY() + ", URX = " + pdf_page.getMediaBox().getURX() + ", URY = " + pdf_page.getMediaBox().getURY()
print "TrimBox : Altura = " + pdf_page.getTrimBox().getHeight() + ", Ancho = " + pdf_page.getTrimBox().getWidth() + ", LLX = " + pdf_page.getTrimBox().getLLX() + ", LLY = " + pdf_page.getTrimBox().getLLY() + ", URX = " + pdf_page.getTrimBox().getURX() + ", URY = " + pdf_page.getTrimBox().getURY()

print "Rect : Altura = " + pdf_page.getRect().getHeight() + ", Ancho = " + pdf_page.getRect().getWidth() + ", LLX = " + pdf_page.getRect().getLLX() + ", LLY = " + pdf_page.getRect().getLLY() + ", URX = " + pdf_page.getRect().getURX() + ", URY = " + pdf_page.getRect().getURY()print "Número de página :- " + pdf_page.getNumber()
print "Rotar :-" + pdf_page.getRotate()
```

**Descargar Código en Ejecución**

Descargar **Obtener Propiedades de la Página (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetPageProperties/GetPageProperties.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/GetPageProperties/GetPageProperties.py)