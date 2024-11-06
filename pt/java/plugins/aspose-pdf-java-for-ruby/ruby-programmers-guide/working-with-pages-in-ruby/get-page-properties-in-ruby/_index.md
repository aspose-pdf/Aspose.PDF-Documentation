---
title: Obter Propriedades da Página em Ruby
type: docs
weight: 50
url: pt/java/get-page-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obter Propriedades da Página

Para obter propriedades da página de um documento Pdf usando **Aspose.PDF Java for Ruby**, simplesmente invoque o módulo **GetPageProperties**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Criar documento PDF

pdf_document = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# obter coleção de páginas

page_collection = pdf_document.getPages()

# obter página específica

pdf_page = page_collection.get_Item(1)

#obter propriedades da página

puts "ArtBox : Altura = " + pdf_page.getArtBox().getHeight().to_s + ", Largura = " + pdf_page.getArtBox().getWidth().to_s + ", LLX = " + pdf_page.getArtBox().getLLX().to_s + ", LLY = " + pdf_page.getArtBox().getLLY().to_s + ", URX = " + pdf_page.getArtBox().getURX().to_s + ", URY = " + pdf_page.getArtBox().getURY().to_s

puts "BleedBox : Altura = " + pdf_page.getBleedBox().getHeight().to_s + ", Largura = " + pdf_page.getBleedBox().getWidth().to_s + ", LLX = " + pdf_page.getBleedBox().getLLX().to_s + ", LLY = " + pdf_page.getBleedBox().getLLY().to_s + ", URX = " + pdf_page.getBleedBox().getURX().to_s + ", URY = " + pdf_page.getBleedBox().getURY().to_s

puts "CropBox : Altura = " + pdf_page.getCropBox().getHeight().to_s + ", Largura = " + pdf_page.getCropBox().getWidth().to_s + ", LLX = " + pdf_page.getCropBox().getLLX().to_s + ", LLY = " + pdf_page.getCropBox().getLLY().to_s + ", URX = " + pdf_page.getCropBox().getURX().to_s + ", URY = " + pdf_page.getCropBox().getURY().to_s

puts "MediaBox : Altura = " + pdf_page.getMediaBox().getHeight().to_s + ", Largura = " + pdf_page.getMediaBox().getWidth().to_s + ", LLX = " + pdf_page.getMediaBox().getLLX().to_s + ", LLY = " + pdf_page.getMediaBox().getLLY().to_s + ", URX = " + pdf_page.getMediaBox().getURX().to_s + ", URY = " + pdf_page.getMediaBox().getURY().to_s

puts "TrimBox : Altura = " + pdf_page.getTrimBox().getHeight().to_s + ", Largura = " + pdf_page.getTrimBox().getWidth().to_s + ", LLX = " + pdf_page.getTrimBox().getLLX().to_s + ", LLY = " + pdf_page.getTrimBox().getLLY().to_s + ", URX = " + pdf_page.getTrimBox().getURX().to_s + ", URY = " + pdf_page.getTrimBox().getURY().to_s

puts "Rect : Altura = " + pdf_page.getRect().getHeight().to_s + ", Largura = " + pdf_page.getRect().getWidth().to_s + ", LLX = " + pdf_page.getRect().getLLX().to_s + ", LLY = " + pdf_page.getRect().getLLY().to_s + ", URX = " + pdf_page.getRect().getURX().to_s + ", URY = " + pdf_page.getRect().getURY().to_s

puts "Número da Página :- " + pdf_page.getNumber().to_s

puts "Rotação :-" + pdf_page.getRotate().to_s
```


## Download Running Code

Baixar **Obter Propriedades da Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpageproperties.rb)