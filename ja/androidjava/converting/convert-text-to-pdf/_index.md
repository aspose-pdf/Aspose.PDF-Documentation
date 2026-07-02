---
title: テキストを PDF に変換
linktitle: テキストを PDF に変換
type: docs
weight: 300
url: /ja/androidjava/convert-text-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java を使用すると、プレーンテキストファイルを PDF に変換したり、事前にフォーマットされたテキストファイルを PDF に変換したりできます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

オンラインで試してください。Aspose.PDF の変換品質を確認し、結果をオンラインでこのリンクで表示できます。 [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

**Aspose.PDF for Android via Java** は、テキストファイルを PDF 形式に変換する機能を提供します。本記事では、Aspose.PDF を使用してテキストファイルを PDF に簡単かつ効率的に変換する方法を示します。

テキストファイルを PDF に変換する必要がある場合、まず何らかのリーダーでソースのテキストファイルを読み取ります。テキストファイルの内容を読み取るために StringBuilder を使用しました。Document オブジェクトをインスタンス化し、Pages コレクションに新しいページを追加します。TextFragment の新しいオブジェクトを作成し、コンストラクタに StringBuilder オブジェクトを渡します。TextFragment オブジェクトを使用して Paragraphs コレクションに新しい段落を追加し、Document クラスの Save メソッドで生成された PDF ファイルを保存します。

## プレーンテキストファイルを PDF に変換する

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

## 事前にフォーマットされたテキストファイルをPDFに変換

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



