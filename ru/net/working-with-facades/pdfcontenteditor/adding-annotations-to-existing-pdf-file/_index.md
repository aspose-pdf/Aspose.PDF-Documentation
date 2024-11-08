---
title: Добавление аннотаций в существующий PDF файл
type: docs
weight: 80
url: /ru/net/adding-annotations-to-existing-pdf-file/
description: Этот раздел объясняет, как добавить аннотации в существующий PDF файл с помощью Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавление аннотации свободного текста в существующий PDF файл (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) позволяет добавлять аннотации различных типов в существующий PDF файл. Вы можете использовать соответствующий метод, чтобы добавить конкретную аннотацию. Например, в следующем фрагменте кода мы использовали метод [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) для добавления аннотации типа [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation).

Любой тип аннотаций может быть добавлен в PDF файл таким же образом. Первым делом, вам нужно создать объект типа [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и привязать входной PDF-файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Во-вторых, вам нужно создать объект Rectangle для указания области аннотации.

После этого вы можете вызвать метод [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) для добавления аннотации [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), а затем использовать метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) для сохранения обновленного PDF-файла.

Следующий пример кода показывает, как добавить аннотацию свободного текста в PDF-файл.

```csharp
  public static void AddFreeTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateFreeText(rect, "Free Text Demo", 1); // последний параметр - номер страницы
            editor.Save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
        }
```
## Добавить текстовую аннотацию в существующий PDF файл (facades)

В этом примере вам также нужно создать объект типа [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и привязать входной PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Во-вторых, необходимо создать объект Rectangle, чтобы указать область аннотации. После этого вы можете вызвать метод [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) для добавления аннотации FreeText, создания заголовка ваших аннотаций и номера страницы, на которой расположена аннотация.

```csharp
 public static void AddTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);
            editor.Save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
        }
```

## Добавить аннотацию линии в существующий PDF файл (фасады)

Мы также указываем прямоугольник, координаты начала и конца линии, номер страницы, толщину, стиль и цвет рамки аннотации, тип штриха линии, тип начала и конца линии.

```csharp
  public static void AddLineAnnotation()
        {
            var document = new Document(_dataDir + "Appartments.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            // Создать аннотацию линии
            editor.CreateLine(
                new System.Drawing.Rectangle(550, 93, 562, 439),
                "Test",
                556, 99, 556, 443, 1, 2,
                System.Drawing.Color.Red,
                "dash",
                new int[] { 1, 0, 3 },
                new[] { "Open", "Open" });
            editor.Save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
        }
```