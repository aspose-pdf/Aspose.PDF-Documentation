---
title: Извлечение изображений из PDF (фасады)
type: docs
weight: 30
url: /java/extract-images/
description: Этот раздел объясняет, как извлекать изображения с помощью Aspose.PDF Facades, используя класс PdfExtractor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Класс [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) позволяет извлекать изображения из PDF файла.
 First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) class and bind input PDF file using bindPdf method. After that, call [extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of hasNextImage and getNextImage methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the getNextImage method which takes file path as argument. The following code snippet shows you how to extract images from the whole PDF to files.

Во-первых, вам нужно создать объект класса [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) и привязать входной PDF-файл, используя метод bindPdf. После этого вызовите метод [extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--), чтобы извлечь все изображения в память. После того как изображения извлечены, вы можете получить их с помощью методов hasNextImage и getNextImage. Вам нужно перебрать все извлеченные изображения, используя цикл while. Чтобы сохранить изображения на диск, вы можете вызвать перегрузку метода getNextImage, который принимает путь к файлу в качестве аргумента. Следующий фрагмент кода показывает, как извлечь изображения из всего PDF в файлы.

```java   
public static void ExtractImages()
 {
    //Create an extractor and bind it to the document
    Document document = new Document(_dataDir + "sample.pdf");
    PdfExtractor extractor = new PdfExtractor(document);
    extractor.setStartPage(1);
    extractor.setEndPage(3);            

    //Run the extractor
    extractor.extractImage();
    int imageNumber = 1;
    //Iterate througth extracted images collection
    while (extractor.hasNextImage())
    {
        //Retrieve image from collection and save it in a file 
        extractor.getNextImage(_dataDir + String.format("image%03d.png", imageNumber++),ImageType.getPng());
    }
}
```