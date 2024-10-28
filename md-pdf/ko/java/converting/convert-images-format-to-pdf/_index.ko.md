---
title: 다양한 이미지 형식을 PDF로 변환
linktitle: 이미지를 PDF로 변환
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: 이 주제는 Aspose.PDF for Java 라이브러리를 사용하여 다양한 이미지 형식을 PDF로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for Java**는 다양한 형식의 이미지를 PDF 파일로 변환할 수 있게 해줍니다. 우리의 라이브러리는 BMP, CGM, DICOM, EMF, JPG, PNG, SVG 및 TIFF 형식과 같은 가장 인기 있는 이미지 형식을 변환하는 코드 스니펫을 제공합니다.

## BMP를 PDF로 변환

**Aspose.PDF for Java** 라이브러리를 사용하여 BMP 파일을 PDF 문서로 변환합니다.

<abbr title="Bitmap Image File">BMP</abbr> 이미지는 .BMP 확장자를 가진 파일로 비트맵 디지털 이미지를 저장하는 데 사용됩니다. 이러한 이미지는 그래픽 어댑터에 독립적이며 장치 독립 비트맵(DIB) 파일 형식이라고도 합니다. Aspose.PDF for Java API를 사용하여 BMP를 PDF로 변환할 수 있습니다.
 따라서 다음 단계에 따라 BMP 이미지를 변환할 수 있습니다:

1. 새로운 문서 초기화
1. 샘플 BMP 이미지 파일 로드
1. 마지막으로 출력 PDF 파일 저장

