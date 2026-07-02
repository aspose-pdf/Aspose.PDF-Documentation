---
title: Конвертировать PDF‑файл в PDF/A
linktitle: Конвертировать PDF‑файл в PDF/A
type: docs
weight: 180
url: /ru/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2026-07-01"
description: Эта тема показывает, как Aspose.PDF for Java позволяет конвертировать PDF‑файл в PDF/A‑совместимый PDF‑файл.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF позволяет конвертировать PDF‑файл в PDF/A‑совместимый PDF‑файл. Перед этим файл должен быть проверен. В этой статье объясняется, как это сделать.

Обратите внимание, что мы используем Adobe Preflight для проверки соответствия PDF/A. Все инструменты на рынке имеют своё «representation» соответствия PDF/A. Пожалуйста, проверьте эту статью на [инструменты валидации PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) для справки. Мы выбрали продукты Adobe для проверки того, как Aspose.PDF создает PDF-файлы, потому что Adobe находится в центре всего, что связано с PDF.

Перед тем как конвертировать PDF в файл, соответствующий PDF/A, проверьте PDF с помощью метода validate. Результат проверки сохраняется в XML‑файл, после чего этот результат также передаётся методу convert. Вы также можете указать действие для элементов, которые нельзя конвертировать, используя [ДействиеПриОшибкеКонвертации](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) перечисление.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## Преобразование PDF в PDF/A_1b

Следующий фрагмент кода показывает, как преобразовать файлы PDF в PDF, соответствующий стандарту PDF/A-1b.

```java
public void convertPDFtoPDFa1b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Save output document
        document.save(pdfaFileName.toString());
    }
```

Для выполнения только проверки используйте следующую строку кода:

```java
public void ValidatePDF_A_1B() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Validate to PDF/A compliant document

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("Document is valid");
        }
        else {
            resultMessage.setText("Document is not valid");
        }
    }
```

## Конвертация PDF в PDF/A_3b

```java
    public void convertPDFtoPDFa3b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Save output document
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Преобразование PDF в PDF/A_3a

```java
public void convertPDFtoPDFa3a() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Save output document
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Конвертация PDF в PDF/A_2a

```java
public void convertPDFtoPDFa2a() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Save output document
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## Преобразование PDF в PDF/A_3U

```java
 public void convertPDFtoPDFa3u() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Save output document
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Создать PDF/A-3 и добавить XML-файл

Aspose.PDF для Android через Java предлагает возможность конвертировать PDF‑файлы в формат PDF/A и также поддерживает добавление файлов в виде вложения в PDF‑документ. Если вам необходимо прикреплять файлы к формату, соответствующему PDF/A, мы рекомендуем использовать значение PDF_A_3A из перечисления com.aspose.pdf.PdfFormat; PDF/A_3a — это формат, который предоставляет возможность прикреплять любые типы файлов в качестве вложения к PDF/A‑совместимому файлу. Однако после прикрепления файла его следует снова конвертировать в формат Pdf-3a, чтобы исправить метаданные. Пожалуйста, ознакомьтесь со следующим фрагментом кода.

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // Save output document
        try {
            // load XML file
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Sample xml file");
            // Add attachment to document's attachment collection
            document.getEmbeddedFiles().add(fileSpecification);
            document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

