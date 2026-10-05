---
title: JavaでPDF/3-A準拠のPDFを作成し、ZUGFeRD請求書を添付する
linktitle: PDFにZUGFeRDを添付する
type: docs
weight: 10
url: /ja/java/attach-zugferd/
description: JavaでZUGFeRD請求書XMLをPDFに添付し、PDF/A-3Aに変換する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDF文書にZUGFeRD請求書XMLを添付する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF/A-3A 準拠の請求書ドキュメントを作成する方法を説明します。請求書 XML を埋め込みファイルとして添付し、MIME タイプと associated-file 関係を設定し、PDF を PDF/A-3A に変換し、最終的な ZUGFeRD 対応ドキュメントを保存する手順を網羅しています。
---
使用する `Document` そして `FileSpecification` ZUGFeRDスタイルのワークフローで、請求書XMLをPDF内にパッケージする必要がある場合のAPI。

## PDFにZUGFeRD請求書XMLを添付する

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 作成する [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) XML請求書ファイル用。
1. 埋め込みファイルのメタデータを設定します（MIME タイプと） [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/)。
1. 追加する [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) ドキュメントの埋め込みファイルコレクションへ。
1. ドキュメントを変換します [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`。
1. 更新された PDF を保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void attachInvoiceZugferdFormat(Path inputFile, Path invoiceFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            String description = "Invoice metadata conforming to ZUGFeRD standard";
            FileSpecification fileSpecification = new FileSpecification(invoiceFile.toString(), description);

            fileSpecification.setMIMEType("text/xml");
            fileSpecification.setAFRelationship(AFRelationship.Alternative);

            document.getEmbeddedFiles().add("factur", fileSpecification);

            String outputFileName = outputFile.toString();
            String logPath = outputFileName.replace(".pdf", "_log.xml");
            document.convert(logPath, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
            document.save(outputFile.toString());
        }
        System.out.println("ZUGFeRD invoice attached to " + outputFile);
    }
```
