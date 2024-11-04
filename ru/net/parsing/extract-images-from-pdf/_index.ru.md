---
title: Извлечение изображений из PDF в C#
linktitle: Извлечение изображений из PDF
type: docs
weight: 20
url: /net/extract-images-from-the-pdf-file/
description: Как извлечь часть изображения из PDF с использованием Aspose.PDF для .NET в C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Изображения находятся в коллекции [Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images) каждой страницы в коллекции [Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources). Чтобы извлечь изображение с определенной страницы, получите изображение из коллекции Images, используя конкретный индекс изображения.

Индекс изображения возвращает объект [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage). Этот объект предоставляет метод Save, который можно использовать для сохранения извлеченного изображения. Следующий фрагмент кода показывает, как извлечь изображения из файла PDF.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

 ```csharp
 // Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 ```
```
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Открыть документ
Document pdfDocument = new Document(dataDir + "ExtractImages.pdf");

// Извлечь конкретное изображение
XImage xImage = pdfDocument.Pages[1].Resources.Images[1];

FileStream outputImage = new FileStream(dataDir + "output.jpg", FileMode.Create);

// Сохранить выходное изображение
xImage.Save(outputImage, ImageFormat.Jpeg);
outputImage.Close();

dataDir = dataDir + "ExtractImages_out.pdf";

// Сохранить обновленный PDF файл
pdfDocument.Save(dataDir);
```
