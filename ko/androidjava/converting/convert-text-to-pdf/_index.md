---
title: 텍스트를 PDF로 변환
linktitle: 텍스트를 PDF로 변환
type: docs
weight: 300
url: /ko/androidjava/convert-text-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java는 일반 텍스트 파일을 PDF로 변환하거나 사전 서식이 지정된 텍스트 파일을 PDF로 변환할 수 있도록 합니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

온라인으로 시도해 보세요. Aspose.PDF 변환 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다. [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

**Aspose.PDF for Android via Java**는 Text 파일을 PDF 형식으로 변환하는 기능을 제공합니다. 이 문서에서는 Aspose.PDF를 사용하여 텍스트 파일을 PDF로 얼마나 쉽고 효율적으로 변환할 수 있는지 보여드립니다.

Text 파일을 PDF로 변환해야 할 때는 먼저 소스 텍스트 파일을 리더로 읽습니다. 우리는 StringBuilder를 사용하여 Text 파일 내용을 읽었습니다. Document 객체를 인스턴스화하고 Pages 컬렉션에 새 페이지를 추가합니다. TextFragment 객체를 생성하고 그 생성자에 StringBuilder 객체를 전달합니다. TextFragment 객체를 사용하여 Paragraphs 컬렉션에 새 단락을 추가하고, Document 클래스의 Save 메서드를 이용해 결과 PDF 파일을 저장합니다.

## 일반 텍스트 파일을 PDF로 변환

```java
public void convertTXTtoPDF_Simple () {
        // Initialize document object

        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        File txtDocumentFileName=new File(fileStorage, "Conversion/rfc822.txt");

        // Instantiate a Document object by calling its empty constructor
        document=new Document();

        // Add a new page in Pages collection of Document
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


        // Create an instance of TextFragment and pass the text from reader object to its
        // constructor as argument
        TextFragment text=new TextFragment(stringBuilder.toString());

        // Add a new text paragraph in paragraphs collection and pass the TextFragment
        // object
        page.getParagraphs().add(text);

        // Save resultant PDF file
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## 사전 형식화된 텍스트 파일을 PDF로 변환

```java
    public void convertPreFormattedTextToPdf () {

        File txtDocumentFile=new File(fileStorage, "Conversion/rfc822.txt");
        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        Path txtDocumentFileName=Paths.get(txtDocumentFile.toString());

        // Read the text file as array of string
        List<String> lines;
        try {
            lines=Files.readAllLines(txtDocumentFileName, ENCODING);
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate a Document object by calling its empty constructor
        document=new Document();

        // Add a new page in Pages collection of Document
        Page page=document.getPages().add();
        int count=4;

        Font font=FontRepository.findFont("Droid Sans Mono");
        // Set left and right margins for better presentation
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(font);
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // check if line contains "form feed" character
            // see https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page=document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(font);
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Create an instance of TextFragment and
                // pass the line to its
                // constructor as argument
                TextFragment text=new TextFragment(line);

                // Add a new text paragraph in paragraphs collection and pass the TextFragment
                // object
                page.getParagraphs().add(text);
            }
        }
        // Save resultant PDF file
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```



