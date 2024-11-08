---
title: CPPでラッパーを使用する
type: docs
weight: 30
url: /ja/net/using-wrapper-in-cpp/
---

## 前提条件

{{% alert color="primary" %}}

Aspose.PDF for .NETをCOM Interopで登録してください。[Use Aspose.pdf for .NET via COM Interop](/pdf/ja/net/use-aspose-pdf-for-net-via-com-interop/)という記事を参照してください。

{{% /alert %}}

## 実装

{{% alert color="primary" %}}

PDFドキュメントからテキストを取得するために[ラッパー](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/)を使用します。

{{% /alert %}}

```cpp

#include "stdafx.h"
#import "C:\\Temp\\PdfText.tlb"
using namespace System;

String^ wrapper(String^ file)
{
    String^ text;
    // ComHelperの作成

    PdfText::IPetrieverPtr retrieverPtr;
    HRESULT hr = retrieverPtr.CreateInstance(__uuidof(PdfText::Petriever));

    if (FAILED(hr))
    {
        Console::WriteLine(L"エラーが発生しました");
    }
    else
    {
        // ライセンスの設定
        retrieverPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        // テキストの取得

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
        Console::WriteLine("パラメータが足りません\nUsage:testCOM <pdf file>");
        return 0;
    }

    String ^text = wrapper(args[0]);
    CoUninitialize();
    Console::WriteLine("抽出されたテキスト:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<empty>");
    Console::WriteLine("---");
    return 0;
}

```


