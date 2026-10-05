---
title: 新着情報
linktitle: 新着情報
type: docs
weight: 10
url: /ja/java/whatsnew/
description: このページでは、最近のリリースで導入された Aspose.PDF for Java の最も人気のある新機能をご紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java の人気の新機能
Abstract: Aspose.PDF for Java ドキュメントの What\u0432\u0402\u2122s New セクションは、最近のリリースで導入された最新の更新、強化、およびバグ修正の概要を提供します。新機能、パフォーマンス向上、互換性の更新がハイライトされ、開発者が PDF 処理の最新の進歩について情報を得られるよう支援します。ドキュメントには、廃止された機能と推奨される代替手段の詳細も含まれています。このセクションを定期的に確認することで、開発者は Java アプリケーションで最も効率的かつ最新の機能を活用し、シームレスな PDF 管理を実現できます。
SoftwareApplication: java
---
## Aspose.PDF 25.12 の新機能

### XFDF内の任意の回転を持つフリーテキスト注釈

XFDF の Free Text アノテーションに任意の回転角度のサポートが追加され、インポートおよびエクスポートされたアノテーションレイアウトがより柔軟になりました。

```java
Document pdfDocument = new Document(inputPdf);
com.aspose.pdf.facades.PdfAnnotationEditor editor = new PdfAnnotationEditor();
editor.bindPdf(pdfDocument);
editor.importAnnotationsFromXfdf(inputXfdf);
editor.save(output);
```

## Aspose.PDF 25.11 の新機能は何ですか

### 非表示データのサニタイズ改善

HiddenDataSanitizer を使用した強化された PDF サニタイズが利用可能になり、ドキュメントからの隠しコンテンツの除去が向上します。

```java
Document document = new Document(pdfFile);
    try
    {
        HiddenDataSanitizationOptions options = HiddenDataSanitizationOptions.all();
        ImageCompressionOptions tmp = new ImageCompressionOptions();
        tmp.setMaxResolution(30);
        tmp.setResizeImages(true);
        tmp.setCompressImages(true);
        options.setImageCompressionOptions(tmp);
        HiddenDataSanitizer sanitizer = new HiddenDataSanitizer(options);
        sanitizer.sanitize(document);
        document.save(getOutputPath("clear_all_resize_img.pdf"));
    }
    finally
    {
        document.close();
    }
```

### PDF最適化中のファイルサイズ削減の改善

PDFの最適化は、フォントのサブセット化の処理方法を改善することで、ファイルサイズの削減をさらに向上させます。

```java
Document document = new Document(inputPath);
    try {
        OptimizationOptions tmp = new OptimizationOptions();
        tmp.setSubsetFonts(true);
        tmp.setAllowReusePageContent(true);
        tmp.setCompressObjects(true);
        tmp.setLinkDuplicateStreams(true);
        tmp.setRemoveUnusedObjects(true);
        tmp.setRemoveUnusedStreams(true);
        tmp.setCompressAllContentStreams(true);
        OptimizationOptions optimizeOptions = tmp;

        document.optimizeResources(optimizeOptions);
        document.save(outputPath);
    } finally {
        document.close();
    }
```

## Aspose.PDF 25.10 の新機能

### PDF から PDF/E への変換サポート

Aspose.PDF for Java は、PDF ドキュメントを PDF/E フォーマットに変換できるようになりました。

```java
Document document = new Document(inputPdf);
document.convert(conversionLog, PdfFormat.PDF_E_1, ConvertErrorAction.Delete);
document.save(outputPdf);
```

### 注釈内のHTMLテキスト

アノテーション内にHTMLテキストを追加するためのサポートが追加されました。

```java
Document pdf = new Document();
    Page page = pdf.getPages().add();
    DefaultAppearance da = new DefaultAppearance("Arial", 12, java.awt.Color.BLACK);
    FreeTextAnnotation freeTextAnnot = new FreeTextAnnotation(page, new Rectangle(100, 600, 500, 700),
            da);
    freeTextAnnot.setRichText("<?xml version=\"1.0\"?><body xmlns=\"http://www.w3.org/1999/xhtml\" "
            + "xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\\\" xfa:APIVersion=\"Acrobat:11.0.23\" "
            + "xfa:spec=\"2.0.2\"  style=\"font-size:12.0pt;color:#00eeff;font-weight:normal;font-style:normal;"
            + "font-family:Arial;font-stretch:normal\"><p dir=\"ltr\">1<p style=\"color:#00ff00;"
            + "font-style:italic\">2</p>3456</p></body>");
    freeTextAnnot.getTextStyle().setColor(java.awt.Color.BLACK);
    freeTextAnnot.getTextStyle().setFontName("Arial");
    //freeTextAnnot.Contents = "This is a rich text";
    freeTextAnnot.setModified(new Date());
    freeTextAnnot.setColor(Color.getRed());
    freeTextAnnot.getBorder().setWidth(0);
    page.getAnnotations().add(freeTextAnnot);
    pdf.save(getOutputPath("out1.pdf"));
```

## Aspose.PDF 25.9 の新機能

### HTML to PDF プラグイン

Aspose.PDF for Javaには、HTMLからPDFへの変換ワークフローを簡素化するHtml to Pdf Pluginsが含まれています。

```java
// Specify the input and output file paths.
String inputPath = "sample.pdf";
String outputPath = "sample.html";

// Create an instance of the PdfHtmlplugin.
PdfHtml converter = new PdfHtml();

// Create an instance of the HtmlToPdfOptionsclass.
HtmlToPdfOptions options = new HtmlToPdfOptions();

// Add the input and output file paths to the options.
options.addInput(new FileDataSource(inputPath));
options.addOutput(new FileDataSource(outputPath));

// Process the PDF to HTML conversion using the plugin and options.
ResultContainer htmlResultContainer = converter.process(options);

// Get the result from the result container.
IOperationResult result = htmlResultContainer.getResultCollectionInternal().get_Item(0);
```

### PDF 1.6 準拠サポート

PDF 1.6 の適合性サポートが、このドキュメントバージョンを必要とするシナリオ向けに追加されました。

## Aspose.PDF 25.8 の新機能

### テーブル境界線スタイルのサポート

テーブルの境界線スタイルのサポートが追加され、テーブルの外観をより細かく制御できるようになりました。

