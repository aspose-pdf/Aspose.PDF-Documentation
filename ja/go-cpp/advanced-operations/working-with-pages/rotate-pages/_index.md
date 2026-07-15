---
title: GoでPDFページを回転する
linktitle: PDFページを回転する
type: docs
weight: 50
url: /ja/go-cpp/rotate-pages/
description: このトピックでは、Go を使用し C++ 経由で既存の PDF ファイルのページ向きをプログラムで回転させる方法について説明します。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for GoでPDFページを回転する
Abstract: Aspose.PDF for Go via C++ は、PDF ドキュメント内のページを回転させるための強力な機能を提供し、開発者が必要に応じてページの向きを変更できるようにします。このライブラリは、ページを 90、180、または 270 度回転させることをサポートしており、文書レイアウトの迅速かつ効率的な調整が可能です。この機能は、向きが間違っているページを修正したり、文書の提示方法を変更したりするのに役立ちます。ドキュメントには、開発者がページ回転機能をアプリケーションにシームレスに統合できるよう、ステップバイステップの手順とコードサンプルが含まれています。
SoftwareApplication: go-cpp
---

このセクションでは、Go を使用して既存の PDF ファイルのページ向きを横向きから縦向き、またはその逆に変更する方法について説明します。

ページを回転させることで、専門的な環境で PDF を印刷または表示する際に適切な位置合わせが保証されます

1. PDF ドキュメントを開きます。
1. PDF ページを回転させます。[PageRotate](https://reference.aspose.com/pdf/go-cpp/organize/rotate/) 関数は、指定されたページに特定の回転（この場合は 180 度）を適用します。
1. 変更を新しいファイルに保存します。[SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) 関数は、元のPDFファイルを保持しながら、更新されたバージョンを保存するために新しいPDFファイルを作成します。

この例では、PDFドキュメントの特定のページを回転させます。

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
    // PageRotate(num int32, rotation int32) rotates page
    err = pdf.PageRotate(1, asposepdf.RotationOn180)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_page1_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

ドキュメント内のすべての PDF ページを回転させるオプションもあります:

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
    // Rotate(rotation int32) rotates PDF-document
    err = pdf.Rotate(asposepdf.RotationOn270)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```