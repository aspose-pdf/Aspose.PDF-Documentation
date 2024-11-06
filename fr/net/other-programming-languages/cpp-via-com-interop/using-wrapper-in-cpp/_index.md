---
title: Utilisation d'un wrapper en CPP
type: docs
weight: 30
url: fr/net/using-wrapper-in-cpp/
---

## Prérequis

{{% alert color="primary" %}}

Veuillez enregistrer Aspose.PDF pour .NET avec COM Interop, veuillez consulter l'article intitulé [Utiliser Aspose.pdf pour .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Implémentation

{{% alert color="primary" %}}

Nous utiliserons un [wrapper](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/) pour récupérer le texte des documents PDF.

{{% /alert %}}

```cpp

#include "stdafx.h"
#import "C:\\Temp\\PdfText.tlb"
using namespace System;

String^ wrapper(String^ file)
{
    String^ text;
    // créer ComHelper

    PdfText::IPetrieverPtr retrieverPtr;
    HRESULT hr = retrieverPtr.CreateInstance(__uuidof(PdfText::Petriever));

    if (FAILED(hr))
    {
        Console::WriteLine(L"Une erreur est survenue");
    }
    else
    {
        // définir la licence
        retrieverPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        // récupérer le texte

        BSTR extractedText = retrieverPtr->GetText((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());
        text = gcnew String(extractedText);
        retrieverPtr.Release();
    }
    return text;
}

int main(array<System::String ^> ^args)
{
    CoInitialize(NULL);
    if (args->Length != 1)
    {
        Console::WriteLine("Paramètres manquants\nUsage:testCOM <fichier pdf>");
        return 0;
    }

    String ^text = wrapper(args[0]);
    CoUninitialize();
    Console::WriteLine("Texte extrait:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<vide>");
    Console::WriteLine("---");
    return 0;
}

```

