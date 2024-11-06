---
title: PDFファイル情報の取得 - ファサード
type: docs
weight: 10
url: ja/java/get-pdf-information/
description: このセクションでは、PdfFileInfoクラスを使用してAspose.PDFファサードでPDFファイル情報を取得する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDFファイルに特有の情報を取得するためには、[PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo)クラスのオブジェクトを作成する必要があります。その後、Subject、Title、Keywords、Creatorなどの個々のプロパティの値を取得できます。

以下のコードスニペットは、PDFファイル情報を取得する方法を示しています。

```java
public static void GetPdfInfo()
    {
        // ドキュメントを開く
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // PDF情報を取得
        System.out.println("Subject: " + fileInfo.getSubject());
        System.out.println("Title: " + fileInfo.getTitle());
        System.out.println("Keywords: " + fileInfo.getKeywords());
        System.out.println("Creator: " + fileInfo.getCreator());
        System.out.println("Creation Date: " + fileInfo.getCreationDate());
        System.out.println("Modification Date: " + fileInfo.getModDate());
        // 有効なPDFであるかどうか、および暗号化されているかどうかを確認
        System.out.println("Is Valid PDF: " + fileInfo.isPdfFile());
        System.out.println("Is Encrypted: " + fileInfo.isEncrypted());

        System.out.println("Page width:" +fileInfo.getPageWidth(1));
    }
```


## メタ情報を取得する

情報を取得するために、[getHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#getHeader--) メソッドを使用します。'Hashtable' を使用して、すべての可能な値を取得します。

```java
public static void GetMetaInfo()
    {        
        // PdffileInfoオブジェクトのインスタンスを作成
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");

        // 既存のすべてのカスタム属性を取得
        Hashtable<String,String> hTable = new Hashtable<String,String>(fInfo.getHeader());

        Enumeration<String> enumerator = hTable.keys();
        while (enumerator.hasMoreElements()) { 
            // キーを取得
            String key = enumerator.nextElement();  
            // そのキーに対応するキーと値を出力
            System.out.println(key + ": " + hTable.get(key));
        }

        // 1つのカスタム属性を取得
        System.out.println( fInfo.getMetaInfo("Reviewer"));
```