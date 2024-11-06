---
title: Aspose.PDF for .NET via COM Interop
type: docs
weight: 20
url: ja/net/use-aspose-pdf-for-net-via-com-interop/
---

{{% alert color="primary" %}}

このトピックの情報は、以下のプログラミング言語のいずれかで [Aspose.PDF for .NET](/pdf/net/) を COM Interop 経由で使用したい場合に適用されます：

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

## COM Interop を使用する

Aspose.PDF for .NET は .NET Framework の制御下で実行され、これを管理されたコードと呼びます。上記のすべての言語で書かれたコードは .NET Framework の外部で実行され、これを管理されていないコードと呼びます。管理されていないコードと Aspose.PDF の間の相互作用は、COM Interop と呼ばれる .NET の機能を介して行われます。

Aspose.PDF オブジェクトは .NET オブジェクトですが、COM Interop を介して使用される場合、プログラミング言語で COM オブジェクトとして表示されます。
Aspose.PDFオブジェクトは.NETオブジェクトですが、COM Interopを介して使用すると、プログラミング言語ではCOMオブジェクトとして表示されます。

{{% alert color="primary" %}}

- COMの世界では、COMサーバーとCOMクライアントを区別します。COMサーバーはCOMクラスを保存し、COMクライアントはCOMサーバーにクラスのインスタンス、つまりCOMオブジェクトを要求します。
- COMクライアント、または単にクライアントアプリケーションは、COMクラスの内容について何かを知っていることもありますし、そのメソッドやプロパティについて全く知らないこともあります。そのため、クライアントアプリケーションは、コンパイル/ビルド時または実行時のみにCOMクラスの構造を発見することができます。この「発見」のプロセスはバインディングとして知られており、**早期バインディング**と**遅延バインディング**があります。
- 簡単に言うと、COMクラスはブラックボックスのようなもので、それを操作するためにはタイプライブラリが必要です。このバイナリファイルには、COMクラスのメソッド、プロパティの説明が含まれており、COMオブジェクトをサポートする高レベル言語は通常、タイプライブラリを追加するための構文表現を持っています。例えば、これはC++の[**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx)です。
- COMクラスは、ブラックボックスのようなもので、操作するためにはタイプライブラリが必要です。このバイナリファイルには、COMクラスのメソッド、プロパティの説明が含まれており、COMオブジェクトをサポートする高レベル言語では、タイプライブラリを追加するための構文表現がよくあります。例えば、C++では[**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx)がそれに当たります。
- タイプライブラリは早期バインディングに使用されます。
- COMオブジェクトは、**ディスパッチインターフェース**（dispinterface）と**仮想関数テーブル**（vtable）の2つの方法でメソッドとプロパティを公開できます。
- **ディスパッチインターフェース**内では、各メソッドとプロパティがユニークなメンバーによって識別され、このメンバーは関数のディスパッチ識別子（または**DispID**）です。
- **vtable**は、COMクラスインターフェースがサポートする関数へのポインターのセットにすぎません。
- 両方のインターフェースを通じてメソッドを公開するオブジェクトは、**デュアルインターフェース**をサポートします。
- 両方のタイプのバインディングには利点があります。
- 両方のタイプのバインディングには利点があります。
- 遅延バインディングメカニズムには大きな利点があります：COM DLLの作成者が異なる関数インターフェースレイアウトで新しいバージョンをリリースすることを決定した場合、それらのメソッドを呼び出すコードはメソッドが利用不可能でない限りクラッシュしません。**vtable**が異なっていても、遅延バインディングは新しいDISPIDsを発見し、適切なメソッドを呼び出すことができます。
{{% /alert %}}

これからマスターする必要があるトピックはこちらです：
{{% alert color="primary" %}}

- あなたのプログラミング言語でCOMオブジェクトを使用する。あなたのプログラミング言語のドキュメントと、このドキュメント内の言語固有のトピックを参照してください。

- .NET COM Interopによって公開されるCOMオブジェクトの操作。MSDNの[非管理コードとの相互運用](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx)および[COMに.NET Frameworkコンポーネントを公開する](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx)を参照してください。

- Aspose.PDFドキュメントオブジェクトモデル。
- Aspose.PDF ドキュメントオブジェクトモデル。

{{% /alert %}}

## Aspose.PDF for .NET を COM Interop で登録

