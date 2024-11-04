---
title: PDF를 EPUB, LaTeX, 텍스트, XPS로 변환하기
linktitle: PDF를 다른 형식으로 변환하기
type: docs
weight: 90
url: /python-java/convert-pdf-to-other-files/
lastmod: "2023-04-06"
keywords: 변환, PDF, EPUB, LaText, 텍스트, XPS, Python
description: 이 주제는 Python을 사용하여 PDF 파일을 EPUB, LaTeX, 텍스트, XPS 등과 같은 다른 파일 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF를 EPUB로 변환하기

{{% alert color="success" %}}
**PDF를 EPUB로 온라인 변환 시도하기**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)을 제공합니다. 여기에서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>**은 국제 디지털 출판 포럼(IDPF)의 무료 오픈 전자책 표준입니다.
 파일의 확장자는 .epub입니다.  
EPUB은 리플로우 가능한 콘텐츠를 위해 설계되었으며, 이는 EPUB 리더가 특정 디스플레이 장치에 맞춰 텍스트를 최적화할 수 있음을 의미합니다. EPUB은 고정 레이아웃 콘텐츠도 지원합니다. 이 형식은 출판사와 변환 하우스가 내부적으로 사용할 수 있을 뿐 아니라 배포 및 판매를 위한 단일 형식으로 의도되었습니다. 이는 Open eBook 표준을 대체합니다.

Aspose.PDF for Python은 PDF 문서를 EPUB 형식으로 변환하는 기능도 지원합니다. Aspose.PDF for Python에는 'EpubSaveOptions'라는 클래스가 있으며, 이는 EPUB 파일을 생성하기 위해 [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 메서드의 두 번째 인수로 사용할 수 있습니다. 이 요구 사항을 Python으로 충족하기 위해 다음 코드 스니펫을 사용해 보세요.

```python
from asposepdf import Api

# 라이선스 초기화
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# Epub으로 변환
documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.epub"
doc.save(documentOutName, Api.SaveFormat.Epub)
```

## PDF를 LaTeX/TeX로 변환

**Aspose.PDF for Python via Java**는 PDF를 LaTeX/TeX로 변환하는 기능을 지원합니다. LaTeX 파일 형식은 특수 마크업이 있는 텍스트 파일 형식으로, 고품질 조판을 위한 TeX 기반 문서 준비 시스템에서 사용됩니다.

{{% alert color="success" %}}
**PDF를 LaTeX/TeX로 온라인에서 변환해보세요**

Aspose.PDF for Python은 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)라는 무료 온라인 애플리케이션을 제공하여, 기능과 품질을 탐색해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF에서 LaTeX/TeX로 무료 앱 사용](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

PDF 파일을 TeX로 변환하기 위해, Aspose.PDF는 변환 과정에서 임시 이미지를 저장하기 위한 OutDirectoryPath 속성을 제공하는 [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/latexsaveoptions/) 클래스를 가지고 있습니다.

다음 코드 스니펫은 Python으로 PDF 파일을 TEX 형식으로 변환하는 과정을 보여줍니다.

```python
from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.tex"
doc.save(documentOutName, Api.SaveFormat.TeX)
```

## PDF를 텍스트로 변환

**Aspose.PDF for Python**은 전체 PDF 문서와 단일 페이지를 텍스트 파일로 변환하는 것을 지원합니다.

### PDF 문서를 텍스트 파일로 변환

'TextDevice' 클래스를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다.

다음 코드 스니펫은 모든 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```python
from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_text"
# PDF 문서 열기
document = Api.Document(input_pdf)

device = Device.TextDevice()

for i in range(0, document.getPages.size):
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.txt"
    # 특정 페이지를 변환하고 텍스트 파일로 저장
    device.process(document.getPages.getPage(i + 1), imageFileName)
```

{{% alert color="success" %}}
**온라인에서 PDF를 텍스트로 변환 시도**

Aspose.PDF for Python은 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 품질을 확인할 수 있습니다.

[![Aspose.PDF 무료 앱으로 PDF를 텍스트로 변환](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF를 XPS로 변환

**Aspose.PDF for Python**은 PDF 파일을 <abbr title="XML Paper Specification">XPS</abbr> 형식으로 변환할 수 있는 기능을 제공합니다. Python을 사용하여 PDF 파일을 XPS 형식으로 변환하는 예제 코드를 사용해 보세요.

{{% alert color="success" %}}
**온라인에서 PDF를 XPS로 변환 시도**

Aspose.PDF for Python은 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 품질을 확인할 수 있습니다.

[![Aspose.PDF 무료 앱으로 PDF를 XPS로 변환](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 파일 형식은 주로 Microsoft Corporation의 XML Paper Specification과 관련이 있습니다. XML Paper Specification(XPS)은 이전에 Metro라는 코드명이 붙었으며 차세대 인쇄 경로(NGPP) 마케팅 개념을 포괄하며, 문서 생성 및 보기 기능을 Windows 운영 체제에 통합하려는 Microsoft의 이니셔티브입니다.

PDF 파일을 XPS로 변환하려면, Aspose.PDF에는 [XpsSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/xpssaveoptions/)이라는 클래스가 있으며, 이는 XPS 파일을 생성하기 위해 [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 메서드의 두 번째 인수로 사용됩니다.

다음 코드는 PDF 파일을 XPS 형식으로 변환하는 과정을 보여줍니다.

```python

from asposepdf import Api

documentName = "../../testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "../../testout/out.xps"
doc.save(documentOutName, Api.SaveFormat.Xps)

```