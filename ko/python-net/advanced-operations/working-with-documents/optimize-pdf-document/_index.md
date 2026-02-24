---
title: Python에서 PDF 크기 최적화, 압축 또는 축소
linktitle: PDF 최적화
type: docs
weight: 30
url: /ko/python-net/optimize-pdf/
description: Aspose.PDF를 사용하여 웹 성능을 개선하고 파일 크기를 줄이기 위해 Python에서 PDF 문서를 최적화하는 방법을 배웁니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF 페이지 압축
Abstract: 이 문서는 PDF 파일을 최적화하여 크기를 줄이고 웹 페이지, 이메일, 스토리지 시스템과 같은 다양한 플랫폼에서 성능을 향상시키는 포괄적인 가이드를 제공합니다. 최적화 기술에는 이미지 크기 축소, 사용되지 않은 리소스 제거, 글꼴 임베드 해제 등이 포함됩니다. 웹용 PDF 최적화 및 전체 파일 크기 감소를 위한 구체적인 방법으로 Python용 Aspose.PDF의 `Optimize` 및 `OptimizeResources` 메서드를 활용합니다. `OptimizationOptions`를 통해 최적화 전략을 맞춤화할 수 있으며, 이미지 압축, 사용되지 않은 객체 및 스트림 제거, 중복 스트림 연결, 글꼴 임베드 해제와 같은 목표 지향적인 작업을 수행합니다. 추가 전략으로는 주석 플래튼, 양식 필드 제거, PDF 파일을 RGB에서 그레이스케일로 변환하여 크기를 더욱 줄이는 방법이 포함됩니다. 또한 이미지 최적화를 위해 FlateDecode 압축을 사용하는 것을 강조하여 품질과 기능을 유지하면서 효과적인 PDF 파일 관리를 보장합니다.
---

PDF 문서는 때때로 추가 데이터를 포함할 수 있습니다. PDF 파일 크기를 줄이면 네트워크 전송 및 저장을 최적화하는 데 도움이 됩니다. 이는 웹 페이지에 게시하거나 소셜 네트워크에 공유하고, 이메일로 전송하거나 저장소에 보관할 때 특히 유용합니다. PDF를 최적화하기 위해 여러 기술을 사용할 수 있습니다:

- 온라인 브라우징을 위한 페이지 콘텐츠 최적화
- 모든 이미지 축소 또는 압축
- 페이지 콘텐츠 재사용 활성화
- 중복 스트림 병합
- 글꼴 임베드 해제
- 사용되지 않은 객체 제거
- 플래튼 폼 필드 제거
- 주석 제거 또는 플래튼

{{% alert color="primary" %}}

최적화 방법에 대한 자세한 설명은 최적화 방법 개요 페이지에서 확인할 수 있습니다.

{{% /alert %}}

## 웹용 PDF 문서 최적화

최적화, 또는 웹용 선형화는 PDF 파일을 웹 브라우저를 통해 온라인으로 보기 적합하도록 만드는 과정을 말합니다. 웹 표시용 파일을 최적화하려면:

