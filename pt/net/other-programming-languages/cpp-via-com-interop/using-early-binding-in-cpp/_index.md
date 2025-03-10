---
title: Usando vinculação antecipada em CPP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/using-early-binding-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using early binding in CPP",
    "alternativeHeadline": "Effortless PDF Text Extraction with C Early Binding",
    "abstract": "Descubra o poder da vinculação antecipada em C com Aspose.PDF for .NET. Este recurso simplifica a extração de texto de arquivos PDF usando COM Interop, proporcionando uma abordagem simplificada que minimiza erros de compilação e melhora a eficiência da codificação. Aproveite as capacidades da vinculação antecipada para melhorar seus projetos em C com manuseio confiável de PDF",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Pré-requisitos

{{% alert color="primary" %}}

Por favor, registre Aspose.PDF for .NET com COM Interop, verifique o artigo intitulado [Use Aspose.pdf para .NET via COM Interop](/pdf/pt/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Exemplo

{{% alert color="primary" %}}

Este é um exemplo simples de código C++ para extrair texto de arquivos PDF usando COM Interop com vinculação antecipada. Antes de executar o exemplo, preste atenção que

- **#import** *typelib.tlb* faz com que o compilador C++ gere 2 arquivos: *typelib.tlh* e *typelib.tli*. Por padrão, esses arquivos são gerados apenas uma vez, então você precisa recompilar completamente o projeto para obter novas versões deles.
- frequentemente, importar apenas um arquivo TLB leva a um grande número de erros de compilação. Existem dois tipos de erros: dependências não resolvidas e nomes conflitantes. Se você não conseguir compilar o projeto, abra o arquivo tlh e olhe para as primeiras linhas que estão comentadas. Aqui você provavelmente verá a seção que começa na linha

```cpp
// Cross-referenced type libraries:
```

e tem um ou mais **#import**'s. Basta copiá-los para o seu código antes de importar a biblioteca de tipos principal e faça isso na ***mesma*** ordem. Assim, você evitará o primeiro tipo de problema. O próximo tipo de problema vem do fato de que o ambiente C++ tem um grande número de macros, funções pré-definidas, etc., que podem entrar em conflito com os métodos da biblioteca de tipos. Por exemplo, GetType já foi amplamente utilizado em C++, mas também Aspose.PDF o possui. Eu encontrei os atributos **rename** e **auto_rename** da diretiva **#import** muito convenientes para se livrar de possíveis avisos e erros.

- às vezes, classes em **uses** namespaces entram em conflito com nomes na biblioteca de tipos, então, nesses casos, o nome completo da classe deve ser usado em vez de **using namespace**. Por exemplo, veja como StringToBSTR é chamado no trecho de código abaixo.
{{% /alert %}}

Para mais detalhes, consulte [este](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) post.

Exemplo em C++

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