---
title: Получение Свойств Страницы в Ruby
type: docs
weight: 50
url: /java/get-page-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Получение Свойств Страницы

Чтобы получить свойства страницы PDF документа с использованием **Aspose.PDF Java для Ruby**, просто вызовите модуль **GetPageProperties**.

Код на Ruby

```java
# Путь к каталогу с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Создать PDF документ

pdf_document = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# получить коллекцию страниц

page_collection = pdf_document.getPages()

# получить конкретную страницу

pdf_page = page_collection.get_Item(1)

# получить свойства страницы

puts "ArtBox : Высота = " + pdf_page.getArtBox().getHeight().to_s + ", Ширина = " + pdf_page.getArtBox().getWidth().to_s + ", LLX = " + pdf_page.getArtBox().getLLX().to_s + ", LLY = " + pdf_page.getArtBox().getLLY().to_s + ", URX = " + pdf_page.getArtBox().getURX().to_s + ", URY = " + pdf_page.getArtBox().getURY().to_s

puts "BleedBox : Высота = " + pdf_page.getBleedBox().getHeight().to_s + ", Ширина = " + pdf_page.getBleedBox().getWidth().to_s + ", LLX = " + pdf_page.getBleedBox().getLLX().to_s + ", LLY = " + pdf_page.getBleedBox().getLLY().to_s + ", URX = " + pdf_page.getBleedBox().getURX().to_s + ", URY = " + pdf_page.getBleedBox().getURY().to_s

puts "CropBox : Высота = " + pdf_page.getCropBox().getHeight().to_s + ", Ширина = " + pdf_page.getCropBox().getWidth().to_s + ", LLX = " + pdf_page.getCropBox().getLLX().to_s + ", LLY = " + pdf_page.getCropBox().getLLY().to_s + ", URX = " + pdf_page.getCropBox().getURX().to_s + ", URY = " + pdf_page.getCropBox().getURY().to_s

puts "MediaBox : Высота = " + pdf_page.getMediaBox().getHeight().to_s + ", Ширина = " + pdf_page.getMediaBox().getWidth().to_s + ", LLX = " + pdf_page.getMediaBox().getLLX().to_s + ", LLY = " + pdf_page.getMediaBox().getLLY().to_s + ", URX = " + pdf_page.getMediaBox().getURX().to_s + ", URY = " + pdf_page.getMediaBox().getURY().to_s

puts "TrimBox : Высота = " + pdf_page.getTrimBox().getHeight().to_s + ", Ширина = " + pdf_page.getTrimBox().getWidth().to_s + ", LLX = " + pdf_page.getTrimBox().getLLX().to_s + ", LLY = " + pdf_page.getTrimBox().getLLY().to_s + ", URX = " + pdf_page.getTrimBox().getURX().to_s + ", URY = " + pdf_page.getTrimBox().getURY().to_s

puts "Rect : Высота = " + pdf_page.getRect().getHeight().to_s + ", Ширина = " + pdf_page.getRect().getWidth().to_s + ", LLX = " + pdf_page.getRect().getLLX().to_s + ", LLY = " + pdf_page.getRect().getLLY().to_s + ", URX = " + pdf_page.getRect().getURX().to_s + ", URY = " + pdf_page.getRect().getURY().to_s

puts "Номер Страницы :- " + pdf_page.getNumber().to_s

puts "Поворот :-" + pdf_page.getRotate().to_s
```


## Скачать Запущенный Код

Скачать **Получить свойства страницы (Aspose.PDF)** с любого из нижеупомянутых социальных сайтов для кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpageproperties.rb)