---
title: Объединение PDF с использованием C++
linktitle: Объединение файлов PDF
type: docs
weight: 50
url: /ru/cpp/merge-pdf-documents/
description: На этой странице объясняется, как объединить документы PDF в один файл PDF с помощью C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Объединение PDF файлов — это не простая задача, но очень популярная. Вы можете использовать библиотеку Aspose.PDF для C++, чтобы быстро и легко объединить PDF файлы в один документ.

## Объединение файлов PDF с использованием C++

Чтобы объединить два PDF файла:

1. Создайте два объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), каждый из которых содержит один из входных PDF файлов.
1. Затем вызовите метод Add коллекции [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) для объекта Document, к которому вы хотите добавить другой PDF файл.
1. Добавьте [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) второго документа в первый файл.
1. Наконец, сохраните выходной PDF файл, используя метод Save.

Следующий фрагмент кода показывает, как объединить файлы PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
void MergingDocuments() {
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String pdfDocumentFileName1("Concat1.pdf");
    String pdfDocumentFileName2("Concat2.pdf");
    String outputFileName("ConcatenatePdfFiles.pdf");

    // Открыть документ
    auto pdfDocument1 = MakeObject<Document>(_dataDir + pdfDocumentFileName1);
    auto pdfDocument2 = MakeObject<Document>(_dataDir + pdfDocumentFileName2);

    // Добавить страницы второго документа к первому
    pdfDocument1->get_Pages()->Add(pdfDocument2->get_Pages());

    // Сохранить объединенный выходной файл
    pdfDocument1->Save(_dataDir+outputFileName);
}
```

## Пример в реальном времени

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) — это бесплатное веб-приложение, которое позволяет вам исследовать, как работает функциональность объединения презентаций.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)