```java
Document document = new Document();
    try {
        Page page = document.getPages().add();

        GraphInfo tmp = new GraphInfo();
        tmp.setDashArray(new int[]{10, 10});
        tmp.setDashPhase(5);
        tmp.setLineWidth(3);
        Table tmp_1 = new Table();
        tmp_1.setBorder(new BorderInfo(BorderSide.Box, tmp));
        tmp_1.setDefaultCellBorder(new BorderInfo(BorderSide.Box, .05f, Color.getWhite()));
        tmp_1.setDefaultCellPadding(new MarginInfo(4.5, 3, 4.5, 3));
        tmp_1.getDefaultCellTextState().setFont(FontRepository.findFont("Arial"));
        tmp_1.getDefaultCellTextState().setFontSize(10);
        tmp_1.getDefaultCellTextState().setHorizontalAlignment(HorizontalAlignment.Left);
        tmp_1.getDefaultCellTextState().setForegroundColor(Color.getBlack());
        Table table1_allSidesSet = tmp_1;
        page.getParagraphs().add(table1_allSidesSet);

        for (int i = 0; i < 10; i++) {
            Row newRow = table1_allSidesSet.getRows().add();
            Cell cellLvl1 = newRow.getCells().add(String.valueOf(i));
        }

        Table tmp_2 = new Table();
        tmp_2.setBorder(new BorderInfo(BorderSide.Box, 1));
        tmp_2.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.05f, Color.getWhite()));
        tmp_2.setDefaultCellPadding(new MarginInfo(4.5, 3, 4.5, 3));
        tmp_2.getDefaultCellTextState().setFont(FontRepository.findFont("Arial"));
        tmp_2.getDefaultCellTextState().setFontSize(10);
        tmp_2.getDefaultCellTextState().setHorizontalAlignment(HorizontalAlignment.Left);
        tmp_2.getDefaultCellTextState().setForegroundColor(Color.getBlack());

//Style1 example
        Table table2_onlyRightSideSet = tmp_2;
        table2_onlyRightSideSet.getBorder().getRight().setDashArray(new int[]{5, 10});
        table2_onlyRightSideSet.getBorder().getRight().setDashPhase(7);
        page.getParagraphs().add(table2_onlyRightSideSet);
//Style2 example
//                Table table3_roundCorner= tmp_2;
//                table3_roundCorner.setCornerStyle(BorderCornerStyle.Round);
//                table3_roundCorner.getBorder().setRoundedBorderRadius(15);
//                page.getParagraphs().add(table3_roundCorner);

        for (int i = 0; i < 10; i++) {
            Row newRow = table2_onlyRightSideSet.getRows().add();
            Cell cellLvl1 = newRow.getCells().add(String.valueOf(i));
        }

        document.save(output);
    } finally {
        if (document != null) {
            document.close();
        }
    }
```

### PDF 内の画像の ALT テキスト抽出

PDF ドキュメント内の画像に対して ALT テキストの説明を取得できるようになり、アクセシビリティ志向の処理に役立ちます。

```java
Document doc = new Document("input.pdf");
    try  {
        // Create ImagePlacementAbsorber object to perform image placement search
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Accept the absorber for all the pages
        doc.getPages().accept(abs);

        // Loop through all ImagePlacements, get image and ImagePlacement Properties
        ImagePlacement imagePlacement = abs.getImagePlacements().get_Item(1);
        {
            // Get the image using ImagePlacement object
            XImage image = imagePlacement.getImage();
            List<String> altTexts = image.getAlternativeText(imagePlacement.getPage());
            System.out.println(altTexts.get(0));
        }
    } finally {
        if (doc != null)
            doc.close();
    }
```

## Aspose.PDF 25.7 の新機能

### PDF ChatGPT プラグイン

Aspose.PDF for Java は現在、PDF に焦点を当てた AI インタラクションシナリオ向けの PDF ChatGPT Plugin を含んでいます。

この例では、ファイルをメッセージ ソースとして追加することで PdfChatGpt プラグインの使用方法を示しています:

```java
PdfChatGpt plugin = new PdfChatGpt();
PdfChatGptRequestOptions options = new PdfChatGptRequestOptions();
options.addOutput(new FileDataSource("PdfChatGPT_output.pdf")); // Add the output file path.
// Add the PDF text source.
// In case of multiple sources, the text from each document will be added to the request message collection
// as a separate message with the role "user".
options.addInput(new FileDataSource("TextSource.pdf"));
options.setApiKey("Your API key.");  // You need to provide the key to access the API.
options.setMaxTokens(1000); // The maximum number of tokens to generate in the chat completion.
// Add the request message.
// In this case, the system message with Content = "You are a helpful assistant." is added by default.
// The role of the query message is "user" by default.
options.setQuery("How many letters in the provided text?");
// Process the request.
ResultContainer result = plugin.process(options);
String fileResultPath = result.getResultCollection().get(0).getData().toString();
ChatCompletion chatCompletionObject = (ChatCompletion)result.getResultCollection().get(1).getData();
```

この例は、リクエストにメッセージを追加することで PdfChatGpt プラグインの使用方法を示しています:

```java
PdfChatGpt plugin = new PdfChatGpt();
PdfChatGptRequestOptions options = new PdfChatGptRequestOptions();
options.addOutput(new FileDataSource("PdfChatGPT_output.pdf")); // Add the output file path.
options.setApiKey("Your API key."); // You need to provide the key to access the API.
options.setMaxTokens(1000); // The maximum number of tokens to generate in the chat completion.
// Add the request messages.
Message message1 = new Message() ;
message1.setContent("You are a helpful assistant.");
message1.setRole(Role.System);
options.getMessages().add(message1);

Message message2 = new Message() ;
message2.setContent("What is the biggest pizza diameter ever made?");
message2.setRole(Role.User);
options.getMessages().add(message2);

// Process the request.
ResultContainer result = plugin.process(options);
String fileResultPath = result.getResultCollection().get(0).getData().toString();
ChatCompletion chatCompletionObject = (ChatCompletion)result.getResultCollection().get(1).getData(); // The ChatGPT API chat completion object.
```

この例は、リクエストに 1 つのメッセージを追加して PdfChatGpt プラグインを使用する方法を示しています：

```java
PdfChatGpt plugin = new PdfChatGpt();
PdfChatGptRequestOptions options = new PdfChatGptRequestOptions();
options.addOutput(new FileDataSource("PdfChatGPT_output.pdf")); // Add the output file path.
options.setApiKey("Your API key."); // You need to provide the key to access the API.
options.setMaxTokens(1000); // The maximum number of tokens to generate in the chat completion.
// Add the request message.
// In this case, the system message with Content = "You are a helpful assistant." is added by default.
// The role of the query message is "user" by default.
options.setQuery("What is the lowest temperature recorded on the Earth?");
// Process the request.
ResultContainer result = plugin.process(options);
String fileResultPath = result.getResultCollection().get(0).getData().toString();
ChatCompletion chatCompletionObject = (ChatCompletion)result.getResultCollection().get(1).getData(); // The ChatGPT API chat completion object.
```

## Aspose.PDF 25.6 の新機能

### 改善された PDF から DOCX への出力書式

PDFからDOCXへの変換は、以前出力形式が正しくなかった文書に対して改善されました。

```java
Document doc = new Document(dataDir + "SD_Aspose.pdf");
DocSaveOptions saveOption = new DocSaveOptions();
saveOption.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
saveOption.setFormat(DocSaveOptions.DocFormat.DocX);
saveOption.setRecognizeBullets(true);
doc.save(dataDir + "SD_Aspose.docx", saveOption);
```

## Aspose.PDF 25.5 の新機能

### PDF から ODS への変換で画像を保持

PDF ドキュメントを ODS に変換する際に、画像が保持されるようになりました。

```java
Document doc = new Document("input.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
doc.save("output.ods", options);
```

### PDFからPDF/Aへの変換中の自動タグ作成

PDFからPDF/Aへの変換は、出力文書のタグ付け結果を向上させるために自動タグ作成をサポートするようになりました。

