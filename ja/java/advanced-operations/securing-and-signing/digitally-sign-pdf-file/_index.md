---
title: PDFにデジタル署名する方法
linktitle: PDFにデジタル署名
type: docs
weight: 10
url: ja/java/digitally-sign-pdf-file/
description: Javaを使用してPDF文書にデジタル署名を行います。JavaベースのアプリケーションでPDFライブラリを使用して、デジタル署名されたPDFを検証または確認します。PKCS1証明書を使用してPDFファイルを認証できます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

署名を使用してPDF文書に署名する際、基本的にその内容が「そのまま」であるべきことを確認します。したがって、その後に加えられた変更は署名を無効にし、文書が変更されたかどうかがわかります。文書を最初に認証することで、ユーザーが認証を無効にすることなく文書に対して行える変更を指定することができます。

言い換えれば、文書はその整合性を保持していると見なされ、受取人は文書を信頼することができます。詳細については、PDFの認証と署名をご覧ください。

上記の要件を達成するために、次のパブリックAPIの変更が行われました。

isCertified(…) メソッドが PdfFileSignature クラスに追加されました。

## デジタル署名でPDFに署名する

```java
public class ExampleDigitallySign {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void SignDocument() {
        String inFile = _dataDir + "DigitallySign.pdf";
        String outFile = _dataDir + "DigitallySign_out.pdf";
        Document document = new Document(inFile);

        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Pa$$w0rd2020"); // PKCS7/PKCS7Detached
                                                                                              // オブジェクトを使用
        signature.sign(1, true, new java.awt.Rectangle(300, 100, 400, 200), pkcs);
        // 出力PDFファイルを保存
        signature.save(outFile);
    }
```

## デジタル署名にタイムスタンプを追加する

Aspose.PDF for Java は、タイムスタンプサーバーまたはWebサービスでPDFにデジタル署名することをサポートしています。

この要件を達成するために、[TimestampSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf/TimestampSettings) クラスが Aspose.PDF 名前空間に追加されました。以下のコードスニペットを見て、タイムスタンプを取得し、それをPDFドキュメントに追加してください。

```java
    public static void SignWithTimeStampServer() {
        Document document = new Document(_dataDir + "SimpleResume.pdf");
        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Start2020");
        TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", ""); // ユーザー/パスワードは省略可能
        pkcs.setTimestampSettings(timestampSettings);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 200, 100);
        // 3つの署名タイプのいずれかを作成
        signature.sign(1, "署名の理由", "連絡先", "場所", true, rect, pkcs);
        // 出力PDFファイルを保存
        signature.save(_dataDir + "DigitallySignWithTimeStamp_out.pdf");
    }
```