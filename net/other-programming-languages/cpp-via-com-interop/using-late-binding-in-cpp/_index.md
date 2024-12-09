---
title: Using late binding in CPP
type: docs
weight: 20
url: /net/using-late-binding-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using late binding in CPP",
    "alternativeHeadline": "Effortless PDF Text Extraction with Late Binding in C",
    "abstract": "The new feature enables developers to extract text from PDF documents using late binding in C through COM Interop with Aspose.PDF. This functionality simplifies the process of text retrieval, facilitating seamless integration into existing C applications without the need for strict type definitions",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Prerequisites

{{% alert color="primary" %}}

Please register Aspose.PDF for .NET with COM Interop, kindly check the article named [Use Aspose.pdf for .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Sample

{{% alert color="primary" %}}

This is a simple C++ code sample to extract text from PDF by means of COM Interop using late binding. For details please look at [this](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) post.

{{% /alert %}}

```cpp
#include "stdafx.h"
#include "comdef.h"

using namespace System;

String ^lateBinding(String ^file)
{
    String^ text;
    DISPID dispid;
    DISPPARAMS dp = { NULL, NULL, 0, 0};
    VARIANTARG vargs[1];
    VARIANT arg, result;
    WCHAR str[255];
    CLSID pclsid;

    // create ComHelper
    IDispatch* comHelperPtr;

    wcscpy_s(str, L"Aspose.Pdf.ComHelper");
    CLSIDFromProgID(str, &pclsid);

    HRESULT hr = CoCreateInstance(pclsid, NULL, CLSCTX_ALL, IID_IDispatch, (void **)&comHelperPtr);
    if (FAILED(hr))
    {
        Console::WriteLine(L"Error occured");
    }
    else
    {
        // set license
        IDispatch* licPtr;
        wcscpy_s(str, L"Aspose.Pdf.License");
        CLSIDFromProgID(str, &pclsid);

        HRESULT hr = CoCreateInstance(pclsid, NULL, CLSCTX_ALL, IID_IDispatch, (void **)&licPtr);

        OLECHAR* setLicense =  L"SetLicense";

        hr = licPtr->GetIDsOfNames(IID_NULL, &setLicense, 1, GetUserDefaultLCID(), &dispid);
        arg.vt = VT_BSTR;

        BSTR lic = SysAllocString(L"C:\\Temp\\Aspose.Pdf.lic");

        arg.bstrVal = lic;

        vargs[0] = arg;

        dp.rgvarg = vargs;

        dp.cArgs = 1;

        hr = licPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_METHOD, &dp, &result, NULL, NULL);

        SysFreeString(lic);

        licPtr.Release();

        // get Document

        OLECHAR* openFile =  L"OpenFile";

        hr = comHelperPtr->GetIDsOfNames(IID_NULL, &openFile, 1, GetUserDefaultLCID(), &dispid);

        arg.vt = VT_BSTR;

        arg.bstrVal = (BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer();

        vargs[0] = arg;

        dp.rgvarg = vargs;

        dp.cArgs = 1;

        hr = comHelperPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_METHOD, &dp, &result, NULL, NULL);

        IDispatch* docPtr = result.pdispVal;

        comHelperPtr.Release();

        //------------------------

        // get Pages for the Document

        OLECHAR* pages =  L"Pages";

        hr = docPtr->GetIDsOfNames(IID_NULL, &pages, 1, GetUserDefaultLCID(), &dispid);

        dp.cArgs = 0;

        hr = docPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_PROPERTYGET, &dp, &result, NULL, NULL);

        IDispatch* pagesPtr = result.pdispVal;

        //------------------------

        // create Absorber

        IDispatch* absorberPtr;

        wcscpy_s(str, L"Aspose.PDF.Text.TextAbsorber");

        CLSIDFromProgID(str, &pclsid);

        hr = CoCreateInstance(pclsid, NULL, CLSCTX_ALL, IID_IDispatch, (void **)&absorberPtr);

        //------------------------

        // browse text

        arg.vt = VT_DISPATCH;

        arg.pdispVal = absorberPtr;

        vargs[0] = arg;

        dp.rgvarg = vargs;

        dp.cArgs = 1;

        OLECHAR* accept_4 = L"Accept_4";

        hr = pagesPtr->GetIDsOfNames(IID_NULL, &accept_4, 1, GetUserDefaultLCID(), &dispid);

        hr = pagesPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_METHOD, &dp, &result, NULL, NULL);

        //------------------------

        // retrieve text

        OLECHAR* _text = L"Text";

        dp.cArgs = 0;

        hr = absorberPtr->GetIDsOfNames(IID_NULL, &_text, 1, GetUserDefaultLCID(), &dispid);

        hr = absorberPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_PROPERTYGET, &dp, &result, 0, 0);

        //------------------------

        text = gcnew String(result.bstrVal);

        docPtr.Release();

        pagesPtr.Release();

        absorberPtr.Release();

    }

    return text;
}

int main(array<System::String ^> ^args)
{
    if (args->Length != 1)
    {
        Console::WriteLine("Missing parameters\nUsage:testCOM <pdf file>");
        return 0;
    }

    CoInitialize(NULL);
    String ^text = lateBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("Extracted text:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<empty>");
    Console::WriteLine("---");
    return 0;
}
```
