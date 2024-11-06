---

title: Convert PDF File to PDF/A 
linktitle: Convert PDF File to PDF/A 
type: docs
weight: 180
url: ru/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2021-06-05"
description: Эта тема показывает, как Aspose.PDF для Java позволяет преобразовать PDF файл в PDF файл, соответствующий стандарту PDF/A.  
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF позволяет вам преобразовать PDF файл в файл, соответствующий стандарту PDF/A. Прежде чем это сделать, файл должен быть проверен. Эта статья объясняет, как это сделать.

Обратите внимание, что мы следуем Adobe Preflight для проверки соответствия PDF/A. Все инструменты на рынке имеют своё собственное "представление" о соответствии PDF/A. Пожалуйста, ознакомьтесь с этой статьей о [инструментах проверки PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) для справки. Мы выбрали продукты Adobe для проверки того, как Aspose.PDF создаёт PDF файлы, потому что Adobe находится в центре всего, что связано с PDF.

Перед преобразованием PDF в файл, соответствующий стандарту PDF/A, проверьте PDF с помощью метода validate.
 Результат проверки сохраняется в XML файл, и затем этот результат также передается в метод convert. Вы также можете указать действие для элементов, которые не могут быть преобразованы, используя перечисление [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## Конвертация PDF в PDF/A_1b

Следующий фрагмент кода показывает, как конвертировать PDF файлы в соответствие с PDF/A-1b.

```java
public void convertPDFtoPDFa1b() {
        // Открыть документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Преобразовать в документ, соответствующий PDF/A
        // Во время процесса конвертации также выполняется проверка
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Сохранить выходной документ
        document.save(pdfaFileName.toString());
    }
```

Для выполнения только проверки используйте следующую строку кода:

```java
public void ValidatePDF_A_1B() {
        // Открыть документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Проверка на соответствие документу PDF/A

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("Документ является действительным");
        }
        else {
            resultMessage.setText("Документ не является действительным");
        }
    }
```

## Конвертация PDF в PDF/A_3b

```java
    public void convertPDFtoPDFa3b() {
        // Открыть документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Преобразование в документ, соответствующий PDF/A
        // Во время процесса преобразования также выполняется проверка
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Сохранить выходной документ
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


## PDF to PDF/A_3a Конвертация

```java
public void convertPDFtoPDFa3a() {
        // Открыть документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Преобразовать в документ, соответствующий PDF/A
        // В процессе преобразования также выполняется проверка
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Сохранить выходной документ
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

## PDF to PDF/A_2a Конвертация

```java
public void convertPDFtoPDFa2a() {
        // Открыть документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Преобразовать в документ, соответствующий PDF/A
        // В процессе преобразования также выполняется проверка
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Сохранить выходной документ
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


## PDF к PDF/A_3U Конвертация

```java
 public void convertPDFtoPDFa3u() {
        // Открыть документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Преобразовать в документ, соответствующий PDF/A
        // Во время процесса преобразования также выполняется проверка
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Сохранить выходной документ
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

## Создать PDF/A-3 и прикрепить XML файл

Aspose.PDF для Android через Java предлагает функцию преобразования PDF файлов в формат PDF/A, а также поддерживает возможность добавления файлов в качестве вложений к PDF документу.
 В случае, если у вас есть требование прикрепить файлы в соответствии с форматом PDF/A, мы рекомендуем использовать значение PDF_A_3A из перечисления com.aspose.pdf.PdfFormat. Формат PDF/A_3a предоставляет возможность прикреплять любые форматы файлов в качестве вложений к файлу, соответствующему стандарту PDF/A. Однако, после того как файл прикреплен, его следует вновь преобразовать в формат Pdf-3a, чтобы исправить метаданные. Пожалуйста, ознакомьтесь со следующим фрагментом кода.

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // Открыть документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Преобразовать в документ, соответствующий PDF/A
        // Во время процесса преобразования также выполняется проверка
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // Сохранить выходной документ
        try {
            // загрузить XML файл
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Пример XML файла");
            // Добавить вложение в коллекцию вложений документа
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