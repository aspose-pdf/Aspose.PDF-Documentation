---
title: PDFテキスト注釈
Texttitle: テキスト注釈
type: docs
weight: 10
url: /java/text-annotation/
description: Aspose.PDF for Javaを使用して、PDFドキュメントにテキスト注釈を追加、取得、および削除できます。
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

注釈の追加、削除、取得は、さまざまな種類の注釈で似ています。例としてテキスト注釈を取り上げます。

## 既存のPDFファイルにテキスト注釈を追加する方法

このチュートリアルでは、既存のPDFドキュメントにテキストを追加する方法を学びます。テキストツールを使用すると、ドキュメント内の任意の場所にテキストを追加できます。テキスト注釈は、PDFドキュメントの特定の場所に添付された注釈です。閉じられると、注釈はアイコンとして表示され、開かれると、選択したフォントとサイズでメモテキストを含むポップアップウィンドウを表示する必要があります。

注釈は特定のページの[Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection)コレクションに含まれています。
 このコレクションには、その個々のページ専用の注釈が含まれています。各ページには独自のAnnotationsコレクションがあります。

特定のページに注釈を追加するには、そのページのAnnotationsコレクションにAddメソッドを使用して追加します。

1. まず、PDFに追加したい注釈を作成します。
1. 次に、入力PDFを開きます。
1. 注釈を[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)オブジェクトのAnnotationsコレクションに追加します。

次のコードスニペットは、PDFページに注釈を追加する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddTextAnnotation()
    {
        // PDFファイルをロード
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);
        Rectangle rect = new Rectangle(200, 750, 400, 790);
        TextAnnotation textAnnotation = new TextAnnotation(page, rect);

        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sample Subject");
        textAnnotation.setState (AnnotationState.Accepted);
        textAnnotation.setContents("注釈のサンプルコンテンツ");
        textAnnotation.setOpen(true);
        textAnnotation.setIcon(TextIcon.Circle);

        Border border = new Border(textAnnotation);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textAnnotation.setBorder(border);
        textAnnotation.setRect(rect);

        page.getAnnotations().add(textAnnotation);
        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

## 新規追加（または作成）フリーテキスト注釈

フリーテキスト注釈は、ページ上に直接テキストを表示します。PdfContentEditor.CreateFreeTextメソッドは、このタイプの注釈を作成することを可能にします。次のスニペットでは、文字列の最初の出現箇所の上にフリーテキスト注釈を追加します。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleFreeTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddFreeTextAnnotation()
    {
        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        DefaultAppearance defaultAppearance = new DefaultAppearance();
        defaultAppearance.setFontName("Helvetica");
        defaultAppearance.setFontSize(12);
        defaultAppearance.setTextColor(java.awt.Color.BLUE);

        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

        freeTextAnnotation.setRichText("フリーテキストデモ");
        page.getAnnotations().add(freeTextAnnotation);
        document.save(_dataDir + "sample_freetext.pdf");
    }
}
```


## 無料テキスト注釈を取得する

Aspose.PDF for Java を使用すると、PDF ドキュメントから無料テキスト注釈を取得できます。

次のコードスニペットを確認して、このタスクを解決してください:

```java
public static void GetFreeTextAnnotation() {
        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "sample_freetext.pdf");

        // AnnotationSelectorを使用して注釈をフィルタリング
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
        page.accept(annotationSelector);
        List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

        // 結果を印刷する
        for (Annotation fa : freeTextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## 無料テキスト注釈を削除する

Aspose.PDF for Java を使用すると、PDF ドキュメントから無料テキスト注釈を削除できます。

次のコードスニペットを確認して、このタスクを解決してください:

```java
  public static void DeleteFreeTextAnnotation() {
         // PDFファイルをロードする
         Document document = new Document(_dataDir + "sample_freetext.pdf");

         // AnnotationSelectorを使用して注釈をフィルタリングする
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
         page.accept(annotationSelector);
         List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

         // 注釈を削除する
         for (Annotation fa : freeTextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_freetext_del.pdf");
    }
```

## PDFファイルのページからすべての注釈を削除する

[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) オブジェクトの [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) コレクションには、その特定のページのすべての注釈が含まれています。
 ページからすべてのアノテーションを削除するには、AnnotationCollection コレクションの *Delete* メソッドを呼び出します。

次のコードスニペットは、特定のページからすべてのアノテーションを削除する方法を示しています。

```java
    public static void DeleteTextAnnotation() {
         // PDFファイルを読み込む
         Document document = new Document(_dataDir + "sample_textannot.pdf");

         // AnnotationSelectorを使用してアノテーションをフィルタリング
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new TextAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> TextAnnotations = annotationSelector.getSelected();

         // アノテーションを削除
         for (Annotation fa : TextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_textannot_del.pdf");
    }
```

## PDFドキュメントのページからすべてのアノテーションを取得

Aspose.PDFを使用すると、ドキュメント全体または特定のページからアノテーションを取得できます。 PDFドキュメントのページからすべての注釈を取得するには、目的のページリソースの[AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection)コレクションをループします。次のコードスニペットは、ページのすべての注釈を取得する方法を示しています。

```java
  public static void GetTextAnnotation() {
        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // AnnotationSelectorを使用して注釈をフィルター
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new TextAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> TextAnnotations = annotationSelector.getSelected();

        // 結果を出力
        for (Annotation fa : TextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```