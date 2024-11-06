---
title: Программное разделение PDF
linktitle: Разделение PDF файлов
type: docs
weight: 60
url: ru/cpp/split-pdf-document/
description: Эта тема показывает, как разделить страницы PDF на отдельные PDF файлы с помощью C++.
lastmod: "2022-09-01"
sitemap:
    changefreq: "monthy"
    priority: 0.7
---

## Живой пример

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) — это бесплатное онлайн веб-приложение, которое позволяет исследовать, как работает функциональность разделения презентаций.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Эта тема показывает, как разделить страницы PDF на отдельные PDF файлы в ваших приложениях на C++. Чтобы разделить страницы PDF на файлы с одной страницей с использованием C++, можно следовать следующим шагам:

1. Проходите по страницам PDF документа через коллекцию [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. Для каждой итерации создайте новый объект Document и скопируйте отдельный объект [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) в пустой документ.
1. Сохраните новый PDF, используя метод Save.

Следующий фрагмент кода на C++ показывает, как разделить страницы PDF на отдельные PDF-файлы.

```cpp
void SplittingDocuments() {
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String documentFileName("sample.pdf");
    
    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + documentFileName);

    int pageCount = 1;

    // Перебор всех страниц
    for(auto page : document->get_Pages())
    {
        auto newDocument = MakeObject<Document>(_dataDir + documentFileName);
        newDocument->get_Pages()->CopyPage(page);
        newDocument->Save(_dataDir + u"page_" + pageCount + u"_out.pdf");
        pageCount++;
    }
}
```