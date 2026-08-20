---
title: 새로운 소식
linktitle: 새로운 소식
type: docs
weight: 10
url: /java/whatsnew/
description: 이 페이지에서는 최근 릴리스에 도입된 Java용 Aspose.PDF의 가장 인기 있는 새로운 기능을 소개합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java용 Aspose.PDF의 인기 있는 새로운 기능
Abstract: Java용 Aspose.PDF 문서의 새로운 기능 섹션은 최근 릴리스에 도입된 최신 업데이트, 개선 사항 및 버그 수정에 대한 개요를 제공합니다. 개발자가 PDF 처리의 최신 발전 사항에 대한 정보를 계속 얻을 수 있도록 새로운 기능, 성능 개선 및 호환성 업데이트를 강조합니다. 설명서에는 더 이상 사용되지 않는 기능과 권장되는 대안에 대한 세부 정보도 포함되어 있습니다. 이 섹션을 정기적으로 검토함으로써 개발자는 원활한 PDF 관리를 위해 Java 애플리케이션에서 가장 효율적이고 최신 기능을 활용하고 있는지 확인할 수 있습니다.
SoftwareApplication: java
---
## Aspose.PDF 25.12의 새로운 기능


### 
XFDF에서 임의 회전이 가능한 자유 텍스트 주석



XFDF의 자유 텍스트 주석에 임의 회전 각도에 대한 지원이 추가되어 가져오고 내보낸 주석 레이아웃이 더욱 유연해졌습니다.


```java
Document pdfDocument = new Document(inputPdf);
com.aspose.pdf.facades.PdfAnnotationEditor editor = new PdfAnnotationEditor();
editor.bindPdf(pdfDocument);
editor.importAnnotationsFromXfdf(inputXfdf);
editor.save(output);
```

## 
Aspose.PDF 25.11의 새로운 기능


### 
숨겨진 데이터 삭제 개선

이제 HiddenDataSanitizer를 통해 향상된 PDF 삭제 기능을 사용하여 문서에서 숨겨진 콘텐츠를 효과적으로 제거할 수 있습니다.


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

### 
PDF 최적화 중 파일 크기 감소 개선



PDF 최적화는 이제 글꼴 하위 설정 처리 방법을 개선하여 파일 크기 감소를 개선합니다.


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

## 
Aspose.PDF 25.10의 새로운 기능


### 
PDF를 PDF/E로 변환 지원

이제 Java용 Aspose.PDF는 PDF 문서를 PDF/E 형식으로 변환하는 것을 지원합니다.


```java
Document document = new Document(inputPdf);
document.convert(conversionLog, PdfFormat.PDF_E_1, ConvertErrorAction.Delete);
document.save(outputPdf);
```

### 
주석의 HTML 텍스트



주석 내부에 HTML 텍스트를 추가하기 위한 지원이 추가되었습니다.


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

## 
Aspose.PDF 25.9의 새로운 기능


### 
HTML을 PDF로 변환하는 플러그인

이제 Java용 Aspose.PDF에는 HTML-PDF 처리 워크플로를 단순화하기 위한 Html to Pdf 플러그인이 포함되어 있습니다.


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

### 
PDF 1.6 적합성 지원



이 문서 버전이 필요한 시나리오를 위해 PDF 1.6 규격에 대한 지원이 추가되었습니다.


## 
Aspose.PDF 25.8의 새로운 기능


### 
표 테두리 스타일 지원

테이블 모양을 더 효과적으로 제어할 수 있도록 테이블 테두리 스타일에 대한 지원이 추가되었습니다.


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

### 
PDF 이미지에 대한 ALT 텍스트 추출



이제 PDF 문서의 이미지에 대한 대체 텍스트 설명을 얻을 수 있어 접근성 지향 처리에 도움이 됩니다.


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

## 
Aspose.PDF 25.7의 새로운 기능


### 
PDF 채팅GPT 플러그인

이제 Java용 Aspose.PDF에는 PDF 중심 AI 상호 작용 시나리오를 위한 PDF ChatGPT 플러그인이 포함되어 있습니다.



