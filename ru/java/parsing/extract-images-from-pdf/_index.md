---
title: Извлечение изображений из PDF с помощью Java
linktitle: Извлечь изображения из PDF
type: docs
weight: 20
url: /java/extract-images-from-the-pdf-file/
description: Узнайте, как извлекать встроенные изображения из файлов PDF с помощью Aspose.PDF для Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь изображения из PDF с помощью Java
Abstract: В этой статье объясняется, как извлечь встроенные изображения из PDF-документа с помощью Aspose.PDF для Java. Он показывает, как открыть исходный PDF-файл, получить доступ к изображению из коллекции ресурсов страницы и сохранить извлеченный XImage во внешний файл.
---
Извлекайте изображения из страниц PDF, когда вам нужно повторно использовать встроенную графику, проверять ресурсы документа или экспортировать изображения для последующей обработки.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и откройте выходной поток для извлеченного файла изображения.
1. Get the target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) from the document and access its `Resources.Images` collection.
1. Retrieve the required [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) object from that image collection by index.
1. Вызовите `image.save(outputImage)`, чтобы записать извлеченные байты изображения в целевой поток.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