```java
Document document = new Document(dataDir+"source.pdf");

PdfFormat format = PdfFormat.PDF_A_1A;
PdfFormatConversionOptions options = new PdfFormatConversionOptions(format, ConvertErrorAction.Delete);
options.setAutoTaggingSettings(AutoTaggingSettings.getDefault());

document.convert(options);
document.save(dataDir+"out_"+BuildVersionInfo.ASSEMBLY_VERSION+"_"+format+"_"+document.getFileName());
document.close();
```

## Aspose.PDF 25.4 の新機能

### PDF から XLSX への変換でハイパーリンクを保持する

PDF 文書を XLSX に変換する際にハイパーリンクが保持されるようになり、エクスポートされたスプレッドシートでのナビゲーションが向上します。

```java
Document doc = new Document("input.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
doc.save("output.xlsx", options);
```

## Aspose.PDF 25.3 の新機能

バージョン 25.2 から PDF デジタル署名の改ざん検出機能が追加されました。デジタル署名の改ざんを検証するには、‘SignaturesCompromiseDetector’ クラスを使用できます。check() メソッドを呼び出して、documentвЂ™s の署名をチェックします。署名の改ざんが検出されない場合、メソッドは true を返します。既存の署名が文書全体をカバーしているか確認するには、‘SignaturesCoverage property’ を使用します。

```java
void check(String pdfFile) {
    final Document document = new Document(pdfFile);
    try {
        SignaturesCompromiseDetector detector = new SignaturesCompromiseDetector(document);

        CompromiseCheckResult result = null;
        CompromiseCheckResult[] referenceToResult = {result};
        System.out.println(detector.check(referenceToResult));
        if (detector.check(referenceToResult)){
            System.out.println("No signature compromise detected");
        }
        result = referenceToResult[0];
        System.out.println(SignaturesCoverage.PartiallySigned == result.getSignaturesCoverage());
        System.out.println(result.hasCompromisedSignatures());
    } finally {
        if (document != null) {
            (document).close();
        }
    }
}
```

## Aspose.PDF 25.2 の新機能

25.2でPDFをPDF/X-4ファイル形式に変換する機能が追加されました：

```java
String iccProfile = "PSO_MFC_Paper_eci";
String outputConditionIdentifier = "FOGRA41";
String inputPdf= dataDir + "PDFToPDFX.pdf";
String outputPdf= dataDir + "PDFToPDFX_out.pdf";
PdfFormat format = PdfFormat.PDF_X_4;

Document document = new Document(inputPdf);
PdfFormatConversionOptions options = new PdfFormatConversionOptions(format, ConvertErrorAction.Delete);
options.setIccProfileFileName(dataDir + iccProfile + ".icc");
options.setOutputIntent(new OutputIntent(outputConditionIdentifier));

document.convert(options);
document.save(outputPdf);
```

バージョン25.2以降、出力HTMLを中央揃えにすることが可能になりました：

```java
Document doc = new Document(dataDir + "pdf_sample.pdf");
// Instantiate HTML Save options object
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Enable option to embed all resources inside the HTML
newOptions.PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml;

// This is just optimization for IE and can be omitted
newOptions.LettersPositioningMethod = LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss;
newOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;
newOptions.FontSavingMode = HtmlSaveOptions.FontSavingModes.SaveInAllFormats;
newOptions.AntialiasingProcessing = HtmlSaveOptions.AntialiasingProcessingType.TryCorrectResultHtml;
newOptions.setSplitIntoPages(false);// force write HTMLs of all pages into one output document
newOptions.setUseZOrder(true);

com.aspose.pdf.SaveOptions.BorderPartStyle style = new com.aspose.pdf.SaveOptions.BorderPartStyle();
style.LineType = com.aspose.pdf.SaveOptions.HtmlBorderLineType.Solid;
style.color = java.awt.Color.BLACK;
style.setWidthInPoints(1);
newOptions.PageBorderIfAny = new com.aspose.pdf.SaveOptions.BorderInfo(style);
doc.save(dataDir + "HTML_19.6.html", newOptions);
```

また、バージョン 25.2 以降、Aspose.PDF を使用してフォントとサイズが指定されたテキストの上昇量と下降量を取得できるようになりました。この新機能はクラス 'com.aspose.pdf.Font' に実装されています。

追加されたメソッド:

**最大上昇点を測定**

-public double getAscentPoint(String str, float fontSize)

**最大降下点を測定します**

- public double getDescentPoint(String str, float fontSize)

```java
String someText = "Testing text";
float fontSize = 10;
TextFragment tf = new TextFragment(someText);
Font f1 = tf.getTextState().getFont();

double getWidthPoint = f1.measureString(someText, fontSize);
double getAscentPoint = f1.getAscentPoint(someText, fontSize);
double getDescentPoint = f1.getDescentPoint(someText, fontSize);

System.out.println(f1.getFontName());
System.out.println(getWidthPoint);
System.out.println(getAscentPoint);
System.out.println(getDescentPoint);
```

## Aspose.PDF 25.1 の新機能

PDF/X および PDF/A 変換のために外部 ICC プロファイルへのパスを渡す機能は、数年前からライブラリに存在しており、PdfFormatConversionOptions.IccProfileFileName プロパティによって有効になっています。現在、OutputIntent クラスのオブジェクトを使用して OutputIntent プロパティを埋めるデータを渡すことも可能です。

次のスニペットは、アノテーション文書をアノテーション FOGRA39 ICC プロファイルを使用して PDF/X-1 に変換する方法を示しています:

```java
String iccProfile = "Coated_Fogra39L_VIGC_300.icc";
String outputConditionIdentifier = "FOGRA39";

Document pdfDocument = new Document("58191_1.pdf");
    try {
        PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.log", PdfFormat.PDF_X_1A, ConvertErrorAction.Delete);
        options.setIccProfileFileName(iccProfile);
        options.setOutputIntent(new OutputIntent(outputConditionIdentifier));
        pdfDocument.convert(options);
        pdfDocument.save("42686_1_PDF_X_1A.pdf");
    } finally {
        if (pdfDocument != null) {
            pdfDocument.dispose();
        }
    }
```

25.1 では、ドキュメントを使用する際に特権情報を取得する機能が追加されました:

```java
Document document = new Document();
document.getPages().add();
    try
    {
        PdfFileInfo info = new PdfFileInfo();
        info.bindPdf(document);
        DocumentPrivilege privilege = info.getDocumentPrivilege();
        System.out.println(2 == privilege.getCopyAllowLevel());
        System.out.println(2 == privilege.getPrintAllowLevel());
        System.out.println(-1 == privilege.getChangeAllowLevel());

        privilege.setCopyAllowLevel(0);
        privilege.setCopyAllowLevel(1);
        privilege.setCopyAllowLevel(2);

        privilege.setPrintAllowLevel(0);
        privilege.setPrintAllowLevel(1);
        privilege.setPrintAllowLevel(2);

        privilege.setChangeAllowLevel(0);
        privilege.setChangeAllowLevel(1);
        privilege.setChangeAllowLevel(2);
        privilege.setChangeAllowLevel(3);
        privilege.setChangeAllowLevel(4);

        PdfFileSecurity fs = new com.aspose.pdf.facades.PdfFileSecurity(document, dataDir + "out_new_Doc"+version+".pdf");
        fs.setPrivilege(privilege);
    }
    finally {
        if (document != null) document.dispose();
        }
```

## Aspose.PDF 24.12 の新機能

