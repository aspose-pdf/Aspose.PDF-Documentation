---
title: Преобразовать PDF/A в PDF
linktitle: Преобразовать PDF/A в PDF
type: docs
weight: 350
url: /ru/androidjava/convert-pdfa-to-pdf/
lastmod: "2026-07-01"
description: Чтобы преобразовать PDF/A в PDF, необходимо удалить ограничения из оригинального документа. Aspose.PDF for Android via Java позволяет решить эту проблему легко и просто.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Преобразование документа PDF/A в PDF означает удаление <abbr title="Portable Document Format Archive
" >PDF/A</abbr> ограничение из оригинального документа. Класс [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) имеет метод RemovePdfaCompliance(..) для удаления
информация о соблюдении PDF из входного/исходного файла.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Create Document object
            document = new Document(pdfaDocumentFileName);

            // Remove PDF/A compliance information
            document.removePdfaCompliance();

            // Save output in XML format
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```

Эта информация также удаляется, если вы вносите какие‑либо изменения в документ (например, добавляете страницы). В следующем примере выходной документ теряет соответствие PDF/A после добавления страницы.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Create Document object
        document = new Document(pdfaDocumentFileName);

        // Adding a new (empty) page removes PDF/A compliance information.
        document.getPages().add();

        // Save updated document
        document.save(pdfDocumentFileName);
    }
```




