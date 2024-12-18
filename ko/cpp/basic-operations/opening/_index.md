---
title: C++를 사용하여 PDF 문서 열기
linktitle: 열기
type: docs
weight: 20
url: /ko/cpp/open-pdf-document/
description: Aspose.PDF의 다음 코드 조각으로 PDF 문서를 여는 C++ 라이브러리를 사용하십시오.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 기존 PDF 문서 열기

문서를 여는 방법은 여러 가지가 있습니다. 가장 쉬운 방법은 파일 이름을 지정하는 것입니다.

```cpp
void OpenDocument()
{
    String fileName("C:\\Samples\\sample.pdf");
    auto document = MakeObject<Document>(fileName);

    int countPages = document->get_Pages()->get_Count();

    std::cout << "Pages " << countPages << std::endl;
}
```

## 스트림에서 기존 PDF 문서 열기

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

## 암호화된 PDF 문서 열기

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

## 메모리 버퍼에서 PDF 문서 열기

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