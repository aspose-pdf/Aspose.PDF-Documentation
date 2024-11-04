---
title: Aspose.PDF Editor
linktitle: Aspose.PDF Editor
type: docs
weight: 10
url: /net/aspose-pdf-editor/
description: Aspose.PDF for .NET은 HTML5 PDF 편집기가 포함된 오픈 소스 웹 기반 PDF 편집기를 시연합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aspose.PDF for .NET의 HTML5 PDF 편집기란 무엇인가요?

Aspose.PDF for .NET의 HTML5 PDF 편집기는 사용자가 온라인으로 PDF 파일을 생성, 편집 및 변환할 수 있게 해주는 오픈 소스 웹 기반 PDF 편집기입니다. 사용자는 자신의 웹 애플리케이션에 편집기를 쉽게 통합하여 PDF 파일을 보고 편집할 수 있습니다. HTML5 PDF 편집기는 HTML5, jQuery Ajax, ASP.NET, Bootstrap을 사용하여 개발되었으며 백엔드는 Aspose.PDF for .NET으로 구동됩니다. 편집기의 사용자 인터페이스는 사용자 요구에 따라 기능을 쉽게 이해하고 향상시킬 수 있도록 매우 간단하게 유지되었습니다.

![Image](../images/aspose-pdf-editor.png)

## 기능

현재 다음 기능을 지원합니다:

- 새 PDF 파일 생성
- PDF 파일 로딩 및 보기
- Dropbox에서 PDF 및 이미지 파일 로딩
- Dropbox에서 PDF 및 이미지 파일 로드
- 다른 파일 형식으로 PDF 파일 내보내기
- PDF 파일 추가 또는 병합
- 새 페이지 삽입
- 페이지 삭제
- PDF 파일에서 페이지 이동
- PDF에 텍스트 삽입
- PDF에서 텍스트 하이라이트
- PDF에 삽입된 텍스트 회전
- PDF에서 텍스트 검색
- PDF에서 텍스트 교체
- 이미지 삽입
- 서명 및 이미지 크기 조정
- 삽입된 항목 드래그 및 위치 지정
- 양식 필드가 있는 PDF 파일 로드
- 편집기를 사용하여 양식 필드 채우기
- 양식 필드 데이터가 있는 PDF 저장 및 내보내기
- 필수 양식 필드 하이라이트
- PDF 파일에 첨부 파일 추가
- 입력 PDF 파일에서 첨부 파일 로드
- 첨부 파일 다운로드
- 첨부 파일 제거
- 자유 손으로 그리기를 사용하여 PDF 서명

## 시스템 요구 사항

HTML5 PDF 편집기는 ASP.NET, C#, HTML5, jQuery, Javascript를 사용하여 개발된 .NET 웹 애플리케이션입니다. HTML5 PDF 편집기를 설정하기 위해 다음과 같은 시스템 환경이 필요합니다.

- Visual Studio 2010 (이상)
- .NET Framework 3.5 (이상)
- Aspose.PDF for .NET
- Aspose.PDF for .NET
- jQuery 2.0.3
- Bootstrap 3.2.0

다음 브라우저 중 하나를 사용하여 애플리케이션을 실행할 수 있습니다:

- Mozilla Firefox (추천)
- Internet Explorer (버전 9 이상)
- Google Chrome
- Apple Safari

## 지원

Aspose에서는 고객 또는 사용자의 모든 종류의 문의에 대해 가능한 최고의 지원을 제공하기 위해 노력합니다. 라이선스 및 판매 관련 또는 기술적 문의에 대해서는 아래 링크를 사용하십시오.

# PDF 편집기 개발자 가이드

## 새 PDF 파일 생성

기존 PDF 문서를 편집하는 것 외에도, Html5 PDF 편집기는 메뉴 바에서 '새 파일 생성' 옵션을 사용하여 처음부터 새 PDF 파일을 생성하는 것도 지원합니다. 이 기능을 사용하면 편집기에서 빈 PDF를 생성하고 텍스트나 이미지를 추가한 다음 원하는 형식으로 저장할 수 있습니다. 다음 섹션에서는 이 기능의 기술적인 세부 사항에 대해 논의할 것입니다.

