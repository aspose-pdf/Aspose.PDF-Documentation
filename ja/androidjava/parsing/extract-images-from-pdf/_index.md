---
title: PDFから画像を抽出する
linktitle: 画像を抽出する
type: docs
weight: 20
url: /ja/androidjava/extract-images-from-the-pdf-file/
description: Javaを使用したAspose.PDF for AndroidでPDFから画像の一部を抽出する方法
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFドキュメントの各ページにはリソース（画像、フォーム、フォント）が含まれています。これらのリソースには、呼び出すことでアクセスできます [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) メソッド。クラス [リソース](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) 含む [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) そして、呼び出すことで画像のリストを取得できます [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) メソッド。

したがって、ページから画像を抽出するには、まずページへの参照を取得し、次にページリソースを取得し、最後に画像コレクションを取得する必要があります。
特定の画像は、たとえばインデックスで抽出できます。

画像のインデックスは次のものを返します。 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) オブジェクトです。
このオブジェクトは、次のものを提供します。 [保存](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) 抽出された画像を保存するために使用できるメソッド。次のコードスニペットは、PDFファイルから画像を抽出する方法を示しています。

 ```java
 public void extractImage () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.Page page=document.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
        // Extract a particular image
        com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
        File file=new File(fileStorage, "extracted-image.jpeg");
        try {
            java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
            // Save output image
            xImage.save(outputImage, ImageType.getJpeg());
            outputImage.close();
        } catch (java.io.IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.
          }
```

