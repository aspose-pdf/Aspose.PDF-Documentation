---
title: PDF를 PNG로 변환
linktitle: PDF를 PNG로 변환
type: docs
weight: 20
url: /androidjava/convert-pdf-to-png/
lastmod: "2021-06-05"
description: 이 페이지는 Aspose.PDF for Android via Java를 사용하여 PDF 페이지를 PNG 이미지로 변환하고, 모든 페이지 및 개별 페이지를 PNG 이미지로 변환하는 방법을 설명합니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 페이지를 <abbr title="Portable Network Graphics">PNG</abbr> 이미지로 변환하는 데 **Aspose.PDF for Android via Java** 라이브러리를 사용하여 접근 가능하고 편리한 방법으로 수행하십시오.

PngDevice 클래스는 PDF 페이지를 PNG 이미지로 변환할 수 있게 해줍니다. 이 클래스는 PDF 파일의 특정 페이지를 PNG 이미지 형식으로 변환할 수 있는 Process라는 메서드를 제공합니다.

## PDF 페이지를 PNG 이미지로 변환

PDF 파일의 모든 페이지를 PNG 파일로 변환하려면 개별 페이지를 반복하여 각각을 PNG 형식으로 변환합니다. 다음 코드 스니펫은 PDF 파일의 모든 페이지를 순회하고 각각을 PNG 이미지로 변환하는 방법을 보여줍니다.

{{% alert color="primary" %}}

온라인으로 시도하세요. Aspose.PDF 변환의 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다 [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## 단일 PDF 페이지를 PNG 이미지로 변환

페이지 인덱스를 Process(..) 메서드의 인수로 전달합니다. 다음 코드 스니펫은 PDF의 첫 번째 페이지를 PNG 형식으로 변환하는 단계를 보여줍니다.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // 출력 이미지를 저장할 스트림 객체 생성
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Resolution 객체 생성
            Resolution resolution = new Resolution(300);

            // 특정 해상도의 PngDevice 객체 생성
            PngDevice PngDevice = new PngDevice(resolution);

            // 특정 페이지를 변환하고 이미지를 스트림에 저장
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // 스트림 닫기
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## 모든 PDF 페이지를 PNG 이미지로 변환

Aspose.PDF for Android via Java는 PDF 파일의 모든 페이지를 이미지로 변환하는 방법을 보여줍니다:

1. 파일의 모든 페이지를 반복합니다.
1. 각 페이지를 개별적으로 변환합니다:
    1. PDF 문서를 로드하기 위해 Document 클래스의 객체를 생성합니다.
    1. 변환하고자 하는 페이지를 가져옵니다.
    1. 페이지를 Png로 변환하기 위해 Process 메소드를 호출합니다.

다음 코드 스니펫은 모든 PDF 페이지를 PNG 이미지로 변환하는 방법을 보여줍니다.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF 파일의 모든 페이지를 반복합니다
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // 출력 이미지를 저장할 스트림 객체를 생성합니다
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Resolution 객체를 생성합니다
            Resolution resolution = new Resolution(300);
            // 특정 해상도로 JpegDevice 객체를 생성합니다
            PngDevice JpegDevice = new PngDevice(resolution);

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


## 특정 PDF 페이지를 PNG 이미지로 변환하기

Aspose.PDF for Android via Java는 특정 페이지를 PNG 형식으로 변환하는 방법을 보여줍니다:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
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
        // 지정된 속성으로 Jpeg 장치 생성
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // 특정 페이지를 변환하고 이미지를 스트림에 저장
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```