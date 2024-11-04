---
title: 고급 기능
linktitle: 고급 기능
type: docs
weight: 120
url: /java/advanced-features/
description: 이 섹션에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 LaTeX 태그를 사용하는 방법을 보여줍니다.
lastmod: "2022-01-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Latex 태그 지원

이 도구는 전반적으로 과학 논문 작성, 책 쓰기 및 기타 다양한 출판 형태를 위해 사용됩니다. 아름답게 디자인된 문서를 만들 뿐만 아니라 수식, 표, 참조 및 참고 문헌과 같은 인쇄 세트의 복잡한 요소들을 매우 빠르게 구현할 수 있으며, 모든 섹션에 일관된 마크업을 제공합니다.

Latex 태그를 사용한 코드 스니펫에서 수학 연습의 예제를 확인해 봅시다.

Aspose.PDF for Java 19.9 버전부터 \begin \end \qedhere Latex 태그에 대한 지원을 제공합니다. 이는 LaTeX 텍스트를 문서 환경에 포함시켜야 하며, 다음 코드 샘플에서 보여줍니다.

```java
String dataDir = Utils.getSharedDataDir(UseLatexScript3.class) + "Text/";





String s =
              "\\usepackage{amsmath,amsthm}" +
              "\\begin{document}" +
              "\\begin{proof} 증명은 다음과 같습니다: " +
              "\\begin{align}" +
              "(x+y)^3&=(x+y)(x+y)^2" +
              "(x+y)(x^2+2xy+y^2)\\\\" +
              "&=x^3+3x^2y+3xy^3+x^3.\\qedhere" +
              "\\end{align}" +
              "\\end{proof}" +
              "\\end{document}";

Document doc = new Document();
Page page = doc.getPages().add();

LatexFragment latex = new LatexFragment(s);

page.getParagraphs().add(latex);
      
doc.save(dataDir + "Script_out.pdf");
```