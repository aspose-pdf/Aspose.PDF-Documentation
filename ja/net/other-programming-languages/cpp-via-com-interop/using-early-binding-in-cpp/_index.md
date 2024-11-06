---
title: CPPでのアーリーバインディングの使用
type: docs
weight: 10
url: ja/net/using-early-binding-in-cpp/
---

## 前提条件

{{% alert color="primary" %}}

Aspose.PDF for .NETをCOM Interopで登録してください。[Use Aspose.pdf for .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)という記事を参照してください。

{{% /alert %}}

## サンプル

{{% alert color="primary" %}}

これは、COM Interopを使用してアーリーバインディングでPDFファイルからテキストを抽出するためのシンプルなC++コードサンプルです。サンプルを実行する前に以下の点に注意してください。

- **#import** *typelib.tlb* は、C++コンパイラに*typelib.tlh* と *typelib.tli* の2つのファイルを生成させます。デフォルトでは、これらのファイルは一度だけ生成されるため、新しいバージョンを取得するにはプロジェクトを完全に再コンパイルする必要があります。
- しばしば一つのTLBファイルのみをインポートすると、多くのコンパイラエラーが発生します。
{{% /alert %}}
- 一つのTLBファイルのインポートだけで多数のコンパイラエラーが発生することがよくあります。

```cpp
// 相互参照されたタイプライブラリ：
```

そして、一つ以上の**#import**があります。メインタイプライブラリをインポートする前にこれらをコードにコピーし、***同じ***順序で行ってください。これにより、最初のタイプの問題を解決できます。次の問題は、C++ 環境には多くのマクロ、事前定義された関数などがあるため、タイプライブラリのメソッドと競合する可能性があるという事実から来ます。たとえば、GetTypeはC++で既に広く使用されていますが、Aspose.PDFにも存在します。**#import**ディレクティブの**rename**および**auto_rename**属性は、可能性のある警告やエラーを回避するのに非常に便利です。
{{% alert color="primary" %}}

- **uses**名前空間のクラスがタイプライブラリの名前と競合する場合があり、そのような場合は、**using namespace**の代わりにクラスの完全な名前を使用する必要があります。以下のコードスニペットでStringToBSTRがどのように呼び出されるかを見てください。
{{% /alert %}}

詳細については、[この](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558)投稿をご覧ください。
詳細については、[この](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558)投稿をご覧ください。

C++ の例

```cpp
#include "stdafx.h"
#import "C:\Windows\Microsoft.NET\Framework\v2.0.50727\System.Drawing.tlb"
#import "C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscorlib.tlb" auto_rename

#import "C:\Temp\Aspose.PDF.tlb" rename("GetType", "GetType_") auto_rename

using namespace System;
String ^earlyBinding(String ^file)
{
    String ^text;
    // ComHelper の作成

    Aspose_Pdf::_ComHelperPtr comHelperPtr;
    HRESULT hr = comHelperPtr.CreateInstance(__uuidof(Aspose_Pdf::ComHelper));
    if (FAILED(hr))
    {
        Console::WriteLine(L"エラーが発生しました");
    }
    else
    {
        // ライセンスの設定
        Aspose_Pdf::_LicensePtr licPtr;
        licPtr.CreateInstance(__uuidof(Aspose_Pdf::License));
        licPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        licPtr.Release();

        // ドキュメントの取得
        Aspose_Pdf::_DocumentPtr docPtr;
        docPtr = comHelperPtr->OpenFile((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());

        comHelperPtr.Release();

        // Absorber の作成
        Aspose_Pdf::_TextAbsorberPtr absorberPtr;
        HRESULT hRes = absorberPtr.CreateInstance(__uuidof(Aspose_Pdf::TextAbsorber));

        // テキストの閲覧
        docPtr->GetPages()->Accept_4(absorberPtr);

        // テキストの取得
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
        Console::WriteLine("パラメータが足りません\n使用方法:testCOM <pdf file>");
        return 0;
    }

    String ^text = earlyBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("抽出されたテキスト:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<empty>");
    Console::WriteLine("---");
    return 0;
}
```