### 작동 원리는?

**HTML - "새 파일 생성" 메뉴 항목이 페이지에서 클릭됩니다**

"새 파일 생성" 메뉴 항목을 클릭하면, Editor.js 파일에서 onNewFileClicked 메소드가 호출됩니다.
"Create New File" 메뉴 항목을 클릭하면 Editor.js 파일의 onNewFileClicked 메소드가 호출됩니다.

**jQuery - 서버에 CreateNewFile 메소드를 위한 Ajax 요청을 보냅니다.**

아래 Editor.js 탭에서 onNewFileClicked 메소드의 소스 코드를 확인할 수 있습니다. 이 메소드는 CanvasSave.aspx.cs 파일의 CreateNewFile 메소드를 호출합니다.

**ASP.NET 웹 메소드가 서버 요청을 처리합니다**

아래 Canvas.aspx.cs 탭에서 CreateNewFile 메소드의 소스 코드를 볼 수 있습니다. 이 메소드는 이전에 로드된 파일과 관련된 모든 기존 데이터를 ResetData 메소드를 사용하여 지웁니다.

**Aspose.PDF for .NET을 사용한 새 PDF 파일 생성**

ResetData 메소드를 사용하여 데이터를 지운 후, CreateNewFile 메소드는 Aspose.PDF for .NET의 Document 클래스를 사용하여 새 PDF 파일을 생성합니다.
아래 탭에서 볼 수 있듯이, Document 객체는 비어 있는 한 페이지로 파일을 생성합니다. 서버에서 파일이 생성된 후, 파일은 ImageConverter 메소드를 사용하여 이미지로 변환되어 캔버스에 로드됩니다.

**결과 파일을 캔버스에 로드합니다.**

서버 측에서 파일이 이미지로 변환된 후, 제어는 Editor.js의 onNewFileClicked 메소드로 다시 반환됩니다.
파일이 서버 측에서 이미지로 변환된 후, 제어는 Editor.js의 onNewFileClicked 메서드로 다시 반환됩니다.

## PDF를 다른 파일 형식으로 내보내기

HTML5 PDF 편집기는 메뉴 바에서 파일 내보내기 옵션을 사용하여 PDF 파일을 다양한 파일 형식으로 내보낼 수 있습니다. 이 기능을 사용하면 원하는 형식으로 PDF 파일을 내보낼 수 있습니다. 다음 섹션에서는 이 기능의 기술적 세부 사항에 대해 논의할 것입니다.

### 작동 원리는 무엇입니까?

**HTML - "파일 내보내기" 메뉴 항목이 페이지에서 클릭됩니다.**

"파일 내보내기" 메뉴 항목을 클릭하면 목록에서 내보낼 형식을 선택할 수 있습니다. 내보낼 형식을 선택한 후, Editor.js 파일에서 "ExportFile" 메서드가 호출됩니다.

**jQuery - Ajax 서버 요청을 method btnFileExport_Click 메서드로 보냅니다**

아래 Editor.js 탭에서 "ExportFile" 메서드의 소스 코드를 확인하세요. 파일 형식 매개변수가 있는 CanvasSave.aspx.cs 파일의 서버 메서드 btnFileExport_Click에 요청을 보냅니다.

**ASP.NET 웹 메서드가 서버 요청을 처리합니다**

아래 Canvas.aspx.cs 탭을 확인하세요.
**클라이언트 브라우저에서 다운로드를 위한 파일 내보내기**

서버에서 파일이 생성된 후, 제어권이 Editor.js의 ExportFile 메소드로 돌아가고 사용자가 ExportToBrowser 메소드를 사용하여 브라우저를 통해 파일을 다운로드할 수 있습니다.

## PDF 파일 추가 또는 병합

