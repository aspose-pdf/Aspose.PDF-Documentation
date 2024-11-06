```
---
title: 즐겨찾기 추가 및 삭제
type: docs
weight: 10
url: ko/cpp/add-and-delete-bookmarks/
---

## <ins>**즐겨찾기 추가**
PdfBookmarkEditor 클래스는 PDF 문서 내에 즐겨찾기를 추가할 수 있도록 합니다. 이 클래스에서 제공하는 CreateBookmarkOfPage 메서드는 지정된 페이지 번호를 대상으로 하는 즐겨찾기를 생성할 수 있게 합니다. 다음 코드 스니펫은 C++ API를 위한 Aspose.PDF의 이 기능을 보여줍니다:



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-CreateBookmark-1.cpp" >}}
## <ins>**기존 문서에 자식 즐겨찾기 추가**
**PdfBookmarkEditor** 클래스를 사용하여 기존 PDF 파일에 자식 즐겨찾기를 추가할 수 있습니다.
``` 문서의 하위 북마크를 추가하려면 **Bookmarks** 및 *Bookmark* 객체를 생성해야 합니다. 개별 **Bookmark** 객체를 **Bookmarks** 객체에 추가할 수 있습니다. 또한 **Bookmark** 객체를 생성하고 해당 **ChildItem** 속성을 **Bookmarks** 객체로 설정해야 합니다. 그런 다음 이 **ChildItem**이 있는 **Bookmark** 객체를 **CreateBookmarks** 메서드에 전달해야 합니다. 마지막으로, **PdfBookmarkEditor** 클래스의 **Save** 메서드를 사용하여 업데이트된 PDF를 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에 하위 북마크를 추가하는 방법을 보여줍니다.



## <ins>**PDF 파일에서 모든 북마크 삭제**
매개변수 없이 **DeleteBookmarks** 메서드를 사용하여 PDF 파일에서 모든 북마크를 삭제할 수 있습니다. 먼저, **PdfBookmarkEditor** 클래스의 객체를 생성하고 **BindPdf** 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그런 다음 **DeleteBookmarks** 메서드를 호출하고 **Save** 메서드를 사용하여 업데이트된 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 PDF 파일에서 모든 북마크를 삭제하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-DeleteAllBookmarks-1.cpp" >}}
## <ins>**PDF 파일에서 특정 북마크 삭제**
특정 북마크를 삭제하려면 문자열(제목) 매개변수를 사용하여 **DeleteBookmarks** 메서드를 호출해야 합니다. 여기서 **title**은 PDF에서 삭제할 북마크를 나타냅니다. **PdfBookmarkEditor** 클래스의 객체를 생성하고 **BindPdf** 메서드를 사용하여 입력 PDF 파일을 바인딩합니다. 그런 다음 **DeleteBookmarks** 메서드를 호출하고 **Save** 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일에서 특정 북마크를 삭제하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-DeleteBookmark-1.cpp" >}}