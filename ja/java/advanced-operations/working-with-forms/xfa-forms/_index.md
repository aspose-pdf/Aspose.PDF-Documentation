---
title: XFA フォームの操作
linktitle: XFA フォーム
type: docs
weight: 20
url: /ja/java/xfa-forms/
description: "Aspose.PDF for Java を使用して、PDF ドキュメント内の XFA フォームを標準の AcroForms に変換する方法を学習してください。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での XFA ベースの PDF フォームの標準の AcroForms への変換"
Abstract: この記事では、Aspose.PDF for Java を使用して XFA ベースのフォームを操作する方法を説明します。動的な XFA フォームを標準の AcroForm に変換する方法と、変換前に ignore-needs-rendering オプションが必要な XFA ドキュメントの処理について解説しています。
---
XFA フォームは標準の AcroForms に変換でき、通常の PDF フォーム API で処理できるようになります。

## 動的 XFA フォームを AcroForm に変換

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ドキュメントの [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) にアクセスし、必要な [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) プロパティを設定してください。
1. 更新した PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## XFA フォームを `ignoreNeedsRendering` を使用して変換

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ドキュメントの [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) にアクセスし、必要な `ignoreNeedsRendering` および [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) プロパティを設定してください。
1. 更新した PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

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
