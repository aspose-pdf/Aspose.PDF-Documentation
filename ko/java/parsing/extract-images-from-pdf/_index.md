---
title: PDF에서 이미지 추출 
linktitle: 이미지 추출
type: docs
weight: 20
url: /ko/java/extract-images-from-the-pdf-file/
description: Aspose.PDF for Java를 사용하여 PDF에서 이미지의 일부를 추출하는 방법
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서의 각 페이지에는 리소스(이미지, 양식 및 글꼴)가 포함되어 있습니다. 우리는 [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) 메서드를 호출하여 이러한 리소스에 접근할 수 있습니다. [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) 클래스에는 [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection)이 포함되어 있으며, [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) 메서드를 호출하여 이미지 목록을 얻을 수 있습니다.

따라서 페이지에서 이미지를 추출하려면 페이지에 대한 참조, 페이지 리소스에 대한 참조, 마지막으로 이미지 컬렉션에 대한 참조를 얻어야 합니다. 특정 이미지는 예를 들어 인덱스를 통해 추출할 수 있습니다.

이미지의 인덱스는 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) 객체를 반환합니다.
이 객체는 추출된 이미지를 저장하는 데 사용할 수 있는 [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) 메서드를 제공합니다. 다음 코드 스니펫은 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다.

```java
public static void Extract_Images(){
    // 문서 디렉토리의 경로
    String _dataDir = "/home/admin1/pdf-examples/Samples/";
    String filePath = _dataDir + "ExtractImages.pdf";

    // PDF 문서 로드
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);
    com.aspose.pdf.XImageCollection xImageCollection = page.getResources().getImages();
    // 특정 이미지 추출
    com.aspose.pdf.XImage xImage = xImageCollection.get_Item(1);

    try {
        java.io.FileOutputStream outputImage = new java.io.FileOutputStream(_dataDir + "output.jpg");
        // 출력 이미지 저장
        xImage.save(outputImage);
        outputImage.close();
    } catch (java.io.FileNotFoundException e) {
        // TODO: 예외 처리
        e.printStackTrace();
    } catch (java.io.IOException e) {
        // TODO: 예외 처리
        e.printStackTrace();
    }
}
```