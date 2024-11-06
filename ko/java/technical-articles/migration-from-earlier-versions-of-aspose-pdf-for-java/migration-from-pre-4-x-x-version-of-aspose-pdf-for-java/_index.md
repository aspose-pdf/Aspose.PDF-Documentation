---
title: Aspose.PDF for Java의 4.x.x 이전 버전에서의 마이그레이션
type: docs
weight: 20
url: ko/java/migration-from-pre-4-x-x-version-of-aspose-pdf-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Aspose.PDF for Java의 새로운 자동 포팅 버전이 출시되었으며, 이제 이 단일 제품은 PDF 문서를 처음부터 생성하는 기능뿐만 아니라 기존 PDF 문서를 조작하는 기능도 지원합니다.

{{% /alert %}}

## 제품 바이너리

{{% alert color="primary" %}}

첫 번째 릴리스 버전(v4.0.0)에서는 두 개의 jar 파일, 즉 **aspose.pdf-3.3.0.jdk15.jar**와 **aspose.pdf-new-4.0.0.jar**를 제공합니다.
{{% /alert %}}

- **aspose.pdf-3.3.0.jdk14.jar**

이 jar 파일은 현재 다운로드 모듈에서 [Aspose.PDF for java 3.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry417659.aspx)라는 제목으로 제공되는 제품 버전과 동일합니다. 앞으로 우리는 이 릴리스 버전을 레거시 Aspose.PDF for Java라고 부를 것입니다. 이 첫 번째 릴리스에서, Aspose.PDF for Java의 기존 사용자들은 동일한 릴리스 버전을 받기 때문에 영향을 받지 않을 수 있습니다. 하지만, 조만간 우리는 이 별도의 jar 파일을 제거할 것이며, 레거시 Aspose.PDF for Java (pre 4.x.x)의 모든 클래스와 열거형은 단일 aspose.pdf-new-4.x.x.jar 파일의 com.aspose.pdf.generator 패키지에서 사용할 수 있게 될 것입니다.

- **aspose.pdf-new-4.0.0.jar**  
  이 jar 파일은 Aspose.PDF for .NET을 Java 플랫폼으로 자동 포팅한 실제 새로운 버전입니다.
 이 jar 파일에는 새로운 문서 객체 모델(DOM)이 포함되어 있어 기존 PDF 파일을 생성 및 조작할 수 있으며, 현재 Aspose.PDF.Kit for Java도 포함되어 있습니다. Aspose.PDF.Kit for Java의 모든 클래스와 열거형은 com.aspose.pdf.facades 패키지에 포함되어 있으며, 2013년 3분기에 Aspose.PDF.Kit for Java는 중단될 예정입니다. 따라서 현재 Aspose.PDF.Kit for Java를 사용 중인 고객께서는 새로 자동 포팅된 릴리스로 코드 마이그레이션을 시도해 보시길 권장합니다.

자동 포팅된 Aspose.PDF for Java의 구조에 대한 더 많은 정보를 얻으려면 다음 블로그 게시물을 확인하십시오.