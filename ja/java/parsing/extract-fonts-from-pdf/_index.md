---
title: PDFからフォントを抽出する
linktitle: フォントを抽出
type: docs
weight: 30
url: /ja/java/extract-fonts-from-pdf/
description: Aspose.PDF for Javaを使用してPDFからフォントを抽出する方法
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFドキュメントからすべてのフォントを取得したい場合は、Documentクラスで提供されている`Document.IDocumentFontUtilities.getAllFonts()`メソッドを使用できます。既存のPDFドキュメントからすべてのフォントを取得するために、以下のコードスニペットを確認してください:

```java
public static void Extract_Fonts() throws FileNotFoundException
{
    // ドキュメントディレクトリへのパス
    String filePath = "<... enter file name ...>";
    
    // PDFドキュメントをロード
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Font[] fonts = pdfDocument.getFontUtilities().getAllFonts();

    for (com.aspose.pdf.Font font : fonts)
    {
        font.save(new FileOutputStream(font.getFontName()));
    }
}
```