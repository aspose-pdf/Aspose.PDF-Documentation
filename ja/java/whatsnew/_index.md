---
title: 新機能
linktitle: 新機能
type: docs
weight: 10
url: /ja/java/whatsnew/
description: このページでは、最近のリリースで導入されたAspose.PDF for Javaの最も人気のある新機能を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-06-05"
---

## Aspose.PDF 24.8の新機能

24.8以降、PDF/A-4形式のサポート:

```java

    Document document = new Document(inputPdf);
    // PDF-2.xドキュメントのみPDF/A-4に変換可能
    document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
    boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
    document.save(outputFile);
```

また、画像スタンプに代替テキストを追加することが可能:

ImageStampにAlternativeTextプロパティが追加されました - それに値が割り当てられると、ドキュメントにImageStampを追加する際に代替テキストが付きます。

```java

    String p1_Alt1 = "*** ページ 1, 代替テキスト 1 ***",
                    p1_Alt2 = "*** ページ 1, 代替テキスト 2 ***",
                    p2_Alt1 = "--- ページ 1, 代替テキスト 1 ---",
                    p2_Alt2 = "--- ページ 1, 代替テキスト 2 ---";

    StructTreeRootElement structTreeRoot = document.getTaggedContent().getStructTreeRootElement();

    ImageStamp imageStamp = new ImageStamp(dataDir + "test.jpg");
    imageStamp.setXIndent(100);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setQuality(100);
    imageStamp.setAlternativeText(p1_Alt1);

    // ページ 1に
    document.getPages().get_Item(1).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p1_Alt2);
    document.getPages().get_Item(1).addStamp(imageStamp);

    // ページ 2に
    document.getPages().add();
    imageStamp.setXIndent(400);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setAlternativeText(p2_Alt1);
    document.getPages().get_Item(2).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p2_Alt2);
    document.getPages().get_Item(2).addStamp(imageStamp);

    // ドキュメントを保存
    document.save(outFile);
```


また、次のコードは、FigureElements内の既存の画像にAlternativeTextを追加する方法を示しています。

```java

    String inFile = dataDir + "46040.pdf";
    String outFile = dataDir + "46040_1_out.pdf";

    Document document = new Document(inFile);

    ITaggedContent taggedContent = document.getTaggedContent();
    StructureElement rootElement = taggedContent.getRootElement();

    Iterator tmp0 = (rootElement.getChildElements()).iterator();
    while (tmp0.hasNext())
    {
        com.aspose.pdf.tagged.logicalstructure.elements.Element element = (com.aspose.pdf.tagged.logicalstructure.elements.Element)tmp0.next();
        if (element instanceof com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)
                {
            com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figureElement = (com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)element;

            // 代替テキストを設定
            figureElement.setAlternativeText("Figure alternative text (technique 1)");
        }
    }

    // ドキュメントを保存
    document.save(outFile);
```


## Aspose.PDF 24.7の新機能

24.7リリース以降、タグ付きPDFの編集の一環として、**Aspose.Pdf.LogicalStructure.Element**に以下のメソッドが追加されました：

- Tag（画像、テキスト、リンクなどの特定のオペレーターにタグを追加）
- InsertChild
- RemoveChild
- ClearChilds

これらのメソッドは、PDFファイルのタグを編集することを可能にします。例えば：

