---
title: 演算子の操作
linktitle: 演算子の操作
type: docs
weight: 170
url: /ja/java/operators/
description: このトピックでは、Aspose.PDFで演算子を使用する方法を説明します。演算子クラスはPDF操作に優れた機能を提供します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF演算子とその使用法の紹介

演算子は、ページ上にグラフィカルな形を描画するなど、実行されるべきアクションを指定するPDFキーワードです。演算子キーワードは、初期ソリッドキャラクター（2Fh）がないことで名前付きオブジェクトと区別されます。演算子は、コンテンツストリーム内でのみ意味があります。

コンテンツストリームは、ページに描画されるグラフィカル要素を説明する指示からなるデータを持つPDFストリームオブジェクトです。PDF演算子の詳細は、[PDF仕様](https://www.adobe.com/devnet/pdf/pdf_reference.html)で見つけることができます。

### 実装の詳細

このトピックでは、Aspose.PDFで演算子を使用する方法を説明します。
 The selected example adds an image into a PDF file to illustrate the concept. To add an image in a PDF file, different operators are needed. This example uses [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), and [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).

選択された例は、概念を説明するために画像をPDFファイルに追加します。PDFファイルに画像を追加するには、異なるオペレーターが必要です。この例では、[GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave)、[ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix)、[Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do)、および [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) を使用します。

- The [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) operator saves the PDF's current graphical state.
- [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) オペレーターは、PDFの現在のグラフィカル状態を保存します。
- The This topic explains how to use operators with Aspose.PDF.
- このトピックでは、Aspose.PDFでオペレーターを使用する方法を説明します。 選択された例は、概念を説明するためにPDFファイルに画像を追加します。PDFファイルに画像を追加するには、さまざまなオペレーターが必要です。この例では、[GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave)、[ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix)、[Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do)、および[GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore)を使用します。
（行列の連結）オペレーターは、画像をPDFページにどのように配置するかを定義するために使用されます。
- [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) オペレーターは、ページに画像を描画します。
- [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) オペレーターは、グラフィカルな状態を復元します。

PDFファイルに画像を追加するには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトを作成し、入力PDFドキュメントを開きます。
1. 画像を追加する特定のページを取得します。
1. ページのリソースコレクションに画像を追加します。
1. 演算子を使用してページに画像を配置します。
   - まず、[GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) 演算子を使用して現在のグラフィック状態を保存します。
   - 次に、[ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix) 演算子を使用して画像を配置する場所を指定します。
   - [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) 演算子を使用してページに画像を描画します。
1. 最後に、[GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) 演算子を使用して更新されたグラフィック状態を保存します。

次のコードスニペットは、PDF 演算子の使用方法を示しています。

```java
public class WorkingWithOperators {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Operators/";

    public static void AddImageUsingOpeartors() {

        // 新しいPDFドキュメントを作成します
        Document pdfDocument = new Document(_dataDir + "PDFOperators.pdf");

        // 画像を追加する必要があるページを取得します
        Page page = pdfDocument.getPages().get_Item(1);

        // 座標を設定します
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // 画像をストリームに読み込みます
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(_dataDir + "PDFOperators.jpg");
        } catch (FileNotFoundException e) {
            // TODO 自動生成されたキャッチブロック
            e.printStackTrace();
        }

        // 画像をページリソースの画像コレクションに追加します
        page.getResources().getImages().add(imageStream);

        // GSave 演算子を使用します: この演算子は現在のグラフィック状態を保存します
        page.getContents().add(new GSave());
        // Rectangle と Matrix オブジェクトを作成します
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // ConcatenateMatrix (行列を連結する) 演算子を使用します: 画像をどのように配置するかを定義します
        page.getContents().add(new ConcatenateMatrix(matrix));

        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Do 演算子を使用します: この演算子は画像を描画します
        page.getContents().add(new Do(ximage.getName()));
        // GRestore 演算子を使用します: この演算子はグラフィック状態を復元します
        page.getContents().add(new GRestore());

        // 更新されたドキュメントを保存します
        pdfDocument.save(_dataDir + "PDFOperators_out.pdf");
    }
```


## オペレーターを使用してページ上にXFormを描画する

このトピックでは、GSave/GRestoreオペレーター、xFormを配置するためのContatenateMatrixオペレーター、およびページ上にxFormを描画するためのDoオペレーターを使用する方法を示します。

以下のコードは、PDFファイルの既存の内容をGSave/GRestoreオペレーターのペアでラップします。このアプローチは、既存の内容の最後に初期グラフィックス状態を取得するのに役立ちます。このアプローチがないと、既存のオペレーターのチェーンの最後に望ましくない変換が残る可能性があります。

```java
    public static void DrawXFormUsingOpeartors() {
        String imageFile = _dataDir + "aspose-logo.jpg";
        String inFile = _dataDir + "DrawXFormOnPage.pdf";
        String outFile = _dataDir + "blank-sample2_out.pdf";

        Document pdfDocument = new Document(inFile);
        OperatorCollection pageContents = pdfDocument.getPages().get_Item(1).getContents();

        // サンプルは以下を示しています
        // GSave/GRestoreオペレーターの使用法
        // xFormを配置するためのContatenateMatrixオペレーターの使用法
        // ページ上にxFormを描画するためのDoオペレーターの使用法

        // 既存の内容をGSave/GRestoreオペレーターのペアでラップ
        // これは既存の内容の最後に初期グラフィックス状態を取得するためのもの
        // そうしないと、既存のオペレーターのチェーンの最後に
        // 望ましくない変換が残る可能性があります
        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());

        // 新しいコマンドの後にグラフィックス状態を適切にクリアするための
        // グラフィックス状態保存オペレーターを追加
        pageContents.add(new GSave());

        // xFormを作成
        XForm form = XForm.createNewForm(pdfDocument.getPages().get_Item(1), pdfDocument);
        pdfDocument.getPages().get_Item(1).getResources().getForms().add(form);
        form.getContents().add(new GSave());

        // 画像の幅と高さを定義
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // 画像をストリームに読み込む
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(imageFile);
        } catch (FileNotFoundException e) {
            // TODO 自動生成されたキャッチブロック
            e.printStackTrace();
        }

        // 画像をXFormリソースのImagesコレクションに追加
        form.getResources().getImages().add(imageStream);
        XImage ximage = form.getResources().getImages().get_Item(form.getResources().getImages().size());
        // Doオペレーターを使用: このオペレーターは画像を描画します
        form.getContents().add(new Do(ximage.getName()));
        form.getContents().add(new GRestore());

        pageContents.add(new GSave());
        // フォームをx=100 y=500座標に配置
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        // Doオペレーターでフォームを描画
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        pageContents.add(new GSave());

        // フォームをx=100 y=300座標に配置
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 300));

        // Doオペレーターでフォームを描画
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        // // GSaveの後にGRestoreでグラフィックス状態を復元
        pageContents.add(new GRestore());
        pdfDocument.save(outFile);
    }
```


## オペレータークラスを使用してグラフィックオブジェクトを削除する

オペレータークラスはPDF操作のための素晴らしい機能を提供します。PDFファイルに[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)クラスの[DeleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) メソッドで削除できないグラフィックが含まれている場合、オペレータークラスを使用してそれらを削除することができます。

次のコードスニペットは、グラフィックを削除する方法を示しています。PDFファイルにグラフィックのためのテキストラベルが含まれている場合、このアプローチを使用するとそれらがPDFファイルに残る可能性があることに注意してください。そのため、そのような画像を削除する別の方法をオペレーターで検索してください。

```java
    public static void RemoveGraphicsOpeartors() {
        Document pdfDocument  = new Document(_dataDir+ "RemoveGraphicsObjects.pdf");
        Page page = pdfDocument.getPages().get_Item(2);
        OperatorCollection oc = page.getContents();

        // 使用されるパス描画オペレーター
        Operator[] operators = new Operator[] {
                new Stroke(),
                new ClosePathStroke(),
                new Fill()
        };

        oc.delete(operators);
        pdfDocument.save(_dataDir+ "No_Graphics_out.pdf");
    }
```


## PDFドキュメントのカラースペースの変更

{{% alert color="primary" %}}

Aspose.PDF for Java 9.0.0は、PDFドキュメントのカラースペースを変更することをサポートしています。RGBカラーをCMYKに、またその逆も可能です。

{{% /alert %}}

以下のメソッドが[Operator](https://reference.aspose.com/java/pdf/com.aspose.pdf/Operator)クラスに実装されており、カラースペースを変更することができます。特定のRGB/CMYKカラーをCMYK/RGBカラースペースに変更し、残りのPDFドキュメントはそのまま保持します。

{{% alert color="primary" %}}
**公開APIの変更**
以下のメソッドが実装されています：

- com.aspose.pdf.Operator.SetRGBColorStroke.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetRGBColor.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetCMYKColorStroke.getRGBColor(new double[4], new double[3])
- com.aspose.pdf.Operator.SetCMYKColor.getRGBColor(new double[4], new double[3])

{{% /alert %}}

以下のコードスニペットは、Aspose.PDF for Javaを使用してカラースペースを変更する方法を示しています。

```java
Document doc = new Document("input_color.pdf");
OperatorCollection contents = doc.getPages().get_Item(1).getContents();
System.out.println("PDFドキュメント内のRGBカラーオペレーターの値");
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetRGBColor || oper instanceof Operator.SetRGBColorStroke)
        try {
            // RGBをCMYKカラーに変換する
            System.out.println(oper.toString());

            double[] rgbFloatArray = new double[] { Double.valueOf(oper.getParameters().get(0).toString()), Double.valueOf(oper.getParameters().get(1).toString()), Double.valueOf(oper.getParameters().get(2).toString()), };
            double[] cmyk = new double[4];
            if (oper instanceof Operator.SetRGBColor) {
                ((Operator.SetRGBColor) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColor(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else if (oper instanceof Operator.SetRGBColorStroke) {
                ((Operator.SetRGBColorStroke) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColorStroke(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else
                throw new java.lang.Throwable("サポートされていないコマンド");

        } catch (Throwable e) {
            e.printStackTrace();
        }
}
doc.save("input_colorout.pdf");

// 結果をテストする
System.out.println("結果PDFドキュメント内の変換されたCMYKカラーオペレーターの値");
doc = new Document("input_colorout.pdf");
contents = doc.getPages().get_Item(1).getContents();
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetCMYKColor || oper instanceof Operator.SetCMYKColorStroke) {
        System.out.println(oper.toString());
    }
}
```