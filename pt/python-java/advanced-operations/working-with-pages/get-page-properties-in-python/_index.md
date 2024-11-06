---
title: Obter Propriedades da Página em Python
type: docs
weight: 50
url: pt/python-java/get-page-properties-in-python/
---

Para obter as propriedades da página de um documento PDF usando **Aspose.PDF Java para Python**, basta invocar a classe **GetPageProperties**.

**Código Python**
```
doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# obter coleção de páginas
page_collection = pdf_document.getPages();

# obter página específica
pdf_page = page_collection.get_Item(1);

# obter propriedades da página
print "ArtBox : Altura = " + pdf_page.getArtBox().getHeight() + ", Largura = " + pdf_page.getArtBox().getWidth() + ", LLX = " + pdf_page.getArtBox().getLLX() + ", LLY = " + pdf_page.getArtBox().getLLY() + ", URX = " + pdf_page.getArtBox().getURX() + ", URY = " + pdf_page.getArtBox().getURY()
print "BleedBox : Altura = " + pdf_page.getBleedBox().getHeight() + ", Largura = " + pdf_page.getBleedBox().getWidth() + ", LLX = " + pdf_page.getBleedBox().getLLX() + ", LLY = " + pdf_page.getBleedBox().getLLY() + ", URX = " + pdf_page.getBleedBox().getURX() + ", URY = " .
 pdf_page.getBleedBox().getURY()
print "CropBox : Altura = " + pdf_page.getCropBox().getHeight() + ", Largura = " + pdf_page.getCropBox().getWidth() + ", LLX = " + pdf_page.getCropBox().getLLX() + ", LLY = " + pdf_page.getCropBox().getLLY() + ", URX = " + pdf_page.getCropBox().getURX() + ", URY = " + pdf_page.getCropBox().getURY()
print "MediaBox : Altura = " + pdf_page.getMediaBox().getHeight() + ", Largura = " + pdf_page.getMediaBox().getWidth() + ", LLX = " + pdf_page.getMediaBox().getLLX() + ", LLY = " + pdf_page.getMediaBox().getLLY() + ", URX = " + pdf_page.getMediaBox().getURX() + ", URY = " + pdf_page.getMediaBox().getURY()
print "TrimBox : Altura = " + pdf_page.getTrimBox().getHeight() + ", Largura = " + pdf_page.getTrimBox().getWidth() + ", LLX = " + pdf_page.getTrimBox().getLLX() + ", LLY = " + pdf_page.getTrimBox().getLLY() + ", URX = " + pdf_page.getTrimBox().getURX() + ", URY = " + pdf_page.getTrimBox().getURY()

print "Rect : Altura = " + pdf_page.getRect().getHeight() + ", Largura = " + pdf_page.getRect().getWidth() + ", LLX = " + pdf_page.getRect().getLLX() + ", LLY = " + pdf_page.getRect().getLLY() + ", URX = " + pdf_page.getRect().getURX() + ", URY = " + pdf_page.getRect().getURY() print "Número da Página :- " + pdf_page.getNumber()
print "Rotacionar :-" + pdf_page.getRotate()

```

**Baixar Código em Execução**

Baixar **Obter Propriedades da Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetPageProperties/GetPageProperties.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/GetPageProperties/GetPageProperties.py)