이 예에서는 파일을 메시지 소스로 추가하여 PdfChatGpt 플러그인을 사용하는 방법을 보여줍니다.


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


이 예에서는 요청에 메시지를 추가하여 PdfChatGpt 플러그인을 사용하는 방법을 보여줍니다.


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


이 예에서는 요청에 하나의 메시지를 추가하여 PdfChatGpt 플러그인을 사용하는 방법을 보여줍니다.


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

## 
Aspose.PDF 25.6의 새로운 기능

### PDF에서 DOCX 출력 형식으로 개선됨



이전에 출력 형식이 올바르지 않았던 문서에 대해 PDF에서 DOCX로의 변환이 개선되었습니다.


```java
Document doc = new Document(dataDir + "SD_Aspose.pdf");
DocSaveOptions saveOption = new DocSaveOptions();
saveOption.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
saveOption.setFormat(DocSaveOptions.DocFormat.DocX);
saveOption.setRecognizeBullets(true);
doc.save(dataDir + "SD_Aspose.docx", saveOption);
```

## 
Aspose.PDF 25.5의 새로운 기능


### 
PDF에서 ODS로의 변환 이미지 보존



이제 PDF 문서를 ODS로 변환할 때 이미지가 보존됩니다.

```java
Document doc = new Document("input.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
doc.save("output.ods", options);
```

### PDF를 PDF/A로 변환하는 동안 자동 태그 생성



PDF에서 PDF/A로의 변환은 이제 자동 태그 생성을 지원하여 출력 문서의 태그 결과를 향상시킵니다.


```java
Document document = new Document(dataDir+"source.pdf");

PdfFormat format = PdfFormat.PDF_A_1A;
PdfFormatConversionOptions options = new PdfFormatConversionOptions(format, ConvertErrorAction.Delete);
options.setAutoTaggingSettings(AutoTaggingSettings.getDefault());

document.convert(options);
document.save(dataDir+"out_"+BuildVersionInfo.ASSEMBLY_VERSION+"_"+format+"_"+document.getFileName());
document.close();
```

## 
Aspose.PDF 25.4의 새로운 기능


### 
PDF에서 XLSX로의 변환에서 하이퍼링크 유지



이제 PDF 문서를 XLSX로 변환할 때 하이퍼링크가 유지되므로 내보낸 스프레드시트의 탐색이 향상됩니다.

```java
Document doc = new Document("input.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
doc.save("output.xlsx", options);
```

## Aspose.PDF 25.3의 새로운 기능



25.2부터 PDF 디지털 서명의 손상을 감지하는 기능이 추가되었습니다. 'SignaturesCompromiseDetector' 클래스를 사용하여 디지털 서명의 손상 여부를 확인할 수 있습니다. 문서의 서명을 확인하려면 check() 메소드를 호출하십시오. 서명 손상이 감지되지 않으면 메서드는 true를 반환합니다. 기존 서명이 문서 전체에 적용되는지 확인하려면 'SignaturesCoverage 속성'을 사용하세요.


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

## 
Aspose.PDF 25.2의 새로운 기능



25.2부터 PDF를 PDF/X-4 파일 형식으로 변환하는 기능이 추가되었습니다.


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


버전 25.2부터 출력 HTML을 중앙 정렬하는 것이 가능해졌습니다.

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

또한 버전 25.2부터 Aspose.PDF를 사용하여 글꼴과 크기가 지정된 텍스트의 상승 및 하강을 얻는 것이 가능해졌습니다. 새로운 기능은 'com.aspose.pdf.Font' 클래스에 구현되었습니다.



추가된 방법:



**최대 상승점 측정**



-public double getAcentPoint(문자열 str, float 글꼴 크기)



**최대 하강점 측정**

- 공개 더블 getDescentPoint(문자열 str, float 글꼴 크기)


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

## 
Aspose.PDF 25.1의 새로운 기능



