---
title: PDF文書をプログラムで作成
linktitle: PDFを作成
type: docs
weight: 10
url: /ja/net/create-document/
description: このページでは、Aspose.PDFライブラリを使用して最初からPDF文書を作成する方法について説明します。
---

Aspose.PDF for .NET APIを使用すると、C#およびVB.NETを使用してPDFファイルを作成および読み取ることができます。このAPIはWinForms、ASP.NETなど、さまざまな.NETアプリケーションで使用できます。この記事では、Aspose.PDF for .NET APIを使用して、.NETアプリケーションでPDFファイルを簡単に生成および読み取る方法を示します。

## C#を使用してPDFファイルを作成する方法

C#を使用してPDFファイルを作成するには、次の手順を使用します。

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスのオブジェクトを作成します
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) オブジェクトの [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) コレクションに [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) オブジェクトを追加します
1.
1. 結果のPDFドキュメントを保存します。

次のコードスニペットは、新しいグラフィカルな[Aspose.Drawing](/pdf/ja/net/drawing/)インターフェースでも機能します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// ドキュメントオブジェクトを初期化
Document document = new Document();
// ページを追加
Page page = document.Pages.Add();
// 新しいページにテキストを追加
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// 更新されたPDFを保存
document.Save(dataDir + "HelloWorld_out.pdf")
```

この場合、私たちはA4ページサイズ、縦向きのPDF一ページドキュメントを作成します。私たちのページは、ページの左上部に「Hello, World」を含むことになります。
