---
title: PDF를 BMP로 변환
linktitle: PDF를 BMP로 변환
type: docs
weight: 40
url: /ko/androidjava/convert-pdf-to-bmp/
lastmod: "2026-07-01"
description: 이 문서는 PDF 페이지를 BMP 이미지로 변환하는 방법, 모든 페이지를 BMP 이미지로 변환하는 방법 및 Java를 사용하여 단일 PDF 페이지를 BMP 이미지로 변환하는 방법을 설명합니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

그 [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) 클래스는 PDF 페이지를 변환하도록 허용합니다 <abbr title="Bitmap Image File">BMP</abbr> 이미지. 이 클래스는 이름이 지정된 메서드를 제공합니다 [프로세스](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) 특정 PDF 파일 페이지를 Bmp 이미지 형식으로 변환할 수 있게 합니다.

{{% alert color="primary" %}}

온라인으로 시도해 보세요. Aspose.PDF 변환 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다. [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

BmpDevice 클래스는 PDF 페이지를 BMP 이미지로 변환할 수 있게 해줍니다. 이 클래스는 process(..) 라는 메서드를 제공하며, 이를 통해 PDF 파일의 특정 페이지를 BMP 이미지로 변환할 수 있습니다.

## PDF 페이지를 BMP 이미지로 변환

PDF 페이지를 BMP 이미지로 변환하려면:

1. 변환하려는 특정 페이지를 얻기 위해 Document 클래스의 객체를 생성합니다.
1. 페이지를 BMP로 변환하려면 process(..) 메서드를 호출합니다.

다음 코드 스니펫은 특정 페이지를 BMP 이미지로 변환하는 방법을 보여줍니다.

```java
//Convert PDF to BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## 모든 PDF 페이지를 BMP 이미지로 변환

PDF 파일의 모든 페이지를 BMP 형식으로 변환하려면 각 개별 페이지를 가져와 BMP 형식으로 변환하도록 반복해야 합니다. 다음 코드 스니펫은 PDF 파일의 모든 페이지를 순회하며 BMP로 변환하는 방법을 보여 줍니다.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

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

## 특정 페이지 영역을 이미지(DOM)로 변환

Aspose.PDF의 이미지 디바이스 객체를 사용하여 PDF 문서를 다양한 이미지 형식으로 변환할 수 있습니다. 그러나 때때로 특정 페이지 영역을 이미지 형식으로 변환해야 하는 요구가 있습니다. 이 요구는 두 단계로 해결할 수 있습니다. 먼저 PDF 페이지를 원하는 영역으로 잘라낸 다음, 원하는 이미지 디바이스 객체를 사용하여 이미지를 변환합니다.

다음 코드 스니펫은 PDF 페이지를 이미지로 변환하는 방법을 보여줍니다.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
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
        // Create BMP device with specified attributes
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```
