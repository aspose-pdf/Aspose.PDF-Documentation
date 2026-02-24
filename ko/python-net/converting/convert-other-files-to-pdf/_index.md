---
title: Python에서 다른 파일 형식을 PDF로 변환
linktitle: 다른 파일 형식을 PDF로 변환
type: docs
weight: 80
url: /ko/python-net/convert-other-files-to-pdf/
lastmod: "2025-09-01"
description: 이 주제에서는 Aspose.PDF를 사용하여 EPUB, MD, PCL, XPS, PS, XML 및 LaTeX와 같은 다른 파일 형식을 PDF 문서로 변환하는 방법을 보여줍니다.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python에서 다른 파일 형식을 PDF로 변환하는 방법
Abstract: 이 문서는 Python을 사용하여 다양한 파일 형식을 PDF로 변환하는 포괄적인 가이드를 제공하며, Aspose.PDF for Python via .NET의 기능을 활용합니다. 이 문서는 EPUB, Markdown, PCL, Text, XPS, PostScript, XML, XSL-FO 및 LaTeX/TeX를 포함한 여러 형식에 대한 변환 과정을 설명합니다. 각 섹션에서는 구체적인 코드 스니펫과 변환 구현 방법을 안내합니다. 이 글은 각 파일 유형에 맞춘 로드 옵션과 같은 Aspose.PDF 기능의 유용성을 강조하여 정확하고 효율적인 변환을 보장합니다. 또한 사용자가 직접 기능을 체험할 수 있도록 무료 온라인 변환 애플리케이션의 제공을 강조합니다. 이 가이드는 개발자가 Python 애플리케이션에 PDF 변환 기능을 통합하려는 경우 실용적인 리소스로 활용됩니다.
---

이 문서는 **Python을 사용하여 다양한 다른 파일 형식을 PDF로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

## OFD를 PDF로 변환

OFD는 Open Fixed-layout Document(오픈 고정 레이아웃 문서, Open Fixed Document 형식이라고도 함)의 약자입니다. 이는 PDF의 대안으로 도입된 중국 국가 표준(GB/T 33190-2016) 전자 문서입니다.

Python에서 OFD를 PDF로 변환하는 단계:

1. OfdLoadOptions()를 사용하여 OFD 로드 옵션을 설정합니다.
1. OFD 문서를 로드합니다.
1. PDF로 저장합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.OfdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## LaTeX/TeX를 PDF로 변환

LaTeX 파일 형식은 TeX 계열 언어의 LaTeX 파생 마크업이 포함된 텍스트 파일 형식이며, LaTeX는 TeX 시스템에서 파생된 형식입니다. LaTeX(ˈleɪtɛk/lay-tek 또는 lah-tek)는 문서 작성 시스템 및 문서 마크업 언어입니다. 이는 수학, 물리학, 컴퓨터 과학을 포함한 다양한 분야에서 과학 문서의 전달 및 출판에 널리 사용됩니다. 또한 한국어, 일본어, 한자, 아라비아어와 같은 복잡한 다국어 자료를 포함한 책과 논문의 준비 및 출판에 핵심적인 역할을 합니다.

LaTeX는 출력 형식을 지정하기 위해 TeX 조판 프로그램을 사용하며, 자체적으로 TeX 매크로 언어로 작성되었습니다.

{{% alert color="success" %}}
**온라인에서 LaTeX/TeX를 PDF로 변환해 보세요**

Aspose.PDF for Python via .NET은 온라인 무료 애플리케이션 ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)를 제공하며, 이를 통해 기능과 품질을 직접 확인해 볼 수 있습니다.

