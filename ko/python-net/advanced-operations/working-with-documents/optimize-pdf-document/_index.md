---
title: 파이썬에서 PDF 파일 최적화하기
linktitle: PDF 최적화
type: docs
weight: 30
url: /ko/python-net/optimize-pdf/
description: Aspose.PDF 파일을 사용하여 Python에서 PDF 파일 크기를 최적화, 압축 및 줄이는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬을 사용하여 PDF 페이지 압축하기
Abstract: 이 문서에서는 웹 페이지, 이메일 및 스토리지 시스템과 같은 다양한 플랫폼에서 PDF 파일을 최적화하여 크기를 줄이고 성능을 향상시키는 방법에 대한 포괄적인 가이드를 제공합니다.최적화 기법에는 이미지 크기 축소, 사용하지 않는 리소스 제거, 글꼴 포함 해제가 포함됩니다.Python용 Aspose.PDF 의 '최적화' 및 'OptimizeResources' 메서드를 활용하여 웹용으로 PDF를 최적화하고 전체 파일 크기를 줄이는 구체적인 방법에 대해 설명합니다.'최적화 옵션'을 통해 최적화 전략을 사용자 정의할 수 있으며, 이를 통해 이미지 압축, 사용하지 않는 객체 및 스트림 제거, 중복 스트림 연결, 글꼴 포함 해제와 같은 특정 작업을 수행할 수 있습니다.추가 전략으로는 주석 병합, 양식 필드 제거, PDF 파일을 RGB에서 그레이스케일로 변환하여 크기를 더욱 줄이는 것이 포함됩니다.또한 이 기사에서는 품질과 기능을 유지하면서 효과적인 PDF 파일 관리를 보장하는 FlateDecode 압축을 이미지 최적화에 사용하는 방법을 중점적으로 설명합니다.
---

PDF 문서에는 때때로 추가 데이터가 포함될 수 있습니다.PDF 파일 크기를 줄이면 네트워크 전송 및 저장을 최적화하는 데 도움이 됩니다.이는 웹 페이지에 게시하거나, 소셜 네트워크에서 공유하거나, 이메일로 전송하거나, 스토리지에 보관할 때 특히 유용합니다.여러 가지 기술을 사용하여 PDF를 최적화할 수 있습니다.

문서를 처음부터 다시 작성하지 않고도 웹 전송, 이메일 공유, 저장 공간 절약 또는 인쇄용 출력을 위해 PDF 크기를 줄여야 하는 경우 이 페이지를 사용하십시오.

- 온라인 브라우징을 위한 페이지 콘텐츠 최적화
- 모든 이미지 축소 또는 압축
- 페이지 콘텐츠 재사용 활성화
- 중복 스트림 병합
- 언임베드 글꼴
- 사용하지 않는 오브젝트 제거
- 병합 양식 필드 제거
- 주석 제거 또는 병합

{{% alert color="primary" %}}

 최적화 방법에 대한 자세한 설명은 최적화 방법 개요 페이지에서 확인할 수 있습니다.

{{% /alert %}}

## 웹용 PDF 문서 최적화

웹의 최적화 또는 선형화는 웹 브라우저를 사용하여 온라인 브라우징에 적합한 PDF 파일을 만드는 프로세스를 말합니다.웹 디스플레이에 맞게 파일을 최적화하려면:

