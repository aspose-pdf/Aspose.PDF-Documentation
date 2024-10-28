---
title: Создание программного документа PDF
linktitle: Создать PDF
type: docs
weight: 10
url: /net/create-document/
description: На этой странице описано, как создать документ PDF с нуля с помощью библиотеки Aspose.PDF.
---

Aspose.PDF для .NET API позволяет создавать и читать файлы PDF с использованием C# и VB.NET. API может использоваться в различных приложениях .NET, включая WinForms, ASP.NET и многие другие. В этой статье мы покажем, как использовать Aspose.PDF для .NET API для легкого создания и чтения файлов PDF в приложениях .NET.

## Как создать файл PDF с использованием C#

Для создания файла PDF с использованием C# можно использовать следующие шаги.

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Добавьте объект [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) в коллекцию [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) объекта Document
1.
1. Сохраните полученный PDF документ

Следующий фрагмент кода также работает с новым графическим интерфейсом [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// Инициализируем объект документа
Document document = new Document();
// Добавляем страницу
Page page = document.Pages.Add();
// Добавляем текст на новую страницу
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// Сохраняем обновленный PDF
document.Save(dataDir + "HelloWorld_out.pdf")
```

В данном случае мы создаем одностраничный PDF-документ формата A4 с портретной ориентацией. Наша страница будет содержать "Hello, World" в верхней левой части страницы.
