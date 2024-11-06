---
title: Сохранение PDF документа с использованием C++
linktitle: Сохранить
type: docs
weight: 30
url: ru/cpp/save-pdf-document/
description: Узнайте, как сохранить PDF файл с библиотекой Aspose.PDF для C++.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Сохранение PDF документа в файловую систему

Вы можете сохранить созданный или измененный PDF документ в файловую систему, используя метод Save класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void SaveDocument()
{
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);
    // выполните некоторые манипуляции, например, добавьте новую пустую страницу
    document->get_Pages()->Add();
    document->Save(_dataDir + modifiedFileName);
}
```

## Сохранение PDF документа в поток

Вы также можете сохранить созданный или измененный PDF документ в поток, используя перегрузки методов Save.

```cpp
void SaveDocumentStream()
{
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);

    // выполните некоторые манипуляции, например, добавьте новую пустую страницу
    document->get_Pages()->Add();

    auto fileStream = System::IO::File::OpenWrite(_dataDir + modifiedFileName);
    document->Save(fileStream);
}
```

## Сохранение в формате PDF/A или PDF/X

PDF/A — это версия формата Portable Document Format (PDF), стандартизированная ISO, для использования в архивировании и долгосрочном хранении электронных документов. PDF/A отличается от PDF тем, что запрещает функции, не подходящие для долгосрочного архивирования, такие как связывание шрифтов (в отличие от встраивания шрифтов) и шифрование. Требования ISO для просмотрщиков PDF/A включают рекомендации по управлению цветом, поддержку встроенных шрифтов и пользовательский интерфейс для чтения встроенных аннотаций.

PDF/X — это подмножество стандарта PDF ISO. Цель PDF/X — облегчить обмен графикой, и поэтому он имеет ряд требований, связанных с печатью, которые не применяются к стандартным PDF файлам.

В обоих случаях используется метод Save для сохранения документов, при этом документы должны быть подготовлены с использованием [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_format_conversion_options).

```cpp
void SaveDocumentAsPDFx()
{
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла
    String infilename("SimpleResume.pdf");
    String outfilename("SimpleResume_A3U.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    auto options = new PdfFormatConversionOptions(Aspose::Pdf::PdfFormat::PDF_A_3U);
    try
    {
        document->Convert(options);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what();
    }

    document->Save(_dataDir + outfilename);
}
```