```java

    Document document = new Document(dataDir + "test.pdf");

    // ドキュメントの最初のページを取得します。
    Page page = document.getPages().get_Item(1);

    // 異なる目的のためのBDC（Begin Dictionary Context）要素を保持するための変数を初期化します。
    BDC imageBdc = null;
    BDC pBdc = null;
    BDC link1Bdc = null;
    BDC link2Bdc = null;
    BDC helloBdc = null;

    // ページのコンテンツを反復処理します。
    for (int i = 1; i <= page.getContents().size(); i++)
    {
        // ページコンテンツから現在のオペレーターを取得します。
        Operator op = page.getContents().get_Item(i);

        // オペレーターがBDCのインスタンスであるかどうかを確認します。
        if (op instanceof BDC) {
        BDC bdc = (BDC)op; // オペレーターをBDCタイプにキャストします。
        if (bdc != null)
        {
            // BDCのMCID（Mark Content Identifier）が0であるかどうかを確認します。
            if (bdc.getProperties().getMCID()[0] != null && bdc.getProperties().getMCID()[0] == 0)
            {
                helloBdc = bdc; // 後で使用するためにBDCを保存します。
            }
        }
    }

    // オペレーターがDo（Draw Object）のインスタンスであるかどうかを確認します。
    if (op instanceof Do) {
        Do doXobj = (Do)op; // オペレーターをDoタイプにキャストします。
        if (doXobj != null)
        {
            // 画像用の新しいBDCを作成し、ページのコンテンツに挿入します。
            imageBdc = new BDC("Figure");
            page.getContents().insert(i - 2, imageBdc); // 現在のオペレーターの前に挿入します。
            i++; // 挿入されたBDCを考慮してインデックスを増やします。
            page.getContents().insert(i + 1, new EMC()); // EMC（End Mark Content）を挿入します。
            i++; // インデックスを再度増やします。
        }
    }

    // オペレーターがTextShowOperator（テキスト表示用）のインスタンスであるかどうかを確認します。
    if (op instanceof TextShowOperator) {
        TextShowOperator tx = (TextShowOperator)op; // オペレーターをTextShowOperatorタイプにキャストします。
        if (tx != null)
        {
            // 特定のテキスト内容を確認し、対応するBDCを挿入します。
            if (tx.getText().contains("efter Ukendt forfatter er licenseret under"))
            {
                pBdc = new BDC("P");
                page.getContents().insert(i - 1, pBdc); // 現在のオペレーターの前に挿入します。
                i++; // インデックスを増やします。
                page.getContents().insert(i + 1, new EMC()); // EMCを挿入します。
                i++; // インデックスを増やします。
            }
            if (tx.getText().contains("CC"))
            {
                link1Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link1Bdc); // 現在のオペレーターの前に挿入します。
                i++; // インデックスを増やします。
                page.getContents().insert(i + 1, new EMC()); // EMCを挿入します。
                i++; // インデックスを増やします。
            }
            if (tx.getText().contains("Dette billede"))
            {
                link2Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link2Bdc); // 現在のオペレーターの前に挿入します。
                i++; // インデックスを増やします。
                page.getContents().insert(i + 1, new EMC()); // EMCを挿入します。
                i++; // インデックスを増やします。
            }
        }
    }
}
 
    // ドキュメントからタグ付きコンテンツを取得します。
    ITaggedContent tagged = document.getTaggedContent();

    // 構造属性を変更するためにタグ付きコンテンツを処理します。
    // タグ付きコンテンツのルート要素の最初の子要素を取得します。
    com.aspose.pdf.tagged.logicalstructure.elements.Element p = tagged.getRootElement().getChildElements().get_Item(1);
    p.clearChilds(); // 既存の子要素をクリアします。

    // helloBdcを親構造要素でタグ付けします。
    MCRElement mcr = p.tag(helloBdc);

    // タグ付けされた要素のための構造属性を作成して設定します。
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
            .getAttributes().createAttributes(AttributeOwnerStandard.Layout);
    StructureAttribute attr = new StructureAttribute(AttributeKey.SpaceAfter);
    attr.setNumberValue(30.625); // Space after属性を設定します。
    attrs.setAttribute(attr); // 構造に属性を適用します。

    // タグ付きコンテンツに新しいFigureElementを作成します。
    com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figure = tagged.createFigureElement();
    tagged.getRootElement().insertChild(figure, 2); // 図要素を2番目の位置に挿入します。
    figure.setAlternativeText("A fly."); // 図の代替テキストを設定します。

    // imageBdcを図要素でタグ付けします。
    MCRElement mcr = figure.tag(imageBdc);

    // 指定されたMCR（Marked Content Reference）の親構造要素を取得します。
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // 要素の後にスペースを設定するための新しいStructureAttributeを作成します。
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(3.625); // スペース後の値を3.625単位に設定します。
    attrs.setAttribute(spaceAfter); // 構造属性にスペース後属性を割り当てます。

    // バウンディングボックス（BBox）の新しいStructureAttributeを作成します。
    StructureAttribute bbox = new StructureAttribute(AttributeKey.BBox);
    bbox.setArrayNumberValue(new Double[][] { new Double[] { (71.9971) }, new Double[] { (375.839) }, new Double[] { (523.299) }, new Double[] { (714.345) } });
    // 構造属性のバウンディングボックス値を設定します。
    attrs.setAttribute(bbox); // 構造属性にバウンディングボックス属性を割り当てます。

    // 配置のための新しいStructureAttributeを作成します。
    StructureAttribute placement = new StructureAttribute(AttributeKey.Placement);
    placement.setNameValue(AttributeName.Placement_Block); // 配置タイプをブロックに設定します。
    attrs.setAttribute(placement); // 構造属性に配置属性を割り当てます。

    // タグ付き構造のルート要素から4番目の子要素を取得します。
    StructureElement p2 = (StructureElement)tagged.getRootElement().getChildElements().get_Item(3);
    p2.clearChilds(); // p2から既存の子要素をクリアします。

    // p2に追加するための新しいSpanElementを作成します。
    SpanElement span1 = tagged.createSpanElement();

    // スパン要素のための構造属性を作成します。
    StructureAttributes attrs = span1.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // テキスト装飾タイプの新しいStructureAttributeを作成します。
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // テキスト装飾を下線に設定します。
    attrs.setAttribute(textDecorationType); // 構造属性にテキスト装飾タイプ属性を割り当てます。

    // テキスト装飾の太さの新しいStructureAttributeを作成します。
    StructureAttribute textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    textDecorationThickness.setNumberValue(0); // テキスト装飾の太さを0に設定します。
    attrs.setAttribute(textDecorationThickness); // 構造属性にテキスト装飾の太さ属性を割り当てます。

    // テキスト装飾の色の新しいStructureAttributeを作成します。
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    textDecorationColor.setArrayNumberValue(new Double[][] { new Double[] { (0.0196075) }, new Double[] { (0.384308) }, new Double[] { (0.756866) } });
    // テキスト装飾のRGB色値を設定します。
    attrs.setAttribute(textDecorationColor); // 構造属性にテキスト装飾の色属性を割り当てます。

    p2.appendChild(span1); // span1要素をp2に追加します。

    // pBdcでタグ付けされた新しいMCR要素を作成します。
    MCRElement mcr = p2.tag(pBdc);
    // MCRの親構造要素を取得し、レイアウト属性を作成します。
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // テキストの整列のための新しいStructureAttributeを作成します。
    StructureAttribute textAlign = new StructureAttribute(AttributeKey.TextAlign);
    textAlign.setNameValue(AttributeName.TextAlign_Center); // テキスト整列を中央に設定します。
    attrs.setAttribute(textAlign); // 構造属性にテキスト整列属性を割り当てます。

    // 要素の後にスペースを設定するための新しいStructureAttributeを作成します。
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(21.75); // スペース後の値を21.75単位に設定します。
    attrs.setAttribute(spaceAfter); // 構造属性にスペース後属性を割り当てます。

    // p2に追加するための新しいSpanElementを作成します。
    SpanElement span2 = tagged.createSpanElement();

    // スパン要素のための構造属性を作成します。
    StructureAttributes attrs = span2.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // テキスト装飾タイプの新しいStructureAttributeを作成します。
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // テキスト装飾を下線に設定します。
    attrs.setAttribute(textDecorationType); // 構造属性にテキスト装飾タイプ属性を割り当てます。

    // 指定されたキーを使用してテキスト装飾の色の新しいStructureAttributeを作成します。
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);

    // テキスト装飾の色属性の配列番号値を設定します。
    // 色はRGB値の配列で表され、各値はDoubleです。
    textDecorationColor.setArrayNumberValue(new Double[][] {
    new Double[] { (0.0196075) }, // 赤成分
    new Double[] { (0.384308) },  // 緑成分
    new Double[] { (0.756866) }   // 青成分
    });

    // textDecorationColor属性をattrsオブジェクトに設定します。
    attrs.setAttribute(textDecorationColor);

    // 親要素p2に子スパン要素を追加します。
    p2.appendChild(span2);

    // 2番目のリンクのための新しいLinkElementインスタンスを作成します。
    LinkElement link2 = tagged.createLinkElement();

    // ランダムに生成されたUUIDを使用してリンク要素に一意のIDを割り当てます。
    link2.setId(UUID.randomUUID().toString());

    // link2要素をspan2の子として追加します。
    span2.appendChild(link2);

    // ページの注釈からリンク2要素に対応する注釈をタグ付けします。
    link2.tag(page.getAnnotations().get_Item(1));

    // link2要素を追加のメタデータまたはコンテキスト（link2Bdc）でタグ付けします。
    link2.tag(link2Bdc);

    // 最初のリンクのための別のLinkElementインスタンスを作成します。
    LinkElement link1 = tagged.createLinkElement();

    // ランダムに生成されたUUIDを使用してlink1要素に一意のIDを割り当てます。
    link1.setId(UUID.randomUUID().toString());

    // link1要素をspan1の子として追加します。
    span1.appendChild(link1);

    // ページの注釈からlink1要素に対応する注釈をタグ付けします。
    link1.tag(page.getAnnotations().get_Item(2));

    // link1要素を追加のメタデータまたはコンテキスト（link1Bdc）でタグ付けします。
    link1.tag(link1Bdc);

    // タグ付きドキュメントのルート要素から最初の子要素を削除します。
    tagged.getRootElement().removeChild(0);

    // 指定された出力ディレクトリに"_out.pdf"というファイル名でドキュメントを保存します。
    document.save(dataDir + "_out.pdf");

```


