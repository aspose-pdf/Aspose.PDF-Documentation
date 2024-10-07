---
title: PDFファイルへのブックマークの追加
type: docs
weight: 20
url: /net/how-to-create-nested-bookmarks/
description: このセクションでは、PdfContentEditorクラスを使ってネストされたブックマークを作成する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

ブックマークを使用すると、PDFドキュメント内の特定のページにリンクを付けて追跡することができます。[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) クラスは、[Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) にあり、既存のPDFファイル内で、指定したページまたはすべてのページに洗練されていながら直感的な方法で独自のブックマークを作成する機能を提供します。

## 実装の詳細

単純なブックマークの作成の他に、時には章の形でブックマークを作成する必要があります。その場合、個々のブックマークを章のブックマーク内にネストします。これにより、章の+記号をクリックすると、ブックマークが展開されるときに中のページが表示されます。以下の図に示すように。
```csharp
   public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.CreateBookmarksAction("ブックマーク 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

            // 結果のPDFをファイルに保存
            editor.Save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```