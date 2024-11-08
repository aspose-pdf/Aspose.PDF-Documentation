---
title: PDFから画像を抽出する
linktitle: 画像を抽出
type: docs
weight: 20
url: /ja/androidjava/extract-images-from-the-pdf-file/
description: Aspose.PDF for Android via Javaを使用してPDFから画像の一部を抽出する方法
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFドキュメントの各ページにはリソース（画像、フォーム、フォント）が含まれています。これらのリソースには[getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--)メソッドを呼び出すことでアクセスできます。[Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources)クラスには[XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection)が含まれており、[getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--)メソッドを呼び出すことで画像のリストを取得できます。

したがって、ページから画像を抽出するには、ページへの参照を取得し、次にページリソース、最後に画像コレクションへのアクセスが必要です。

特定の画像は、例えばインデックスを使用して抽出できます。

The image's index returns an [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) object.  
このオブジェクトは、抽出された画像を保存するために使用できる [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) メソッドを提供します。次のコードスニペットは、PDFファイルから画像を抽出する方法を示しています。

```java
public void extractImage () {
        // ドキュメントを開く
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.Page page=document.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
        // 特定の画像を抽出
        com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
        File file=new File(fileStorage, "extracted-image.jpeg");
        try {
            java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
            // 出力画像を保存
            xImage.save(outputImage, ImageType.getJpeg());
            outputImage.close();
        } catch (java.io.IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.
          }
```