バージョン24.12以降、サロゲートペア文字のサポートが可能になっています。

「surrogate pair」という用語は、UTF-16エンコーディング方式で高いコードポイントを持つUnicode文字をエンコードすることを指します。

```java
String surrogate_pair  = "рџЊ‰";
    System.out.println(surrogate_pair.length());//==2
    Document doc = new Document();
    Page p = doc. getPages().add();
//add the path to the required fonts that contains surrogate pair characters
    FontRepository.addLocalFontPath("C:\\Fonts\\Noto_Emoji");
    Font f = FontRepository.findFont("Noto Emoji");
    System.out.println(f.doesFontContainAllCharacters(surrogate_pair));
    TextFragment textFragment = new TextFragment();
    TextSegment segment = new TextSegment(surrogate_pair);
    segment.getTextState().setFont(f);
    textFragment.setText(surrogate_pair);
    textFragment.getSegments().add(segment);

    p.getParagraphs().add(textFragment);
    doc.save(dataDir + "out_24_11_.pdf");
```

バージョン24.12以降、PDF文書をPDF/A-4に変換できるようになりました。PDF 2.0をベースとした標準の第4部は、2020年後半に公開されました。

以下のコードスニペットは、入力ドキュメントが PDF 2.0 より以前のバージョンである場合に、ドキュメントを PDF/A-4 形式に変換する方法を示しています。

```java
Document document = new Document(inputPdf);
// Only PDF-2.x documents can be converted to PDF/A-4
document.convert("log1.xml", PdfFormat.v_2_0, ConvertErrorAction.Delete);
document.save(tmpOutputFile);

document = new Document(tmpOutputFile);
document.convert("log2.xml", PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
document.save("output.pdf");
```

## Aspose.PDF 24.9 の新機能は何ですか

このリリースでは、低レベルの関数を使用してアクセシブルな PDF を作成することが可能です:

次のコードスニペットは、PDFドキュメントとそのタグ付けされたコンテンツで動作し、Aspose.PDF ライブラリを使用して処理します。

```java
//Create template document with simple text
Document documentTemp = new Document();
        Page page = documentTemp .getPages().add();
        TextFragment fragment = new TextFragment("Helloworld");
        page.getParagraphs().add(fragment);
        documentTemp .save(output);

//Add tag to the text in the document
Document document = new Document(output);
        OperatorCollection operators = document.getPages().get_Item(1).getContents();
        for (int i = 1; i <= operators.size(); i++) {
            Operator op = operators.get_Item(i);
            if (op instanceof BT) {
                BDC bdc = new BDC("P", new BDCProperties(new Integer[]{1}, "ru", "Hello world"));
                operators.insert(i - 1, bdc);
                i += 1;
            }

            if (op instanceof ET) {
                operators.insert(i + 1, new EMC());
                i += 1;
            }
        }

        ITaggedContent content = document.getTaggedContent();
        SpanElement span = content.createSpanElement();
        content.getRootElement().appendChild(span);
        for (Operator op :  operators) {
            if (op instanceof BDC) {
                BDC bdc = (BDC)op;
                if (bdc != null) {
                    span.tag(bdc);
                }
            }
        }

        document.save(output);
```

その `GraphicalPdfComparer` PDF ドキュメントとページのグラフィック比較のためにクラスが追加されました。グラフィック比較はドキュメントページ画像を扱います。結果は as an として返されます。 `ImagesDifference` オブジェクトまたは元の画像と差分を結合した画像を含むPDF文書としてです。グラフィック比較は、テキストやグラフィックコンテンツにわずかな差異がある文書に最も有用です。

次のコードスニペットは、2つの PDF ドキュメントのグラフィック比較を実演し、差分を含む画像を結果の PDF ドキュメントに保存します：

```java
GraphicalPdfComparer comparer = new GraphicalPdfComparer();
    comparer.setThreshold(3.0);
    comparer.setColor(Color.getRed());
    comparer.setResolution(new Resolution(300));

    Document doc1 = new Document(dataDir+"graph_compare.pdf");
    Document doc2 = new Document(dataDir+"graph_compare_.pdf");
    comparer.compareDocumentsToPdf(doc2, doc1, dataDir+"graph_compare_24_9__.pdf");
    doc1.close();
    doc2.close();
```

## Aspose.PDF 24.8 の新機能

24.8以降、PDF/A-4形式のサポート:

```java
Document document = new Document(inputPdf);
// Only PDF-2.x documents can be converted to PDF/A-4
document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
document.save(outputFile);
```

また、Image Stamp の代替テキストを追加することは可能ですか：

ImageStamp に AlternativeText プロパティが追加されました。値が割り当てられた場合、ドキュメントに ImageStamp を追加するときに代替テキストが設定されます。

```java
String p1_Alt1 = "*** page 1, Alt text 1 ***",
                p1_Alt2 = "*** page 1, Alt text 2 ***",
                p2_Alt1 = "--- page 1, Alt text 1 ---",
                p2_Alt2 = "--- page 1, Alt text 2 ---";

StructTreeRootElement structTreeRoot = document.getTaggedContent().getStructTreeRootElement();

ImageStamp imageStamp = new ImageStamp(dataDir + "test.jpg");
imageStamp.setXIndent(100);
imageStamp.setYIndent(700);
imageStamp.setWidth(50);
imageStamp.setHeight(50);
imageStamp.setQuality(100);
imageStamp.setAlternativeText(p1_Alt1);

// To page 1
document.getPages().get_Item(1).addStamp(imageStamp);

imageStamp.setYIndent(500);
imageStamp.setAlternativeText(p1_Alt2);
document.getPages().get_Item(1).addStamp(imageStamp);

// To page 2
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

// Save document
document.save(outFile);
```

また、以下のコードは FigureElements 内の既存画像に AlternativeText を追加する方法を示しています。

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

        // Set Alternative Text
        figureElement.setAlternativeText("Figure alternative text (technique 1)");
    }
}

