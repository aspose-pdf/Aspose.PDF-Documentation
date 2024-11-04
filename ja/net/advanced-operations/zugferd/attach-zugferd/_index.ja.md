---
title: PDF/3-A 準拠PDFの作成とZUGFeRD請求書の添付
linktitle: PDFにZUGFeRDを添付
type: docs
weight: 10
url: /net/attach-zugferd/
description: Aspose.PDF for .NETでZUGFeRDを含むPDFドキュメントを生成する方法を学びます
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFにZUGFeRDを添付

このコードスニペットは[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

PDFにZUGFeRDを添付するための推奨ステップは以下の通りです：

* 入力および出力PDFファイルが位置するフォルダへのパス変数を定義します。
* パスから既存のPDFファイル（例："ZUGFeRD-test.pdf"）を読み込んでドキュメントオブジェクトを作成します。
* "factur-x.xml"という名前の別のファイルのパスと説明を提供して[FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/)オブジェクトを作成します。このファイルにはZUGFeRD標準に準拠したインボイスメタデータが含まれています。
* ファイル仕様オブジェクトにプロパティを追加します。説明、MIMEタイプ、AF関係などです。
* ファイル仕様オブジェクトに説明、MIMEタイプ、AF関係などのプロパティを追加します。
* ファイル仕様オブジェクトを文書の埋め込みファイルコレクションに追加します。ファイル名はZUGFeRD標準に従って指定する必要があります（例: "factur-x.xml"）。
* 文書をPDF/A-3U形式に変換します。これは、電子文書の長期保存を保証するPDFのサブセットです。PDF/A-3Uは、PDFドキュメントに任意の形式のファイルを埋め込むことを許可します。
* 変換された文書を新しいPDFファイルとして保存します（例: "ZUGFeRD-res.pdf"）。

```cs
var path = @"C:\Samples\ZUGFeRD\";

var document = new Aspose.Pdf.Document(Path.Combine(path,"ZUGFeRD-test.pdf"));
// 新しいファイルを添付ファイルとして追加するための設定
var description = "ZUGFeRD標準に準拠した請求書メタデータ";
var fileSpecification = new Aspose.Pdf.FileSpecification(Path.Combine(path, "factur-x.xml"), description)
{
    Description = "Zugferd",
    MIMEType = "text/xml",
    AFRelationship = Aspose.Pdf.AFRelationship.Alternative
};
// 添付ファイルを文書の添付ファイルコレクションに追加
document.EmbeddedFiles.Add(fileSpecification);
document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.PDF_A_3U, Aspose.Pdf.ConvertErrorAction.Delete);
document.Save(Path.Combine(path, "ZUGFeRD-res.pdf"));
```

convert メソッドは、ストリーム、PDF形式、変換エラーアクションをパラメータとして取ります。ストリームパラメータは、変換ログを保存するために使用できます。変換エラーアクションパラメータは、変換中にエラーが発生した場合の対処方法を指定します。この場合、「Delete」と設定されており、PDF/A-3U形式に準拠していない要素はドキュメントから削除されます。
```
