---
title: Aspose.PDF Java for Jython
type: docs
weight: 60
url: ko/java/aspose-pdf-java-for-jython/
lastmod: "2021-06-05"
---

## 소개

### Jython이란 무엇인가?

Jython은 명확성과 표현력을 결합한 Python의 Java 구현입니다. Jython은 상업적 및 비상업적 용도로 무료로 사용할 수 있으며 소스 코드와 함께 배포됩니다. Jython은 Java를 보완하며 다음 작업에 특히 적합합니다:

- **임베디드 스크립팅** - Java 프로그래머는 시스템에 Jython 라이브러리를 추가하여 최종 사용자가 애플리케이션에 기능을 추가하는 간단하거나 복잡한 스크립트를 작성할 수 있습니다.
- **대화형 실험** - Jython은 Java 패키지나 실행 중인 Java 애플리케이션과 상호작용할 수 있는 대화형 인터프리터를 제공합니다. 이를 통해 프로그래머는 Jython을 사용하여 Java 시스템을 실험하고 디버그할 수 있습니다.
- **신속한 애플리케이션 개발** - Python 프로그램은 일반적으로 동등한 Java 프로그램보다 2-10배 짧습니다.
 프로그래머의 생산성이 직접적으로 증가합니다. Python과 Java 간의 원활한 상호 작용을 통해 개발자들은 개발 중과 제품 출시에 두 언어를 자유롭게 혼합할 수 있습니다.

### Aspose.PDF for Java

Aspose.PDF for Java는 Adobe Acrobat을 사용하지 않고도 Java 애플리케이션이 PDF 문서를 읽고, 쓰고, 조작할 수 있게 하는 PDF 문서 생성 구성 요소입니다.

Aspose.PDF for Java는 놀라운 기능의 부를 제공하는 적절한 가격의 구성 요소로, PDF 압축 옵션, 표 생성 및 조작, 그래프 지원, 이미지 기능, 광범위한 하이퍼링크 기능, 확장된 보안 제어 및 사용자 정의 글꼴 처리를 포함합니다.

Aspose.PDF for Java를 통해 제공된 API와 XML 템플릿을 통해 직접 PDF 파일을 생성할 수 있습니다. Aspose.PDF for Java를 사용하면 애플리케이션에 빠르게 PDF 기능을 추가할 수도 있습니다.

### Aspose.PDF Java for Jython

Aspose.PDF Java for Jython은 Jython에서 Aspose.PDF for Java API 사용 예제를 시연/제공하는 프로젝트입니다.
## 시스템 요구 사항 및 지원 플랫폼

### 시스템 요구 사항

다음은 Aspose.PDF Java for Jython을 사용하기 위한 시스템 요구 사항입니다:

- Java 1.5 이상 설치
- 다운로드한 Aspose.PDF 컴포넌트
- Jython 2.7.0

### 지원 플랫폼

다음은 지원되는 플랫폼입니다:

- Aspose.PDF 15.4 및 그 이상.
- Java IDE (Eclipse, NetBeans ...)

## 다운로드 설치 및 사용

### 다운로드

다음 실행 예제의 릴리스는 GitHub에서 다운로드할 수 있습니다:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

Aspose.PDF for Java 컴포넌트를 다운로드합니다:

- [Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)

### 설치

- 다운로드한 Aspose.PDF for Java jar 파일을 "lib" 디렉토리에 넣습니다.
- _*init*_.py 파일에서 "your-lib"을 다운로드한 jar 파일명으로 교체합니다.

### 사용

다음 예제 코드를 사용하여 Pdf를 doc 문서로 변환할 수 있습니다:

```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'


        # 대상 문서를 엽니다
        pdf = Document(dataDir + 'input1.pdf')

        # 연결된 출력 파일(대상 문서)을 저장합니다
        pdf.save(dataDir + "output.doc")

        print "문서가 성공적으로 변환되었습니다"


if __name__ == '__main__':       

    PdfToDoc()
```


## 지원, 확장 및 기여

### 지원

Aspose의 첫날부터, 우리는 단지 고객에게 좋은 제품을 제공하는 것만으로는 충분하지 않다는 것을 알고 있었습니다. 우리는 또한 좋은 서비스를 제공해야 했습니다. 우리도 개발자이며, 기술적인 문제나 소프트웨어의 버그로 인해 해야 할 일을 할 수 없을 때 얼마나 좌절스러운지 이해합니다. 우리는 문제를 해결하기 위해 여기에 있으며, 문제를 만들기 위해 있는 것이 아닙니다.

이것이 우리가 무료 지원을 제공하는 이유입니다. 우리의 제품을 사용하는 모든 사람, 구매했든 평가판을 사용하든, 우리의 전적인 관심과 존경을 받을 자격이 있습니다.

Aspose.PDF Java for Jython 관련 문제나 제안을 다음 플랫폼을 사용하여 기록할 수 있습니다:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### 확장 및 기여

Aspose.PDF Java for Jython은 오픈 소스이며, 그 소스 코드는 아래 나열된 주요 소셜 코딩 웹사이트에서 이용할 수 있습니다.
 개발자들은 소스 코드를 다운로드하고 새로운 기능을 제안하거나 추가하거나 기존 기능을 개선하여 기여하도록 권장됩니다. 이를 통해 다른 사람들도 이점을 얻을 수 있습니다.

### 소스 코드

다음 위치 중 하나에서 최신 소스 코드를 얻을 수 있습니다

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java)