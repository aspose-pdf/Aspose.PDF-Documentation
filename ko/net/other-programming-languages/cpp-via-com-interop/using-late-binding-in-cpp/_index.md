---
title: CPP에서 지연 바인딩 사용하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/using-late-binding-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using late binding in CPP",
    "alternativeHeadline": "Effortless PDF Text Extraction with Late Binding in C",
    "abstract": "이 새로운 기능은 개발자가 Aspose.PDF와의 COM Interop을 통해 C에서 지연 바인딩을 사용하여 PDF 문서에서 텍스트를 추출할 수 있게 합니다. 이 기능은 텍스트 검색 과정을 단순화하여 엄격한 타입 정의 없이 기존 C 애플리케이션에 원활하게 통합할 수 있도록 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "473",
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
    "url": "/net/using-late-binding-in-cpp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-late-binding-in-cpp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 필수 조건

{{% alert color="primary" %}}

COM Interop으로 Aspose.PDF for .NET를 등록해 주세요. [COM Interop을 통한 Aspose.pdf for .NET 사용하기](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)라는 기사를 확인해 주세요.

{{% /alert %}}

## 샘플

{{% alert color="primary" %}}

이것은 지연 바인딩을 사용하여 COM Interop을 통해 PDF에서 텍스트를 추출하는 간단한 C++ 코드 샘플입니다. 자세한 내용은 [이](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) 게시물을 참조하세요.

{{% /alert %}}

```cpp
#include "pch.h"
#include "comdef.h"

using namespace System;

String^ lateBinding(String^ file)
{
    String^ text;
    DISPID dispid;
    DISPPARAMS dp = { NULL, NULL, 0, 0 };
    VARIANTARG vargs[1];
    VARIANT arg, result;
    WCHAR str[255];
    CLSID pclsid;

    // Create ComHelper
    IDispatch* comHelperPtr;

    wcscpy_s(str, L"Aspose.Pdf.ComHelper");
    CLSIDFromProgID(str, &pclsid);

    HRESULT hr = CoCreateInstance(pclsid, NULL, CLSCTX_ALL, IID_IDispatch, (void**)&comHelperPtr);
    if (FAILED(hr))
    {
        Console::WriteLine(L"Error occured");
    }
    else
    {
        // Set license
        IDispatch* licPtr;
        wcscpy_s(str, L"Aspose.Pdf.License");
        CLSIDFromProgID(str, &pclsid);

        HRESULT hr = CoCreateInstance(pclsid, NULL, CLSCTX_ALL, IID_IDispatch, (void**)&licPtr);

        OLECHAR* setLicense = L"SetLicense";

        hr = licPtr->GetIDsOfNames(IID_NULL, &setLicense, 1, GetUserDefaultLCID(), &dispid);
        arg.vt = VT_BSTR;

        BSTR lic = SysAllocString(L"C:\\Temp\\Aspose.Pdf.lic");

        arg.bstrVal = lic;

        vargs[0] = arg;

        dp.rgvarg = vargs;

        dp.cArgs = 1;

        hr = licPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_METHOD, &dp, &result, NULL, NULL);

        SysFreeString(lic);

        licPtr->Release();

        // Get Document

        OLECHAR* openFile = L"OpenFile";

        hr = comHelperPtr->GetIDsOfNames(IID_NULL, &openFile, 1, GetUserDefaultLCID(), &dispid);

        arg.vt = VT_BSTR;

        arg.bstrVal = (BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer();

        vargs[0] = arg;

        dp.rgvarg = vargs;

        dp.cArgs = 1;

        hr = comHelperPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_METHOD, &dp, &result, NULL, NULL);

        IDispatch* docPtr = result.pdispVal;

        comHelperPtr->Release();

        // Get Pages for the Document

        OLECHAR* pages = L"Pages";

        hr = docPtr->GetIDsOfNames(IID_NULL, &pages, 1, GetUserDefaultLCID(), &dispid);

        dp.cArgs = 0;

        hr = docPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_PROPERTYGET, &dp, &result, NULL, NULL);

        IDispatch* pagesPtr = result.pdispVal;

        // Create Absorber

        IDispatch* absorberPtr;

        wcscpy_s(str, L"Aspose.PDF.Text.TextAbsorber");

        CLSIDFromProgID(str, &pclsid);

        hr = CoCreateInstance(pclsid, NULL, CLSCTX_ALL, IID_IDispatch, (void**)&absorberPtr);

        // Browse text

        arg.vt = VT_DISPATCH;

        arg.pdispVal = absorberPtr;

        vargs[0] = arg;

        dp.rgvarg = vargs;

        dp.cArgs = 1;

        OLECHAR* accept_4 = L"Accept_4";

        hr = pagesPtr->GetIDsOfNames(IID_NULL, &accept_4, 1, GetUserDefaultLCID(), &dispid);

        hr = pagesPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_METHOD, &dp, &result, NULL, NULL);

        // Retrieve text

        OLECHAR* _text = L"Text";

        dp.cArgs = 0;

        hr = absorberPtr->GetIDsOfNames(IID_NULL, &_text, 1, GetUserDefaultLCID(), &dispid);

        hr = absorberPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_PROPERTYGET, &dp, &result, 0, 0);

        text = gcnew String(result.bstrVal);

        docPtr->Release();

        pagesPtr->Release();

        absorberPtr->Release();

    }

    return text;
}

int main(array<System::String^>^ args)
{
    if (args->Length != 1)
    {
        Console::WriteLine("Missing parameters\nUsage:testCOM.exe <pdf file>");
        return 0;
    }

    CoInitialize(NULL);
    String^ text = lateBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("Extracted text:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<empty>");
    Console::WriteLine("---");
    return 0;
}
```