## Aspose.PDF 24.6の新機能

バージョン24.6以降、Aspose.PDF for Javaはjava.security.cert.X509Certificate、java.security.PrivateKeyを使用してPDFに署名することができます：

このコードは証明書ストアから証明書と秘密鍵を取得し、それらを使用してPDFドキュメントの最初のページにデジタル署名を適用します。

```java

    KeyStore trustStore = KeyStore.getInstance("Windows");
    trustStore.load(null, null);
    java.security.cert.X509Certificate certificate = (java.security.cert.X509Certificate) trustStore.getCertificate("ProfMoriarty");
    PrivateKey key = (PrivateKey) trustStore.getKey("ProfMoriarty", null);

    PdfFileSignature pdfSign = new PdfFileSignature(getInputPdf());
    Signature signature = new ExternalSignature(certificate, key);
    pdfSign.sign(1, "reasonTest", "contactTest", "locationTest", true, new java.awt.Rectangle(1, 691, 100, 100), signature);

    pdfSign.save("PDFJAVA.pdf");
    pdfSign.close();
```

## Aspose.PDF 24.5の新機能

24.5リリース以降、フォームエディタプラグインが実装されました。

**フォームエディタを使用してPDFのフォームを編集する方法**

- ライセンスキーを設定します
- PDFフォームを操作するためのメソッドを提供するFormEditorクラスのインスタンスを作成します
- PDFドキュメントにフォームフィールドを追加するためのオプションを指定するFormEditorAddOptionsクラスのインスタンスを作成します
- ファイルパスやストリームを表すFileDataSourceクラスを使用して、FormEditorAddOptionsオブジェクトに入力ファイルソースと出力ファイルソースを追加します
- FormEditorオブジェクトのProcessメソッドを呼び出し、FormEditorAddOptionsオブジェクトをパラメータとして渡します
- ResultContainer.resultCollectionを使用して結果にアクセスします

```java

    // PDFファイルの入力パスと出力パスを指定します。
    String inputPath = "sample.pdf";
    String outputPath = "out.pdf";

    // FormEditorプラグインのインスタンスを作成します。
    FormEditor pdfFormPlugin = new FormEditor();

    // フォームフィールドを追加するためのオプションを作成します。
    ArrayList<FormFieldCreateOptions> options = new ArrayList<FormFieldCreateOptions>();

    // テキストボックスフォームフィールドを作成します。
    FormTextBoxFieldCreateOptions tmp1 = new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 600, 90, 610));
    tmp1.setValue("TextBoxField");
    tmp1.setColor(Color.getChocolate());
    tmp1.setPartialName("TexBoxField");
    options.add(tmp1);

    // コンボボックスフォームフィールドを作成します。
    FormComboBoxFieldCreateOptions tmp2 = new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 800, 350, 815));

    tmp2.setColor(com.aspose.pdf.Color.getRed());
    tmp2.setEditable(new Boolean[]{true});
    tmp2.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    ArrayList<String> list1 = new ArrayList<String>();
    list1.add("p1");
    list1.add("p2");
    list1.add("p3");
    tmp2.setOptions(list1);
    tmp2.setSelected(new Integer[]{2});
    tmp2.setPartialName("ComboBoxField");
    options.add(tmp2);

    // チェックボックスフォームフィールドを作成します。
    FormCheckBoxFieldCreateOptions tmp3 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715));
    tmp3.setValue("CheckBoxField 1");
    tmp3.setPartialName("CheckBoxField_1");
    tmp3.setColor(Color.getBlue());
    options.add(tmp3);

    // チェックボックスフォームフィールドを作成します。
    FormCheckBoxFieldCreateOptions tmp4 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(100, 700, 190, 715));
    tmp4.setChecked(new Boolean[]{true});
    tmp4.setValue("CheckBoxField 2");
    tmp4.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    tmp4.setStyle(new Integer[]{BoxStyle.Cross});
    options.add(tmp4);

    // チェックボックスフォームフィールドを作成します。
    FormCheckBoxFieldCreateOptions tmp5 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(200, 700, 390, 715));
    tmp5.setPartialName("CheckBoxField_3");
    tmp5.setValue("CheckBoxField 3");
    tmp5.setStyle(new Integer[]{BoxStyle.Star});
    tmp5.setChecked(new Boolean[]{true});
    tmp5.setTextHorizontalAlignment(new HorizontalAlignment[]{HorizontalAlignment.Center});
    options.add(tmp5);

    FormEditorAddOptions opt = new FormEditorAddOptions(options);

    // 入力ファイルと出力ファイルをオプションに追加します。
    opt.addInput(new FileDataSource(inputPath));
    opt.addOutput(new FileDataSource(outputPath));

    // プラグインを使用してフォームフィールドを処理します。
    ResultContainer results = pdfFormPlugin.process(opt);
```


このリリースでは、PDFレイヤーを操作することができます。例えば：

- PDFレイヤーをロックする
- PDFレイヤーの要素を抽出する
- レイヤードPDFをフラット化する
- PDF内のすべてのレイヤーを1つに統合する

**PDFレイヤーをロックする**

バージョン24.5以降、PDFを開き、最初のページの特定のレイヤーをロックし、変更を保存することができます。2つの新しいメソッドと1つのプロパティが追加されました：

Layer.Lock(); - レイヤーをロックします。
Layer.Unlock(); - レイヤーのロックを解除します。
Layer.Locked; - プロパティ、レイヤーのロック状態を示します。

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    Layer layer = page.getLayers().get(0);

    layer.lock();

    document.save(output);
```

**PDFレイヤーの要素を抽出する**

Aspose.PDF for Javaライブラリは、最初のページから各レイヤーを抽出し、それぞれのレイヤーを別々のファイルに保存することができます。

レイヤーから新しいPDFを作成するには、次のコードスニペットを使用できます：

```java

    Document document = new Document(inputPath);
    java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

    for (Layer layer : layers)
    {
        layer.save(outputPath);
    }
```


**PDFのレイヤーをフラット化する**

Aspose.PDF for Javaライブラリは、PDFを開き、最初のページの各レイヤーを反復処理して、各レイヤーをフラット化し、ページ上で永続的にします。

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);

    for (Layer layer : page.getLayers())
    {
        layer.flatten(true);
    }
    document.save(output);
```

Layer.flatten(boolean cleanupContentStream)メソッドは、コンテンツストリームからオプションのコンテンツグループマーカーを削除するかどうかを指定するブールパラメータを受け入れます。cleanupContentStreamパラメータをfalseに設定すると、フラット化のプロセスが高速化されます。

