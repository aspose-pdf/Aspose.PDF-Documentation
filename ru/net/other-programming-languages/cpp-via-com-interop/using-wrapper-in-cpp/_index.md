---
title: Использование оболочки в CPP
type: docs
weight: 30
url: ru/net/using-wrapper-in-cpp/
---

## Предварительные требования

{{% alert color="primary" %}}

Пожалуйста, зарегистрируйте Aspose.PDF для .NET с COM Interop, обратите внимание на статью под названием [Использование Aspose.pdf для .NET через COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Реализация

{{% alert color="primary" %}}

Мы будем использовать [оболочку](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/) для извлечения текста из PDF документов.

{{% /alert %}}

```cpp

#include "stdafx.h"
#import "C:\\Temp\\PdfText.tlb"
using namespace System;

String^ wrapper(String^ file)
{
    String^ text;
    // создать ComHelper

    PdfText::IPetrieverPtr retrieverPtr;
    HRESULT hr = retrieverPtr.CreateInstance(__uuidof(PdfText::Petriever));

    if (FAILED(hr))
    {
        Console::WriteLine(L"Произошла ошибка");
    }
    else
    {
        // установить лицензию
        retrieverPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        // извлечь текст

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
        Console::WriteLine("Отсутствуют параметры\nИспользование:testCOM <pdf file>");
        return 0;
    }

    String ^text = wrapper(args[0]);
    CoUninitialize();
    Console::WriteLine("Извлеченный текст:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<пусто>");
    Console::WriteLine("---");
    return 0;
}

```

