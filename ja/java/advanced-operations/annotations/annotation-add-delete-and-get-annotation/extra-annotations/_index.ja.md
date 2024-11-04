---
title: 追加の種類のPDF注釈を使用する
linktitle: 追加の注釈
type: docs
weight: 60
url: /java/extra-annotations/
description: このセクションでは、PDFドキュメントに追加の種類の注釈を追加、取得、削除する方法について説明します。
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 既存のPDFファイルにキャレット注釈を追加する方法

キャレット注釈は、テキスト編集を示す記号です。キャレット注釈はマークアップ注釈でもあるため、CaretクラスはMarkupクラスから派生し、キャレット注釈のプロパティを取得または設定し、キャレット注釈の外観の流れをリセットする機能を提供します。

キャレット注釈を作成する手順:

1. PDFファイルをロードする - 新しい[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)。

1. 新しい[Caret Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/CaretAnnotation)を作成し、Caretパラメータ（新しいRectangle、タイトル、Subject、Flags、color、width、StartingStyle、EndingStyle）を設定します。この注釈はテキストの挿入を示すために使用されます。
1. 新しい[StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation)を作成し、パラメータ（新しいRectangle、タイトル、color、新しいQuadPointsと新しいポイント、Subject、InReplyTo、ReplyType）を設定します。
1. その後、注釈をページに追加できます。

次のコードスニペットは、Caret AnnotationをPDFファイルに追加する方法を示しています:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCaretAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCaretAnnotation() {
        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "sample.pdf");
        // この注釈はテキストの挿入を示すために使用されます
        CaretAnnotation caretAnnotation1 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769));
        caretAnnotation1.setTitle("Aspose User");
        caretAnnotation1.setSubject("Inserted text 1");
        caretAnnotation1.setFlags(AnnotationFlags.Print);
        caretAnnotation1.setColor(Color.getBlue());

        // この注釈はテキストの置換を示すために使用されます
        CaretAnnotation caretAnnotation2 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(361.246, 727.908, 370.081, 735.107));

        caretAnnotation2.setTitle("Aspose User");
        caretAnnotation2.setFlags(AnnotationFlags.Print);
        caretAnnotation2.setSubject("Inserted text 2");
        caretAnnotation2.setColor(Color.getBlue());

        StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1), new Rectangle(318.407, 727.826, 368.916, 740.098));

        strikeOutAnnotation.setColor(Color.getBlue());
        strikeOutAnnotation.setQuadPoints(new Point[] { new Point(321.66, 739.416),
                new Point(365.664, 739.416), new Point(321.66, 728.508),
                new Point(365.664, 728.508) });

        strikeOutAnnotation.setSubject("Cross-out");
        strikeOutAnnotation.setInReplyTo(caretAnnotation2);
        strikeOutAnnotation.setReplyType(ReplyType.Group);

        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation1);
        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation2);
        document.getPages().get_Item(1).getAnnotations().add(strikeOutAnnotation);

        document.save(_dataDir + "sample_caret.pdf");

    }
