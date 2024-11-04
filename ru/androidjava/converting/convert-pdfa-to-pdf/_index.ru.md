---
title: Конвертировать PDF/A в PDF 
linktitle: Конвертировать PDF/A в PDF
type: docs
weight: 350
url: /androidjava/convert-pdfa-to-pdf/
lastmod: "2021-06-05"
description: Чтобы конвертировать PDF/A в PDF, следует удалить ограничения из оригинального документа. Aspose.PDF для Android через Java позволяет решить эту задачу легко и просто.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Конвертация документа PDF/A в PDF означает удаление ограничения <abbr title="Portable Document Format Archive
">PDF/A</abbr> из оригинального документа. Класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) имеет метод RemovePdfaCompliance(..) для удаления
информации о соответствии PDF из входного/исходного файла.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Создать объект Document
            document = new Document(pdfaDocumentFileName);

            // Удалить информацию о соответствии PDF/A
            document.removePdfaCompliance();

            // Сохранить результат в формате XML
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```


Эта информация также удаляется, если вы вносите какие-либо изменения в документ (например, добавляете страницы). В следующем примере выходной документ теряет соответствие PDF/A после добавления страницы.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Создание объекта Document
        document = new Document(pdfaDocumentFileName);

        // Добавление новой (пустой) страницы удаляет информацию о соответствии PDF/A.
        document.getPages().add();

        // Сохранение обновленного документа
        document.save(pdfDocumentFileName);
    }
```