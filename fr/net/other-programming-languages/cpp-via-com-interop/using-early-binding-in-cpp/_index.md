---
title: Utilisation de la liaison anticipée en CPP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/using-early-binding-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using early binding in CPP",
    "alternativeHeadline": "Effortless PDF Text Extraction with C Early Binding",
    "abstract": "Découvrez la puissance de la liaison anticipée en C avec Aspose.PDF for .NET. Cette fonctionnalité simplifie l'extraction de texte à partir de fichiers PDF en utilisant COM Interop, offrant une approche rationalisée qui minimise les erreurs de compilation et améliore l'efficacité du codage. Profitez des capacités de la liaison anticipée pour améliorer vos projets C avec une gestion fiable des PDF.",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Prérequis

{{% alert color="primary" %}}

Veuillez enregistrer Aspose.PDF for .NET avec COM Interop, veuillez consulter l'article intitulé [Utiliser Aspose.pdf pour .NET via COM Interop](/pdf/fr/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Exemple

{{% alert color="primary" %}}

Ceci est un exemple simple de code C++ pour extraire du texte à partir de fichiers PDF en utilisant COM Interop avec liaison anticipée. Avant d'exécuter l'exemple, faites attention à ce qui suit :

- **#import** *typelib.tlb* fait que le compilateur C++ génère 2 fichiers : *typelib.tlh* et *typelib.tli*. Par défaut, ces fichiers ne sont générés qu'une seule fois, donc vous devez recompiler complètement le projet pour obtenir de nouvelles versions.
- souvent, l'importation d'un seul fichier TLB entraîne un grand nombre d'erreurs de compilation. Il existe deux types d'erreurs : dépendances non résolues et noms conflictuels. Si vous ne pouvez pas compiler le projet, ouvrez le fichier tlh et regardez les premières lignes qui sont commentées. Vous verrez probablement la section qui commence par la ligne

```cpp
// Cross-referenced type libraries:
```

et contient un ou plusieurs **#import**. Il suffit de les copier dans votre code avant d'importer la bibliothèque de types principale et de le faire dans le ***même*** ordre. Ainsi, vous éviterez le premier type de problème. Le deuxième type de problème provient du fait que l'environnement C++ a un grand nombre de macros, de fonctions prédéfinies, etc., qui peuvent entrer en conflit avec les méthodes de la bibliothèque de types. Par exemple, GetType a déjà été largement utilisé en C++, mais Aspose.PDF l'a également. J'ai trouvé que les attributs **rename** et **auto_rename** de la directive **#import** sont très pratiques pour se débarrasser des avertissements et des erreurs possibles.

- parfois, les classes dans les espaces de noms **uses** entrent en conflit avec les noms dans la bibliothèque de types, donc dans de tels cas, le nom complet de la classe doit être utilisé au lieu de **using namespace**. Par exemple, voyez comment StringToBSTR est appelé dans l'extrait de code ci-dessous.
{{% /alert %}}

Pour plus de détails, veuillez consulter [ceci](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558).

Exemple C++

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