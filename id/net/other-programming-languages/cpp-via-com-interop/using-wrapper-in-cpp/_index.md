---
title: Menggunakan wrapper di CPP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/using-wrapper-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using wrapper in CPP",
    "alternativeHeadline": "Effortlessly Extract Text from PDF Using Wrapper",
    "abstract": "Fungsi wrapper baru di C memungkinkan pengguna untuk dengan mudah mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF for .NET melalui COM Interop. Fitur ini menyederhanakan proses pengambilan konten dengan memungkinkan interaksi langsung dengan file PDF melalui assembly wrapper yang dapat diakses dan efisien. Tingkatkan aplikasi Anda dengan kemampuan pengambilan teks yang kuat ini sambil memastikan integrasi yang lancar dalam ekosistem .NET",
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
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat mengatasi tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Prasyarat

{{% alert color="primary" %}}

Silakan daftarkan Aspose.PDF for .NET dengan COM Interop, silakan periksa artikel yang berjudul [Gunakan Aspose.pdf untuk .NET melalui COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Detail implementasi

{{% alert color="primary" %}}

Kami akan menggunakan [wrapper](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/) untuk mengambil teks dari dokumen PDF.

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