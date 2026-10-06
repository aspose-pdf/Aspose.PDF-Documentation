---
title: "Java での スマートカードからPDFドキュメントに署名"
linktitle: スマートカードによるPDF署名
type: docs
weight: 30
url: /ja/java/sign-pdf-document-from-smart-card/
description: "Aspose.PDF における証明書ベースの PDF 署名に関する現在の Java サンプルのカバレッジを確認してください。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 現在の Java サンプルセットにおける証明書ベースのPDF署名のカバレッジ
Abstract: このページは、Java ドキュメントのソースツリーで利用可能な署名サンプルの現在の範囲について説明しています。リポジトリには PFX または PKCS7 資格情報を使用した証明書ベースの PDF 署名サンプルが含まれていますが、現在のところ Java 用の専用スマートカード証明書ストアのサンプルは含まれていません。
---
現在の Java リポジトリには、専用のソースバックされたスマートカード署名サンプルが `facades/pdffilesignature` 配下に含まれていませんが、以下のワークフローはローカル証明書ストアから選択した証明書で PDF に署名する典型的な API パターンを示しています。

## スマートカードから PDF ドキュメントに署名

1. 元の PDF を開いて [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を取得してください。
1. [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードを作成し、元の PDF ドキュメントをバインドしてください。
1. ローカル証明書を取得し、必要な [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) を作成してください。
1. ビジュアル署名の外観と対象の [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) を構成してください。
1. PDF 文書に署名を適用するには、[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードを使用してください。
1. 更新された PDF ドキュメントを保存してください。
1. 読み込んだドキュメントを [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードにバインドするには、`bindPdf(...)` を使用してください。
1. スマートカード資格情報を表すローカル証明書を取得するには、`getLocalCertificate()` を呼び出してください。
1. 証明書が見つかったか確認してください。見つからない場合は、変更のない出力ファイルを保存し、ワークフローを停止してください。
1. 選択された証明書から [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) を作成してください。
1. 視覚的な署名外観の画像を設定するには、`setSignatureAppearance(...)` を使用してください。
1. `sign(...)` を呼び出す際は、対象ページ、理由、連絡先、場所、可視性フラグ、署名の [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)、および外部署名オブジェクトを指定してください。
1. 署名された PDF を出力パスに保存してください。

```java
public static void signWithSmartCard(Path inputFile, Path outputFile, Path pngFile) {
    try (Document document = new Document(inputFile.toString());
            PdfFileSignature pdfSignature = new PdfFileSignature()) {
        pdfSignature.bindPdf(document);
        X509Certificate2 selectedCertificate = getLocalCertificate();
        if (selectedCertificate == null) {
            System.out.println("Local certificate was not found.");
            document.save(outputFile.toString());
            return;
        }

        ExternalSignature externalSignature = new ExternalSignature(selectedCertificate, null);
        pdfSignature.setSignatureAppearance(pngFile.toString());
        pdfSignature.sign(1, "Reason", "Contact", "Location", true,
                new java.awt.Rectangle(100, 100, 200, 200), externalSignature);
        pdfSignature.save(outputFile.toString());
    }
}
```
