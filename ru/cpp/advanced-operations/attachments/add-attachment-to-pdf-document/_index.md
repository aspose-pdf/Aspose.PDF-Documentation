---
title: Добавление вложения в PDF документ
linktitle: Добавление вложения в PDF документ
type: docs
weight: 10
url: /ru/cpp/add-attachment-to-pdf-document/
description: Эта страница описывает, как добавить вложение в PDF файл с помощью библиотеки Aspose.PDF для C++
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Вложения могут содержать разнообразную информацию и могут быть различных типов файлов. Эта статья объясняет, как добавить вложение в PDF файл.

1. Создайте новый C++ проект.
1. Добавьте ссылку на Aspose.PDF DLL.
1. Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Создайте объект [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) с файлом, который вы добавляете, и описанием файла.
1. Добавьте объект [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) в коллекцию [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) с помощью метода Add коллекции.

Коллекция [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) содержит все вложения в PDF файле. Следующий фрагмент кода показывает, как добавить вложение в PDF документ.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithAttachments::AddingAttachment()
{

String _dataDir("C:\\Samples\\");


// Открыть документ

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddAttachment.pdf");


// Настроить новый файл для добавления в качестве вложения

auto fileSpecification = MakeObject<FileSpecification>(_dataDir + u"test.txt", u"Пример текстового файла");


// Добавить вложение в коллекцию вложений документа

pdfDocument->get_EmbeddedFiles()->Add(fileSpecification);


// Сохранить новый результат

pdfDocument->Save(_dataDir + u"AddAttachment_out.pdf");
}
```