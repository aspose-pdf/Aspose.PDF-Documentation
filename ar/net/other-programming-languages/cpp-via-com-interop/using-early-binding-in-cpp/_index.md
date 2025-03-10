---
title: استخدام الربط المبكر في CPP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/using-early-binding-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using early binding in CPP",
    "alternativeHeadline": "Effortless PDF Text Extraction with C Early Binding",
    "abstract": "اكتشف قوة الربط المبكر في C مع Aspose.PDF for .NET. هذه الميزة تبسط استخراج النص من ملفات PDF باستخدام COM Interop، مما يوفر نهجًا مبسطًا يقلل من أخطاء التجميع ويعزز كفاءة البرمجة. استغل قدرات الربط المبكر لتحسين مشاريع C الخاصة بك مع معالجة PDF موثوقة.",
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
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## المتطلبات الأساسية

{{% alert color="primary" %}}

يرجى تسجيل Aspose.PDF for .NET مع COM Interop، يرجى مراجعة المقالة المسماة [استخدام Aspose.pdf لـ .NET عبر COM Interop](/pdf/ar/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## عينة

{{% alert color="primary" %}}

هذه عينة بسيطة من كود C++ لاستخراج النص من ملفات PDF باستخدام COM Interop مع الربط المبكر. قبل تشغيل العينة، انتبه إلى أن

- **#import** *typelib.tlb* يجعل مترجم C++ ينشئ ملفين: *typelib.tlh* و *typelib.tli*. بشكل افتراضي، يتم إنشاء هذه الملفات مرة واحدة فقط، لذا تحتاج إلى إعادة تجميع المشروع بالكامل للحصول على إصدارات جديدة منها.
- غالبًا ما يؤدي استيراد ملف TLB واحد فقط إلى عدد كبير من أخطاء المترجم. هناك نوعان من الأخطاء: الاعتماديات غير المحلولة والأسماء المتضاربة. إذا لم تتمكن من تجميع المشروع، افتح ملف tlh وانظر إلى الأسطر الأولى التي تم التعليق عليها. هنا سترى على الأرجح القسم الذي يبدأ من السطر

```cpp
// Cross-referenced type libraries:
```

ويحتوي على واحد أو أكثر من **#import**. فقط انسخها إلى كودك قبل استيراد مكتبة الأنواع الرئيسية وقم بذلك بنفس الترتيب. وبالتالي ستتجنب النوع الأول من المشكلة. النوع التالي من المشكلة يأتي من حقيقة أن بيئة C++ تحتوي على عدد كبير من الماكرو، الدوال المعرفة مسبقًا، إلخ، والتي يمكن أن تتعارض مع طرق مكتبة الأنواع. على سبيل المثال، تم استخدام GetType على نطاق واسع في C++ ولكن أيضًا Aspose.PDF لديها ذلك. وجدت أن سمات **rename** و **auto_rename** في توجيه **#import** مريحة جدًا للتخلص من التحذيرات والأخطاء المحتملة.

- أحيانًا تتعارض الفئات في **uses** مع الأسماء في مكتبة الأنواع، لذا في مثل هذه الحالات، يجب استخدام الاسم الكامل للفئة بدلاً من **using namespace**. على سبيل المثال، انظر كيف يتم استدعاء StringToBSTR في مقتطف الكود أدناه.
{{% /alert %}}

للحصول على التفاصيل، يرجى الاطلاع على [هذا](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) المنشور.

مثال C++

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