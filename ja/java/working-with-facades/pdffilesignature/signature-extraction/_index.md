---
title: 署名抽出
linktitle: 署名抽出
type: docs
weight: 50
url: /ja/java/signature-extraction/
description: Java と PdfFileSignature を使用して、署名済み PDF から署名証明書を抽出する方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF から署名証明書を抽出する
Abstract: Aspose.PDF for Java を使用して PDF 署名に関連付けられた証明書を抽出する方法を学びます。現在の Java のサンプルセットには、証明書を出力ストリームに抽出する例が含まれていますが、署名画像を個別に抽出するサンプルは含まれていません。
---
## 署名証明書の抽出

既存の署名に関連付けられた証明書を保存する必要がある場合に、このワークフローを使用します。

### 手順

1. 作成 `PdfFileSignature` インスタンスを作成し、署名されたPDFをバインドしてください。
2. 検査する署名名を選択してください。
3. 呼び出す `extractCertificate` 証明書ストリームを開くために。
4. 証明書バイトを出力ファイルにコピーしてください。
5. ストリームリソースとファサードオブジェクトを閉じます。

### Java の例

```java
public static void extractSignatureCertificate(Path inputFile, Path outputFile) throws Exception {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        try (InputStream inputStream = pdfSignature.extractCertificate(signatureName);
             OutputStream outputStream = Files.newOutputStream(outputFile)) {
            inputStream.transferTo(outputStream);
        }
    } finally {
        pdfSignature.close();
    }
}
```

現在の `PdfFileSignatureExamples.java` クラスには、レンダリングされた署名画像を抽出するための専用の Java サンプルが含まれていません。
