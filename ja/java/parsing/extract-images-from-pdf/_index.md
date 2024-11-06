---  
title: PDFから画像を抽出する  
linktitle: 画像を抽出  
type: docs  
weight: 20  
url: ja/java/extract-images-from-the-pdf-file/  
description: Aspose.PDF for Javaを使用してPDFから画像の一部を抽出する方法  
lastmod: "2021-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---

PDFドキュメントの各ページには、リソース（画像、フォーム、フォント）が含まれています。これらのリソースには、[getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) メソッドを呼び出すことでアクセスできます。クラス [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) には [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) が含まれており、[getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) メソッドを呼び出すことで画像のリストを取得できます。

したがって、ページから画像を抽出するには、まずページの参照を取得し、次にページのリソース、最後に画像コレクションへの参照を取得する必要があります。特定の画像は、例えばインデックスで抽出できます。

画像のインデックスは、[XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) オブジェクトを返します。
このオブジェクトは、抽出された画像を保存するために使用できる[Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-)メソッドを提供します。次のコードスニペットは、PDFファイルから画像を抽出する方法を示しています。

```java
public static void Extract_Images(){
        // ドキュメントディレクトリへのパス
        String _dataDir = "/home/admin1/pdf-examples/Samples/";
        String filePath = _dataDir + "ExtractImages.pdf";

        // PDFドキュメントをロード
        com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

        com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection = page.getResources().getImages();
        // 特定の画像を抽出
        com.aspose.pdf.XImage xImage = xImageCollection.get_Item(1);

        try {
            java.io.FileOutputStream outputImage = new java.io.FileOutputStream(_dataDir + "output.jpg");
            // 出力画像を保存
            xImage.save(outputImage);
            outputImage.close();
        } catch (java.io.FileNotFoundException e) {
            // TODO: 例外を処理
            e.printStackTrace();
        } catch (java.io.IOException e) {
            // TODO: 例外を処理
            e.printStackTrace();
        }
    }
```