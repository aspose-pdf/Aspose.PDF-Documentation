---
title: Java を使用したテキストベースの注釈
linktitle: テキスト注釈
type: docs
weight: 10
url: /ja/java/text-based-annotations/
description: "Aspose.PDF for Java を使用して、フリーテキスト、ハイライト、取り消し線、波線、下線のマークアップを含むテキストベースの PDF 注釈の作成、確認、削除方法を学習してください。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での テキスト PDF 注釈の操作"
Abstract: "この記事では、Aspose.PDF for Java における 5 つのテキストベースの注釈タイプ（フリーテキスト、ハイライト、取り消し線、波線、下線）の使用方法を示します。注釈の追加、取得、削除の方法に加え、テキストのマーキングやインタラクティブなマークアップのフラット化といった高度なテクニックも学習できます。"
---
テキストベースの注釈により、レビューアや開発者は PDF ドキュメントに対して、コアコンテンツを変更することなく、インタラクティブなノート、ハイライト、マークアップを追加できます。このセクションでは、文書レビューのワークフロー、コンプライアンスシナリオ、コラボレーティブなフィードバックサイクルで使用される実用的な 5 つの注釈タイプについて説明します。

## クイックリファレンス：アノテーションタイプ

この記事では、次のテキストベースの注釈タイプについて説明します。

- **Free Text**：メモやコメントを追加するための編集可能なテキストボックス
- **Highlight**：重要なテキストの箇所に対する視覚的強調
- **Strikeout**：レビュー中に削除または修正のためにテキストに印を付けます
- **Squiggly**：エラーや懸念を示すための波形下線
- **Underline**：伝統的な下線の強調（オプションで四点精度）

## フリーテキスト注釈の追加、取得、削除

フリーテキスト注釈は、文書構造に影響を与えることなく編集可能な浮動テキストボックスとして機能します。これらの例を使用して、コメントボックスを追加したり、プロパティを確認したり、削除したりしてください。

### フリーテキスト注釈の追加

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/freetextannotation/) を、矩形と外観設定で作成してください。
1. ページに注釈を追加し、ドキュメントを保存してください。

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```

### フリーテキスト注釈の取得

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページ上のアノテーションを反復処理し、[AnnotationType.FreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/) でフィルタリングしてください。
1. 注釈のプロパティまたは境界を取得してください。

```java
public static void freeTextAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### フリーテキスト注釈の削除

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページのアノテーションを反復処理し、タイプでフィルタリングすることで、フリーテキスト注釈を見つけてください。
1. 一致する注釈を削除リストに追加し、ページから削除してください。
1. 更新された文書を保存してください。

```java
public static void freeTextAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## ハイライト注釈を追加、取得、削除

ハイライト注釈は、半透明のオーバーレイで重要な箇所をマークします。これらの例を使用して、文書レビュー用のハイライトを作成し、既存のハイライトを検索し、マークアップをクリーンアップしてください。

### ハイライト注釈の追加

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) を、ハイライト領域を定義する長方形とともに作成してください。
1. ページに注釈を追加し、ドキュメントを保存してください。

```java
public static void textHighlightAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(300, 750, 320, 770, true));

        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

### ハイライト注釈の取得

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 注釈を反復処理し、[AnnotationType.Highlight](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/) でフィルタリングしてください。
1. バウンドや色などの注釈プロパティを読み取ってください。

```java
public static void textHighlightAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### ハイライト注釈の削除

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. タイプで注釈をフィルタリングして、ハイライト注釈を収集してください。
1. ページから各注釈を削除してください。
1. 更新された文書を保存してください。

```java
public static void textHighlightAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## ストライクアウト注釈を追加、取得、削除

取り消し線注釈は、削除、却下、または修正を示すためにテキストに取り消し線を引きます。ドキュメントレビュー中に取り消し線マークアップを適用し、マークされたテキストを検索し、取り消し線注釈を削除するには、これらの例を使用してください。

### 取り消し線注釈の追加

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/) を四角形、タイトル、色を指定して作成してください。
1. ページに注釈を追加し、ドキュメントを保存してください。

```java
public static void textStrikeoutAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        strikeoutAnnotation.setTitle("Aspose User");
        strikeoutAnnotation.setSubject("Inserted text 1");
        strikeoutAnnotation.setFlags(AnnotationFlags.Print);
        strikeoutAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(strikeoutAnnotation);
        document.save(outputFile.toString());
    }
}
```

### 取り消し線の注釈の取得

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 注釈を反復処理し、[AnnotationType.StrikeOut](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/) でフィルタリングしてください。
1. 注釈のメタデータまたは境界を読み取ってください。

```java
public static void textStrikeoutAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### 取り消し線注釈の削除

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. タイプでフィルタリングして取り消し線注釈を収集してください。
1. ページから各注釈を削除してください。
1. 更新された文書を保存してください。

```java
public static void textStrikeoutAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 波線注釈の追加、取得、削除

波線注釈（波形の下線）は、潜在的なエラー、懸念、または注意が必要な項目を強調表示します。これらの例を使用して問題のあるテキストにマーキングし、波線注釈を検査し、文書から削除してください。

