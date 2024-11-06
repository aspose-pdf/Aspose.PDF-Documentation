---
title: PDFから画像を抽出する (ファサード)
type: docs
weight: 30
url: ja/java/extract-images/
description: このセクションでは、PdfExtractorクラスを使用してAspose.PDF Facadesで画像を抽出する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) クラスは、PDFファイルから画像を抽出することを可能にします。
 最初に、[PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) クラスのオブジェクトを作成し、bindPdf メソッドを使用して入力 PDF ファイルをバインドする必要があります。その後、[extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) メソッドを呼び出して、すべての画像をメモリに抽出します。画像が抽出されたら、hasNextImage および getNextImage メソッドを使用してそれらの画像を取得できます。while ループを使用して、抽出されたすべての画像をループする必要があります。画像をディスクに保存するには、ファイル パスを引数として取る getNextImage メソッドのオーバーロードを呼び出すことができます。次のコードスニペットは、PDF 全体から画像をファイルに抽出する方法を示しています。

```java   
public static void ExtractImages()
 {
    //エクストラクターを作成してドキュメントにバインドする
    Document document = new Document(_dataDir + "sample.pdf");
    PdfExtractor extractor = new PdfExtractor(document);
    extractor.setStartPage(1);
    extractor.setEndPage(3);            

    //エクストラクターを実行する
    extractor.extractImage();
    int imageNumber = 1;
    //抽出された画像コレクションを反復処理する
    while (extractor.hasNextImage())
    {
        //コレクションから画像を取得し、ファイルに保存する
        extractor.getNextImage(_dataDir + String.format("image%03d.png", imageNumber++),ImageType.getPng());
    }
}
```