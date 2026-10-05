---
title: "Java での PDF オペレーターの操作"
linktitle: オペレーターの使用
type: docs
weight: 90
url: /ja/java/working-with-operators/
description: "Java で低レベルの PDF オペレーターを使用して、コンテンツストリームの操作、画像の配置、XForm の再利用、グラフィックのクリーンアップを行う方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での低レベル PDF オペレーターによるコンテンツストリームの制御"
Abstract: "この記事では、Aspose.PDF for Java における低レベル PDF オペレーターの使い方について説明します。画像を正確に配置する方法、再利用可能な XForm コンテンツを描画する方法、PDF ページからグラフィックオペレーターを削除する方法を学びます。"
---
## PDF オペレーターの概要と使用方法

オペレーターは、ページ上で図形を描画するなど、実行する動作を指定する PDF キーワードです。オペレーターのキーワードは、先頭にスラッシュ文字（2Fh）がないことで名前付きオブジェクトと区別されます。オペレーターはコンテンツストリーム内でのみ意味を持ちます。

コンテンツストリームは、ページに描画するグラフィカル要素を記述する命令をデータとして持つ PDF ストリームオブジェクトです。PDF オペレーターの詳細は、[PDF 仕様](https://opensource.adobe.com/dc-acrobat-sdk-docs/) を参照してください。

Java で PDF コンテンツストリームを直接制御する必要がある場合に、このページを使用してください。たとえば、明示的な行列計算で画像を配置したり、XForm を通じて同じグラフィックを複数回再利用したり、ページから低レベルの描画指示を削除したりする場合です。

## PDF オペレーターを使用した画像の追加

画像の配置を高レベルのレイアウト API ではなく、コンテンツストリームレベルで正確に制御する必要がある場合は、低レベルのオペレーターを使用してください。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を使用してソース PDF を開いてください。
1. 対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を取得してください。
1. 入力画像ストリームをページリソースに追加し、返されたリソース名を保持してください。
1. 対象領域を定義する [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) を作成してください。
1. その境界値から [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) を構築してください。
1. [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) を使用して現在のグラフィックス状態を保存してください。
1. [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) を使用して画像の位置を設定してください。
1. [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) を使用して画像を描画してください。
1. [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) を使用して以前のグラフィックス状態を復元してください。
1. 更新された PDF ドキュメントを保存してください。

```java
public static void addImageUsingPdfOperators(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        String imageName = page.getResources().getImages().add(imageStream);

        Rectangle rectangle = new Rectangle(100, 100, 200, 200, true);
        Matrix matrix = new Matrix(new double[]{
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY()
        });

        page.getContents().add(new GSave());
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageName));
        page.getContents().add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("Image added with PDF operators to " + outputFile);
}
```

## ページへの再利用可能な XForm コンテンツの描画

同じ画像やグラフィックを、PDF ファイル内でリソースを重複させずに複数回レンダリングする必要がある場合にこのアプローチを使用します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を使用してソース PDF を開いてください。
1. 対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を取得してください。
1. その [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/) にアクセスしてください。
1. 既存のページ コンテンツを [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) および [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) でラップし、後の変換が元のコンテンツ ストリームに漏れ出さないようにしてください。
1. [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) リソースを作成してください。
1. 画像をフォームリソースに追加してください。
1. [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) を使用して、フォーム内の座標変換を適用してください。
1. [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) を使用して、フォーム内に画像を描画してください。
1. 変換行列を追加し、フォーム名を `Do` オペレーターで実行することで、同じフォームを複数のページ座標に配置してください。
1. グラフィックス状態を復元してください。
1. 出力 PDF を保存してください。

```java
public static void drawXFormOnPage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        OperatorCollection pageContents = page.getContents();

        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());
        pageContents.add(new GSave());

        XForm form = XForm.createNewForm(page, document);
        page.getResources().getForms().add(form);

        form.getContents().add(new GSave());
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));
        String imageName = form.getResources().getImages().add(imageStream);
        form.getContents().add(new Do(imageName));
        form.getContents().add(new GRestore());

        addFormAt(pageContents, form.getName(), 100, 500);
        addFormAt(pageContents, form.getName(), 100, 300);

        pageContents.add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("XForm drawn on page in " + outputFile);
}

private static void addFormAt(OperatorCollection pageContents, String formName, double x, double y) {
    pageContents.add(new GSave());
    pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, x, y));
    pageContents.add(new Do(formName));
    pageContents.add(new GRestore());
}
```

## ページからグラフィック演算子の削除

ページにベクトル描画オペレーターが含まれており、コンテンツストリームから直接削除する必要がある場合は、この例を使用してください。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で開き、対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を取得してください。
1. ページコンテンツのオペレーターを反復処理し、[Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/)、[ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/)、および [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/) のインスタンスを収集してください。
1. 収集されたオペレーターをページコンテンツから削除し、更新された PDF を保存してください。

この手法は対象となる描画指示のみを削除します。ページに関連するテキストラベルやその他の非グラフィック演算子が含まれている場合、これらの項目はコンテンツストリームに残り、別途のクリーンアップ処理が必要になることがあります。

```java
public static void removeGraphicsObjects(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Operator> operatorsToRemove = new ArrayList<>();
        for (Object item : page.getContents()) {
            Operator operator = (Operator) item;
            if (operator instanceof Stroke || operator instanceof ClosePathStroke || operator instanceof Fill) {
                operatorsToRemove.add(operator);
            }
        }
        page.getContents().delete(operatorsToRemove);
        document.save(outputFile.toString());
    }
    System.out.println("Graphics operators removed in " + outputFile);
}
```

## 関連トピック

- [Java での高度な PDF 操作](/pdf/ja/java/advanced-operations/)
- [Java を使用した PDF の画像操作](/pdf/ja/java/working-with-images/)
- [Java での PDF ページ操作](/pdf/ja/java/working-with-pages/)
- [Java でのベクターグラフィックスの取り扱い](/pdf/ja/java/working-with-vector-graphics/)
