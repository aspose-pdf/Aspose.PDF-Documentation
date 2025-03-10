---
title: CPP에서 조기 바인딩 사용하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/using-early-binding-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using early binding in CPP",
    "alternativeHeadline": "Effortless PDF Text Extraction with C Early Binding",
    "abstract": "Aspose.PDF for .NET을 사용하여 C의 조기 바인딩의 힘을 발견하십시오. 이 기능은 COM Interop을 사용하여 PDF 파일에서 텍스트 추출을 단순화하여 컴파일 오류를 최소화하고 코딩 효율성을 향상시키는 간소화된 접근 방식을 제공합니다. 조기 바인딩의 기능을 활용하여 신뢰할 수 있는 PDF 처리를 통해 C 프로젝트를 개선하십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "523",
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
    "url": "/net/using-early-binding-in-cpp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-early-binding-in-cpp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 전제 조건

{{% alert color="primary" %}}

COM Interop으로 Aspose.PDF for .NET을 등록하십시오. [COM Interop을 통해 Aspose.pdf for .NET 사용하기](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)라는 기사를 확인하십시오.

{{% /alert %}}

## 샘플

{{% alert color="primary" %}}

다음은 조기 바인딩을 사용하여 COM Interop을 통해 PDF 파일에서 텍스트를 추출하는 간단한 C++ 코드 샘플입니다. 샘플을 실행하기 전에 다음 사항에 유의하십시오.

- **#import** *typelib.tlb*는 C++ 컴파일러가 2개의 파일인 *typelib.tlh*와 *typelib.tli*를 생성하게 합니다. 기본적으로 이 파일들은 한 번만 생성되므로, 새로운 버전을 얻으려면 프로젝트를 완전히 다시 컴파일해야 합니다.
- 종종 하나의 TLB 파일만 가져오는 것이 많은 컴파일 오류를 초래합니다. 오류에는 해결되지 않은 종속성과 이름 충돌의 두 가지 유형이 있습니다. 프로젝트를 컴파일할 수 없는 경우 tlh 파일을 열고 주석 처리된 첫 번째 줄을 확인하십시오. 여기에서 다음과 같은 섹션을 볼 수 있습니다.

```cpp
// Cross-referenced type libraries:
```

하나 이상의 **#import**가 포함되어 있습니다. 이를 코드에 복사하여 기본 타입 라이브러리를 가져오기 전에 ***같은*** 순서로 수행하십시오. 이렇게 하면 첫 번째 유형의 문제를 피할 수 있습니다. 다음 유형의 문제는 C++ 환경에 많은 매크로, 미리 정의된 함수 등이 있어 타입 라이브러리 메서드와 충돌할 수 있다는 사실에서 발생합니다. 예를 들어, GetType은 C++에서 널리 사용되지만 Aspose.PDF에서도 사용됩니다. **#import** 지시문의 **rename** 및 **auto_rename** 속성이 가능한 경고 및 오류를 제거하는 데 매우 유용하다는 것을 알았습니다.

- 때때로 **uses** 네임스페이스의 클래스가 타입 라이브러리의 이름과 충돌하므로 이러한 경우에는 **using namespace** 대신 전체 클래스 이름을 사용해야 합니다. 예를 들어, 아래 코드 조각에서 StringToBSTR이 호출되는 방식을 참조하십시오.
{{% /alert %}}

자세한 내용은 [이](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) 게시물을 참조하십시오.

C++ 예제

```cpp
#include "stdafx.h"
#import "C:\Windows\Microsoft.NET\Framework\v2.0.50727\System.Drawing.tlb"
#import "C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscorlib.tlb" auto_rename

#import "C:\Temp\Aspose.PDF.tlb" rename("GetType", "GetType_") auto_rename

using namespace System;
String ^earlyBinding(String ^file)
{
    String ^text;
    // Create ComHelper

    Aspose_Pdf::_ComHelperPtr comHelperPtr;
    HRESULT hr = comHelperPtr.CreateInstance(__uuidof(Aspose_Pdf::ComHelper));
    if (FAILED(hr))
    {
        Console::WriteLine(L"Error occured");
    }
    else
    {
        // Set license
        Aspose_Pdf::_LicensePtr licPtr;
        licPtr.CreateInstance(__uuidof(Aspose_Pdf::License));
        licPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        licPtr.Release();

        // Get Document
        Aspose_Pdf::_DocumentPtr docPtr;
        docPtr = comHelperPtr->OpenFile((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());

        comHelperPtr.Release();

        // Create Absorber
        Aspose_Pdf::_TextAbsorberPtr absorberPtr;
        HRESULT hRes = absorberPtr.CreateInstance(__uuidof(Aspose_Pdf::TextAbsorber));

        // Browse text
        docPtr->GetPages()->Accept_4(absorberPtr);

        // Retrieve text
        BSTR extractedText = absorberPtr->GetText();
        text = gcnew String(extractedText);
        docPtr.Release();
        absorberPtr.Release();
    }
    return text;
}

int main(array<System::String ^> ^args)
{
    CoInitialize(NULL);
    if (args->Length != 1)
    {
        Console::WriteLine("Missing parameters\nUsage:testCOM <pdf file>");
        return 0;
    }

    String ^text = earlyBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("Extracted text:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<empty>");
    Console::WriteLine("---");
    return 0;
}
```