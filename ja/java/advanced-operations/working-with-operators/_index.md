---
title: JavaでPDFオペレーターを扱う
linktitle: オペレーターの使用
type: docs
weight: 90
url: /ja/java/working-with-operators/
description: Javaで低レベルのPDFオペレーターを使用して、コンテンツストリームの操作、画像の配置、XFormの再利用、グラフィックのクリーンアップを行う方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaでコンテンツストリーム制御に低レベルのPDFオペレーターを使用する
Abstract: この記事では、Aspose.PDF for Java における低レベル PDF 演算子の使い方について説明します。画像を正確に配置する方法、再利用可能な XForm コンテンツを描画する方法、PDF ページからグラフィック演算子を削除する方法を学びます。
---
## PDF 演算子の概要と使用方法

演算子は、ページ上にグラフィカルな形状を描画するなど、実行すべき動作を指定する PDF キーワードです。演算子キーワードは、先頭にスラッシュ文字（2Fh）がないことで名前付きオブジェクトと区別されます。演算子はコンテンツストリーム内でのみ意味を持ちます。

コンテンツストリームは、ページに描画されるグラフィカル要素を記述した命令からなるデータを持つ PDF ストリームオブジェクトです。PDF 演算子の詳細については、 [PDF 仕様](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

JavaでPDFコンテンツストリームを直接制御する必要がある場合にこのページを使用してください。たとえば、明示的な行列計算で画像を配置したり、XFormを通じて同じグラフィックを複数回再利用したり、ページから低レベルの描画指示を削除したりする場合です。

## PDF演算子を使用した画像の追加

画像の配置を高レベルのレイアウトAPIではなく、コンテンツストリームレベルで正確に制御する必要がある場合は、低レベルの演算子を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を取得してください。
1. 入力画像ストリームをページリソースに追加し、返されたリソース名を保持してください。
1. 作成する [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) ターゲット領域を定義し、構築する [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) その境界から。
1. 使用 [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) 現在のグラフィックス状態を保持するために、 [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) 画像の位置を決めるために、 [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) それを描画し、 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) 以前の状態に復元してください。
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

1. ソースPDFを開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), ターゲットを取得 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), そしてそれにアクセス [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/)。
1. 既存のページ コンテンツをでラップする [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) そして [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) 後の変換が元のコンテンツ ストリームに漏れ出さないように。
1. 作成する [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) リソース、画像をフォームリソースに追加し、使用します [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) プラス [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) フォーム内に画像を描画するために。
1. 変換行列を追加し、フォーム名を使用して実行することで、同じフォームを複数のページ座標に配置します。 `Do` オペレーター。
1. グラフィックス状態を復元し、出力 PDF を保存します。

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

ページにベクトル描画オペレーターが含まれ、コンテンツストリームから直接削除すべき場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を取得してください。
1. ページコンテンツのオペレーターを反復処理し、インスタンスを収集する [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/)、そして [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/)。
1. 収集されたオペレーターをページ内容から削除し、更新されたPDFを保存してください。

この手法は対象となる描画指示のみを削除します。ページに関連するテキストラベルやその他の非グラフィック演算子が含まれている場合、これらの項目はコンテンツストリームに残り、別個のクリーンアップパスが必要になることがあります。

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

- [Javaでの高度なPDF操作](/pdf/ja/java/advanced-operations/)
- [Java を使用して PDF の画像を操作する](/pdf/ja/java/working-with-images/)
- [JavaでPDFページを操作する](/pdf/ja/java/working-with-pages/)
- [Javaでベクターグラフィックスを扱う](/pdf/ja/java/working-with-vector-graphics/)
