---
title: Конвертировать PDF в DOC
linktitle: Конвертировать PDF в DOC
type: docs
weight: 70
url: /ru/androidjava/convert-pdf-to-doc/
lastmod: "2026-07-01"
description: Конвертировать файл PDF в формат DOC легко и полностью контролировать процесс с Aspose.PDF for Android via Java. Узнайте больше о том, как оптимизировать конвертацию файлов Microsoft Word Doc в PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Одна из самых популярных функций — конвертация PDF в Microsoft Word DOC, что делает содержимое легко управляемым. Aspose.PDF for Android via Java позволяет конвертировать файлы PDF в DOC.

**Aspose.PDF for Android via Java** может создавать PDF‑документы с нуля и является отличным набором инструментов для обновления, редактирования и манипулирования существующими PDF‑документами. Важной функцией является возможность конвертировать страницы и целые PDF‑документы в изображения. Ещё одна популярная функция — конвертация PDF в Microsoft Word DOC, что делает содержимое легко управляемым. (Большинство пользователей не могут редактировать PDF‑документы, но могут легко работать с таблицами, текстом и изображениями в Microsoft Word.)

Чтобы упростить процесс и сделать его понятным, Aspose.PDF for Android via Java предоставляет двухстрочный код для преобразования исходного PDF‑файла в файл DOC.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

Следующий фрагмент кода показывает процесс преобразования PDF-файла в формат DOC.

```java
 public void convertPDFtoDOC() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Save the file into MS document format
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


