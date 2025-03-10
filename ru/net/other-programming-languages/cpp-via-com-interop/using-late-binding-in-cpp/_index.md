---
title: Использование позднего связывания в CPP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/using-late-binding-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using late binding in CPP",
    "alternativeHeadline": "Effortless PDF Text Extraction with Late Binding in C",
    "abstract": "Новая функция позволяет разработчикам извлекать текст из PDF-документов с помощью позднего связывания на языке C через COM Interop с Aspose.PDF. Эта функциональность упрощает процесс извлечения текста, облегчая беспроблемную интеграцию в существующие приложения на C без необходимости строгого определения типов",
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
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

## Необходимые условия

{{% alert color="primary" %}}

Пожалуйста, зарегистрируйте Aspose.PDF for .NET с COM Interop, ознакомьтесь со статьёй под названием [Используйте Aspose.pdf для .NET через COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Пример

{{% alert color="primary" %}}

Это простой пример кода на C++, который демонстрирует извлечение текста из PDF с помощью COM Interop и позднего связывания. Для получения подробной информации ознакомьтесь с [этим](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) сообщением.

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