---
title: Открытие PDF документа с использованием C++
linktitle: Открыть
type: docs
weight: 20
url: /cpp/open-pdf-document/
description: Используйте библиотеку C++ для открытия вашего PDF документа с помощью следующего фрагмента кода от Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Открыть существующий PDF документ

Существуют несколько способов открыть документ. Самый простой - указать имя файла.

```cpp
void OpenDocument()
{
    String fileName("C:\\Samples\\sample.pdf");
    auto document = MakeObject<Document>(fileName);

    int countPages = document->get_Pages()->get_Count();

    std::cout << "Страницы " << countPages << std::endl;
}
```

## Открыть существующий PDF документ из потока

```cpp
void OpenDocumentStream()
{
    String fileName("C:\\Samples\\sample.pdf");
    System::SharedPtr<System::IO::MemoryStream> stream;
    auto document = MakeObject<Document>(System::IO::File::OpenRead(fileName));

    int countPages = document->get_Pages()->get_Count();

    std::cout << "Страницы " << countPages << std::endl;
}
```

## Открыть зашифрованный PDF-документ

```cpp
void BasicOperations::OpenDocumentWithPassword()
{
    String fileName("C:\\Samples\\sample-pswd.pdf");
    String password("Aspose2020");
    try
    {
        auto document = MakeObject<Document>(fileName, password);
        int countPages = document->get_Pages()->get_Count();

        std::cout << "Страницы " << countPages << std::endl;
    }
    catch (InvalidPasswordException e)
    {
        std::cerr << e.what();
    }
}
```

## Открыть PDF-документ из буфера памяти

```cpp
#include <system/io/memory_stream.h>
#include <system/buffer.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>

// ...

void OpenDocumentMemory(const uint8_t *buffer, int size) {

    auto arr = MakeArray<uint8_t>(size);
    Buffer::BlockCopy(buffer, 0, arr->data_ptr(), 0, size);

    auto document = MakeObject<Document>(MakeObject<System::IO::MemoryStream>(arr));

    int countPages = document->get_Pages()->get_Count();

    std::cout << "Страницы " << countPages << std::endl;
}
```