Aspose.PDF for .NET をインストールし、COM Interop で登録されていることを確認する必要があります（非管理コードから呼び出すことができるようにするため）。

{{% alert color="primary" %}}

Aspose.PDF for .NET を手動で COM Interop に登録するには：

1. **スタート** メニューから、**すべてのプログラム**、次に **Microsoft Visual Studio**、**Visual Studio Tools**、最後に **Visual Studio コマンドプロンプト** を選択します。
1. アセンブリを登録するコマンドを入力します：
   1. .NET Framework 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /codebase
   1. .NET Framework 3.5
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /codebase
   1. .NET Framework 4.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

/codebase は Aspose.PDF.dll が GAC にない場合のみ必要です。このオプションを使用すると、regasm はレジストリにアセンブリのパスを設定します。
{{% alert color="primary" %}}
regasm.exeは.NET Framework SDKに含まれるツールです。すべての.NET Framework SDKツールは*\Microsoft .NET\Framework\<FrameworkVersion>*ディレクトリにあります。例えば*C:\Windows\Microsoft .NET\Framework\v4.0.30319*です。Visual Studio .NETを使用する場合：
**スタート**メニューから**プログラム**を選択し、次に**Microsoft Visual Studio .NET**、**Visual Studio .NET Tools**、最後に**Visual Studio .NET 2003 コマンドプロンプト**を選択します。
これにより、必要な環境変数が設定されたコマンドプロンプトが実行されます。
{{% /alert %}}

### ProgIDs

ProgIDは「プログラム的識別子」を意味します。これはオブジェクトを作成するために使用されるCOMクラスの名前です。ProgIDにはライブラリ名"Aspose.PDF"とクラス名が含まれます。

### タイプライブラリ

{{% alert color="primary" %}}
プログラミング言語（例えばVisual BasicやDelphi）がCOMタイプライブラリを参照できる場合、Aspose.PDF.tlbへの参照を追加し、オブジェクトブラウザでAspose.PDF for .NETのクラス、メソッド、プロパティ、列挙をすべて確認してください。
{{% /alert %}}
あなたのプログラミング言語（例えばVisual BasicやDelphi）がCOMタイプライブラリを参照できる場合、Aspose.PDF.tlbへの参照を追加し、オブジェクトブラウザでAspose.PDF for .NETのすべてのクラス、メソッド、プロパティ、および列挙を確認します。

TLBファイルを生成するには：
{{% alert color="primary" %}}

- .NET Framework 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.tlb" /codebase
- .NET Framework 3.5
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.tlb" /codebase
- .NET Framework 4.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## COMオブジェクトの作成

COMオブジェクトの作成は、通常の.NETオブジェクトの作成に似ています：

```vb

'空のコンストラクタを呼び出してPdfインスタンスをインスタンス化する

Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

```
一度作成すると、COMオブジェクトのようにオブジェクトのメソッドやプロパティにアクセスできます：

```vb
'Pdfオブジェクトにセクションを追加
pdf.Sections.Add(pdfsection)
```

一部のメソッドにはオーバーロードがあり、COMインタロップによって数値のサフィックスが追加されて公開されますが、最初のメソッドは変更されません。たとえば、Pdf.SaveメソッドのオーバーロードはPdf.Save、Pdf.Save_2などになります。

詳細については、このドキュメントの言語別の記事を参照してください。

## ラッパーアセンブリの作成

Aspose.PDF for .NETの多くのクラス、メソッド、プロパティを使用する必要がある場合は、ラッパーアセンブリ（C#または他の.NETプログラミング言語を使用）を作成することを検討してください。ラッパーアセンブリは、管理されていないコードから直接 Aspose.PDF for .NET を使用するのを避けるのに役立ちます。

良いアプローチは、Aspose.PDF for .NETを参照してすべての作業を行い、管理されていないコードに最小限のクラスとメソッドのみを公開する.NETアセンブリを開発することです。
.NETアセンブリを開発し、Aspose.PDF for .NETを参照してすべての作業を行い、最小限のクラスとメソッドのみをアンマネージドコードに公開することが良いアプローチです。

COM Interopを介して呼び出す必要があるクラスとメソッドの数を減らすことで、プロジェクトが簡素化されます。.NETクラスをCOM Interopを通じて使用するには、高度なスキルがしばしば必要です。
