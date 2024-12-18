---
title: Menggunakan wrapper di CPP
type: docs
weight: 30
url: /id/net/using-wrapper-in-cpp/
---

## Prasyarat

{{% alert color="primary" %}}

Silakan daftarkan Aspose.PDF untuk .NET dengan COM Interop, silakan periksa artikel dengan nama [Gunakan Aspose.pdf untuk .NET via COM Interop](/pdf/id/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Implementasi

{{% alert color="primary" %}}

Kami akan menggunakan [wrapper](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/) untuk mengambil teks dari dokumen PDF.

{{% /alert %}}

```cpp

#include "stdafx.h"
#import "C:\\Temp\\PdfText.tlb"
using namespace System;

String^ wrapper(String^ file)
{
    String^ text;
    // create ComHelper

    PdfText::IPetrieverPtr retrieverPtr;
    HRESULT hr = retrieverPtr.CreateInstance(__uuidof(PdfText::Petriever));

    if (FAILED(hr))
    {
        Console::WriteLine(L"Error occured");
    }
    else
    {
        // set license
        retrieverPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        // retrieve text

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
        Console::WriteLine("Missing parameters\nUsage:testCOM <pdf file>");
        return 0;
    }

    String ^text = wrapper(args[0]);
    CoUninitialize();
    Console::WriteLine("Extracted text:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<empty>");
    Console::WriteLine("---");
    return 0;
}

```


