---
title: CPP에서 래퍼 사용하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/using-wrapper-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using wrapper in CPP",
    "alternativeHeadline": "Effortlessly Extract Text from PDF Using Wrapper",
    "abstract": "C의 새로운 래퍼 기능은 사용자가 COM Interop을 통해 Aspose.PDF for .NET를 사용하여 PDF 문서에서 텍스트를 원활하게 추출할 수 있도록 합니다. 이 기능은 접근 가능하고 효율적인 래퍼 어셈블리를 통해 PDF 파일과의 직접적인 상호작용을 가능하게 하여 콘텐츠를 검색하는 과정을 단순화합니다. .NET 생태계 내에서 원활한 통합을 보장하면서 이 강력한 텍스트 검색 기능으로 애플리케이션을 향상시키십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "194",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/using-wrapper-in-cpp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-wrapper-in-cpp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 필수 조건

{{% alert color="primary" %}}

COM Interop을 통해 Aspose.PDF for .NET를 등록해 주십시오. [COM Interop을 통해 Aspose.pdf for .NET 사용하기](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)라는 기사를 확인해 주십시오.

{{% /alert %}}

## 구현 세부사항

{{% alert color="primary" %}}

PDF 문서에서 텍스트를 검색하기 위해 [래퍼](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/)를 사용할 것입니다.

{{% /alert %}}

```cpp
#include "pch.h"
#include <comdef.h>

#import "TextRetriever.tlb"
using namespace System;

String^ wrapper(String^ file)
{
    String^ text;

    TextRetriever::IRetrieverPtr retrieverPtr;
    HRESULT hr = retrieverPtr.CreateInstance(__uuidof(TextRetriever::Retriever));

    if (FAILED(hr))
    {
        Console::WriteLine(L"Error occured");
    }
    else
    {
        // set license
        retrieverPtr->SetLicense("Aspose.PDF.lic");
        // retrieve text

        BSTR extractedText = retrieverPtr->GetText((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());
        text = gcnew String(extractedText);
        retrieverPtr.Release();
    }
    return text;
}

int main(array<System::String^>^ args)
{
    CoInitialize(NULL);
    if (args->Length != 1)
    {
        Console::WriteLine("Missing parameters\nUsage:testCOM <pdf file>");
        return 0;
    }

    String^ text = wrapper(args[0]);
    CoUninitialize();
    Console::WriteLine("Extracted text:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<empty>");
    Console::WriteLine("---");
    return 0;
}
```