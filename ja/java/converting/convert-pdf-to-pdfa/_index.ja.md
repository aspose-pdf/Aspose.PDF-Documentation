---
title: PDFをPDF/A形式に変換する
linktitle: PDFをPDF/A形式に変換する
type: docs
weight: 100
url: /java/convert-pdf-to-pdfa/
lastmod: "2021-11-19"
description: このトピックでは、Aspose.PDFがPDFファイルをPDF/A準拠のPDFファイルに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Java**は、PDFファイルをPDF/A準拠のPDFファイルに変換することを可能にします。そうする前に、ファイルは検証されなければなりません。この記事ではその方法を説明します。

PDF/Aの適合性を検証するために、Adobe Preflightを使用しています。市場に出回っているツールは、それぞれ独自のPDF/A適合性の「表現」を持っています。参考のために[PDF/A検証ツール](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results)に関するこの記事を確認してください。Aspose.PDFが生成するPDFファイルの検証にはAdobe製品を選択しました。なぜなら、AdobeはPDFに関するすべての中心にいるからです。

PDFをPDF/A準拠のファイルに変換する前に、validateメソッドを使用してPDFを検証してください。
 検証結果はXMLファイルに保存され、その結果はconvertメソッドにも渡されます。[ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction)列挙型を使用して変換できない要素のアクションを指定することもできます。

## PDFからPDF/A_1bへの変換

次のコードスニペットは、PDFファイルをPDF/A-1b準拠のPDFに変換する方法を示しています。

```java
// ドキュメントを開く
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// PDF/A準拠のドキュメントに変換
// 変換プロセス中に検証も行われます
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

// 出力ドキュメントを保存
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

検証のみを行うには、次のコード行を使用します：

```java
// ドキュメントを開く
Document document = new Document(DATA_DIR + "ValidatePDFAStandard.pdf");

// PDF/A-1a用のPDFを検証
if (document.validate(DATA_DIR + "validation-result-A1A.xml", PdfFormat.PDF_A_1B)) {
    System.out.println("Valid");
} else {
    System.out.println("Non valid");
}
document.close();
```

## PDF to PDF/A_3b Conversion

[Aspose.PDF for Java 9.3.0](https://downloads.aspose.com/pdf/java)から、APIはPDFファイルをPDF/A_3b形式に変換することもサポートしています。

```java
// ドキュメントを開く
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// PDF/A準拠のドキュメントに変換する
// 変換プロセス中に検証も実行されます
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

// 出力ドキュメントを保存
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

## PDF to PDF/A_3a Conversion

[Aspose.PDF for Java 10.6.0](https://downloads.aspose.com/pdf/java)から、APIはPDFファイルをPDF/A_3a形式に変換することもサポートしています。

```java
// ドキュメントを開く
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// PDF/A準拠のドキュメントに変換する
// 変換プロセス中に検証も実行されます
document.convert("file.log", PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

// 出力ドキュメントを保存
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```


## PDF to PDF/A_2a Conversion

[Aspose.PDF for Java 10.2.0](https://downloads.aspose.com/pdf/java) のリリースから、API は PDF ファイルを PDF/A3 形式に変換する機能を提供しています。

```java
    public static void ConvertPDFtoPDFa2a() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // PDF/A 準拠のドキュメントに変換する
        // 変換プロセス中に、検証も実行されます
        pdfDocument.convert("file.log", PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // 出力ドキュメントを保存する
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## PDF to PDF/A_3U Conversion

Aspose.PDF for Java 17.2.0 のリリースから、API は PDF ファイルを PDF/A_3U 形式に変換する機能を提供しています。

```java
    public static void ConvertPDFtoPDFa3u() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // PDF/A 準拠のドキュメントに変換する
        // 変換プロセス中に、検証も実行されます
        pdfDocument.convert("file.log", PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // 出力ドキュメントを保存する
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```


## PDF/A-3を作成し、XMLファイルを添付する

Aspose.PDF for Javaは、PDFファイルをPDF/A形式に変換する機能を提供し、PDFドキュメントにファイルを添付する機能もサポートしています。PDF/A準拠形式にファイルを添付する必要がある場合は、com.aspose.pdf.PdfFormat列挙からPDF_A_3A値を使用することをお勧めします。PDF/A_3a形式は、PDF/A準拠ファイルに任意のファイル形式を添付する機能を提供します。ただし、ファイルを添付した後は、メタデータを修正するために、再度Pdf-3a形式に変換する必要があります。以下のコードスニペットをご覧ください。

```java
    public static void ConvertPDFtoPDFa3u_attachXML() {
        Document doc = new Document();
        // PDFファイルにページを追加
        doc.getPages().add();
        // XMLファイルを読み込む
        FileSpecification fileSpecification = new FileSpecification(_dataDir + "attachment.xml", "サンプルXMLファイル");
        // ドキュメントの添付ファイルコレクションに添付を追加
        doc.getEmbeddedFiles().add(fileSpecification);
        // PDF/A_3a変換を実行
        doc.convert(_dataDir + "log.xml", PdfFormat.PDF_A_3A/* または PDF_A_3B */, ConvertErrorAction.Delete);
        // 最終PDFファイルを保存
        doc.save(_dataDir + "attached_PDFA_3A.pdf");
    }
```


{{% alert color="primary" %}}
**PDFをPDF/Aにオンラインで変換してみよう**

Aspose.PDF for Javaは、オンラインで無料で利用できるアプリケーション["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}