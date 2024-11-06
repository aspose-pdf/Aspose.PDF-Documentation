---
title: Преобразование PDF в DOC 
linktitle: Преобразование PDF в DOC
type: docs
weight: 70
url: ru/androidjava/convert-pdf-to-doc/
lastmod: "2021-06-05"
description: Преобразуйте PDF-файл в формат DOC с легкостью и полным контролем с помощью Aspose.PDF для Android через Java. Узнайте больше о том, как настроить преобразование файла Microsoft Word Doc в PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Одной из самых популярных функций является преобразование PDF в Microsoft Word DOC, что делает содержание легким для манипуляции. Aspose.PDF для Android через Java позволяет вам конвертировать PDF-файлы в DOC.

**Aspose.PDF для Android через Java** может создавать PDF-документы с нуля и является отличным инструментарием для обновления, редактирования и манипулирования существующими PDF-документами.
 Важной функцией является возможность преобразования страниц и целых PDF-документов в изображения. Другой популярной функцией является преобразование PDF в Microsoft Word DOC, что делает контент легким для редактирования. (Большинство пользователей не могут редактировать PDF-документы, но могут легко работать с таблицами, текстом и изображениями в Microsoft Word.)

Чтобы сделать вещи простыми и понятными, Aspose.PDF для Android через Java предоставляет двухстрочный код для преобразования исходного PDF-файла в DOC-файл.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество преобразования Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

Следующий фрагмент кода показывает процесс преобразования PDF-файла в формат DOC.

```java
 public void convertPDFtoDOC() {
        // Открыть исходный PDF-документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Сохранить файл в формате MS документа
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```