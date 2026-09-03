---
title: Создание совместимого с PDF/3-A PDF и прикрепление счета ZUGFeRD в Java
linktitle: Прикрепить ZUGFeRD к PDF
type: docs
weight: 10
url: /ru/java/attach-zugferd/
description: Узнайте, как прикрепить XML‑счет ZUGFeRD к PDF и преобразовать его в PDF/A-3A с помощью Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Прикрепить XML‑счет ZUGFeRD к PDF‑документу с помощью Java
Abstract: В этой статье объясняется, как создать совместимый с PDF/A-3A документ‑счёт с использованием Aspose.PDF for Java. Рассматривается прикрепление XML‑счета в виде вложенного файла, настройка MIME‑типа и отношения associated‑file, преобразование PDF в PDF/A-3A и сохранение готового ZUGFeRD‑готового документа.
---
Используйте `Document` и `FileSpecification` API, когда вам нужно упаковать XML счета‑фактуры внутрь PDF для рабочих процессов в стиле ZUGFeRD.

## Прикрепите XML-счет ZUGFeRD к PDF

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) для XML-файла счета.
1. Установите метаданные встроенного файла, включая тип MIME и [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/).
1. Добавьте [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) в коллекцию встроенных файлов документа.
1. Преобразуйте документ в [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`.
1. Сохраните обновлённый PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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


