---
title: Aspose.PDF 자이썬용 자바
linktitle: Aspose.PDF 자이썬용 자바
type: docs
weight: 60
url: /java/aspose-pdf-java-for-jython/
description: Java용 Aspose.PDF의 강력한 기능을 Jython과 결합하세요. Python 기반 Java 환경에서 PDF 파일을 손쉽게 조작할 수 있습니다.
lastmod: "2026-06-09"
---
## 
소개


### 
자이썬이란 무엇인가?



Jython은 표현력과 명확성을 결합한 Python의 Java 구현입니다. Jython은 상업적, 비상업적 용도로 모두 무료로 사용할 수 있으며 소스 코드와 함께 배포됩니다. Jython은 Java를 보완하며 특히 다음 작업에 적합합니다.


- 
**임베디드 스크립팅** - Java 프로그래머는 Jython 라이브러리를 시스템에 추가하여 최종 사용자가 애플리케이션에 기능을 추가하는 간단하거나 복잡한 스크립트를 작성할 수 있습니다.

- 
**대화형 실험** - Jython은 Java 패키지 또는 실행 중인 Java 애플리케이션과 상호 작용하는 데 사용할 수 있는 대화형 인터프리터를 제공합니다. 이를 통해 프로그래머는 Jython을 사용하여 모든 Java 시스템을 실험하고 디버그할 수 있습니다.

- 
**신속한 애플리케이션 개발** - Python 프로그램은 일반적으로 동등한 Java 프로그램보다 2~10배 더 짧습니다. 이는 프로그래머 생산성 향상으로 직접적으로 이어집니다. Python과 Java 간의 원활한 상호 작용을 통해 개발자는 개발 과정과 제품 출시 과정에서 두 언어를 자유롭게 혼합할 수 있습니다.


### 
Java용 Aspose.PDF



Aspose.PDF for Java는 Java 응용 프로그램이 Adobe Acrobat을 사용하지 않고도 PDF 문서를 읽고, 쓰고, 조작할 수 있게 해주는 PDF 문서 생성 구성 요소입니다.



Aspose.PDF for Java는 PDF 압축 옵션, 테이블 생성 및 조작, 그래프 지원, 이미지 기능, 광범위한 하이퍼링크 기능, 확장된 보안 제어 및 사용자 정의 글꼴 처리 등 믿을 수 없을 정도로 풍부한 기능을 제공하는 저렴한 가격의 구성 요소입니다.



Aspose.PDF for Java를 사용하면 제공된 API 및 XML 템플릿을 통해 직접 PDF 파일을 만들 수 있습니다. Aspose.PDF for Java를 사용하면 애플리케이션에 PDF 기능을 즉시 추가할 수 있습니다.


### 
Aspose.PDF 자이썬용 자바



Aspose.PDF Java for Jython은 Jython에서 Aspose.PDF for Java API 사용 예제를 시연/제공하는 프로젝트입니다.


## 
시스템 요구 사항 및 지원 플랫폼


### 
시스템 요구 사항



다음은 Jython용 Aspose.PDF Java를 사용하기 위한 시스템 요구 사항입니다.


- 
Java 1.5 이상이 설치되어 있습니다.

- 
Aspose.PDF 구성 요소를 다운로드했습니다.

- 
자이썬 2.7.0


### 
지원되는 플랫폼



지원되는 플랫폼은 다음과 같습니다.


- 
Aspose.PDF 15.4 이상.

- 
자바 IDE(Eclipse, NetBeans ...)


## 
다운로드 설치 및 사용법


### 
다운로드 중



다음 릴리스의 실행 예제를 GitHub에서 다운로드할 수 있습니다.


- 
[Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)



Java 구성 요소용 Aspose.PDF 다운로드:


- 
[Java용 Aspose.PDF](https://downloads.aspose.com/pdf/java)


### 
설치 중


- 
다운로드한 Aspose.PDF for Java jar 파일을 "lib" 디렉터리에 넣습니다.

- 
"your-lib"를 _*init*_.py 파일에서 다운로드한 jar 파일 이름으로 바꾸세요.


### 
사용



다음 예제 코드를 사용하여 PDF를 문서 문서로 변환할 수 있습니다.


```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'

        # Open the target document
        pdf = Document(dataDir + 'input1.pdf')

        # Save the concatenated output file (the target document)
        pdf.save(dataDir + "output.doc")

        print "Document has been converted successfully"

if __name__ == '__main__':

    PdfToDoc()
```

## 
지원, 확장 및 기여


### 
지원



Aspose의 초창기부터 우리는 고객에게 좋은 제품을 제공하는 것만으로는 충분하지 않다는 것을 알고 있었습니다. 우리는 또한 좋은 서비스를 제공해야 했습니다. 우리는 개발자이며 기술적인 문제나 소프트웨어의 문제로 인해 필요한 작업을 수행할 수 없을 때 얼마나 실망스러운지 이해합니다. 우리는 문제를 만들기 위해 온 것이 아니라 문제를 해결하기 위해 왔습니다.



이것이 우리가 무료 지원을 제공하는 이유입니다. 우리 제품을 사용하는 사람은 제품을 구입했거나 평가판을 사용하고 있는지 여부에 관계없이 우리의 모든 관심과 존경을 받을 자격이 있습니다.



다음 플랫폼 중 하나를 사용하여 Jython용 Aspose.PDF Java와 관련된 문제나 제안 사항을 기록할 수 있습니다.


- 
[Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)


### 
확장 및 기여



Aspose.PDF Jython용 Java는 오픈 소스이며 해당 소스 코드는 아래 나열된 주요 소셜 코딩 웹 사이트에서 사용할 수 있습니다. 개발자는 소스 코드를 다운로드하고 새로운 기능을 제안 또는 추가하거나 기존 기능을 개선하여 기여하여 다른 사람들도 혜택을 누릴 수 있도록 권장됩니다.


### 
소스 코드



다음 위치 중 하나에서 최신 소스 코드를 얻을 수 있습니다.


- 
[Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java)
