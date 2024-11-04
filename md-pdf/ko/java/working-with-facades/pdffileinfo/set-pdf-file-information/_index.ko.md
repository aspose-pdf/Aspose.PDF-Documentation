---
title: PDF 파일 정보 설정 - 파사드
type: docs
weight: 20
url: /java/set-pdf-information/
description: 이 섹션에서는 PdfFileInfo 클래스를 사용하여 Aspose.PDF Facades로 PDF 파일 정보를 설정하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) 클래스는 PDF 문서의 파일 특정 정보를 설정할 수 있게 해줍니다. [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) 클래스의 객체를 생성한 다음, 저자, 제목, 키워드, 작성자 등과 같은 다양한 파일 특정 속성을 설정해야 합니다. 마지막으로, [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) 객체의 [saveNewInfo(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#saveNewInfo-java.io.OutputStream-) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일 정보를 설정하는 방법을 보여줍니다.

```java
 public static void SetPdfInfo()
    {
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // PDF 정보 설정
        fileInfo.setAuthor("Aspose");
        fileInfo.setTitle ("Hello World!");
        fileInfo.setKeywords("Peace and Development");
        fileInfo.setCreator ("Aspose");
        
        // 업데이트된 파일 저장
        fileInfo.saveNewInfo(_dataDir + "SetfileInfo_out.pdf");
    }
```


## 메타 정보 설정

[setMetaInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#setMetaInfo-java.lang.String-java.lang.String-) 메서드를 사용하면 정보를 추가할 수 있습니다. 우리의 예제에서는 필드를 추가했습니다. 다음 코드 스니펫을 확인하세요:

```java
   public static void SetMetaInfo()
    {
        // PdffileInfo 객체의 인스턴스 생성
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "sample.pdf");
       
        // 새로운 고객 속성을 메타 정보로 설정
        fInfo.setMetaInfo("Reviewer", "Aspose.PDF user");

        // 업데이트된 파일 저장
        fInfo.saveNewInfo(_dataDir + "SetMetaInfo_out.pdf");

    }
```