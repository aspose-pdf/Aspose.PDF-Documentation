---
title: Umbraco PDF 가져오기 모듈
type: docs
weight: 10
url: /ko/net/umbraco-pdf-import-module/
description: Umbraco PDF 가져오기 모듈 설치 및 사용 방법을 알아보세요
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 소개

**Aspose.PDF for .NET** 은 Adobe Acrobat을 사용하지 않고도 .NET 애플리케이션에서 PDF 문서를 읽고, 쓰고, 조작할 수 있게 해주는 PDF 문서 생성 및 조작 구성 요소입니다. 또한 PDF 문서에 포함된 폼과 폼 필드를 생성하고 관리할 수 있습니다.

**Aspose.PDF for .NET** 은 저렴하고 PDF 압축 옵션, 표 생성 및 조작 지원, 그래프 객체 지원, 광범위한 하이퍼링크 기능, 확장된 보안 제어, 사용자 정의 글꼴 처리, 데이터 소스와의 통합, 북마크 추가 또는 제거, 목차 생성, 첨부 파일 및 주석 추가, 업데이트, 삭제, PDF 양식 데이터 가져오기 또는 내보내기, 텍스트 및 이미지 추가, 교체 또는 삭제, 페이지 분할, 연결, 추출 또는 삽입, 페이지를 이미지로 변환, PDF 문서 인쇄 등을 포함하여 놀라운 기능을 제공합니다.
**Aspose.PDF for .NET**은 저렴하며 PDF 압축 옵션, 테이블 생성 및 조작, 그래프 객체 지원, 광범위한 하이퍼링크 기능, 확장된 보안 제어, 사용자 정의 글꼴 처리, 데이터 소스와의 통합, 북마크 추가 또는 제거, 목차 생성, 첨부 파일 및 주석 추가, 업데이트, 삭제, PDF 양식 데이터의 가져오기 또는 내보내기, 텍스트 및 이미지 추가, 교체 또는 제거, 페이지 분할, 연결, 추출 또는 삽입, 페이지를 이미지로 변환, PDF 문서 인쇄 등을 포함한 놀라운 다양한 기능을 제공합니다.

### **모듈 기능**

