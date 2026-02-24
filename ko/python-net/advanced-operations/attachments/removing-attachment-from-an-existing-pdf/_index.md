---
title: Python을 사용하여 PDF에서 첨부 파일 제거
linktitle: 기존 PDF에서 첨부 파일 제거
type: docs
weight: 30
url: /ko/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF는 PDF 문서에서 첨부 파일을 제거할 수 있습니다. Aspose.PDF for Python via .NET 라이브러리를 사용하여 Python PDF API로 PDF 파일의 첨부 파일을 제거하십시오.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 첨부 파일 삭제하는 방법
Abstract: 이 문서는 Aspose.PDF for Python을 사용하여 PDF 파일에서 첨부 파일을 제거하는 방법을 설명합니다. PDF 문서의 첨부 파일은 `Document` 객체의 `EmbeddedFiles` 컬렉션에 저장됩니다. PDF에서 모든 첨부 파일을 삭제하려면 `EmbeddedFiles` 컬렉션의 `delete()` 메서드를 호출한 다음 `Document` 객체의 `save()` 메서드를 사용하여 업데이트된 문서를 저장하면 됩니다. 이 과정을 보여주는 코드 스니펫이 제공되어, 문서를 열고, 첨부 파일을 삭제하며, 수정된 파일을 저장하는 단계가 시연됩니다.
---

Aspose.PDF for Python은 PDF 파일에서 첨부 파일을 제거할 수 있습니다. PDF 문서의 첨부 파일은 Document 객체의 [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 컬렉션에 저장됩니다.

PDF 파일과 연관된 모든 첨부 파일을 삭제하려면:

1. [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 컬렉션의 [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) 메서드를 호출합니다.
1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 업데이트된 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에서 첨부 파일을 제거하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all attachments
    document.embedded_files.delete()

    # Save updated file
    document.save(output_pdf)
```


