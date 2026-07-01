---
title: PDF를 JPG로 변환
linktitle: PDF를 JPG로 변환
type: docs
weight: 10
url: /ko/androidjava/convert-pdf-to-jpg/
description:  이 페이지에서는 PDF 페이지를 JPEG 이미지로 변환하는 방법, Aspose.PDF for Android via Java를 사용하여 모든 페이지와 단일 페이지를 JPEG 이미지로 변환하는 방법을 설명합니다.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 페이지를 JPG 이미지로 변환

JpegDevice 클래스는 PDF 페이지를 JPEG 이미지로 변환할 수 있게 해줍니다. 이 클래스는 process(..)라는 메서드를 제공하며, 이를 사용하여 PDF 파일의 특정 페이지를 JPEG 이미지로 변환할 수 있습니다.

{{% alert color="primary" %}}

온라인으로 시도해 보세요. Aspose.PDF 변환 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다.  [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## 단일 PDF 페이지를 JPG 이미지로 변환

Aspose.PDF for Android via Java은 단일 페이지를 Jpeg 형식으로 변환할 수 있도록 합니다.

한 페이지만 JPEG 이미지로 변환하려면:

1. 변환하려는 페이지를 가져오기 위해 Document 클래스의 객체를 생성합니다.
1. process(..) 메서드를 호출하여 페이지를 JPEG 이미지로 변환합니다.

다음 코드 스니펫은 PDF의 첫 페이지를 Jpeg 형식으로 변환하는 단계들을 보여줍니다.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create JpegDevice object with particular resolution
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## 모든 PDF 페이지를 JPG 이미지로 변환합니다

Aspose.PDF for Android via Java를 사용하면 PDF 파일의 모든 페이지를 이미지로 변환할 수 있습니다:

1. 파일의 모든 페이지를 순회합니다.
1. 각 페이지를 개별적으로 변환합니다:
    - PDF 문서를 로드하기 위해 Document 클래스의 객체를 생성합니다.
    - 변환하려는 페이지를 가져옵니다.
    - 페이지를 Jpeg로 변환하기 위해 Process 메서드를 호출합니다.

다음 코드 스니펫은 모든 PDF 페이지를 Jpeg 이미지로 변환하는 방법을 보여줍니다.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create JpegDevice object with particular resolution
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Close the stream
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```

## 특정 PDF 페이지를 JPG 이미지로 변환합니다

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get rectangle of particular page region
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // set CropBox value as per rectangle of desired page region
        document.getPages().get_Item(1).setCropBox(pageRect);
        // save cropped document into stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // open cropped PDF document from stream and convert to image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create Jpeg device with specified attributes
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
