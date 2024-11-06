---
title: Извлечение изображений из PDF 
linktitle: Извлечение изображений
type: docs
weight: 20
url: ru/java/extract-images-from-the-pdf-file/
description: Как извлечь часть изображения из PDF с использованием Aspose.PDF для Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Каждая страница в PDF документе содержит ресурсы (изображения, формы и шрифты). Мы можем получить доступ к этим ресурсам, вызвав метод [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). Класс [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) содержит [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection), и мы можем получить список изображений, вызвав метод [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Таким образом, чтобы извлечь изображение со страницы, нам нужно получить ссылку на страницу, затем на ресурсы страницы и, наконец, на коллекцию изображений.
Конкретное изображение мы можем извлечь, например, по индексу.

Индекс изображения возвращает объект [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
Этот объект предоставляет метод [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-), который может быть использован для сохранения извлеченного изображения. Следующий фрагмент кода показывает, как извлечь изображения из PDF файла.

```java
public static void Extract_Images(){
       // Путь к каталогу с документами.
       String _dataDir = "/home/admin1/pdf-examples/Samples/";
       String filePath = _dataDir + "ExtractImages.pdf";

       // Загрузить PDF документ
       com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

       com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);
       com.aspose.pdf.XImageCollection xImageCollection = page.getResources().getImages();
       // Извлечь конкретное изображение
       com.aspose.pdf.XImage xImage = xImageCollection.get_Item(1);

       try {
           java.io.FileOutputStream outputImage = new java.io.FileOutputStream(_dataDir + "output.jpg");
           // Сохранить выходное изображение
           xImage.save(outputImage);
           outputImage.close();
       } catch (java.io.FileNotFoundException e) {
           // TODO: обработать исключение
           e.printStackTrace();
       } catch (java.io.IOException e) {
           // TODO: обработать исключение
           e.printStackTrace();
       }
   }
```