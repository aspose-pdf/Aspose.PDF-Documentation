---
title: "Java での PDF/A-3A 準拠の PDF を作成し、ZUGFeRD 請求書の添付"
linktitle: "PDF に ZUGFeRD の添付"
type: docs
weight: 10
url: /ja/java/attach-zugferd/
description: "Java で ZUGFeRD 請求書 XML を PDF に添付し、PDF/A-3A に変換する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF 文書に ZUGFeRD 請求書 XML の添付"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF/A-3A 準拠の請求書ドキュメントを作成する方法を説明します。請求書 XML を埋め込みファイルとして添付し、MIME タイプと associated-file 関係を設定し、PDF を PDF/A-3A に変換し、最終的な ZUGFeRD 対応ドキュメントを保存する手順を網羅しています。
---
ZUGFeRD スタイルのワークフローで請求書 XML を PDF 内にパッケージングする必要がある場合、`Document` および `FileSpecification` API を使用します。

## PDF に ZUGFeRD 請求書 XML の添付

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. XML 請求書ファイル用に [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) を作成してください。
1. 埋め込みファイルのメタデータ（MIME タイプおよび [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/)）を設定してください。
1. 作成した [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) をドキュメントの埋め込みファイル コレクションへ追加してください。
1. ドキュメントを [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A` に変換してください。
1. 更新した PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

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
