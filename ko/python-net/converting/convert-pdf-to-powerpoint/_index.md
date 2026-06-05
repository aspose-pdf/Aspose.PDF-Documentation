---
title: Python에서 PDF를 PowerPoint로 변환
linktitle: PDF를 PowerPoint로 변환
type: docs
weight: 30
url: /ko/python-net/convert-pdf-to-powerpoint/
description: Python에서 PDF를 PowerPoint로 변환하는 방법을 배우세요. 여기에는 PDF를 PPTX로 변환하고, 슬라이드를 이미지로 저장하며, Aspose.PDF를 사용한 사용자 지정 이미지 해상도가 포함됩니다.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF를 PPTX PowerPoint 슬라이드로 변환
Abstract: 이 문서는 Aspose.PDF for Python via .NET을 사용하여 PDF 파일을 PowerPoint 프레젠테이션으로 변환하는 방법을 보여줍니다. PDF를 PPTX로 변환하고, 슬라이드를 이미지로 변환하며, 프레젠테이션 출력에 대한 이미지 해상도를 설정하는 내용을 다룹니다.
---

## Python에서 PDF를 PowerPoint로 변환

**Aspose.PDF for Python via .NET**은 Python 코드에서 PDF 파일을 PowerPoint PPTX 프레젠테이션으로 변환할 수 있게 해줍니다.

PDF 보고서, 슬라이드 데크, 브로셔 또는 유인물을 PowerPoint 파일로 재활용해야 할 때 이 워크플로를 사용하십시오. 변환 중에 각 PDF 페이지가 PPTX 파일의 개별 슬라이드로 변환됩니다.

PDF를 PPTX로 변환하는 동안 텍스트는 선택 가능한 텍스트로 렌더링되어 PowerPoint에서 업데이트할 수 있습니다. PDF 파일을 PPTX 형식으로 변환하려면 Aspose.PDF가 제공합니다. [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 클래스. a를 전달하십시오 `PptxSaveOptions` 두 번째 인수로 객체를 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드.

## Python에서 PDF를 PPTX로 변환

PDF를 PPTX로 변환하려면 다음 코드 단계를 사용하십시오.

단계: Python에서 PDF를 PowerPoint로 변환

1. 인스턴스를 생성합니다 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스.
1. 인스턴스를 생성합니다 [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 클래스.
1. 호출 [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)
```

## PDF를 슬라이드 이미지로 PPTX 변환

{{% alert color="success" %}}
**PDF를 PowerPoint로 온라인 변환해 보세요**

Aspose.PDF는 온라인을 제공합니다 ["PDF를 PPTX로"](https://products.aspose.app/pdf/conversion/pdf-to-pptx) 변환 품질을 테스트할 수 있는 애플리케이션.


[![Aspose.PDF 변환 PDF to PPTX with App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

검색 가능한 PDF를 선택 가능한 텍스트가 아니라 이미지로 PPTX 변환해야 할 경우, Aspose.PDF는 해당 기능을 via 제공한다. [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 클래스. 이를 달성하려면, 속성을 설정합니다 [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) 의 [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 다음 코드 샘플에 표시된 대로 클래스를 'true'로 설정합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_slides_as_images(infile, outfile):

    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(outfile, save_options)
```

## 맞춤 이미지 해상도로 PDF를 PPTX로 변환

이 메서드는 PDF 문서를 PowerPoint (PPTX) 파일로 변환하면서 향상된 품질을 위해 사용자 지정 이미지 해상도(300 DPI)를 설정합니다.

1. PDF를 'ap.Document' 객체에 로드합니다.
1. 'PptxSaveOptions' 인스턴스를 생성합니다.
1. 'image_resolution' 속성을 300 DPI로 설정하여 고품질 렌더링을 수행합니다.
1. 정의된 저장 옵션을 사용하여 PDF를 PPTX 파일로 저장합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_image_resolution(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(outfile, save_options)
```

## 관련 변환

- [PDF를 Word로 변환](/pdf/ko/python-net/convert-pdf-to-word/) 슬라이드 대신 편집 가능한 문서 출력용.
- [PDF를 Excel로 변환](/pdf/ko/python-net/convert-pdf-to-excel/) 원본 PDF에 표가 많은 비즈니스 데이터가 포함된 경우.
- [PDF를 HTML로 변환](/pdf/ko/python-net/convert-pdf-to-html/) 브라우저 준비가 된 퍼블리싱 워크플로를 위해.
