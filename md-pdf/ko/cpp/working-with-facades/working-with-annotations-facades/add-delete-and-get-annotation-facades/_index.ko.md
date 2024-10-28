---
title: 기존 PDF 파일에 주석 추가, 삭제 및 가져오기 - Facades
type: docs
weight: 10
url: /cpp/add-delete-and-get-annotation-facades/
---

## <ins>**PdfContentEditor를 사용하여 기존 PDF 파일에 주석 추가**
**PdfContentEditor**를 사용하면 기존 PDF 파일에 다양한 유형의 주석을 추가할 수 있습니다. **PdfContentEditor** 클래스의 해당 메서드를 사용하여 기존 PDF 문서에 특정 유형의 주석을 추가할 수 있습니다. 예를 들어, 다음 코드 스니펫에서는 **CreateText(...)** 및 **CreateFreeText(...)** 메서드를 사용하여 각각 기존 PDF에 댓글 및 자유 텍스트 주석을 추가했습니다. **PdfContentEditor** 클래스를 사용하여 주석을 추가하려면 다음 단계를 수행해야 합니다:

- Facades::PdfContentEditor의 객체를 생성합니다.
- **BindPdf(...)** 메서드를 사용하여 기존 PDF를 로드합니다.
- 주석을 생성하기 위해 해당 메서드를 호출합니다. 예: **CreateText(...), CreateFreeText(...), 등.**
- **Save(...)** 메서드를 사용하여 PDF 문서를 저장합니다.
### **기존 PDF 문서에 댓글 추가하기**

다음 코드 스니펫은 기존 PDF 파일에 댓글을 추가하는 방법을 보여줍니다.
```

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-AddAnnotation-AddAnnotation.cpp" >}}
## <ins>**기존 PDF의 모든 주석 삭제**
Aspose.PDF for C++는 PDF 문서에서 모든 주석을 삭제할 수 있는 **PdfAnnotationEditor** 클래스를 제공합니다. 기존 PDF에서 모든 주석을 삭제하려면, **PdfAnnotationEditor** 클래스의 객체를 생성하고 기존 문서를 엽니다. 그런 다음, PdfAnnotationEditor 클래스의 **DeleteAnnotations(...)** 메서드를 사용하여 주석을 삭제할 수 있습니다. 다음 코드 스니펫은 목적을 달성하기 위해 PdfAnnotationEditor의 사용법을 보여줍니다:



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteAllAnnotations-1.cpp" >}}
## <ins>**지정된 유형에 따라 모든 주석 삭제**
**PdfAnnotationEditor** 클래스를 사용하여 기존 PDF 파일에서 지정된 주석 유형에 따라 모든 주석을 삭제할 수 있습니다. 이 작업을 수행하기 위해서는 **PdfAnnotationEditor** 객체를 생성하고 **BindPdf** 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, 문자열 매개변수를 사용하여 **DeleteAnnotations** 메서드를 호출하여 파일에서 모든 주석을 삭제합니다. 문자열 매개변수는 삭제할 주석 유형을 나타냅니다. 마지막으로, **Save** 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 지정된 주석 유형에 따라 모든 주석을 삭제하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteParticularAnnotation-1.cpp" >}}
## <ins>**기존 PDF 파일의 주석 업데이트/수정**
PDF 문서에서 주석을 업데이트 수정하려면, **PdfAnnotationEditor** 클래스의 **ModifyAnnotations(...)** 메서드를 사용할 수 있습니다. 이 메서드는 주석 객체와 함께 주석의 시작 및 끝 인덱스를 받습니다. 다음 코드 스니펫은 **ModifyAnnotations(...)** 메서드의 사용법을 보여줍니다:

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ModifyAnnotations-1.cpp" >}}## <ins>**XFDF에서 PDF 파일로 주석 가져오기**
**PdfAnnotationEditor** 클래스의 **ImportAnnotationFromXfdf** 메서드를 사용하면 주석을 PDF 파일로 가져올 수 있습니다. 주석을 가져오려면 **PdfAnnotationEditor** 객체를 생성하고 **BindPdf** 메서드를 사용하여 PDF 파일을 바인딩해야 합니다. 그런 다음 PDF 파일에 가져오려는 주석 유형의 열거형을 생성해야 합니다. 그런 다음 **ImportAnnotationFromXfdf** 메서드를 사용하여 주석을 가져올 수 있습니다. 마지막으로 **PdfAnnotationEditor** 객체의 **Save** 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 XFDF 파일에서 주석을 가져오는 방법을 보여줍니다.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ImportAnnotations-1.cpp" >}}
## **PDF 파일에서 XFDF로 주석 내보내기**
**ExportAnnotationXfdf** 메서드를 사용하면 PDF 파일에서 주석을 내보낼 수 있습니다. 주석을 내보내려면 **PdfAnnotationEditor** 객체를 생성하고 **BindPdf** 메서드를 사용하여 PDF 파일을 바인딩해야 합니다. 그런 다음 PDF 파일에서 내보내고자 하는 주석 유형의 열거형을 만들어야 합니다. 그런 다음 **ExportAnnotationXfdf** 메서드를 사용하여 주석을 가져올 수 있습니다. 마지막으로 **PdfAnnotationEditor** 객체의 **Save** 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 XFDF 파일로 주석을 내보내는 방법을 보여줍니다.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExportAnnotations-1.cpp" >}}
## <ins>기존 PDF 파일에서 주석 추출
**ExtractAnnotations** 메서드를 사용하면 PDF 파일에서 주석을 추출할 수 있습니다. 문서를 주석을 추출하려면, **PdfAnnotationEditor** 객체를 생성하고 **BindPdf** 메서드를 사용하여 PDF 파일을 바인딩해야 합니다. 그 후, PDF 파일에서 추출하려는 주석 유형의 열거형을 생성해야 합니다. 그런 다음 **Extract** **Annotations** 메서드를 사용하여 주석을 ArrayPtr로 추출할 수 있습니다. 그 후, 이 리스트를 반복하여 개별 주석을 가져올 수 있습니다. 마지막으로, **PdfAnnotationEditor** 객체의 **Save** 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일에서 주석을 추출하는 방법을 보여줍니다.