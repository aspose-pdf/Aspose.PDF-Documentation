---
title: JavaでスマートカードからPDFドキュメントに署名する
linktitle: スマートカードによるPDF署名
type: docs
weight: 30
url: /ja/java/sign-pdf-document-from-smart-card/
description: Aspose.PDF における証明書ベースのPDF署名に関する現在の Java サンプルのカバレッジを確認してください。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 現在の Java サンプルセットにおける証明書ベースのPDF署名のカバレッジ
Abstract: このページは、Java ドキュメントのソースツリーで利用可能な署名サンプルの現在の範囲について説明しています。リポジトリには PFX または PKCS7 資格情報を使用した証明書ベースの PDF 署名サンプルが含まれていますが、現在のところ Java 用の専用スマートカード証明書ストアのサンプルは含まれていません。
---
現在の Java リポジトリには、専用のソースバックされたスマートカード署名サンプルが以下に含まれていません。 `facades/pdffilesignature`、ただし、以下のワークフローはローカル証明書ストアから選択した証明書で PDF に署名する典型的な API パターンを示しています。

## スマートカードから PDF ドキュメントに署名する

1. 元の PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 作成する [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードと元の PDF ドキュメントをバインドしてください。
1. ローカル証明書を取得し、必要なものを作成します [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/).
1. ビジュアル署名の外観と対象を構成します [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)。
1. PDF文書に署名を適用します [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/)。
1. 更新されたPDFドキュメントを保存してください。
1. 読み込んだドキュメントをバインドする [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサード付き `bindPdf(...)`。
1. スマートカード資格情報を表すローカル証明書を取得するには、呼び出すことで `getLocalCertificate()`.
1. 証明書が見つかったか確認します。見つからない場合は、変更のない出力ファイルを保存し、ワークフローを停止してください。
1. 作成します [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) 選択された証明書から。
1. 視覚的な署名外観の画像を設定する `setSignatureAppearance(...)`。
1. 呼び出し `sign(...)` 対象ページ、理由、連絡先、場所、可視性フラグ、署名 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), および外部署名オブジェクト。
1. 署名されたPDFを出力パスに保存してください。

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
