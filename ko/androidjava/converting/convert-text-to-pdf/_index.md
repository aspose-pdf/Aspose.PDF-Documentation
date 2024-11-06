---
title: 텍스트를 PDF로 변환
linktitle: 텍스트를 PDF로 변환
type: docs
weight: 300
url: ko/androidjava/convert-text-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Java는 일반 텍스트 파일을 PDF로 변환하거나 사전 포맷된 텍스트 파일을 PDF로 변환할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

온라인으로 시도해 보세요. 이 링크에서 Aspose.PDF 변환의 품질을 확인하고 결과를 온라인으로 볼 수 있습니다 [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

**Aspose.PDF for Android via Java**는 텍스트 파일을 PDF 형식으로 변환할 수 있는 기능을 제공합니다. 이 문서에서는 Aspose.PDF를 사용하여 텍스트 파일을 PDF로 얼마나 쉽게 그리고 효율적으로 변환할 수 있는지 보여줍니다.

텍스트 파일을 PDF로 변환해야 할 때, 먼저 소스 텍스트 파일을 일부 리더에서 읽으십시오.
 우리는 StringBuilder를 사용하여 텍스트 파일 내용을 읽었습니다. Document 객체를 인스턴스화하고 Pages 컬렉션에 새 페이지를 추가합니다. TextFragment의 새 객체를 생성하고 StringBuilder 객체를 생성자에 전달합니다. TextFragment 객체를 사용하여 Paragraphs 컬렉션에 새 단락을 추가하고 Document 클래스의 Save 메서드를 사용하여 결과 PDF 파일을 저장합니다.

## 일반 텍스트 파일을 PDF로 변환

```java
public void convertTXTtoPDF_Simple () {
        // 문서 객체 초기화

        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        File txtDocumentFileName=new File(fileStorage, "Conversion/rfc822.txt");

        // 비어 있는 생성자를 호출하여 Document 객체를 인스턴스화합니다.
        document=new Document();

        // Document의 Pages 컬렉션에 새 페이지를 추가합니다.
        Page page=document.getPages().add();

        String string;
        StringBuilder stringBuilder=new StringBuilder();
        InputStream is;
        try {
            is=new FileInputStream(txtDocumentFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        BufferedReader reader=new BufferedReader(new InputStreamReader(is));
        while (true) {
            try {
                if ((string=reader.readLine()) == null) break;
            } catch (IOException e) {
                resultMessage.setText(e.getMessage());
                return;
            }
            stringBuilder.append(string).append("\n");
        }
        try {
            is.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // TextFragment의 인스턴스를 생성하고 reader 객체의 텍스트를 인수로
        // 생성자에 전달합니다.
        TextFragment text=new TextFragment(stringBuilder.toString());

        // 단락 컬렉션에 새 텍스트 단락을 추가하고 TextFragment
        // 객체를 전달합니다.
        page.getParagraphs().add(text);

        // 결과 PDF 파일 저장
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## 사전 서식이 지정된 텍스트 파일을 PDF로 변환

```java
    public void convertPreFormattedTextToPdf () {

        File txtDocumentFile=new File(fileStorage, "Conversion/rfc822.txt");
        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        Path txtDocumentFileName=Paths.get(txtDocumentFile.toString());

        // 텍스트 파일을 문자열 배열로 읽기
        List<String> lines;
        try {
            lines=Files.readAllLines(txtDocumentFileName, ENCODING);
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 빈 생성자를 호출하여 Document 객체를 인스턴스화
        document=new Document();

        // Document의 Pages 컬렉션에 새 페이지 추가
        Page page=document.getPages().add();
        int count=4;

        Font font=FontRepository.findFont("Droid Sans Mono");
        // 더 나은 표시를 위해 왼쪽 및 오른쪽 여백 설정
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(font);
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // 줄에 "양식 피드" 문자가 포함되어 있는지 확인
            // https://en.wikipedia.org/wiki/Page_break 참조
            if (line.startsWith("\f")) {
                page=document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(font);
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // TextFragment의 인스턴스를 생성하고
                // 줄을 인수로 전달하여
                // 생성자에 전달
                TextFragment text=new TextFragment(line);

                // 단락 컬렉션에 새 텍스트 단락을 추가하고 TextFragment
                // 객체를 전달
                page.getParagraphs().add(text);
            }
        }
        // 결과 PDF 파일 저장
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```