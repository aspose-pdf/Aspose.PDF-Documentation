---
title: PDF를 PNG로 변환
linktitle: PDF를 PNG로 변환
type: docs
weight: 20
url: /ko/androidjava/convert-pdf-to-png/
lastmod: "2026-07-01"
description: 이 페이지에서는 PDF 페이지를 PNG 이미지로 변환하는 방법과 Aspose.PDF for Android via Java를 사용하여 전체 페이지와 개별 페이지를 PNG 이미지로 변환하는 방법을 설명합니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 페이지를 변환하기 위해 **Aspose.PDF for Android via Java** 라이브러리를 사용하십시오 <abbr title="Portable Network Graphics">PNG</abbr> 이미지를 접근 가능하고 편리한 방식으로.

PngDevice 클래스는 PDF 페이지를 PNG 이미지로 변환할 수 있게 해줍니다. 이 클래스는 Process라는 메서드를 제공하며, 이를 통해 PDF 파일의 특정 페이지를 PNG 이미지 형식으로 변환할 수 있습니다.

## PDF 페이지를 PNG 이미지로 변환

PDF 파일의 모든 페이지를 PNG 파일로 변환하려면 개별 페이지를 반복해서 각 페이지를 PNG 형식으로 변환합니다. 다음 코드 스니펫은 PDF 파일의 모든 페이지를 탐색하고 각 페이지를 PNG 이미지로 변환하는 방법을 보여줍니다.

{{% alert color="primary" %}} 

온라인으로 시도해 보세요. Aspose.PDF 변환 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다. [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## 단일 PDF 페이지를 PNG 이미지로 변환

Process(..) 메서드에 페이지 인덱스를 인수로 전달합니다.
다음 코드 스니펫은 PDF의 첫 페이지를 PNG 형식으로 변환하는 단계를 보여줍니다.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create PngDevice object with particular resolution
            PngDevice PngDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## 모든 PDF 페이지를 PNG 이미지로 변환

Aspose.PDF for Android via Java는 PDF 파일의 모든 페이지를 이미지로 변환하는 방법을 보여줍니다:

1. 파일의 모든 페이지를 순회합니다.
1. 각 페이지를 개별적으로 변환합니다:
    1. PDF 문서를 로드하기 위해 Document 클래스의 객체를 생성합니다.
    1. 변환하려는 페이지를 가져옵니다.
    1. 페이지를 Png로 변환하기 위해 Process 메서드를 호출합니다.

다음 코드 조각은 모든 PDF 페이지를 PNG 이미지로 변환하는 방법을 보여줍니다.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
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
            PngDevice JpegDevice = new PngDevice(resolution);

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

## 특정 PDF 페이지를 PNG 이미지로 변환

Aspose.PDF for Android via Java는 특정 페이지를 PNG 형식으로 변환하는 방법을 보여줍니다:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
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
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
