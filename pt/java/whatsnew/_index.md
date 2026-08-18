---
title: O que há de novo
linktitle: O que há de novo
type: docs
weight: 10
url: /java/whatsnew/
description: Nesta página apresentamos os novos recursos mais populares do Aspose.PDF para Java que foram introduzidos em versões recentes.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Novos recursos populares em Aspose.PDF para Java
Abstract: A seção Novidades da documentação do Aspose.PDF para Java fornece uma visão geral das atualizações, aprimoramentos e correções de bugs mais recentes introduzidas em versões recentes. Ele destaca novos recursos, melhorias de desempenho e atualizações de compatibilidade para ajudar os desenvolvedores a se manterem informados sobre os últimos avanços no processamento de PDF. A documentação também inclui detalhes sobre funcionalidades obsoletas e alternativas recomendadas. Ao revisar regularmente esta seção, os desenvolvedores podem garantir que estão utilizando os recursos mais eficientes e atualizados em seus aplicativos Java para um gerenciamento perfeito de PDF.
SoftwareApplication: java
---
## O que há de novo no Aspose.PDF 25.12

### Anotações de texto livre com rotação arbitrária em XFDF

Foi adicionado suporte para ângulos de rotação arbitrários para anotações de texto livre no XFDF, tornando os layouts de anotações importados e exportados mais flexíveis.

```java
Document pdfDocument = new Document(inputPdf);
com.aspose.pdf.facades.PdfAnnotationEditor editor = new PdfAnnotationEditor();
editor.bindPdf(pdfDocument);
editor.importAnnotationsFromXfdf(inputXfdf);
editor.save(output);
```

## O que há de novo no Aspose.PDF 25.11

### Melhorias na limpeza de dados ocultos

A limpeza aprimorada de PDF agora está disponível por meio do HiddenDataSanitizer para melhorar a remoção de conteúdo oculto dos documentos.

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

### Redução aprimorada do tamanho do arquivo durante a otimização de PDF

A otimização de PDF agora melhora a redução do tamanho do arquivo, refinando a forma como o subconjunto de fontes é tratado.

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

## O que há de novo no Aspose.PDF 25.10

### Suporte para conversão de PDF para PDF/E

Aspose.PDF para Java agora suporta a conversão de documentos PDF para o formato PDF/E.

```java
Document document = new Document(inputPdf);
document.convert(conversionLog, PdfFormat.PDF_E_1, ConvertErrorAction.Delete);
document.save(outputPdf);
```

### Texto HTML em anotações

Foi adicionado suporte para adicionar texto HTML dentro de anotações.

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

## O que há de novo no Aspose.PDF 25.9

### Plug-ins de HTML para PDF

Aspose.PDF para Java agora inclui plug-ins HTML para PDF para simplificar os fluxos de trabalho de processamento de HTML para PDF.

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

### Suporte à conformidade do PDF 1.6

O suporte para conformidade com PDF 1.6 foi adicionado para cenários que exigem esta versão do documento.

## O que há de novo no Aspose.PDF 25.8

### Suporte para estilo de borda de tabela

Foi adicionado suporte para estilos de borda de tabela para fornecer mais controle sobre a aparência da tabela.

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

### Extração de texto ALT para imagens em PDF

Agora você pode obter descrições de texto ALT para imagens em documentos PDF, o que ajuda no processamento orientado para acessibilidade.

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

## O que há de novo no Aspose.PDF 25.7

### Plug-in PDF ChatGPT

Aspose.PDF para Java agora inclui um plug-in PDF ChatGPT para cenários de interação de IA com foco em PDF.

O exemplo demonstra como usar o plugin PdfChatGpt adicionando arquivo(s) como fonte da mensagem:

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

O exemplo demonstra como usar o plugin PdfChatGpt adicionando mensagens à solicitação:

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

O exemplo demonstra como usar o plugin PdfChatGpt adicionando uma mensagem à solicitação:

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

## O que há de novo no Aspose.PDF 25.6

### Formatação aprimorada de saída de PDF para DOCX

