---
title: Создание PDF/3-A совместимого PDF и прикрепление счета-фактуры ZUGFeRD в C#
linktitle: Прикрепление ZUGFeRD к PDF
type: docs
weight: 10
url: /net/attach-zugferd/
description: Узнайте, как генерировать документ PDF с ZUGFeRD в Aspose.PDF для .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Прикрепление ZUGFeRD к PDF

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Мы рекомендуем следовать следующим шагам для прикрепления ZUGFeRD к PDF:

* Определите переменную пути, которая указывает на папку, где расположены входные и выходные файлы PDF.
* Создайте объект документа, загрузив существующий файл PDF (например, "ZUGFeRD-test.pdf") из указанного пути.
* Создайте объект [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/), предоставив путь и описание другого файла под названием "factur-x.xml", который содержит метаданные счета, соответствующие стандарту ZUGFeRD.
* Добавьте свойства к объекту спецификации файла, такие как описание, MIME-тип и отношение AF.
* Добавьте свойства к объекту спецификации файла, такие как описание, MIME-тип и отношение AF.
* Добавьте объект спецификации файла в коллекцию встроенных файлов документа. Имя файла должно соответствовать стандарту ZUGFeRD, например, "factur-x.xml".
* Конвертируйте документ в формат PDF/A-3U, подмножество PDF, которое обеспечивает долгосрочное сохранение электронных документов. PDF/A-3U позволяет встраивать файлы любого формата в PDF документы.
* Сохраните преобразованный документ как новый PDF файл (например, "ZUGFeRD-res.pdf").

```cs
var path = @"C:\Samples\ZUGFeRD\";

var document = new Aspose.Pdf.Document(Path.Combine(path,"ZUGFeRD-test.pdf"));
// Настройка нового файла для добавления в качестве вложения
var description = "Метаданные счета, соответствующие стандарту ZUGFeRD";
var fileSpecification = new Aspose.Pdf.FileSpecification(Path.Combine(path, "factur-x.xml"), description)
{
    Description = "Zugferd",
    MIMEType = "text/xml",
    AFRelationship = Aspose.Pdf.AFRelationship.Alternative
};
// Добавление вложения в коллекцию вложений документа
document.EmbeddedFiles.Add(fileSpecification);
document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.PDF_A_3U, Aspose.Pdf.ConvertErrorAction.Delete);
document.Save(Path.Combine(path, "ZUGFeRD-res.pdf"));
```
Метод convert принимает поток, формат PDF и действие при ошибке конвертации в качестве параметров. Параметр потока может быть использован для сохранения журнала конвертации. Параметр действия при ошибке конвертации указывает, что делать, если во время конвертации возникают ошибки. В данном случае он установлен в значение "Delete", что означает, что любые элементы, не соответствующие формату PDF/A-3U, будут удалены из документа.