**PDF内のすべてのレイヤーを1つにマージする**

Aspose.PDF for Javaライブラリは、すべてのPDFレイヤーまたは特定のレイヤーを最初のページに新しいレイヤーとしてマージし、更新されたドキュメントを保存することを可能にします。

ページ上のすべてのレイヤーをマージするために、次の2つのメソッドが追加されました：

- void mergeLayers(String newLayerName);

- void mergeLayers(String newLayerName, String newOptionalContentGroupId);

2番目のパラメーターは、オプションのコンテンツグループマーカーの名前を変更することを可能にします。デフォルト値は "oc1" (/OC /oc1 BDC) です。

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    page.mergeLayers("NewLayerName");

    // または page.mergeLayers("NewLayerName", "OC1");

    document.save(output);
```

## Aspose.PDF 24.4の新機能

このリリースでは、PDF用のJavaプラグインが導入されました:

- フォームフラッターナープラグイン

```java

    FormFlattener pdfFormPlugin = new FormFlattener();

    FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

    opt.addInput(new FileDataSource("sample.pdf"));
    opt.addOutput(new FileDataSource("sample-flat.pdf"));

    ResultContainer result = pdfFormPlugin.process(opt);

    // 結果を確認します。
    java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- フォームエクスポーター

```java

    Rectangle rect = new com.aspose.pdf.Rectangle(0, 220, 600, 330);

    // プラグインの使用。
    FormExporter pdfFormPlugin = new FormExporter();
    SelectField selectField = new SelectField() {
      public boolean invoke(Field field) {
        return field instanceof TextBoxField && field.getPageIndex() == 2 && rect.isInclude(field.getRect(), 0);
      }
    };
    FormExporterValuesToCsvOptions opt = new FormExporterValuesToCsvOptions(selectField, ';');

    opt.addInput(new FileDataSource(inputFileNameWithFields));
    opt.addInput(new FileDataSource(getInputPath("document-1.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-2.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-3.pdf")));
    opt.addOutput(new FileDataSource(getOutputPath("out.csv")));
    ResultContainer result = pdfFormPlugin.process(opt);

    // 結果を確認します。
    System.out.println(result.getResultCollectionInternal().size() > 0);
    System.out.println(result.getResultCollectionInternal().get_Item(0).isFile());
    System.out.println(result.getResultCollectionInternal().get_Item(0).getData().toString());
```


- マージプラグイン

```java

    String input1 = "sample.pdf";
    String input2 = "sample.pdf";

    String output = "TestMergeFileAndStream_ResultAsFile.pdf";

    Merger merger = new Merger();

    MergeOptions opt = new MergeOptions();
    opt.addInput(new FileDataSource(input1));
    opt.addInput(new StreamDataSource(new FileInputStream(input2)));

    opt.addOutput(new FileDataSource(output));

    ResultContainer results = merger.process(opt);

    System.out.println(results.getResultCollection().size());
    System.out.println(results.getResultCollection().get(0).isFile());
```

- オプティマイザープラグイン

PDFドキュメントのサイズをどのようにして縮小するか？

```java

    String input = "Test.pdf";
    String output = "Optimized.pdf";

    Optimizer optimizer = new Optimizer();

    OptimizeOptions opt = new OptimizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    optimizer.process(opt);
```

PDFドキュメントのサイズをどのように変更するか？

```java

    String input = "sample.pdf";
    String output = "ResizeMain.pdf";

    Optimizer organizer = new Optimizer();

    ResizeOptions opt = new ResizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    opt.setPageSize(PageSize.getA1());

    organizer.process(opt);
```


PDFドキュメントを回転させる方法？

```java

    String input = "sample.pdf";
    String output = "OptimizerRotateMain.pdf";

    Optimizer optimizer = new Optimizer();

    RotateOptions opt = new RotateOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));
    opt.setRotation(Rotation.on90);

    ResultContainer results = optimizer.process(opt);
```

## Aspose.PDF 24.3の新機能

24.3から、TextFragmentAbsorberでフレーズのリストを検索する機能を実装。

```java

    String[] expressions = new String[] {
      //電話番号を検出
      "\\b\\d{3}-\\d{3}-\\d{4}\\b",
      //カード番号を検出
      "\\b(?:\\d[ -]*?){13,16}\\b"
    };
    Document document = new Document(input);

    TextFragmentCollection newTextFragmentCollection = new TextFragmentCollection();

    Pattern[] regexes = new Pattern[6];
    for (int i = 0; i < expressions.length; i++) {
      regexes[i] = Pattern.compile(expressions[i], Pattern.CASE_INSENSITIVE);
    }
    TextFragmentAbsorber newAbsorber = new TextFragmentAbsorber(regexes, new TextSearchOptions(true));
    document.getPages().accept(newAbsorber);
    HashMap < Pattern, TextFragmentCollection > map = newAbsorber.getRegexResults();
```


次の機能は、PDFからMarkdownへのコンバーターにテーブルを変換する機能を追加することです。

```java

    Document doc = new Document(dataDir + "56201.pdf");
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    doc.save(dataDir + "56201.md", saveOptions);
```

## Aspose.PDF 24.2の新機能

24.2からは、AcroFormsを使用してPDFに透かしを追加することが可能です。TextStampはAcroFormファイルでの使用に適しています。XFAファイルに対してTextStampを使用すると、通常のPDFファイルのようにページにテキストが描画されます（XFAファイルを読み取れないPDFビューア、たとえばChromeブラウザではこれが確認できます）。XFAファイルにテキストを追加するには、XFAファイルの内部XMLで変更する必要があります。

```java

    String sourceName = dataDir + "551.3xfa.pdf";
    String targetName = dataDir + "output_2_" + BuildVersionInfo.AssemblyVersion + ".pdf";

    Document pdfDocument = new Document(sourceName);
    XFA xfa = pdfDocument.getForm().getXFA();

    String watermark =
    "<subform>" +
    "<draw rotate=\"90\" x=\"100px\" y=\"100px\">" +
    "<value>" +
    "<text>Sample Stamp</text>\n" +
    "</value>" +
    "<font typeface=\"Arial\" size=\"14px\" weight=\"bold\" posture=\"italic\">" +
    "<fill>" +
    "<color value=\"0,128,0\"/>" +
    "</fill>" +
    "</font>" +
    "</draw>" +
    "</subform>";

    xfa.appendToTemplate("//tpl:pageArea", watermark);

    pdfDocument.save(targetName);
    pdfDocument.close();
```


状態モデルを注釈に設定する  
setReviewStateとsetMarkedStateをMarkupAnnotationクラスから使用して、必要な状態を設定することができます。  
すべてのマークアップ注釈には、利用可能な状態設定オプションがあります。