A conversão de PDF para DOCX foi aprimorada para documentos cujo formato de saída estava incorreto anteriormente.

```java
Document doc = new Document(dataDir + "SD_Aspose.pdf");
DocSaveOptions saveOption = new DocSaveOptions();
saveOption.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
saveOption.setFormat(DocSaveOptions.DocFormat.DocX);
saveOption.setRecognizeBullets(true);
doc.save(dataDir + "SD_Aspose.docx", saveOption);
```

## O que há de novo no Aspose.PDF 25.5

### Preservar imagens em PDF para conversão ODS

As imagens agora são preservadas ao converter documentos PDF em ODS.

```java
Document doc = new Document("input.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
doc.save("output.ods", options);
```

### Criação automática de tags durante a conversão de PDF para PDF/A

A conversão de PDF para PDF/A agora oferece suporte à criação automática de tags para melhorar os resultados da marcação no documento de saída.

```java
Document document = new Document(dataDir+"source.pdf");

PdfFormat format = PdfFormat.PDF_A_1A;
PdfFormatConversionOptions options = new PdfFormatConversionOptions(format, ConvertErrorAction.Delete);
options.setAutoTaggingSettings(AutoTaggingSettings.getDefault());

document.convert(options);
document.save(dataDir+"out_"+BuildVersionInfo.ASSEMBLY_VERSION+"_"+format+"_"+document.getFileName());
document.close();
```

## O que há de novo no Aspose.PDF 25.4

### Preservar hiperlinks na conversão de PDF para XLSX

Os hiperlinks agora são preservados na conversão de documentos PDF para XLSX, melhorando a navegação nas planilhas exportadas.

```java
Document doc = new Document("input.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
doc.save("output.xlsx", options);
```

## O que há de novo no Aspose.PDF 25.3

Desde a versão 25.2 foi adicionada a capacidade de detectar comprometimento de assinaturas digitais de PDF. Você pode usar a classe 'SignaturesCompromiseDetector' para verificar se há comprometimento de assinaturas digitais. Chame o método check() para verificar as assinaturas do documento. Se nenhum comprometimento de assinatura for detectado, o método retornará verdadeiro. Para verificar se as assinaturas existentes cobrem todo o documento, utilize a 'propriedade SignaturesCoverage'.

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

## O que há de novo no Aspose.PDF 25.2

Desde a versão 25.2 foi adicionada a capacidade de converter PDF para o formato de arquivo PDF/X-4:

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

Desde a versão 25.2, é possível centralizar o alinhamento do HTML de saída:

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

Além disso, desde a versão 25.2, é possível obter a subida e descida de um texto de acordo com a fonte e tamanho com Aspose.PDF. O novo recurso foi implementado na classe ‘com.aspose.pdf.Font’.

Métodos adicionados:

**Mede o ponto máximo de subida**

-public double getAscentPoint(String str, float fontSize)

**Mede o ponto máximo de descida**

- público duplo getDescentPoint(String str, float fontSize)

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

## O que há de novo no Aspose.PDF 25.1

A capacidade de passar o caminho para o perfil ICC externo para conversão de PDF/X e PDF/A já existe na biblioteca há alguns anos, habilitada pela propriedade PdfFormatConversionOptions.IccProfileFileName. Agora também é possível passar dados para preencher as propriedades OutputIntent usando um objeto da classe OutputIntent.

O trecho a seguir mostra como converter um documento de anotação em PDF/X-1 usando o perfil ICC de anotação FOGRA39:

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

Desde a versão 25.1 foi adicionada a capacidade de obter informações sobre privilégios ao usar documentos:

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

## O que há de novo no Aspose.PDF 24.12

Desde a versão 24.12, é possível oferecer suporte a pares de caracteres substitutos.

O termo 'par substituto' refere-se à codificação de caracteres Unicode com pontos de código elevados no esquema de codificação UTF-16.

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

Desde a versão 24.12, é possível converter documentos PDF em PDF/A-4. A parte 4 do padrão, baseada no PDF 2.0, foi publicada no final de 2020.

