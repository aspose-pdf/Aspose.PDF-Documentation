---
title: Using wrapper in CPP
type: docs
weight: 30
url: /net/using-wrapper-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using wrapper in CPP",
    "alternativeHeadline": "Effortlessly Extract Text from PDF Using Wrapper",
    "abstract": "The new wrapper functionality in C allows users to seamlessly extract text from PDF documents using Aspose.PDF for .NET via COM Interop. This feature simplifies the process of retrieving content by enabling direct interaction with PDF files through an accessible and efficient wrapper assembly. Enhance your applications with this powerful text retrieval capability while ensuring smooth integration within the .NET ecosystem",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Prerequisites

{{% alert color="primary" %}}

Please register Aspose.PDF for .NET with COM Interop, kindly check the article named [Use Aspose.pdf for .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Implementation details

{{% alert color="primary" %}}

We will use a [wrapper](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/) to retrieve text from PDF documents.

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
