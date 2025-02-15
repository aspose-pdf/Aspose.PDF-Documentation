---
title: Ouvrir un document PDF en utilisant C++
linktitle: Ouvrir
type: docs
weight: 20
url: /fr/cpp/open-pdf-document/
description: Utilisez la bibliothèque C++ pour ouvrir votre document PDF avec le prochain extrait de code par Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ouvrir un document PDF existant

Il existe plusieurs façons d'ouvrir un document. La plus simple est de spécifier un nom de fichier.

```cpp
void OpenDocument()
{
    String fileName("C:\\Samples\\sample.pdf");
    auto document = MakeObject<Document>(fileName);

    int countPages = document->get_Pages()->get_Count();

    std::cout << "Pages " << countPages << std::endl;
}
```

## Ouvrir un document PDF existant depuis un flux

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

## Ouvrir un document PDF chiffré

```cpp
void BasicOperations::OpenDocumentWithPassword()
{
    String fileName("C:\\Samples\\sample-pswd.pdf");
    String password("Aspose2020");
    try
    {
        auto document = MakeObject<Document>(fileName, password);
        int countPages = document->get_Pages()->get_Count();

        std::cout << "Pages " << countPages << std::endl;
    }
    catch (InvalidPasswordException e)
    {
        std::cerr << e.what();
    }
}
```

## Ouvrir un document PDF à partir d'un tampon mémoire

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

    std::cout << "Pages " << countPages << std::endl;
}
```