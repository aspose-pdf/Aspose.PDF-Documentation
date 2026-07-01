---
title: PDF ファイルを PDF/A に変換する
linktitle: PDF ファイルを PDF/A に変換する
type: docs
weight: 180
url: /ja/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2026-07-01"
description: このトピックでは、Aspose.PDF for Java が PDF ファイルを PDF/A 準拠の PDF ファイルに変換する方法を示します。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF を使用すると、PDF ファイルを PDF/A 準拠の PDF ファイルに変換できます。その前に、ファイルを検証する必要があります。本記事では、その方法を説明します。

Adobe Preflight を使用して PDF/A の適合性を検証していることにご注意ください。市場にあるすべてのツールは、PDF/A の適合性について独自の「表現」を持っています。この記事をご確認ください on [PDF/A バリデーション ツール](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) 参考までに。Adobe が PDF に関係するすべての中心にあるため、Aspose.PDF が PDF ファイルを生成する方法を検証するために Adobe 製品を選びました。

PDF を PDF/A 準拠ファイルに変換する前に、validate メソッドを使用して PDF を検証します。検証結果は XML ファイルに保存され、そしてこの結果は convert メソッドにも渡されます。変換できない要素に対して実行するアクションを指定することもできます。 [変換エラー アクション](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) 列挙。

{{% alert color="primary" %}}

オンラインでお試しください。Aspose.PDF 変換の品質を確認し、結果をオンラインでこのリンクから表示できます。 [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## PDF から PDF/A_1b への変換

以下のコードスニペットは、PDF ファイルを PDF/A-1b 準拠の PDF に変換する方法を示しています。

```java
public void convertPDFtoPDFa1b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Save output document
        document.save(pdfaFileName.toString());
    }
```

検証のみを実行するには、次のコード行を使用してください：

```java
public void ValidatePDF_A_1B() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Validate to PDF/A compliant document

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("Document is valid");
        }
        else {
            resultMessage.setText("Document is not valid");
        }
    }
```

## PDFからPDF/A_3bへの変換

```java
    public void convertPDFtoPDFa3b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Save output document
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

## PDF を PDF/A_3a に変換

```java
public void convertPDFtoPDFa3a() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Save output document
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
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Save output document
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

## PDF to PDF/A_3U 変換

```java
 public void convertPDFtoPDFa3u() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Save output document
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

## PDF/A-3 を作成し、XML ファイルを添付する

Aspose.PDF for Android via Java は、PDF ファイルを PDF/A 形式に変換する機能を提供し、また PDF ドキュメントにファイルを添付する機能もサポートしています。PDF/A 準拠形式にファイルを添付する必要がある場合は、com.aspose.pdf.PdfFormat 列挙体の PDF_A_3A 値の使用を推奨します。PDF/A_3a は、任意のファイル形式を PDF/A 準拠ファイルに添付できる機能を提供する形式です。ただし、ファイルを添付した後は、メタデータを修正するために再度 Pdf-3a 形式に変換する必要があります。以下のコードスニペットをご覧ください。

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // Save output document
        try {
            // load XML file
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Sample xml file");
            // Add attachment to document's attachment collection
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

