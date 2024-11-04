---
title: 기존 PDF 파일에 이미지 추가
linktitle: 이미지 추가
type: docs
weight: 10
url: /java/add-image-to-existing-pdf-file/
description: 이 섹션에서는 Java 라이브러리를 사용하여 기존 PDF 파일에 이미지를 추가하는 방법을 설명합니다.
lastmod: "2021-06-05"
---

모든 PDF 페이지는 리소스와 콘텐츠 속성을 포함합니다. 리소스는 예를 들어 이미지와 양식일 수 있으며, 콘텐츠는 PDF 연산자로 표현됩니다. 각 연산자는 이름과 인수를 가집니다. 이 예제에서는 연산자를 사용하여 PDF 파일에 이미지를 추가합니다.

기존 PDF 파일에 이미지를 추가하려면:

- [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 생성하고 입력 PDF 문서를 엽니다.
- 이미지를 추가하고자 하는 페이지를 가져옵니다.
- 페이지의 [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) 컬렉션에 이미지를 추가합니다.
- 연산자를 사용하여 페이지에 이미지를 배치합니다:
- 현재 그래픽 상태를 저장하려면 GSave 연산자를 사용합니다.

- [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/concatenatematrix) 연산자를 사용하여 이미지가 배치될 위치를 지정합니다.
- 페이지에 이미지를 그리기 위해 [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/class-use/Do) 연산자를 사용합니다.
- 마지막으로, 업데이트된 그래픽 상태를 저장하기 위해 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/grestore) 연산자를 사용합니다.
- 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에 이미지를 추가하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfFileMend;
import com.aspose.pdf.operators.*;

public class ExampleAddImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddImageToExistingPDF() throws IOException {
        // 문서 열기
        Document pdfDocument1 = new Document(_dataDir + "sample.pdf");

        // 좌표 설정
        int lowerLeftX = 50;
        int lowerLeftY = 750;
        int upperRightX = 100;
        int upperRightY = 800;

        // 이미지를 추가할 페이지 가져오기
        Page page = pdfDocument1.getPages().get_Item(1);

        // 스트림에 이미지 로드
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(_dataDir + "logo.png"));

        // 페이지 리소스의 이미지 컬렉션에 이미지 추가
        page.getResources().getImages().add(imageStream);

        // GSave 연산자 사용: 이 연산자는 현재 그래픽 상태를 저장합니다
        page.getContents().add(new GSave());

        // Rectangle 및 Matrix 객체 생성
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // ConcatenateMatrix (행렬 연결) 연산자 사용: 이미지가 어떻게 배치되어야 하는지를 정의합니다
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

        // Do 연산자 사용: 이 연산자는 이미지를 그립니다
        page.getContents().add(new Do(ximage.getName()));

        // GRestore 연산자 사용: 이 연산자는 그래픽 상태를 복원합니다
        page.getContents().add(new GRestore());

        // 새 PDF 저장
        pdfDocument1.save(_dataDir + "updated_document.pdf");

        // 이미지 스트림 닫기
        imageStream.close();
    }
```


## BufferedImage에서 PDF로 이미지 추가

Aspose.PDF for Java 9.5.0 릴리스부터 BufferedImage 인스턴스에서 PDF 문서로 이미지를 추가하는 기능이 도입되었습니다. 이 요구 사항을 지원하기 위해 메소드가 구현되었습니다: [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection).add(BufferedImage image);

```java
    public static void AddingImageFromBufferedImageIntoPDF() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();
        page.getResources().getImages().add(originalImage);
    }
```
이미지를 추가하기 위해 FileInputStream 객체뿐만 아니라 모든 InputStream을 사용할 수 있습니다. 따라서 java.io.ByteArrayInputStream 객체를 사용할 때 시스템에 파일을 저장할 필요가 없습니다:

```java
    public static void AddingImageFromBufferedImageIntoPDF2() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        ByteArrayOutputStream baos = new ByteArrayOutputStream();

        Document pdfDocument = new Document();
        ImageIO.write(originalImage, "jpg", baos);
        baos.flush();
        Page page = pdfDocument.getPages().get_Item(1);
        page.getResources().getImages().add(new ByteArrayInputStream(baos.toByteArray()));
    }