// Save document
document.save(outFile);
```

## Aspose.PDF 24.7 の新機能

24.7 リリース以降、タグ付けされた PDF の編集の一環として、**Aspose.Pdf.LogicalStructure.Element** にメソッドが追加されました：

- タグ（画像、テキスト、リンクなどの特定の要素にタグを追加）
- 子要素を挿入
- 子要素を削除
- 子要素をクリア

これらのメソッドを使用すると、たとえば PDF ファイルのタグを編集できます。

```java
    Document document = new Document(dataDir + "test.pdf");

    // Retrieve the first page of the document.
    Page page = document.getPages().get_Item(1);

    // Initialize variables to hold BDC (Begin Dictionary Context) elements for different purposes.
    BDC imageBdc = null;
    BDC pBdc = null;
    BDC link1Bdc = null;
    BDC link2Bdc = null;
    BDC helloBdc = null;

    // Iterate through the contents of the page.
    for (int i = 1; i <= page.getContents().size(); i++)
    {
        // Get the current operator from the page contents.
        Operator op = page.getContents().get_Item(i);

        // Check if the operator is an instance of BDC.
        if (op instanceof BDC) {
        BDC bdc = (BDC)op; // Cast the operator to BDC type.
        if (bdc != null)
        {
            // Check if the MCID (Mark Content Identifier) of the BDC is 0.
            if (bdc.getProperties().getMCID()[0] != null && bdc.getProperties().getMCID()[0] == 0)
            {
                helloBdc = bdc; // Store the BDC for later use.
            }
        }
    }

    // Check if the operator is an instance of Do (Draw Object).
    if (op instanceof Do) {
        Do doXobj = (Do)op; // Cast the operator to Do type.
        if (doXobj != null)
        {
            // Create a new BDC for an image and insert it into the page contents.
            imageBdc = new BDC("Figure");
            page.getContents().insert(i - 2, imageBdc); // Insert before the current operator.
            i++; // Increment the index to account for the inserted BDC.
            page.getContents().insert(i + 1, new EMC()); // Insert an EMC (End Mark Content).
            i++; // Increment the index again.
        }
    }

    // Check if the operator is an instance of TextShowOperator (for text display).
    if (op instanceof TextShowOperator) {
        TextShowOperator tx = (TextShowOperator)op; // Cast the operator to TextShowOperator type.
        if (tx != null)
        {
            // Check for specific text content and insert corresponding BDCs.
            if (tx.getText().contains("efter Ukendt forfatter er licenseret under"))
            {
                pBdc = new BDC("P");
                page.getContents().insert(i - 1, pBdc); // Insert before the current operator.
                i++; // Increment the index.
                page.getContents().insert(i + 1, new EMC()); // Insert an EMC.
                i++; // Increment the index.
            }
            if (tx.getText().contains("CC"))
            {
                link1Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link1Bdc); // Insert before the current operator.
                i++; // Increment the index.
                page.getContents().insert(i + 1, new EMC()); // Insert an EMC.
                i++; // Increment the index.
            }
            if (tx.getText().contains("Dette billede"))
            {
                link2Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link2Bdc); // Insert before the current operator.
                i++; // Increment the index.
                page.getContents().insert(i + 1, new EMC()); // Insert an EMC.
                i++; // Increment the index.
            }
        }
    }
}

    // Retrieve the tagged content from the document.
    ITaggedContent tagged = document.getTaggedContent();

    // Process the tagged content to modify structure attributes.
    // Get the first child element of the root element in the tagged content.
    com.aspose.pdf.tagged.logicalstructure.elements.Element p = tagged.getRootElement().getChildElements().get_Item(1);
    p.clearChilds(); // Clear existing child elements.

    // Tag the helloBdc with the parent structure element.
    MCRElement mcr = p.tag(helloBdc);

    // Create and set structure attributes for the tagged element.
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
            .getAttributes().createAttributes(AttributeOwnerStandard.Layout);
    StructureAttribute attr = new StructureAttribute(AttributeKey.SpaceAfter);
    attr.setNumberValue(30.625); // Set space after attribute.
    attrs.setAttribute(attr); // Apply the attribute to the structure.

    // Create  a new FigureElement in the tagged content.
    com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figure = tagged.createFigureElement();
    tagged.getRootElement().insertChild(figure, 2); // Insert the figure element at the second position.
    figure.setAlternativeText("A fly."); // Set alternative text for the figure.

    // Tag the imageBdc with the figure element.
    MCRElement mcr = figure.tag(imageBdc);

    // Retrieve the parent structure element of the specified MCR (Marked Content Reference)
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Create a new StructureAttribute for space after the element
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(3.625); // Set the space after value to 3.625 units
    attrs.setAttribute(spaceAfter); // Assign the space after attribute to the structure attributes

    // Create a new StructureAttribute for bounding box (BBox)
    StructureAttribute bbox = new StructureAttribute(AttributeKey.BBox);
    bbox.setArrayNumberValue(new Double[][] { new Double[] { (71.9971) }, new Double[] { (375.839) }, new Double[] { (523.299) }, new Double[] { (714.345) } });
    // Set the bounding box values for the structure attribute
    attrs.setAttribute(bbox); // Assign the bounding box attribute to the structure attributes

    // Create a new StructureAttribute for placement
    StructureAttribute placement = new StructureAttribute(AttributeKey.Placement);
    placement.setNameValue(AttributeName.Placement_Block); // Set the placement type to block
    attrs.setAttribute(placement); // Assign the placement attribute to the structure attributes

    // Retrieve the fourth child element from the root element of the tagged structure
    StructureElement p2 = (StructureElement)tagged.getRootElement().getChildElements().get_Item(3);
    p2.clearChilds(); // Clear any existing child elements from p2

    // Create a new SpanElement to be added to p2
    SpanElement span1 = tagged.createSpanElement();

    // Create structure attributes for the span element
    StructureAttributes attrs = span1.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Create a new StructureAttribute for text decoration type
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Set text decoration to underline
    attrs.setAttribute(textDecorationType); // Assign the text decoration type attribute to the structure attributes

    // Create a new StructureAttribute for text decoration thickness
    StructureAttribute textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    textDecorationThickness.setNumberValue(0); // Set the thickness of the text decoration to 0
    attrs.setAttribute(textDecorationThickness); // Assign the text decoration thickness attribute to the structure attributes

    // Create a new StructureAttribute for text decoration color
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    textDecorationColor.setArrayNumberValue(new Double[][] { new Double[] { (0.0196075) }, new Double[] { (0.384308) }, new Double[] { (0.756866) } });
    // Set the RGB color values for the text decoration
    attrs.setAttribute(textDecorationColor); // Assign the text decoration color attribute to the structure attributes

    p2.appendChild(span1); // Append the span1 element to p2

    // Create a new MCR element and tag it with pBdc
    MCRElement mcr = p2.tag(pBdc);
    // Retrieve the parent structure element of the MCR and create layout attributes
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Create a new StructureAttribute for text alignment
    StructureAttribute textAlign = new StructureAttribute(AttributeKey.TextAlign);
    textAlign.setNameValue(AttributeName.TextAlign_Center); // Set text alignment to center
    attrs.setAttribute(textAlign); // Assign the text alignment attribute to the structure attributes

    // Create a new StructureAttribute for space after the element
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(21.75); // Set the space after value to 21.75 units
    attrs.setAttribute(spaceAfter); // Assign the space after attribute to the structure attributes

    // Create a new SpanElement to be added to p2
    SpanElement span2 = tagged.createSpanElement();

    // Create structure attributes for the span element
    StructureAttributes attrs = span2.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Create a new StructureAttribute for text decoration type
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Set text decoration to underline
    attrs.setAttribute(textDecorationType); // Assign the text decoration type attribute to the structure attributes

    // Create a new StructureAttribute for text decoration color using the specified key.
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);

    // Set the array number value for the text decoration color attribute.
    // The color is represented in an array of RGB values, where each value is a Double.
    textDecorationColor.setArrayNumberValue(new Double[][] {
    new Double[] { (0.0196075) }, // Red component
    new Double[] { (0.384308) },  // Green component
    new Double[] { (0.756866) }   // Blue component
    });

    // Set the text decoration color attribute to the attrs object.
    attrs.setAttribute(textDecorationColor);

    // Append a child span element to the parent element p2.
    p2.appendChild(span2);

    // Create a new LinkElement instance for the second link.
    LinkElement link2 = tagged.createLinkElement();

    // Assign a unique ID to the link element using a randomly generated UUID.
    link2.setId(UUID.randomUUID().toString());

    // Append the link2 element as a child of span2.
    span2.appendChild(link2);

    // Tag the link2 element with the corresponding annotation from the page's annotations.
    link2.tag(page.getAnnotations().get_Item(1));

    // Tag the link2 element with additional metadata or context (link2Bdc).
    link2.tag(link2Bdc);

    // Create another LinkElement instance for the first link.
    LinkElement link1 = tagged.createLinkElement();

    // Assign a unique ID to the link1 element using a randomly generated UUID.
    link1.setId(UUID.randomUUID().toString());

    // Append the link1 element as a child of span1.
    span1.appendChild(link1);

    // Tag the link1 element with the corresponding annotation from the page's annotations.
    link1.tag(page.getAnnotations().get_Item(2));

    // Tag the link1 element with additional metadata or context (link1Bdc).
    link1.tag(link1Bdc);

    // Remove the first child element from the root element of the tagged document.
    tagged.getRootElement().removeChild(0);

    // Save the document to the specified output directory with the filename "_out.pdf".
    document.save(dataDir + "_out.pdf");
