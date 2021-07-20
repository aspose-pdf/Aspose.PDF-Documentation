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