---
title: Установка информации о PDF файле
type: docs
weight: 40
url: /net/set-pdf-file-information/
description: Этот раздел объясняет, как установить информацию о PDF файле с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Класс [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) позволяет устанавливать специфическую информацию файла PDF. Вам нужно создать объект класса [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo), а затем установить различные свойства, специфичные для файла, такие как Author, Title, Keyword и Creator и т.д. Наконец, сохраните обновленный PDF файл, используя метод [SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) объекта [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo).

Следующий фрагмент кода показывает, как установить информацию о PDF файле.

```csharp
 public static void SetPdfInfo()
        {
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf")
            {
                // Set PDF information
                Author = "Aspose",
                Title = "Hello World!",
                Keywords = "Peace and Development",
                Creator = "Aspose"
            };
            // Save updated file
            fileInfo.SaveNewInfo(_dataDir + "SetFileInfo_out.pdf");
        }
```

## Установить метаинформацию

Метод [SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) позволяет добавить любую информацию. В нашем примере мы добавили поле. Проверьте следующий фрагмент кода:

```csharp
 public static void SetMetaInfo()
        {
            // Создать экземпляр объекта PdfFileInfo
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "sample.pdf");

            // Установить новый атрибут клиента как метаинформацию
            fInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

            // Сохранить обновленный файл
            fInfo.SaveNewInfo(_dataDir + "SetMetaInfo_out.pdf");
```