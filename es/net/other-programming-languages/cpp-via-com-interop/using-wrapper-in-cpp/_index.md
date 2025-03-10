---
title: Usando wrapper en CPP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/using-wrapper-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using wrapper in CPP",
    "alternativeHeadline": "Effortlessly Extract Text from PDF Using Wrapper",
    "abstract": "La nueva funcionalidad de wrapper en C permite a los usuarios extraer texto de documentos PDF sin problemas utilizando Aspose.PDF for .NET a través de COM Interop. Esta característica simplifica el proceso de recuperación de contenido al permitir la interacción directa con archivos PDF a través de un ensamblaje de wrapper accesible y eficiente. Mejora tus aplicaciones con esta poderosa capacidad de recuperación de texto mientras aseguras una integración fluida dentro del ecosistema .NET",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Prerrequisitos

{{% alert color="primary" %}}

Por favor, registra Aspose.PDF for .NET con COM Interop, consulta el artículo titulado [Usar Aspose.pdf para .NET a través de COM Interop](/pdf/es/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Detalles de implementación

{{% alert color="primary" %}}

Usaremos un [wrapper](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/) para recuperar texto de documentos PDF.

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