### 波線注釈の追加

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/squigglyannotation/) を四角形とタイトルを指定して作成してください。
1. ページに注釈を追加し、ドキュメントを保存してください。

```java
public static void textSquigglyAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(
                page,
                new Rectangle(67, 317, 261, 459, true));
        squigglyAnnotation.setTitle("John Smith");
        squigglyAnnotation.setColor(Color.getBlue());

        page.getAnnotations().add(squigglyAnnotation);
        document.save(outputFile.toString());
    }
}
```

### 波線アノテーションの取得

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 注釈を反復処理し、[AnnotationType.Squiggly](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/) でフィルタリングしてください。
1. アノテーションの境界またはメタデータを読み取ってください。

```java
public static void textSquigglyAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### 波線注釈の削除

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. タイプでフィルタリングして波線アノテーションを収集してください。
1. ページから各注釈を削除してください。
1. 更新された文書を保存してください。

```java
public static void textSquigglyAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 下線アノテーションを追加、取得、削除

下線アノテーションは、伝統的な下線で重要な箇所を強調します。これらの例を使用して下線を作成し、マークされたテキスト内容を読み取り、ページから下線アノテーションを削除してください。

### 下線注釈の追加

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) を矩形と色で作成してください。
1. ページに注釈を追加し、ドキュメントを保存してください。

```java
public static void textUnderlineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

### 下線注釈の取得

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 注釈を反復処理し、[AnnotationType.Underline](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/) でフィルタリングしてください。
1. 注釈のプロパティまたは境界を読み取ってください。

```java
public static void textUnderlineAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### 下線注釈の削除

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. タイプでフィルタリングし、下線注釈を収集してください。
1. ページから各注釈を削除してください。
1. 更新された文書を保存してください。

```java
public static void textUnderlineAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## quad points を使用した下線アノテーションの追加

この例では、矩形から導出されたクアッドポイントを使用して、下線領域を明示的に定義しています。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) を作成し、その四隅点を計算してください。
1. ページに注釈を追加し、ドキュメントを保存してください。

```java
public static void textUnderlineWithQuadPointsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rect = new Rectangle(299.988, 713.664, 308.708, 720.769, true);
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), rect);
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline with Quad Points");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        underlineAnnotation.setQuadPoints(new com.aspose.pdf.Point[]{
                new com.aspose.pdf.Point(rect.getLLX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getURY()),
                new com.aspose.pdf.Point(rect.getLLX(), rect.getURY())
        });

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 下線注釈からマークされたテキストの取得

下線注釈でカバーされている実際のテキスト内容を取得します。これらの例では、2つのアプローチを示しています：マークされたテキスト全体を単一の文字列として読む方法、またはテキストフラグメントを個別に処理して詳細な分析を行う方法です。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページ上の下線注釈を順に処理してください。
1. `getMarkedText()` または `getMarkedTextFragments()` のいずれかを呼び出して、結果を印刷してください。

```java
public static void textUnderlineMarkedTextGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                System.out.println("Marked text: " + ua.getMarkedText());
            }
        }
    }
}
```

```java
public static void textUnderlineMarkedFragmentsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                for (TextFragment fragment : ua.getMarkedTextFragments()) {
                    System.out.println("Fragment text: " + fragment.getText());
                }
            }
        }
    }
}
```

## タイトルによる下線アノテーションの削除

タイトルなどのメタデータプロパティでフィルタリングすることで、注釈を選択的に削除できます。このアプローチにより、著者や目的別に注釈のターゲットとなるクリーンアップが可能になります。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. タイトルで下線アノテーションをフィルタリングしてください。
1. 一致する注釈を削除し、更新されたドキュメントを保存してください。

```java
public static void textUnderlineByTitleDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<UnderlineAnnotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                if ("Aspose User".equals(ua.getTitle())) {
                    toDelete.add(ua);
                }
            }
        }
        for (UnderlineAnnotation ua : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(ua);
        }
        document.save(outputFile.toString());
    }
}
```

## アンダーライン注釈の追加とフラット化

インタラクティブな下線アノテーションをフラット化して、永久的なページコンテンツに変換します。これにより、さらに編集できなくなりますが、すべての PDF ビューアで下線の外観が保持されます。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページへ [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) を追加してください。
1. 注釈に対して `flatten()` を呼び出し、出力ファイルを保存してください。

```java
public static void textUnderlineFlattenAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline to Flatten");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        underlineAnnotation.flatten();

        document.save(outputFile.toString());
    }
}
```

## 関連注釈トピック

- [インタラクティブ注釈](/pdf/ja/java/interactive-annotations/)
- [マークアップ注釈](/pdf/ja/java/markup-annotations/)
- [セキュリティ注釈](/pdf/ja/java/security-annotations/)
- [形状注釈](/pdf/ja/java/shape-annotations/)
- [透かし注釈](/pdf/ja/java/watermark-annotations/)
- [アノテーションのインポートとエクスポート](/pdf/ja/java/import-export-annotations/)
