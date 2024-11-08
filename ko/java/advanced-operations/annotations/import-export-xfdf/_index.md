---
title: 주석을 XFDF 형식으로 가져오기 및 내보내기
linktitle: 주석을 XFDF 형식으로 가져오기 및 내보내기
type: docs
weight: 40
url: /ko/java/import-export-xfdf/
description: Aspose.PDF for Java 라이브러리를 사용하여 XFDF 형식으로 주석을 가져오고 내보낼 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF는 XML Forms Data Format의 약자입니다. 이것은 XML 기반 파일 형식입니다. 이 파일 형식은 PDF 양식에 포함된 양식 데이터 또는 주석을 나타내는 데 사용됩니다. XFDF는 여러 가지 목적에 사용될 수 있지만, 우리의 경우에는 양식 데이터 또는 주석을 다른 컴퓨터나 서버 등에 보내거나 받는 데 사용할 수 있으며, 양식 데이터 또는 주석을 보관하는 데 사용할 수 있습니다. 이 문서에서는 Aspose.Pdf.Facades가 이 개념을 어떻게 고려했는지, 그리고 주석 데이터를 XFDF 파일로 가져오고 내보낼 수 있는 방법을 살펴보겠습니다.

{{% /alert %}}

**Aspose.PDF for Java**는 PDF 문서를 편집할 때 기능이 풍부한 구성 요소입니다.
 우리가 알다시피 XFDF는 PDF 양식 조작의 중요한 측면이며, Aspose.PDF for Java의 Aspose.Pdf.Facades 네임스페이스는 이를 매우 잘 고려하여 주석 데이터를 XFDF 파일로 가져오고 내보내는 메서드를 제공하고 있습니다.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 클래스는 XFDF 파일로 주석을 가져오고 내보내기 위한 두 가지 메서드를 포함하고 있습니다. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 메소드는 PDF 문서에서 XFDF 파일로 주석을 내보내는 기능을 제공합니다. 반면 [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 메소드는 기존 XFDF 파일에서 주석을 가져올 수 있게 합니다. 주석을 가져오거나 내보내기 위해서는 주석 유형을 지정해야 합니다. 이러한 유형은 열거형 형태로 지정할 수 있으며, 그런 다음 이 열거형을 인수로 전달하여 이러한 메소드 중 하나를 호출합니다. 이렇게 하면 지정된 유형의 주석만 XFDF 파일로 가져오거나 내보낼 수 있습니다.

다음 코드 스니펫은 주석을 XFDF 파일로 내보내는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;
import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleAnnotationImportExport {
    // 문서 디렉토리 경로.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    /*
     * XFDF 파일에서 주석 가져오기 XML Forms Data Format (XFDF) 파일
     * Adobe Acrobat, PDF 작성 응용 프로그램에 의해 생성됨; 페이지 양식 요소 및 값의 설명을 저장하며,
     * 텍스트 필드의 이름 및 값과 같은 정보를 포함함; PDF 문서로 가져올 수 있는 양식 데이터를 저장하는 데 사용됨.
     * PdfAnnotationEditor 클래스의 ImportAnnotationsFromXfdf 메소드를 사용하여
     * XFDF 파일에서 PDF로 주석 데이터를 가져올 수 있습니다.
     */

    public static void ExportAnnotationXFDF() throws IOException {
        // PdfAnnotationEditor 객체 생성
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

        // 주석 편집기에 PDF 문서 바인딩
        AnnotationEditor.bindPdf(_dataDir + "AnnotationDemo1.pdf");

        // 주석 내보내기
        FileOutputStream fileStream = new FileOutputStream(_dataDir + "exportannotations.xfdf");
        int[] annotType = { AnnotationType.Line, AnnotationType.Square };
        AnnotationEditor.exportAnnotationsXfdf(fileStream, 1, 1, annotType);
        fileStream.flush();
        fileStream.close();
    }
```

다음 코드 스니펫은 XFDF 파일로 주석을 가져오는 방법을 설명합니다:

```java
public static void ImportAnnotationXFDF()
{
    // PdfAnnotationEditor 객체 생성
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // 새 PDF 문서 생성
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // 주석 가져오기
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // 출력 PDF 저장
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## 주석을 한 번에 내보내고 가져오는 또 다른 방법

아래 코드에서 ImportAnnotations 메서드는 다른 PDF 문서에서 직접 주석을 가져올 수 있습니다.

```java
    public static void ImportAnnotationFromPDF() throws IOException {
        // PdfAnnotationEditor 객체 생성
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
        // 새 PDF 문서 생성
        Document document = new Document();

        document.getPages().add();
        AnnotationEditor.bindPdf(document);
        String exportFileName = _dataDir + "exportannotations.xfdf";
        java.io.File f = new java.io.File(exportFileName);
        if (!f.exists()) {
            ExportAnnotationXFDF();
        }

        // 주석 편집기는 여러 PDF 문서에서 주석을 가져올 수 있지만,
        // 이 예제에서는 하나만 사용합니다.
        String[] fileNames = { _dataDir + "AnnotationDemo1.pdf" };
        AnnotationEditor.importAnnotations(fileNames);

        // 출력 PDF 저장
        document.save(_dataDir + "AnnotationDemo3.pdf");
    }
}
```