```

## Aspose.PDF 24.6 の新機能は何ですか

24.6以降、Aspose.PDF for Javaはjava.security.cert.X509Certificateおよびjava.security.PrivateKeyを使用してPDFに署名できるようになりました:

このコードは証明書ストアから証明書と秘密鍵を取得し、それらを使用して PDF ドキュメントの最初のページにデジタル署名を適用します。

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

## Aspose.PDF 24.5 の新機能

24.5 リリース以降、Form Editor Plugins が実装されました。

**Form Editor を使用して PDF のフォームを編集する方法**

- ライセンスキーを設定してください
- FormEditor クラスのインスタンスを作成します。このクラスは PDF フォームの操作用メソッドを提供します。
- FormEditorAddOptions クラスのインスタンスを作成します。このクラスは PDF ドキュメントにフォームフィールドを追加するためのオプションを指定します。
- FileDataSource クラス（ファイルパスまたはストリームを表す）を使用して、FormEditorAddOptions オブジェクトに入力ファイル ソースと出力ファイル ソースを追加します。
- FormEditor オブジェクトの Process メソッドを呼び出し、FormEditorAddOptions オブジェクトをパラメータとして渡します。
- ResultContainer.resultCollection を使用して結果にアクセスします

```java
// Specify the input and output paths for the PDF files.
String inputPath = "sample.pdf";
String outputPath = "out.pdf";

// Create an instance of the FormEditor plugin.
FormEditor pdfFormPlugin = new FormEditor();

// Create options for adding form fields.
ArrayList<FormFieldCreateOptions> options = new ArrayList<FormFieldCreateOptions>();

// Create a textbox form field.
FormTextBoxFieldCreateOptions tmp1 = new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 600, 90, 610));
tmp1.setValue("TextBoxField");
tmp1.setColor(Color.getChocolate());
tmp1.setPartialName("TexBoxField");
options.add(tmp1);

// Create a combo box form field.
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

// Create a checkbox form field.
FormCheckBoxFieldCreateOptions tmp3 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715));
tmp3.setValue("CheckBoxField 1");
tmp3.setPartialName("CheckBoxField_1");
tmp3.setColor(Color.getBlue());
options.add(tmp3);

// Create a checkbox form field.
FormCheckBoxFieldCreateOptions tmp4 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(100, 700, 190, 715));
tmp4.setChecked(new Boolean[]{true});
tmp4.setValue("CheckBoxField 2");
tmp4.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
tmp4.setStyle(new Integer[]{BoxStyle.Cross});
options.add(tmp4);

// Create a checkbox form field.
FormCheckBoxFieldCreateOptions tmp5 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(200, 700, 390, 715));
tmp5.setPartialName("CheckBoxField_3");
tmp5.setValue("CheckBoxField 3");
tmp5.setStyle(new Integer[]{BoxStyle.Star});
tmp5.setChecked(new Boolean[]{true});
tmp5.setTextHorizontalAlignment(new HorizontalAlignment[]{HorizontalAlignment.Center});
options.add(tmp5);

FormEditorAddOptions opt = new FormEditorAddOptions(options);

// Add input and output files to the options.
opt.addInput(new FileDataSource(inputPath));
opt.addOutput(new FileDataSource(outputPath));

// Process the form fields using the plugin.
ResultContainer results = pdfFormPlugin.process(opt);
```

このリリースではPDFレイヤーを操作できるようになりました。例えば：

- PDFレイヤーをロックする
- PDFレイヤー要素を抽出
- レイヤー化されたPDFをフラット化する
- PDF内のすべてのレイヤーを1つに統合する

**PDFレイヤーをロックする**

24.5 リリース以降、PDF を開き、最初のページの特定のレイヤーをロックし、変更を加えた状態でドキュメントを保存できます。2 つの新しいメソッドと 1 つのプロパティが追加されました:

Layer.Lock(); -  レイヤーをロックします。
Layer.Unlock(); - レイヤーのロックを解除します。
Layer.Locked; - プロパティ、レイヤーのロック状態を示す。

```java
Document document = new Document(input);
Page page = document.getPages().get_Item(1);
Layer layer = page.getLayers().get(0);

layer.lock();

document.save(output);
```

**PDFレイヤー要素を抽出**

Aspose.PDF for Java ライブラリは、最初のページから各レイヤーを抽出し、各レイヤーを別々のファイルに保存することができます。

レイヤーから新しい PDF を作成するには、以下のコードスニペットを使用できます：

```java
Document document = new Document(inputPath);
java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

for (Layer layer : layers)
{
    layer.save(outputPath);
}
```

**レイヤー化されたPDFをフラット化**

Aspose.PDF for Java ライブラリは PDF を開き、最初のページの各レイヤーを反復処理し、各レイヤーをフラット化してページ上に永続的にします。

```java
Document document = new Document(input);
Page page = document.getPages().get_Item(1);

for (Layer layer : page.getLayers())
{
    layer.flatten(true);
}
document.save(output);
```

Layer.flatten(boolean cleanupContentStream) メソッドは、コンテンツ ストリームからオプション コンテンツ グループ マーカーを削除するかどうかを指定する boolean パラメータを受け取ります。
cleanupContentStream パラメータを false に設定すると、フラッテン化のプロセスが高速化します。

**PDF内のすべてのレイヤーを1つに結合**

Aspose.PDF for Java ライブラリは、最初のページのすべての PDF レイヤーまたは特定のレイヤーを新しいレイヤーにマージし、更新されたドキュメントを保存します。

ページ上のすべてのレイヤーを統合するために、2つのメソッドが追加されました：

- void mergeLayers(String newLayerName);
- void mergeLayers(String newLayerName, String newOptionalContentGroupId);

第2パラメータはオプショナルコンテンツグループマーカーの名前変更を可能にします。デフォルト値は "oc1" (/OC /oc1 BDC) です。

```java
Document document = new Document(input);
Page page = document.getPages().get_Item(1);
page.mergeLayers("NewLayerName");

// Or page.mergeLayers("NewLayerName", "OC1");

document.save(output);
```

## Aspose.PDF 24.4 の新機能

このリリースでは PDF 用の Java プラグインが導入されました:

- フォーム フラッテンナープラグイン

```java
FormFlattener pdfFormPlugin = new FormFlattener();

FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

opt.addInput(new FileDataSource("sample.pdf"));
opt.addOutput(new FileDataSource("sample-flat.pdf"));

ResultContainer result = pdfFormPlugin.process(opt);

// Check result.
java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- フォームエクスポーター

```java
Rectangle rect = new com.aspose.pdf.Rectangle(0, 220, 600, 330);

// Plugin use.
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

// Check result.
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

PDF文書のサイズを減らす方法は？

```java
String input = "Test.pdf";
String output = "Optimized.pdf";

Optimizer optimizer = new Optimizer();

OptimizeOptions opt = new OptimizeOptions();
opt.addInput(new FileDataSource(input));
opt.addOutput(new FileDataSource(output));

optimizer.process(opt);
```

PDFドキュメントのサイズを変更する方法は？

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

PDF ドキュメントを回転させる方法は？

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

## Aspose.PDF 24.3 の新機能

24.3から、TextFragmentAbsorberでフレーズのリストに対する検索を実装する。

```java
String[] expressions = new String[] {
  //detect phone number
  "\\b\\d{3}-\\d{3}-\\d{4}\\b",
  //detect card number
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

次の機能は、PDFからMarkdownへのコンバータ用にテーブルを変換する機能を追加することです

```java
Document doc = new Document(dataDir + "56201.pdf");
MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
doc.save(dataDir + "56201.md", saveOptions);
```

## Aspose.PDF 24.2 の新機能は何ですか？

24.2 以降、AcroForms を使用した PDF に Watermark を追加できるようになりました。TextStamp は AcroForm ファイルでの使用に適しています。XFA ファイルに対して TextStamp を使用すると、テキストは通常の PDF ファイルと同様にページ上に描画されます（たとえば Chrome ブラウザなど XFA ファイルを読み取れない PDF ビューアで確認できます）。XFA ファイルにテキストを追加するには、XFA ファイルの内部 XML を変更する必要があります。

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

注釈の StateModel を設定
MarkupAnnotation クラスの setReviewState と setMarkedState を使用して、必要な状態を設定できます。
すべてのマークアップ注釈には、Set State オプションが利用可能です。

```java
// Open the source PDF document
Document pdfDocument = new Document();
pdfDocument.getPages().add();
// Create annotation
TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.getPages().get_Item(1), new Rectangle(200,
        400, 400, 600));

//Set annotation title
textAnnotation.setTitle("Sample Annotation Title");

//Set annotation subject
textAnnotation.setSubject("Sample Subject");
//Specify the annotation contents
textAnnotation.setContents("Sample contents for the annotation");
textAnnotation.setOpen(true);
textAnnotation.setIcon(TextIcon.Key);
com.aspose.pdf.Border border = new com.aspose.pdf.Border(textAnnotation);
border.setWidth(5);
border.setDash(new Dash(1, 1));
textAnnotation.setBorder(border);
String userName1 = "Aspose1";
textAnnotation.setReviewState(AnnotationState.Rejected, userName1);
textAnnotation.setRect(new Rectangle(200, 400, 400, 600));

//Add annotation in the annotations collection of the page
pdfDocument.getPages().get_Item(1).getAnnotations().add(textAnnotation);
pdfDocument.processParagraphs();

//Save the output file
pdfDocument.save(dataDir + "output_24_2_Rejected.pdf");

pdfDocument = new Document(dataDir + "output" + version + "3.pdf");
TextAnnotation textAnnotation2 = (TextAnnotation) pdfDocument.getPages().get_Item(1).getAnnotations().get_Item(1);

String userName2 = "Aspose2";
textAnnotation2.setReviewState(AnnotationState.Accepted, userName2);
pdfDocument.save(dataDir + "output_24_2_Rejected_and_Accepted.pdf");
```

24.2 から OFD から PDF への変換を実装:

```java
Document document = new Document(inputPath, new OfdLoadOptions());
document.save(outputPath);
```

## Aspose.PDF 24.1 の新機能

24.1 リリースから PDF から Markdown への変換を実装します:

```java
final Document doc = new Document(inputPdfPath);
MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
doc.save(markdownOutputFilePath, saveOptions);
```

また、24.1 では、InterruptMonitor を使用したスレッドの割り込みが実装されました。

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

      //foreach to while statements conversion
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
      System.out.println("Interrupting the save thread at " + System.currentTimeMillis());
    } finally {
      if (document != null) {
        document.close();
      }
    }

  }

}).start();

System.out.println("Process is started thread at " + System.currentTimeMillis());

// The timeout should be less than the time required for full document save (without interruption).
Thread.sleep(500);

// Interrupt the process
monitor.interrupt();

System.out.println("Interrupted the save thread at " + System.currentTimeMillis());
```

## Aspose.PDF 23.12 の新機能は何ですか

フォームは見つけることができ、テキストは以下のコードスニペットを使用して置き換えることができます：

```java
Document document = new Document(input);
String expectedText = "This is a text added while creating new PDF in Kofx Power PDF Standard.";

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

または、フォームを完全に削除できます:

```java
Document document = new Document(input);
XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

//foreach to while statements conversion
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

フォームを削除する別のバリエーション：

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

- 次のコード スニペットを使用して、すべてのフォームを削除できます。

```java
Document document = new Document(input);

XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

forms.clear();

document.save(output);
```

## Aspose.PDF 23.11 の新機能は何ですか

このリリースから、PDFファイルの非表示テキストを削除できるようになりました：

```java
Document document = new Document(inputFile);

TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
document.getPages().accept(textAbsorber);

msStringBuilder result = new msStringBuilder();

//foreach to while statements conversion
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

## Aspose.PDF 23.10 の新機能

現在のアップデートでは、タグ付けされたPDFからタグを削除する3つのバージョンが提供されています。

- documentElement（ルートツリー要素）からいくつかのノード要素を削除する：

```java
Document document = new Document(inputPath);
RootElement structure = document.getLogicalStructure();
Element documentElement = structure.getChildren().get_Item(0);
Element structElement = (documentElement.getChildren().getCount() > 1) ?  documentElement.getChildren().get_Item(1) : null;
documentElement.getChildren().remove(structElement);
// You can also delete the structElement itself
            //if (structElement != null)
            //{
            //    structElement.remove();
            //}
document.save(outputPath);
```

- ドキュメントからすべてのマークされた要素タグを削除しますが、構造要素は保持してください：

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

- すべてのタグを削除する:

```java
Document document = new Document(inputPath);
RootElement structure = document.getLogicalStructure();
Element root = structure.getChildren().get_Item(0);
root.remove();
document.save(outputPath);
```

文字の高さを測定する新機能を実装しました。次のコードを使用して文字の高さを測定してください：

```java
Document doc = new Document("input.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.visit(doc.getPages().get_Item(1));
double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```

測定は文書に埋め込まれたフォントに基づいていることに注意してください。次元の情報が欠落している場合、このメソッドは 0 を返します。

## Aspose.PDF 23.9 の新機能は何ですか

23.9 のサポートから、入力可能なフィールドから子アノテーションを削除できるようになりました。

例 1:

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

例 2:

