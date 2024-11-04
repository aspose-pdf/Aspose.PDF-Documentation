---
title: Abrir Documento PDF usando C++
linktitle: Abrir
type: docs
weight: 20
url: /cpp/open-pdf-document/
description: Use a biblioteca C++ para abrir seu documento PDF com o próximo trecho de código da Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Abrir documento PDF existente

Existem várias maneiras de abrir um documento. A mais fácil é especificar um nome de arquivo.

```cpp
void OpenDocument()
{
    String fileName("C:\\Samples\\sample.pdf");
    auto document = MakeObject<Document>(fileName);

    int countPages = document->get_Pages()->get_Count();

    std::cout << "Pages " << countPages << std::endl;
}
```

## Abrir documento PDF existente a partir de um fluxo

```cpp
void OpenDocumentStream()
{
    String fileName("C:\\Samples\\sample.pdf");
    System::SharedPtr<System::IO::MemoryStream> stream;
    auto document = MakeObject<Document>(System::IO::File::OpenRead(fileName));

    int countPages = document->get_Pages()->get_Count();

    std::cout << "Pages " << countPages << std::endl;
}
```

## Abrir documento PDF criptografado

```cpp
void BasicOperations::OpenDocumentWithPassword()
{
    String fileName("C:\\Samples\\sample-pswd.pdf");
    String password("Aspose2020");
    try
    {
        auto document = MakeObject<Document>(fileName, password);
        int countPages = document->get_Pages()->get_Count();

        std::cout << "Páginas " << countPages << std::endl;
    }
    catch (InvalidPasswordException e)
    {
        std::cerr << e.what();
    }
}
```

## Abrir documento PDF a partir de buffer de memória

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

    std::cout << "Páginas " << countPages << std::endl;
}
```