```


## Get Caret Annotation

PDFドキュメントでキャレット注釈を取得するには、次のコードスニペットを使用してください

```java
    public static void GetCaretAnnotation() {
        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // AnnotationSelectorを使用して注釈をフィルタリング
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // 結果を出力
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## Delete Caret Annotation

PDFファイルからキャレット注釈を削除する方法を示す次のコードスニペット。

```java
public static void DeleteCaretAnnotation() {
        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // AnnotationSelectorを使用して注釈をフィルタリング
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // 注釈を削除
        for (Annotation ca : caretAnnotations) {
            document.getPages().get_Item(1).getAnnotations().delete(ca);
        }
        document.save(_dataDir + "sample_caret_del.pdf");
    }
```


A [Link Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) は、ドキュメント内の他の場所への宛先や、実行するアクションへのハイパーテキストリンクです。

## リンク注釈を追加

リンクは、ページ上の任意の場所に配置できる長方形の領域です。各リンクには、それに関連付けられた対応するPDFアクションがあります。このアクションは、ユーザーがこのリンクの領域をクリックしたときに実行されます。

次のコードスニペットは、電話番号の例を使用してPDFファイルにリンク注釈を追加する方法を示しています:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLinkAnnotation {

    // ドキュメントディレクトリへのパス。

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLinkAnnotation() {
        try {
            // PDFファイルをロード
            Document document = new Document(_dataDir + "SimpleResume.pdf");
            Page page = document.getPages().get_Item(1);

            // 電話番号を見つけるために TextFragmentAbsorber オブジェクトを作成
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("678-555-0103");

            // 1ページ目のみにアブソーバを適用
            page.accept(textFragmentAbsorber);

            TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

            // リンク注釈を作成し、電話番号を呼び出すアクションを設定
            LinkAnnotation linkAnnotation = new LinkAnnotation(page, phoneNumberFragment.getRectangle());
            linkAnnotation.setAction(new GoToURIAction("callto:678-555-0103"));

            // ページに注釈を追加
            page.getAnnotations().add(linkAnnotation);
            document.save(_dataDir + "SimpleResume_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## リンク注釈を取得

次のコードスニペットを使用して、PDFドキュメントからリンク注釈を取得してみてください。

```java
    public static void GetLinkAnnotations() {

        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // AnnotationSelectorを使用して注釈をフィルター
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        // 結果を出力
        for (Annotation la : linkAnnotations) {

            LinkAnnotation l = (LinkAnnotation) la;

            // 各リンク注釈のURLを出力
            System.out.println("URI: " + ((GoToURIAction) l.getAction()).getURI());

            TextAbsorber absorber = new TextAbsorber();
            absorber.getTextSearchOptions().setLimitToPageBounds(true);
            absorber.getTextSearchOptions().setRectangle(l.getRect());
            page.accept(absorber);

            String extractedText = absorber.getText();

            // ハイパーリンクに関連付けられたテキストを出力
            System.out.println(extractedText);
        }
    }
```


## リンク注釈の削除

以下のコードスニペットは、PDFファイルからリンク注釈を削除する方法を示しています。これには、1ページ目のすべてのリンク注釈を見つけて削除する必要があります。その後、注釈が削除されたドキュメントを保存します。

```java
    public static void DeleteLinkAnnotations() {
        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // AnnotationSelectorを使用して注釈をフィルタリング
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        for (Annotation la : linkAnnotations)
            page.getAnnotations().delete(la);

        // 注釈が削除されたドキュメントを保存
        document.save(_dataDir + "SimpleResume_del.pdf");
    }
```

## Aspose.PDF for Javaを使用して特定のページ領域を編集注釈で編集する

Aspose.PDF for Javaは、既存のPDFファイルに注釈を追加および操作する機能をサポートしています。最近、一部のお客様からPDFドキュメントの特定のページ領域からテキスト、画像などの要素を削除（墨消し）する必要があると投稿されました。この要件を満たすために、RedactionAnnotationというクラスが提供されており、特定のページ領域を墨消しするために使用することができ、既存のRedactionAnnotationを操作してそれらを墨消しする（すなわち、注釈をフラットにし、その下のテキストを削除する）こともできます。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleRedactAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RedactionAnnotation() {

        // ドキュメントを開く
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // 特定のページ領域に対するRedactionAnnotationインスタンスを作成
        RedactionAnnotation annot = new RedactionAnnotation(page, new Rectangle(200, 500, 300, 600));
        annot.setFillColor(Color.getGreen());
        annot.setBorderColor(Color.getYellow());
        annot.setColor(Color.getBlue());

        // 墨消し注釈に印刷されるテキスト
        annot.setOverlayText("REDACTED");
        annot.setTextAlignment(HorizontalAlignment.Center);

        // 墨消し注釈にオーバーレイテキストを繰り返す
        annot.setRepeat(true);

        // 最初のページの注釈コレクションに注釈を追加
        page.getAnnotations().add(annot);

        // 注釈をフラットにし、ページ内容を墨消し（すなわち、テキストと画像を削除）
        annot.redact();
        document.save(_dataDir + "RedactPage_out.pdf");
    }
```


## ファサードアプローチ

Aspose.PDF.Facades 名前空間には、PDF ファイル内の既存の注釈を操作する機能を提供する [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) というクラスもあります。このクラスには、特定のページ領域を削除する機能を提供する [RedactArea(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Redaction#getredactArea-com.aspose.pdf.Page-com.aspose.pdf.Rectangle-java.awt.Color-) という名前のメソッドが含まれています。

```java
    public static void RedactionAnnotationFacades(){
        PdfAnnotationEditor editor = new PdfAnnotationEditor();

        editor.bindPdf(_dataDir + "sample.pdf");

        // 特定のページ領域を削除
        editor.redactArea(1, new Rectangle(100, 100, 20, 70), java.awt.Color.white);
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.save( _dataDir + "FacadesApproach_out.pdf");
    }
```