PDF/X 및 PDF/A 변환을 위해 외부 ICC 프로필에 대한 경로를 전달하는 기능은 PdfFormatConversionOptions.IccProfileFileName 속성에 의해 활성화되어 몇 년 동안 이미 라이브러리에 존재했습니다. 이제 OutputIntent 클래스의 개체를 사용하여 OutputIntent 속성을 채우기 위해 데이터를 전달할 수도 있습니다.



다음 스니펫은 주석 FOGRA39 ICC 프로필을 사용하여 주석 문서를 PDF/X-1로 변환하는 방법을 보여줍니다.


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


25.1부터 문서 사용 시 권한에 대한 정보를 얻는 기능이 추가되었습니다.

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

## Aspose.PDF 24.12의 새로운 기능



버전 24.12부터 서로게이트 쌍 문자 지원이 가능해졌습니다.



'서로게이트 쌍'이라는 용어는 UTF-16 인코딩 체계에서 높은 코드 포인트를 사용하여 유니코드 문자를 인코딩하는 것을 의미합니다.


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


버전 24.12부터 PDF 문서를 PDF/A-4로 변환하는 것이 가능해졌습니다. PDF 2.0을 기반으로 하는 표준 파트 4가 2020년 말에 출판되었습니다.



다음 코드 조각은 입력 문서가 2.0보다 이전 PDF 버전인 경우 문서를 PDF/A-4 형식으로 변환하는 방법을 보여줍니다.

```java
Document document = new Document(inputPdf);
// Only PDF-2.x documents can be converted to PDF/A-4
document.convert("log1.xml", PdfFormat.v_2_0, ConvertErrorAction.Delete);
document.save(tmpOutputFile);

document = new Document(tmpOutputFile);
document.convert("log2.xml", PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
document.save("output.pdf");
```

## Aspose.PDF 24.9의 새로운 기능



이 릴리스에서는 하위 수준 기능을 사용하여 액세스 가능한 PDF를 생성할 수 있습니다.



다음 코드 조각은 Aspose.PDF 라이브러리를 활용하여 PDF 문서 및 태그가 지정된 콘텐츠와 함께 작동합니다.


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


PDF 문서와 페이지의 그래픽 비교를 위해 `GraphicalPdfComparer` 클래스가 추가되었습니다. 그래픽 비교는 문서 페이지 이미지를 다룹니다. 결과는 `ImagesDifference` 개체로 반환되거나 원본과 차이점이 병합된 이미지가 포함된 PDF 문서로 반환됩니다. 그래픽 비교는 텍스트나 그래픽 내용에 약간의 차이가 있는 문서에 가장 유용합니다.



다음 코드 조각은 두 PDF 문서의 그래픽 비교를 보여주고 차이점이 있는 이미지를 결과 PDF 문서에 저장합니다.

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

## Aspose.PDF 24.8의 새로운 기능



24.8부터 PDF/A-4 형식 지원:


```java
Document document = new Document(inputPdf);
// Only PDF-2.x documents can be converted to PDF/A-4
document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
document.save(outputFile);
```


또한 이미지 스탬프에 대체 텍스트를 추가할 수 있습니까?



AlternativeText 속성이 ImageStamp에 추가되었습니다. 값이 할당된 경우 ImageStamp를 문서에 추가하면 대체 텍스트가 포함됩니다.


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


또한 다음 코드는 FigureElements의 기존 이미지에 AlternativeText를 추가하는 방법을 보여줍니다.

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

## Aspose.PDF 24.7의 새로운 기능



24.7 릴리스부터 태그가 지정된 PDF 편집의 일부로 **Aspose.Pdf.LogicalStructure.Element**에 메서드가 추가되었습니다.


- 
태그(이미지, 텍스트, 링크 등 특정 연산자에 태그 추가)

- 
삽입하위

- 
자식 제거
- 클리어차일즈



이러한 방법을 사용하면 PDF 파일 태그를 편집할 수 있습니다. 예:


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

## 
Aspose.PDF 24.6의 새로운 기능



24.6부터 Java용 Aspose.PDF에서는 java.security.cert.X509Certificate, java.security.PrivateKey를 사용하여 PDF에 서명할 수 있습니다.



