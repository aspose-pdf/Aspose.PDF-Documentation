---
title: Buka Dokumen PDF menggunakan C++
linktitle: Buka
type: docs
weight: 20
url: /id/cpp/open-pdf-document/
description: Gunakan pustaka C++ untuk membuka dokumen PDF Anda dengan cuplikan kode berikut oleh Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Buka dokumen PDF yang sudah ada

Ada beberapa cara untuk membuka dokumen. Cara termudah adalah dengan menentukan nama file.

```cpp
void OpenDocument()
{
    String fileName("C:\\Samples\\sample.pdf");
    auto document = MakeObject<Document>(fileName);

    int countPages = document->get_Pages()->get_Count();

    std::cout << "Pages " << countPages << std::endl;
}
```

## Buka dokumen PDF yang sudah ada dari stream

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

## Buka dokumen PDF terenkripsi

```cpp
void BasicOperations::OpenDocumentWithPassword()
{
    String fileName("C:\\Samples\\sample-pswd.pdf");
    String password("Aspose2020");
    try
    {
        auto document = MakeObject<Document>(fileName, password);
        int countPages = document->get_Pages()->get_Count();

        std::cout << "Halaman " << countPages << std::endl;
    }
    catch (InvalidPasswordException e)
    {
        std::cerr << e.what();
    }
}
```

## Buka dokumen PDF dari buffer memori

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

    std::cout << "Halaman " << countPages << std::endl;
}
```