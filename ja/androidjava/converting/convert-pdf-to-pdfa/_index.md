---
title: PDFファイルをPDF/Aに変換する 
linktitle: PDFファイルをPDF/Aに変換する 
type: docs
weight: 180
url: ja/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2021-06-05"
description: このトピックでは、Aspose.PDF for Javaを使用してPDFファイルをPDF/A準拠のPDFファイルに変換する方法を示します。  
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDFを使用すると、PDFファイルをPDF/A準拠のPDFファイルに変換できます。その前に、ファイルを検証する必要があります。この記事ではその方法を説明します。

PDF/A準拠の検証にはAdobe Preflightを使用していることに注意してください。市場のすべてのツールは、PDF/A準拠の「表現」を独自に持っています。参考のために[PDF/A検証ツール](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results)に関するこの記事をご覧ください。Aspose.PDFが生成するPDFファイルを確認するために、Adobe製品を選択しました。なぜなら、AdobeはPDFに関連するすべての中心にいるからです。

PDFをPDF/A準拠のファイルに変換する前に、validateメソッドを使用してPDFを検証してください。
 検証結果はXMLファイルに保存され、その結果もconvertメソッドに渡されます。変換できない要素に対するアクションを[ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction)列挙で指定することもできます。

{{% alert color="primary" %}}

オンラインで試してください。Aspose.PDFの変換品質を確認し、このリンクで結果をオンラインで見ることができます。[products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## PDFからPDF/A_1bへの変換

以下のコードスニペットは、PDFファイルをPDF/A-1b準拠のPDFに変換する方法を示しています。

```java
public void convertPDFtoPDFa1b() {
        // ドキュメントを開く
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/A準拠ドキュメントに変換
        // 変換プロセス中に検証も行われます
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // 出力ドキュメントを保存
        document.save(pdfaFileName.toString());
    }
```

ドキュメントの検証のみを行うには、次のコード行を使用します:

```java
public void ValidatePDF_A_1B() {
        // ドキュメントを開く
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/A準拠のドキュメントを検証する

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("ドキュメントは有効です");
        }
        else {
            resultMessage.setText("ドキュメントは無効です");
        }
    }
```

## PDFからPDF/A_3bへの変換

```java
    public void convertPDFtoPDFa3b() {
        // ドキュメントを開く
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/A準拠のドキュメントに変換する
        // 変換プロセス中に検証も行われます
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // 出力ドキュメントを保存する
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## PDFからPDF/A_3aへの変換

```java
public void convertPDFtoPDFa3a() {
        // ドキュメントを開く
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/Aに準拠したドキュメントに変換
        // 変換プロセス中に、検証も行われます
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // 出力ドキュメントを保存
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## PDFからPDF/A_2aへの変換

```java
public void convertPDFtoPDFa2a() {
        // ドキュメントを開く
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/Aに準拠したドキュメントに変換
        // 変換プロセス中に、検証も行われます
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // 出力ドキュメントを保存
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## PDF to PDF/A_3U Conversion

```java
 public void convertPDFtoPDFa3u() {
        // ドキュメントを開く
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/Aに準拠したドキュメントに変換する
        // 変換プロセス中に、検証も行われる
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // 出力ドキュメントを保存する
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## PDF/A-3を作成しXMLファイルを添付

Aspose.PDF for Android via Javaは、PDFファイルをPDF/A形式に変換する機能を提供し、PDFドキュメントにファイルを添付する機能もサポートしています。
 ファイルをPDF/A準拠形式に添付する必要がある場合は、com.aspose.pdf.PdfFormat列挙からPDF_A_3Aの値を使用することをお勧めします。PDF/A_3aは、PDF/A準拠ファイルに任意のファイル形式を添付できる形式です。ただし、ファイルを添付した後は、メタデータを修正するために再度Pdf-3a形式に変換する必要があります。以下のコードスニペットをご覧ください。

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // ドキュメントを開く
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/A準拠のドキュメントに変換
        // 変換プロセス中に検証も行われます
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // 出力ドキュメントを保存
        try {
            // XMLファイルを読み込む
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "サンプルXMLファイル");
            // ドキュメントの添付ファイルコレクションに添付ファイルを追加
            document.getEmbeddedFiles().add(fileSpecification);
            document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```