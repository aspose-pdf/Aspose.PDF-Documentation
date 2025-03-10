---
title: Uso de enlace temprano en CPP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/using-early-binding-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using early binding in CPP",
    "alternativeHeadline": "Effortless PDF Text Extraction with C Early Binding",
    "abstract": "Descubre el poder del enlace temprano en C con Aspose.PDF for .NET. Esta característica simplifica la extracción de texto de archivos PDF utilizando COM Interop, proporcionando un enfoque optimizado que minimiza los errores de compilación y mejora la eficiencia en la codificación. Aprovecha las capacidades del enlace temprano para mejorar tus proyectos en C con un manejo confiable de PDF",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Requisitos previos

{{% alert color="primary" %}}

Por favor, registra Aspose.PDF for .NET con COM Interop, revisa el artículo titulado [Usar Aspose.pdf para .NET a través de COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Ejemplo

{{% alert color="primary" %}}

Este es un simple ejemplo de código en C++ para extraer texto de archivos PDF utilizando COM Interop con enlace temprano. Antes de ejecutar el ejemplo, presta atención a que

- **#import** *typelib.tlb* hace que el compilador de C++ genere 2 archivos: *typelib.tlh* y *typelib.tli*. Por defecto, estos archivos se generan solo una vez, por lo que necesitas recompilar completamente el proyecto para obtener nuevas versiones de ellos.
- a menudo, importar solo un archivo TLB conduce a un gran número de errores de compilación. Hay dos tipos de errores: dependencias no resueltas y nombres en conflicto. Si no puedes compilar el proyecto, abre el archivo tlh y mira las primeras líneas que están comentadas. Aquí probablemente verás la sección que comienza desde la línea

```cpp
// Cross-referenced type libraries:
```

y tiene uno o más **#import**. Simplemente cópialos en tu código antes de importar la biblioteca de tipos principal y hazlo en el ***mismo*** orden. Así evitarás el primer tipo de problema. El siguiente tipo de problema proviene del hecho de que el entorno de C++ tiene un gran número de macros, funciones predefinidas, etc., que pueden entrar en conflicto con los métodos de la biblioteca de tipos. Por ejemplo, GetType ya se ha utilizado ampliamente en C++, pero Aspose.PDF también lo tiene. Encontré que los atributos **rename** y **auto_rename** de la directiva **#import** son muy convenientes para deshacerse de posibles advertencias y errores.

- a veces, las clases en los espacios de nombres **uses** entran en conflicto con los nombres en la biblioteca de tipos, por lo que en tales casos, se debe usar el nombre completo de la clase en lugar de **using namespace**. Por ejemplo, observa cómo se llama StringToBSTR en el fragmento de código a continuación.
{{% /alert %}}

Para más detalles, consulta [este](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) artículo.

Ejemplo en C++

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