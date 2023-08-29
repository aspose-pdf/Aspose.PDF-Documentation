---
title: What's new 
linktitle: What's new
type: docs
weight: 10
url: /java/whatsnew/
description: In this page introduces the most popular new features in Aspose.PDF for Java that have been introduced in recent releases.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-06-05"
---

## What's new in Aspose.PDF 23.6

From 23.6 version support the add the ability to set the title of the HTML, Epub page.

code for HTML:

```java

    HtmlSaveOptions options = new HtmlSaveOptions();
    options.setFixedLayout(true);
    options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
    options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
    options.setTitle("</title>NEW PAGE & TITILE</head>");

    Document document = new Document(inputPath);
    document.save(outPath, options);
```

code for EPUB:

```java

    EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
    epubSaveOptions.setTitle("</title>NEW PAGE & TITILE</head>");
    epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

    Document document = new Document(inputPath);
    document.save(outPath, epubSaveOptions);
```

From 23.6 support to provide an API for positioning vector graphics:

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
## What's new in Aspose.PDF 23.1

From 23.1 version support to create PrinterMark annotation. Added one of the annotation variant: ColorBarAnnotation.

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

## What's new in Aspose.PDF 22.12

From this release support to convert PDF to DICOM Image:


```java

    DicomDevice device = new DicomDevice(PageSize.getA4());
    Document doc = new Document("Input.pdf");
    ByteArrayOutputStream stream = new ByteArrayOutputStream();
    device.process(doc.getPages().get_Item(1), stream);
```

## What's new in Aspose.PDF 22.9

From 22.09 support adding property for modify the order of the subject rubrics (E=, CN=, O=, OU=, ) into the signature.

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
## What's new in Aspose.PDF 22.8

From Aspose.PDF 23.8 support to add method for rebuild xref table:

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


## What's new in Aspose.PDF 22.6

PDF to PDF_A_1A - implement option to remove transparency color to avoid large output file size.

From version 22.5 customer is able to control quality of converted transparency, and the output file size as a result:

```java
    opts.setTransparencyResolution(300);
```

## What's new in Aspose.PDF 22.5

During PDF/A conversion transparent content is removed and replaced with image.
We have implemented a new feature, and now the customer can control the quality of the image with the parameter TransparencyResolution:

```java

    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
    PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
    options.setTransparencyResolution(300);
    pdfDocument.convert(options);
    pdfDocument.save("finalOutput.pdf");
```        

## What's new in Aspose.PDF 22.4

This release includes information for Aspose.PDF for Java:

- PDF to ODS: Recognize text in subscript and superscript;

**example**

```java

    Document pdfDocument = new Document("Superscript-Subscript.pdf");
    ExcelSaveOptions options = new ExcelSaveOptions();
    options.Format = ExcelSaveOptions.ExcelFormat.ODS;
    pdfDocument.Save("output.ods"), options);
```

- PDF to XMLSpreadSheet2003: Recognize text in subscript and superscript;

- PDF to Excel: Recognize text in subscript and superscript;

## What's new in Aspose.PDF 22.3

PDF to ODS: Support for RTL is available in version 22.3

```java

    ExcelSaveOptions options = new ExcelSaveOptions();
    options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    pdfDocument.save("output.ods", options);
```

## What's new in Aspose.PDF 22.2

This release includes the PDF to XSLX: Support for RTL (Hebrew, Arabic).

## What's new in Aspose.PDF 22.1

Aspose.PDF for Java allows loading documents Portable Document Format (PDF) version 2.0.

## What's new in Aspose.PDF 21.10

### How to detect hidden text?

Please use the following code:

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

## What's new in Aspose.PDF 21.8

### How to change text color in Digital Signature?

In the 21.8 version  setForegroundColor, it allows changing text color in Digital Signature:

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

## What's new in Aspose.PDF 21.6

### Hiding image using ImagePlacementAbsorber from the document

With Aspose.PDF for Java you can hide images using ImagePlacementAbsorber from the document:

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

## What's new in Aspose.PDF 21.5

### Add API for merging images

Aspose.PDF 21.4 allows you to combine Images. Merges list of image streams as one image stream. Png/jpg/tiff outputs formats are supported, in case of using non supported format output stream encoded as Jpeg by default.
Follow the next code snippet:

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

## What's new in Aspose.PDF 21.02

Aspose.PDF v21.02 Sign PDF with PAdES LTV Signatures

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