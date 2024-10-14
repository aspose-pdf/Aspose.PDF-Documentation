---
title: שימוש בעטיפה ב-CPP
type: docs
weight: 30
url: /net/using-wrapper-in-cpp/
---

## דרישות מוקדמות

{{% alert color="primary" %}}

נא לרשום את Aspose.PDF עבור .NET עם COM Interop, אנא בדוק את המאמר בשם [שימוש ב-Aspose.pdf עבור .NET דרך COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## יישום

{{% alert color="primary" %}}

נשתמש ב[עטיפה](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/) כדי לאחזר טקסט ממסמכי PDF.

{{% /alert %}}

```cpp

#include "stdafx.h"
#import "C:\\Temp\\PdfText.tlb"
using namespace System;

String^ wrapper(String^ file)
{
    String^ text;
    // יצירת ComHelper

    PdfText::IPetrieverPtr retrieverPtr;
    HRESULT hr = retrieverPtr.CreateInstance(__uuidof(PdfText::Petriever));

    if (FAILED(hr))
    {
        Console::WriteLine(L"אירעה שגיאה");
    }
    else
    {
        // הגדרת רישיון
        retrieverPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        // אחזור טקסט

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
        Console::WriteLine("חסרים פרמטרים\nשימוש:testCOM <קובץ pdf>");
        return 0;
    }

    String ^text = wrapper(args[0]);
    CoUninitialize();
    Console::WriteLine("טקסט שהופק:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<ריק>");
    Console::WriteLine("---");
    return 0;
}

```