```java

    // ソースPDFドキュメントを開く
    Document pdfDocument = new Document();
    pdfDocument.getPages().add();
    // 注釈を作成
    TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.getPages().get_Item(1), new Rectangle(200,
            400, 400, 600));

    // 注釈のタイトルを設定
    textAnnotation.setTitle("サンプル注釈タイトル");

    // 注釈の件名を設定
    textAnnotation.setSubject("サンプル件名");
    // 注釈の内容を指定
    textAnnotation.setContents("注釈のサンプル内容");
    textAnnotation.setOpen(true);
    textAnnotation.setIcon(TextIcon.Key);
    com.aspose.pdf.Border border = new com.aspose.pdf.Border(textAnnotation);
    border.setWidth(5);
    border.setDash(new Dash(1, 1));
    textAnnotation.setBorder(border);
    String userName1 = "Aspose1";
    textAnnotation.setReviewState(AnnotationState.Rejected, userName1);
    textAnnotation.setRect(new Rectangle(200, 400, 400, 600));

    // 注釈をページの注釈コレクションに追加
    pdfDocument.getPages().get_Item(1).getAnnotations().add(textAnnotation);
    pdfDocument.processParagraphs();

    // 出力ファイルを保存
    pdfDocument.save(dataDir + "output_24_2_Rejected.pdf");

    pdfDocument = new Document(dataDir + "output" + version + "3.pdf");
    TextAnnotation textAnnotation2 = (TextAnnotation) pdfDocument.getPages().get_Item(1).getAnnotations().get_Item(1);

    String userName2 = "Aspose2";
    textAnnotation2.setReviewState(AnnotationState.Accepted, userName2);
    pdfDocument.save(dataDir + "output_24_2_Rejected_and_Accepted.pdf");
```


24.2からOFDからPDFへの変換を実装：

```java

    Document document = new Document(inputPath, new OfdLoadOptions());
    document.save(outputPath);
```

## Aspose.PDF 24.1の新機能

24.1リリースからPDFからMarkdownへの変換を実装：

```java

    final Document doc = new Document(inputPdfPath);
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
    doc.save(markdownOutputFilePath, saveOptions);
```

また、24.1ではInterruptMonitorを使用したスレッドの中断が実装されました。

```java

    final InterruptMonitor monitor = new InterruptMonitor();

    new Thread(new Runnable() {

      public void run() {

        InterruptMonitor.setThreadLocalInstance(monitor);
        Document document = new Document();

        try {
          Page page = document.getPages().insert(1);
          PageInfo pageInfo = page.getPageInfo();
          pageInfo.setLandscape(true);
          Table topicTable = new Table();
          topicTable.setBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setColumnWidths("5% 10% 5% 60% 10% 10%");
          topicTable.setRepeatingRowsCount(1);

          Row topicRow = topicTable.getRows().add();

          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");

          // foreachからwhileステートメントへの変換
          Iterator tmp0 = (topicRow.getCells()).iterator();
          while (tmp0.hasNext()) {
            Cell cell = (Cell) tmp0.next();
            cell.setVerticalAlignment(VerticalAlignment.Center);
            cell.setAlignment(HorizontalAlignment.Center);
          }

          Row row2 = topicTable.getRows().add();
          row2.getCells().add("text");
          row2.getCells().add("text");
          row2.getCells().add("text");
          String LongText = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.";
          row2.getCells().add(LongText);
          row2.getCells().add("text");
          row2.getCells().add("text");
          page.getParagraphs().add(topicTable);
          document.save(dataDir + "out" + version + ".pdf");

        } catch (com.aspose.pdf.exceptions.OperationCanceledException ex) {
          System.out.println("保存スレッドを中断しています: " + System.currentTimeMillis());
        } finally {
          if (document != null) {
            document.close();
          }
        }

      }

    }).start();

    System.out.println("プロセスがスレッドで開始しました: " + System.currentTimeMillis());

    // タイムアウトは、完全なドキュメントの保存に必要な時間（中断なし）より短くする必要があります。
    Thread.sleep(500);

    // プロセスを中断
    monitor.interrupt();

    System.out.println("保存スレッドを中断しました: " + System.currentTimeMillis());
```


## Aspose.PDF 23.12の新機能

フォームは以下のコードスニペットを使用して見つけることができ、テキストを置き換えることができます:

```java

    Document document = new Document(input);
    String expectedText = "これはKofx Power PDF Standardで新しいPDFを作成中に追加されたテキストです。";

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
      XForm form = (XForm) tmp0.next();
      if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(form);

        Iterator tmp1 = (absorber.getTextFragments()).iterator();
        while (tmp1.hasNext()) {
          TextFragment fragment = (TextFragment) tmp1.next();
          fragment.setText("");
        }
      }
    }

    document.save(output);
```            

または、フォームを完全に削除することもできます:

```java

    Document document = new Document(input);
    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    //foreachをwhile文に変換
    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
        XForm form = (XForm) tmp0.next();
        if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
            String name = forms.getFormName(form);
            forms.delete(name);
        }
    }

    document.save(output);
```


別の方法でフォームを削除する:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    for (int i = 1; i <= forms.size(); i++) {
        if ("Typewriter".equals(forms.get_Item(i).getIT()) && "Form".equals(forms.get_Item(i).getSubtype())) {
            forms.delete(forms.get_Item(i).getName());
        }
    }

    document.save(output);
``` 

- 次のコードスニペットを使用して、すべてのフォームを削除できます:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    forms.clear();

    document.save(output);
```

## Aspose.PDF 23.11の新機能

このリリースから、PDFファイルから隠しテキストを削除することが可能になりました:

```java

    Document document = new Document(inputFile);

    TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
    textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
    document.getPages().accept(textAbsorber);

    msStringBuilder result = new msStringBuilder();

    //foreachをwhile文に変換
    Iterator tmp0 = (textAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext()) {
            TextFragment fragment = (TextFragment) tmp0.next();
            if (fragment.getTextState().isInvisible()) {
                result.append(fragment.getText());
                fragment.setText("");
            }
        }

    document.save(outputFile);
```


## Aspose.PDF 23.10の新機能

現在のアップデートでは、タグ付きPDFからタグを削除する3つのバージョンを紹介します。

- ドキュメントの要素（ルートツリー要素）からいくつかのノード要素を削除する:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element documentElement = structure.getChildren().get_Item(0);
    Element structElement = (documentElement.getChildren().getCount() > 1) ?  documentElement.getChildren().get_Item(1) : null;
    documentElement.getChildren().remove(structElement);
    // structElement自体を削除することもできます
                //if (structElement != null)
                //{
                //    structElement.remove();
                //}
    document.save(outputPath);
