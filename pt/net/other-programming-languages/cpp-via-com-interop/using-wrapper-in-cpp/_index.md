---
title: Usando wrapper em CPP
type: docs
weight: 30
url: pt/net/using-wrapper-in-cpp/
---

## Pré-requisitos

{{% alert color="primary" %}}

Por favor, registre o Aspose.PDF para .NET com COM Interop, verifique o artigo chamado [Use Aspose.pdf para .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Implementação

{{% alert color="primary" %}}

Usaremos um [wrapper](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/) para recuperar texto de documentos PDF.

{{% /alert %}}

```cpp

#include "stdafx.h"
#import "C:\\Temp\\PdfText.tlb"
using namespace System;

String^ wrapper(String^ file)
{
    String^ text;
    // criar ComHelper

    PdfText::IPetrieverPtr retrieverPtr;
    HRESULT hr = retrieverPtr.CreateInstance(__uuidof(PdfText::Petriever));

    if (FAILED(hr))
    {
        Console::WriteLine(L"Erro ocorrido");
    }
    else
    {
        // definir licença
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
        Console::WriteLine("Parâmetros ausentes\nUso: testCOM <arquivo pdf>");
        return 0;
    }

    String ^text = wrapper(args[0]);
    CoUninitialize();
    Console::WriteLine("Texto extraído:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<vazio>");
    Console::WriteLine("---");
    return 0;
}

```

