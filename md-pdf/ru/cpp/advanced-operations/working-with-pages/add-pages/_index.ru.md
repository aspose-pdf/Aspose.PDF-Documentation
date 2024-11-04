---
title: Добавить страницы в PDF с C++
linktitle: Добавить страницы
type: docs
weight: 10
url: /cpp/add-pages/
description: Эта статья обучает, как вставить (добавить) страницу в нужное место в PDF файле. Узнайте, как перемещать, удалять (удалять) страницы из PDF файла с использованием C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Этот раздел показывает, как добавить страницы в PDF, используя библиотеку **Aspose.PDF для C++**.

Aspose.PDF для C++ API предоставляет полную гибкость для работы со страницами в PDF документе с использованием C++.

Он поддерживает все страницы PDF документа в [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection), который может быть использован для работы с PDF страницами. Aspose.PDF для C++ позволяет вставить страницу в PDF документ в любое место в файле, а также добавлять страницы в конец PDF файла.

## Добавить или вставить страницу в PDF файл

Aspose.PDF для C++ позволяет вставить страницу в PDF документ в любое место в файле, а также добавлять страницы в конец PDF файла.

### Вставить пустую страницу в PDF файл в нужное место

Следующий пример кода объясняет, как добавить страницу в PDF-документ.

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) с входным PDF-файлом.
2. Вызовите метод [Insert](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#a1fb1fe44df4d325df5ad41b691501bb2) коллекции [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) с указанным индексом.
3. Сохраните выходной PDF

Следующий фрагмент кода показывает, как вставить страницу в PDF-файл.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void InsertEmptyPageAtDesiredLocation() {
    // Открыть документ
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Вставить пустую страницу в PDF
    document->get_Pages()->Insert(2);

    // Сохранить выходной файл
    document->Save(_dataDir + outputFileName);
}
```

In the following code example, you can insert an empty page to the desired location by copying the parameters of the specified page:

```cpp
void InsertEmptyPageAtDesiredLocation2() {
    // Открыть документ
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto page = document->get_Pages()->idx_get(1);
    // Вставить пустую страницу в PDF
    auto pageNew = document->get_Pages()->Insert(2);

    //копировать параметры страницы со страницы 1
    pageNew->set_ArtBox(page->get_ArtBox());
    pageNew->set_BleedBox(page->get_BleedBox());
    pageNew->set_CropBox(page->get_CropBox());
    pageNew->set_MediaBox(page->get_MediaBox());
    pageNew->set_TrimBox(page->get_TrimBox());

    // Сохранить выходной файл
    document->Save(_dataDir + outputFileName);
}
```

### Добавить пустую страницу в конец PDF файла

Иногда вы хотите убедиться, что документ заканчивается на пустой странице. Этот раздел объясняет, как вставить пустую страницу в конец PDF-документа.

Чтобы вставить пустую страницу в конец PDF-файла:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) с входным PDF-файлом.
1. Вызовите метод [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) коллекции [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection), без параметров.
1. Сохраните выходной PDF, используя метод Save.

Следующий фрагмент кода показывает, как вставить пустую страницу в конец PDF-файла.

```cpp
void AddEmptyPageEnd() {
    // Открыть документ
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String inputFileName("InsertEmptyPageAtEnd.pdf");
    String outputFileName("InsertEmptyPageAtEnd_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Вставить пустую страницу в конец PDF-файла
    document->get_Pages()->Add();

    // Сохранить выходной файл
    document->Save(_dataDir + outputFileName);
}
```