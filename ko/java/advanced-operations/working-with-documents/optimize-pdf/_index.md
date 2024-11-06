---
title: Java에서 PDF 크기를 최적화, 압축 또는 줄이기
linktitle: PDF 문서 최적화
type: docs
weight: 40
url: ko/java/optimize-pdf/
description: PDF 파일 최적화, 모든 이미지 축소, PDF 크기 줄이기, 폰트 임베드 해제, Java로 사용되지 않는 객체 제거.
lastmod: "2021-06-05"
---

PDF 문서에는 때때로 추가 데이터가 포함될 수 있습니다. PDF 파일의 크기를 줄이면 네트워크 전송 및 저장소를 최적화하는 데 도움이 됩니다. 이는 특히 웹 페이지에 게시하거나 소셜 네트워크에서 공유하거나 이메일로 보내거나 저장소에 보관할 때 유용합니다. PDF를 최적화하기 위해 몇 가지 기술을 사용할 수 있습니다:

- 온라인 브라우징을 위한 페이지 콘텐츠 최적화
- 모든 이미지 축소 또는 압축
- 페이지 콘텐츠 재사용 활성화
- 중복 스트림 병합
- 폰트 임베드 해제
- 사용되지 않는 객체 제거
- 평탄화된 폼 필드 제거
- 주석 제거 또는 평탄화

## 웹용 PDF 문서 최적화

최적화 또는 선형화는 웹 브라우저를 사용하여 온라인 브라우징에 적합한 PDF 파일을 만드는 프로세스를 말합니다.
 Aspose.PDF는 이 프로세스를 지원합니다.

웹 표시를 위해 PDF를 최적화하려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체에서 입력 문서를 엽니다.
1. [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--) 메서드를 사용합니다.
1. save(..) 메서드를 사용하여 최적화된 문서를 저장합니다.

다음 코드 스니펫은 웹을 위해 PDF 문서를 최적화하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.time.Clock;
import java.time.Duration;

import com.aspose.pdf.*;
import com.aspose.pdf.optimization.ImageCompressionVersion;
import com.aspose.pdf.optimization.ImageEncoding;

public class ExampleOptimize {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void OptimizePDFDocumentForTheWeb() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // 웹 최적화
        pdfDocument.optimize();

        // 출력 문서 저장
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## PDF 파일 크기 줄이기

이 주제는 PDF 파일 크기를 최적화/줄이는 단계를 설명합니다. Aspose.PDF API는 불필요한 객체를 제거하고 이미지를 포함한 PDF 파일을 압축하여 출력 PDF를 최적화할 수 있는 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) 클래스를 제공합니다. 이 두 가지 옵션은 다음 섹션에서 설명됩니다.

### 불필요한 객체 제거
중복되고 사용되지 않는 객체를 제거하여 PDF 문서의 크기를 최적화할 수 있습니다. 다음 코드 스니펫은 방법을 보여줍니다.

```java
public static void ReduceSizePDF() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // PDF 문서 최적화. 그러나 이 방법이 문서 축소를 보장할 수는 없습니다.
        pdfDocument.optimizeResources();

        // 출력 문서 저장
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## 모든 이미지 축소 또는 압축하기

If the source PDF file contains images, consider compressing the images and setting their quality. In order to enable image compression, pass true as an argument to the setCompressImages(..) method. All the images in a document will be re-compressed. The compression is defined by the setImageQuality(..) method, which is the value of the quality in percent. 100% is unchanged quality and image size. To decrease image size, pass an argument of less than 100 to the setImageQuality(..) method.

만약 소스 PDF 파일에 이미지가 포함되어 있다면, 이미지를 압축하고 품질을 설정하는 것을 고려하십시오. 이미지 압축을 활성화하기 위해서는 setCompressImages(..) 메서드에 true를 인수로 전달하십시오. 문서의 모든 이미지는 재압축됩니다. 압축은 setImageQuality(..) 메서드에 의해 정의되며, 이는 품질의 백분율 값입니다. 100%는 변경되지 않은 품질과 이미지 크기입니다. 이미지 크기를 줄이기 위해서는 setImageQuality(..) 메서드에 100보다 작은 값을 인수로 전달하십시오.

```java
public static void ShrinkingCompressing() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "Shrinkimage.pdf");

        // Initialize OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Set CompressImages option
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Set ImageQuality option
        optimizationOptions.getImageCompressionOptions().setImageQuality(50);

        // Optimize PDF document using OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "Shrinkimage_out.pdf";
        // Save updated document
        pdfDocument.save(_dataDir);
    }
