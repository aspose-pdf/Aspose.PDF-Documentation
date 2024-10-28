---
title: Добавление Javascript-действий в существующий PDF файл
type: docs
weight: 10
url: /java/adding-javascript-actions/
description: Этот раздел объясняет, как добавить Javascript-действия в существующий PDF файл с помощью Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Класс [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor), представленный в пакете com.aspose.pdf.facades, предоставляет возможность добавлять Javascript-действия в PDF файл. Вы можете создать ссылку с последовательными действиями, соответствующими выполнению элемента меню в PDF просмотрщике. Этот класс также предоставляет возможность создавать дополнительные действия для событий документа.

Прежде всего, объект рисуется в [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), в нашем примере это [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
 И установите действие [createJavaScriptLink](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createJavaScriptLink-java.lang.String-java.awt.Rectangle-int-java.awt.Color-) для прямоугольника. После этого вы можете сохранить ваш документ.

```java
 public static void AddingJavascriptActions() {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");
        // создать Javascript ссылку
        java.awt.Rectangle rect = new java.awt.Rectangle(50, 750, 50, 50);
        String code = "app.alert('Добро пожаловать в Aspose!');";
        editor.createJavaScriptLink(code, rect, 1, java.awt.Color.GREEN);
        // сохранить выходной файл
        editor.save(_dataDir+"JavaScriptAdded_output.pdf");
    }
```