---
title: Python에서 PDF를 PowerPoint로 변환
linktitle: PDF를 PowerPoint로 변환
type: docs
weight: 30
url: /ko/python-net/convert-pdf-to-powerpoint/
description: Aspose.PDF for Python via .NET를 사용하여 PDF를 PowerPoint 프레젠테이션으로 쉽게 변환하는 방법을 배우세요. 원활한 PDF에서 PPTX 변환을 위한 단계별 가이드.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF를 PowerPoint로 변환하는 방법
Abstract: 이 기사에서는 PDF 파일을 Python을 사용하여 PowerPoint 프레젠테이션(PPTX 형식)으로 변환하는 포괄적인 가이드를 제공합니다. .NET을 통한 Aspose.PDF for Python을 사용하여 PDF 페이지를 PPTX 파일의 개별 슬라이드로 변환하는 방법을 소개합니다. 변환에 필요한 단계, Document 및 PptxSaveOptions 클래스의 인스턴스를 생성하고 Save 메서드를 활용하는 방법을 설명합니다. 또한 PptxSaveOptions의 특정 속성을 설정하여 슬라이드를 이미지로 변환하는 기능도 강조합니다. 변환 과정을 보여주는 코드 스니펫이 제공됩니다. 또한 PDF에서 PPTX 변환 기능을 테스트할 수 있는 온라인 애플리케이션을 언급하여 사용자가 직접 체험할 수 있도록 합니다. 더불어 이와 관련된 다양한 주제와 기능을 나열하여 Python을 이용한 PDF에서 PowerPoint 변환의 다재다능함과 프로그래밍 방식 접근을 강조합니다.
---

## Python PDF를 PowerPoint 및 PPTX로 변환

**Aspose.PDF for Python via .NET**는 PDF를 PPTX로 변환하는 진행 상황을 추적할 수 있게 합니다.

우리는 PPT/PPTX 프레젠테이션을 생성하고 조작할 수 있는 기능을 제공하는 Aspose.Slides라는 API를 보유하고 있습니다. 이 API는 또한 <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> 파일을 PDF 형식으로 변환하는 기능을 제공합니다. 변환 과정에서 PDF 파일의 개별 페이지가 PPTX 파일의 별도 슬라이드로 변환됩니다.

PDF를 PPTX로 변환하는 동안 텍스트는 선택/수정이 가능한 텍스트로 렌더링됩니다. PDF 파일을 PPTX 형식으로 변환하려면 Aspose.PDF에서 제공하는 [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 클래스를 사용해야 함을 알려드립니다. PptxSaveOptions 클래스의 객체는 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드의 두 번째 인수로 전달됩니다. 다음 코드 스니펫은 PDF 파일을 PPTX 형식으로 변환하는 과정을 보여줍니다.

## Python 및 Aspose.PDF for Python via .NET를 사용한 간단한 PDF에서 PowerPoint 변환

PDF를 PPTX로 변환하기 위해 Aspose.PDF for Python은 다음 코드 단계들을 사용할 것을 권장합니다.

단계: Python에서 PDF를 PowerPoint로 변환

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 인스턴스를 생성합니다.
1. [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 클래스의 인스턴스를 생성합니다.
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.PptxSaveOptions()
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 슬라이드를 이미지로 하여 PDF를 PPTX로 변환

{{% alert color="success" %}}
**온라인에서 PDF를 PowerPoint로 변환해 보세요**

Aspose.PDF는 온라인 무료 애플리케이션 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)을 제공하며, 이를 통해 기능과 품질을 직접 확인해 볼 수 있습니다.


[![Aspose.PDF 변환 PDF to PPTX 무료 앱](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

검색 가능한 PDF를 선택 가능한 텍스트가 아니라 이미지 형태의 PPTX로 변환해야 하는 경우, Aspose.PDF는 [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 클래스를 통해 해당 기능을 제공합니다. 이를 구현하려면 아래 코드 예시와 같이 [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 클래스의 [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) 속성을 'true'로 설정하십시오.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 사용자 지정 이미지 해상도로 PDF를 PPTX로 변환

이 방법은 PDF 문서를 PowerPoint(PPTX) 파일로 변환하면서 향상된 품질을 위해 사용자 지정 이미지 해상도(300 DPI)를 설정합니다.

1. PDF를 'ap.Document' 객체에 로드합니다.
1. 'PptxSaveOptions' 인스턴스를 생성합니다.
1. 고품질 렌더링을 위해 'image_resolution' 속성을 300 DPI로 설정합니다.
1. 정의된 저장 옵션을 사용하여 PDF를 PPTX 파일로 저장합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

