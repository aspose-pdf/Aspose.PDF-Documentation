---
title: Извлечение Вложений из PDF Файла
type: docs
weight: 10
url: ru/java/extract-attachments/
description: Этот раздел объясняет, как извлекать вложения из pdf с помощью класса PdfExtractor.
lastmod: "2021-06-05"
draft: false
---

Одна из основных категорий в рамках возможностей извлечения [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) - это извлечение вложений.
 This category provides a set of methods, which not only help extract the attachments but also provides the methods which can give you the attachment related information i.e. [GetAttachmentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachmentInfo--) and [GetAttachName](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachNames--) methods provide attachment information and attachment name respectively. In order to extract and then get attachments we use [ExtractAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractAttachment--) and [GetAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachment--) methods.

Следующая часть кода показывает, как использовать методы PdfExtractor:

```java
  public static void ExtractAttachments() {
        PdfExtractor pdfExtractor = new PdfExtractor();
        pdfExtractor.bindPdf(_dataDir + "sample-attach.pdf");

        // Извлечение вложений
        pdfExtractor.extractAttachment();

        // Получение имен вложений
        if (pdfExtractor.getAttachNames().size() > 0) {
            System.out.println("Извлечение и сохранение...");
            // Получение извлеченных вложений
            pdfExtractor.getAttachment(_dataDir);
        }
    }
```