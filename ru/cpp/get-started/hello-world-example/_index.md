---
title: Aspose.PDF С++ Example
linktitle: Hello World Example
type: docs
weight: 40
url: /ru/cpp/hello-world-example/
description: Эта страница показывает, как использовать простое программирование для создания PDF-документа, содержащего текст - Hello World.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.6
---

Пример "Hello World" традиционно используется для ознакомления с функциями языка программирования или программного обеспечения с простым примером использования.

Aspose.PDF для C++ — это API для работы с PDF, богатый функциями, который позволяет разработчикам встраивать возможности создания, манипуляции и преобразования PDF-документов в свои приложения на C++. Он поддерживает работу со многими популярными форматами файлов, включая PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX и форматы файлов изображений. В этой статье мы создаем PDF-документ, содержащий текст "Hello World!". После установки Aspose.PDF для C++ в вашей среде, вы можете выполнить приведенный ниже пример кода, чтобы увидеть, как работает API Aspose.PDF.

Ниже приведенный фрагмент кода следует этим шагам:

1. Создайте [класс String](https://reference.aspose.com/pdf/cpp/class/system.string) для имени пути и имени файла.
1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). На этом шаге мы создадим пустой PDF-документ с некоторыми метаданными, но без страниц.
1. Добавьте [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) к объекту документа. Теперь в нашем документе будет одна страница.
1. [Сохраните](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) полученный PDF-документ

Следующий фрагмент кода - это программа Hello World, демонстрирующая работу Aspose.PDF для C++ API.

```cpp
void ExampleSimple()
{
    // Буфер для хранения объединенного пути.
    String outputFileName;

    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String filename("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Добавить текст на новую страницу
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Сохранить обновленный PDF
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```