Html5 PDF Editor는 메뉴 바의 파일 추가 옵션을 사용하여 PDF 파일을 추가하거나 병합할 수 있는 기능을 지원합니다. 이 기능을 사용하면 입력 파일에 PDF 파일을 추가할 수 있습니다. 다음 섹션에서 이 기능의 기술적인 세부 사항에 대해 논의할 것입니다.

### 작동 원리는?

**HTML - 페이지에서 "파일 추가" 메뉴 항목이 클릭됩니다.**

"파일 추가" 메뉴 항목을 클릭하면 파일 업로드 대화 상자를 사용하여 파일을 업로드할 수 있습니다. 파일이 업로드되면 Editor.js 파일의 "fileSelected" 메소드가 호출됩니다.

**jQuery - ProcessRequest 메소드에 대한 서버 요청 전송**

아래 Editor.js 탭에서 "fileSelected" 메소드의 소스 코드를 확인하세요.
**ASP.NET 웹 메서드는 서버 요청을 처리합니다**

Canvas.aspx.cs 탭을 확인하세요. 전달된 폼 매개변수에 따라 서버에 저장될 파일이 선택되고 "AppendFile" 메서드가 호출됩니다. AppendFile 메서드는 Aspose.PDF for .NET을 사용하여 업로드된 파일을 추가하고, 결과 파일을 이미지로 변환한 후 "fileSelected" 메서드로 제어를 반환합니다.

**파일 추가 후 캔버스 내용 업데이트**

서버에서 파일이 생성된 후, 제어는 Editor.js의 "fileSeleceted" 메서드로 반환되며, 이 메서드는 에디터의 내용을 업데이트합니다.

## 로컬 PDF 파일 업로드

HTML5 PDF Editor는 메뉴 바의 컴퓨터에서 열기 옵션을 사용하여 로컬 기계에서 PDF 파일을 업로드 할 수 있습니다. 이 기능을 사용하면 기존 PDF 파일을 열고 PDF 파일을 편집할 수 있습니다. 다음 섹션에서는 이 기능의 기술적 세부 사항에 대해 논의할 것입니다.

### 작동 원리는?

**HTML - 페이지에서 "컴퓨터에서 열기" 메뉴 항목이 클릭됩니다.**
**HTML - "컴퓨터에서 열기" 메뉴 항목이 페이지에서 클릭됩니다.**

"컴퓨터에서 열기" 메뉴 항목을 클릭하면 파일 업로드 대화 상자를 사용하여 입력 파일을 업로드할 수 있습니다. 파일이 업로드되면 Editor.js 파일에서 "fileSelected" 메소드가 호출됩니다.

**jQuery - ProcessRequest 메소드를 위한 서버 요청 보내기**

아래 Editor.js 탭에서 "fileSelected" 메소드의 소스 코드를 확인하세요. 파일이 서버에 게시되고 CanvasSave.aspx.cs 파일에서 "ProcessRequest" 메소드가 호출됩니다.

**ASP.NET 웹 메소드가 서버 요청을 처리합니다**

아래 Canvas.aspx.cs 탭을 보세요. 전달된 폼 매개변수에 따라, 업로드할 파일이 서버에 저장되고, "ResetData" 메소드를 사용하여 데이터를 초기화하고 "ImageConverter" 메소드가 호출됩니다. ImageConverter 메소드는 Aspose.PDF for .NET을 사용하여 업로드된 파일을 이미지로 변환하고 제어를 다시 "fileSelected" 메소드로 반환합니다.

**파일 업로드 후 캔버스 내용 업데이트**

서버에서 파일이 생성된 후, 제어는 Editor.js의 "fileSeleceted" 메소드로 다시 반환되며, 편집기의 내용을 업데이트합니다.
파일이 서버에서 생성된 후, "fileSeleceted" 메소드로 제어가 반환되어 Editor.js에서 편집기의 내용을 업데이트합니다.

## PDF 파일에 페이지 추가

Html5 PDF 편집기를 사용하여 메뉴 바에서 페이지 추가 옵션을 사용하여 PDF 파일에 새 페이지를 추가할 수 있습니다. 이 기능을 사용하면 PDF 파일에 빈 페이지를 추가할 수 있습니다. 다음 섹션에서는 이 기능의 기술적 세부 사항에 대해 논의할 것입니다.

