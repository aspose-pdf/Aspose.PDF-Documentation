---
title: Извлечение объектов диаграмм из PDF-документа (фасады)
type: docs
weight: 20
url: /java/extract-chart-objects/
description: В этом разделе объясняется, как извлекать объекты диаграмм из PDF с помощью Aspose.PDF Facades, используя класс PdfExtractor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлечение объектов диаграмм из PDF-документа (фасады)

PDF позволяет группировать содержимое страницы в элементы, называемые **Помеченное содержимое**. Adobe Acrobat показывает их как "контейнеры". Объекты диаграмм размещаются в таких объектах. Мы представили новый метод extractMarkedContentAsImages() в классе PdfExtractor для извлечения этих объектов. Этот метод рендерит каждое **Помеченное содержимое** в отдельное изображение. Пожалуйста, обратите внимание, что все диаграммы не полностью размещены в одном контейнере. Из-за этого некоторые диаграммы будут сохранены в виде отдельных изображений по частям.

Обратите внимание, что правильное группирование содержимого в контейнеры — это ответственность дизайнера PDF-документа.
 If you want to get charts with header or other objects you should either edit/create the PDF document where whole chart is placed in one container.

Если вы хотите получить диаграммы с заголовком или другими объектами, вам следует либо отредактировать/создать PDF-документ, где вся диаграмма размещена в одном контейнере.

```java

 //Open document
 //Открыть документ

Document document = new Document("sample.pdf");

//instantiate PdfExtractor
//Создать экземпляр PdfExtractor

PdfExtractor pdfExtractor = new PdfExtractor();

//Extract Chart objects as image in a folder
//Извлечь объекты диаграммы как изображения в папку

pdfExtractor.extractMarkedContentAsImages(document.getPages().get_Item(1), "C:/Temp/Charts_page_1");

document.close();
```