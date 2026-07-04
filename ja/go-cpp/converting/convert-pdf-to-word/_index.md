---
title: GoでPDFをWord文書に変換する
linktitle: PDFをWordに変換する
type: docs
weight: 10
url: /ja/go-cpp/convert-pdf-to-doc/
lastmod: "2026-07-04"
description: PDFをDOC（DOCX）に変換するためのGoコードの書き方を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go を使用した PDF から Word への変換ツール
Abstract: C++ 経由の Aspose.PDF for Go は、元のテキスト、画像、表、そして全体の文書構造を保持しながら、PDF ドキュメントを DOC 形式へシームレスに変換できるようにします。この機能により、開発者は静的な PDF をさらに編集や処理が可能な Word ファイルに変換できます。ライブラリは変換出力を制御するためのさまざまなカスタマイズオプションを提供し、高い忠実性と正確性を保証します。ドキュメントには、開発者がアプリケーションで PDF から DOC への変換を効率的に実装できるよう、詳細な手順とサンプルコードが含まれています。
SoftwareApplication: go-cpp
---

Microsoft Word や DOC および DOCX 形式をサポートするその他のワードプロセッサで PDF ファイルの内容を編集するためです。PDF ファイルは編集可能ですが、DOC と DOCX ファイルはより柔軟でカスタマイズ可能です。

## PDF を DOC に変換

提供された Go コード スニペットは、Aspose.PDF ライブラリを使用して PDF ドキュメントを DOC に変換する方法を示しています:

1. PDF ドキュメントを開く。
1. 使用して PDF ファイルを DOC に変換する [SaveDoc](https://reference.aspose.com/pdf/go-cpp/convert/savedoc/) 関数。
1. PDFドキュメントを閉じ、割り当てられたリソースを解放します。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // SaveDoc(filename string) saves previously opened PDF-document as Doc-document with filename
      err = pdf.SaveDoc("sample.doc")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF をオンラインで DOC に変換してみましょう**

Aspose.PDF for Go はオンラインの無料アプリケーションを提供します ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), そこで機能と品質を調査しようとすることができます。

[![PDF を DOC に変換](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## PDF を DOCX に変換

Aspose.PDF for Go API を使用すると、PDF ドキュメントを DOCX に読み取りおよび変換できます。DOCX は、構造がプレーンバイナリから XML とバイナリ ファイルの組み合わせに変更された、Microsoft Word ドキュメントのよく知られた形式です。Docx ファイルは Word 2007 およびそれ以降のバージョンで開くことができますが、DOC ファイル拡張子をサポートする以前の MS Word バージョンでは開けません。

提供された Go のコードスニペットは、Aspose.PDF ライブラリを使用して PDF ドキュメントを DOCX に変換する方法を示しています：

1. PDF ドキュメントを開く。
1. PDF ファイルを DOCX に変換するには [SaveDocX](https://reference.aspose.com/pdf/go-cpp/convert/savedocx/) 関数。
1. PDFドキュメントを閉じ、割り当てられたリソースを解放します。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // SaveDocX(filename string) saves previously opened PDF-document as DocX-document with filename
      err = pdf.SaveDocX("sample.docx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF をオンラインで DOCX に変換してみてください**

Aspose.PDF for Go はオンラインの無料アプリケーションを提供します ["PDF を Word に"](https://products.aspose.app/pdf/conversion/pdf-to-docx), そこで機能と品質を調査しようとすることができます。

[![Aspose.PDF 変換 PDF to Word 無料アプリ](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}