### 작동 원리는?

**HTML - "페이지 추가" 메뉴 항목이 페이지에서 클릭됨**

"페이지 추가" 메뉴 항목을 클릭하면 Editor.js 파일의 "AddPage" 메소드가 호출됩니다.

**jQuery - AddPage_Click 메소드에 대해 서버로 Ajax 요청을 보냅니다.**

아래 Editor.js 탭에서 AddPage 메소드의 소스 코드를 확인하세요. 이는 CanvasSave.aspx.cs 파일의 AddPage_Click 메소드를 호출합니다.

**ASP.NET 웹 메소드가 서버 요청을 처리합니다**

아래 Canvas.aspx.cs 탭에서 AddPage_Click 메소드의 소스 코드를 확인하세요.
## PDF 파일에서 페이지 삭제

Html5 PDF 편집기를 사용하면 메뉴 바의 삭제 페이지 옵션을 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다. 다음 섹션에서는 이 기능의 기술적 세부 사항에 대해 논의할 것입니다.

### 작동 원리는?

**HTML - "페이지 삭제" 메뉴 항목이 페이지에서 클릭됨**

"페이지 삭제" 메뉴 항목을 클릭하면 Editor.js 파일에서 DeletePage 메소드가 호출됩니다.

**jQuery - 서버에 DeletePage_Click 메소드에 대한 Ajax 요청을 보냄**

Editor.js 탭 아래에서 DeletePage 메소드의 소스 코드를 확인하세요. 그것은 CanvasSave.aspx.cs 파일에서 DeletePage_Click 메소드를 호출합니다.

**ASP.NET 웹 메소드가 서버 요청을 처리함**

Canvas.aspx.cs 탭 아래에서 DeletePage_Click 메소드의 소스 코드를 확인하세요. Aspose.PDF.Document.Page 컬렉션의 Delete 메소드를 사용하여 PDF 파일에서 선택된 페이지를 삭제합니다.

**편집 내용 업데이트**

PDF 파일에서 페이지를 삭제한 후에는 제어가 Editor.js 파일의 DeletePage 메소드로 다시 반환되어 페이지 번호를 업데이트하고 삭제된 페이지와 관련된 모든 컬렉션을 updateIndexesDelete 메소드를 사용하여 제거합니다.
PDF 파일에서 페이지를 삭제한 후에는 Editor.js 파일의 DeletePage 메소드로 제어가 반환되어 페이지 번호를 업데이트하고 삭제된 페이지와 관련된 모든 컬렉션을 updateIndexesDelete 메소드를 사용하여 제거합니다.

## PDF 파일에서 페이지 이동

Html5 PDF 편집기를 사용하면 메뉴 바의 페이지 이동 옵션을 사용하여 PDF 파일에서 페이지를 이동할 수 있습니다. 페이지 이동 메뉴 항목을 클릭하면 선택한 페이지의 새 위치를 지정하기 위한 입력 대화 상자가 표시됩니다. 다음 섹션에서는 이 기능의 기술적 세부 사항에 대해 논의할 것입니다.

### 작동 원리는?

**HTML - "페이지 이동" 메뉴 항목이 페이지에서 클릭됩니다**

"페이지 이동" 메뉴 항목을 클릭하면 새 위치를 얻기 위한 입력 대화 상자가 표시됩니다. 페이지 번호를 제공하고 "이동" 버튼을 누르면 Editor.js 파일의 "이동" 메소드가 호출됩니다.

**jQuery - MovePages 메소드에 대해 서버로 Ajax 요청을 보냅니다.**

아래 Editor.js 탭에서 Move 메소드의 소스 코드를 참조하십시오. 이 메소드는 MovePage 메소드를 호출하고 CanvasSave.aspx.cs 파일의 MovePages 메소드에 이동 시작, 이동 종료, 페이지 목록과 같은 세부 정보를 전달합니다.
**ASP.NET 웹 메소드는 서버 요청을 처리합니다**