이 코드는 인증서 저장소에서 인증서와 개인 키를 검색한 다음 이를 사용하여 PDF 문서의 첫 번째 페이지에 디지털 서명을 적용합니다.

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

## Aspose.PDF 24.5의 새로운 기능



24.5 릴리스부터 양식 편집기 플러그인이 구현되었습니다.



**양식 편집기를 사용하여 PDF의 양식을 편집하는 방법**


- 
라이센스 키 설정

- 
PDF 양식을 조작하기 위한 메서드를 제공하는 FormEditor 클래스의 인스턴스를 만듭니다.
- PDF 문서에 양식 필드를 추가하기 위한 옵션을 지정하는 FormEditorAddOptions 클래스의 인스턴스를 만듭니다.

- 
파일 경로 또는 스트림을 나타내는 FileDataSource 클래스를 사용하여 FormEditorAddOptions 개체에 입력 파일 소스 및 출력 파일 소스를 추가합니다.

- 
FormEditorAddOptions 개체를 매개변수로 전달하여 FormEditor 개체의 Process 메서드를 호출합니다.

- 
ResultContainer.resultCollection을 사용하여 결과에 액세스합니다.


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


이 릴리스에서는 PDF 레이어로 작업할 수 있습니다. 예를 들어:

- PDF 레이어 잠그기

- 
PDF 레이어 요소 추출

- 
레이어가 있는 PDF 병합

- 
PDF 내부의 모든 레이어를 하나로 병합



**PDF 레이어 잠그기**

24.5 릴리스부터 PDF를 열고, 첫 번째 페이지에서 특정 레이어를 잠그고, 변경 사항이 포함된 문서를 저장할 수 있습니다. 두 가지 새로운 메서드가 있으며 하나의 속성이 추가되었습니다.



레이어.잠금(); - 레이어를 잠급니다.


레이어.잠금해제(); - 레이어의 잠금을 해제합니다.


레이어.잠김; - 레이어 잠금 상태를 나타내는 속성입니다.


```java
Document document = new Document(input);
Page page = document.getPages().get_Item(1);
Layer layer = page.getLayers().get(0);

layer.lock();

document.save(output);
```


**PDF 레이어 요소 추출**

Aspose.PDF for Java 라이브러리를 사용하면 첫 번째 페이지에서 각 레이어를 추출하고 각 레이어를 별도의 파일에 저장할 수 있습니다.



레이어에서 새 PDF를 만들려면 다음 코드 조각을 사용할 수 있습니다.


```java
Document document = new Document(inputPath);
java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

for (Layer layer : layers)
{
    layer.save(outputPath);
}
```


**레이어가 있는 PDF 병합**



Java용 Aspose.PDF 라이브러리는 PDF를 열고, 첫 번째 페이지의 각 레이어를 반복하고, 각 레이어를 병합하여 페이지에 영구적으로 만듭니다.


```java
Document document = new Document(input);
Page page = document.getPages().get_Item(1);

for (Layer layer : page.getLayers())
{
    layer.flatten(true);
}
document.save(output);
```


Layer.Flatten(boolean cleanupContentStream) 메소드는 콘텐츠 스트림에서 선택적 콘텐츠 그룹 마커를 제거할지 여부를 지정하는 부울 매개변수를 허용합니다.
cleanupContentStream 매개변수를 false로 설정하면 평면화 프로세스 속도가 빨라집니다.



**PDF 내부의 모든 레이어를 하나로 병합**



Aspose.PDF for Java 라이브러리를 사용하면 모든 PDF 레이어 또는 첫 번째 페이지의 특정 레이어를 새 레이어로 병합하고 업데이트된 문서를 저장할 수 있습니다.



페이지의 모든 레이어를 병합하기 위해 두 가지 방법이 추가되었습니다.


- 
void mergeLayers(String newLayerName);
- void mergeLayers(String newLayerName, String newOptionalContentGroupId);



