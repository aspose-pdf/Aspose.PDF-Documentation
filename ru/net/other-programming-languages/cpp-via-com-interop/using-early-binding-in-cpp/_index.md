---
title: Использование раннего связывания в CPP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/using-early-binding-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using early binding in CPP",
    "alternativeHeadline": "Effortless PDF Text Extraction with C Early Binding",
    "abstract": "Откройте для себя возможности раннего связывания в C с Aspose.PDF for .NET. Эта функция упрощает извлечение текста из PDF-файлов с использованием COM Interop, предоставляя упрощенный подход, который минимизирует ошибки компиляции и повышает эффективность кодирования. Используйте возможности раннего связывания, чтобы улучшить свои проекты на C с надежной обработкой PDF",
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
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Предварительные требования

{{% alert color="primary" %}}

Пожалуйста, зарегистрируйте Aspose.PDF for .NET с COM Interop, внимательно ознакомьтесь со статьей под названием [Используйте Aspose.pdf для .NET через COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Пример

{{% alert color="primary" %}}

Это простой пример кода на C++, чтобы извлечь текст из PDF-файлов с использованием COM Interop и раннего связывания. Перед запуском примера обратите внимание на то, что

- **#import** *typelib.tlb* заставляет компилятор C++ генерировать 2 файла: *typelib.tlh* и *typelib.tli*. По умолчанию эти файлы генерируются только один раз, поэтому вам нужно полностью перекомпилировать проект, чтобы получить новые версии этих файлов.
- часто импорт только одного TLB файла приводит к большому количеству ошибок компиляции. Существует два типа ошибок: неразрешенные зависимости и конфликтующие имена. Если вы не можете скомпилировать проект, откройте файл tlh и посмотрите на первые строки, которые закомментированы. Здесь вы, вероятно, увидите раздел, который начинается с строки

```cpp
// Cross-referenced type libraries:
```

и имеет одно или несколько **#import**. Просто скопируйте их в свой код перед импортом основной библиотеки типов и сделайте это в ***том же*** порядке. Таким образом, вы устраните первую проблему. Следующая проблема возникает из-за того, что среда C++ имеет большое количество макросов, предопределенных функций и т.д., которые могут конфликтовать с методами библиотеки типов. Например, GetType уже широко используется в C++, но также и в Aspose.PDF. Я нашел атрибуты **rename** и **auto_rename** директивы **#import** очень удобными для устранения возможных предупреждений и ошибок.

- иногда классы в **uses** пространствах имен конфликтуют с именами в библиотеке типов, поэтому в таких случаях необходимо использовать полное имя класса вместо **using namespace**. Например, смотрите, как StringToBSTR вызывается в приведенном ниже фрагменте кода.
{{% /alert %}}

Для получения подробной информации, пожалуйста, посмотрите [это](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) сообщение.

Пример C++

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