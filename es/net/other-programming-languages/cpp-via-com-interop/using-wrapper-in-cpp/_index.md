---
title: Usando wrapper en CPP
type: docs
weight: 30
url: /es/net/using-wrapper-in-cpp/
---

## Prerrequisitos

{{% alert color="primary" %}}

Por favor, regístrese en Aspose.PDF para .NET con COM Interop, consulte el artículo titulado [Usar Aspose.pdf para .NET vía COM Interop](/pdf/es/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Implementación

{{% alert color="primary" %}}

Usaremos un [wrapper](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/) para recuperar texto de documentos PDF.

{{% /alert %}}

```cpp

#include "stdafx.h"
#import "C:\\Temp\\PdfText.tlb"
using namespace System;

String^ wrapper(String^ file)
{
    String^ text;
    // crear ComHelper

    PdfText::IPetrieverPtr retrieverPtr;
    HRESULT hr = retrieverPtr.CreateInstance(__uuidof(PdfText::Petriever));

    if (FAILED(hr))
    {
        Console::WriteLine(L"Error ocurrido");
    }
    else
    {
        // establecer licencia
        retrieverPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        // recuperar texto

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
        Console::WriteLine("Faltan parámetros\nUso:testCOM <archivo pdf>");
        return 0;
    }

    String ^text = wrapper(args[0]);
    CoUninitialize();
    Console::WriteLine("Texto extraído:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<vacío>");
    Console::WriteLine("---");
    return 0;
}

```

