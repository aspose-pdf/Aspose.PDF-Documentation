---
title: Извлечение шрифтов из PDF C#
linktitle: Извлечение шрифтов из PDF
type: docs
weight: 30
url: /ru/net/extract-fonts-from-pdf/
description: Используйте библиотеку Aspose.PDF для .NET для извлечения всех встроенных шрифтов из вашего PDF документа.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Если вы хотите получить все шрифты из документа PDF, вы можете использовать метод FontUtilities.GetAllFonts(), предоставленный в классе Document. Пожалуйста, проверьте следующий фрагмент кода, чтобы получить все шрифты из существующего документа PDF:

Данный фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

