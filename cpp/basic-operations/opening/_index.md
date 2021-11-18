---
title: Open PDF Document using C++
linktitle: Open
type: docs
weight: 20
url: /cpp/open-pdf-document/
description: Learn how to open a PDF file with Aspose.PDF for C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Open existing PDF document

There are several ways to open a document. The easiest is to specify a file name.

```cpp
void OpenDocument()
{
    String fileName("C:\\Samples\\sample.pdf");
    auto document = MakeObject<Document>(fileName);

    int countPages = document->get_Pages()->get_Count();

    std::cout << "Pages " << countPages << std::endl;
}
```

## Open existing PDF document from stream

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

## Open encrypted PDF document

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
