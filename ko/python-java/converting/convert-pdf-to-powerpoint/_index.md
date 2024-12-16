---
title: PDF를 파워포인트로 변환하기 파이썬에서
linktitle: PDF를 파워포인트로 변환
type: docs
weight: 30
url: /ko/python-java/convert-pdf-to-powerpoint/
description: Aspose.PDF를 사용하여 PDF를 파이썬에서 PPT (파워포인트) 형식으로 변환할 수 있습니다. PDF를 PPTX로 슬라이드를 이미지로 변환할 수 있는 방법이 있습니다.
lastmod: "2023-04-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 개요

PDF 파일을 파워포인트로 변환할 수 있을까요? 네, 가능합니다! 그리고 그것은 쉽습니다!
이 기사는 **파이썬을 사용하여 PDF를 파워포인트로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

_형식_: **PPTX**
- [파이썬 PDF를 PPTX로](#python-pdf-to-pptx)
- [파이썬 PDF를 PPTX로 변환](#python-pdf-to-pptx)
- [파이썬 PDF 파일을 PPTX로 변환하는 방법](#python-pdf-to-pptx)

_형식_: **파워포인트**
- [파이썬 PDF를 파워포인트로](#python-pdf-to-powerpoint)
- [파이썬 PDF를 파워포인트로 변환](#python-pdf-to-powerpoint)
- [파이썬 PDF 파일을 파워포인트로 변환하는 방법](#python-pdf-to-powerpoint)


## 파이썬 PDF를 파워포인트와 PPTX로 변환하기

**Aspose.PDF for Python via Java**는 PDF를 PPTX로 변환하는 진행 상황을 추적할 수 있게 해줍니다.

우리는 Aspose.Slides라는 API를 가지고 있으며, PPT/PPTX 프레젠테이션을 생성하고 조작하는 기능을 제공합니다. 이 API는 또한 PPT/PPTX 파일을 PDF 형식으로 변환하는 기능도 제공합니다. 이 변환 과정에서 PDF 파일의 개별 페이지는 PPTX 파일의 개별 슬라이드로 변환됩니다.

PDF에서 <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>로 변환하는 동안, 텍스트는 선택/업데이트할 수 있는 텍스트로 렌더링됩니다. PDF 파일을 PPTX 형식으로 변환하기 위해, Aspose.PDF는 [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions)라는 클래스를 제공합니다. PptxSaveOptions 클래스의 객체는 [`Document.Save(..) method`](https://reference.aspose.com/pdf/java/aspose.pdf/document/methods/save)의 두 번째 인수로 전달됩니다. 다음 코드 스니펫은 PDF 파일을 PPTX 형식으로 변환하는 프로세스를 보여줍니다.

## Python 및 Aspose.PDF for Python을 사용한 PDF에서 PowerPoint로의 간단한 변환

PDF를 PPTX로 변환하려면, Aspose.PDF for Python은 다음 코드 단계를 사용할 것을 권장합니다.

<a name="csharp-pdf-to-powerpoint"><strong>단계: Python에서 PDF를 PowerPoint로 변환</strong></a> | <a name="csharp-pdf-to-pptx"><strong>단계: Python에서 PDF를 PPTX로 변환</strong></a>

1. [Document](https://reference.aspose.com/pdf/java/aspose.pdf/document) 클래스의 인스턴스를 생성합니다.
2. [PptxSaveOptions](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions) 클래스의 인스턴스를 생성합니다.
3. PDF를 PPTX로 저장하기 위해 **Document** 객체의 **Save** 메소드를 사용합니다.

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# PDF 문서 열기
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SeparateImages = True
save_options._OptimizeTextBoxes = True

# 파일을 MS Word 문서 형식으로 저장
document.save(output_pdf, save_options)
```


## PDF를 이미지 슬라이드로 PPTX로 변환하기

{{% alert color="success" %}}
**PDF를 PowerPoint로 온라인에서 변환해보세요**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)를 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

만약 선택 가능한 텍스트 대신 이미지로 검색 가능한 PDF를 PPTX로 변환해야 하는 경우, Aspose.PDF는 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/) 클래스를 통해 이러한 기능을 제공합니다. 이를 위해, 다음 코드 샘플에서 보이는 것처럼 [PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/) 클래스의 속성 [SlidesAsImages](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/#properties)를 'true'로 설정합니다.

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# PDF 문서 열기
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SlidesAsImages = True

# 파일을 MS Word 문서 형식으로 저장
document.save(output_pdf, save_options)
```


## 관련 항목

이 문서는 다음 주제도 다룹니다. 코드는 위와 동일합니다.

_형식_: **PowerPoint**
- [Python PDF to PowerPoint Code](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint API](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint Programmatically](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint Library](#python-pdf-to-powerpoint)
- [Python Save PDF as PowerPoint](#python-pdf-to-powerpoint)
- [Python Generate PowerPoint from PDF](#python-pdf-to-powerpoint)
- [Python Create PowerPoint from PDF](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint Converter](#python-pdf-to-powerpoint)

_형식_: **PPTX**
- [Python PDF to PPTX Code](#python-pdf-to-pptx)
- [Python PDF to PPTX API](#python-pdf-to-pptx)
- [Python PDF to PPTX Programmatically](#python-pdf-to-pptx)
- [Python PDF to PPTX Library](#python-pdf-to-pptx)
- [Python Save PDF as PPTX](#python-pdf-to-pptx)
- [Python Generate PPTX from PDF](#python-pdf-to-pptx)
- [Python Create PPTX from PDF](#python-pdf-to-pptx)

- [Python PDF to PPTX Converter](#python-pdf-to-pptx)