1. 입력 문서를 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체에서 엽니다.
1. [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용합니다.
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 최적화된 문서를 저장합니다.

다음 코드 스니펫은 웹용 PDF 문서를 최적화하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    document.optimize()
    document.save(path_outfile)
```

## PDF 크기 축소

[OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드는 불필요한 정보를 제거하여 문서 크기를 줄일 수 있게 해줍니다. 기본적으로 이 메서드는 다음과 같이 작동합니다:

- 문서 페이지에서 사용되지 않는 리소스가 제거됩니다
- 동일한 리소스가 하나의 객체로 합쳐집니다
- 사용되지 않은 객체가 삭제됩니다

아래 스니펫은 예시입니다. 다만, 이 메서드가 문서 축소를 보장하지는 못한다는 점에 유의하세요.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(output_pdf)
```

## 최적화 전략 관리

우리는 최적화 전략을 맞춤화할 수도 있습니다. 현재 [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드는 5가지 기술을 사용합니다. 이러한 기술은 [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) 매개변수를 사용하여 OptimizeResources() 메서드와 함께 적용할 수 있습니다.

### 모든 이미지 축소 또는 압축

이미지를 다루는 방법은 두 가지입니다: 이미지 품질을 낮추거나 해상도를 변경합니다. 어떤 경우든 [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/)를 적용해야 합니다. 다음 예시에서는 ImageQuality를 50으로 낮추어 이미지를 축소합니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### 사용되지 않은 객체 제거

PDF 문서는 때때로 문서 내 다른 객체에서 참조되지 않는 PDF 객체를 포함할 수 있습니다. 예를 들어, 페이지가 문서 페이지 트리에서 제거되었지만 해당 페이지 객체 자체는 제거되지 않은 경우가 있습니다. 이러한 객체를 제거해도 문서가 무효화되지 않으며 오히려 크기가 줄어듭니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedObject option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### 사용되지 않은 스트림 제거

때때로 문서에는 사용되지 않는 리소스 스트림이 포함됩니다. 이러한 스트림은 페이지 리소스 사전에서 참조되기 때문에 “사용되지 않은 객체”가 아니며, 따라서 “사용되지 않은 객체 제거” 메서드로는 삭제되지 않습니다. 하지만 이러한 스트림은 페이지 콘텐츠와는 전혀 사용되지 않습니다. 이는 이미지가 페이지에서 제거되었지만 페이지 리소스에서는 제거되지 않은 경우에 발생할 수 있습니다. 또한, 문서에서 페이지를 추출하고 추출된 페이지들이 동일한 Resources 객체와 같은 “공통” 리소스를 공유할 때도 자주 발생합니다. 페이지 콘텐츠를 분석하여 리소스 스트림이 사용되는지를 판단하고, 사용되지 않는 스트림을 제거합니다. 이는 때때로 문서 크기를 감소시킵니다. 이 기술의 사용은 이전 단계와 유사합니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### 중복 스트림 연결

몇몇 문서는 여러 개의 동일한 리소스 스트림(예: 이미지)을 포함할 수 있습니다. 이는 예를 들어 문서를 자체와 연결(concatenate)할 때 발생할 수 있습니다. 출력 문서는 동일한 리소스 스트림의 두 개 독립 사본을 포함합니다. 우리는 모든 리소스 스트림을 분석하고 비교합니다. 스트림이 중복된 경우, 하나로 병합되어 사본이 하나만 남게 됩니다. 참조는 적절히 변경되고 객체의 복사본은 제거됩니다. 경우에 따라 이는 문서 크기를 감소시키는 데 도움이 됩니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set LinkDuplicateStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### 글꼴 임베드 해제

문서가 임베드된 글꼴을 사용한다면 모든 글꼴 데이터가 문서에 저장된다는 의미입니다. 장점은 사용자의 컴퓨터에 해당 글꼴이 설치되어 있지 않아도 문서를 볼 수 있다는 점입니다. 그러나 글꼴을 임베드하면 문서 크기가 증가합니다. 임베드 해제 메서드는 모든 임베드된 글꼴을 제거합니다. 따라서 문서 크기가 감소하지만, 올바른 글꼴이 설치되지 않은 경우 문서를 읽을 수 없게 될 수 있습니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set UnembedFonts  option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

최적화 리소스는 이러한 메서드들을 문서에 적용합니다. 이 중 하나라도 적용되면 문서 크기가 대부분 감소할 것입니다. 어떤 메서드도 적용되지 않으면 문서 크기는 변하지 않으며 이는 명백합니다.

## PDF 문서 크기를 줄이는 추가 방법

### 주석 제거 또는 평탄화

주석이 불필요할 경우 삭제할 수 있습니다. 필요하지만 추가 편집이 필요하지 않을 경우 평탄화할 수 있습니다. 이러한 두 기술 모두 파일 크기를 줄입니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(output_pdf)
```

### 양식 필드 제거

PDF 문서에 AcroForms가 포함되어 있으면 양식 필드를 평탄화하여 파일 크기를 줄일 수 있습니다.

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```

### PDF를 RGB 색공간에서 그레이스케일로 변환

PDF 파일은 텍스트, 이미지, 첨부 파일, 주석, 그래프 및 기타 객체로 구성됩니다. PDF 파일을 인쇄할 때 더 빠르게 처리하기 위해 RGB 색공간에서 그레이스케일로 변환해야 하는 경우가 있을 수 있습니다. 또한 파일을 그레이스케일로 변환하면 문서 크기도 감소하지만, 문서 품질이 떨어질 수도 있습니다. 이 기능은 현재 Adobe Acrobat의 Pre‑Flight 기능에서 지원되지만, Office 자동화와 관련해서는 Aspose.PDF가 문서 조작을 위한 최고의 솔루션을 제공합니다. 이 요구 사항을 구현하려면 다음 코드 조각을 사용할 수 있습니다.

```python

    import aspose.pdf as ap

    # Load source PDF file
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(output_pdf)
```

### FlateDecode 압축

Aspose.PDF for Python via .NET는 PDF 최적화 기능을 위한 FlateDecode 압축 지원을 제공합니다. 아래 코드 조각은 최적화 옵션에서 이미지를 **FlateDecode** 압축으로 저장하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open Document
    doc = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(output_pdf)
```


