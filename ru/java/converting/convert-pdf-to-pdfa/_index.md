---
title: Convert PDF to PDF/A formats 
linktitle: Convert PDF to PDF/A formats
type: docs
weight: 100
url: /ru/java/convert-pdf-to-pdfa/
lastmod: "2021-11-19"
description: Этот раздел показывает, как Aspose.PDF позволяет конвертировать PDF-файл в PDF/A совместимый PDF-файл. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Java** позволяет конвертировать PDF-файл в PDF/A совместимый PDF-файл. Перед этим файл должен быть проверен. В этой статье объясняется, как это сделать.

Обратите внимание, что мы следуем Adobe Preflight для проверки соответствия PDF/A. Все инструменты на рынке имеют свое собственное "представление" соответствия PDF/A. Пожалуйста, ознакомьтесь с этой статьей о [инструментах проверки PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) для справки. Мы выбрали продукты Adobe для проверки того, как Aspose.PDF создает PDF-файлы, потому что Adobe находится в центре всего, что связано с PDF.

Перед конвертацией PDF в PDF/A совместимый файл, проверьте PDF, используя метод validate.
 Результат проверки сохраняется в XML-файл, и затем этот результат также передается в метод преобразования. Вы также можете указать действие для элементов, которые не могут быть преобразованы, используя перечисление [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

## Конвертация PDF в PDF/A_1b

Следующий фрагмент кода показывает, как конвертировать PDF-файлы в PDF, совместимый с PDF/A-1b.

```java
// Открыть документ
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Преобразовать в документ, совместимый с PDF/A
// Во время процесса преобразования также выполняется валидация
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

// Сохранить выходной документ
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

Чтобы выполнить только валидацию, используйте следующую строку кода:

```java
// Открыть документ
Document document = new Document(DATA_DIR + "ValidatePDFAStandard.pdf");

// Проверить PDF на соответствие PDF/A-1a
if (document.validate(DATA_DIR + "validation-result-A1A.xml", PdfFormat.PDF_A_1B)) {
    System.out.println("Действительный");
} else {
    System.out.println("Недействительный");
}
document.close();
```

## PDF to PDF/A_3b Conversion

Начиная с [Aspose.PDF for Java 9.3.0](https://downloads.aspose.com/pdf/java), API также поддерживает преобразование PDF файлов в формат PDF/A_3b.

```java
// Открыть документ
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Преобразовать в документ, соответствующий PDF/A
// В процессе преобразования также выполняется проверка
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

// Сохранить выходной документ
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

## PDF to PDF/A_3a Conversion

Начиная с [Aspose.PDF for Java 10.6.0](https://downloads.aspose.com/pdf/java), API также поддерживает преобразование PDF файлов в формат PDF/A_3a.

```java
// Открыть документ
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Преобразовать в документ, соответствующий PDF/A
// В процессе преобразования также выполняется проверка
document.convert("file.log", PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

// Сохранить выходной документ
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```


## PDF to PDF/A_2a Conversion

Начиная с версии [Aspose.PDF for Java 10.2.0](https://downloads.aspose.com/pdf/java), API предлагает функцию преобразования PDF файлов в формат PDF/A3.

```java
    public static void ConvertPDFtoPDFa2a() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Преобразовать в документ, соответствующий PDF/A
        // Во время процесса преобразования также выполняется проверка
        pdfDocument.convert("file.log", PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Сохранить выходной документ
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## PDF to PDF/A_3U Conversion

Начиная с версии Aspose.PDF for Java 17.2.0, API предлагает функцию преобразования PDF файлов в формат PDF/A_3U.

```java
    public static void ConvertPDFtoPDFa3u() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Преобразовать в документ, соответствующий PDF/A
        // Во время процесса преобразования также выполняется проверка
        pdfDocument.convert("file.log", PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Сохранить выходной документ
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```


## Создание PDF/A-3 и прикрепление XML-файла

Aspose.PDF для Java предлагает возможность конвертировать PDF-файлы в формат PDF/A, а также поддерживает возможности добавления файлов в качестве вложений к PDF-документу. Если у вас есть необходимость прикрепить файлы к формату, соответствующему PDF/A, мы рекомендуем использовать значение PDF_A_3A из перечисления com.aspose.pdf.PdfFormat. PDF/A_3a - это формат, который предоставляет возможность прикреплять любой формат файла в качестве вложения к файлу, соответствующему PDF/A. Однако, как только файл прикреплен, вы должны снова конвертировать его в формат Pdf-3a, чтобы исправить метаданные. Пожалуйста, ознакомьтесь с приведенным ниже фрагментом кода.

```java
    public static void ConvertPDFtoPDFa3u_attachXML() {
        Document doc = new Document();
        // добавить страницу в PDF-файл
        doc.getPages().add();
        // загрузить XML файл
        FileSpecification fileSpecification = new FileSpecification(_dataDir + "attachment.xml", "Пример XML файла");
        // Добавить вложение в коллекцию вложений документа
        doc.getEmbeddedFiles().add(fileSpecification);
        // выполнить преобразование в PDF/A_3a
        doc.convert(_dataDir + "log.xml", PdfFormat.PDF_A_3A/* или PDF_A_3B */, ConvertErrorAction.Delete);
        // сохранить конечный PDF файл
        doc.save(_dataDir + "attached_PDFA_3A.pdf");
    }
```


{{% alert color="primary" %}}
**Попробуйте преобразовать PDF в PDF/A онлайн**

Aspose.PDF для Java предлагает вам бесплатное онлайн-приложение ["PDF в PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), где вы можете попробовать изучить функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в PDF/A с бесплатным приложением](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}