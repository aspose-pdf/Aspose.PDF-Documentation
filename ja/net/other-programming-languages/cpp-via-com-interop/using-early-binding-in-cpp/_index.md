---
title: CPPでの早期バインディングの使用
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/using-early-binding-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using early binding in CPP",
    "alternativeHeadline": "Effortless PDF Text Extraction with C Early Binding",
    "abstract": "COM Interopを使用してPDFファイルからのテキスト抽出を簡素化するAspose.PDF for .NETの早期バインディングの力を発見してください。この機能は、コンパイルエラーを最小限に抑え、コーディング効率を向上させる合理化されたアプローチを提供します。信頼性の高いPDF処理でCプロジェクトを改善するために早期バインディングの機能を活用してください。",
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
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 前提条件

{{% alert color="primary" %}}

COM Interopを使用してAspose.PDF for .NETに登録してください。詳細は、[COM Interop経由でAspose.pdf for .NETを使用する](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)という記事を確認してください。

{{% /alert %}}

## サンプル

{{% alert color="primary" %}}

これは、早期バインディングを使用してCOM Interop経由でPDFファイルからテキストを抽出するためのシンプルなC++コードサンプルです。サンプルを実行する前に、以下に注意してください。

- **#import** *typelib.tlb*は、C++コンパイラに2つのファイルを生成させます: *typelib.tlh*と*typelib.tli*。デフォルトでは、これらのファイルは一度だけ生成されるため、新しいバージョンを取得するにはプロジェクトを完全に再コンパイルする必要があります。
- TLBファイルを1つだけインポートすることが多くのコンパイラエラーを引き起こすことがあります。エラーには、未解決の依存関係と名前の衝突の2種類があります。プロジェクトをコンパイルできない場合は、tlhファイルを開いて、コメントアウトされた最初の行を確認してください。ここには、次の行から始まるセクションが表示されるでしょう。

```cpp
// Cross-referenced type libraries:
```

そして1つ以上の**#import**があります。それらをメインのタイプライブラリをインポートする前にコードにコピーし、***同じ***順序で行ってください。これにより、最初のタイプの問題を回避できます。次のタイプの問題は、C++環境に多くのマクロや事前定義された関数などがあり、これがタイプライブラリのメソッドと衝突することから生じます。例えば、GetTypeはC++で広く使用されていますが、Aspose.PDFにもあります。**#import**ディレクティブの**rename**および**auto_rename**属性は、可能な警告やエラーを取り除くのに非常に便利です。

- 時々、**uses**名前空間内のクラスがタイプライブラリ内の名前と衝突することがあるため、そのような場合は**using namespace**の代わりに完全なクラス名を使用する必要があります。例えば、以下のコードスニペットでStringToBSTRがどのように呼ばれているかを見てください。
{{% /alert %}}

詳細については、[こちら](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558)の投稿を参照してください。

C++の例

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