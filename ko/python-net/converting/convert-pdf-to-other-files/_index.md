---
title: Python에서 PDF를 EPUB, LaTeX, Text, XPS로 변환
linktitle: PDF를 다른 형식으로 변환
type: docs
weight: 90
url: /ko/python-net/convert-pdf-to-other-files/
lastmod: "2025-09-27"
description: 이 주제에서는 Python을 사용하여 PDF 파일을 EPUB, LaTeX, Text, XPS 등과 같은 다른 파일 형식으로 변환하는 방법을 보여줍니다.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Python에서 PDF를 다른 형식으로 변환하는 방법
Abstract: 이 문서는 Aspose.PDF for Python을 사용하여 PDF 파일을 다양한 형식으로 변환하는 포괄적인 가이드를 제공합니다. 여기에서는 PDF를 EPUB, LaTeX/TeX, Text, XPS 및 XML 형식으로 변환하는 방법을 다룹니다. 각 섹션은 Aspose가 제공하는 온라인 무료 애플리케이션을 사용해 해당 형식으로 PDF를 변환해 보라는 초대로 시작되며, 이러한 도구의 사용 편의성과 품질을 강조합니다.
---

## PDF를 EPUB로 변환

{{% alert color="success" %}}
**온라인에서 PDF를 EPUB로 변환해 보세요**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF를 EPUB로"](https://products.aspose.app/pdf/conversion/pdf-to-epub)를 제공하며, 이를 통해 기능 및 품질을 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 EPUB로 무료 앱](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr>은 국제 디지털 출판 포럼(IDPF)에서 만든 무료 개방 전자책 표준입니다. 파일 확장자는 .epub입니다.
EPUB은 재흐름 가능한 콘텐츠를 위해 설계되어, EPUB 리더가 특정 디스플레이 장치에 맞게 텍스트를 최적화할 수 있습니다. EPUB은 고정 레이아웃 콘텐츠도 지원합니다. 이 형식은 출판사와 변환 업체가 내부에서뿐만 아니라 배포 및 판매를 위해 사용할 수 있는 단일 형식으로 의도되었습니다. 이는 Open eBook 표준을 대체합니다.

Aspose.PDF for Python은 PDF 문서를 EPUB 형식으로 변환하는 기능도 지원합니다. Aspose.PDF for Python에는 'EpubSaveOptions'라는 클래스가 있으며, 이는 [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드의 두 번째 인수로 사용되어 EPUB 파일을 생성할 수 있습니다.
Python으로 이 요구사항을 수행하려면 아래 코드 스니펫을 사용해 보세요.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = (
        ap.EpubSaveOptions.RecognitionMode.FLOW
    )
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF를 LaTeX/TeX로 변환

**Aspose.PDF for Python via .NET** PDF를 LaTeX/TeX로 변환하는 것을 지원합니다.
LaTeX 파일 형식은 특수 마크업이 포함된 텍스트 파일 형식이며, 고품질 조판을 위해 TeX 기반 문서 작성 시스템에서 사용됩니다.

{{% alert color="success" %}}
**온라인에서 PDF를 LaTeX/TeX로 변환해 보세요**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF를 LaTeX로"](https://products.aspose.app/pdf/conversion/pdf-to-tex)를 제공하며, 이를 통해 기능 및 품질을 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 LaTeX/TeX로 무료 앱](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

PDF 파일을 TeX로 변환하려면 Aspose.PDF의 [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) 클래스를 사용하며, 이 클래스는 변환 과정 중 임시 이미지를 저장하기 위한 OutDirectoryPath 속성을 제공합니다.

다음 코드 스니펫은 Python을 사용하여 PDF 파일을 TEX 형식으로 변환하는 과정을 보여줍니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.LaTeXSaveOptions()

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## PDF를 Text로 변환

**Aspose.PDF for Python**은 전체 PDF 문서 및 단일 페이지를 Text 파일로 변환하는 것을 지원합니다. 'TextDevice' 클래스를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다. 다음 코드 스니펫은 모든 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 PDF를 Text로 변환해 보세요**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF를 Text로"](https://products.aspose.app/pdf/conversion/pdf-to-txt)를 제공하며, 이를 통해 기능 및 품질을 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 Text로 무료 앱](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF를 XPS로 변환

**Aspose.PDF for Python**은 PDF 파일을 XPS 형식으로 변환할 수 있는 기능을 제공합니다. Python을 사용하여 PDF 파일을 XPS 형식으로 변환하려면 아래 코드 스니펫을 사용해 보세요.

{{% alert color="success" %}}
**온라인에서 PDF를 XPS로 변환해 보세요**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF를 XPS로"](https://products.aspose.app/pdf/conversion/pdf-to-xps)를 제공하며, 이를 통해 기능 및 품질을 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 XPS로 무료 앱](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 파일 형식은 주로 Microsoft Corporation의 XML Paper Specification과 관련됩니다. XML Paper Specification (XPS)은 이전에 Metro라는 코드명으로 불렸으며 Next Generation Print Path(NGPP) 마케팅 개념을 포함한 것으로, Windows 운영 체제에 문서 작성 및 보기 기능을 통합하려는 Microsoft의 이니셔티브입니다.

PDF 파일을 XPS로 변환하려면 Aspose.PDF의 [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) 클래스를 사용하며, 이 클래스는 [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드의 두 번째 인수로 사용되어 XPS 파일을 생성합니다.

다음 코드 스니펫은 PDF 파일을 XPS 형식으로 변환하는 과정을 보여줍니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF를 MD로 변환

Aspose.PDF에는 PDF 문서를 이미지와 리소스를 보존하면서 Markdown(MD) 형식으로 변환하는 'MarkdownSaveOptions()' 클래스가 있습니다.

1. 'ap.Document'를 사용하여 원본 PDF를 로드합니다.
1. 'MarkdownSaveOptions'의 인스턴스를 생성합니다.
1. 'resources_directory_name'을 'images'로 설정합니다 – 추출된 이미지는 이 폴더에 저장됩니다.
1. 구성한 옵션을 사용하여 변환된 Markdown 문서를 저장합니다.
1. 변환 후 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.MarkdownSaveOptions()
    # save_options.extract_vector_graphics = True
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

지정된 이미지 폴더에 텍스트와 연결된 이미지가 저장된 Markdown 파일입니다.

## PDF를 MobiXML로 변환

이 메서드는 PDF 문서를 Kindle 기기용 전자책에 일반적으로 사용되는 MOBI(MobiXML) 형식으로 변환합니다.

1. 'ap.Document'를 사용하여 원본 PDF 문서를 로드합니다.
1. 문서를 형식 'ap.SaveFormat.MOBI_XML'으로 저장합니다.
1. 변환이 완료되면 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.save(path_outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