O trecho de código a seguir demonstra como converter um documento no formato PDF/A-4 quando o documento de entrada é uma versão PDF anterior à 2.0.

```java
Document document = new Document(inputPdf);
// Only PDF-2.x documents can be converted to PDF/A-4
document.convert("log1.xml", PdfFormat.v_2_0, ConvertErrorAction.Delete);
document.save(tmpOutputFile);

document = new Document(tmpOutputFile);
document.convert("log2.xml", PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
document.save("output.pdf");
```

## O que há de novo no Aspose.PDF 24.9

Nesta versão é possível criar um PDF acessível usando funções de baixo nível:

O próximo trecho de código funciona com um documento PDF e seu conteúdo marcado, utilizando uma biblioteca Aspose.PDF para processá-lo.

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

A classe `GraphicalPdfComparer` é adicionada para comparação gráfica de documentos e páginas PDF. A comparação gráfica trata de imagens de páginas de documentos. Retorna o resultado como um objeto `ImagesDifference` ou como um documento PDF que contém imagens mescladas do original e as diferenças. A comparação gráfica é mais útil para documentos que apresentam pequenas diferenças no texto ou no conteúdo gráfico.

O trecho de código a seguir demonstra a comparação gráfica de dois documentos PDF e salva uma imagem com as diferenças no documento PDF resultante:

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

## O que há de novo no Aspose.PDF 24.8

Desde 24.8, suporte para o formato PDF/A-4:

```java
Document document = new Document(inputPdf);
// Only PDF-2.x documents can be converted to PDF/A-4
document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
document.save(outputFile);
```

Além disso, é possível adicionar texto alternativo para o Image Stamp:

A propriedade AlternativeText foi adicionada ao ImageStamp - se um valor for atribuído a ela, então, ao adicionar um ImageStamp a um documento, ele terá Texto Alternativo.

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

Além disso, o código a seguir mostra como adicionar AlternativeText nas imagens existentes em FigureElements.

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

## O que há de novo no Aspose.PDF 24.7

Desde a versão 24.7, como parte da edição do PDF marcado, foram adicionados métodos em **Aspose.Pdf.LogicalStructure.Element**:

- Tag (adicione tags a operadores específicos, como imagens, texto e links)
- Inserir Filho
- RemoverCriança
- ClearChilds

Esses métodos permitem editar tags de arquivos PDF, por exemplo:

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

## O que há de novo no Aspose.PDF 24.6

Desde 24.6 Aspose.PDF para Java permite assinar PDF com java.security.cert.X509Certificate, java.security.PrivateKey:

Este código recupera um certificado e uma chave privada do armazenamento de certificados e os utiliza para aplicar uma assinatura digital à primeira página de um documento PDF.

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

## O que há de novo no Aspose.PDF 24.5

Desde a versão 24.5, os plug-ins do Editor de Formulários foram implementados.

**Como editar formulários em PDF usando o Editor de formulários**

- Defina suas chaves de licença
- Crie uma instância da classe FormEditor, que fornece métodos para manipular formulários PDF
- Crie uma instância da classe FormEditorAddOptions, que especifica as opções para adicionar campos de formulário a um documento PDF
- Adicione uma origem de arquivo de entrada e uma origem de arquivo de saída ao objeto FormEditorAddOptions, usando a classe FileDataSource que representa um caminho de arquivo ou fluxo
- Chame o método Process do objeto FormEditor, passando o objeto FormEditorAddOptions como parâmetro
- Acesse o resultado usando ResultContainer.resultCollection

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

Esta versão nos permite trabalhar com camadas de PDF. Por exemplo:

- bloquear uma camada PDF
- extrair elementos da camada PDF
- achatar um PDF em camadas
- mesclar todas as camadas dentro do PDF em uma

**Bloquear uma camada de PDF**

Desde a versão 24.5, você pode abrir um PDF, bloquear uma camada específica na primeira página e salvar o documento com as alterações. Existem dois novos métodos e uma propriedade foi adicionada:

Camada.Lock(); - Bloqueia a camada.
Camada.Unlock(); - Desbloqueia a camada.
Camada.Bloqueada; - Propriedade, indicando o estado bloqueado da camada.

