---
title: Сохранение PDF документа программно
linktitle: Сохранение PDF
type: docs
weight: 30
url: /net/save-pdf-document/
description: Узнайте, как сохранить PDF файл на C# с помощью библиотеки Aspose.PDF для .NET. Сохранение PDF документа в файловую систему, в поток и в веб-приложениях.
aliases:
    - /net/saving/
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Следующий фрагмент кода также работает с новым графическим интерфейсом [Aspose.Drawing](/pdf/net/drawing/).

## Сохранение PDF документа в файловую систему

Вы можете сохранить созданный или измененный PDF документ в файловую систему, используя метод `Save` класса `Document`.
Если вы не указываете тип формата (опции), то документ сохраняется в формате Aspose.PDF v.1.7 (*.pdf).

```csharp
public static void SaveDocument()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // выполнить некоторые манипуляции, например, добавить новую пустую страницу
    pdfDocument.Pages.Add();
    pdfDocument.Save(modifiedFileName);
}
```
## Сохранение PDF-документа в поток

Вы также можете сохранить созданный или измененный PDF-документ в поток, используя перегрузки методов `Save`.

```csharp
public static void SaveDocumentStream()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // произвести некоторые манипуляции, например добавить новую пустую страницу
    pdfDocument.Pages.Add();
    pdfDocument.Save(System.IO.File.OpenWrite(modifiedFileName));
}
```

## Сохранение PDF-документа в веб-приложениях

Для сохранения документов в веб-приложениях можно использовать вышеуказанные способы. Кроме того, класс `Document` имеет перегруженный метод `Save` для использования с классом [HttpResponse](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpresponse?view=netframework-4.8).

```csharp
var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
var pdfDocument = new Aspose.Pdf.Document(originalFileName);
// произвести некоторые манипуляции, например добавить новую пустую страницу
pdfDocument.Pages.Add();
pdfDocument.Save(Response, originalFileName, ContentDisposition.Attachment, new PdfSaveOptions());
```
Для получения более подробного объяснения, пожалуйста, перейдите в раздел [Витрина](/pdf/net/showcases/).

## Сохранение в формате PDF/A или PDF/X

PDF/A является стандартизированной по ISO версией формата Portable Document Format (PDF) для использования в архивировании и долгосрочном сохранении электронных документов.
PDF/A отличается от PDF тем, что запрещает функции, не подходящие для долгосрочного архивирования, такие как связывание шрифтов (в отличие от встраивания шрифтов) и шифрование. Требования ISO к просмотрщикам PDF/A включают руководства по управлению цветом, поддержку встроенных шрифтов и пользовательский интерфейс для чтения встроенных аннотаций.

PDF/X является подмножеством стандарта PDF ISO. Цель PDF/X заключается в облегчении обмена графикой, поэтому он имеет ряд требований, связанных с печатью, которые не применимы к стандартным файлам PDF.

В обоих случаях используется метод `Save` для сохранения документов, в то время как документы должны быть подготовлены с использованием метода `Convert`.

```csharp
public static void SaveDocumentAsPDFx()
{
    var pdfDocument = new Aspose.Pdf.Document("..\\..\\..\\Samples\\SimpleResume.pdf");
    pdfDocument.Pages.Add();
    pdfDocument.Convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    pdfDocument.Save("..\\..\\..\\Samples\\SimpleResume_X3.pdf");
}
```

