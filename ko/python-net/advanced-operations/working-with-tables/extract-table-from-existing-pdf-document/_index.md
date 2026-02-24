---
title: PDF 문서에서 테이블 추출
linktitle: 테이블 추출
type: docs
weight: 20
url: /ko/python-net/extracting-table/
description: Aspose.PDF for Python via .NET는 PDF 문서에 포함된 테이블을 다양한 방식으로 조작할 수 있게 해줍니다.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 테이블을 추출하는 방법
Abstract: 이 문서에서는 Python을 사용하여 PDF 문서에서 테이블을 추출하는 과정에 대해 설명하며, 특히 Aspose.PDF for Python via .NET 라이브러리를 활용합니다. PDF 문서를 로드하고 페이지를 순회하며 `TableAbsorber` 클래스를 사용해 테이블 데이터를 식별하고 추출하는 코드 예제가 제공됩니다. 코드는 각 테이블, 행, 셀을 순회하면서 텍스트 조각을 수집하고 추출된 텍스트를 출력합니다. 이 방법은 PDF 내 표 형식 데이터에 대한 데이터 추출 및 분석 작업을 위한 강력한 도구로 강조됩니다.
---

## PDF에서 테이블 추출

Python을 사용하여 PDF에서 테이블을 추출하는 것은 데이터 추출 및 분석에 매우 유용할 수 있습니다. Aspose.PDF for Python via .NET 라이브러리를 사용하면 PDF 문서에 포함된 테이블을 다양한 데이터 관련 작업에 효율적으로 활용할 수 있습니다.

이 코드 조각은 기존 PDF 파일을 열고 각 페이지에서 테이블을 스캔하여 셀 텍스트 내용을 추출합니다. 'TableAbsorber'를 사용해 테이블을 감지한 후 행과 셀을 순회하면서 내부 텍스트를 출력합니다.

1. PDF를 ap.Document 객체에 로드합니다.
1. 페이지를 순회합니다.
1. TableAbsorber 객체를 생성합니다.
1. 테이블을 순회합니다.
1. 행과 셀을 순회합니다.
1. 셀에서 텍스트를 추출하고 출력합니다.

이 예제는 PDF를 읽고 모든 테이블을 찾아 행별로 셀 내용을 출력합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    document = ap.Document(path_infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row")
                for cell in row.cell_list:
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        txt = ""
                        for seg in fragment.segments:
                            txt += seg.text
                        print(txt)
```


