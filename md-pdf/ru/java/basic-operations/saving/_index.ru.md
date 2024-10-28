---
title: Сохранить PDF документ 
linktitle: Сохранить
type: docs
weight: 30
url: /java/save-pdf-document/
description: Узнайте, как сохранить PDF файл с библиотекой Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Сохранить PDF документ в файловую систему

Вы можете сохранить созданный или измененный PDF документ в файловую систему, используя метод Save класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
Если вы не указываете тип формата (опции), то документ сохраняется в формате Aspose.PDF v.1.7 (*.pdf).

```java
package com.aspose.pdf.examples;


import java.io.FileOutputStream;

import java.nio.file.Path;
import java.nio.file.Paths;
import com.aspose.pdf.*;

public final class BasicOperationsSave {

    private BasicOperationsSave() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) {
        SaveDocument();
        SaveDocumentStream();
        SaveDocumentAsPDFx();
    }

    public static void SaveDocument() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // выполнить некоторые изменения, например, добавить новую пустую страницу
        pdfDocument.getPages().add();
        pdfDocument.save(modifiedFileName);
    }
```


## Сохранение PDF документа в поток

Вы также можете сохранить созданный или измененный PDF документ в поток, используя перегрузки методов Save.

```java
public static void SaveDocumentStream() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // выполните некоторые манипуляции, например, добавьте новую пустую страницу
        pdfDocument.getPages().add();
        try {
            pdfDocument.save(new FileOutputStream(modifiedFileName));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

```

## Сохранение PDF документа в веб-приложениях

Для сохранения документов в веб-приложениях вы можете использовать предложенные выше способы. Кроме того, класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) имеет перегруженный метод Save.
```java
    // @RequestMapping(value = "/files/{file_name}", method = RequestMethod.GET)
    // public void getFile(@PathVariable("file_name") String fileName, HttpServletResponse response) {
    //     try {
    //         response.setContentType("application/pdf");
    //         // получите ваш файл как InputStream
    //         InputStream is = new FileInputStream(_dataDir + fileName);
    //         // скопируйте его в OutputStream ответа
    //         org.apache.commons.io.IOUtils.copy(is, response.getOutputStream());
    //         response.flushBuffer();
    //     } catch (IOException ex) {
    //         log.info("Ошибка при записи файла в выходной поток. Имя файла было '{}'", fileName, ex);
    //         throw new RuntimeException("Ошибка ввода-вывода при записи файла в выходной поток");
    //     }
    // }
```


Для более детального объяснения, пожалуйста, перейдите в раздел [Showcase]().

## Сохранение в формате PDF/A или PDF/X

PDF/A — это стандартизированная версия формата Portable Document Format (PDF) по ISO для использования в архивировании и долгосрочном хранении электронных документов. PDF/A отличается от PDF тем, что запрещает функции, не подходящие для долгосрочного архивирования, такие как связывание шрифтов (в отличие от встраивания шрифтов) и шифрование. Требования ISO для просмотрщиков PDF/A включают рекомендации по управлению цветом, поддержку встроенных шрифтов и пользовательский интерфейс для чтения встроенных аннотаций.

PDF/X является подмножеством стандарта PDF ISO. Цель PDF/X — облегчить обмен графикой, и поэтому он имеет ряд требований, связанных с печатью, которые не применяются к стандартным файлам PDF.

В обоих случаях метод Save используется для хранения документов, в то время как документы должны быть подготовлены с использованием метода Convert.

```java
public static void SaveDocumentAsPDFx() {
        Document pdfDocument = new Document("../../../Samples/SimpleResume.pdf");
        pdfDocument.getPages().add();
        pdfDocument.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
        pdfDocument.save("../../../Samples/SimpleResume_X3.pdf");
    }

}
```