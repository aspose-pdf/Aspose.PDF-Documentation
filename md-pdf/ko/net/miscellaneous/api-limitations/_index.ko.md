---
title: API 제한 사항
type: docs
weight: 70
url: /net/api-limitations/
---

## **Xsl Fo to Pdf**
다음은 XSL-FO 지원의 알려진 문제점들입니다.

- SVG는 지원되지 않습니다.
## **PDF 생성자 정보**
- **Application** 및 **Producer** 필드에 값을 설정할 수 없다는 점을 유의해 주세요. 이 필드에는 Aspose Ltd. 및 Aspose.PDF for .NET x.x.x가 표시됩니다.
## **기타**
다음은 일부 다른 알려진 문제점들입니다.

- Pdf/X는 지원되지 않습니다.
- 동적 XFA 양식은 지원되지 않습니다: PDF를 로딩할 때 생성/렌더링되는 페이지이기 때문에, Adobe Acrobat/Reader에서 이러한 가상 페이지나 여러 페이지를 추출하고 저장할 수 없습니다. 대신 우리(및 Adobe Acrobat)는 오류 메시지만 포함된 하나의 진짜 페이지만 추출할 수 있습니다.
- 특수 기호 $p와 $P는 빈 문자로 끝나지 않으면 작동하지 않습니다.
- HTML을 PDF로 변환 :- HTML은 매우 광범위한 언어이며, Aspose.PDF for .NET의 새로운 버전이 출시될 때마다 우리는 HTML을 PDF로 변환하는 더 나은 버전을 제공하기 위해 최선을 다하고 있습니다(*모든 종류의 HTML을 지원함으로써*) 하지만 HTML 파일이 다양한 성격/구조 및 복잡성을 가지고 있기 때문에, 때때로 우리의 컴포넌트는 HTML 내용을 PDF 형식으로 렌더링할 때 복잡한 구조의 문서를 사용할 때 일반적으로 발생하는 서식 문제를 일으킬 수 있습니다.
- HTML에서 PDF 변환: HTML은 매우 광범위한 언어이며, Aspose.PDF for .NET의 새 버전이 출시될 때마다 더 나은 HTML에서 PDF 변환 기능(*모든 종류의 HTML을 지원함으로써*)을 제공하기 위해 최선을 다하고 있습니다. 그러나 다양한 성격/구조 및 복잡성을 가진 수많은 HTML 파일이 존재하기 때문에, 때때로 복잡한 구조의 문서를 사용할 때 PDF 형식으로 HTML 내용을 렌더링하는 과정에서 형식 문제가 발생할 수 있습니다.
- MS Word for Macintosh에서는 글꼴 임베딩이 지원되지 않으며, MS Word for Windows에서는 TrueType 글꼴에만 한정된다는 점을 유의하십시오. 따라서 Aspose.PDF for .NET을 통해 PDF에서 DOC으로 변환된 결과로 생성된 Word(DOC) 파일을 MAC OS의 MS Word에서 볼 때, 임베딩된 글꼴이 대체됩니다. 자세한 내용은 [macsupportcentral](http://www.macsupportcentral.com/2012/05/embed-fonts-microsoft-office-word-files/)을 참조하십시오.
