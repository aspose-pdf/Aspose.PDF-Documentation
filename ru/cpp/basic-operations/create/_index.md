---
title: Создание PDF документа с использованием C++
linktitle: Создать
type: docs
weight: 10
url: ru/cpp/create-document/
description: Самая популярная и основная задача работы с PDF файлом - создание документа с нуля. Используйте библиотеку Aspose.PDF для C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF для C++** API позволяет разработчикам приложений на C++ встроить функциональность обработки PDF документов в их приложения. Он может использоваться для создания и чтения PDF файлов без необходимости установки какого-либо другого программного обеспечения на базовой машине. Aspose.PDF для C++ может использоваться в различных типах приложений на C++, таких как QT, MFC и консольные приложения.

## Как создать PDF файл с использованием C++

Для создания PDF файла с использованием C++ можно использовать следующие шаги.

1. Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. Добавьте [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) к объекту документа
1. Создайте объект [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) в коллекцию [Paragraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs/) страницы
1. Сохраните полученный PDF документ

```cpp
void CreatePDF() {
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String filename("sample-new.pdf");

    // Инициализировать объект документа
    auto document = MakeObject<Document>();
    // Добавить страницу
    auto page = document->get_Pages()->Add();

    // Добавить текст на новую страницу
    auto textFragment = MakeObject<TextFragment>(u"Hello World!");
    page->get_Paragraphs()->Add(textFragment);

    // Сохранить обновленный PDF
    String outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```