```


## 기존 PDF 파일에 이미지 추가하기 (Facades)

PDF 파일에 이미지를 추가하는 또 다른 쉬운 방법이 있습니다. [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend) 클래스의 AddImage 메서드를 사용할 수 있습니다. AddImage 메서드는 추가할 이미지, 이미지가 추가될 페이지 번호 및 좌표 정보를 필요로 합니다. 그런 다음 Close 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 기존 PDF 파일에 이미지를 추가하는 방법을 보여줍니다.

```java
    public static void AddImageInAnExistingPDFFile_Facades() {
        // 문서 열기
        PdfFileMend mender = new PdfFileMend();

        // 텍스트를 추가하기 위해 PdfFileMend 객체 생성
        mender.bindPdf(_dataDir + "AddImage.pdf");

        // PDF 파일에 이미지 추가
        mender.addImage(_dataDir + "aspose-logo.jpg", 1, 100, 600, 200, 700);

        // 변경 사항 저장
        mender.save(_dataDir + "AddImage_out.pdf");

        // PdfFileMend 객체 닫기
        mender.close();
    }
```


## PDF 문서에서 단일 이미지를 여러 번 참조 추가

때때로 우리는 동일한 이미지를 PDF 문서에서 여러 번 사용해야 할 필요가 있습니다. 새로운 인스턴스를 추가하면 결과 PDF 문서의 크기가 증가합니다. 우리는 이미지 컬렉션에 Ximage 객체를 추가할 수 있는 새로운 메소드 XImageCollection.add(XImage)를 추가했습니다. 이 메소드는 원본 이미지와 동일한 PDF 객체에 대한 참조를 추가하여 PDF 문서 크기를 최적화할 수 있습니다.

```java
    public static void AddReferenceOfaSingleImageMultipleTimes() throws FileNotFoundException {
        Rectangle imageRectangle = new Rectangle(0, 0, 30, 15);
        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        document.getPages().add();
        java.io.FileInputStream imageStream = new java.io.FileInputStream(
                new java.io.File(_dataDir + "aspose-logo.png"));

        XImage image = null;

        for (Page page : document.getPages()) {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.getRect());
            XForm form = annotation.getAppearance().get_Item("N");
            form.setBBox(page.getRect());
            String name;
            if (image == null) {
                name = form.getResources().getImages().add(imageStream);
                image = form.getResources().getImages().get_Item(name);
            } else {
                name = form.getResources().getImages().add(image);
            }
            form.getContents().add(new GSave());
            form.getContents().add(new ConcatenateMatrix(
                    new Matrix(imageRectangle.getWidth(), 0, 0, imageRectangle.getHeight(), 0, 0)));
            form.getContents().add(new Do(name));
            form.getContents().add(new GRestore());
            page.getAnnotations().add(annotation, false);
            imageRectangle = new Rectangle(0, 0, imageRectangle.getWidth() * 1.01, imageRectangle.getHeight() * 1.01);
        }
        document.save(_dataDir + "output.pdf");
    }
```


## PDF 내부 이미지가 컬러인지 흑백인지 식별하기

다양한 유형의 압축이 이미지를 압축하여 크기를 줄일 수 있습니다. 이미지에 적용되는 압축 유형은 원본 이미지의 ColorSpace에 따라 달라집니다. 즉, 이미지가 컬러(RGB)인 경우 JPEG2000 압축을 적용하고, 흑백인 경우 JBIG2/JBIG2000 압축을 적용해야 합니다. 따라서 각 이미지 유형을 식별하고 적절한 유형의 압축을 사용하면 최적의 출력물을 생성할 수 있습니다.

PDF 파일에는 텍스트, 이미지, 그래프, 첨부 파일, 주석 등의 요소가 포함될 수 있으며, 원본 PDF 파일에 이미지가 포함된 경우 이미지의 색상 공간을 확인하고 적절한 압축을 적용하여 PDF 파일 크기를 줄일 수 있습니다. 다음 코드 스니펫은 PDF 내부의 이미지가 컬러인지 흑백인지 식별하는 단계를 보여줍니다.

```java
    public static void CheckColors() {

        Document document = new Document(_dataDir + "test4.pdf");
        try {
            // PDF 파일의 모든 페이지를 반복 처리
            for (Page page : (Iterable<Page>) document.getPages()) {
                // 이미지 배치 흡수기 인스턴스 생성
                ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
                page.accept(abs);
                for (ImagePlacement ia : (Iterable<ImagePlacement>) abs.getImagePlacements()) {
                    /* ColorType */
                    int colorType = ia.getImage().getColorType();
                    switch (colorType) {
                    case ColorType.Grayscale:
                        System.out.println("Grayscale Image");
                        break;
                    case ColorType.Rgb:
                        System.out.println("Colored Image");
                        break;
                    }
                }
            }
        } catch (Exception ex) {
            System.out.println("파일 읽기 오류 = " + document.getFileName());
        }
    }
}
```