[![Aspose.PDF Convertion LaTeX/TeX to PDF with Free App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Python에서 TEX를 PDF로 변환하는 단계:

1. LatexLoadOptions()를 사용하여 LaTeX 로드 옵션을 설정합니다.
1. LaTeX 문서를 로드합니다.
1. PDF로 저장합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.LatexLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
## OFD를 PDF로 변환

OFD는 Open Fixed-layout Document(오픈 고정 레이아웃 문서, Open Fixed Document 형식이라고도 함)의 약자입니다. 이는 PDF의 대안으로 도입된 중국 국가 표준(GB/T 33190-2016) 전자 문서입니다.

Python에서 OFD를 PDF로 변환하는 단계:

1. OfdLoadOptions()를 사용하여 OFD 로드 옵션을 설정합니다.
1. OFD 문서를 로드합니다.
1. PDF로 저장합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.OfdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## LaTeX/TeX를 PDF로 변환

LaTeX 파일 형식은 TeX 계열 언어의 LaTeX 파생 마크업이 포함된 텍스트 파일 형식이며, LaTeX는 TeX 시스템에서 파생된 형식입니다. LaTeX(ˈleɪtɛk/lay-tek 또는 lah-tek)는 문서 작성 시스템 및 문서 마크업 언어입니다. 이는 수학, 물리학, 컴퓨터 과학을 포함한 다양한 분야에서 과학 문서의 전달 및 출판에 널리 사용됩니다. 또한 산스크리트어와 아라비아어와 같은 복잡한 다국어 자료를 포함한 책과 논문의 준비 및 출판에 중요한 역할을 합니다. LaTeX는 출력 형식을 지정하기 위해 TeX 조판 프로그램을 사용하며, 자체적으로 TeX 매크로 언어로 작성되었습니다.

{{% alert color="success" %}}
**온라인에서 LaTeX/TeX를 PDF로 변환해 보세요**

Aspose.PDF for Python via .NET은 온라인 무료 애플리케이션 ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)를 제공하며, 이를 통해 기능과 품질을 직접 확인해 볼 수 있습니다.

[![Aspose.PDF Convertion LaTeX/TeX to PDF with Free App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Python에서 TEX를 PDF로 변환하는 단계:

1. LatexLoadOptions()를 사용하여 LaTeX 로드 옵션을 설정합니다.
1. LaTeX 문서를 로드합니다.
1. PDF로 저장합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.LatexLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## EPUB을 PDF로 변환

**Aspose.PDF for Python via .NET** 은 EPUB 파일을 PDF 형식으로 간편하게 변환할 수 있게 합니다.

EPUB(전자 출판의 약자)는 국제 디지털 출판 포럼(IDPF)에서 제공하는 무료 및 오픈 전자책 표준입니다. 파일 확장자는 .epub입니다. EPUB는 재배열 가능한 컨텐츠를 위해 설계되었으며, 이는 EPUB 리더가 특정 디스플레이 장치에 맞게 텍스트를 최적화할 수 있음을 의미합니다.

<abbr title="전자 출판">EPUB</abbr> 또한 고정 레이아웃 컨텐츠를 지원합니다. 이 형식은 출판사와 변환 업체가 사내에서 사용할 수 있는 단일 포맷으로, 배포 및 판매에도 활용됩니다. Open eBook 표준을 대체합니다. EPUB 3 버전은 또한 도서 산업 연구 그룹(BISG)에서 권장하는 표준화된 모범 사례, 연구, 정보 및 이벤트, 컨텐츠 패키징을 위한 주요 도서 무역 협회입니다.

{{% alert color="success" %}}
**온라인에서 EPUB을 PDF로 변환해 보세요**

Aspose.PDF for Python via .NET 은 온라인 무료 애플리케이션 ["EPUB을 PDF로"](https://products.aspose.app/pdf/conversion/epub-to-pdf)을 제공하며, 기능과 품질을 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 EPUB을 PDF로 무료 앱](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

Python에서 EPUB을 PDF로 변환하는 단계:

1. EpubLoadOptions()를 사용하여 EPUB 문서를 로드합니다.
1. EPUB을 PDF로 변환합니다.
1. 확인 메시지를 출력합니다.

다음 코드 조각은 Python을 사용하여 EPUB 파일을 PDF 형식으로 변환하는 방법을 보여줍니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.EpubLoadOptions()
    document = ap.Document(path_infile, load_options)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Markdown을 PDF로 변환

**이 기능은 버전 19.6 이상에서 지원됩니다.**

{{% alert color="success" %}}
**온라인에서 Markdown을 PDF로 변환해 보세요**

Aspose.PDF for Python via .NET 은 온라인 무료 애플리케이션 ["Markdown을 PDF로"](https://products.aspose.app/pdf/conversion/md-to-pdf)을 제공하며, 기능과 품질을 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 Markdown을 PDF로 무료 앱](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Aspose.PDF for Python via .NET이 제공하는 이 코드 조각은 Markdown 파일을 PDF로 변환하는 데 도움을 주며, 문서 공유, 서식 보존 및 인쇄 호환성을 향상시킵니다.

다음 코드 조각은 Aspose.PDF 라이브러리를 사용하여 이 기능을 활용하는 방법을 보여줍니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.MdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## PCL을 PDF로 변환

<abbr title="프린터 명령어 언어">PCL</abbr> (Printer Command Language)는 표준 프린터 기능에 접근하기 위해 HP가 개발한 프린터 언어입니다. PCL 레벨 1부터 5e/5c까지는 명령 기반 언어로, 수신 순서대로 처리 및 해석되는 제어 시퀀스를 사용합니다. 소비자 수준에서는 프린터 드라이버가 PCL 데이터 스트림을 생성합니다. 또한 맞춤형 애플리케이션에서도 PCL 출력을 쉽게 생성할 수 있습니다.

{{% alert color="success" %}}
**온라인에서 PCL을 PDF로 변환해 보세요**

Aspose.PDF for .NET 은 온라인 무료 애플리케이션 ["PCL을 PDF로"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)을 제공하며, 기능과 품질을 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 PCL을 PDF로 무료 앱](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

PCL을 PDF로 변환하려면 Aspose.PDF의 클래스 [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions)를 사용하여 LoadOptions 객체를 초기화합니다. 이후 이 객체를 Document 객체 초기화 시 인수로 전달하여 PDF 렌더링 엔진이 소스 문서의 입력 포맷을 판단하도록 돕습니다.

다음 코드 조각은 PCL 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

Python에서 PCL을 PDF로 변환하는 단계:

1. PclLoadOptions()를 사용하여 PCL 로드 옵션을 설정합니다.
1. 문서를 로드합니다.
1. PDF로 저장합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## 서식이 지정된 텍스트를 PDF로 변환

**Aspose.PDF for Python via .NET** 은 일반 텍스트와 서식이 지정된 텍스트 파일을 PDF 형식으로 변환하는 기능을 지원합니다.

텍스트를 PDF로 변환한다는 것은 텍스트 조각을 PDF 페이지에 추가한다는 의미입니다. 텍스트 파일의 경우, 우리는 두 종류의 텍스트를 다룹니다: 고정 포맷(예: 줄당 80자, 25줄)과 비포맷(일반 텍스트)입니다. 필요에 따라 직접 추가를 제어하거나 라이브러리의 알고리즘에 맡길 수 있습니다.

{{% alert color="success" %}}
**온라인에서 텍스트를 PDF로 변환해 보세요**

Aspose.PDF for Python via .NET 은 온라인 무료 애플리케이션 ["텍스트를 PDF로"](https://products.aspose.app/pdf/conversion/txt-to-pdf)을 제공하며, 기능과 품질을 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 TEXT를 PDF로 무료 앱](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

Python에서 텍스트를 PDF로 변환하는 단계:

1. 입력 텍스트 파일을 한 줄씩 읽습니다.
1. 일관된 텍스트 정렬을 위해 고정폭 폰트(Courier New)를 설정합니다.
1. 새 PDF 문서를 생성하고 사용자 정의 여백 및 글꼴 설정으로 첫 페이지를 추가합니다.
1. 텍스트 파일의 각 줄을 반복합니다. 타자기 효과를 위해 'monospace_font' 글꼴을 크기 12로 사용합니다.
1. 페이지 생성을 최대 4페이지로 제한합니다.
1. 최종 PDF를 지정된 경로에 저장합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    with open(path_infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## PostScript를 PDF로 변환

이 예제는 Aspose.PDF for Python via .NET을 사용하여 PostScript 파일을 PDF 문서로 변환하는 방법을 보여줍니다.

1. PS 파일을 올바르게 해석하기 위해 'PsLoadOptions' 인스턴스를 생성합니다.
1. 로드 옵션을 사용하여 'PostScript' 파일을 Document 객체에 로드합니다.
1. 문서를 PDF 형식으로 원하는 출력 경로에 저장합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.PsLoadOptions()

    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## XPS를 PDF로 변환

**Aspose.PDF for Python via .NET** 은 <abbr title="XML Paper Specification">XPS</abbr> 파일을 PDF 형식으로 변환하는 기능을 지원합니다. 이 문서를 확인하여 작업을 해결하세요.

XPS 파일 형식은 주로 Microsoft Corporation의 XML Paper Specification과 연관됩니다. XML Paper Specification (XPS), 이전에는 Metro라는 코드명으로 불렸으며 Next Generation Print Path (NGPP) 마케팅 개념을 포괄하는, Microsoft가 Windows 운영 체제에 문서 생성 및 보기를 통합하려는 이니셔티브입니다.

다음 코드 스니펫은 Python을 사용하여 XPS 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.XpsLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 XPS 형식을 PDF로 변환해 보세요**

Aspose.PDF for Python via .NET은 온라인 무료 애플리케이션 ["XPS를 PDF로"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)을 제공하며, 여기서 기능과 품질을 확인해 볼 수 있습니다.

[![무료 앱으로 XPS를 PDF로 변환하는 Aspose.PDF](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## XSL-FO를 PDF로 변환

다음 코드 스니펫을 사용하여 Aspose.PDF for Python via .NET으로 XSLFO를 PDF 형식으로 변환할 수 있습니다:

```python

    from os import path
    import aspose.pdf as ap

    path_xsltfile = path.join(self.data_dir, xsltfile)
    path_xmlfile = path.join(self.data_dir, xmlfile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.XslFoLoadOptions(path_xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately
    )
    document = ap.Document(path_xmlfile, load_options)
    document.save(path_outfile)

    print(xmlfile + " converted into " + outfile)
```

## XSLT를 사용한 XML을 PDF로 변환

이 예제는 XSLT 템플릿을 사용하여 XML 파일을 HTML로 변환한 다음, 해당 HTML을 Aspose.PDF에 로드하여 PDF로 변환하는 방법을 보여줍니다.

1. HTML-to-PDF 변환을 구성하기 위해 'HtmlLoadOptions' 인스턴스를 생성합니다.
1. 변환된 HTML 파일을 Aspose.PDF Document 객체에 로드합니다.
1. 지정된 출력 경로에 문서를 PDF로 저장합니다.
1. 변환이 성공적으로 완료된 후 임시 HTML 파일을 제거합니다.

```python

    from os import path
    import aspose.pdf as ap

    def transform_xml_to_html(xml_file, xslt_file, html_file):
        from lxml import etree
        """
        Transform XML to HTML using XSLT and return as a stream
        """
        # Parse XML document
        xml_doc = etree.parse(xml_file)

        # Parse XSLT stylesheet
        xslt_doc = etree.parse(xslt_file)
        transform = etree.XSLT(xslt_doc)

        # Apply transformation
        result = transform(xml_doc)

        # Save result to HTML file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(str(result))


    def convert_XML_to_PDF(template, infile, outfile):
        path_infile = path.join(data_dir, infile)
        path_outfile = path.join(data_dir, "python", outfile)
        path_template = path.join(data_dir, template)
        path_temp_file = path.join(data_dir, "temp.html")

        load_options = ap.HtmlLoadOptions()
        transform_xml_to_html(path_infile, path_template, path_temp_file)

        document = ap.Document(path_temp_file, load_options)
        document.save(path_outfile)

        if path.exists(path_temp_file):
            os.remove(path_temp_file)

        print(infile + " converted into " + outfile)
```