```

- ドキュメントからすべてのマーク付き要素のタグを削除するが、構造要素は保持する:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root= structure.getChildren().get_Item(0);
    Queue<Element> queue = new ArrayDeque<Element>();
    queue.add(root);
    for (Element element : structure.getChildren() ) {
        queue.add(element);
        for (Element child : element.getChildren())
        {
            queue.add(child);
        }
    }
    for (Element element:queue ) {
        if (element instanceof TextElement  || element instanceof FigureElement)
            element.remove();
    }
    document.save(outputPath);
```


- タグをすべて削除します:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root = structure.getChildren().get_Item(0);
    root.remove();
    document.save(outputPath);
```

新機能として文字の高さを測定する機能を実装しました。以下のコードを使用して文字の高さを測定します:

```java

    Document doc = new Document("input.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.visit(doc.getPages().get_Item(1));
    double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```

測定は、文書に埋め込まれたフォントに基づいていることに注意してください。寸法に関する情報が欠落している場合、このメソッドは0を返します。

## Aspose.PDF 23.9の新機能

23.9からは、入力可能フィールドから子注釈を削除する機能をサポートします。

例1:

```java

    String input = "55343_1.pdf";
    Document doc = new Document(input);
    final String fieldName = "1 Vehicle Identification Number";
    Field field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
    Rectangle rect = field.getRect();
    doc.getForm().addFieldAppearance(field, 2, rect);
    System.out.println(2 == field.size());

    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(2 == field.size());
    doc.getForm().removeFieldAppearance(field, 1);

    System.out.println(0 == field.size());
    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
```


example 2:

```java

    {
    String option1 = "オプション 1";
    String option2 = "オプション 2";
    String outputPdf = "output.pdf";

    final Document document = new Document();
    try /*JAVA: 使用していました*/ {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

        // 最初のチェックボックスグループオプションの値を設定
        checkbox.setExportValue(option1);
        checkbox.addOption(option2);
        document.getForm().add(checkbox);
        java.util.List < String > tmp0 = new ArrayList < String > ();
        tmp0.add("Off");
        tmp0.add(option1);
        tmp0.add(option2);
        System.out.println(collectionAssert_AreEqual(tmp0, checkbox.getAllowedStates()));
        checkbox.setValue(option2);

        WidgetAnnotation f = document.getForm().get_Item(1);
        document.getForm().removeFieldAppearance((Field) f, 2);

        checkbox = (CheckboxField) document.getForm().get_Item(1);
        java.util.List < String > tmp1 = new java.util.ArrayList < String > ();
        tmp1.add("Off");
        tmp1.add(option1);
        System.out.println(collectionAssert_AreEqual(tmp1, checkbox.getAllowedStates()));

        document.save(outputPdf);
    } finally {
        if (document != null)(document).close();
    }
    }
    public static boolean collectionAssert_AreEqual(java.util.List < String > value1,
    java.util.List < String > value2) {
    if (value1.size() == value2.size()) {
        for (int i = 0; i < value1.size(); i++) {
        if (!value1.get(i).equals(value2.get(i)))
            return false;
        }
    } else {
        return false;
    }
    return true;
    }
```


ImageFilterType.Flateを使用して画像を追加すると、透明性が保持されません。

```java

    Document document = new Document();
    Page page = document.getPages().add();

    FileInputStream stream = new FileInputStream(("55037_1.png"));

    page.getResources().getImages().addWithImageFilterType(stream, ImageFilterType.Flate);
    page.getContents().add(new GSave());
    Rectangle rectangle = new Rectangle(413, 428, 548, 564);
    Matrix matrix = new Matrix(
      new double[] {
        rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY()
      });

    page.getContents().add(new ConcatenateMatrix(matrix));
    XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
    page.getContents().add(new Do(ximage.getName()));
    page.getContents().add(new GRestore());
    document.save(getOutputPath("55157.pdf"));
    stream.close();
```

## Aspose.PDF 23.8の新機能


PDF文書内のインクリメンタルアップデートを検出するための関数が23.8で追加されました。この関数は、ドキュメントがインクリメンタルアップデートで保存された場合は 'true' を返し、それ以外の場合は 'false' を返します。

```java

    Document doc = new Document(dataDir+"PDF_Support_Tech_Note.pdf");
    boolean not_updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(not_updatedIncrementally);

    doc.getPages().add();
    doc.saveIncrementally(dataDir+"PDF_updatedIncrementally.pdf");

    doc = new Document(dataDir+"PDF_updatedIncrementally.pdf");
    boolean updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(updatedIncrementally);
    doc.close();
```    

もう一つの機能は、入力PDFから出力PDFへのOutputIntentsのコピーです。

ドキュメント内の出力インテントにアクセスできるように、新しいパブリックプロパティDocument.getOutputIntents()を追加しました。現在のところ、既に何らかのドキュメントに存在する出力インテントの使用のみサポートされており、ユーザーが一からOutputIntentを作成することはできません。

```java

    Document document1 = new Document(dataDir+"pdfa.pdf");
    Document resultDocument = new Document();
    resultDocument.getPages().add(document1.getPages());

    for (OutputIntent intent : document1.getOutputIntents())
    {
        resultDocument.getOutputIntents().addItem(intent);
    }

    resultDocument.save(dataDir+"resultpath.pdf");
```  


Aspose.PDF 23.8から形状抽出のサポートを追加:

```java

{
    String input1 = getInputPdf("46298_1");
    String input2 = getInputPdf("46298_2");

    Document source = new Document(input1);
    Document dest = new Document(input2);

    Page destPage = dest.getPages().get_Item(1);

    TextFragmentAbsorber tfAbsorber = new TextFragmentAbsorber();
    tfAbsorber.visit(source.getPages().get_Item(1));

    //foreachをwhile文に変換
    Iterator tmp0 = ( tfAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext())
        {
            TextFragment textFragment = (TextFragment)tmp0.next();
            System.out.println(textFragment.getText());
            addTextImproved(destPage, textFragment);
        }

    ImagePlacementAbsorber imageAbsorber = new ImagePlacementAbsorber();
    imageAbsorber.visit(source);

    Iterator tmp1 = ( imageAbsorber.getImagePlacements()).iterator();
        while (tmp1.hasNext())
        {
            ImagePlacement image = (ImagePlacement)tmp1.next();
            destPage.addImage(image.getImage().toStream(), image.getRectangle());
        }

    GraphicsAbsorber vectorAbsorber = new GraphicsAbsorber();
    vectorAbsorber.visit(source.getPages().get_Item(1));
    Rectangle area = new Rectangle(90, 250, 300, 400);
    dest.getPages().get_Item(1).addGraphics(vectorAbsorber.getElements(), area);
    dest.save(getOutputPath("46298-out.pdf"));
    }

    private static void addTextImproved(Page page, TextFragment textFragment)
    {
        TextFragment local = new TextFragment();
        local.setPosition(textFragment.getPosition());

        // 元のPDFとページサイズが異なるため、新しい位置を再計算
        local.getPosition().setXIndent(textFragment.getPosition().getXIndent());//2.5 * 72;
        double newPageHeight = page.getPageRect(true).getHeight();
        double oldPageHeight = textFragment.getPage().getPageRect(true).getHeight();
        local.getPosition().setYIndent(textFragment.getPosition().getYIndent());

        local.setText(textFragment.getText());
        local.getTextState().setFont(textFragment.getTextState().getFont());
        local.getTextState().setFontSize(textFragment.getTextState().getFontSize());

        local.getTextState().setFormattingOptions(textFragment.getTextState().getFormattingOptions());
        local.getTextState().setForegroundColor(textFragment.getTextState().getForegroundColor());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(local);
    }
```


テキストを追加するときにオーバーフローを検出する機能もサポートしています:

```java

    Document doc = new Document();
    String paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
    Rectangle rectangle = new Rectangle(100, 600, 500, 700, false);
    TextParagraph paragraph = new TextParagraph();
    TextFragment fragment = new TextFragment(paragraphContent);
    paragraph.setVerticalAlignment(VerticalAlignment.Top);
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    paragraph.setRectangle(rectangle);
    boolean isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    while (!isFitRectangle)
    {
        fragment.getTextState().setFontSize(fragment.getTextState().getFontSize() - 0.5f);
        isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    }
    paragraph.appendLine(fragment);
    TextBuilder builder = new TextBuilder(doc.getPages().add());
    builder.appendParagraph(paragraph);
    doc.save(output);
```


## Aspose.PDF 23.7の新機能

23.7バージョンから、印刷ダイアログプリセットのページスケーリングをサポート：

```java

    Document document = new Document();
    document.getPages().add();
    document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
    document.save(outputPdf);

    Document documentOutput = new Document(outputPdf);
    int printScaling = documentOutput.getPrintScaling();
    System.out.println("PrintScaling: " + printScaling);
```

## Aspose.PDF 23.6の新機能

23.6バージョンから、HTMLやEpubページのタイトルを設定する機能を追加。

HTML用のコード：

```java

    HtmlSaveOptions options = new HtmlSaveOptions();
    options.setFixedLayout(true);
    options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
    options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
    options.setTitle("</title>NEW PAGE & TITILE</head>");

    Document document = new Document(inputPath);
    document.save(outPath, options);
```


EPUB用コード：

```java

    EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
    epubSaveOptions.setTitle("</title>NEW PAGE & TITILE</head>");
    epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

    Document document = new Document(inputPath);
    document.save(outPath, epubSaveOptions);
```

23.6からベクターグラフィックスの位置を決定するためのAPIを提供するサポート：

```java

    Document document = new Document(input);
    VectorGraphicsAbsorber vectorAbsorber = new VectorGraphicsAbsorber();
    vectorAbsorber.visit(document.getPages().get_Item(1));

    SubPath subPath1 = vectorAbsorber.getSubPaths().get_Item(2);
    SubPath subPath2 = vectorAbsorber.getSubPaths().get_Item(3);
    SubPath subPath3 = vectorAbsorber.getSubPaths().get_Item(4);

    Point point1 = new Point(subPath1.getPosition().getX() + 200, subPath1.getPosition().getY() - 100);
    Point point2 = new Point(subPath2.getPosition().getX() + 200, subPath2.getPosition().getY() - 100);
    Point point3 = new Point(subPath3.getPosition().getX() + 200, subPath3.getPosition().getY() - 100);

    subPath1.setPosition(point1);
    subPath2.setPosition(point2);
    subPath3.setPosition(point3);

    document.save(output);
```

## Aspose.PDF 23.1の新機能

23.1バージョンから、PrinterMark注釈の作成をサポートしました。注釈のバリアントの1つとして、ColorBarAnnotationを追加しました。

```java

    Document doc = new Document();
    Page page = doc.getPages().add();
    page.setTrimBox(new com.aspose.pdf.Rectangle(20, 20, 580, 820));
    Rectangle rectBlack = new com.aspose.pdf.Rectangle(100, 300, 300, 320);
    Rectangle rectCyan = new com.aspose.pdf.Rectangle(200, 600, 260, 690);
    Rectangle rectMagenta = new com.aspose.pdf.Rectangle(10, 650, 140, 670);

    ColorBarAnnotation colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    ColorBarAnnotation colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    ColorBarAnnotation colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.setColorOfCMYK(ColorsOfCMYK.Magenta);
    ColorBarAnnotation colorBarYellow = new ColorBarAnnotation(page, new com.aspose.pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.getAnnotations().add(colorBarBlack);
    page.getAnnotations().add(colorBarCyan);
    page.getAnnotations().add(colorBaMagenta);
    page.getAnnotations().add(colorBarYellow);
    doc.save("outFile.pdf");
```


## Aspose.PDF 22.12の新機能

このリリースから、PDFをDICOMイメージに変換するサポート:

```java
    DicomDevice device = new DicomDevice(PageSize.getA4());
    Document doc = new Document("Input.pdf");
    ByteArrayOutputStream stream = new ByteArrayOutputStream();
    device.process(doc.getPages().get_Item(1), stream);
```

## Aspose.PDF 22.9の新機能

22.09から、署名内で件名のルーブリックの順序を変更するプロパティを追加するサポート:

```java
    String inputPdf = getInputPath("input.pdf");
    String inputPfx = getInputPath("input.pfx");
    String outputPdf = getOutputPath("out.pdf");

    final PdfFileSignature fileSign = new PdfFileSignature();
    try 
    {
        fileSign.bindPdf(inputPdf);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 400, 100);
        PKCS7Detached signature = new PKCS7Detached(inputPfx, "123456789");
        signature.setDate(new Date());
        signature.setCustomAppearance( new SignatureCustomAppearance());
        signature.getCustomAppearance().setUseDigitalSubjectFormat(true);
        signature.getCustomAppearance().setDigitalSubjectFormat(new /*SubjectNameElements*/int[] { SubjectNameElements.CN, SubjectNameElements.O });

        fileSign.sign(1, true, rect, signature);
        fileSign.save(outputPdf);
    }
    finally { 
        if (fileSign != null) 
            fileSign.close(); 
    }
```

## Aspose.PDF 22.8の新機能

Aspose.PDF 23.8から、xrefテーブルを再構築するためのメソッドの追加がサポートされます：

```java

    PdfFileSanitization sanitizer = new PdfFileSanitization();
    try {
        sanitizer.bindPdf(dataDir + "50528_1.pdf");
        sanitizer.rebuildXrefAndTrailer();
        sanitizer.save(dataDir + "50528_1" + version + ".pdf");
    } finally {
        if (sanitizer != null) ( sanitizer).close();
    }
```

## Aspose.PDF 22.6の新機能

PDFからPDF_A_1Aへの変換で、出力ファイルサイズが大きくなるのを避けるために透明色を除去するオプションを実装しました。

バージョン22.5から、顧客は変換された透明性の品質とその結果としての出力ファイルサイズを制御できるようになりました：

```java
    opts.setTransparencyResolution(300);
```

## Aspose.PDF 22.5の新機能

PDF/A変換中に透明なコンテンツが削除され、画像に置き換えられます。 新機能を実装しました。これにより、顧客はTransparencyResolutionパラメータで画像の品質を制御できるようになりました：

```java

    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
    PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
    options.setTransparencyResolution(300);
    pdfDocument.convert(options);
    pdfDocument.save("finalOutput.pdf");
```


## Aspose.PDF 22.4の新機能

このリリースには、Aspose.PDF for Javaの情報が含まれています：

- PDFからODSへの変換: 上付き文字と下付き文字のテキストを認識;

**例**

```java

    Document pdfDocument = new Document("Superscript-Subscript.pdf");
    ExcelSaveOptions options = new ExcelSaveOptions();
    options.Format = ExcelSaveOptions.ExcelFormat.ODS;
    pdfDocument.Save("output.ods"), options);
