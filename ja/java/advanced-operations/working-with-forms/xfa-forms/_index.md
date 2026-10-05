---
title: XFA フォームの操作
linktitle: XFA フォーム
type: docs
weight: 20
url: /ja/java/xfa-forms/
description: Aspose.PDF for Java を使用して、PDF ドキュメント内の XFA フォームを標準の AcroForms に変換する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で XFA ベースの PDF フォームを標準の AcroForms に変換する
Abstract: この記事では、Aspose.PDF for Java を使用して XFA ベースのフォームを操作する方法を説明します。動的な XFA フォームを標準の AcroForm に変換する方法と、変換前に ignore-needs-rendering オプションが必要な XFA ドキュメントの処理について解説しています。
---
XFA フォームは標準の AcroForms に変換でき、通常の PDF フォーム API で処理できるようになります。

## 動的 XFA フォームを AcroForm に変換する

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ドキュメントにアクセスする [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) 必要なものを設定する [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) プロパティ。
1. 更新されたPDFを保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## XFA フォームを変換する `ignoreNeedsRendering`

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ドキュメントにアクセスする [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) 必要なものを設定する `ignoreNeedsRendering` と [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) プロパティ。
1. 更新されたPDFを保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void convertXfaFormWithIgnoreNeedsRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (!document.getForm().getNeedsRendering() && document.getForm().hasXfa()) {
            document.getForm().setIgnoreNeedsRendering(true);
        }
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```
