---
title: Open PDF document programmatically
linktitle: Open PDF
type: docs
weight: 20
url: /cpp/open-pdf-document/
description: Open PDF files in C++ from a path, stream, or memory and load password-protected documents.
lastmod: "2026-10-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Open a PDF from a file

1. Pass the input file path to the [Document constructor](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/document/).
1. Read the number of pages with [PageCollection::get_Count()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/get_count/).
1. Print the page count.

```cpp
#include <iostream>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Exceptions/InvalidPasswordException.h>

using namespace System;
using namespace Aspose::Pdf;

void OpenDocument(String path_infile)
{
    auto document = MakeObject<Document>(path_infile);
    int countPages = document->get_Pages()->get_Count();
    std::cout << "Number of Pages :" << countPages << std::endl;
}
```

## Open a PDF from a file stream

1. Open a readable stream with [System::IO::File::OpenRead()](https://reference.aspose.com/pdf/cpp/system.io/file/openread/).
1. Pass the stream to the [Document constructor](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/document/).
1. Read the number of pages with [PageCollection::get_Count()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/get_count/).
1. Print the page count.

```cpp
#include <iostream>

#include <system/io/file.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Exceptions/InvalidPasswordException.h>

using namespace System;
using namespace Aspose::Pdf;
void OpenDocumentStream(String path_infile)
{
    auto document = MakeObject<Document>(System::IO::File::OpenRead(path_infile));
    int countPages = document->get_Pages()->get_Count();
    std::cout << "Number of Pages :" << countPages << std::endl;
}
```

## Open a PDF from memory

1. Read the input PDF into a byte array.
1. Create a [System::IO::MemoryStream](https://reference.aspose.com/pdf/cpp/system.io/memorystream/) from the byte array.
1. Pass the memory stream to the [Document constructor](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/document/).
1. Read the number of pages with [PageCollection::get_Count()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/get_count/).
1. Print the page count.

```cpp
#include <iostream>

#include <system/io/file.h>
#include <system/io/memory_stream.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

using namespace System;
using namespace Aspose::Pdf;

void OpenDocumentMemory(String path_infile)
{
    auto bytes = System::IO::File::ReadAllBytes(path_infile);
    auto document = MakeObject<Document>(MakeObject<System::IO::MemoryStream>(bytes));

    int countPages = document->get_Pages()->get_Count();
    std::cout << "Pages " << countPages << std::endl;
}
```

## Open a password-protected PDF

1. Pass the input file path and password to the [Document constructor](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/document/).
1. Read the number of pages with [PageCollection::get_Count()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/get_count/).
1. Print the page count.
1. Catch [InvalidPasswordException](https://reference.aspose.com/pdf/cpp/aspose.pdf/) if the password is incorrect.

```cpp
#include <iostream>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Exceptions/InvalidPasswordException.h>

using namespace System;
using namespace Aspose::Pdf;
void OpenDocumentWithPassword(String path_infile, String password)
{
    try
    {
        auto document = MakeObject<Document>(path_infile, password);
        int countPages = document->get_Pages()->get_Count();

        std::cout << "Pages " << countPages << std::endl;
    }
    catch (Aspose::Pdf::InvalidPasswordException& e)
    {
        std::cerr << e.what();
    }
}
```