```

- PDFからXMLSpreadSheet2003への変換: 上付き文字と下付き文字のテキストを認識;

- PDFからExcelへの変換: 上付き文字と下付き文字のテキストを認識;

## Aspose.PDF 22.3の新機能

PDFからODSへの変換: RTLのサポートはバージョン22.3で利用可能です

```java

    ExcelSaveOptions options = new ExcelSaveOptions();
    options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    pdfDocument.save("output.ods", options);
```

## Aspose.PDF 22.2の新機能

このリリースには、PDFからXSLXへの変換: RTL（ヘブライ語、アラビア語）のサポートが含まれています。

## Aspose.PDF 22.1の新機能

Aspose.PDF for Javaは、Portable Document Format (PDF) バージョン2.0のドキュメントのロードを可能にします。

## Aspose.PDF 21.10の新機能

### 隠しテキストを検出する方法は？

次のコードを使用してください:

```java

Document pdf = new Document(inFile);
        Page page = pdf.getPages().get_Item(1);
        TextFragmentAbsorber textFragmentAbsorber = new com.aspose.pdf.TextFragmentAbsorber();
        page.accept(textFragmentAbsorber);
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

        int fragmentsCount = textFragmentAbsorber.getTextFragments().size();
        int invisibleCount = 0;

        Iterator tmp0 = ( textFragmentCollection).iterator();
            while (tmp0.hasNext())
            {
                com.aspose.pdf.TextFragment fragment = (com.aspose.pdf.TextFragment)tmp0.next();
                System.out.println(fragment.getText());
                System.out.println(fragment.getTextState().isInvisible());
                if (fragment.getTextState().isInvisible())
                    invisibleCount++;
            }
