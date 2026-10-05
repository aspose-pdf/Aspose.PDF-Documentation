---
title: JavaでPDFページを回転させる
linktitle: PDFページの回転
type: docs
weight: 110
url: /ja/java/rotate-pages/
description: JavaでPDFページを回転させ、ページの向きを変更する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFページを回転させる
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ページを回転させる方法を説明します。サンプルでは、ドキュメント内のすべてのページを反復処理し、90 度の回転を適用して、更新された PDF を保存します。
---
1 ページまたは複数ページの向きを変更する必要がある場合は、ページ回転 API を使用してください。

## すべてのページを90度回転させる

文書内のすべてのページを時計回りに回転させる必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. すべてを反復処理する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) オブジェクトを取得し、回転値を設定してください。
1. 更新された PDF を保存してください。

```java
public static void rotatePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.setRotate(Rotation.on90);
        }
        document.save(outputFile.toString());
    }
}
```