```

이미지를 낮은 해상도로 조정하는 또 다른 방법이 있습니다. 이 경우, ResizeImages를 true로 설정하고 MaxResolution을 적절한 값으로 설정해야 합니다.

```java
public static void ShrinkingCompressing2() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // OptimizationOptions 초기화
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // CompressImages 옵션 설정
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);
        // ImageQuality 옵션 설정
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // ResizeImage 옵션 설정
        optimizationOptions.getImageCompressionOptions().setResizeImages(true);

        // MaxResolution 옵션 설정
        optimizationOptions.getImageCompressionOptions().setMaxResolution(300);

        // OptimizationOptions를 사용하여 PDF 문서 최적화
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "ResizeImages_out.pdf";
        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir);
    }
```

또 다른 중요한 문제는 실행 시간입니다. 그러나 다시 말하지만, 이 설정도 관리할 수 있습니다. 현재 우리는 표준과 빠른 두 가지 알고리즘을 사용할 수 있습니다. 실행 시간을 제어하려면 Version 속성을 설정해야 합니다. 다음 코드 스니펫은 빠른 알고리즘을 보여줍니다:

```java
public static void ShrinkingCompressing3() {

        Clock clock = Clock.systemUTC();

        Duration tickDuration = Duration.ofNanos(250000);
        Clock clock1 = Clock.tick(clock, tickDuration);
        System.out.println("시작 : " + clock.instant());

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // OptimizationOptions 초기화
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // CompressImages 옵션 설정
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // ImageQuality 옵션 설정
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // 이미지 압축 버전을 빠르게 설정
        optimizationOptions.getImageCompressionOptions().setVersion(ImageCompressionVersion.Fast);

        // OptimizationOptions를 사용하여 PDF 문서 최적화
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "ResizeImages_out.pdf";

        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir);
        System.out.println("종료 : " + clock1.instant());
    }
```

## 사용되지 않는 객체 제거

PDF 문서는 때때로 문서 내 다른 객체에서 참조되지 않는 PDF 객체를 포함할 수 있습니다. 예를 들어, 페이지가 문서 페이지 트리에서 제거되었지만 페이지 객체 자체는 제거되지 않은 경우에 발생할 수 있습니다. 이러한 객체를 제거하는 것은 문서를 무효화하지 않으며 오히려 문서의 크기를 줄입니다.

```java
    public static void RemovingUnusedObjects() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        
        optimizationOptions.setRemoveUnusedObjects(true);
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "emoveUnusedObjects_out.pdf";

        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir);

    }
```
## 사용되지 않는 스트림 제거

때때로 문서에는 사용되지 않는 리소스 스트림이 포함되어 있습니다.
 이 스트림들은 페이지의 리소스 사전에서 참조되기 때문에 "사용되지 않는 객체"가 아닙니다. 이는 이미지가 페이지에서 제거되었지만 페이지 리소스에서는 제거되지 않은 경우에 발생할 수 있습니다. 또한, 문서에서 페이지가 추출되고 문서 페이지에 "공통" 리소스, 즉 동일한 Resources 객체가 있을 때 이러한 상황이 자주 발생합니다. 리소스 스트림이 사용되는지 여부를 판단하기 위해 페이지 내용을 분석합니다. 사용되지 않는 스트림은 제거됩니다. 때때로 이것은 문서 크기를 줄입니다.

```java
public static void RemovingUnusedStream() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + 
        "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "removeUnusedObjects_out.pdf";
        
        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir);
        
    }
```
## 중복 스트림 연결

때때로 문서는 여러 개의 동일한 리소스 스트림(예: 이미지)을 포함합니다. 이는 예를 들어 문서가 자신과 연결될 때 발생할 수 있습니다. 출력 문서는 동일한 리소스 스트림의 두 개의 독립적인 복사본을 포함합니다. 우리는 모든 리소스 스트림을 분석하고 비교합니다. 스트림이 중복된 경우 병합됩니다. 즉, 한 개의 복사본만 남기고 참조가 적절하게 변경되며 객체의 복사본이 제거됩니다. 때로는 이렇게 하면 문서 크기가 줄어듭니다.

```java
    public static void LinkingDuplicateStream() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        
        // OptimizationOptions를 사용하여 PDF 문서 최적화
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir);
    }
```

또한, AllowReusePageContent 설정을 사용할 수 있습니다. 이 속성이 true로 설정되면, 동일한 페이지에 대해 문서를 최적화할 때 페이지 콘텐츠가 재사용됩니다.

```java
public static void AllowReusePageContent() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setAllowReusePageContent(true);
        
        // OptimizationOptions를 사용하여 PDF 문서 최적화
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir);
    }
