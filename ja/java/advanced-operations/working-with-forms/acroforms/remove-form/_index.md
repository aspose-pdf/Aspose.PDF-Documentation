---
title: "Java での PDFからフォームの削除"
linktitle: "フォームの削除"
type: docs
weight: 70
url: /ja/java/remove-form/
description: Aspose.PDF for Java を使用して PDF ページからフォームオブジェクトを削除します。完全なクリーンアップと対象を絞った削除を含みます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFページからフォームリソースを削除する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントからフォームリソースを削除する方法を説明します。ページからすべてのフォームをクリアする方法と、ページのフォームコレクションをフィルタリングした後に選択された Typewriter フォームリソースのみを削除する方法を取り上げています。
---
これらの例は、フィールド値を変更するだけではなく、ページからフォームリソースを削除します。

## ページからすべての Form リソースの削除

選択したページのすべての Form リソースを一度の操作で削除する必要がある場合は、このサンプルを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. アクセスする [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) 対象ページに対して。
1. コレクションをクリアし、更新されたドキュメントを保存します。

```java
public static void removeAllForms(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        forms.clear();
        document.save(outputFile.toString());
    }
}
```

## 特定のフォームリソースの削除

Typewriter フォームなど、選択されたフォームリソースのみを削除する必要がある場合にこの例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. アクセスする [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) 対象ページに対して。
1. フィルタリングする [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) 削除したいリソースをコレクションから削除します。
1. 更新された PDF を保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void removeSpecifiedForm(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        List<String> formNames = new ArrayList<>();
        for (XForm form : forms) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                formNames.add(forms.getFormName(form));
            }
        }
        for (String formName : formNames) {
            forms.delete(formName);
        }
        document.save(outputFile.toString());
    }
}
```
