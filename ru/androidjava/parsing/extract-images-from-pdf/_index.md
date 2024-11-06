---
title: Извлечение изображений из PDF
linktitle: Извлечение изображений
type: docs
weight: 20
url: ru/androidjava/extract-images-from-the-pdf-file/
description: Как извлечь часть изображения из PDF с использованием Aspose.PDF для Android через Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Каждая страница в PDF документе содержит ресурсы (изображения, формы и шрифты). Мы можем получить доступ к этим ресурсам, вызвав метод [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). Класс [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) содержит [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection), и мы можем получить список изображений, вызвав метод [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Таким образом, чтобы извлечь изображение со страницы, нам нужно получить ссылку на страницу, затем на ресурсы страницы и, наконец, на коллекцию изображений.

Конкретное изображение мы можем извлечь, например, по индексу.

The image's index returns an [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) объект. Этот объект предоставляет метод [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-), который может быть использован для сохранения извлеченного изображения. Следующий фрагмент кода показывает, как извлечь изображения из PDF файла.

 ```java
 public void extractImage () {
        // Открыть документ
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.Page page=document.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
        // Извлечь определенное изображение
        com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
        File file=new File(fileStorage, "extracted-image.jpeg");
        try {
            java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
            // Сохранить извлеченное изображение
            xImage.save(outputImage, ImageType.getJpeg());
            outputImage.close();
        } catch (java.io.IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.
          }
```