Umbraco PDF Import는 [Aspose](http://www.aspose.com/)에서 제공하는 오픈 소스 애드온으로, 개발자가 다른 소프트웨어 없이 어떤 PDF 문서의 내용도 읽을 수 있게 해줍니다.
Umbraco PDF 가져오기는 개발자가 다른 소프트웨어 없이 모든 PDF 문서의 내용을 가져오거나 읽을 수 있게 해 주는 [Aspose](http://www.aspose.com/)에서 제공하는 오픈 소스 애드온입니다.

## 시스템 요구 사항 및 지원 플랫폼

### **시스템 요구 사항**

Aspose .NET Pdf 가져오기 Umbraco 모듈을 설정하려면 다음 요구 사항을 충족해야 합니다:

- Umbraco 6.0 +

다른 버전의 Umbraco에 이 모듈을 설치하고 싶다면 언제든지 문의해 주세요.

### **지원 플랫폼**

이 모듈은 모든 버전에서 지원됩니다

- ASP.NET 4.0에서 실행되는 Umbraco

## 다운로드

다음 위치 중 하나에서 Aspose .NET Pdf 가져오기 Umbraco를 다운로드할 수 있습니다

- [CodePlex](https://asposeumbraco.codeplex.com/releases)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/releases)
- [Sourceforge](https://sourceforge.net/projects/asposeumbraco/files/)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/downloads)
- [Umbraco](https://our.umbraco.org/projects/developer-tools/import-from-pdf-using-aspose-pdf)
- [Umbraco](https://our.umbraco.org/projects/developer-tools/import-from-pdf-using-aspose-pdf)

## 설치하기

다운로드한 후, 다음 단계에 따라 이 패키지를 Umbraco 웹사이트에 설치하세요:

1. Umbraco **개발자** 섹션에 로그인하세요, 예를 들어 <http://www.myblog.com/umbraco/>
1. 트리에서 **패키지** 폴더를 확장하세요.
   여기서 패키지를 설치하는 두 가지 방법이 있습니다: **로컬 패키지 설치**를 선택하거나 **Umbraco 패키지 리포지토리**를 검색하세요.
1. **로컬 패키지**를 설치하는 경우, 패키지를 압축 해제하지 말고 Umbraco에 zip을 로드하세요.
1. 화면의 지시에 따릅니다.

**참고:** 설치하는 동안 '최대 요청 길이 초과' 오류가 발생할 수 있습니다. Umbraco web.config 파일에서 'maxRequestLength' 값을 업데이트함으로써 이 문제를 쉽게 해결할 수 있습니다.

```xml
  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
```

## 사용하기

매크로를 설치한 후, 웹사이트에서 사용하기 시작하는 것은 정말 간단합니다:

1.
1. 화면 하단 왼쪽의 섹션 목록에서 **설정**을 클릭하세요.
1. **템플릿** 노드를 확장하고 매크로를 추가하고자 하는 템플릿을 선택하세요, 예를 들어 블로그 포스트.
1. 선택한 템플릿에서 버튼을 추가하고 싶은 위치를 선택하세요.
1. 상단 리본에서 **매크로 삽입**을 클릭하세요.
1. **매크로 선택**에서 설치된 매크로를 선택하고 **확인**을 클릭하세요.

템플릿이 성공적으로 추가되었습니다. 이제 **PDF에서 가져오기**라는 제목의 버튼이 이 템플릿을 사용하여 생성된 모든 페이지에 표시됩니다. 누구나 버튼을 클릭하기만 하면 PDF 문서의 내용을 가져올 수 있습니다.

## 비디오 데모

아래 비디오를 확인하셔서 모듈을 작동하는 모습을 보세요.

## 지원, 확장 및 기여

### 지원

Aspose의 초기부터 우리는 고객에게 좋은 제품을 제공하는 것만으로는 충분하지 않을 것이라는 것을 알고 있었습니다.
Aspose의 초기부터 우리는 고객에게 좋은 제품을 제공하는 것만으로는 충분하지 않다는 것을 알고 있었습니다.

이것이 우리가 무료 지원을 제공하는 이유입니다. 우리 제품을 구매하셨든 평가판을 사용하고 계시든, 모든 사용자는 우리의 최대한의 주의와 존중을 받을 자격이 있습니다.

Aspose.PDF .NET for Umbraco 모듈과 관련된 문제나 제안을 다음 플랫폼 중 하나를 사용하여 기록할 수 있습니다.

- [CodePlex](https://asposeumbraco.codeplex.com/workitem/list/basic)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/issues)
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/tickets/?source=navbar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/issues?status=new&status=open)

#### Pdf에서 가져오기

- [Microsoft Developer Network - Q and A](https://code.msdn.microsoft.com/Umbraco-Import-from-Pdf-d4659bc8/view/Discussions#content)

### 확장하고 기여하십시오.

Aspose .NET PDF Import for Umbraco는 오픈 소스이며 소스 코드는 아래에 나열된 주요 소셜 코딩 웹사이트에서 사용할 수 있습니다.
Aspose .NET PDF Import for Umbraco는 오픈 소스이며, 소스 코드는 아래 나열된 주요 소셜 코딩 웹사이트에서 이용 가능합니다.

#### 소스 코드

다음 위치 중 하나에서 최신 소스 코드를 얻을 수 있습니다.

- [CodePlex](https://asposeumbraco.codeplex.com/SourceControl/latest)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco)
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/code/ci/master/tree/)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/src)

#### 소스 코드 구성 방법

소스 코드를 열고 확장하려면 다음이 설치되어 있어야 합니다.

- Visual Studio 2010 이상

시작하려면 다음 간단한 단계를 따르세요.

1. 소스 코드를 다운로드/클론합니다.
1. Visual Studio 2010을 열고 **파일** > **프로젝트 열기**를 선택합니다.
1. 다운로드한 최신 소스 코드를 찾아 **Aspose.Import from PDF.sln**을 엽니다.