Canvas.aspx.cs 탭 아래의 MovePages 메소드의 소스 코드를 보십시오. 이 메소드는 Aspose.PDF.Document.Pages 컬렉션을 사용하여 페이지를 이동합니다.

**편집 내용 업데이트**

페이지를 이동한 후, 제어는 Editor.js 파일의 MovePage 메소드로 돌아가고, MoveUpdate 메소드를 사용하여 편집기의 다른 컬렉션과 관련된 페이지 인덱스 및 정보를 업데이트합니다.

## PDF 파일에 텍스트 삽입

Html5 PDF 편집기를 사용하면 메뉴 바에서 텍스트 모드 옵션을 선택하여 PDF 파일에 텍스트를 삽입할 수 있습니다. 텍스트 모드 메뉴 항목을 선택하고 텍스트를 추가하고자 하는 편집기의 위치를 클릭하면 아래와 같이 원하는 텍스트를 입력하고 형식을 지정할 수 있는 입력 대화 상자가 표시됩니다:

다음 섹션에서는 이 기능의 기술적인 세부 사항에 대해 논의할 것입니다.
다음 섹션에서는 이 기능의 기술적인 세부 사항을 논의할 것입니다.

### 작동 원리는?

**HTML - "텍스트 모드" 메뉴 항목이 페이지에서 선택됨**

"텍스트 모드" 메뉴 항목을 선택하고 PDF 파일에 텍스트를 삽입하고자 하는 편집기 위치를 클릭하면 입력 대화 상자가 나타나 페이지에 삽입할 텍스트를 입력하도록 요청합니다. 텍스트를 제공하고 "확인" 버튼을 누르면 Editor.js 파일의 "saveTextFromArea" 메소드가 호출됩니다.

**Javascript - 입력 대화 상자에서 입력 텍스트를 가져와 편집기에 표시**

아래에 있는 Editor.js 탭에서 입력 대화 상자에서 텍스트를 가져와 편집기에 표시하고 나중에 서버 측에서 PDF 파일에 텍스트를 삽입하는 데 사용되는 도형 컬렉션에 데이터를 저장하는 saveTextFromArea 메소드의 소스 코드를 확인할 수 있습니다. 파일이 저장될 때 호출되는 saveFile 메소드의 소스 코드도 확인할 수 있습니다.

**ASP.NET 웹 메소드가 서버 요청을 처리**

위에서 언급한 바와 같이, GetTextStamp 메소드를 사용하여 PDF 파일에 텍스트 도장을 삽입하는 save 작업을 수행할 때 실제로 원본 PDF 파일에 텍스트가 삽입됩니다.
위에서 언급한 것처럼, GetTextStamp 메소드를 사용하여 PDF 파일에 텍스트 스탬프를 삽입하는 저장 작업을 수행할 때 실제로 우리의 원본 PDF 파일에 텍스트가 삽입됩니다.

## PDF 파일에서 텍스트 강조

Html5 PDF 편집기를 사용하면 메뉴 바에서 '강조 모드' 옵션을 선택하여 PDF 파일에서 텍스트를 강조할 수 있습니다. '강조 모드' 메뉴 항목을 선택하면 직사각형 강조 도구를 사용하여 텍스트와 영역을 강조할 수 있습니다. 다음 섹션에서는 이 기능의 기술적 세부 사항에 대해 논의할 예정입니다.

### 작동 원리는?

**HTML - 페이지에서 '강조 모드' 메뉴 항목이 선택됨**

'강조 모드' 메뉴 항목을 선택하면 PDF 파일의 텍스트나 항목 주위에 직사각형 강조를 그릴 수 있습니다. 이 과정의 구현은 Editor.js 파일의 "tools.rect" 메소드에서 볼 수 있습니다.

**Javascript - 편집기에서 강조 직사각형 그리기.**

