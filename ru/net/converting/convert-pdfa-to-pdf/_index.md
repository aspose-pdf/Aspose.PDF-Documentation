---
title: Конвертация PDF/A в формат PDF
linktitle: Конвертация PDF/A в формат PDF
type: docs
weight: 110
url: ru/net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: Эта тема покажет, как Aspose.PDF позволяет конвертировать файл PDF/A в документ PDF с помощью библиотеки .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Конвертация документа PDF/A в PDF

Конвертация документа PDF/A в PDF означает снятие ограничений <abbr title="Portable Document Format Archive">PDF/A</abbr> с оригинального документа.
Класс [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) имеет метод [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance) для удаления информации о соответствии PDF из входного/исходного файла.

```csharp
public static void ConvertPDFAtoPDF()
{
    // Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // Удаление информации о соответствии PDF/A
    pdfDocument.RemovePdfaCompliance();
    // Сохранение обновленного документа
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
Эта информация также удаляется, если вы вносите изменения в документ (например, добавляете страницы). В следующем примере выходной документ теряет соответствие PDF/A после добавления страницы.

```csharp
public static void ConvertPDFAtoPDFAdvanced()
{
    // Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // Добавление новой (пустой) страницы удаляет информацию о соответствии PDF/A.
    pdfDocument.Pages.Add();
    // Сохранить обновленный документ
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
