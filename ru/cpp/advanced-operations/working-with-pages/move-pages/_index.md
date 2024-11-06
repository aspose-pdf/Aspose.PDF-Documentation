---
title: Перемещение страниц PDF программно на C++
linktitle: Перемещение страниц PDF
type: docs
weight: 20
url: ru/cpp/move-pages/
description: Попробуйте переместить страницы в нужное место или в конец PDF файла с помощью Aspose.PDF для C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Перемещение страницы из одного PDF документа в другой

Перемещение страниц PDF в документе — это очень интересная и популярная задача.
В этой теме объясняется, как переместить страницу из одного PDF документа в конец другого документа с использованием C++.
Чтобы переместить страницу, мы должны:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) с исходным PDF файлом.
1. Получите страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Добавьте](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) страницу в целевой документ.
1. Сохраните выходной PDF, используя метод Save.
1. [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) страницу в исходном документе.
1. Сохраните исходный PDF, используя метод Save.

Следующий фрагмент кода показывает, как переместить одну страницу.

```cpp
void MovePage()
{
    // Открыть документ
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    dstDocument->get_Pages()->Add(page);
    // Сохранить выходной файл
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete(2);
    srcDocument->Save(dstFileName);
}
```

## Перемещение нескольких страниц из одного PDF документа в другой

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) с исходным PDF файлом.
1. Определите массив с номерами страниц для перемещения.
1. Запустите цикл по массиву:
1. Получите страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Добавьте](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) страницу в целевой документ.
1. Сохраните выходной PDF, используя метод Save.
1. [Удалите](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) страницу в исходном документе.
1. Сохраните исходный PDF, используя метод Save.

Следующий фрагмент кода показывает, как вставить пустую страницу в конец PDF файла.

```cpp
void MoveBunchPages()
{
    // Открыть документ
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();


    auto pages = MakeArray<int>({ 1,3 });

    for (auto pageIndex : pages)
    {
        auto page = srcDocument->get_Pages()->idx_get(pageIndex);
        dstDocument->get_Pages()->Add(page);
    }
    // Сохранить выходные файлы
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete();
    srcDocument->Save(dstFileName);
}
```
## Перемещение страницы в новое место в текущем PDF документе

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) с исходным PDF файлом.
1. Получите страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Добавьте](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) страницу на новое место (например, в конец).
1. [Удалите](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) страницу в предыдущем месте.
1. Сохраните выходной PDF, используя метод Save.

```cpp
void MovePagesInOnePDF()
{
    // Открыть документ
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    srcDocument->get_Pages()->Add(page);
    srcDocument->get_Pages()->Delete(2);

    // Сохранить выходной файл
    srcDocument->Save(dstFileName);
}
```