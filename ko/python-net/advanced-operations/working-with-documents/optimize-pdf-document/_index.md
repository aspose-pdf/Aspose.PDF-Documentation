---
title: PDF 크기 최적화, 압축 또는 줄이기
linktitle: PDF 최적화
type: docs
weight: 30
url: /ko/python-net/optimize-pdf/
description: PDF 파일 최적화, 모든 이미지 축소, PDF 크기 줄이기, 폰트 비내장화, 사용되지 않는 객체 제거를 Python으로 수행합니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python을 사용하여 PDF 최적화",
    "alternativeHeadline": "Python으로 PDF 최적화하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, optimize pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "PDF 파일 최적화, 모든 이미지 축소, PDF 크기 줄이기, 폰트 비내장화, 사용되지 않는 객체 제거를 Python으로 수행합니다."
}
</script>


PDF 문서는 때때로 추가 데이터를 포함할 수 있습니다. PDF 파일의 크기를 줄이면 네트워크 전송 및 저장을 최적화하는 데 도움이 됩니다. 이는 웹 페이지에 게시하거나, 소셜 네트워크에서 공유하거나, 이메일로 전송하거나, 저장소에 보관할 때 특히 유용합니다. PDF를 최적화하기 위해 몇 가지 기술을 사용할 수 있습니다:

- 온라인 브라우징을 위한 페이지 콘텐츠 최적화
- 모든 이미지 축소 또는 압축
- 페이지 콘텐츠 재사용 가능하도록 설정
- 중복 스트림 병합
- 글꼴 제거
- 사용되지 않는 객체 제거
- 평면화된 폼 필드 제거
- 주석 제거 또는 평면화

{{% alert color="primary" %}}

최적화 방법에 대한 자세한 설명은 최적화 방법 개요 페이지에서 찾을 수 있습니다.

{{% /alert %}}

## 웹을 위한 PDF 문서 최적화

