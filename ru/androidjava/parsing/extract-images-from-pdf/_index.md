---
title: Извлечь изображения из PDF
linktitle: Извлечь изображения
type: docs
weight: 20
url: /ru/androidjava/extract-images-from-the-pdf-file/
description: Как извлечь часть изображения из PDF с помощью Aspose.PDF for Android via Java
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Каждая страница PDF‑документа содержит ресурсы (изображения, формы и шрифты). Мы можем получить доступ к этим ресурсам, вызвав [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) метод. Class [Ресурсы](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) содержат [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) и мы можем получить список изображений, вызвав [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) метод.

Таким образом, чтобы извлечь изображение со страницы, нам нужно получить ссылку на страницу, затем на ресурсы страницы и, наконец, на коллекцию изображений.
Конкретное изображение мы можем извлечь, например, по индексу.

Индекс изображения возвращает [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) объект.
Этот объект предоставляет [Сохранить](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) метод, который можно использовать для сохранения извлечённого изображения. Следующий фрагмент кода показывает, как извлекать изображения из PDF‑файла.

 ```java
 public void extractImage () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.Page page=document.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
        // Extract a particular image
        com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
        File file=new File(fileStorage, "extracted-image.jpeg");
        try {
            java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
            // Save output image
            xImage.save(outputImage, ImageType.getJpeg());
            outputImage.close();
        } catch (java.io.IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.
          }
```

