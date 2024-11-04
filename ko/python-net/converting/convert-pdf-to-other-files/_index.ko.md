---
title: PDF를 EPUB, LaTeX, 텍스트, XPS로 변환하기
linktitle: PDF를 다른 형식으로 변환하기
type: docs
weight: 90
url: /python-net/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: 변환, PDF, EPUB, LaText, 텍스트, XPS, Python
description: 이 주제는 Python을 사용하여 PDF 파일을 EPUB, LaTeX, 텍스트, XPS 등과 같은 다른 파일 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF를 EPUB로 변환하기

{{% alert color="success" %}}
**PDF를 EPUB로 온라인 변환 시도하기**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)를 제공합니다. 여기에서 기능과 작동 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>**은 국제 디지털 출판 포럼(IDPF)에서 제공하는 무료 및 오픈 전자책 표준입니다.
 파일의 확장자는 .epub입니다.  
EPUB는 리플로우 가능한 콘텐츠를 위해 설계되었으며, 이는 EPUB 리더가 특정 디스플레이 장치에 맞게 텍스트를 최적화할 수 있음을 의미합니다. EPUB는 고정 레이아웃 콘텐츠도 지원합니다. 이 형식은 출판사와 변환 업체가 내부적으로 사용할 수 있는 단일 형식으로 의도되었으며, 배포 및 판매를 위한 형식으로도 사용됩니다. 이는 Open eBook 표준을 대체합니다.

Aspose.PDF for Python은 또한 PDF 문서를 EPUB 형식으로 변환하는 기능을 지원합니다. Aspose.PDF for Python에는 'EpubSaveOptions'라는 클래스가 있으며, 이는 EPUB 파일을 생성하기 위해 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메소드의 두 번째 인수로 사용할 수 있습니다. 이 요구 사항을 Python으로 수행하기 위해 다음 코드 스니펫을 사용해 보십시오.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_epub.epub"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    # Epub 저장 옵션 인스턴스화
    save_options = ap.EpubSaveOptions()

    # 콘텐츠의 레이아웃 지정
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW

    # ePUB 문서 저장
    document.save(output_pdf, save_options)
```

## PDF를 LaTeX/TeX로 변환

**Aspose.PDF for Python via .NET**은 PDF를 LaTeX/TeX로 변환하는 것을 지원합니다. LaTeX 파일 형식은 특수 마크업이 있는 텍스트 파일 형식이며, 고품질 조판을 위한 TeX 기반 문서 준비 시스템에서 사용됩니다.

{{% alert color="success" %}}
**PDF를 LaTeX/TeX로 온라인에서 변환해보세요**

Aspose.PDF for Python은 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)라는 무료 온라인 애플리케이션을 제공하여 기능과 품질을 확인할 수 있습니다.

[![Aspose.PDF 변환 PDF를 LaTeX/TeX로 무료 앱과 함께](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

PDF 파일을 TeX로 변환하기 위해, Aspose.PDF는 변환 과정 동안 임시 이미지를 저장하기 위한 속성 OutDirectoryPath를 제공하는 [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) 클래스를 가지고 있습니다.

다음 코드 스니펫은 Python으로 PDF 파일을 TEX 형식으로 변환하는 과정을 보여줍니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tex.tex"
    # PDF 문서 열기
    document = ap.Document(input_pdf)
    # LaTeXSaveOptions 객체 인스턴스화
    saveOptions = ap.LaTeXSaveOptions()
    document.save(output_pdf, saveOptions)
```

## PDF를 텍스트로 변환

**Aspose.PDF for Python**은 전체 PDF 문서 및 단일 페이지를 텍스트 파일로 변환하는 것을 지원합니다.

### PDF 문서를 텍스트 파일로 변환

'TextDevice' 클래스를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다.

다음 코드 스니펫은 모든 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    # 텍스트 장치 생성
    textDevice = ap.devices.TextDevice()

    # 특정 페이지를 변환하고 저장
    textDevice.process(document.pages[1], output_pdf)
```


{{% alert color="success" %}}
 **PDF를 텍스트로 변환 시도하기**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)를 제공하여 기능과 품질을 조사할 수 있습니다.

[![Aspose.PDF 변환 PDF를 텍스트로 변환하는 무료 앱](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF를 XPS로 변환하기

**Aspose.PDF for Python**은 PDF 파일을 <abbr title="XML Paper Specification">XPS</abbr> 형식으로 변환할 수 있는 기능을 제공합니다. Python을 사용하여 PDF 파일을 XPS 형식으로 변환하는 코드 스니펫을 사용해 봅시다.

{{% alert color="success" %}}
**PDF를 XPS로 변환 시도하기**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)를 제공하여 기능과 품질을 조사할 수 있습니다.

[![Aspose.PDF 변환 PDF를 XPS로 변환하는 무료 앱](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 파일 형식은 주로 Microsoft Corporation의 XML Paper Specification과 관련이 있습니다. XML Paper Specification(XPS)은 이전에 Metro라는 코드명이 있었으며 Next Generation Print Path(NGPP) 마케팅 개념을 포함하고 있으며, Windows 운영 체제에 문서 생성 및 보기를 통합하려는 Microsoft의 이니셔티브입니다.

PDF 파일을 XPS로 변환하기 위해, Aspose.PDF는 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드의 두 번째 인수로 사용되는 클래스 [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/)를 제공합니다. 이를 통해 XPS 파일을 생성할 수 있습니다.

다음 코드 스니펫은 PDF 파일을 XPS 형식으로 변환하는 과정을 보여줍니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xps.xps"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    # XPS 저장 옵션 인스턴스화
    save_options = ap.XpsSaveOptions()

    # XPS 문서 저장
    document.save(output_pdf, save_options)
```

## PDF를 XML로 변환

{{% alert color="success" %}}
**PDF를 XML로 온라인으로 변환해보세요**

Aspose.PDF for Python은 온라인 무료 응용 프로그램 ["PDF to XML"](https://products.aspose.app/pdf/conversion/pdf-to-xml)을 제공하여 기능과 품질을 확인할 수 있습니다.

[![Aspose.PDF 변환 PDF를 XML로 무료 앱](pdf_to_xml.png)](https://products.aspose.app/pdf/conversion/pdf-to-xml)
{{% /alert %}}

<abbr title="Extensible Markup Language">XML</abbr>은 임의의 데이터를 저장, 전송 및 재구성하기 위한 마크업 언어 및 파일 형식입니다.

Aspose.PDF for Python은 PDF 문서를 XML 형식으로 변환하는 기능도 지원합니다. Aspose.PDF for Python에는 'XmlSaveOptions'라는 클래스가 있으며, 이는 XML 파일을 생성하기 위해 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드의 두 번째 인수로 사용할 수 있습니다. 이 요구 사항을 Python으로 수행하려면 다음 코드 스니펫을 사용해 보십시오.

```python

    import aspose.pdf as ap

    def convert_pdf_to_xml(self, infile, outfile):
        path_infile = self.dataDir + infile
        path_outfile = self.dataDir + outfile

        # PDF 문서 열기

        document = ap.Document(path_infile)

        # XML 저장 옵션 인스턴스화
        save_options = ap.XmlSaveOptions()

        # XML 문서 저장
        document.save(path_outfile, save_options)
        print(infile + "이(가) " + outfile + "(으)로 변환되었습니다")
```