따라서 다음 코드 스니펫은 이러한 단계를 따르고 Java를 사용하여 BMP를 PDF로 변환하는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertBMPtoPDF {

    private ConvertBMPtoPDF() {
    }

    private static Path _dataDir = Paths.get("<set path to samples>");

    public static void main(String[] args) throws FileNotFoundException {
        // 문서 객체 초기화
        Document document = new Document();

        Page page = document.getPages().add();        
        Image image = new Image();
        
        // 샘플 BMP 이미지 파일 로드
        image.setFile(Paths.get(_dataDir.toString(), "Sample.bmp").toString());
        page.getParagraphs().add(image);
        
        // 출력 PDF 문서 저장
        document.save(Paths.get(_dataDir.toString(),"BMPtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**BMP를 PDF로 온라인 변환 시도**

Aspose는 여러분이 기능과 품질을 조사해볼 수 있는 온라인 무료 애플리케이션 ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)을 제공합니다.

[![Aspose.PDF BMP를 PDF로 변환 무료 앱 사용](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## CGM을 PDF로 변환

<abbr title="Computer Graphics Metafile">CGM</abbr>은 그래픽 정보의 저장 및 검색을 위한 벡터 기반 2D 이미지 파일 형식을 제공하는 ISO 표준입니다. CGM은 장치 독립적인 형식입니다. CGM은 프로그램 읽기 속도에 가장 적합한 바이너리, 가장 작은 파일 크기를 생성하고 더 빠른 데이터 전송을 허용하는 문자 기반, 사용자가 텍스트 편집기로 파일을 읽고 수정할 수 있도록 하는 명확한 텍스트 인코딩의 세 가지 다른 인코딩 방법을 지원하는 벡터 그래픽 형식입니다.

다음 코드 스니펫은 Aspose.PDF for Java를 사용하여 CGM 파일을 PDF 형식으로 변환하는 방법을 보여줍니다.

1. [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) 클래스를 생성합니다.
1. 소스 파일명과 옵션을 명시하여 [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) 클래스의 인스턴스를 생성합니다.
1. 원하는 파일 이름으로 문서를 저장합니다.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertCGMtoPDF {

    private ConvertCGMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // CGM LoadOptions 생성
        CgmLoadOptions options = new CgmLoadOptions();

        // 문서 객체 초기화
        String cgmFileName = Paths.get(_dataDir.toString(), "corvette.cgm").toString();
        Document document = new Document(cgmFileName, options);

        // 출력 PDF 문서 저장
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


## DICOM을 PDF로 변환

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr>은 의료 이미징에서 정보를 처리, 저장, 출력 및 전송하기 위한 표준입니다. 파일 형식 정의와 네트워크 통신 프로토콜을 포함합니다.

Aspose.PDF for Java는 DICOM 파일을 PDF 형식으로 변환할 수 있습니다. 다음 코드 스니펫을 확인하세요:

1. 스트림에 이미지를 로드합니다
1. [문서 객체](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)를 초기화합니다
1. 샘플 DICOM 이미지 파일을 로드합니다
1. 출력 PDF 문서를 저장합니다

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertDICOMtoPDF {

    private ConvertDICOMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // 스트림에 이미지를 로드합니다
        FileInputStream imageStream = new FileInputStream(
            new java.io.File(Paths.get(_dataDir.toString(),"0002.dcm").toString()));

        // 문서 객체를 초기화합니다
        Document document = new Document();
        document.getPages().add();
        
        // 샘플 DICOM 이미지 파일을 로드합니다
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setImageStream(imageStream);

        document.getPages().get_Item(1).getParagraphs().add(image);

        // 출력 PDF 문서를 저장합니다
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**DICOM을 PDF로 온라인 변환 시도**

Aspose는 ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion DICOM to PDF using Free App](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMF를 PDF로 변환

향상된 메타파일 형식 (<abbr title="Enhanced metafile format">EMF</abbr>)은 그래픽 이미지를 장치 독립적으로 저장합니다. EMF의 메타파일은 가변 길이 기록을 시간 순서대로 포함하며, 이를 해석하여 저장된 이미지를 출력 장치에서 렌더링할 수 있습니다.

EMF를 PDF로 변환하는 여러 가지 방법이 있습니다.

## Image 클래스 사용

PDF 문서는 페이지로 구성되며, 각 페이지는 하나 이상의 단락 개체를 포함합니다. 단락은 텍스트, 이미지, 표, 플로팅 박스, 그래프, 제목, 양식 필드 또는 첨부 파일일 수 있습니다.

이미지 파일을 PDF 형식으로 변환하려면 이를 단락에 포함하십시오.

로컬 하드 드라이브의 물리적 위치에 있거나 웹 URL에서 찾을 수 있거나 Stream 인스턴스에 있는 이미지를 변환할 수 있습니다.

이미지를 추가하려면:

1. com.aspose.pdf.Image 클래스의 객체를 생성합니다.
1. 페이지 인스턴스의 [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) 컬렉션에 이미지를 추가합니다.
1. 이미지의 경로 또는 소스를 지정합니다.
    - 이미지가 하드 드라이브의 위치에 있을 경우, [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image) 메서드를 사용하여 경로 위치를 지정합니다.
    - 이미지가 FileInputStream에 있을 경우, 이미지를 담고 있는 객체를 [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image) 메서드에 전달합니다.

다음 코드 스니펫은 이미지 객체를 로드하고, 페이지 여백을 설정하고, 페이지에 이미지를 배치하고, 결과를 PDF로 저장하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;

/**
 * EMF를 PDF로 변환
 */

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;

public final class ConvertEMFtoPDF {

    private ConvertEMFtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        convertEMFtoPDF_01();
        convertEMFtoPDF_02();
    }

    

    public static void convertEMFtoPDF_01() throws FileNotFoundException {                
        // 문서 객체 인스턴스화
        Document doc = new Document();
        // 문서의 페이지 컬렉션에 페이지 추가
        Page page = doc.getPages().add();
        // 소스 이미지 파일을 Stream 객체로 로드
        java.io.FileInputStream fs = new java.io.FileInputStream(
            Paths.get(_dataDir.toString(),"source.emf").toString());

        // 이미지가 맞도록 여백 설정 등
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);

        page.setCropBox(new Rectangle(0, 0, 400, 400));
        // 이미지 객체 생성
        Image image1 = new Image();
        // 섹션의 단락 컬렉션에 이미지 추가
        page.getParagraphs().add(image1);
        // 이미지 파일 스트림 설정
        image1.setImageStream(fs);
        // 결과 PDF 파일 저장
        doc.save("EMFtoPDF_01.pdf");
    }   
    public static void convertEMFtoPDF_02() throws IOException {
        // 아래 코드 참조
    } 
}
```


### BufferedImage에서 이미지 추가

Aspose.PDF for Java는 Stream 인스턴스에서 이미지를 로드하는 기능도 제공하며, 이미지를 BufferedImage 객체에 로드하여 Pdf 파일의 단락 컬렉션에 배치할 수 있습니다.

```java
public static void convertEMFtoPDF_02() throws IOException {    
    Document doc = new Document();
    // Pdf 파일의 페이지 컬렉션에 페이지 추가
    Page page = doc.getPages().add();
    // 이미지 인스턴스 생성
    Image image1 = new Image();
    // BufferedImage 인스턴스 생성
    java.awt.image.BufferedImage bufferedImage = ImageIO.read(new File("source.emf"));
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    // Buffered Image를 OutputStream 인스턴스에 쓰기
    ImageIO.write(bufferedImage, "emf", baos);
    baos.flush();
    ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
    // 첫 번째 페이지의 단락 컬렉션에 이미지 추가
    page.getParagraphs().add(image1);
    // Buffered image를 보유한 OutputStream으로 이미지 스트림 설정
    image1.setImageStream(bais);
    // 결과 PDF 파일 저장
    doc.save("BufferedImage.pdf");
}
```


## PDF 연산자를 사용하여 이미지 추가

모든 PDF 페이지 객체는 [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) 및 [getContents()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getContents--) 메서드를 포함합니다. 리소스는 예를 들어 이미지와 폼일 수 있으며, 콘텐츠는 일련의 PDF 연산자로 표현됩니다. 각 연산자는 고유한 이름과 인수를 가지고 있습니다.

이 예제는 연산자를 사용하여 PDF 파일에 이미지를 추가합니다.

기존 PDF 파일에 이미지를 추가하려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 생성하고 입력 PDF 문서를 엽니다.
1. 이미지를 추가하려는 페이지를 가져옵니다.
1. 페이지의 [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) 컬렉션에 이미지를 추가합니다.
1. 연산자를 사용하여 페이지에 이미지를 배치합니다:
   1. GSave 연산자를 사용하여 현재 그래픽 상태를 저장합니다.
   1. ConcatenateMatrix 연산자를 사용하여 이미지가 배치될 위치를 지정합니다.

1. Do 연산자를 사용하여 페이지에 이미지를 그립니다.
   1. 마지막으로, GRestore 연산자를 사용하여 업데이트된 그래픽 상태를 저장합니다.
1. 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에 이미지를 추가하는 방법을 보여줍니다.

```java
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.Pdf-for-Java를 참조하세요.
// 문서 열기
Document pdfDocument1 = new Document("input.pdf");

// 좌표 설정
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// 이미지를 추가할 페이지 가져오기
Page page = pdfDocument1.getPages().get_Item(1);

// 스트림에 이미지 로드
java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));

// 페이지 리소스의 이미지 컬렉션에 이미지 추가
page.getResources().getImages().add(imageStream);

// GSave 연산자 사용: 이 연산자는 현재 그래픽 상태를 저장합니다.
page.getContents().add(new Operator.GSave());

// Rectangle 및 Matrix 객체 생성
Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

// ConcatenateMatrix(행렬 연결) 연산자 사용: 이미지가 배치되는 방법을 정의합니다.
page.getContents().add(new Operator.ConcatenateMatrix(matrix));
XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

// Do 연산자 사용: 이 연산자는 이미지를 그립니다.
page.getContents().add(new Operator.Do(ximage.getName()));

// GRestore 연산자 사용: 이 연산자는 그래픽 상태를 복원합니다.
page.getContents().add(new Operator.GRestore());

// 새로운 PDF 저장
pdfDocument1.save("Updated_document.pdf");

// 이미지 스트림 닫기
imageStream.close();
```


{{% alert color="success" %}}
**EMF를 PDF로 온라인 변환 시도**

Aspose는 ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)라는 무료 온라인 애플리케이션을 제공하며, 여기서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 EMF를 PDF로 무료 앱 사용](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## JPG를 PDF로 변환

JPG를 PDF로 변환하는 방법에 대해 고민할 필요가 없습니다. Apose.PDF for Java 라이브러리가 최상의 선택을 제공합니다.

Aspose.PDF for Java를 사용하여 다음 단계에 따라 JPG 이미지를 PDF로 매우 쉽게 변환할 수 있습니다:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 객체 초기화
1. JPG 이미지 로드 및 단락에 추가
1. 출력 PDF 저장

아래 코드 스니펫은 Java를 사용하여 JPG 이미지를 PDF로 변환하는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertJPEGtoPDF {

    private static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // 문서 객체 초기화
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // 샘플 JPEG 이미지 파일 로드
        image.setFile(Paths.get(_dataDir.toString(), "Sample.jpg").toString());
        page.getParagraphs().add(image);

        // 출력 PDF 문서 저장
        document.save(Paths.get(_dataDir.toString(),"JPEGtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**JPG를 PDF로 온라인 변환 시도하기**

Aspose는 여러분이 기능과 품질을 조사해볼 수 있는 온라인 무료 애플리케이션 ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)를 제공합니다.

[![Aspose.PDF Convertion JPG to PDF using Free App](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## PNG를 PDF로 변환하기

**Aspose.PDF for Java**는 PNG 이미지를 PDF 형식으로 변환하는 기능을 지원합니다. 다음 코드 스니펫을 확인하여 작업을 구현하세요.

<abbr title="Portable Network Graphics">PNG</abbr>는 무손실 압축을 사용하는 래스터 이미지 파일 형식을 나타내며, 이는 사용자들 사이에서 인기가 있습니다.

PNG를 PDF 이미지로 변환할 수 있는 단계는 다음과 같습니다:

1. 입력 PNG 이미지 로드
1. 높이 및 너비 값 읽기
1. 새 문서 생성 및 페이지 추가
1. 페이지 크기 설정
1. 출력 파일 저장

또한, 아래 코드 스니펫은 Java 애플리케이션에서 PNG를 PDF로 변환하는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

/**
 * PNG를 PDF로 변환
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPNGtoPDF {

    private ConvertPNGtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // 문서 객체 초기화
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // 샘플 BMP 이미지 파일 로드
        image.setFile(Paths.get(_dataDir.toString(), "Sample.png").toString());

        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getParagraphs().add(image);

        // 출력 PDF 문서 저장
        document.save(Paths.get(_dataDir.toString(), "PNGtoPDF.pdf").toString());
    }
}

```


{{% alert color="success" %}}
**PNG를 PDF로 온라인 변환 시도**

Aspose는 ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)라는 온라인 무료 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 PNG to PDF 무료 앱 사용](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## SVG를 PDF로 변환

Scalable Vector Graphics (SVG)는 2차원 벡터 그래픽을 위한 XML 기반 파일 형식의 사양 가족으로, 정적 및 동적(대화형 또는 애니메이션) 모두를 포함합니다. SVG 사양은 1999년부터 월드 와이드 웹 컨소시엄(W3C)에 의해 개발 중인 오픈 표준입니다.

SVG 이미지와 그 행동은 XML 텍스트 파일로 정의됩니다.
 이것은 검색, 인덱싱, 스크립팅 및 필요한 경우 압축할 수 있음을 의미합니다. XML 파일로서, SVG 이미지는 모든 텍스트 편집기로 생성 및 편집할 수 있지만, Inkscape와 같은 드로잉 프로그램을 사용하여 생성하는 것이 종종 더 편리합니다.

## SVG 파일을 PDF 형식으로 변환하는 방법

SVG 파일을 PDF로 변환하려면 [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) 객체를 초기화하는 데 사용되는 [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions)이라는 클래스를 사용하십시오. 이후 이 객체는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 객체 초기화 시 인수로 전달되어 PDF 렌더링 엔진이 소스 문서의 입력 형식을 결정하는 데 도움을 줍니다.

다음 코드 스니펫은 SVG 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```java
// 문서 객체 초기화

String pdfDocumentFileName = Paths.get(_dataDir.toString(), "svg_test.pdf").toString();
String svgDocumentFileName = Paths.get(_dataDir.toString(), "car.svg").toString();

SvgLoadOptions option = new SvgLoadOptions();
Document pdfDocument = new Document(svgDocumentFileName, option);
pdfDocument.save(pdfDocumentFileName);
```

{{% alert color="success" %}}
**SVG 형식을 PDF로 온라인 변환 시도**

Aspose.PDF for Java는 ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)라는 온라인 무료 애플리케이션을 제공하여 기능과 품질을 조사할 수 있습니다.

[![Aspose.PDF로 SVG를 PDF로 변환하는 무료 앱](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## TIFF를 PDF로 변환

**Aspose.PDF for Java** 파일 형식은 단일 프레임 또는 다중 프레임 <abbr title="Tag Image File Format">TIFF</abbr> 이미지를 지원합니다. 이는 Java 애플리케이션에서 TIFF 이미지를 PDF로 변환할 수 있음을 의미합니다.

TIFF 또는 TIF, 태그 이미지 파일 형식은 이 파일 형식 표준을 준수하는 다양한 장치에서 사용하도록 설계된 래스터 이미지를 나타냅니다.
 TIFF 이미지는 서로 다른 이미지로 구성된 여러 프레임을 포함할 수 있습니다. Aspose.PDF 파일 형식도 지원되며, 단일 프레임 또는 다중 프레임 TIFF 이미지가 될 수 있습니다. 따라서 Java 애플리케이션에서 TIFF 이미지를 PDF로 변환할 수 있습니다. 그래서 우리는 다중 페이지 TIFF 이미지를 다중 페이지 PDF 문서로 변환하는 예제를 아래 단계와 함께 고려할 것입니다:

1. Document 클래스의 인스턴스 생성
1. 입력 TIFF 이미지 로드
1. 마지막으로, 이미지를 PDF 페이지로 저장

또한, 다음 코드 스니펫은 다중 페이지 또는 다중 프레임 TIFF 이미지를 PDF로 변환하는 방법을 보여줍니다:

```java
import com.aspose.pdf.Document;
import com.aspose.pdf.Image;
import com.aspose.pdf.Page;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * TIFF를 PDF로 변환합니다.
 */
public final class ConvertTIFFtoPDF {

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertTIFFtoPDF() {
    }

    public static void run() throws IOException {
        // 문서 객체 초기화
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        image.setFile(Paths.get(DATA_DIR.toString(), "Sample.tiff").toString());
        page.getParagraphs().add(image);

        // 출력 PDF 문서 저장
        document.save(Paths.get(DATA_DIR.toString(), "TIFFtoPDF.pdf").toString());
        document.close();
    }    
}
```