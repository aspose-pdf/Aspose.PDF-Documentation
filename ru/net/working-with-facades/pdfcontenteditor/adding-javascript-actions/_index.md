---
title: Adding Javascript actions PDF 
type: docs
weight: 10
url: /ru/net/adding-javascript-actions/
description: Этот раздел объясняет, как добавить Javascript-действия в существующий PDF-файл с помощью Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Класс [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor), представленный в пакете Aspose.Pdf.Facades, предоставляет гибкость для добавления Javascript-действий в PDF-файл. Вы можете создать ссылку с последовательными действиями, соответствующими выполнению пункта меню в просмотрщике PDF. Этот класс также предоставляет возможность создавать дополнительные действия для событий документа.

Прежде всего, в [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) рисуется объект, в нашем примере это [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle). И установите действие [createJavaScriptLink](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) для прямоугольника. После этого вы можете сохранить свой документ.

```csharp
  public static void AddingJavascriptActions()
        {
            PdfContentEditor editor = new PdfContentEditor();
            editor.BindPdf(_dataDir + "sample.pdf");
            // создать Javascript ссылку
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(50, 750, 50, 50);
            String code = "app.alert('Welcome to Aspose!');";
            editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);
            // сохранить выходной файл
            editor.Save(_dataDir + "JavaScriptAdded_output.pdf");
        }
```