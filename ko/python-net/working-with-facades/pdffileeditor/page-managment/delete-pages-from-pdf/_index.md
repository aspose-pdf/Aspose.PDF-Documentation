---
title: PDF에서 페이지 삭제
type: docs
weight: 20
url: /ko/python-net/delete-pages-from-pdf/
description: 파이썬용 Aspose.PDF 파일을 사용하여 PDF 문서에서 선택한 페이지를 제거합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 문서의 특정 페이지 삭제하기
Abstract: Python용 Aspose.PDF 파일을 사용하여 PDF 문서에서 선택한 페이지를 제거하는 방법을 알아봅니다.이 예제에서는 프로그래밍 방식으로 기존 PDF 파일에서 특정 페이지를 삭제하여 제거된 페이지 없이 새 문서를 만드는 방법을 보여줍니다.
---

때때로 PDF 문서에는 제거해야 하는 불필요하거나 민감한 페이지가 포함되어 있습니다.개발자는 Python용 Aspose.PDF 를 사용하여 파일을 수동으로 편집하지 않고도 프로그래밍 방식으로 PDF에서 특정 페이지를 삭제할 수 있습니다.

이 예제에서는 의 delete 메서드를 사용하는 방법을 보여줍니다. [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) PDF 문서에서 페이지를 제거하는 클래스입니다.삭제할 페이지 번호를 지정하여 원하지 않는 페이지를 제외한 새 PDF를 만들 수 있습니다.이 기능은 보고서를 정리하거나, 기밀 정보를 제거하거나, 사용자 정의 문서 추출을 준비하는 데 유용합니다.

1. PDF 파일 편집기 개체 만들기
1. 삭제할 페이지를 정의합니다.
1. 페이지를 삭제합니다.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir


    # Delete Pages from PDF
    def delete_pages_from_pdf(infile, outfile):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page numbers to be deleted (1-based index)
        pages_to_delete = [2, 4]

        # Delete the specified pages from the PDF document
        pdf_editor.delete(infile, pages_to_delete, outfile)
```