1. 에서 입력 문서 열기 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 목적.
1. 사용 [최적화](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 방법.
1. 를 사용하여 최적화된 문서를 저장합니다. [저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 방법.

다음 코드 스니펫은 웹용 PDF 문서를 최적화하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def optimize_pdf(infile, outfile):
    document = ap.Document(infile)
    document.optimize()
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## PDF 크기 줄이기

더 [리소스 최적화 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하면 불필요한 정보를 제거하여 문서 크기를 줄일 수 있습니다.기본적으로 이 방법은 다음과 같이 작동합니다.

- 문서 페이지에서 사용되지 않는 리소스는 제거됩니다.
- 동일한 리소스가 하나의 오브젝트로 결합됩니다.
- 사용하지 않은 객체는 삭제됩니다.

아래 스니펫은 예시입니다.하지만 이 방법으로는 문서 축소를 보장할 수 없다는 점에 유의하세요.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def reduce_size_pdf(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## 최적화 전략 관리

최적화 전략을 사용자 지정할 수도 있습니다.현재 [리소스 최적화 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 방법은 5가지 기법을 사용합니다.이러한 기술은 다음과 함께 optimizeResources () 메서드를 사용하여 적용할 수 있습니다. [최적화 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) 매개변수.

### 모든 이미지 축소 또는 압축

이미지 작업에는 이미지 품질을 낮추거나 해상도를 변경하는 두 가지 방법이 있습니다.어떤 경우든 [이미지 압축 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) 적용해야 합니다.다음 예에서는 이미지 품질을 50으로 줄여 이미지를 축소합니다.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def shrinking_or_compressing_all_images(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### 사용하지 않은 오브젝트 제거

PDF 문서에는 문서의 다른 객체에서 참조되지 않는 PDF 객체가 포함되는 경우가 있습니다.예를 들어, 문서 페이지 트리에서 페이지는 제거되었지만 페이지 개체 자체는 제거되지 않은 경우 이런 일이 발생할 수 있습니다.이러한 개체를 제거해도 문서가 유효하지 않게 되는 것이 아니라 축소됩니다.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_objects(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedObjects option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### 미사용 스트림 제거

문서에 사용되지 않은 리소스 스트림이 포함되어 있는 경우가 있습니다.이러한 스트림은 페이지 리소스 사전에서 참조되므로 “미사용 객체”가 아닙니다.따라서 “사용하지 않은 개체 제거” 방법을 사용해도 제거되지 않습니다.하지만 이러한 스트림은 페이지 콘텐츠와 함께 사용되지 않습니다.이미지가 페이지에서는 제거되었지만 페이지 리소스에서는 제거되지 않은 경우에 이런 일이 발생할 수 있습니다.또한 이러한 상황은 문서에서 페이지를 추출하고 문서 페이지에 “공통” 리소스, 즉 동일한 리소스 개체가 있을 때 자주 발생합니다.리소스 스트림의 사용 여부를 확인하기 위해 페이지 콘텐츠를 분석합니다.사용하지 않은 스트림은 제거됩니다.이로 인해 문서 크기가 줄어드는 경우가 있습니다.이 기법의 사용은 이전 단계와 비슷합니다.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### 중복 스트림 연결

일부 문서에는 동일한 리소스 스트림 (예: 이미지) 이 여러 개 포함될 수 있습니다.예를 들어 문서가 그 자체와 연결된 경우 이런 일이 발생할 수 있습니다.출력 문서에는 동일한 리소스 스트림의 독립적인 사본 두 개가 포함되어 있습니다.모든 리소스 스트림을 분석하고 비교합니다.스트림이 복제되면 병합됩니다. 즉, 복사본이 하나만 남습니다.참조가 적절하게 변경되고 객체 사본이 제거됩니다.경우에 따라 문서 크기를 줄이는 데 도움이 됩니다.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def linking_duplicate_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set link_duplicate_streams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplicate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### 글꼴 언임베딩

문서에 포함된 글꼴이 사용되는 경우 모든 글꼴 데이터가 문서에 저장된다는 의미입니다.장점은 사용자의 컴퓨터에 글꼴이 설치되어 있는지 여부와 상관없이 문서를 볼 수 있다는 것입니다.하지만 글꼴을 포함하면 문서 크기가 커집니다.unembed fonts 메서드는 포함된 글꼴을 모두 제거합니다.따라서 문서 크기는 줄어들지만 올바른 글꼴을 설치하지 않으면 문서 자체를 읽을 수 없게 될 수 있습니다.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def unembed_fonts(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set unembed_fonts option
    optimize_options = ap.optimization.OptimizationOptions()
    optimize_options.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimize_options)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

최적화 리소스는 이러한 메서드를 문서에 적용합니다.이러한 방법 중 하나라도 적용하면 문서 크기가 줄어들 가능성이 큽니다.이러한 방법을 전혀 적용하지 않으면 문서 크기가 변경되지 않습니다. 이는 명백합니다.

## PDF 문서 크기를 줄이는 추가 방법

### 주석 제거 또는 병합하기

주석은 불필요한 경우 삭제할 수 있습니다.필요하지만 추가 편집이 필요하지 않은 경우 병합할 수 있습니다.두 방법 모두 파일 크기를 줄일 수 있습니다.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_annotations(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(outfile)
```

### 양식 필드 제거

PDF 문서에 AcroForms가 포함된 경우 양식 필드를 평면화하여 파일 크기를 줄일 수 있습니다.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_forms(infile, outfile):
    # Load source PDF form
    doc = ap.Document(infile)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### PDF를 RGB 컬러스페이스에서 그레이스케일로 변환

PDF 파일은 텍스트, 이미지, 첨부 파일, 주석, 그래프 및 기타 개체로 구성됩니다.PDF 파일을 더 빠르게 인쇄하려면 PDF를 RGB 색상 공간에서 회색조로 변환해야 하는 요구 사항이 있을 수 있습니다.또한 파일을 그레이스케일로 변환하면 문서 크기도 줄어들지만 문서 품질이 저하될 수도 있습니다.이 기능은 현재 Adobe Acrobat의 Pre-Flight 기능에서 지원되지만, 사무 자동화에 대해 말씀드리자면 Aspose.PDF 는 문서 조작에 이러한 이점을 제공하는 궁극적인 솔루션입니다.이 요구 사항을 충족하기 위해 다음 코드 스니펫을 사용할 수 있습니다.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def сonvert_PDF_from_RGB_colorspace_to_grayscale(infile, outfile):
    document = ap.Document(infile)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(outfile)
```

### 플랫 디코드 압축

.NET을 통한 파이썬용 Aspose.PDF 는 PDF 최적화 기능을 위한 플랫디코드 압축을 지원합니다.아래 코드 스니펫은 최적화 옵션을 사용하여 **FlateDecode** 압축으로 이미지를 저장하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def using_flatedecode_compression(infile, outfile):

    # Open Document
    doc = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = (
        ap.optimization.ImageEncoding.FLATE
    )
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(outfile)
```

## 관련 문서 주제

- [파이썬에서 PDF 문서로 작업하기](/pdf/ko/python-net/working-with-documents/)
- [파이썬으로 PDF 파일 병합](/pdf/ko/python-net/merge-pdf-documents/)
- [파이썬으로 PDF 파일 분할하기](/pdf/ko/python-net/split-document/)
- [파이썬에서 PDF 문서 조작하기](/pdf/ko/python-net/manipulate-pdf-document/)

