---
title: Создание PDF-файла, совместимого с PDF/3-A, и прикрепление счета-фактуры ZUGFeRD на Java.
linktitle: Прикрепите ZUGFeRD в PDF
type: docs
weight: 10
url: /java/attach-zugferd/
description: Узнайте, как прикрепить XML-счет ZUGFeRD к PDF-файлу и преобразовать его в PDF/A-3A на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Прикрепите XML-счет-фактуру ZUGFeRD к PDF-документу с помощью Java.
Abstract: В этой статье объясняется, как создать документ счета-фактуры, соответствующий PDF/A-3A, с помощью Aspose.PDF для Java. В нем рассматривается прикрепление XML-счета-фактуры в виде встроенного файла, установка типа MIME и связи связанного файла, преобразование PDF в PDF/A-3A и сохранение окончательного документа, готового к ZUGFeRD.
---
Используйте API `Document` и `FileSpecification`, когда вам нужно упаковать XML-счет-фактуру в PDF-файл для рабочих процессов в стиле ZUGFeRD.

## Прикрепите XML-счет ZUGFeRD к PDF-файлу.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) для XML-файла счета.
1. Установите метаданные встроенного файла, включая тип MIME и [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/).
1. Добавьте [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) в коллекцию встроенных файлов документа.
1. Преобразуйте документ в [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`.
1. Сохраните обновленный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void attachInvoiceZugferdFormat(Path inputFile, Path invoiceFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            String description = "Invoice metadata conforming to ZUGFeRD standard";
            FileSpecification fileSpecification = new FileSpecification(invoiceFile.toString(), description);

            fileSpecification.setMIMEType("text/xml");
            fileSpecification.setAFRelationship(AFRelationship.Alternative);

            document.getEmbeddedFiles().add("factur", fileSpecification);

            String outputFileName = outputFile.toString();
            String logPath = outputFileName.replace(".pdf", "_log.xml");
            document.convert(logPath, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
            document.save(outputFile.toString());
        }
        System.out.println("ZUGFeRD invoice attached to " + outputFile);
    }
```
