---
title: PDFファイルメタデータの操作
linktitle: PDFファイルメタデータ
type: docs
weight: 140
url: /java/pdf-file-metadata/
description: このセクションでは、PDFファイルの情報を取得する方法、PDFファイルからXMPメタデータを取得する方法、PDFファイル情報を設定する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイル情報の取得

PDFファイルに関するファイル固有の情報を取得するには、まず[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスの[getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--)メソッドを使用して[DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo)オブジェクトを取得します。[DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo)オブジェクトが取得されたら、個々のプロパティの値を取得できます。

以下のコードスニペットは、PDFファイル情報を設定する方法を示しています。

```java
public class ExampleMetadata {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Metadata/";

    public static void GetPDFFileInformation() {
        // 新しいPDFドキュメントを作成
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
        // ドキュメント情報を取得
        DocumentInfo docInfo = pdfDocument.getInfo();
        // ドキュメント情報を表示
        System.out.println("著者: " + docInfo.getAuthor());
        System.out.println("作成日: " + docInfo.getCreationDate());
        System.out.println("キーワード: " + docInfo.getKeywords());
        System.out.println("修正日: " + docInfo.getModDate());
        System.out.println("件名: " + docInfo.getSubject());
        System.out.println("タイトル: " + docInfo.getTitle());
    }
```


## PDFファイル情報の設定

Aspose.PDF for Javaを使用すると、PDFに対して特定のファイル情報（著者、作成日、件名、タイトルなど）を設定することができます。

この情報を設定するには：

1. [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) オブジェクトを作成します。
2. プロパティの値を設定します。
3. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスの [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) メソッドを使用して、更新されたドキュメントを保存します。

{{% alert color="primary" %}}

**Producer** および **Creator** フィールドに対して値を設定することはできません。これらのフィールドには Aspose.PDF for Java x.x.x が表示されますのでご注意ください。

{{% /alert %}}

次のコードスニペットは、PDFファイル情報を設定する方法を示しています。

```java
 public static void SetPDFFileInformation() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // ドキュメント情報を指定する
        DocumentInfo docInfo = new DocumentInfo(pdfDocument);

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(new java.util.Date());
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(new java.util.Date());
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");

        // 出力ドキュメントを保存する
        pdfDocument.save(_dataDir + "SetFileInfo_out.pdf");
    }
```


## PDFファイルからXMPメタデータを取得する

Aspose.PDF for Javaを使用すると、PDFファイルのXMPメタデータにアクセスできます。

PDFファイルのメタデータを取得するには、

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトを作成し、入力PDFファイルを開きます。
1. [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) プロパティを使用してメタデータを取得します。

次のコードスニペットは、PDFファイルからメタデータを取得する方法を示しています。

```java
   public static void GetXMPMetadata() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");

        System.out.println("xmp:CreateDate: " + pdfDocument.getMetadata().get_Item("xmp:CreateDate"));
        System.out.println("xmp:Nickname: " + pdfDocument.getMetadata().get_Item("xmp:Nickname"));
        System.out.println("xmp:CustomProperty: " + pdfDocument.getMetadata().get_Item("xmp:CustomProperty"));

    }
```

## PDFファイルにXMPメタデータを設定する

Aspose.PDF for Javaを使用すると、PDFファイルにメタデータを設定できます。
 メタデータを設定するには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトを作成します。
1. [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) プロパティを使用してメタデータの値を設定します。
1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) メソッドを使用して更新されたドキュメントを保存します。

次のコードスニペットは、PDFファイルにメタデータを設定する方法を示しています。

```java
    public static void SetXMPMetadata() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // プロパティを設定
        pdfDocument.getMetadata().set_Item("xmp:CreateDate", new XmpValue(new java.util.Date()));
        pdfDocument.getMetadata().set_Item("xmp:Nickname", new XmpValue("Nickname"));
        pdfDocument.getMetadata().set_Item("xmp:CustomProperty", new XmpValue("Custom Value"));

        // ドキュメントを保存
        pdfDocument.save(_dataDir + "SetXMPMetadata.pdf");
    }
```

## プレフィックス付きメタデータの挿入

一部の開発者は、プレフィックス付きで新しいメタデータ名前空間を作成する必要があります。以下のコードスニペットは、プレフィックス付きでメタデータを挿入する方法を示しています。

```java
    public static void InsertMetadataWithPrefix() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");
        pdfDocument.getMetadata().registerNamespaceUri("adc", "http://tempuri.org/adc/1.0");
        pdfDocument.getMetadata().set_Item("adc:format", new XmpValue("application/pdf"));
        pdfDocument.getMetadata().set_Item("adc:title", new XmpValue("alternative title"));        
        // ドキュメントを保存
        pdfDocument.save(_dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```