아래 Editor.js 탭에서 tool.rect 메소드의 소스 코드를 확인하십시오. 이 메소드는 사용자가 편집기의 임의 위치에 강조 직사각형을 그릴 수 있게 합니다.
Editor.js 탭 아래에는 사용자가 편집기의 어떤 위치에서든 강조 표시 사각형을 그릴 수 있도록 하는 tool.rect 메소드의 소스 코드가 있습니다.

**ASP.NET 웹 메소드는 서버 요청을 처리합니다**

위에서 언급했듯이, 강조 표시는 GetImageStamp 메소드를 사용하여 저장 작업을 수행할 때 원본 PDF 파일에 실제로 삽입됩니다. 이 메소드는 편집기에서 지정한 위치에 이미지 스탬프를 원본 PDF 파일에 삽입합니다. Canvas.aspx.cs 탭 아래에 GetImageStamp 메소드의 소스 코드가 있습니다. 이는 Aspose.PDF.ImageStamp 클래스를 사용하여 PDF 파일에 강조 표시 사각형을 삽입합니다.

## PDF 파일에서 텍스트 검색

Html5 PDF 편집기를 사용하면 메뉴 바에서 검색 텍스트 옵션을 사용하여 PDF 파일에서 텍스트를 검색할 수 있습니다. 검색 텍스트 메뉴 항목을 클릭하면 아래와 같이 텍스트를 입력할 수 있는 대화 상자가 표시됩니다:

텍스트를 제공하고 검색을 누르면 검색된 단어의 모든 인스턴스가 아래와 같이 강조 표시됩니다:

### 작동 원리는?

**HTML - 페이지에서 "검색 텍스트" 메뉴 항목이 클릭됩니다**
**HTML - "텍스트 검색" 메뉴 항목이 클릭됩니다**

"텍스트 검색" 메뉴 항목을 클릭하면 텍스트를 입력할 입력 대화 상자가 나타납니다. 텍스트를 입력하고 검색 버튼을 누르면 "이동" 메서드가 호출되어 페이지 이동 작업이 수행되는지 검색 작업이 수행되는지를 확인한 다음 Editor.js 파일에서 performSearch 메서드를 호출합니다.

**jQuery - Ajax 서버 요청 보내기 SearchData 메서드에 대한 요청**

아래 Editor.js 탭을 참조하여 입력 텍스트와 _CanvasSave.aspx.cs_ 파일의 서버 메서드 SearchData로 요청을 보내는 performSearch 메서드의 소스 코드를 확인하세요.

**ASP.NET 웹 메서드가 서버 요청을 처리합니다**

아래 _Canvas.aspx.cs_ 탭을 참조하세요.
_Canvas.aspx.cs_ 탭을 아래에서 확인하세요.

## PDF 파일에서 텍스트 교체하기

Html5 PDF 편집기를 사용하면 메뉴 바의 텍스트 교체 옵션을 사용하여 PDF 파일의 기존 텍스트를 교체할 수 있습니다. 텍스트 교체 메뉴 항목을 클릭하면 검색하고 교체할 텍스트를 입력할 대화 상자가 표시됩니다.

### 작동 원리는?

**HTML - "텍스트 교체" 메뉴 항목이 페이지에서 클릭됨**

"텍스트 교체" 메뉴 항목을 클릭하면 검색하고 교체할 텍스트를 입력하는 입력 대화 상자가 표시됩니다. 텍스트를 입력하고 교체 버튼을 누르면 Editor.js 파일의 "ReplaceText" 메소드가 호출됩니다.

**jQuery - Ajax 서버 요청을 ReplaceText 메소드로 보냄**

Editor.js 탭 아래에서 ReplaceText 메소드의 소스 코드를 확인하세요. 이 메소드는 입력 텍스트 대화 상자에서 입력 텍스트를 가져와 CanvasSave.aspx.cs 파일의 서버 메소드 ReplaceText로 요청을 보냅니다.

**ASP.NET 웹 메소드가 서버 요청을 처리함**

Canvas.aspx.cs 탭 아래에서 확인하세요.
## PDF 파일 로드하기