두 번째 매개변수를 사용하면 선택적 콘텐츠 그룹 마커의 이름을 바꿀 수 있습니다. 기본값은 "oc1"(/OC/oc1 BDC)입니다.


```java
Document document = new Document(input);
Page page = document.getPages().get_Item(1);
page.mergeLayers("NewLayerName");

// Or page.mergeLayers("NewLayerName", "OC1");

document.save(output);
```

## 
Aspose.PDF 24.4의 새로운 기능



이번 릴리스에는 PDF용 Java 플러그인이 도입되었습니다.


- 
양식 병합 플러그인

```java
FormFlattener pdfFormPlugin = new FormFlattener();

FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

opt.addInput(new FileDataSource("sample.pdf"));
opt.addOutput(new FileDataSource("sample-flat.pdf"));

ResultContainer result = pdfFormPlugin.process(opt);

// Check result.
java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- 양식 내보내기


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

- 
병합 플러그인


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

- 
최적화 플러그인



PDF 문서의 크기를 줄이는 방법은 무엇입니까?


```java
String input = "Test.pdf";
String output = "Optimized.pdf";

Optimizer optimizer = new Optimizer();

OptimizeOptions opt = new OptimizeOptions();
opt.addInput(new FileDataSource(input));
opt.addOutput(new FileDataSource(output));

optimizer.process(opt);
```


PDF 문서의 크기를 조정하는 방법은 무엇입니까?

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

PDF 문서를 회전하는 방법은 무엇입니까?


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

## 
Aspose.PDF 24.3의 새로운 기능



24.3부터 TextFragmentAbsorber의 구문 목록을 통한 검색을 구현합니다.


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


다음 기능은 PDF용 테이블을 Markdown 변환기로 변환하는 기능을 추가하는 것입니다.


```java
Document doc = new Document(dataDir + "56201.pdf");
MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
doc.save(dataDir + "56201.md", saveOptions);
```

## 
Aspose.PDF 24.2의 새로운 기능

24.2부터 AcroForms를 사용하여 PDF에 워터마크를 추가할 수 있습니다. TextStamp는 AcroForm 파일과 함께 사용하기에 적합합니다. XFA 파일용 TextStamp를 사용하면 일반 PDF 파일처럼 페이지에 텍스트가 그려집니다(예를 들어 Chrome 브라우저에서 XFA 파일을 읽을 수 없는 PDF 뷰어에서 볼 수 있음). XFA 파일에 텍스트를 추가하려면 XFA 파일의 내부 XML에서 텍스트를 변경해야 합니다.


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


주석에 대한 StateModel 설정


MarkupAnnotation 클래스의 setReviewState 및 setMarkedState를 사용하여 필요한 상태를 설정할 수 있습니다.


모든 마크업 주석에는 사용 가능한 상태 설정 옵션이 있습니다.


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


24.2에서 OFD를 PDF로 변환 구현:

```java
Document document = new Document(inputPath, new OfdLoadOptions());
document.save(outputPath);
```

## Aspose.PDF 24.1의 새로운 기능



24.1 릴리스부터 PDF를 Markdown으로 변환 구현:


```java
final Document doc = new Document(inputPdfPath);
MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
doc.save(markdownOutputFilePath, saveOptions);
```


또한 24.1에서는 InterruptMonitor를 사용한 스레드 중단이 구현되었습니다.


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

## 
Aspose.PDF 23.12의 새로운 기능



양식을 찾을 수 있으며 다음 코드 조각을 사용하여 텍스트를 바꿀 수 있습니다.

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

또는 양식을 완전히 제거할 수 있습니다.


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


양식을 제거하는 또 다른 변형:


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

- 
다음 코드 조각을 사용하여 모든 양식을 삭제할 수 있습니다.


```java
Document document = new Document(input);

XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

forms.clear();

