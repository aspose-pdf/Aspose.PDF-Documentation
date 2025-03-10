---
title: Aspose.PDF for .NET の COM Interop経由
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/use-aspose-pdf-for-net-via-com-interop/
description: COM Interopを介してAspose.PDF for .NETを使用して、非.NETアプリケーションとのシームレスな統合を実現する方法を発見してください。
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF for .NET via COM Interop",
    "alternativeHeadline": "Aspose.PDF for .NET Enables COM Interop Usage",
    "abstract": "Aspose.PDF for .NETは、COM Interopを介してさまざまなプログラミング言語とのシームレスな統合をサポートし、開発者が.NETフレームワークの外でその強力なPDF操作機能を利用できるようにします。この機能は、Aspose.PDFオブジェクトをCOMオブジェクトに変換することで柔軟性を高め、アンマネージドコードとのインタラクションを簡素化し、早期および遅延バインディング技術を通じて高いパフォーマンスを維持します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1338",
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
    "url": "/net/use-aspose-pdf-for-net-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/use-aspose-pdf-for-net-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

このトピックの情報は、次のプログラミング言語のいずれかでCOM Interopを介して[Aspose.PDF for .NET](/pdf/net/)を使用したいシナリオに適用されます：

- ASP
- Delphi
- JScript
- Perl
- PHP
- PowerBuilder
- Python
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## COM Interopを使用する

Aspose.PDF for .NETは.NETフレームワークの制御下で実行され、これをマネージドコードと呼びます。上記のすべての言語で書かれたコードは.NETフレームワークの外で実行され、これをアンマネージドコードと呼びます。アンマネージドコードとAspose.PDFの間の相互作用は、COM Interopと呼ばれる.NETの機能を介して行われます。

Aspose.PDFオブジェクトは.NETオブジェクトですが、COM Interopを介して使用されると、プログラミング言語内でCOMオブジェクトとして表示されます。したがって、[Aspose.PDF for .NET](/pdf/net/)を使用し始める前に、プログラミング言語でCOMオブジェクトを作成および使用する方法を知っておくことが最善です。

{{% alert color="primary" %}}

- COMの世界では、COMサーバーとCOMクライアントを区別します。COMサーバーはCOMクラスを保存し、COMクライアントはCOMサーバーにクラスインスタンス、つまりCOMオブジェクトを要求します。
- COMクライアント、または単にクライアントアプリケーションは、COMクラスの内容について何かを知っているか、またはそのメソッドやプロパティについて全く知らない場合があります。したがって、クライアントアプリケーションは、コンパイル/ビルド時または実行時にのみCOMクラスの構造を発見できます。「発見」のプロセスはバインディングとして知られ、**早期バインディング**と**遅延バインディング**があります。
- 簡単に言えば、COMクラスはブラックボックスのようなもので、それを操作するにはタイプライブラリが必要です。このバイナリファイルにはCOMクラスのメソッド、プロパティの説明が含まれており、COMオブジェクトを操作することをサポートする高水準言語は、タイプライブラリを追加するための構文表現を持つことがよくあります。たとえば、C++では[**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx)です。
- タイプライブラリは早期バインディングに使用されます。
- COMオブジェクトは、**ディスパッチインターフェース**（dispinterface）とその**vtable**（仮想関数テーブル）の2つの方法でメソッドとプロパティを公開できます。
- **dispinterface**内では、各メソッドとプロパティは一意のメンバーによって識別されます。このメンバーは関数のディスパッチ識別子（または**DispID**）です。
- **vtable**は、COMクラスインターフェースがサポートする関数へのポインタのセットです。
- 両方のインターフェースを介してメソッドを公開するオブジェクトは、**デュアルインターフェース**をサポートします。
- 両方のバインディングタイプには利点があります。早期バインディングは、パフォーマンスの向上とコンパイル時の構文チェックを提供します。遅延バインディングは、COMクラスの将来のバージョンと***互換性を持たせる***ことを意図してクライアントを作成する場合に最も有利です。遅延バインディングでは、タイプライブラリからの情報がクライアントに「ハードワイヤード」されていないため、クライアントがコード変更なしでCOMクラスの将来のバージョンで動作できるという自信が高まります。
- 遅延バインディングメカニズムには大きな利点があります。COM DLLの作成者が異なる関数インターフェースレイアウトで新しいバージョンをリリースすることを決定した場合、そのメソッドを呼び出すコードは、メソッドがもはや利用できない場合を除いてクラッシュしません。たとえ**vtable**が異なっていても、遅延バインディングは新しいDISPIDsを発見し、適切なメソッドを呼び出すことができます。
{{% /alert %}}

習得する必要があるトピックは次のとおりです：
{{% alert color="primary" %}}

