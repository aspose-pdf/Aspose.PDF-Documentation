---
title: Converter Texto para PDF
linktitle: Converter Texto para PDF
type: docs
weight: 300
url: /pt/androidjava/convert-text-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java permite que você converta um arquivo de texto simples para PDF ou converta um arquivo de texto pré-formatado para PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

Experimente online. Você pode verificar a qualidade da conversão Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

**Aspose.PDF for Android via Java** fornece a capacidade de converter arquivos de Texto para o formato PDF. Neste artigo, demonstramos como de forma fácil e eficiente podemos converter um arquivo de texto para PDF usando Aspose.PDF.

Quando você precisar converter um arquivo de Texto para PDF, primeiro leia o arquivo de texto de origem em algum leitor. Nós utilizamos StringBuilder para ler o conteúdo do arquivo de Texto. Instancie o objeto Document e adicione uma nova página na coleção Pages. Crie um novo objeto TextFragment e passe o objeto StringBuilder para o seu construtor. Adicione um novo parágrafo na coleção Paragraphs usando o objeto TextFragment e salve o arquivo PDF resultante usando o método Save da classe Document.

## Converter arquivo de texto simples para PDF

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

## Converter arquivo de texto pré-formatado para PDF

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



