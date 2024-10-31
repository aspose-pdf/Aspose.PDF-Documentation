---
title: PDF를 JPG로 변환하기
linktitle: PDF를 JPG로 변환하기
type: docs
weight: 10
url: /androidjava/convert-pdf-to-jpg/
description: 이 페이지는 Aspose.PDF for Android via Java를 사용하여 PDF 페이지를 JPEG 이미지로 변환하는 방법과 모든 페이지와 단일 페이지를 JPEG 이미지로 변환하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 페이지를 JPG 이미지로 변환하기

JpegDevice 클래스는 PDF 페이지를 JPEG 이미지로 변환할 수 있게 합니다. 이 클래스는 process(..)라는 메소드를 제공하여 PDF 파일의 특정 페이지를 JPEG 이미지로 변환할 수 있습니다.

{{% alert color="primary" %}}

온라인으로 시도해보세요. 이 링크에서 Aspose.PDF 변환의 품질을 확인하고 결과를 온라인으로 볼 수 있습니다 [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}

## 단일 PDF 페이지를 JPG 이미지로 변환하기

Aspose.PDF for Android via Java를 사용하면 단일 페이지를 Jpeg 형식으로 변환할 수 있습니다.

단일 페이지를 JPEG 이미지로 변환하려면:

1. 변환하려는 페이지를 가져오기 위해 Document 클래스의 객체를 생성합니다.
2. 페이지를 JPEG 이미지로 변환하기 위해 process(..) 메서드를 호출합니다.

다음 코드 스니펫은 PDF의 첫 번째 페이지를 JPEG 형식으로 변환하는 단계들을 보여줍니다.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // 출력 이미지를 저장하기 위한 스트림 객체를 생성합니다
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // 해상도 객체를 생성합니다
            Resolution resolution = new Resolution(300);

            // 특정 해상도의 JpegDevice 객체를 생성합니다
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // 특정 페이지를 변환하고 이미지를 스트림에 저장합니다
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // 스트림을 닫습니다
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## 모든 PDF 페이지를 JPG 이미지로 변환

Aspose.PDF for Android via Java를 사용하여 PDF 파일의 모든 페이지를 이미지로 변환할 수 있습니다:

1. 파일의 모든 페이지를 순회합니다.
2. 각 페이지를 개별적으로 변환합니다:
    - PDF 문서를 로드하기 위해 Document 클래스의 객체를 생성합니다.
    - 변환하려는 페이지를 가져옵니다.
    - 페이지를 Jpeg으로 변환하기 위해 Process 메서드를 호출합니다.

다음 코드 스니펫은 모든 PDF 페이지를 Jpeg 이미지로 변환하는 방법을 보여줍니다.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF 파일의 모든 페이지를 순회합니다
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // 출력 이미지를 저장할 스트림 객체를 생성합니다
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // 해상도 객체를 생성합니다
            Resolution resolution = new Resolution(300);
            // 특정 해상도로 JpegDevice 객체를 생성합니다
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // 특정 페이지를 변환하고 이미지를 스트림에 저장합니다
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // 스트림을 닫습니다
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


## 특정 PDF 페이지를 JPG 이미지로 변환

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
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

        // 스트림에서 잘린 PDF 문서를 열고 이미지로 변환
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // 해상도 객체 생성
        Resolution resolution = new Resolution(300);
        // 지정된 속성을 가진 Jpeg 장치 생성
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // 특정 페이지를 변환하고 이미지를 스트림에 저장
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```