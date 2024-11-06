---
title: Использование раннего связывания в CPP
type: docs
weight: 10
url: ru/net/using-early-binding-in-cpp/
---

## Предварительные требования

{{% alert color="primary" %}}

Пожалуйста, зарегистрируйте Aspose.PDF для .NET с COM Interop, обратитесь к статье под названием [Использование Aspose.pdf для .NET через COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Пример

{{% alert color="primary" %}}

Это простой пример кода на C++ для извлечения текста из PDF файлов с использованием COM Interop с ранним связыванием. Перед запуском примера обратите внимание на то, что

- **#import** *typelib.tlb* заставляет компилятор C++ генерировать 2 файла: *typelib.tlh* и *typelib.tli*. По умолчанию эти файлы генерируются только один раз, поэтому вам нужно полностью перекомпилировать проект, чтобы получить новые версии этих файлов.
- часто импорт только одного файла TLB приводит к большому количеству ошибок компилятора.
- Часто импортирование только одного файла TLB приводит к большому количеству ошибок компилятора.

```cpp
// Взаимосвязанные библиотеки типов:
```

и содержит один или более **#import**'s. Просто скопируйте их в свой код перед импортом основной библиотеки типов и делайте это в ***том же*** порядке. Таким образом, вы справитесь с первым типом проблемы. Следующий тип проблемы возникает из-за того, что в среде C++ есть большое количество макросов, предопределенных функций и т.д., которые могут конфликтовать с методами библиотеки типов. Например, GetType уже широко используется в C++, но также и Aspose.PDF имеет его. Я нашел, что атрибуты **rename** и **auto_rename** директивы **#import** очень удобны для устранения возможных предупреждений и ошибок.

- иногда классы в пространствах имен **uses** конфликтуют с именами в библиотеке типов, поэтому в таких случаях следует использовать полное имя класса вместо **using namespace**. Например, смотрите, как вызывается StringToBSTR в приведенном ниже фрагменте кода.
{{% /alert %}}

Для подробностей пожалуйста посмотрите [этот](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) пост.
Для деталей, пожалуйста, ознакомьтесь с [этим](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) постом.

Пример на C++

```cpp
#include "stdafx.h"
#import "C:\Windows\Microsoft.NET\Framework\v2.0.50727\System.Drawing.tlb"
#import "C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscorlib.tlb" auto_rename

#import "C:\Temp\Aspose.PDF.tlb" rename("GetType", "GetType_") auto_rename

using namespace System;
String ^earlyBinding(String ^file)
{
    String ^text;
    // создать ComHelper

    Aspose_Pdf::_ComHelperPtr comHelperPtr;
    HRESULT hr = comHelperPtr.CreateInstance(__uuidof(Aspose_Pdf::ComHelper));
    if (FAILED(hr))
    {
        Console::WriteLine(L"Произошла ошибка");
    }
    else
    {
        // установить лицензию
        Aspose_Pdf::_LicensePtr licPtr;
        licPtr.CreateInstance(__uuidof(Aspose_Pdf::License));
        licPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        licPtr.Release();

        // получить Документ
        Aspose_Pdf::_DocumentPtr docPtr;
        docPtr = comHelperPtr->OpenFile((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());

        comHelperPtr.Release();

        // создать Absorber
        Aspose_Pdf::_TextAbsorberPtr absorberPtr;
        HRESULT hRes = absorberPtr.CreateInstance(__uuidof(Aspose_Pdf::TextAbsorber));

        // просмотреть текст
        docPtr->GetPages()->Accept_4(absorberPtr);

        // извлечь текст
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
        Console::WriteLine("Отсутствуют параметры\nИспользование:testCOM <pdf файл>");
        return 0;
    }

    String ^text = earlyBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("Извлеченный текст:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<пусто>");
    Console::WriteLine("---");
    return 0;
}
```

