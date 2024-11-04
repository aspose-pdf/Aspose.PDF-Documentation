---
title: 파이썬에서 PDF를 파워포인트로 변환
linktitle: PDF를 파워포인트로 변환
type: docs
weight: 30
url: /python-net/convert-pdf-to-powerpoint/
description: Aspose.PDF는 파이썬을 사용하여 PDF를 PPT(파워포인트) 형식으로 변환할 수 있습니다. 한 가지 방법으로는 슬라이드를 이미지로 변환하여 PDF를 PPTX로 변환할 수 있는 가능성이 있습니다.
lastmod: "2022-12-23"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 개요

PDF 파일을 파워포인트로 변환할 수 있나요? 네, 가능합니다! 그리고 쉽습니다!
이 글에서는 파이썬을 사용하여 **PDF를 파워포인트로 변환하는 방법**을 설명합니다. 이 주제를 다룹니다.

_형식_: **PPTX**
- [파이썬 PDF를 PPTX로](#python-pdf-to-pptx)
- [파이썬 PDF를 PPTX로 변환](#python-pdf-to-pptx)
- [파이썬 PDF 파일을 PPTX로 변환하는 방법](#python-pdf-to-pptx)

_형식_: **파워포인트**
- [파이썬 PDF를 파워포인트로](#python-pdf-to-powerpoint)
- [파이썬 PDF를 파워포인트로 변환](#python-pdf-to-powerpoint)
- [파이썬 PDF 파일을 파워포인트로 변환하는 방법](#python-pdf-to-powerpoint)


## 파이썬 PDF를 파워포인트 및 PPTX 변환

**Aspose.PDF for Python via .NET**은 PDF에서 PPTX로의 변환 진행 상황을 추적할 수 있게 해줍니다.

우리는 Aspose.Slides라는 API를 가지고 있으며, 이를 통해 PPT/PPTX 프레젠테이션을 생성하고 조작할 수 있는 기능을 제공합니다. 이 API는 또한 PPT/PPTX 파일을 PDF 형식으로 변환하는 기능도 제공합니다. 이 변환 과정에서 PDF 파일의 개별 페이지는 PPTX 파일의 개별 슬라이드로 변환됩니다.

PDF에서 <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>로 변환하는 동안 텍스트는 선택/업데이트할 수 있는 텍스트로 렌더링됩니다. PDF 파일을 PPTX 형식으로 변환하기 위해서는 Aspose.PDF에서 [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/)라는 클래스를 제공합니다. PptxSaveOptions 클래스의 객체는 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)의 두 번째 인수로 전달됩니다. 다음 코드 스니펫은 PDF 파일을 PPTX 형식으로 변환하는 과정을 보여줍니다.

## Python과 Aspose.PDF for Python을 사용한 간단한 PDF에서 PowerPoint로의 변환

PDF를 PPTX로 변환하기 위해, Aspose.PDF for Python은 다음 코드 단계를 사용할 것을 권장합니다.

<a name="csharp-pdf-to-powerpoint"><strong>단계: Python에서 PDF를 PowerPoint로 변환</strong></a> | <a name="csharp-pdf-to-pptx"><strong>단계: Python에서 PDF를 PPTX로 변환</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 인스턴스를 생성합니다.
2. [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 클래스의 인스턴스를 생성합니다.
3. **Document** 객체의 **Save** 메서드를 사용하여 PDF를 PPTX로 저장합니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx.pptx"
    # PDF 문서 열기
    document = ap.Document(input_pdf)
    # PptxSaveOptions 인스턴스 생성
    save_option = ap.PptxSaveOptions()
    # 파일을 MS PowerPoint 형식으로 저장
    document.save(output_pdf, save_option)
```

## 슬라이드를 이미지로 하여 PDF를 PPTX로 변환


{{% alert color="success" %}}
**PDF를 PowerPoint로 온라인 변환 시도**

Aspose.PDF for Python은 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)라는 온라인 무료 애플리케이션을 제공하여 기능과 품질을 탐구할 수 있습니다.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

선택 가능한 텍스트 대신 이미지로 PDF를 PPTX로 변환해야 하는 경우, Aspose.PDF는 [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 클래스를 통해 이러한 기능을 제공합니다. 이를 위해, 아래의 코드 샘플에 보여진 것처럼 [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 클래스의 [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) 속성을 'true'로 설정하십시오.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_pptx_with_slides_as_images.pptx"
    # PDF 문서 열기
    document = ap.Document(input_pdf)
    # PptxSaveOptions 인스턴스 생성
    save_option = ap.PptxSaveOptions()
    save_option.slides_as_images = True
    # 파일을 MS PowerPoint 형식으로 저장
    document.save(output_pdf, save_option)
```


## 참고 

이 문서에서는 다음 주제도 다룹니다. 코드는 위와 동일합니다.

_형식_: **PowerPoint**
- [Python PDF를 PowerPoint 코드로](#python-pdf-to-powerpoint)
- [Python PDF를 PowerPoint API로](#python-pdf-to-powerpoint)
- [Python PDF를 PowerPoint로 프로그래밍 방식으로](#python-pdf-to-powerpoint)
- [Python PDF를 PowerPoint 라이브러리로](#python-pdf-to-powerpoint)
- [Python PDF를 PowerPoint로 저장](#python-pdf-to-powerpoint)
- [Python PDF에서 PowerPoint 생성](#python-pdf-to-powerpoint)
- [Python PDF에서 PowerPoint 생성](#python-pdf-to-powerpoint)
- [Python PDF를 PowerPoint 변환기](#python-pdf-to-powerpoint)

_형식_: **PPTX**
- [Python PDF를 PPTX 코드로](#python-pdf-to-pptx)
- [Python PDF를 PPTX API로](#python-pdf-to-pptx)
- [Python PDF를 PPTX로 프로그래밍 방식으로](#python-pdf-to-pptx)
- [Python PDF를 PPTX 라이브러리로](#python-pdf-to-pptx)
- [Python PDF를 PPTX로 저장](#python-pdf-to-pptx)
- [Python PDF에서 PPTX 생성](#python-pdf-to-pptx)
- [Python PDF에서 PPTX 생성](#python-pdf-to-pptx)
- [Python PDF를 PPTX 변환기](#python-pdf-to-pptx)