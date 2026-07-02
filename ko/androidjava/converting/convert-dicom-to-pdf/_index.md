---
title: DICOM을 PDF로 변환
linktitle: DICOM을 PDF로 변환
type: docs
weight: 250
url: /ko/androidjava/convert-dicom-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java를 사용하여 DICOM 형식으로 저장된 의료 이미지를 PDF 파일로 변환합니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> 의료 영상에서 정보를 처리, 저장, 인쇄 및 전송하기 위한 표준입니다. 파일 형식 정의와 네트워크 통신 프로토콜을 포함합니다.

Aspsoe.PDF for Java를 사용하면 DICOM 파일을 PDF 형식으로 변환할 수 있으며, 다음 코드 조각을 확인하십시오:

1. 스트림에 이미지 로드
1. 초기화 [`Document object`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. 샘플 DICOM 이미지 파일 로드
1. 출력 PDF 문서 저장

```java
//    Convert DICOM to PDF
    public void convertDICOMtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/bmode.dcm");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

