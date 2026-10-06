---
title: 署名情報
linktitle: 署名情報
type: docs
weight: 60
url: /ja/java/signature-information/
description: Java の PdfFileSignature を使用して、署名付き PDF から署名名と署名者の詳細を読み取る方法を学びます。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF ドキュメントから署名の詳細を読み取る
Abstract: Aspose.PDF for Java を使用して署名メタデータを検査する方法を学びます。Java の例では、最初に利用可能な署名名を読み取り、署名者、日付、理由、場所を署名付き PDF から取得します。
---
## 署名情報の取得

PDF に誰が署名したか、どのような署名メタデータが保存されているかを検査する必要がある場合にこの Workflow を使用します。

### 手順

1. `PdfFileSignature` インスタンスを作成し、署名された PDF をバインドしてください。
2. 署名コレクションを読み取り、署名名を選択してください。
3. 署名者名、日付、理由、および場所の署名情報アクセサを呼び出してください。
4. 完了したら、ファサードオブジェクトを閉じてください。

### Java の例

```java
public static void getSignatureInformation(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature Names: " + pdfSignature.getSignNames());
        System.out.println("Signer: " + pdfSignature.getSignerName(signatureName));
        System.out.println("Date: " + pdfSignature.getDateTime(signatureName));
        System.out.println("Reason: " + pdfSignature.getReason(signatureName));
        System.out.println("Location: " + pdfSignature.getLocation(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
