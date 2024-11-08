---
title: Конвертировать PDF/A в формат PDF
linktitle: Конвертировать PDF/A в формат PDF
type: docs
weight: 110
url: /ru/java/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать файл PDF/A в PDF документ с помощью Java библиотеки.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Конвертировать документ PDF/A в PDF

Конвертирование документа PDF/A в PDF означает удаление ограничений <abbr title="Portable Document Format Archive">PDF/A</abbr> из оригинального документа. Класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) имеет метод RemovePdfaCompliance(..) для удаления информации о соответствии PDF из входного/исходного файла.

```java
public static void runPDFA_to_PDF() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Создать объект Document
    Document document = new Document(pdfaDocumentFileName);

    // Удалить информацию о соответствии PDF/A
    document.removePdfaCompliance();

    // Сохранить результат в формате XML
    document.save(documentFileName);
    document.close();
}
```


This info also removes if you make any changes in the document (e.g. add pages). In the following example, the output document loses PDF/A compliance after the page adding.

```java
public static void runPDFAtoPDFAdvanced() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Создание объекта Document
    Document document = new Document(pdfaDocumentFileName);

    // Добавление новой (пустой) страницы удаляет информацию о соответствии PDF/A.
    document.getPages().add();

    // Сохранение обновленного документа
    document.save(documentFileName);
    document.close();
}
```