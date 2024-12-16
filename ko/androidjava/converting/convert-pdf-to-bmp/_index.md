---
title: PDF를 BMP로 변환 
linktitle: PDF를 BMP로 변환
type: docs
weight: 40
url: /ko/androidjava/convert-pdf-to-bmp/
lastmod: "2021-06-05"
description: 이 문서는 PDF 페이지를 BMP 이미지로 변환하고, 모든 페이지를 BMP 이미지로 변환하며, 단일 PDF 페이지를 BMP 이미지로 변환하는 방법을 Java로 설명합니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) 클래스는 PDF 페이지를 <abbr title="Bitmap Image File">BMP</abbr> 이미지로 변환할 수 있게 해줍니다. 이 클래스는 [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process)라는 메서드를 제공하며, 이를 통해 PDF 파일의 특정 페이지를 Bmp 이미지 형식으로 변환할 수 있습니다.

{{% alert color="primary" %}}

온라인으로 시도해보세요. Aspose.PDF의 변환 품질을 확인하고 결과를 온라인에서 확인할 수 있습니다. [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

BmpDevice 클래스는 PDF 페이지를 BMP 이미지로 변환할 수 있게 해줍니다.
 이 클래스는 PDF 파일의 특정 페이지를 BMP 이미지로 변환할 수 있는 process(..)라는 메서드를 제공합니다.

## PDF 페이지를 BMP 이미지로 변환

PDF 페이지를 BMP 이미지로 변환하려면:

1. 변환하려는 특정 페이지를 얻기 위해 Document 클래스의 객체를 생성하세요.
1. 페이지를 BMP로 변환하기 위해 process(..) 메서드를 호출하세요.

다음 코드 스니펫은 특정 페이지를 BMP 이미지로 변환하는 방법을 보여줍니다.

```java
//PDF를 BMP로 변환
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // 출력 이미지를 저장할 스트림 객체 생성
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // 해상도 객체 생성
            Resolution resolution = new Resolution(300);

            // 특정 해상도로 BmpDevice 객체 생성
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // 특정 페이지를 변환하고 이미지를 스트림에 저장
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // 스트림 닫기
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## 모든 PDF 페이지를 BMP 이미지로 변환

PDF 파일의 모든 페이지를 BMP 형식으로 변환하려면 각 개별 페이지를 반복하여 BMP 형식으로 변환해야 합니다. 다음 코드 스니펫은 PDF 파일의 모든 페이지를 순회하고 이를 BMP로 변환하는 방법을 보여줍니다.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF 파일의 모든 페이지를 루프
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // 출력 이미지를 저장할 스트림 객체 생성
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // 해상도 객체 생성
            Resolution resolution = new Resolution(300);
            // 특정 해상도로 BmpDevice 객체 생성
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // 특정 페이지를 변환하고 이미지를 스트림에 저장
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // 스트림 닫기
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


## 특정 페이지 영역을 이미지(DOM)로 변환하기

우리는 Aspose.PDF의 이미지 장치 객체를 사용하여 PDF 문서를 다양한 이미지 포맷으로 변환할 수 있습니다. 그러나 때때로 특정 페이지 영역을 이미지 포맷으로 변환해야 할 때가 있습니다. 이 요구를 두 단계로 충족할 수 있습니다. 처음에는 PDF 페이지를 원하는 영역으로 자르고 나중에 원하는 이미지 장치 객체를 사용하여 이미지를 변환합니다.

다음 코드 스니펫은 PDF 페이지를 이미지로 변환하는 방법을 보여줍니다.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // 특정 페이지 영역의 사각형 가져오기
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // 원하는 페이지 영역의 사각형에 따라 CropBox 값 설정
        document.getPages().get_Item(1).setCropBox(pageRect);
        // 잘린 문서를 스트림에 저장
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // 스트림에서 잘린 PDF 문서를 열고 이미지를 변환
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // 해상도 객체 생성
        Resolution resolution = new Resolution(300);
        // 지정된 속성으로 BMP 장치 생성
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // 특정 페이지를 변환하고 이미지를 스트림에 저장
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```