```java
{
String option1 = "option 1";
String option2 = "option 2";
String outputPdf = "output.pdf";

final Document document = new Document();
try /*JAVA: was using*/ {
    Page page = document.getPages().add();

    CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

    // Set the first checkbox group option value
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

ImageFilterType.Flate を使用して画像を追加すると、透明性が保持されません。

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

PDF ドキュメントのインクリメンタル更新を検出する機能が 23.8 で追加されました。この機能は、ドキュメントがインクリメンタル更新で保存された場合に ‘true’ を返し、それ以外の場合は ‘false’ を返します。

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

もう1つの機能は、入力 PDF から宛先 PDF へ OutputIntents をコピーすることです

Document.getOutputIntents()という新しい public プロパティを追加し、ドキュメント内の出力インテントにアクセスできるようにしました。
当面は、すでに文書内に存在する出力インテントの使用のみがサポートされており、ユーザーは OutputIntent をゼロから作成できません。

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

Aspose.PDF 23.8 のサポートから、シェイプ抽出を追加:

```java
{
    String input1 = getInputPdf("46298_1");
    String input2 = getInputPdf("46298_2");

    Document source = new Document(input1);
    Document dest = new Document(input2);

    Page destPage = dest.getPages().get_Item(1);

    TextFragmentAbsorber tfAbsorber = new TextFragmentAbsorber();
    tfAbsorber.visit(source.getPages().get_Item(1));

    //foreach to while statements conversion
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

        // Recalculate a new position since page size differs the originl PDF
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

テキストを追加する際にオーバーフローを検出する機能もサポートしています:

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

## Aspose.PDF 23.7 の新機能

バージョン23.7から、Print Dialog Presets の Page Scaling をサポートします:

```java
Document document = new Document();
document.getPages().add();
document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
document.save(outputPdf);

Document documentOutput = new Document(outputPdf);
int printScaling = documentOutput.getPrintScaling();
System.out.println("PrintScaling: " + printScaling);
```

## Aspose.PDF 23.6 の新機能

23.6バージョンから、HTMLおよびEpubページのタイトルを設定する機能を追加でサポートします。

HTML のコード:

```java
HtmlSaveOptions options = new HtmlSaveOptions();
options.setFixedLayout(true);
options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
options.setTitle("</title>NEW PAGE & TITILE</head>");

Document document = new Document(inputPath);
document.save(outPath, options);
```

EPUB のコード：

```java
EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
epubSaveOptions.setTitle("</title>NEW PAGE & TITILE</head>");
epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

Document document = new Document(inputPath);
document.save(outPath, epubSaveOptions);
```

23.6 のサポートからベクターグラフィックの配置用 API を提供:

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

## Aspose.PDF 23.1 の新機能は何ですか？

23.1バージョンからPrinterMarkアノテーションの作成をサポートしています。アノテーションのバリエーションの一つ、ColorBarAnnotationが追加されました。

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

## Aspose.PDF 22.12 の新機能は何ですか？

このリリースでは、PDF を DICOM 画像に変換することがサポートされます:

```java
DicomDevice device = new DicomDevice(PageSize.getA4());
Document doc = new Document("Input.pdf");
ByteArrayOutputStream stream = new ByteArrayOutputStream();
device.process(doc.getPages().get_Item(1), stream);
```

## Aspose.PDF 22.9 の新機能

22.09から、署名におけるサブジェクトルビック（E=、CN=、O=、OU=、）の順序を変更するためのプロパティの追加をサポートします。

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

## Aspose.PDF 22.8 の新機能

Aspose.PDF 23.8 から、xref テーブルを再構築するメソッドの追加をサポート:

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

## Aspose.PDF 22.6 の新機能は何ですか

PDF to PDF_A_1A - 大きな出力ファイルサイズを回避するために、透明色を削除するオプションを実装する。

バージョン 22.5 以降、顧客は変換された透過の品質と、その結果としての出力ファイルサイズを制御できるようになりました：

```java
opts.setTransparencyResolution(300);
```

## Aspose.PDF 22.5 の新機能

PDF/A変換中に透明なコンテンツは削除され、画像に置き換えられます。
新機能を実装しましたので、顧客はパラメータ TransparencyResolution: を使用して画像の品質を制御できるようになりました。

```java
com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
options.setTransparencyResolution(300);
pdfDocument.convert(options);
pdfDocument.save("finalOutput.pdf");
```

## Aspose.PDF 22.4 の新機能は何ですか？

このリリースには Aspose.PDF for Java の情報が含まれています:

- PDF to ODS: 下付き文字と上付き文字のテキストを認識する;

**例**

```java
Document pdfDocument = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
pdfDocument.Save("output.ods"), options);
```

- PDF to XMLSpreadSheet2003: 下付き文字と上付き文字のテキストを認識する;

- PDFからExcelへ：下付き文字と上付き文字のテキストを認識する；

## Aspose.PDF 22.3 の新機能

PDF to ODS: RTL のサポートはバージョン 22.3 で利用可能です。

```java
ExcelSaveOptions options = new ExcelSaveOptions();
options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
pdfDocument.save("output.ods", options);
```

## Aspose.PDF 22.2 の新機能は何ですか

このリリースには PDF から XSLX への変換が含まれます：RTL（ヘブライ語、アラビア語）サポート。

## Aspose.PDF 22.1 の新機能

Aspose.PDF for Java は、Portable Document Format (PDF) バージョン 2.0 のドキュメントの読み込みを許可します。

## Aspose.PDF 21.10 の新機能

### 隠しテキストを検出する方法は？

以下のコードをご使用ください：

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

### デジタル署名のテキスト色を変更する方法は？

21.8 バージョンの setForegroundColor では、Digital Signature のテキスト色を変更できます。

```java
Please, use the following code:

    PdfFileSignature pdfSign = new PdfFileSignature();
    pdfSign.bindPdf(inFile);
    //create a rectangle for signature location
    java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);
    PKCS7 pkcs = new PKCS7(inPfxFile, "");

    pkcs.setCustomAppearance( new SignatureCustomAppearance());
//set text color
    pkcs.getCustomAppearance().setForegroundColor(Color.getGreen());

    // sign the PDF file
    pdfSign.sign(1, true, rect, pkcs);
    //save output PDF file
    pdfSign.save(outFile);
```

## Aspose.PDF 21.6 の新機能

### ImagePlacementAbsorber を使用してドキュメントから画像を非表示にする

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

### 画像をマージするためのAPIの追加

Aspose.PDF 21.4 は画像の結合を可能にします。画像ストリームのリストを 1 つの画像ストリームにマージします。Png/jpg/tiff の出力形式がサポートされており、サポートされていない形式を使用した場合、出力ストリームはデフォルトで Jpeg としてエンコードされます。
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

また、画像を Tiff 形式で結合することもできます:

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

## Aspose.PDF 21.02 の新機能は何ですか？

Aspose.PDF v21.02でPDFをPAdES LTV署名で署名

```java
final Document document = new Document(inputPdf);
    try
    {
        PdfFileSignature signature = new PdfFileSignature(document);
        PKCS7 pkcs7 = new PKCS7(getInputPath("cert.pfx"), "password");
        //Sign PDF with PAdES LTV Signatures
        pkcs7.setUseLtv(true);

        signature.sign(1, true, new Rectangle(100, 100, 300, 300), pkcs7);
        signature.save(outputPdf);
    }
    finally { if (document != null) (document).dispose(); }
```