```java
Document document = new Document(input);
Page page = document.getPages().get_Item(1);
Layer layer = page.getLayers().get(0);

layer.lock();

document.save(output);
```

**Extraia elementos da camada PDF**

A biblioteca Aspose.PDF para Java permite extrações de cada camada da primeira página e salva cada camada em um arquivo separado.

Para criar um novo PDF a partir de uma camada, o seguinte trecho de código pode ser usado:

```java
Document document = new Document(inputPath);
java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

for (Layer layer : layers)
{
    layer.save(outputPath);
}
```

**Achate um PDF em camadas**

A biblioteca Aspose.PDF para Java abre um PDF, percorre cada camada da primeira página e nivela cada camada, tornando-a permanente na página.

```java
Document document = new Document(input);
Page page = document.getPages().get_Item(1);

for (Layer layer : page.getLayers())
{
    layer.flatten(true);
}
document.save(output);
```

O método Layer.flatten(boolean cleanupContentStream) aceita o parâmetro booleano que especifica se os marcadores de grupo de conteúdo opcionais devem ser removidos do fluxo de conteúdo.
Definir o parâmetro cleanupContentStream como false acelera o processo de nivelamento.

**Mesclar todas as camadas dentro do PDF em uma só**

A biblioteca Aspose.PDF para Java permite mesclar todas as camadas do PDF ou uma camada específica na primeira página em uma nova camada e salvar o documento atualizado.

Dois métodos foram adicionados para mesclar todas as camadas da página:

- void mergeLayers(String newLayerName);
- void mergeLayers(String newLayerName, String newOptionalContentGroupId);

O segundo parâmetro permite renomear o marcador opcional do grupo de conteúdo. O valor padrão é "oc1" (/OC /oc1 BDC).

```java
Document document = new Document(input);
Page page = document.getPages().get_Item(1);
page.mergeLayers("NewLayerName");

// Or page.mergeLayers("NewLayerName", "OC1");

document.save(output);
```

## O que há de novo no Aspose.PDF 24.4

Esta versão introduziu plug-ins Java para PDF:

- Plug-in de nivelamento de formulário

```java
FormFlattener pdfFormPlugin = new FormFlattener();

FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

opt.addInput(new FileDataSource("sample.pdf"));
opt.addOutput(new FileDataSource("sample-flat.pdf"));

ResultContainer result = pdfFormPlugin.process(opt);

// Check result.
java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- Exportador de formulários

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

- Plug-in de fusão

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

- Plug-in otimizador

Como reduzir o tamanho dos documentos PDF?

```java
String input = "Test.pdf";
String output = "Optimized.pdf";

Optimizer optimizer = new Optimizer();

OptimizeOptions opt = new OptimizeOptions();
opt.addInput(new FileDataSource(input));
opt.addOutput(new FileDataSource(output));

optimizer.process(opt);
```

Como redimensionar documentos PDF?

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

Como girar documentos PDF?

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

## O que há de novo no Aspose.PDF 24.3

A partir de 24.3 implemente uma busca através de uma lista de frases em um TextFragmentAbsorber.

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

O próximo recurso é adicionar a capacidade de converter tabelas para o conversor de PDF para Markdown

```java
Document doc = new Document(dataDir + "56201.pdf");
MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
doc.save(dataDir + "56201.md", saveOptions);
```

## O que há de novo no Aspose.PDF 24.2

A partir de 24.2 é possível adicionar marca d'água em PDF com AcroForms. TextStamp é adequado para uso com arquivos AcroForm. Se você usar TextStamp para arquivos XFA, o texto será desenhado na página como em um arquivo PDF normal (isso pode ser visto nos visualizadores de PDF que não conseguem ler arquivos XFA, por exemplo, em um navegador Chrome). Para adicionar texto ao arquivo XFA, ele deve ser alterado no XML interno do arquivo XFA.

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

Definir StateModel para anotação
Podemos usar setReviewState e setMarkedState da classe MarkupAnnotation para definir o estado necessário.
Todas as anotações de marcação têm uma opção Definir estado disponível.

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

A partir de 24.2 implemente a conversão de OFD para PDF:

```java
Document document = new Document(inputPath, new OfdLoadOptions());
document.save(outputPath);
```

## O que há de novo no Aspose.PDF 24.1

A partir da versão 24.1, implemente a conversão de PDF para Markdown:

```java
final Document doc = new Document(inputPdfPath);
MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
doc.save(markdownOutputFilePath, saveOptions);
```

Além disso, em 24.1, a interrupção do thread usando o InterruptMonitor foi implementada.

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

## O que há de novo no Aspose.PDF 23.12

O formulário pode ser encontrado e o texto pode ser substituído usando o seguinte trecho de código:

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

Ou o formulário pode ser completamente removido:

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

Outra variante de remoção do formulário:

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

- Todos os formulários podem ser excluídos usando o seguinte trecho de código:

```java
Document document = new Document(input);

XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

forms.clear();

document.save(output);
```

## O que há de novo no Aspose.PDF 23.11

A partir desta versão é possível remover texto oculto do arquivo PDF:

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

## O que há de novo no Aspose.PDF 23.10

A atualização atual apresenta três versões de Remoção de tags de PDFs marcados.

- Remova algum elemento de nó de um documentElement (elemento da árvore raiz):

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

- Remova todas as tags dos elementos marcados do documento, mas mantenha os elementos da estrutura:

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

- Remova as tags:

```java
Document document = new Document(inputPath);
RootElement structure = document.getLogicalStructure();
Element root = structure.getChildren().get_Item(0);
root.remove();
document.save(outputPath);
```

Implementamos um novo recurso para medir a altura dos caracteres. Use o seguinte código para medir a altura de um caractere:

```java
Document doc = new Document("input.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.visit(doc.getPages().get_Item(1));
double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```

Observe que a medição é baseada na fonte incorporada no documento. Se alguma informação de uma dimensão estiver faltando, este método retornará 0.

## O que há de novo no Aspose.PDF 23.9

A partir da versão 23.9, suporte para remover uma anotação filha de um campo preenchível.

exemplo 1:

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

exemplo 2:

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

Adicionar imagem com ImageFilterType.Flate não preserva a transparência.

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

## O que há de novo no Aspose.PDF 23.8

A função para detectar atualizações incrementais em um documento PDF foi adicionada na versão 23.8. Esta função retorna 'true' onde o documento foi salvo com atualizações incrementais, caso contrário, retorna 'false'.

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

Mais um recurso é Copiar OutputIntents do PDF de entrada para o PDF de destino

Adicionamos uma nova propriedade pública Document.getOutputIntents() para permitir acesso às intenções de saída em um documento.
Por enquanto, apenas o uso de intenções de saída já existentes em alguns documentos é suportado, o usuário não pode criar OutputIntent do zero.

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

Do suporte Aspose.PDF 23.8 para adicionar a extração de forma:

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

Também suporta a capacidade de detectar Overflow ao adicionar texto:

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

## O que há de novo no Aspose.PDF 23.7

A partir da versão 23.7, há suporte para o dimensionamento da página de predefinições da caixa de diálogo de impressão:

```java
Document document = new Document();
document.getPages().add();
document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
document.save(outputPdf);

Document documentOutput = new Document(outputPdf);
int printScaling = documentOutput.getPrintScaling();
System.out.println("PrintScaling: " + printScaling);
```

## O que há de novo no Aspose.PDF 23.6

A partir da versão 23.6 suporta a adição da capacidade de definir o título da página HTML, Epub.

código para HTML:

```java
HtmlSaveOptions options = new HtmlSaveOptions();
options.setFixedLayout(true);
options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
options.setTitle("</title>NEW PAGE & TITILE</head>");

Document document = new Document(inputPath);
document.save(outPath, options);
```

código para EPUB:

```java
EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
epubSaveOptions.setTitle("</title>NEW PAGE & TITILE</head>");
epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

Document document = new Document(inputPath);
document.save(outPath, epubSaveOptions);
```

A partir do suporte 23.6 para fornecer uma API para posicionamento de gráficos vetoriais:

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

## O que há de novo no Aspose.PDF 23.1

A partir da versão 23.1, suporte para criação de anotações PrinterMark. Adicionada uma das variantes de anotação: ColorBarAnnotation.

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

## O que há de novo no Aspose.PDF 22.12

A partir desta versão, suporte para converter PDF em imagem DICOM:

```java
DicomDevice device = new DicomDevice(PageSize.getA4());
Document doc = new Document("Input.pdf");
ByteArrayOutputStream stream = new ByteArrayOutputStream();
device.process(doc.getPages().get_Item(1), stream);
```

## O que há de novo no Aspose.PDF 22.9

A partir de 22.09, suporte para adição de propriedade para modificar a ordem das rubricas do assunto (E=, CN=, O=, OU=, ) na assinatura.

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

## O que há de novo no Aspose.PDF 22.8

Do suporte do Aspose.PDF 23.8 para adicionar método para reconstruir a tabela refex:

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

## O que há de novo no Aspose.PDF 22.6

PDF para PDF_A_1A - implementa a opção para remover a cor da transparência para evitar arquivos de saída grandes.

A partir da versão 22.5, o cliente é capaz de controlar a qualidade da transparência convertida e, como resultado, o tamanho do arquivo de saída:

```java
opts.setTransparencyResolution(300);
```

## O que há de novo no Aspose.PDF 22.5

Durante a conversão de PDF/A, o conteúdo transparente é removido e substituído por imagem.
Implementamos uma nova funcionalidade, e agora o cliente pode controlar a qualidade da imagem com o parâmetro TransparencyResolution:

```java
com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
options.setTransparencyResolution(300);
pdfDocument.convert(options);
pdfDocument.save("finalOutput.pdf");
```

## O que há de novo no Aspose.PDF 22.4

Esta versão inclui informações para Aspose.PDF para Java:

- PDF para ODS: Reconhece texto em subscrito e sobrescrito;

**exemplo**

```java
Document pdfDocument = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
pdfDocument.Save("output.ods"), options);
```

- PDF para XMLSpreadSheet2003: Reconhece texto em subscrito e sobrescrito;

- PDF para Excel: Reconhecer texto subscrito e sobrescrito;

## O que há de novo no Aspose.PDF 22.3

PDF para ODS: suporte para RTL está disponível na versão 22.3

```java
ExcelSaveOptions options = new ExcelSaveOptions();
options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
pdfDocument.save("output.ods", options);
```

## O que há de novo no Aspose.PDF 22.2

Esta versão inclui PDF para XSLX: Suporte para RTL (hebraico, árabe).

## O que há de novo no Aspose.PDF 22.1

Aspose.PDF para Java permite carregar documentos Portable Document Format (PDF) versão 2.0.

## O que há de novo no Aspose.PDF 21.10

### Como detectar texto oculto?

Por favor, use o seguinte código:

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

## O que há de novo no Aspose.PDF 21.8

### Como alterar a cor do texto na Assinatura Digital?

Na versão 21.8 setForegroundColor, permite alterar a cor do texto na Assinatura Digital:

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

## O que há de novo no Aspose.PDF 21.6

### Ocultando imagem usando ImagePlacementAbsorber do documento

Com Aspose.PDF for Java você pode ocultar imagens usando ImagePlacementAbsorber do documento:

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

## O que há de novo no Aspose.PDF 21.5

### Adicionar API para mesclar imagens

Aspose.PDF 21.4 permite combinar imagens. Mescla a lista de fluxos de imagens como um único fluxo de imagens. Os formatos de saída Png/jpg/tiff são suportados, no caso de usar fluxo de saída de formato não suportado codificado como Jpeg por padrão.
Siga o próximo trecho de código:

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

Além disso, você pode mesclar suas imagens no formato Tiff:

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

## O que há de novo no Aspose.PDF 21.02

Aspose.PDF v21.02 Assine PDF com assinaturas PAdES LTV

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
