---
title: Python을 사용하여 PDF 페이지 회전
linktitle: PDF 페이지 회전
type: docs
weight: 110
url: /ko/python-net/rotate-pages/
description: 이 주제에서는 Python을 사용하여 기존 PDF 파일의 페이지 방향을 프로그래밍 방식으로 회전하는 방법을 설명합니다.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF 페이지 회전하는 방법
Abstract: 이 문서에서는 Python을 사용하여 기존 PDF 파일의 페이지 방향을 프로그래밍 방식으로 업데이트하거나 변경하는 방법에 대한 가이드를 제공합니다. .NET을 통한 Aspose.PDF for Python을 활용하면, 페이지의 MediaBox 속성을 조정하여 가로 및 세로 방향을 쉽게 전환할 수 있습니다. 이 문서에는 PDF 문서의 페이지를 순회하고, MediaBox의 크기와 위치를 수정하며, 필요한 경우 CropBox를 조정하는 Python 코드 예제가 포함되어 있습니다. 또한, 원하는 방향을 얻기 위해 'rotate' 메서드를 사용하여 페이지의 회전 각도를 설정하는 방법을 설명합니다. 마지막으로 업데이트된 PDF 파일을 저장하는 과정으로 마무리됩니다.
---

이 주제에서는 Python을 사용하여 기존 PDF 파일의 페이지 방향을 프로그래밍 방식으로 회전하는 방법을 설명합니다.

## 페이지 방향 변경

이 함수는 Aspose.PDF for Python을 사용하여 PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)의 모든 페이지를 시계 방향으로 90도 회전합니다.
스캔한 문서가 가로로 표시되는 등 페이지 방향 문제를 수정하는 데 유용합니다. 원본 PDF는 변경되지 않으며, 회전된 버전은 새 파일로 저장됩니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_page(infile, outfile):
    """
    Rotate all pages in a PDF document by 90 degrees clockwise.

    Demonstrates how to rotate PDF pages using the Aspose.PDF library.
    This function applies a 90-degree clockwise rotation to every page
    in the input document and saves the result to a new file.

    Args:
        infile (str): Path to the input PDF file to rotate.
        outfile (str): Path where the rotated PDF will be saved.

    Returns:
        None: The function modifies the PDF pages and saves to the output path.

    Note:
        - Applies 90-degree clockwise rotation (ap.Rotation.ON90) to all pages
        - Rotates every page in the document uniformly
        - The original document is not modified; a new file is created
        - Rotation options include: ON90 (90°), ON180 (180°), ON270 (270°)
        - Useful for correcting page orientation or adjusting layout

    Example:
        >>> rotate_page("input.pdf", "rotated_output.pdf")
        # Rotates all pages 90 degrees clockwise and saves to rotated_output.pdf
    """
    document = ap.Document(infile)
    for page in document.pages:
        # `page` is a `Page` object; `rotate` uses the `Rotation` enum
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```