Html5 PDF 편집기를 사용하면 양식 필드가 포함된 PDF 파일을 로드하고 작업할 수 있습니다. 양식 필드가 포함된 파일이 편집기에서 로드되면 모든 양식 필드가 편집을 위해 로드됩니다. 다음 섹션에서는 이 기능의 기술적 세부 사항에 대해 논의할 것입니다.

### 작동 원리는?

**HTML - "컴퓨터에서 열기" 메뉴 항목 클릭됨**

"컴퓨터에서 열기" 메뉴 항목을 클릭하면 파일 업로드 대화상자를 통해 양식 필드가 포함된 입력 파일을 업로드할 수 있습니다. 파일이 업로드되면 Editor.js 파일에서 "fileSelected" 메서드가 호출됩니다.

**jQuery - ProcessRequest 메서드에 대한 서버 요청 보내기**

파일이 서버로 전송되고 CanvasSave.aspx.cs 파일에서 "ProcessRequest" 메서드가 호출됩니다.

**ASP.NET 웹 메서드가 서버 요청을 처리합니다**

Canvas.aspx.cs 탭을 참조하세요.
**캔버스에 양식 필드 로드**

캔버스에 있는 모든 필드를 생성하는 데 사용되는 Editor.js의 manageFields 메소드를 아래 Editor.js 탭에서 확인하세요. 서버 측에서 전송된 정보에 기초하여 캔버스에 HTML 필드 컨트롤을 그립니다. 서버 측의 유형 및 위치 정보를 사용합니다.

## 필수 양식 필드 강조

Html5 PDF 편집기를 사용하여 편집기에서 필수 양식 필드를 강조 표시할 수 있습니다. 양식 필드가 포함된 파일이 편집기에 로드되면, 모든 필수 양식 필드가 사용자가 편집을 돕기 위해 강조 표시됩니다. 다음 섹션에서는 이 기능의 기술적 세부 사항에 대해 논의할 것입니다.

### 작동 원리는?

**HTML - "컴퓨터에서 열기" 메뉴 항목이 페이지에서 클릭됩니다.**

"컴퓨터에서 열기" 메뉴 항목을 클릭하면, 파일 업로드 대화 상자를 사용하여 양식 필드가 포함된 입력 파일을 업로드할 수 있습니다. 파일이 업로드되면 Editor.js 파일의 "fileSelected" 메소드가 호출됩니다.

**jQuery - ProcessRequest 메소드에 대한 서버 요청 전송**
**jQuery - 서버 요청을 ProcessRequest 메소드로 전송**

파일이 서버로 전송되고 CanvasSave.aspx.cs 파일에서 "ProcessRequest" 메소드가 호출됩니다.

**ASP.NET 웹 메소드가 서버 요청을 처리**

아래의 Canvas.aspx.cs 탭을 참조하세요. 전달된 폼 파라미터에 따라, 업로드할 파일이 서버에 저장되고, ImageConverter 메소드는 업로드된 파일을 이미지로 변환하며 "CheckFields" 메소드가 호출됩니다. 이 메소드는 Aspose.PDF.InteractiveFeatures.Forms 클래스를 사용하여 모든 폼 필드를 확인하고 필드 유형, 위치 등에 대한 정보를 수집합니다. 모든 폼 필드의 세부 정보를 얻은 후, Aspose.PDF.Facades.IsRequiredField 메소드를 사용하여 필수 폼 필드인지의 여부를 확인하고 필드 컬렉션을 ImageConverter 메소드로 반환합니다. ImageConverter 메소드는 제어권을 Editor.js의 "fileSelected" 메소드로 반환합니다.

**캔버스에 폼 필드 로딩**

아래의 Editor.js 탭을 참조하세요. Editor.js의 manageFields 메소드는 서버 측에서 보낸 정보를 기반으로 캔버스에 모든 필드를 생성하는 데 사용됩니다.

Editor.js 탭을 참조하세요. Editor.js의 manageFields 메서드는 서버 측에서 반환된 정보를 기반으로 캔버스에 모든 필드를 생성하는 데 사용됩니다.
```