```


## Aspose.PDF 21.8 の新機能

### デジタル署名のテキストカラーを変更する方法

21.8 バージョンでは、setForegroundColor によりデジタル署名のテキストカラーを変更できます:

```java
次のコードを使用してください:

                    PdfFileSignature pdfSign = new PdfFileSignature();                
                    pdfSign.bindPdf(inFile);
                    // 署名位置のための矩形を作成
                    java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);
                    PKCS7 pkcs = new PKCS7(inPfxFile, "");

                    pkcs.setCustomAppearance( new SignatureCustomAppearance());
// テキストカラーを設定
                    pkcs.getCustomAppearance().setForegroundColor(Color.getGreen());

                    // PDF ファイルに署名
                    pdfSign.sign(1, true, rect, pkcs);
                    // 出力 PDF ファイルを保存
                    pdfSign.save(outFile);
```

## Aspose.PDF 21.6 の新機能

### ドキュメントから ImagePlacementAbsorber を使用して画像を非表示にする方法

Aspose.PDF for Java を使用すると、ドキュメントから ImagePlacementAbsorber を使用して画像を非表示にできます:

```java
      Document doc = new Document("input.pdf");

        for (Page page : doc.getPages()) {
            ImagePlacementAbsorber ipa = new ImagePlacementAbsorber();
            ipa.visit(page);
            for (ImagePlacement ip : ipa.getImagePlacements()) {
                ip.hide();
            }
        }

        doc.save("out.pdf");
```

## Aspose.PDF 21.5 の新機能

### 画像を結合するための API を追加

Aspose.PDF 21.4 では、画像を結合することができます。画像ストリームのリストを1つの画像ストリームとして結合します。Png/jpg/tiff の出力形式がサポートされており、非対応の形式を使用した場合、出力ストリームはデフォルトで Jpeg としてエンコードされます。
次のコードスニペットに従ってください:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile300dpi = new FileInputStream("image1.jpg");
        try  {
            inputImagesStreams.add(inputFile300dpi);
            InputStream inputFile600dpi = new FileInputStream("image2.jpg");
            try {
                inputImagesStreams.add(inputFile600dpi);
                inputStream = PdfConverter.mergeImages(
                        inputImagesStreams,
                        com.aspose.pdf.ImageFormat.Jpeg,
                        ImageMergeMode.Vertical,
                        new Integer(1),
                        new Integer(1)
                );
            } finally {
                if (inputFile600dpi != null) (inputFile600dpi).close();
            }
        } finally {
            if (inputFile300dpi != null) (inputFile300dpi).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out.pdf");
        inputStream.close();
```


Also you may merge you images as Tiff format:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile1 = new FileInputStream("1.tif");
        try  {
            inputImagesStreams.add(inputFile1);
            InputStream inputFile2 = new FileInputStream("2.tif");
            try {
                inputImagesStreams.add(inputFile2);
                inputStream = PdfConverter.mergeImagesAsTiff(inputImagesStreams);
            } finally {
                if (inputFile2 != null) (inputFile2).close();
            }
        } finally {
            if (inputFile1 != null) (inputFile1).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out2.pdf");
        inputStream.close();
```

## Aspose.PDF 21.02の新機能について

Aspose.PDF v21.02 PAdES LTV署名でPDFに署名する

```java
final Document document = new Document(inputPdf);
    try 
    {
        PdfFileSignature signature = new PdfFileSignature(document);
        PKCS7 pkcs7 = new PKCS7(getInputPath("cert.pfx"), "password");
        //PAdES LTV署名でPDFに署名する
        pkcs7.setUseLtv(true);

        signature.sign(1, true, new Rectangle(100, 100, 300, 300), pkcs7);
        signature.save(outputPdf);
    }
    finally { if (document != null) (document).dispose(); }
```