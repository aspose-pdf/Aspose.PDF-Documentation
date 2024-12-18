---
title: PDFファイル情報の設定 - ファサード
type: docs
weight: 20
url: /ja/java/set-pdf-information/
description: このセクションでは、PdfFileInfoクラスを使用してAspose.PDFファサードでPDFファイル情報を設定する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) クラスは、PDFドキュメントのファイル固有の情報を設定することを可能にします。まず、[PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) クラスのオブジェクトを作成し、次に著者、タイトル、キーワード、作成者などの異なるファイル固有のプロパティを設定します。最後に、[PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) オブジェクトの [saveNewInfo(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#saveNewInfo-java.io.OutputStream-) メソッドを使用して更新されたPDFファイルを保存します。

次のコードスニペットは、PDFファイル情報を設定する方法を示しています。

```java
 public static void SetPdfInfo()
    {
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // PDF情報の設定
        fileInfo.setAuthor("Aspose");
        fileInfo.setTitle ("Hello World!");
        fileInfo.setKeywords("Peace and Development");
        fileInfo.setCreator ("Aspose");
        
        // 更新されたファイルを保存
        fileInfo.saveNewInfo(_dataDir + "SetfileInfo_out.pdf");
    }
```


## メタ情報を設定する

[setMetaInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#setMetaInfo-java.lang.String-java.lang.String-) メソッドを使用すると、任意の情報を追加できます。私たちの例では、フィールドを追加しました。次のコードスニペットを確認してください:

```java
   public static void SetMetaInfo()
    {
        // PdffileInfoオブジェクトのインスタンスを作成
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "sample.pdf");
       
        // 新しい顧客属性をメタ情報として設定
        fInfo.setMetaInfo("Reviewer", "Aspose.PDF user");

        // 更新されたファイルを保存
        fInfo.saveNewInfo(_dataDir + "SetMetaInfo_out.pdf");

    }
```