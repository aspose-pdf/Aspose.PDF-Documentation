---
title: 在 CPP 中使用早期绑定
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/using-early-binding-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using early binding in CPP",
    "alternativeHeadline": "Effortless PDF Text Extraction with C Early Binding",
    "abstract": "发现 C 中早期绑定的强大功能。此功能通过 COM Interop 简化了从 PDF 文件中提取文本的过程，提供了一种简化的方法，最小化编译错误并提高编码效率。利用早期绑定的能力来改善您的 C 项目，可靠地处理 PDF。",
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
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 前提条件

{{% alert color="primary" %}}

请使用 COM Interop 注册 Aspose.PDF for .NET，请查看名为 [通过 COM Interop 使用 Aspose.pdf for .NET](/pdf/net/use-aspose-pdf-for-net-via-com-interop/) 的文章。

{{% /alert %}}

## 示例

{{% alert color="primary" %}}

这是一个简单的 C++ 代码示例，使用早期绑定通过 COM Interop 从 PDF 文件中提取文本。在运行示例之前，请注意

- **#import** *typelib.tlb* 会使 C++ 编译器生成 2 个文件：*typelib.tlh* 和 *typelib.tli*。默认情况下，这些文件只会生成一次，因此您需要完全重新编译项目以获取它们的新版本。
- 通常仅导入一个 TLB 文件会导致大量编译错误。错误有两种类型：未解决的依赖关系和名称冲突。如果您无法编译项目，请打开 tlh 文件并查看注释的前几行。在这里，您可能会看到从以下行开始的部分

```cpp
// Cross-referenced type libraries:
```

并且有一个或多个 **#import**。只需在导入主类型库之前将它们复制到您的代码中，并以 ***相同*** 的顺序进行操作。这样您就可以解决第一种类型的问题。第二种问题来自于 C++ 环境中有大量宏、预定义函数等，可能与类型库方法冲突。例如，GetType 已在 C++ 中广泛使用，但 Aspose.PDF 也有它。我发现 **#import** 指令的 **rename** 和 **auto_rename** 属性非常方便，可以消除可能的警告和错误。

- 有时 **uses** 命名空间中的类与类型库中的名称冲突，因此在这种情况下，必须使用完整的类名，而不是 **using namespace**。例如，请查看下面代码片段中如何调用 StringToBSTR。
{{% /alert %}}

有关详细信息，请查看 [这篇](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) 文章。

C++ 示例

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