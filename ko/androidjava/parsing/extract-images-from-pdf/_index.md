---
title: PDF에서 이미지 추출
linktitle: 이미지 추출
type: docs
weight: 20
url: /ko/androidjava/extract-images-from-the-pdf-file/
description: Aspose.PDF for Android via Java를 사용하여 PDF에서 이미지의 일부를 추출하는 방법
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서의 각 페이지는 리소스(이미지, 양식 및 글꼴)를 포함하고 있습니다. [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) 메서드를 호출하여 이러한 리소스에 접근할 수 있습니다. [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) 클래스는 [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection)을 포함하고 있으며, [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) 메서드를 호출하여 이미지 목록을 얻을 수 있습니다.

따라서 페이지에서 이미지를 추출하려면 페이지, 다음으로 페이지 리소스, 마지막으로 이미지 컬렉션에 대한 참조를 얻어야 합니다.

특정 이미지는 예를 들어 인덱스를 통해 추출할 수 있습니다.

The image's index returns an [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) object.
This object provides a [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

 ```java
 public void extractImage () {
        // 문서 열기
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.Page page=document.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
        // 특정 이미지 추출
        com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
        File file=new File(fileStorage, "extracted-image.jpeg");
        try {
            java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
            // 출력 이미지 저장
            xImage.save(outputImage, ImageType.getJpeg());
            outputImage.close();
        } catch (java.io.IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.
          }
```