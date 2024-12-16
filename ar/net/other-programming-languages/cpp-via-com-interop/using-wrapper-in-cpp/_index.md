---
title: استخدام الغلاف في CPP
type: docs
weight: 30
url: /ar/net/using-wrapper-in-cpp/
---

## المتطلبات الأساسية

{{% alert color="primary" %}}

يرجى تسجيل Aspose.PDF لـ .NET مع COM Interop، يرجى التحقق من المقالة المسماة [استخدام Aspose.pdf لـ .NET عبر COM Interop](/pdf/ar/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## التنفيذ

{{% alert color="primary" %}}

سنستخدم [غلاف](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/) لاسترجاع النص من مستندات PDF.

{{% /alert %}}

```cpp

#include "stdafx.h"
#import "C:\\Temp\\PdfText.tlb"
using namespace System;

String^ wrapper(String^ file)
{
    String^ text;
    // إنشاء ComHelper

    PdfText::IPetrieverPtr retrieverPtr;
    HRESULT hr = retrieverPtr.CreateInstance(__uuidof(PdfText::Petriever));

    if (FAILED(hr))
    {
        Console::WriteLine(L"حدث خطأ");
    }
    else
    {
        // تعيين الترخيص
        retrieverPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        // استرجاع النص

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
        Console::WriteLine("معلمات مفقودة\nاستخدام:testCOM <ملف pdf>");
        return 0;
    }

    String ^text = wrapper(args[0]);
    CoUninitialize();
    Console::WriteLine("النص المستخرج:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<فارغ>");
    Console::WriteLine("---");
    return 0;
}

```