- プログラミング言語でのCOMオブジェクトの使用。プログラミング言語のドキュメントと、このドキュメントの後半にある言語固有のトピックを参照してください。

- .NET COM Interopによって公開されたCOMオブジェクトの操作。MSDNの[アンマネージドコードとの相互運用](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx)および[COMへの.NETフレームワークコンポーネントの公開](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx)を参照してください。

- Aspose.PDFドキュメントオブジェクトモデル。MSDNの[Aspose.PDFプログラマーズガイド](http://www.aspose.com/docs/display/pdfnet/Programmers+Guide)および[APIリファレンス](http://www.aspose.com/docs/display/pdfnet/Aspose.PDF+for+.NET+API+Reference)を参照してください。

{{% /alert %}}

## COM InteropでAspose.PDF for .NETを登録する

Aspose.PDF for .NETをインストールし、COM Interopに登録されていることを確認する必要があります（アンマネージドコードから呼び出せるようにするため）。

{{% alert color="primary" %}}

COM Interop用にAspose.PDF for .NETを手動で登録するには：

1. **スタート**メニューから、**すべてのプログラム**を選択し、次に**Microsoft Visual Studio**、**Visual Studio Tools**、最後に**Visual Studioコマンドプロンプト**を選択します。
1. アセンブリを登録するためのコマンドを入力します：
   1. .NET Framework 4.8.1
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /codebase
   1. .NET 6.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /codebase
   1. .NET 7.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /codebase
   1. .NET 8.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /codebase
   1. .NET Standard 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

/codebaseは、Aspose.PDF.dllがGACにない場合にのみ必要です。このオプションを使用すると、regasmはアセンブリのパスをレジストリに追加します。

{{% alert color="primary" %}}

regasm.exeは.NET Framework SDKに含まれているツールです。すべての.NET Framework SDKツールは、*\Microsoft .NET\Framevork\<FrameworkVersion>*ディレクトリにあります。たとえば、*C:\Windows\Microsoft .NET\Framework\v4.0.30319*です。Visual Studio .NETを使用している場合：
**スタート**メニューから、**プログラム**を選択し、次に**Visual Studio 2022**、最後に**VS 2022用の開発者コマンドプロンプト**を選択します。
必要な環境変数が設定されたコマンドプロンプトが実行されます。

{{% /alert %}}

### ProgIDs

ProgIDは「プログラム識別子」の略です。オブジェクトを作成するために使用されるCOMクラスの名前です。ProgIDはライブラリ名「Aspose.PDF」とクラス名で構成されています。

### タイプライブラリ

{{% alert color="primary" %}}

プログラミング言語（たとえばVisual BasicやDelphi）がCOMタイプライブラリを参照することを許可する場合、Aspose.PDF.tlbへの参照を追加し、オブジェクトブラウザでAspose.PDF for .NETのすべてのクラス、メソッド、プロパティ、および列挙を表示します。

TLBファイルを生成するには：

- .NET Framework 4.8.1
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.tlb" /codebase
- .NET 6.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.tlb" /codebase
- .NET 7.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.tlb" /codebase
- .NET 8.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.tlb" /codebase
- .NET Standard 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## COMオブジェクトの作成

COMオブジェクトの作成は、通常の.NETオブジェクトの作成に似ています：

```vb
'Instantiate Pdf instance by calling its empty constructor
Dim document
Set document = CreateObject("Aspose.Pdf.Document")

```

作成後、COMオブジェクトのようにオブジェクトのメソッドとプロパティにアクセスできます：

```vb
'Add page to the document
document.Pages.Add()
```

一部のメソッドにはオーバーロードがあり、最初のメソッドを除いて、数値のサフィックスが追加されてCOM Interopによって公開されます。たとえば、Document.SaveメソッドのオーバーロードはDocument.Save、Document.Save_2などになります。

詳細については、このドキュメントの後半にある言語固有の記事を参照してください。

## ラッパーアセンブリの作成

Aspose.PDF for .NETのクラス、メソッド、プロパティを多く使用する必要がある場合は、ラッパーアセンブリを作成することを検討してください（C#または他の.NETプログラミング言語を使用）。ラッパーアセンブリは、アンマネージドコードからAspose.PDF for .NETを直接使用するのを避けるのに役立ちます。

良いアプローチは、Aspose.PDF for .NETを参照する.NETアセンブリを開発し、それとのすべての作業を行い、アンマネージドコードに対して最小限のクラスとメソッドのセットのみを公開することです。アプリケーションは、その後、ラッパーライブラリのみで動作する必要があります。

COM Interopを介して呼び出す必要があるクラスとメソッドの数を減らすことで、プロジェクトが簡素化されます。COM Interopを介して.NETクラスを使用するには、しばしば高度なスキルが必要です。