웹을 위한 최적화 또는 선형화는 웹 브라우저를 사용하여 온라인 브라우징에 적합한 PDF 파일을 만드는 과정을 의미합니다. 웹 디스플레이에 파일을 최적화하려면:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체에서 입력 문서를 엽니다.
1. [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용합니다.
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 최적화된 문서를 저장합니다.

다음 코드 스니펫은 웹을 위해 PDF 문서를 최적화하는 방법을 보여줍니다.

```python 

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 웹을 위해 최적화
    document.optimize()

    # 출력 문서 저장
    document.save(output_pdf)
```

## PDF 크기 줄이기

[OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드는 불필요한 정보를 제거하여 문서 크기를 줄일 수 있도록 해줍니다. 기본적으로 이 메서드는 다음과 같이 작동합니다:

- 문서 페이지에서 사용되지 않는 리소스가 제거됩니다.
- 동일한 리소스는 하나의 객체로 결합됩니다.

- 사용되지 않는 객체가 삭제됩니다.

아래 스니펫은 예제입니다. 하지만, 이 방법이 문서 축소를 보장할 수는 없습니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    # PDF 문서 최적화. 하지만, 이 방법이 문서 축소를 보장할 수는 없습니다
    document.optimize_resources()
    # 업데이트된 문서 저장
    document.save(output_pdf)
```

## 최적화 전략 관리

우리는 최적화 전략을 사용자 정의할 수도 있습니다. 현재, [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메소드는 5가지 기술을 사용합니다. 이 기술들은 [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) 매개변수를 사용하여 OptimizeResources() 메소드를 통해 적용될 수 있습니다.

### 모든 이미지 축소 또는 압축

우리는 이미지 품질을 낮추고/또는 해상도를 변경하는 두 가지 방법으로 이미지를 다룰 수 있습니다.
 어쨌든, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/)을 적용해야 합니다. 다음 예제에서는 ImageQuality를 50으로 줄여 이미지를 축소합니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    # OptimizationOptions 초기화
    optimizeOptions = ap.optimization.OptimizationOptions()
    # CompressImages 옵션 설정
    optimizeOptions.image_compression_options.compress_images = True
    # ImageQuality 옵션 설정
    optimizeOptions.image_compression_options.image_quality = 50
    # OptimizationOptions를 사용하여 PDF 문서 최적화
    document.optimize_resources(optimizeOptions)
    # 업데이트된 문서 저장
    document.save(output_pdf)
```

### 사용되지 않는 객체 제거하기

PDF 문서에는 가끔 문서 내의 다른 객체에서 참조되지 않는 PDF 객체가 포함되어 있을 수 있습니다. 이러한 상황은 예를 들어, 페이지가 문서 페이지 트리에서 제거되었지만 페이지 객체 자체는 제거되지 않았을 때 발생할 수 있습니다. 이러한 객체를 제거하는 것은 문서를 무효화하지 않으며 오히려 문서의 크기를 줄입니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    # RemoveUsedObject 옵션 설정
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # OptimizationOptions를 사용하여 PDF 문서 최적화
    document.optimize_resources(optimizeOptions)
    # 업데이트된 문서 저장
    document.save(output_pdf)
```

### 사용되지 않는 스트림 제거

때때로 문서에는 사용되지 않는 리소스 스트림이 포함되어 있습니다. 이 스트림들은 페이지 리소스 사전에서 참조되기 때문에 "사용되지 않는 객체"가 아닙니다. 따라서 "사용되지 않는 객체 제거" 방법으로 제거되지 않습니다. 하지만 이 스트림들은 페이지 콘텐츠와 함께 사용되지 않습니다. 이는 이미지가 페이지에서 제거되었지만 페이지 리소스에서는 제거되지 않은 경우에 발생할 수 있습니다. 또한, 문서에서 페이지가 추출되고 문서 페이지가 "공통" 리소스, 즉 동일한 Resources 객체를 가지고 있을 때 이 상황이 자주 발생합니다. 리소스 스트림이 사용되는지 여부를 결정하기 위해 페이지 콘텐츠가 분석됩니다. 사용되지 않는 스트림은 제거됩니다. 이는 때때로 문서 크기를 줄여줍니다. 이 기술의 사용은 이전 단계와 유사합니다:

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    # RemoveUsedStreams 옵션 설정
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # OptimizationOptions를 사용하여 PDF 문서 최적화
    document.optimize_resources(optimizeOptions)
    # 업데이트된 문서 저장
    document.save(output_pdf)
```

### 중복 스트림 연결

일부 문서는 여러 개의 동일한 리소스 스트림(예: 이미지)을 포함할 수 있습니다. 예를 들어, 문서가 자기 자신과 연결될 때 이런 일이 발생할 수 있습니다. 출력 문서에는 동일한 리소스 스트림의 두 개의 독립적인 복사본이 포함됩니다. 우리는 모든 리소스 스트림을 분석하고 비교합니다. 스트림이 중복되면 병합되며, 즉 하나의 복사본만 남게 됩니다. 참조가 적절히 변경되고, 객체의 복사본은 제거됩니다. 경우에 따라 문서 크기를 줄이는 데 도움이 됩니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    # LinkDuplcateStreams 옵션 설정
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # OptimizationOptions를 사용하여 PDF 문서 최적화
    document.optimize_resources(optimizeOptions)
    # 업데이트된 문서 저장
    document.save(output_pdf)
```

### 글꼴 내장 해제

문서가 내장된 글꼴을 사용하는 경우, 이는 모든 글꼴 데이터가 문서에 저장됨을 의미합니다.
 사용자 기기에 글꼴이 설치되어 있는지 여부에 관계없이 문서를 볼 수 있다는 장점이 있습니다. 하지만 글꼴을 포함하면 문서 크기가 커집니다. 포함된 글꼴 제거 방법은 모든 포함된 글꼴을 제거합니다. 따라서 문서 크기는 줄어들지만 올바른 글꼴이 설치되지 않은 경우 문서 자체가 읽을 수 없게 될 수 있습니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    # UnembedFonts 옵션 설정
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # OptimizationOptions를 사용하여 PDF 문서 최적화
    document.optimize_resources(optimizeOptions)
    # 업데이트된 문서 저장
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "원본 파일 크기: {}. 줄어든 파일 크기: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

최적화 리소스는 이러한 방법을 문서에 적용합니다. 이 방법들이 적용되면 문서 크기가 대부분 줄어들 것입니다. 이러한 방법들이 적용되지 않으면 문서 크기는 변하지 않을 것입니다.

## PDF 문서 크기를 줄이는 추가 방법

### 주석 제거 또는 평탄화

주석은 불필요할 경우 삭제할 수 있습니다. 필요하지만 추가 편집이 필요하지 않을 경우 평탄화할 수 있습니다. 이 두 가지 기술 모두 파일 크기를 줄일 것입니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    # 주석 평탄화
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # 업데이트된 문서 저장
    document.save(output_pdf)
```

### 양식 필드 제거

PDF 문서에 AcroForms가 포함되어 있는 경우, 양식 필드를 평탄화하여 파일 크기를 줄일 수 있습니다.

```python

    import aspose.pdf as ap

    # 소스 PDF 양식 로드
    doc = ap.Document(input_pdf)

    # 양식 평탄화
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # 업데이트된 문서 저장
    doc.save(output_pdf)
```

### RGB 색상 공간의 PDF를 그레이스케일로 변환

PDF 파일은 텍스트, 이미지, 첨부 파일, 주석, 그래프 및 기타 객체로 구성됩니다. PDF를 RGB 색상 공간에서 그레이스케일로 변환해야 하는 요구 사항이 있을 수 있으며, 이렇게 하면 PDF 파일을 인쇄할 때 더 빠르게 처리할 수 있습니다. 또한 파일이 그레이스케일로 변환되면 문서 크기가 줄어들지만, 문서 품질이 저하될 수도 있습니다. 이 기능은 현재 Adobe Acrobat의 Pre-Flight 기능에서 지원되지만, 오피스 자동화와 관련하여 Aspose.PDF는 문서 조작을 위한 궁극적인 솔루션을 제공합니다. 이 요구 사항을 충족하기 위해 다음 코드 스니펫을 사용할 수 있습니다.

```python

    import aspose.pdf as ap

    # 소스 PDF 파일 로드
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # RGB 색상 공간 이미지를 그레이스케일 색상 공간으로 변환
        strategy.convert(page)

    # 결과 파일 저장
    document.save(output_pdf)
```


### FlateDecode 압축

Aspose.PDF for Python via .NET은 PDF 최적화 기능을 위한 FlateDecode 압축 지원을 제공합니다. 아래의 코드 스니펫은 이미지 저장에 **FlateDecode** 압축 옵션을 사용하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    # 문서 열기
    doc = ap.Document(input_pdf)
    # OptimizationOptions 초기화
    optimizationOptions = ap.optimization.OptimizationOptions()
    # FlateDecode 압축을 사용하여 이미지를 최적화하려면 최적화 옵션을 Flate로 설정
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # 최적화 옵션 설정
    doc.optimize_resources(optimizationOptions)
    # 문서 저장
    doc.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>