document.save(output);
```

## 
Aspose.PDF 23.11의 새로운 기능



이번 릴리스에서는 PDF 파일에서 숨겨진 텍스트를 제거할 수 있습니다:

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

## Aspose.PDF 23.10의 새로운 기능



현재 업데이트는 태그가 있는 PDF에서 태그 제거의 세 가지 버전을 제공합니다.


- 
documentElement(루트 트리 요소)에서 일부 노드 요소를 제거합니다.


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

- 
문서에서 표시된 모든 요소 태그를 제거하고 구조 요소는 유지합니다.


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

- 
태그를 전혀 제거하십시오.

```java
Document document = new Document(inputPath);
RootElement structure = document.getLogicalStructure();
Element root = structure.getChildren().get_Item(0);
root.remove();
document.save(outputPath);
```

문자 높이를 측정하는 새로운 기능을 구현했습니다. 다음 코드를 사용하여 문자의 높이를 측정합니다.


```java
Document doc = new Document("input.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.visit(doc.getPages().get_Item(1));
double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```


측정은 문서에 포함된 글꼴을 기반으로 합니다. 차원에 대한 정보가 누락된 경우 이 메서드는 0을 반환합니다.


## 
Aspose.PDF 23.9의 새로운 기능



23.9에서는 채울 수 있는 필드에서 하위 주석을 제거하는 기능이 지원됩니다.



예 1:

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

예 2:


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


ImageFilterType.Flate를 사용하여 이미지를 추가하면 투명도가 유지되지 않습니다.


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

## 
Aspose.PDF 23.8의 새로운 기능



PDF 문서에서 증분 업데이트를 감지하는 기능이 23.8에 추가되었습니다. 이 함수는 문서가 증분 업데이트로 저장된 경우 'true'를 반환하고, 그렇지 않으면 'false'를 반환합니다.


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


또 하나의 기능은 입력 PDF에서 대상 PDF로 OutputIntents 복사입니다.

문서의 출력 의도에 대한 액세스를 허용하기 위해 새로운 공용 속성 Document.getOutputIntents()를 추가합니다.


당분간은 일부 문서 출력 의도에 이미 존재하는 사용만 지원되므로 사용자는 처음부터 OutputIntent를 생성할 수 없습니다.


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


Aspose.PDF 23.8 지원에서 모양 추출을 추가합니다.


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


또한 텍스트를 추가할 때 오버플로를 감지하는 기능도 지원합니다.


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

## 
Aspose.PDF 23.7의 새로운 기능

23.7 버전부터 인쇄 대화 상자 사전 설정 페이지 크기 조정이 지원됩니다.


```java
Document document = new Document();
document.getPages().add();
document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
document.save(outputPdf);

Document documentOutput = new Document(outputPdf);
int printScaling = documentOutput.getPrintScaling();
System.out.println("PrintScaling: " + printScaling);
```

## 
Aspose.PDF 23.6의 새로운 기능



23.6 버전부터 HTML, Epub 페이지의 제목을 설정하는 기능이 추가되었습니다.



HTML 코드:


```java
HtmlSaveOptions options = new HtmlSaveOptions();
options.setFixedLayout(true);
options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
options.setTitle("</title>NEW PAGE & TITILE</head>");

Document document = new Document(inputPath);
document.save(outPath, options);
```


EPUB용 코드:

```java
EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
epubSaveOptions.setTitle("</title>NEW PAGE & TITILE</head>");
epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

Document document = new Document(inputPath);
document.save(outPath, epubSaveOptions);
```

23.6 지원부터 벡터 그래픽 위치 지정을 위한 API 제공:


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

## 
Aspose.PDF 23.1의 새로운 기능



23.1 버전부터 PrinterMark 주석 생성이 지원됩니다. 주석 변형 중 하나인 ColorBarAnnotation을 추가했습니다.


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

## 
Aspose.PDF 22.12의 새로운 기능



이번 릴리스에서는 PDF를 DICOM 이미지로 변환하는 기능이 지원됩니다.

```java
DicomDevice device = new DicomDevice(PageSize.getA4());
Document doc = new Document("Input.pdf");
ByteArrayOutputStream stream = new ByteArrayOutputStream();
device.process(doc.getPages().get_Item(1), stream);
```

## Aspose.PDF 22.9의 새로운 기능



22.09부터 주제 루브릭(E=, CN=, O=, OU=, )의 순서를 서명에 수정하기 위한 속성 추가를 지원합니다.


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

## 
Aspose.PDF 22.8의 새로운 기능



Aspose.PDF 23.8 지원에서 외부 참조 테이블 재구축을 위한 방법 추가:


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

## 
Aspose.PDF 22.6의 새로운 기능

PDF를 PDF_A_1A로 - 큰 출력 파일 크기를 피하기 위해 투명도 색상을 제거하는 옵션을 구현합니다.



버전 22.5부터 고객은 변환된 투명도의 품질과 결과적으로 출력 파일 크기를 제어할 수 있습니다.


```java
opts.setTransparencyResolution(300);
```

## 
Aspose.PDF 22.5의 새로운 기능



PDF/A 변환 중에 투명한 내용이 제거되고 이미지로 대체됩니다.


새로운 기능을 구현했으며 이제 고객은 TransparencyResolution 매개변수를 사용하여 이미지 품질을 제어할 수 있습니다.

```java
com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
options.setTransparencyResolution(300);
pdfDocument.convert(options);
pdfDocument.save("finalOutput.pdf");
```

## Aspose.PDF 22.4의 새로운 기능



이 릴리스에는 Java용 Aspose.PDF에 대한 정보가 포함되어 있습니다.


- 
PDF를 ODS로: 아래 첨자와 위 첨자로 된 텍스트를 인식합니다.



**예**


```java
Document pdfDocument = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
pdfDocument.Save("output.ods"), options);
```

- 
PDF에서 XMLSpreadSheet2003으로: 아래 첨자와 위 첨자의 텍스트를 인식합니다.

- PDF를 Excel로: 아래 첨자와 위 첨자로 된 텍스트를 인식합니다.


## 
Aspose.PDF 22.3의 새로운 기능



PDF에서 ODS로: 버전 22.3에서 RTL 지원이 가능합니다.


```java
ExcelSaveOptions options = new ExcelSaveOptions();
options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
pdfDocument.save("output.ods", options);
```

## 
Aspose.PDF 22.2의 새로운 기능



이 릴리스에는 XSLX에 대한 PDF: RTL 지원(히브리어, 아랍어)이 포함되어 있습니다.

## Aspose.PDF 22.1의 새로운 기능



Java용 Aspose.PDF를 사용하면 PDF(Portable Document Format) 버전 2.0 문서를 로드할 수 있습니다.


## 
Aspose.PDF 21.10의 새로운 기능


### 
숨겨진 텍스트를 감지하는 방법은 무엇입니까?



다음 코드를 사용하세요:

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

## Aspose.PDF 21.8의 새로운 기능


### 
디지털 서명에서 텍스트 색상을 변경하는 방법은 무엇입니까?



21.8 버전 setForegroundColor에서는 디지털 서명의 텍스트 색상을 변경할 수 있습니다.


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

## 
Aspose.PDF 21.6의 새로운 기능


### 
문서에서 ImagePlacementAbsorber를 사용하여 이미지 숨기기

Java용 Aspose.PDF를 사용하면 ImagePlacementAbsorber를 사용하여 문서에서 이미지를 숨길 수 있습니다.


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

## 
Aspose.PDF 21.5의 새로운 기능


### 
이미지 병합을 위한 API 추가



Aspose.PDF 21.4를 사용하면 이미지를 결합할 수 있습니다. 이미지 스트림 목록을 하나의 이미지 스트림으로 병합합니다. 기본적으로 Jpeg로 인코딩된 지원되지 않는 형식의 출력 스트림을 사용하는 경우 Png/jpg/tiff 출력 형식이 지원됩니다.


다음 코드 조각을 따르십시오.

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

또한 이미지를 Tiff 형식으로 병합할 수도 있습니다.


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

## 
Aspose.PDF 21.02의 새로운 기능



Aspose.PDF v21.02 PAdES LTV 서명으로 PDF에 서명

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