```
## 폰트 내장 해제

문서가 내장 폰트를 사용하는 경우, 모든 폰트 데이터가 문서에 포함된 것을 의미합니다.
 문서의 장점은 사용자의 컴퓨터에 폰트가 설치되어 있지 않더라도 문서를 볼 수 있다는 점입니다. 하지만 폰트를 포함하면 문서의 크기가 커집니다. 포함된 폰트를 제거하는 방법은 모든 포함된 폰트를 제거합니다. 이렇게 하면 문서의 크기는 줄어들지만, 올바른 폰트가 설치되어 있지 않으면 문서가 읽을 수 없게 될 수 있습니다.

```java
    public static void UnembedFonts() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setUnembedFonts(true);
        
        // OptimizationOptions를 사용하여 PDF 문서 최적화
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir);
    }
```

## 주석 제거 또는 평면화

주석이 불필요한 경우 삭제할 수 있습니다. 필요할 때 추가 편집이 필요하지 않으면 평탄화할 수 있습니다. 이 두 기술 모두 파일 크기를 줄일 것입니다.

```java
    public static void FlatteningAnnotations() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        for (Page page : pdfDocument.getPages()) {
            for (Annotation annotation : page.getAnnotations())
                annotation.flatten();
        }

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir);
    }

```
## 양식 필드 제거

PDF 문서에 AcroForms가 포함되어 있는 경우 양식 필드를 평탄화하여 파일 크기를 줄일 수 있습니다.

```java
    public static void RemovingFormFields() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        // 양식 평탄화
        if (pdfDocument.getForm().getFields().length > 0) {
            for (Field field : pdfDocument.getForm().getFields()) {
                field.flatten();
            }
        }
        _dataDir = _dataDir + "FlattenForms_out.pdf";
        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir);
    }

```
## RGB 색상 공간의 PDF를 그레이스케일로 변환하기

PDF 파일은 텍스트, 이미지, 첨부 파일, 주석, 그래프 및 기타 객체로 구성됩니다. PDF를 RGB 색상 공간에서 그레이스케일로 변환해야 하는 요구 사항이 있을 수 있습니다. 이렇게 하면 해당 PDF 파일을 인쇄할 때 더 빨라질 것입니다. 또한 파일을 그레이스케일로 변환하면 문서의 크기도 줄어들지만, 이로 인해 문서의 품질이 떨어질 수 있습니다. 현재 이 기능은 Adobe Acrobat의 Pre-Flight 기능에 의해 지원되지만, Office 자동화에 대해 이야기할 때 Aspose.PDF는 문서 조작을 위한 최상의 솔루션을 제공합니다.

이 요구 사항을 달성하기 위해 다음 코드 스니펫을 사용할 수 있습니다.

```java
    public static void ConvertRGBtoGrayscale() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        com.aspose.pdf.RgbToDeviceGrayConversionStrategy strategy = new com.aspose.pdf.RgbToDeviceGrayConversionStrategy();
        for (int idxPage = 1; idxPage <= pdfDocument.getPages().size(); idxPage++) {
            Page page = pdfDocument.getPages().get_Item(idxPage);
            strategy.convert(page);
        }
        pdfDocument.save("output.pdf");
    }
```

## FlateDecode 압축

Aspose.PDF for Java는 PDF 최적화 기능을 위한 FlateDecode 압축을 지원합니다. 아래 코드 스니펫은 FlateDecode 압축으로 이미지를 저장하기 위해 최적화 옵션을 사용하는 방법을 보여줍니다:

```java
    public static void FlateDecodeCompression() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);

        // OptimizationOptions를 사용하여 PDF 문서 최적화
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir);
    }
```
## XImageCollection에 이미지 저장

Aspose.PDF for Java는 FlateDecode 압축을 사용하여 새로운 이미지를 [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection)에 저장할 수 있는 기능을 제공합니다.
 이 옵션을 활성화하려면 ImageFilterType.Flate 플래그를 사용할 수 있습니다. 다음 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다:

```java
    public static void StoreImageInXImageCollection() {
        // 문서 초기화
        Document document = new Document();
        document.getPages().add();
        Page page = document.getPages().get_Item(1);

        // 이미지 스트림으로 로드
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        page.getResources().getImages().add(imageStream, ImageFilterType.Flate);
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        page.getContents().add(new com.aspose.pdf.operators.GSave());

        // 좌표 설정
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });
        // ConcatenateMatrix (행렬 연결) 연산자 사용: 이미지가 어떻게 배치되어야 하는지 정의
        page.getContents().add(new com.aspose.pdf.operators.ConcatenateMatrix(matrix));
        page.getContents().add(new com.aspose.pdf.operators.Do(ximage.getName()));
        page.getContents().add(new com.aspose.pdf.operators.GRestore());

        document.save(_dataDir + "FlateDecodeCompression.pdf");
    }

}
```